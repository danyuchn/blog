---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "Claude Code this week: 1M context as a management problem, quota anxiety goes collective, SpaceX takes Cursor"
slug: en/claude-code-tips-apr-w18
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-trends
  - ai-workflow
description: "Observations from 4/23–4/29: the right mental model for 1M context, Claude quota anxiety as a subscription design phenomenon, SpaceX beating Microsoft to Cursor for $60B, Claude 4.7 identifying a journalist from 125 words, and what happens when you let Claude Code DJ."
---

## 1M context is a management problem, not a capacity problem

A well-made visual breakdown of Claude Code's session management logic circulated this week. My own understanding aligns with what it laid out.

The key mental shift: when context grew from 200k to 1M, the instinct was "great, I can put more in." But larger context means higher management overhead — attention gets diluted, old information interferes with new tasks, model performance drifts downward. That's context rot.

Five operations for five situations:

- **Continue**: same task, keep full context
- **/rewind**: took a wrong turn, go back to the fork
- **/clear**: new task, clean slate
- **/compact**: context getting bloated, summarize history and preserve continuity
- **Subagents**: high-noise subtask, let a sub-agent handle it, only bring back the conclusion

The easiest trap: waiting until context is maxed out and most chaotic before reaching for compact. That's also when summary is least reliable and important context is most likely to get dropped. Better habit: compact at the end of small tasks, not when things are already overwhelming.

## The natural history of quota anxiety

Threads this week was full of a psychology I recognized immediately.

Screenshots showing Claude Max weekly limits at 92%, ten hours until reset. Friends in group chats saying: "My reset is tomorrow at 7am." "I can't sleep until I burn through it." "I'm dreaming about wasting tokens."

Then on 4/28, someone posted: "Whenever I'm approaching reset day with 20% left, I can't eat, can't sleep, just trying to burn through every last token."

This isn't a personal quirk. It's a collective anxiety designed into the product. Monthly subscription plus usage caps naturally creates an "I need to use it all or I'm losing money" feeling — same mechanism as a gym membership. The difference is a gym membership makes you feel guilty about your body. Claude makes you feel guilty about your intellectual output.

Practical fix: don't track the reset date at all. Actually productive Claude sessions don't need "token sprints."

## SpaceX takes Cursor for $60B, Microsoft doesn't bid

Biggest industry news of the week: SpaceX secured the right to acquire Cursor at $60B. CNBC reported Microsoft had evaluated the acquisition but ultimately didn't make an offer.

Cursor is the most mature AI coding tool outside of Claude Code itself, with a large user base. Valuation was under $10B less than a year ago. Half a year later: $60B, and Musk moved faster than Microsoft.

The downstream effect I keep thinking about: training data strategy. Cursor processes massive volumes of real developer coding sessions daily — that's extremely high-quality LLM training material. Musk has been looking for data. This is one move that solves two problems.

## Claude 4.7 identified a journalist from 125 words

This one stopped me.

Author Kelsey Piper shared 125 words of an unpublished political column with Claude 4.7, and Claude named her. She switched to the API, used a friend's computer, tried articles with different styles — Claude identified her every time. ChatGPT and Gemini got it wrong.

Model-level recognition of writing fingerprints has outpaced most people's intuitions. And this was 125 words.

Writing has a property that's hard to eliminate: stylistic habits are systematic, not random. Word choice tendencies, sentence rhythm, how you structure an argument — all of it travels with you regardless of topic. Strong enough models can now read authorship from a single paragraph.

There's a privacy dimension here. There's also something else: if you've been consistently feeding an AI your own thinking, its model of you is probably more detailed than you realize.

## Side project: using Claude Code to make music

On 4/25, I tried something that turned out to be more fun than expected: making Deep House music with Claude Code + Strudel REPL.

Strudel is a live coding music environment that runs in the browser, using JavaScript-style syntax to describe musical structure. I had Claude Code write the Strudel code, and built a small MCP server that lets Claude detect which section is currently playing (groove / breakdown / drop / peak) and switch between sections at the right moments.

End result: I became a one-person DJ directing AI from my apartment. Opus 4.7 running at 1M context handled the live coding cycle steadily.

Music and code share something: both manage structure on a timeline. Claude's grasp of that structure was better than I expected. Not that it has musical taste — more that it clearly understood what "return to the main melody after 8 bars" actually means in terms of the code it needs to write.

## Tool of the week: neat-freak

Someone built a skill called [neat-freak](https://github.com/KKKKhazix/khazix-skills) whose description opens with: "Every time I finish a task and want to close the window, if I don't run /neat first, I feel physically uncomfortable."

What it does: after each task, run `/neat` to auto-sync `CLAUDE.md` / `AGENTS.md`, `docs/`, and agent memory, then output a change summary. The problem it solves: code goes through seven or eight iterations but documentation is still the original version, memory still references SQLite even though you switched to PostgreSQL months ago.

This tool turns "knowledge base sync" from a quarterly deep-clean into a per-task habit. My preference would be an automatic trigger at session end rather than manual invocation — but the concept is right. Documentation drift is a slow-accumulation problem, not a sudden-collapse problem. It needs frequency, not force.
