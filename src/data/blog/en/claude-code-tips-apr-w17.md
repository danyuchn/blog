---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T05:00:00Z
title: "Practical Claude Code Setup: Slimming CLAUDE.md, Quota Control, and Automated Workflows"
slug: en/claude-code-tips-apr-w17
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-workflow
description: 'When CLAUDE.md swells past a thousand lines, instructions get dropped, and rate limits hit within minutes, your harness needs an overhaul. A practical guide to splitting Rules, Memory, and Hooks, delegating to Haiku subagents, caching rules, Ghostty click fixes, and an automated video pipeline.'
tldr: 'Tired of Claude Code forgetting long instructions or burning through your quota in 15 minutes? Split your setup into separate rules, memory, and auto-checks, delegate long reading to lightweight models, and attach images in new messages rather than editing old ones. Treating it as a divided system keeps complex workflows running smoothly.'
---

When I first adopted Claude Code as my daily driver, I walked straight into two familiar traps: stuffing every guideline into a single config file until it grew past a thousand lines and the model started forgetting things, and watching my 5-hour quota sit comfortably at 55% at 9:00 AM only to slam into a hard limit fifteen minutes later.

Over months of tuning configuration files, terminal quirks, and token budgets—eventually automating an entire video pipeline that drove real channel growth—the core takeaway was clear: Claude Code handles complex work reliably only when you give it clear boundaries and split up its responsibilities, rather than dumping every wish into a single file.

## Don't Cram Everything into CLAUDE.md: Rules, Memory, and Hooks

Most users only know about `CLAUDE.md`, overlooking how much Rules, Memory, and automated Hooks can take off its plate. I used to let my own `CLAUDE.md` swell past a thousand lines, complaining that Claude was getting clumsy whenever it dropped an instruction.

In reality, forcing technical specs, guidelines, and history into a single file makes the context unwieldy; once it passes a thousand lines, the model naturally misses things. A cleaner architecture separates configuration across three layers:

- **Rules**: Cross-project technical guidelines, gotcha lists, and tool routing tables. Import them from `CLAUDE.md` on demand using `@path/to/rule.md`.
- **Memory**: Session-level user preferences, current project state, and post-mortems of past mistakes. Auto-memory pulls only the relevant entries whenever you start a new conversation.
- **Hooks**: Automated behaviors configured in `settings.json` (such as `SessionStart` checks, `PreToolUse` interception, and `PostToolUse` reminders). Whatever the model might skip, the harness enforces.

When configuring permission modes, people often ask how to stop approval prompts from interrupting every routine action. In practice, pairing bypass mode with hooks works best: bypass mode eliminates nagging false positives, while hooks step in at genuinely risky operations like deleting files, pushing to remotes, or sending external communications.

Over the weekend, I put together a video breaking down how these advanced settings divide the work: <https://www.youtube.com/watch?v=kSFty4XwXS8>

## Reducing Friction: Plain-Language Explanations and Terminal Click Targets

Beyond modular configs, reducing day-to-day friction makes a huge difference when you live inside the tool all day.

When onboarding students without an engineering background, the most frequent roadblock is Claude Code generating dense technical jargon that leaves them lost. Clearing that communication barrier takes two steps:

1. Run `/config` and switch to `explanatory mode`.
2. Add a rule to `CLAUDE.md` instructing the model to explain its current actions in plain, non-technical language.

Combining those two tweaks lowers the comprehension bar enough that even a middle schooler can follow what Claude is doing.

Another friction point shows up right in the terminal. In Ghostty, standard Flicker mode frequently botches scrollback rendering, redrawing the same conversation history multiple times and turning review into a garbled mess. To fix that, I switched to No Flicker mode with fixed text rows and mouse capture enabled.

That solved the rendering glitch, but triggered an immediate side effect: Ghostty's native `cmd+click` shortcut for opening links and file paths was captured by Claude Code, breaking click-to-open detection for certain paths. (Disabling mouse capture made things worse, completely breaking trackpad scrolling through history and locking the viewport onto the prompt input).

To fix the click detection, I had Claude Code generate various path formatting styles and tested them one by one. The only format that consistently triggered clean click targets went straight into my `CLAUDE.md`:

> Always format file locations as absolute `file://` URLs (e.g., `file:///Users/danyuchn/path/file.md`); the `file://` prefix is required for clickable links. Exceptions: code blocks, command examples, and function arguments keep their original format.

## Quota and Cache Economics: Keeping Heavy Models Off Grunt Work

Under heavy daily usage, assigning grunt work to an expensive flagship model will burn through your rate limits in no time.

When plowing through long documents, never feed the entire raw text directly to your primary frontier model. Processing massive contexts on high-end models explodes token consumption and introduces attention dilution. A far more economical approach is chunking the document and delegating it to cheaper Haiku subagents:

> Dispatch several Haiku agents to read this document in chunks. Pass the file directly to them without extracting the text yourself (to conserve quota), then summarize their findings.

The secret to this prompt is explicitly stating "pass the file directly to them," preventing the primary model from touching the raw text and racking up tokens. Splitting the document prevents attention dilution, while Haiku keeps costs negligible.

Alongside smart subagent delegation, understanding prompt caching is essential for managing your quota. Following version 4.7, official documentation on cache invalidation remained vague. After inspecting raw cache telemetry across dozens of runs, I confirmed one critical rule:

**Appending images in a new message does not bust the cache; editing an earlier message does.**

If you need to supply reference screenshots or mockups, simply send them in a fresh follow-up message instead of going back to edit earlier prompts.

## Script to Publish: An Automated Video Pipeline with 90% AI Collaboration

Once your configs, interface, and quota management are dialed in, Claude Code can drive extensive end-to-end production pipelines. Here is my actual workflow for producing programmatic Remotion videos:

1. Research the topic, checking official documentation and community best practices.
2. Draft the voiceover script and mark placeholders for screen recordings.
3. Record the voiceover and auto-remove filler words in CapCut.
4. Feed subtitles and audio back to Claude Code to start designing animations.
5. Record the actual on-screen walkthrough while Claude works.
6. Run basic video cleanups on the screen recording in CapCut.
7. Once the recording is ready, Claude has usually finished the animation code; feed the clip back to let it embed the footage.
8. Review animations for visual bugs or off-beat timing, directing adjustments and having Claude take screenshots to self-verify.
9. Render the final video and thumbnail.
10. While rendering, have Claude correct typos in the subtitle file and draft the YouTube title and description.
11. With the video exported, upload it directly via the YouTube API and schedule the release.

Roughly 90% of this pipeline runs on deep AI collaboration, leaving only about 10% for manual tasks—mostly because parts of CapCut lack API integration, and I personally dislike the feel of synthesized AI voiceovers.

I plan to package and open-source this automated video pipeline as a reusable Skill module later. You can see a sample video produced with this setup here: <https://youtu.be/J1WjxzzSzv8?si=w8jLGhBjh8_0HbYR>

## When Domain Expertise Meets Execution: Leverage for Non-Engineers

This collaboration model stretches far beyond my own video setup; it proved just as powerful during live teaching sessions.

While coaching a student on Claude Code recently, I discovered he had spent eight years running YouTube partnerships at Google. I mentioned offhand that my new channel was struggling to gain traction, and he generously shared several core strategies for driving organic YouTube growth.

After class, while having Claude Code organize and archive our session notes, I came across that exchange and casually prompted it: "Can you try implementing his advice?" and handed over the channel's API credentials.

Within 24 hours, views surged noticeably, and channel subscribers doubled in a single day.

That outcome completely flipped the dynamic. Even without any programming background, his sharp planning instincts and command clarity were immediately obvious. Working with AI came naturally to him—he picked up concepts instantly, easily covering four hours of progress in a single hour.

## A Reality Check on Rate Limits

No matter how smooth your workflow feels, daily production eventually crashes into strict rate limits. Especially on flagship models, you will almost certainly experience this: looking at your 5-hour quota sitting at 55% at 9:00 AM, only to hit a wall fifteen minutes later and wait out the cooldown:

```
You've hit your rate limit.
- Reset Friday 07:00 AM
```

This has been reality ever since Opus 4.7 dropped. For a detailed breakdown of how that played out, check my earlier [quota incident log](/blog/posts/en/claude-code-quota-incident-log), which documented what happened during launch week.

Facing inevitable rate limits, defensive habits come down to three straightforward practices:
First, delegate long-document reading to lightweight models like Haiku for chunked summaries, keeping raw files away from your primary agent;
Second, send images and extra context in new messages so you don't invalidate existing prompt cache;
Third, pair permission bypass with automated hooks to skip repetitive confirmations while safeguarding destructive actions.

Once you set up Claude Code as a system with rules, memory, hooks, and multi-model routing, it stops feeling like a fragile chatbot and turns into a reliable second brain you can lean on every day, even within tight quotas.

## Appendix

A quick reference for the advanced configurations and technical specs mentioned in this post:

- **Rules (`~/.claude/rules/`)**: Imported into `CLAUDE.md` on demand using `@path/to/rule.md`. Ideal for storing cross-project engineering conventions, gotchas, and tool routing tables.
- **Session Memory**: Uses the auto-memory system to track session-level user preferences, project statuses, and post-mortems, automatically pulling relevant entries into fresh sessions.
- **Automated Hooks (`settings.json`)**: Intercepts lifecycle events, including `SessionStart` initial checks, `PreToolUse` command verification, and `PostToolUse` reminders.
- **Terminal Display & Click Targets**: Set Ghostty to No Flicker mode for fixed text rows, and format file paths as absolute URLs with the `file://` protocol to keep paths clickable when mouse capture is active.
- **Official Updates**: For changelogs and detailed release notes across Claude Code versions, see the official CHANGELOG: <https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>

<!--
2026-10-26 拼接順稿：
- 「除了自己用 Claude Code 產影片，這週教課時還碰上一個意料外的應用實例。」— 類型：銜接
（在「Xoogler 幫我長流量」節開頭補上一句銜接，交代從影片製作延伸到教學應用）

2026-11-12 舊文盤點整篇重寫：
將原本零散的設定碎念、踩坑紀錄與實戰案例，重構成「配置拆分、互動介面、額度經濟、實戰工作流」的完整架構，去除離題批判，技術細節收斂至附錄。
-->