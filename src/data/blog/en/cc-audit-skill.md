---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T15:00:00Z
title: "cc-audit: A Skill That Stops Claude Code from Burning Your Tokens"
slug: en/cc-audit-skill
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - token-optimization
description: 'I turned my viral token-saving tips into an automated audit skill for Claude Code. Feed it to Claude Code, and it inspects your settings, recent sessions, rules, and context usage to hand you an actionable checklist of fixes.'
tldr: 'Built-in usage stats show how much Claude Code quota you burned, but not which settings are draining it. Installing the open-source cc-audit skill runs a five-minute check across your default model, your last 5 sessions'' cache hits, and path-specific rules—pointing out the exact file and line to fix.'
---

Anthropic keeps messing with Claude's rate limits lately. People complain, but at the end of the day, we still have to use it. Instead of sweating over an empty token bar every afternoon, a much more practical move is hunting down the configs and habits quietly burning through your quota. A while back, I put together a long thread on token-saving tips that got over a thousand likes, and someone in the comments suggested turning it into a skill.

So I built it, and here it is: <https://github.com/danyuchn/cc-audit>

It's a health-check skill specifically designed for your Claude Code setup. Feed the repo link to Claude Code, let it install it for you, and you can run a diagnostic right away.

## Why Not Just Run /stats?

The first question most people ask is obvious: doesn't the terminal already have `/stats` for checking usage?

The built-in `/stats` command does tell you how many tokens the current session consumed, but it fails to answer three fundamental questions:

1. Why did it use so many?
2. Which specific settings are burning through the quota?
3. Now that you have the numbers, what exact changes should you make next?

`/stats` shows the weight on the scale without diagnosing the cause. cc-audit acts as an automated physical: instead of raw numbers, you get a structured report and an actionable punch list. Every single entry maps directly to a specific file, line number, and recommended edit, saving you from guessing or combing through documentation.

## The Four Checks in cc-audit

Once triggered, cc-audit walks through four steps to take a full inventory of your setup and recent token usage:

**Step 1: Static Config Review**

It starts by inspecting your baseline environment:
- Whether your default model is set to Sonnet (Sonnet is far cheaper than Opus for most daily tasks, and more than capable enough).
- Configured hooks, especially rogue post-hooks that silently eat tokens.
- The MCP server list—each server carries a fixed overhead every time you launch a session.
- Line counts across rules files, flagging any rule file that bloats past 200 lines and needs splitting.
- Currently mounted skills.

**Step 2: JSONL Session Analysis (Last 5 Sessions)**

This is the heart of the audit. It pulls JSONL logs from your last five sessions and runs a deep pass on each one:
- **Context utilization**: Calculated as `(input_tokens + cache_creation + cache_read) / 200000`. If you run a 1M context window session, the denominator switches to `1,000,000`. This gives you an immediate read on whether your context is sitting at 80% or 30%.
- **Cache lifetime and tier**: Extracted from `ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`. As long as you are on a Claude subscription within plan limits, the main thread gets a 1-hour cache; subagents or overage usage drop to a 5-minute cache.
- **Compact count**: Scans for the `summary` keyword in `type=system` messages to see whether `/compact` was triggered during the session.
- **Cache misses after image pastes**: Detects instances where user content has an image type followed by an assistant message with `cache_read < 500`, catching cases where an image broke prompt caching.

Once this step finishes, everything is laid bare: total tokens spent, whether auto-compact kicked in, whether a pasted screenshot wrecked your cache, and whether you were hovering at 30% or 80% context capacity.

**Step 3: Checking Official Best Practices**

A common concern with static audit tools is that rules go stale. Here, cc-audit uses WebFetch to pull Anthropic's latest official Claude Code documentation live and compares the newest recommendations against your config. Because it fetches updates dynamically on each run, the advice never falls out of date.

**Step 4: Path-Specificity Check for Rules**

It checks whether your rules files should use conditional loading with `paths:`. With path filters, specialized rules only load into context when relevant files appear in the workspace, instead of permanently eating tokens in every session. It is one of the biggest token savers available, yet surprisingly few people use it.

## Turn Auditing into a Regular Refactoring Habit

I used to audit everything manually against the docs, which easily took 30 to 40 minutes and left plenty of room to miss things. Packaging it into a skill cut that down to a fully automated five-minute run that covers every item in one shot.

If you want to bake this into your routine, the best time to run it is right before your quota resets. As I mentioned in my [Obsidian + Claude Code workflow](/blog/posts/en/obsidian-claude-code-workflow) piece, quota reset day makes you a temporary "token billionaire." With tokens to spare, that is the prime window to refactor your environment, split bloated rules, and prune unused configs.

Give this link to Claude Code: <https://github.com/danyuchn/cc-audit>

It will install it, verify everything, and then you just type `/cc-audit` to start.

<!-- 2026-11-12 舊文盤點整篇重寫：將文末後記對快取時效與上下文視窗公式的修正整合進步驟內文，把檢查流程改為連貫的四大面向，並以清楚的安裝指引作為全文唯一的收尾。 -->
