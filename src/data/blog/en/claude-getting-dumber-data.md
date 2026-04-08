---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T14:00:00Z
title: "Is Claude Getting Dumber? Someone Finally Brought Data"
slug: en/claude-getting-dumber-data
featured: false
draft: false
tags:
  - claude-code
  - ai-trends
  - ai-tools
description: People have been complaining Claude is getting dumber for weeks. Anthropic's response has been "it's a usage problem." Then someone pulled the JSONL and showed it's measurable, not vibes. The Issue got closed anyway.
---

People have been complaining Claude is getting dumber for weeks. Anthropic's standard reply has been "peak-hour limits are tighter" and "it's a usage problem." The April 3rd investigation notice basically told everyone to use Opus less, don't resume idle conversations, and shrink your context window—translation: "you're holding it wrong."

Then this week someone went straight to the JSONL, pulled model behavior metrics across February and March, and showed it's not vibes—it's measurable. The Issue got closed anyway.

GitHub Issue #42796: <https://github.com/anthropics/claude-code/issues/42796>

Here are his numbers.

## Thinking Depth Cut by 73%

| Period | Median thinking | Redact ratio |
|--------|----------------|--------------|
| Baseline (1/30–2/8) | ~2,200 chars | — |
| Late February | ~720 chars (-67%) | — |
| After 3/12 | ~600 chars (-73%) | 99%+ (fully redacted) |

The Redact ratio is the scariest part: 1.5% on 3/5, then 24.7% on 3/7, then 58.4% on 3/8, and 99%+ from 3/10 onward. You can no longer see what the model is thinking.

## Tool Usage Behavior Collapsed

| Metric | Baseline | March+ | Change |
|--------|----------|--------|--------|
| Read:Edit ratio | 6.6 | 2.0 | -70% |
| Edit without reading first | 6.2% | 33.7% | 5x+ |
| Full-file write (rewrite whole file) | 4.9% | 11.1% | 2.3x |
| Reasoning loops (self-contradictions) | 8.2 / 1000 tool calls | 26.6 / 1000 tool calls | 3x |

"Edit without reading first" jumped from 6% to 33%. That explains why Claude has been blindly editing your files—because it literally is. Full-file write doubled too, meaning every small tweak triggers a whole-file rewrite, and token consumption doubles with it.

## User Experience Metrics

| Metric | February | March | Change |
|--------|----------|-------|--------|
| Stop hook violations (bailing early) | 0 | 173 (over 17 days, ~10/day) | — |
| User frustration language ratio | 5.8% | 9.8% | +68% |
| User interruptions / 1000 tool calls | 0.9 | 11 | 12x |

User interruptions went from 0.9 to 11 per thousand tool calls. Your temper didn't get worse—the model got more deserving of being yelled at.

## Cost Exploded 80x

This section is the jaw-dropper:

| Metric | February | March | Change |
|--------|----------|-------|--------|
| User prompts sent | 5,608 | 5,701 | ≈ flat |
| API requests | 1,498 | 119,341 | 80x |
| Output tokens | 0.97M | 62.60M | 64x |
| Estimated cost | $345 | $42,xxx | ~120x |

Users typed the same number of messages, but API requests behind the scenes went up 80x, output tokens 64x, cost ~120x. This isn't "Opus costs more than Sonnet." This is the model redoing, retrying, rewriting, and looping on itself.

## Then the Issue Got Closed

No official response to any of these numbers. Issue closed.

What this person did was simple: he trusted the data. He was right, but nobody wanted to hear it.

The "gap" people keep complaining about isn't mystical. Last week was fine, this week isn't, your usage habits are identical, but the model is blind-editing files, getting stuck in loops, and firing 80x the API calls per message—that's not "peak-hour limiting." That's the model being tampered with.

I do consulting work, and my workflow is deeply coupled to Claude Code. In this situation, the pragmatic move isn't to argue—it's to prepare a Plan B. OpenCode + GLM/Kimi/MiniMax, config and memory fully backed up, ready to switch at any moment. I wrote about the full setup in [Anthropic Trust Crisis and My Backup Plan](/blog/posts/en/anthropic-trust-crisis-backup).

AI companies always get cocky once they have enough users. Don't buy annual subscriptions, don't depend on a single vendor. That's the single most important thing to learn about working with AI in 2026.
