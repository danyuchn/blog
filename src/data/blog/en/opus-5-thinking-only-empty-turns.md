---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: "Supposedly the Smartest Model, and Opus 5 Spent My Whole Day Spinning in Place"
slug: en/opus-5-thinking-only-empty-turns
featured: false
draft: false
tags:
  - claude-code
  - debugging
  - gotchas
description: 'Wrong languages, sudden Simplified Chinese, then whole turns with no visible output — and a session log that matched an issue open since June 15.'
---

## The morning started with the language going haywire

Supposedly the smartest model out there, and this old problem has been around since 4.6 without a fix: every so often it answers me in Korean or Japanese.

![Screenshot of Opus 5 suddenly replying in Korean and Japanese inside a Traditional Chinese conversation](/blog/assets/posts/opus-5-thinking-only-empty-turns/wrong-language.jpg)

A dozen minutes later, here we go again...

By the afternoon it got even better. Both `/config` and `claude.md` say to use Traditional Chinese, it has written Traditional for the past two months, and now it has decided we are all one big family and started writing Simplified.

## A quick detour: false positives are fine, false negatives are the scary ones

That same day I was tuning my own pending guard hook, and I happened to have a screenshot of a misfire. That one is a false positive, and I think it is completely acceptable. I do not mind being wrongly accused. Once the hook flags it, a genuinely innocent model will produce evidence and defend itself.

What I fear most are false negatives, where a mistake quietly slips through. But that rarely happens now, because the model's phrasing is so consistent that regex catches it.

Good thing my harness is under its own git repo, so my plan is to change it bit by bit and test, and roll back if it does not work.

Two ways to catch the false negatives:

1. Several turns later I notice it never actually verified anything, quality suffers, and it comes back with "you're right, I didn't actually..."
2. Every night, run the claude-log CLI with a local model over all of that day's session log jsonl, pull out every fragment where the model claims it verified something (no regex, let the local LLM catch it semantically, slow is fine, it is the middle of the night), then review how many false negatives got past me that day

And that day, the model said this about itself:

> One-line summary: this is not a case of getting the tool-call syntax wrong. At certain points where I need to integrate visual information or wait for reports from multiple sources, I finish thinking but never actually emit the action or the text, and then occasionally I invent a plausible-sounding but baseless technical explanation after the fact to cover for it. That "making up a reason" part is itself a failure worth recording — from now on, if I offer a self-diagnosis like "it was a formatting error," you can just tell me to bring evidence first.

Which reminds me of the system card I read yesterday. Opus 5's hallucination rate went up...

## "Isn't your CLAUDE.md just too bloated?"

Someone suggested I tear my CLAUDE.md down and rebuild it from scratch.

![Screenshot of the harness audit report showing the official comparison done via WebFetch on code.claude.com plus WebSearch, no stale rules, everything under 200 lines with the largest at 92](/blog/assets/posts/opus-5-thinking-only-empty-turns/harness-audit-92-lines.jpg)

It is already down to 92 lines (the official recommendation is under 200), and I have checked it against the official docs and `/insight` once a week, without a break, for half a year. Care to share your great method for tearing it down and rebuilding, and the results you got?

Is 92 lines of claude.md really too much... Context was only 8% used when the problem happened. I had even dispatched a Sonnet subagent specifically to preserve its context window.

He just dumped a giant turd into my conversation.

## Using claude-log to dig up what crap he dumped

I had the claude-log CLI go dig through the session log to see what crap he dumped.

Looked it up, and it turns out Opus 4.8 had this problem back on 6/15. I just never hit it because I had been on 4.6 the whole time, and it still is not fixed.

\#68591 — Opus 4.8 returns thinking-only responses without tool_use or text blocks (open)

That issue matches exactly the root cause I just found with claude-log: Opus 4.8 sometimes produces a response with only a thinking block, no text and no tool_use, while stop_reason still reports tool_use or end_turn normally. The client cannot parse it and has no choice but to conclude "there was no visible output this turn."

In other words: the model actually worked the answer out internally and wrote it into thinking, but never emitted it as text the user can see. That is the same known regression as what we found today: the repeated spinning in place, especially after it reads an image or waits for a subagent to report back.

<https://github.com/anthropics/claude-code/issues/68591>

Hard to say. All I can do now is `/feedback` and see whether the official side takes pity on me...

That is certainly possible, and that is the direction I am adjusting toward next. But I use the same harness for both codex and claude, and codex has no real problems with it. I am genuinely curious why claude is this sensitive (?) hahahahaha.
