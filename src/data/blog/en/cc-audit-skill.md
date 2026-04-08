---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T15:00:00Z
title: "cc-audit: A Skill That Forces You to Save Claude Code Quota"
slug: en/cc-audit-skill
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - token-optimization
description: I turned my viral list of quota-saving tips into a skill. Hand the GitHub link to Claude Code to install, and it'll audit your settings, recent sessions, rules bloat, and context usage, then hand back an actionable fix list.
---

Claude has been messing with quotas lately and everyone's complaining. Complaining aside, Claude is still what I use to work. A while back I posted a long list of quota-saving tips on Threads, which ended up getting a thousand-plus likes. Someone suggested it should be a skill, so I built one.

Here it is: <https://github.com/danyuchn/cc-audit>

Hand the link to Claude Code and ask it to install.

## What It Does

cc-audit is a health-check skill. When triggered, it runs four steps and hands back a structured report and an actionable fix list.

### Step 1: Static Config Audit

- Is your default model set to Sonnet? Sonnet is much cheaper than Opus for most tasks and usually enough.
- What hooks are configured? Any runaway post-hooks silently eating tokens?
- MCP server list—each one is a fixed startup overhead.
- Line counts per rules file—catches rules that have bloated past 200 lines and need splitting.
- Skills list.

### Step 2: JSONL Session Analysis (last 5 sessions)

This is the meat of it. It pulls your five most recent JSONL files and computes, per session:

- **Context usage**: `(input_tokens + cache_creation + cache_read) / 200000`
- **Cache type**: distinguishes Pro's 5-minute cache (`ephemeral_5m_input_tokens`) from Team/Enterprise's 1-hour cache (`ephemeral_1h_input_tokens`)
- **Compact triggers**: detects `/compact` events via `type=system` messages with a `summary` key
- **Image-triggered cache misses**: spots the pattern "user content has image type + next assistant message has cache_read < 500"

After the run you get a clear view per session: how many tokens it cost, whether auto-compact ran, whether a pasted image nuked the cache, whether context usage was 80% or 30%.

### Step 3: Check Against Official Best Practices

This step WebFetches the latest Anthropic Claude Code docs and compares your current setup against official recommendations. Are the tips I wrote getting outdated? They can't, because it re-fetches every run.

### Step 4: Rules Path-Specificity Check

It checks whether your rules should have a `paths:` condition so they only load when relevant file paths show up. This one saves a lot, and most people don't know about it.

## Why Not Just Use `/stats`?

Claude Code's built-in `/stats` tells you "this session used X tokens," but it doesn't tell you:

1. Why it used that much
2. Which settings are the culprits
3. What to change next

cc-audit's output is an actionable fix list. Each item points to a specific file, specific line, specific change. You don't have to cross-reference docs and guess.

## Build the Habit

My own usage is to run cc-audit every week on Claude Max reset day. Pair this with the workflow I wrote about in [Obsidian + Claude Code](/blog/posts/en/obsidian-claude-code-workflow)—the day your weekly quota is about to reset and you're temporarily a "single-day token millionaire" is exactly when you should be doing this kind of refactor.

I used to do this by hand, cross-checking docs, and it took 30-40 minutes. As a skill, it's fully automated in five minutes and I stop forgetting items.

Hand this link to Claude Code: <https://github.com/danyuchn/cc-audit>

It'll install and verify, then you just type `/cc-audit` to run.
