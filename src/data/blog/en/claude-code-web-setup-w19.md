---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "Two Worlds of Web-Based Claude Code Setup"
slug: en/claude-code-web-setup-w19
featured: false
draft: false
tags:
  - claude-code
  - ai-coding-tools
  - ai-workflow
description: Web Claude Code has two completely different runtimes — cloud VM and remote-control. Here is what I learned setting up both, the small bugs I hit, and why some user-level configs simply cannot be lifted to the cloud as-is.
---

The iOS Claude app is so bad that I gave up. Combined with the fact that recent updates have all gone to the desktop app and the web app, my phone now uses web Claude Code exclusively.

After a couple of weeks of real use, here is what is worth knowing.

## Two runtimes, very different

Web CC actually has two completely different execution environments:

1. **Cloud VM** — runs on a cloud-hosted virtual machine
2. **Remote-control** — connects back to your always-on home computer's CC session

### Remote-control is the simple one

It is just your home machine's session shown through a different UI. `claude.md`, rules, hooks, memories, skills, MCP — all of it works the same.

Two small bugs I have found:

- The slash menu only surfaces official commands and skill prompts. Custom commands you installed locally do not appear in the menu. But typing the full name or invoking them by phrasing still works.
- Bypass mode is not exposed in the web mode switcher. The web UI only goes up to Auto. If you need bypass, switch to the CLI.

### Cloud VM is where it gets interesting

When the VM boots, it injects a system-reminder containing `claude.md`, rules, skills, MCP, environment info, and so on. But everything inside `.claude/` is pulled from your remote git repository. So you have to make sure the bits you want are not gitignored.

Committing the entire config folder is also a bad idea — it contains massive history conversation jsonl files that should be excluded.

A few key differences:

- **Only project-level `.claude/` is visible in the cloud.** The project-local `.claude/` (committed, readable in cloud) and your home `~/.claude/` (user-level, not committed, not readable in cloud) end up out of sync in obvious ways.
- **Only remote MCPs work** — local `server` MCPs are unreachable. This severely limits remote scheduled jobs.
- **Some sensitive env vars should not be committed.** So web Claude Code lets you configure VM-specific environment variables and pre-launch setup scripts in its UI.

## Take

The two web modes serve different needs: remote-control is for "my computer is doing work, I'm on the go"; cloud VM is for "spin up a clean environment for this project." But migrating user-level config to the cloud means accepting that you are essentially writing a leaner cloud-only version of `.claude/`.

The actual setup info-cards from my Threads post:

![Web Claude Code setup, part 1](/blog/assets/posts/claude-code-web-setup-w19/web-setup-1.jpg)

![Web Claude Code setup, part 2](/blog/assets/posts/claude-code-web-setup-w19/web-setup-2.jpg)
