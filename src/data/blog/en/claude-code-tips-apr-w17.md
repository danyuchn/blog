---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T05:00:00Z
title: "Claude Code This Week: Offloading CLAUDE.md, Quota-Saving Tricks, Ghostty Click Fix"
slug: en/claude-code-tips-apr-w17
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-workflow
description: A handful of Claude Code settings and money-saving tricks I picked up this week — how Rules/Memory/Hooks offload CLAUDE.md, fixing cmd+click in Ghostty No Flicker mode, dispatching long-read work to Haiku for quota relief, and the cache difference between pasting images and editing prior messages after 4.7.
---

A few Claude Code settings and tricks I accumulated this week. Nothing is brand new, but all of them are things I learned by running face-first into the wall. Organized by topic.

## Stop stuffing everything into CLAUDE.md

Most people only know the "memo file" (CLAUDE.md) and don't know that Rules, Memory, and Hooks can all share its load. I used to be the guy with a 1000-line CLAUDE.md yelling at Claude for forgetting things.

Then I slowly learned to split it:

- **Rules** (`~/.claude/rules/`): Cross-project technical rules, trap lists, tool routing tables. Use `@path/to/rule.md` to import from CLAUDE.md.
- **Memory** (auto memory): Session-level user preferences, project state, error log. Relevant entries auto-load in new conversations.
- **Hooks** (`settings.json`): Automated behaviors (SessionStart checks, PreToolUse interception, PostToolUse reminders). The model doesn't run these. The harness does.

I recorded a weekend video explaining the division of labor: <https://www.youtube.com/watch?v=kSFty4XwXS8>

## Explanatory mode: for non-engineering learners

A common issue when onboarding students: Claude Code throws around too much jargon, and they can't follow.

Two-step fix:

1. `/config` → `explanatory mode`. It shifts into explanation mode.
2. If that's still not clear, add a rule in CLAUDE.md asking it to explain what it's doing in plain, non-technical language.

Those two together bring Claude's output down to a level a middle schooler can follow.

## The Ghostty click trap: cmd+click breaks in No Flicker mode

The traditional Flicker mode has been rendering poorly in Ghostty lately. It renders the same stretch of history multiple times, so scrolling back shows a jumbled mess. I switched to No Flicker mode (text lines fixed, mouse takes over).

That solved the original problem, and immediately surfaced the next one: Ghostty's original `cmd+click` to open links and file paths was being intercepted by Claude Code. Some paths Claude Code couldn't recognize or open.

I had Claude Code generate link formats one by one for me to test. Conclusion, now in CLAUDE.md:

> File paths must use absolute `file://` URLs (e.g., `file:///Users/danyuchn/path/file.md`). The `file://` prefix is required for clickability. Exceptions: inside code blocks, command examples, and function parameters. Keep their original format.

Side note: why not just disable the mouse takeover? Because it's worse. Without mouse takeover, trackpad scrolling is completely uncontrollable in history. It gets locked into the input field.

## Quota savings: dispatch long reads to Haiku

This week's trick: for long-document reading, don't let the main agent read it directly. High-tier models burn tokens on long inputs. Instead:

> Dispatch several Haiku agents to read segments of this document. Hand them the file directly. Don't extract text yourself (saves quota). Then synthesize their summaries.

Splitting into segments avoids attention dilution, and using Haiku saves cost. Explicitly tell it to "hand over the file directly" so the higher-tier main agent doesn't touch the long text and burn tokens.

## After 4.7: pasting images vs editing prior messages, cache behavior

A new lesson this week: the official Claude Code docs leave this unclear.

**Pasting an image in a new message does NOT invalidate the cache. Editing a prior message DOES.**

I pulled the actual cache fields to prove this. So if you want to attach a reference image, keep pasting new messages. Don't go back and edit an old one.

On a side note: when you're wrong, admit it. Don't double down. Too many people in Taiwan love to double down; it looks bad, and honest apology + responsible correction is something everyone still needs to learn. The rule applies to humans and models equally.

## In practice: bypass + hooks

People sometimes ask me how to set permission mode so it doesn't keep popping dialogs. In practice I use `bypass` + hooks. Bypass kills the false-positive friction, hooks intercept at the genuinely dangerous points (file deletion, remote push, outbound communication).

## Remotion video production workflow

I've been getting smooth at making Remotion videos in Claude Code. Rough workflow:

1. Research the topic, check official docs and community best practices
2. Design the narration script, mark where screen recordings are needed
3. Record narration, strip filler words in Jianying
4. Send the subtitle and audio back to Claude Code, ask it to start designing animations
5. Meanwhile, I record the screen demos
6. Do light post-production in Jianying
7. By now the animations are roughly done. Send the video back to Claude Code for embedding
8. Check whether animations stay in sync, any dropped beats. If so, direct corrections and ask it to screenshot-verify itself
9. Output final video and thumbnail
10. While waiting, have it fix subtitle typos and prepare video title + description
11. Once output lands, upload via YouTube API with scheduled publish

The full pipeline is ~90% deep AI involvement, 10% is Jianying features that don't have API/MCP access, plus my personal preference against AI-synthesized voice.

Plan to open source this as a Skill eventually. Sample video: <https://youtu.be/J1WjxzzSzv8?si=w8jLGhBjh8_0HbYR>

## And an unexpected case: a Xoogler grew my channel

A few days ago I was teaching a student how to use Claude Code and accidentally learned he'd worked at Google for 8 years on YouTube-related products.

I casually said, "Our startup channel's traffic won't grow, it's so frustrating," and he generously shared a few content strategies for growing YouTube channels (is that insider information?).

After class, while I was asking Claude Code to archive the class transcript, I hit that portion of the conversation and asked Claude Code: can you try executing his advice? Then gave it API access to my channel.

24 hours later, traffic exploded. Subscribers doubled in a day.

So this time I called him my teacher. Xooglers are genuinely sharp. You can feel it in conversation. No coding background, but whether it's planning logic or directing AI execution, he picks things up instantly. We did four hours of work in one.

## Rate limit reality check

One last rant: you know that feeling when at 9 AM your 5-hour quota is at 55%, and 15 minutes later you hit the limit and need a nap to reset?

```
You've hit your rate limit.
- Reset Friday 07:00 AM
```

That's daily life after Opus 4.7. If you haven't read [my Opus 4.7 one-week recap](/posts/en/opus-47-week-review) from this week, pair it with this one.

Official changelog: <https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>
