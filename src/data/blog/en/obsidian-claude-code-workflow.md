---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-20T04:00:00Z
title: "Obsidian + Claude Code: My Daily Knowledge Management Workflow"
slug: en/obsidian-claude-code-workflow
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - productivity
description: Put your entire life into Obsidian, then let Claude Code tap in. How I do daily logs, manage to-dos, and why local Markdown beats Notion.
---

My Obsidian vault holds my diary, work logs, ideas, stray thoughts, links across all my projects, and every to-do item big and small. Then I hook Claude Code into it, so AI can directly read and write all of that data.

This isn't some fancy architecture. It's just plain old "put everything in one place and let AI see it too." But it works surprisingly well.

## Daily Logs: /obsidian log

The `/obsidian` log function is incredibly useful. It takes everything you did in a conversation session, timestamps it, and writes it to your daily log.

When I finish a chunk of work, I just type `/obsidian log` and it's automatically recorded. Every week I roll up the daily logs into a weekly review, and I get a clear picture of what I actually accomplished. No need to deliberately write daily reports—the work itself becomes the report.

## To-dos: Blocking vs. Non-blocking

The beauty of putting your whole life into Obsidian and connecting it to Claude Code is that it can tell me at any point which to-dos are blocking (waiting on someone else or a dependency) and which are non-blocking (things I can do right now).

Then, in the gaps between my conversations with Claude Code, it automatically handles the non-blocking items. I often ask Claude "what should I do today?" and it pulls all the to-dos from the vault, prioritizes them, and starts knocking out the doable ones while we chat.

## The Quota Reset Day Ritual

When your weekly quota is about to reset within a day and you're temporarily a "single-day token millionaire," that's the time to go into planning mode:

One, give it full computer access, scan every project that uses Claude Code, and get recommendations for archiving outdated and temp files.

Two, use the claude-log CLI to read all session transcripts from the past week, find spots where communication with Claude Code was rough, then use official docs and best practices to refine your Claude.md, rules, and memory files.

Trust me, this will make the following week significantly smoother.

## Why Obsidian Beats Notion

One word: local.

Your data lives in local Markdown files. If Obsidian vanishes tomorrow, your data is still there. Notion's data lives in the cloud—export formats are limited, and you never know when they'll change their API, pricing, or policies.

More importantly, local Markdown files can be read and written by Claude Code directly, with zero middleware. Notion requires API integration—one more layer means one more point of failure.

Simple, reliable, no vendor lock-in. That's what a knowledge management tool should look like.
