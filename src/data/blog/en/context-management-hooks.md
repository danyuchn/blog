---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-22T04:00:00Z
title: "The Real Next Level in Claude Code: Context Management and Hooks"
slug: en/context-management-hooks
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: From Claude.md to Hooks — sharing the context management upgrade after heavy daily Claude Code usage. When rules pile up and compliance drops, Hooks become the perfect gatekeeper.
---

Most people switching from chat windows to Claude Code hit a wall early on because they don't understand Claude.md. The next wall is understanding it but not knowing how to manage context.

I've been trying to explain it simply: AI models like Claude are stateless. Every time you open a new window, it's a genius new hire who just walked in the door. The difference is that a human new hire takes weeks to train, but an AI new hire just needs the right documentation and becomes a veteran in seconds. Claude.md is that documentation. Made a mistake you don't want repeated? Write it in there.

Someone asked me the real difference between Cowork and Code. My answer: you can move everything to Code. Code has permission to read your Chat project conversation history and build claude.md from it. Code is Cowork with more permissions and more freedom. Use Cowork long enough and you'll feel the sandbox limitations. Code doesn't have that problem — as long as you have security awareness, backups, and basic version control knowledge. The final form is leaving the app entirely and going to terminal Claude Code. That smoothness can be described in one phrase: unchained. There's no going back.

## Too Many Rules, Compliance Crashes

After heavy daily use, I found that stuffing too many rules into Claude.md, Rules, and memory just doesn't work. No amount of restructuring or trimming helps — instruction compliance drops hard.

There's been extensive discussion about this internationally. The consensus is that Cowork loads entire files into context — unlike CLI, which can precisely control what gets loaded — and its context maintenance is poor, carrying the full history of every previous step. A single complex Cowork session consumes quota equivalent to dozens of normal chat messages. Max 5x's "225+ messages" translates to roughly 10-20 substantive Cowork operations.

CLI's advantages become clear: prompt caching under subscription doesn't double-charge, precise context control, on-demand progressive injection. In short, CLI context is cleaner and more focused — no sandbox noise to process.

Claude.md is still important, but use indexing to keep it under 200 lines.

## Hooks: The Perfect Gatekeeper

So what do you do when rules pile up? That's when I discovered the value of Hooks. They're the kind of rule that "triggers mandatorily when conditions are met — the model cannot possibly ignore it." Unlike rules written in Claude.md, Hooks are hardcoded triggers, not suggestions the model can choose to follow or not.

I set up hooks for everything that absolutely cannot be ignored:

**External communication gatekeeper**: Any operation that sends outbound messages (Gmail, Slack, etc.) triggers a permission ask. I've tested this — it doesn't get overridden by bypass permissions. Even if you normally bypass everything, when this triggers it will 100% stop and ask you before executing.

**Security scan gatekeeper**: Any installation of external Skills, MCP servers, or packages triggers a reminder to run `/security-scan` first, report security risks, and wait for approval.

**Work journal gatekeeper**: After every git commit, write an Obsidian work journal entry, check and tick off todos, and clean up orphaned idle processes.

No more worrying after that. Hooks are the perfect gatekeeper.

If you feel like Claude.md isn't doing much for you, it's time to learn Hooks.
