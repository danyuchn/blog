---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T16:30:00Z
title: "This Week in the Claude Code Ecosystem: Four Resources I Bookmarked"
slug: en/claude-code-ecosystem-roundup-apr08
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-trends
description: Enterprise office tools, Taiwan local services, a hobby vertical, beginner onboarding—four different corners of the Claude Code ecosystem all shipped something this week. Each represents a use case that's still underexplored.
---

Four new Claude Code resources landed in my bookmarks this week. Individually they look small, but lined up side by side you notice something: **Claude Code isn't just a coding axis anymore.** It's slowly filling in enterprise office tools, local services, hobby verticals, and beginner onboarding.

All four had real value for me. Sharing the list for anyone else hunting for application ideas.

## 1. Microsoft 365 CLI — The Enterprise Office Automation Gateway

The most common question I get from enterprise students is, "Can Claude Code plug into my work tools?" They usually mean Teams, Outlook, SharePoint, OneDrive—the whole Microsoft 365 stack.

The answer is yes. And there are two tools:

- **`m365`** (PnP Community): high-level commands that understand business context. Install it and you can `m365 teams channel message list` without touching Graph API.
- **`mgc`** (Microsoft official): direct mapping to Graph API endpoints. 100% coverage, but you'll be reading API docs.

For Claude Code, `m365` is the pick. `npm install -g @pnp/cli-microsoft365` and you're done. Personal accounts log in straight away; corporate accounts depend on IT policy for Admin Consent.

Practical workflows: pull Teams meeting transcripts → Claude summarizes → auto-post back to the channel; batch-manage SharePoint document library permissions; onboarding/offboarding automation. The "stuff I do every day but not enough to justify writing code for" category—suddenly the cost drops to zero.

GitHub: <https://github.com/pnp/cli-microsoft365>

## 2. job104-cli — A Taiwan Job Board POC

[@miblue119](https://www.threads.com/@miblue119/post/DWwL7YZGmK1) built an unofficial CLI/Skills POC for 104 (Taiwan's biggest job board) that lets AI agents search listings and query uploaded résumés. Pure experiment, non-profit, explicitly restricted from commercial use by anyone but 104 itself.

Why it matters? Because it's the first Taiwan-local service where someone actually shipped a Claude Code integration. 104 hasn't done this and probably won't for a while, but one person put a working POC out there.

The architecture (CLI + Skills, two layers) is exactly what we teach at AgentCrew Academy—there's a CLI that handles the actual API calls, and a Skill wrapper on top for Claude to read. For anyone trying to "Claude-Code-ify" their internal company tools, this repo is a great reference.

- Site: <https://job104-cli.dev/>
- CLI: <https://github.com/MIBlue119/job104_cli>
- Skills: <https://github.com/MIBlue119/job104-cli-skills>
- Install: `brew install MIBlue119/tap/job104-cli` or `uv tool install job104-cli`

I'd love to see POCs for 1111, CakeResume, and MetaHR next. There are too many useful Taiwan-local services still stuck in web UI land.

## 3. Sports Betting Skills — Hobbies Deserve Logic Too

I bookmarked these because a friend asked whether Claude could help with sports betting. Turns out mcpmarket already has two:

- **Market Mechanics & Betting**: bankroll management. Kelly Criterion to size your bets, Brier score to track prediction accuracy, edge detection to find gaps between bookmaker odds and real win rates (value bets). Basically a layer that keeps gambling from turning into entertainment losses.
- **sports-betting-analyzer**: intelligence analysis. Spreads, over/unders, prop bets, historical matchups, form, injuries, value-bet identification.

Both target US sports (NBA/NFL), so Taiwan lottery formats would need their own odds feed. And before installing: run `/security-scan`. mcpmarket skill quality varies a lot.

The takeaway that stuck with me: **any domain with stable input (data) + stable logic (rules) can become a skill**. Sports betting is an extreme example, but the same framework applies to anything data-plus-judgment work—stock picks, fund analysis, real estate evaluation, you name it.

## 4. Claude Code Install Guide Resources

The fourth bookmark is slightly different—I was collecting material for the AgentCrew Academy site's install guide update, and figured I might as well share.

The biggest Windows student pain point isn't Claude Code itself—it's **Git not being installed + `.local\bin` not in PATH**. I used to think this was edge-case. Teaching has taught me it's the default: at least half the Windows students in every cohort hit this wall.

Cleanest Windows one-liner:

```powershell
winget install Git.Git --accept-package-agreements --accept-source-agreements --silent; irm https://claude.ai/install.ps1 | iex
```

`winget` is built into Windows 10/11—no extra install needed. This one command installs Git, installs Claude Code, and sets up PATH. The only thing the student needs to confirm is the UAC dialog. After it finishes, close and reopen PowerShell so Git picks up the PATH change.

Mac is simpler:

```bash
brew install --cask claude-code
```

Or the official `curl -fsSL https://claude.ai/install.sh | bash`.

Further reading:

- [Claude Code Quickstart (Official)](https://code.claude.com/docs/en/quickstart)
- [SmartScope — Windows Native Installation Guide](https://smartscope.blog/en/generative-ai/claude/claude-code-windows-native-installation/)

## An Observation

Looking at all four together, the throughline is this: **Claude Code's boundary was never "writing code"—it's "anything with a CLI or an API."**

Enterprise systems have APIs (Microsoft Graph), so m365 exists. A Taiwan local service has an unofficial CLI (job104-cli), and someone wraps it into a skill. Sports betting has data and formulas, so Kelly Criterion and Brier scores become skills. Even installation itself has become "one-line workflow."

Whether you end up using Claude Code depends entirely on whether you've trained yourself to ask "does this thing have a CLI?" as a reflex. If yes, you can plug in. If no, you wait for someone else's POC or build your own.

Probably more of these next week. This kind of weekly roundup might become a habit—collecting fragmented resources before I forget them, and treating the list as my "who's doing what" radar for the ecosystem.
