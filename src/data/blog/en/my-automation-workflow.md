---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T10:00:00Z
title: "My Claude Code Automation Stack: /loop, Monitor Tool, the Skill System, Obsidian Reflection Reviews"
slug: en/my-automation-workflow
featured: false
draft: false
tags:
  - claude-code
  - automation
  - ai-workflow
description: From /loop clocking in for me at ERP, to Monitor Tool as a background event gatekeeper, to Google Map MCP saving browser clicks, to Obsidian + Mirror framework for weekly reflection. Here's my six-month Claude Code automation stack, plus a clarification of how commands and skills actually split.
---

After six months my Claude Code workflow has accumulated an automation stack.

This isn't a "how to set up X" post. I want to string together the automation mechanisms I actually use daily and show how they divide up the work. Hopefully useful for anyone exploring a similar setup.

## Preface: commands vs skills, finally clear

First, a point of frequent confusion.

I finally figured it out after reading the official docs: custom commands is the old format, already merged into the skill system. They're compatible, but skills add directory structure support, frontmatter control, and auto-triggering.

Going forward, just call everything a skill.

If you're still writing `.md` files in `.claude/commands/`, the official guidance is to migrate to `~/.claude/skills/`. Migration isn't complex, mainly adding frontmatter.

This clarification mattered for my stack's layering. I used to put "command-like" things in commands and "knowledge-like" things in skills. Now I can manage both under a unified skill structure.

## Layer 1: the `/loop` scheduler

`/loop`, added in a recent Claude Code release, is one of the most practically useful new features this half-year.

Real uses:

**Case A: auto clock-in**

```
/loop 1d clock me in on the ERP
```

Congratulations, you've earned fully automatic work days.

**Case B: Messenger DM relay**

Some teammates still communicate through Messenger personal accounts, and Meta doesn't provide API access for personal accounts. I used to screenshot or copy-paste messages.

Now `/loop` can run the task on a schedule. Periodically open Chrome MCP, read new messages, summarize, drop into my designated folder.

The essence of `/loop` is that "periodic execution" is the simplest automation, but also the piece Claude Code lacked for the longest time. Having it means a lot of small tasks don't need manual triggering.

## Layer 2: Monitor Tool as event gatekeeper

Claude Code recently shipped Monitor Tool: let Claude write a background watcher script (logs, PR status, API endpoints), wake the agent only when a significant event is detected, consume zero tokens the rest of the time.

Essentially a gatekeeper for the agent: don't rush me, come back when something happens.

Monitor Tool and `/loop` complement each other:

- `/loop`: periodic, unconditional execution (I know what to do and when)
- Monitor Tool: sporadic, condition-triggered (I only want to act when a specific thing happens)

The former is scheduling, the latter is interrupts. Together they cover most automation needs.

My current Monitor Tool uses:

- Watching GitHub Actions failure notifications
- Watching Vercel deploy status
- Watching specific API endpoint response changes (external SaaS status)

These used to be a separate Terminal window running `watch` or `tail -f`. Now tokens aren't consumed, and the agent is only invoked when the event hits.

## Layer 3: the MCP tooling layer

MCP (Model Context Protocol) is the standard protocol that lets Claude call external services directly. My commonly-used ones:

**Google Map MCP** (official, from Anthropic)

Genuinely good. Query locations, calculate distances, find routes. Workflows that used to require flipping between browser tabs collapse to a single command. Especially useful for me since I'm often out and about in Thailand.

**agent-browser** (skill, from Vercel)

Chrome MCP is both token-heavy and disconnect-prone. It's a last resort. If you don't need a persistent logged-in session, Vercel's agent-browser skill is much better.

My browser routing decisions:

- Needs a logged-in session (Google, Notion, etc.) → Chrome MCP
- Aggressive bot detection (Reddit, LinkedIn) → Chrome MCP or JSON API
- Everything else → agent-browser

**crawl4ai**

Pair with agent-browser. `/agent-browser` suits interactive use; `/crawl4ai` is for bulk data extraction.

## Layer 4: design-type skills, creative use

`/frontend-design` looks ugly? What now?

Tell it to redesign, and have it generate 20 static HTML variants for you to pick from.

I discovered this recently. Previously I'd tweak details directly (change color codes, adjust padding). Ten iterations in, still wrong. Switching to "give me 20 versions, I'll pick" is roughly 10x more efficient than slow iteration.

The logic behind this: AI is good at generate, bad at iterate. Asking it to produce many candidates at once beats asking it to revise one candidate.

This principle generalizes to other generative skills: writing slogans, designing logos, naming things, drafting opening lines. All of them: "give me 20, I'll choose" beats "give me 1, we'll refine."

## Layer 5: Obsidian + Mirror framework weekly review

My Obsidian vault contains:

- Journal
- Work log
- Ideas
- Thoughts
- Project cross-links
- All tasks big and small

I frequently ask Claude "what should I do today," and each week I use the Mirror framework for a reflection review:

1. Read the past week's daily notes
2. Check whether my trajectory matches my life goals
3. Identify the lesson I least want to face (e.g., procrastination)
4. Apply the Atomic Habits framework to propose improvements for next week

This is the stack's "reflection layer." The layers below execute, this one audits whether execution direction is right.

Without this layer, stronger automation just means faster wrong-direction work. With this layer, automation is an amplifier instead of an error amplifier.

## The overall architecture

Stacking the five layers:

```
[Reflection]  Obsidian + Mirror framework          ← direction calibration
[Tooling]     MCP (Google Map / agent-browser)     ← capability extension
[Interrupt]   Monitor Tool                         ← event-triggered
[Schedule]    /loop                                ← time-triggered
[Command]     skills (on-demand)                   ← manually invoked
```

From bottom up, each layer solves a different problem. Bottom two (command, schedule) do the work. Middle two (interrupt, tooling) improve efficiency. Top (reflection) sets direction.

## What I didn't put in the workflow

Equally worth mentioning. Things I tried and dropped:

- **AI-synthesized voice**: Personal preference, I still record voiceover myself for videos
- **Complex multi-agent orchestration**: Claude Code's subagent is already enough. More elaborate frameworks (CrewAI, Autogen) are overkill for my use case
- **Auto-posting to social platforms**: I'd rather manually review before sending. Auto-posting too easily produces tone-off content
- **Dumping large datasets into Opus**: Now I discuss the schema with Opus first, then batch-process with cheaper models on SiliconFlow / OpenRouter

Subtraction matters as much as addition. A workflow isn't "more tools = better." What should be there, is. What shouldn't, doesn't take up slot.

## What's next

The piece I'm still missing is "long-term memory integration." Obsidian, auto memory, CLAUDE.md, and rules. These four knowledge sources run in parallel right now with no unified indexing.

Ideal state is a meta-skill that can search across all four sources. Probably next month's project.
