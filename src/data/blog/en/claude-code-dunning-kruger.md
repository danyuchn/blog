---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T05:00:00Z
title: "The Claude Code Dunning-Kruger Curve: From Complete Stranger to Total Sync"
slug: en/claude-code-dunning-kruger
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: 'A non-engineer power user''s journey through the Claude Code Dunning-Kruger curve: from day-one confusion and day-three hubris to week-two wall-hitting, before mastering rules, skills, and multi-model collaboration.'
---

I don't have an engineering background, but over the past six months, I've used Claude Code to refactor databases, connect frontends and backends, coordinate multi-agent setups, and deploy production apps completely on my own.

These days, when I work alongside AI, terms like fork, branch, merge, push, fallback, prop, and hook roll off my tongue. But looking back at when I first started, I went through a textbook Dunning-Kruger curve: from wide-eyed curiosity and fleeting arrogance to crashing hard into endless brick walls, before finally discovering how to get the AI into absolute sync with how I work.

This is an outsider's honest breakdown of moving from hitting walls to total sync, along with the collaboration rules that made it happen.

## Riding the Dunning-Kruger Curve: From Peak Hubris to the Valley of Despair

During my first two weeks with Claude Code, my mental state swung wildly:

**Day 1: Bewilderment**
What even is this? A 90s BBS forum?
As a tech outsider, I felt an inexplicable fondness for Claude Code's raw terminal interface, and at first I couldn't figure out why. Then it clicked: I'm from the BBS and PTT generation. Typing in a terminal felt surprisingly nostalgic, like hanging out on old text-only bulletin boards back in the day.

**Day 3: Hubris**
Started getting the hang of it and honestly thought Claude Code and I were unstoppable.

**Week 2: Meltdown**
Absolute nightmare. Once the beginner honeymoon ended, everything broke down. It started forgetting context constantly, spewing out throwaway scratch files and analysis reports, burning through API limits at lightning speed, and looping endlessly on tricky bugs.

## The Week 3 Turning Point: Managing AI Like a New Hire

By week three, the turning point finally arrived. I figured out how to actually work with it.

Instead of getting frustrated or blindly retrying prompts, a single command changed everything:

> "Spin up multiple agents to investigate my current codebase structure, markdown docs, test scripts, and git commit history in parallel. Then: 1. Clean up and consolidate documentation 2. Update outdated content 3. Draft the custom Skills I need 4. Rewrite claude.md 5. Recommend suitable sub-agents and MCP servers."

The payoff was immediate. Token usage dropped by 50%, the endless trial-and-error stopped, and my development speed easily doubled. The AI and I were finally operating in total sync.

When you think about it, it's just like onboarding a new teammate at work: organize the background info, keep docs fresh, provide clear SOPs, and lay out communication norms and tools. The only difference is you can't control a human's mood or quirks, whereas AI is much easier to steer once expectations are clear.

## Understanding the Toolkit: The Executive Assistant Analogy for Skills and MCP

A lot of people mix up Skills and MCP. The easiest mental model is thinking of them like an executive assistant:

- **Skills** are essentially structured prompt engineering, sometimes paired with helper scripts. Think of them as an "expert handbook."
- **MCP**, on the other hand, provides the interface to connect to a specific platform and call external services. Think of it as a "banking app."

Imagine hiring an executive assistant with a stack of handbooks on their desk. When you ask them to handle bookkeeping, they first scan the titles, grab the "Financial Operations Manual," and flip through it to learn your preferences, where receipts are kept, and which apps to use. Then, they open your pre-authenticated banking app (MCP) to pull live account data from each bank.

In practice, a few Skill combinations have worked especially well for me:

- `/ui-ux-pro-max` and `/frontend-design`: Paired with color palettes from HAPPY HUES, this lets me spin up clean prototypes fast.
- Remotion Skill: Generating programmatic videos inside Claude Code, combined with Anthropic's official Frontend Skill to restyle components, produces an aesthetic that surprisingly matches Claude's official marketing pages.

## Put to the Test: Shipping a Massive Overhaul in Under 24 Hours

Once, I used Claude Code to knock out a full day's worth of work: refactoring code, purging redundant functions, restructuring and migrating a backend database, and rewiring schemas across the entire codebase. At one point, I accidentally mixed up staging and production schemas, triggering a minor crisis. But down the stretch, I dispatched four agents in parallel to audit the frontend and backend code, database state, and git commits.

When the dust settled, the entire overhaul had taken less than 24 hours.

Just staring at the field mappings between the old and new schemas made me want to set the database on fire. Coming out the other side, I couldn't help wondering: before AI came along, how on earth did traditional developers pull off projects like this, and how many weeks did it take them?

Beyond writing code, it's also great for technical writing—I can polish documents and drop them straight into Overleaf without a hitch.

## Environment Choices and Multi-Model Workflows

The more I use it, the more convinced I become: **IDEs just tie Claude's hands, while Claude in the CLI is completely unleashed.**

Without the clunky IDE wrappers, calling CLI tools feels noticeably more responsive and flexible. My everyday go-to is pairing the Claude Extension with Claude Code—it just flies.

As for people recommending Google Antigravity, my verdict is dead simple:

1. Open Terminal
2. `brew install --cask claude-code`
3. Set up an account and load credits
4. Delete Antigravity

When facing complex engineering tasks, there's no need to stick rigidly to a single model. Sometimes when Opus gets stuck, handing the exact same problem to Codex nails it on the first try.

Codex runs agonizingly slow, but its debugging chops are legendary. My rule of thumb is straightforward: Claude Code for day-to-day building, and Codex the moment a nasty bug turns into an infinite loop. Slow and steady wins the race—play to each model's strengths.

## Cost Breakdown and Practical Notes

Running `!npx ccusage@latest monthly` inside Claude Code prints your monthly token usage, calculated against standard API pricing.

For flat-rate subscribers, this is pure dopamine. On my $200 subscription, my actual token consumption worked out to $3,225 worth of API credits. On February 1st alone, I had already burned through nearly $200 in equivalent usage.

One quick heads-up on tool updates: ccusage now bundles usage from all detected coding CLIs (Codex, Gemini CLI, etc.) into a single report. If you only want to see your Claude Code metrics, run `npx ccusage@latest claude monthly` instead.

## Appendix

Common parameters and query options for ccusage:

- `daily`: Daily breakdown
- `--since YYYYMMDD --until YYYYMMDD`: Specify a date range
- `--breakdown`: Split by model

<!--
2026-10-26 拼接順稿：
無新增過渡句。
（將混在成本管理小節中的技術文件與術語感觸段落移至「一天完成大型工程」節末，並將 ccusage 後記歸位至成本管理小節內）

2026-11-12 舊文盤點整篇重寫：
以達克曲線為統一敘事主軸，重整心路歷程、秘書手冊（Skills/MCP）心智模型與多模型/成本工具，將零散後記與參數收束至文末與附錄。
-->
