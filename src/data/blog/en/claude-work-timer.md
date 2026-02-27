---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-27T02:00:00Z
title: "claude-work-timer: Auto-Track Your Claude Code Working Hours"
slug: en/claude-work-timer
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - open-source
description: "Billing clients by the hour with Claude Code? I built an open-source plugin to track actual working time automatically."
---

## The Problem

More and more developers are using Claude Code for client work — myself included. But there's one need that hasn't been addressed: how do you accurately track Claude Code working hours?

For hourly-billed projects, clients can ask for time logs at any moment. And if you're any good with Claude Code, you're probably running four or five projects in parallel across split windows. How do you accurately calculate the actual time spent on a specific project — including conversations, file reads, writes, and tool calls — minus all the idle time when you went to grab coffee or reply to messages?

I looked around. Nobody had built this. So I built it myself.

## claude-work-timer

[claude-work-timer](https://github.com/danyuchn/claude-work-timer) is an open-source CLI tool that reads your Claude Code session history and calculates precise conversation and tool-call durations.

Here's what it does:

- Reads session JSONL history files
- Calculates actual time spent on each conversation turn and tool call
- Automatically strips out idle gaps longer than 5 minutes
- What's left is your real working time

It supports filtering by project, so even if you had five projects running simultaneously, you can get a separate time report for each one.

## Installation and Usage

The easiest way: paste the GitHub link into Claude Code and ask it to install the tool and check your project hours. It'll handle everything.

Or install manually:

```bash
npm install -g claude-work-timer
```

Check working hours:

```bash
claude-work-timer --project /path/to/your/project
```

GitHub repo: [github.com/danyuchn/claude-work-timer](https://github.com/danyuchn/claude-work-timer)
