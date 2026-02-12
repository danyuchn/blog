---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T05:00:00Z
title: "The Dunning-Kruger Curve of Claude Code: From Clueless to Perfect Sync"
slug: en/claude-code-dunning-kruger
featured: true
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: A heavy user with zero engineering background shares the Dunning-Kruger curve of Claude Code from day one to week three, and the workflow that finally clicked.
---

I'm not an engineer by training, but over the past six months I've used Claude Code for database refactoring, front-end/back-end integration, multi-agent orchestration, and deployment. Here's what the journey actually looked like for a complete outsider.

## The Dunning-Kruger Effect

**Day one:**
Total confusion. What is this? A BBS terminal?

As a complete tech outsider, I had this inexplicable fondness for Claude Code's pure CLI interface. Couldn't figure out why at first. Then it hit me -- I'm from the PTT generation. The CLI felt like using PTT all over again, familiar and weirdly comforting.

**Day three:**
Starting to get the hang of it. Feeling like me plus Claude Code could take on the world.

**Week two:**
Furious. It kept forgetting things, spitting out piles of garbage temp files and reports, burning through quota at lightning speed, and hitting the same wall over and over on complex bugs.

**Week three -- the turning point.**

I finally figured out how to work with it. One prompt changed everything:

> "Spin up multiple Agents to investigate my current codebase structure, markdown docs, test scripts, and git commit history in parallel. Then: 1. Clean up and consolidate docs 2. Update outdated content 3. Write the Skills I need 4. Rewrite claude.md 5. Suggest suitable sub-agents and MCPs"

After that, quota usage dropped 50%. No more banging my head against the wall retrying the same thing. Development speed doubled. It felt like we were finally in perfect sync.

When you think about it, it's the same as onboarding someone at a company. Organize the materials, update the content, provide a clear operations manual, communicate your style preferences, set up collaboration tools. The difference is you can't control a person's talent or temperament, but AI is way easier to work with on that front.

## CLI Is the Final Form

The more I use it, the more certain I am: **any IDE just ties Claude's hands. Claude in the CLI is Claude fully unleashed.**

Without IDE constraints, tool invocation in the CLI is noticeably more flexible. My go-to combo is Claude Extension paired with Claude Code -- the efficiency is insane.

Someone recommended Google Antigravity. My verdict:

1. Open Terminal
2. `brew install --cask claude-code`
3. Sign up and add credits
4. Delete Antigravity

## A Full-Scale Project in One Day

One time I spent a single day with Claude Code doing: code refactoring, redundant function cleanup, back-end database refactoring and migration (accidentally mixed up staging and production schemas in the middle -- minor disaster), and wiring up old and new database schemas with the codebase. At the end I had 4 Agents simultaneously reviewing front-end code, back-end code, database contents, and git commits.

When it was done, I realized it hadn't even been 24 hours.

Just looking at the old vs. new schema field mappings made me want to set the database on fire. I'm genuinely curious -- in the years before AI, how did engineers do all this, and how long did it take them?

## Skills vs. MCP in Plain English

A lot of people can't tell Skills and MCP apart. Let me use a secretary analogy:

**Skills** are essentially structured prompt engineering, maybe paired with some scripts. Think of them as expert handbooks.

**MCP** is all about the interface -- connecting to a specific platform so the model can call external services. Think of it as a banking app.

Imagine you have a secretary with several handbooks. When you ask them to manage your finances, they scan the titles of each handbook, find the one labeled "Financial Management Guide: Read This When Handling Accounts," open it up, learn your habits from the chapters inside -- where your accounts are, which apps to use. Then they pull up the pre-authenticated banking apps (MCP) and fetch data from each bank to review the books.

A few Skills I've found genuinely useful:
- `/ui-ux-pro-max` and `/frontend-design`: pair them with HAPPY HUE's color palette references and you can prototype directly
- Remotion Skill: make videos inside Claude Code, combine it with Anthropic's official Frontend Skill to redesign the look -- the output actually ends up with Claude's website aesthetic

## Codex: Slow and Steady Wins the Debug

Stuff that Opus can't crack? Hand it to Codex and it nails it in one pass. Codex is slow as hell, but for debugging it's godlike.

My rule of thumb: Claude Code for day-to-day development, switch to Codex when a complex bug has you going in circles. Don't get married to a single model.

## Cost Management

Here's a practical tip: type `!npx ccusage@latest monthly` in Claude Code and it'll show your monthly token usage, priced out at API rates.

For subscribers, this is pure dopamine. On my $200 USD subscription, the actual token value used came out to $3,225. And it was barely the first day of February when I'd already burned through nearly $200 worth.

Other flags:
- `daily`: daily breakdown
- `--since YYYYMMDD --until YYYYMMDD`: specify a date range
- `--breakdown`: split by model

Also fantastic for writing technical docs -- drop it into Overleaf and it passes first try. I'm noticing my conversations with AI are getting increasingly nerdy -- fork, branch, merge, push, fallback, prop, hook -- these words are in my mouth every single day now.
