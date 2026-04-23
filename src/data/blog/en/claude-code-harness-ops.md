---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T08:00:00Z
title: "Two Months of Claude Code Harness Ops: Crashes, Zombies, Cache Misses, and Plan Mode Edges"
slug: en/claude-code-harness-ops
featured: false
draft: false
tags:
  - claude-code
  - harness
  - ai-workflow
description: From March to April, running Claude Code as a long-running harness surfaced a bunch of issues. Survival tactics during the outage, my hook for cleaning up zombie processes, the resume cache-miss fix in 2.1.90, the silent memory bloat in 2.1.100, and the Plan-Mode-question-density problem after 4.7.
---

After six months of using Claude Code as a daily driver, I've come to a realization: the model's capability is already enough. What actually bottlenecks efficiency is the harness itself.

The harness is the outer layer that wraps the model and lets it run long-form. How cache gets managed, how conversations resume, how background processes get cleaned up, what you do when an official service goes down.

This post collects harness-level issues I hit from March through April, plus the fixes that landed along the way.

## The day Claude had a major outage

One day in March Claude had a major outage. I was instantly knocked back to the stone age, and a day felt like a year.

That day I thought about:

- Those days of manually copy-pasting AI chat window contents. Only a year or two ago.
- Those days of writing by typing alone, no AI. Only three or four years ago.

I'm not sure whether I've evolved or devolved.

My survival playbook during outages has stabilized:

- Sleep several times
- Deep-clean the house
- Restart the exercise routine
- Refresh the Claude status page once per hour

This stack is accidentally healthy. It turns out "Claude is down" is a mechanism that forces me back into doing things humans should be doing.

## My hook: zombie process cleanup

This half-year I wrote a hook that fires whenever I type `/clear`, `git commit and push`, or `/obsidian log` (all of which mean "this session's work is done, I'm checkpointing"). The hook cleans up leftover zombie processes.

Why the need? Because Claude Code spins up a variety of child processes in long conversations (agent-browser, Chrome MCP, Python script runners, background bash). Some finish but don't clean up cleanly. Run `ps aux` a few days later and you've got a pile of orphans. A few days without cleaning and the system quietly eats memory.

The beauty of a hook is that it auto-triggers. I don't have to remember to clean up. The act of ending work itself triggers cleanup.

This is textbook harness engineering: the model itself won't do this, so you have to add the mechanism externally.

## 2.1.90 finally fixed resume cache miss

Mid-April, 30 minutes before I wrote this paragraph, Claude Code shipped 2.1.90. It finally fixed the resume-causes-cache-miss problem.

Every time you resumed a long conversation, the first message would rebuild the entire cache. So you paid an "admission ticket" to continue working. Resume five or six times a day and you're cooked.

After the fix, the improvement was immediately felt.

This bug existed for a long time. A lot of us got burned without knowing why. You'd wonder "why does my first message after resuming burn so much token" and assume you wrote too-long prompts. Actually, the resume mechanism was doing the damage.

Once fixed, my long-running project sessions became genuinely resumable.

## 2.1.100: two quiet fixes worth noting

CC 2.1.100 had two fixes worth noting:

1. **Tagging large files no longer does JSON escape processing**, which meaningfully reduced token consumption. If you `@`-mentioned a large file and token usage mysteriously ballooned, this was it.
2. **Fixed the long-session memory explosion bug**, caused by markdown syntax highlight cache.

Both bugs silently ate resources. After the fix, the same work consumes noticeably less token.

This category of "silent bug" is the hardest to catch at the harness layer. The model appears to be operating normally, but resource management underneath is quietly leaking.

## Plan Mode's question density (the 4.7 issue)

Six questions. Is that Claude Code Plan Mode asking? I'm in auto mode. Why is the question density higher than plan mode?

After 4.7, this tendency got noticeably worse. My guess:

- The new adaptive thinking mechanism makes the model do more self-check at launch
- Part of that self-check surfaces as "confirming with the user"
- Result: auto mode question density is comparable to plan mode

This is a hidden harness tax. You pick auto expecting smooth flow, instead you get interrupted six times.

My current workaround is to front-load every potential clarification point into the first message, killing the source of "possible questions." Not perfect, but it compresses six questions to one or two.

## Harness Engineering has a long way to go

Watching these small fixes pile up week by week, I'm increasingly convinced harness engineering has a long road ahead.

Model capability progresses at a relatively steady pace, but the harness layer is far behind. A lot of "Claude Code sucks" complaints aren't actually about the model being bad. The outer mechanism just isn't mature enough.

Problems at this layer include but aren't limited to:

- State management (resume / cache / compact)
- Process lifecycle (agent child processes, hooks, background tasks)
- Conversation flow control (plan mode / auto mode / permission mode)
- Error recovery (outage fallback, interrupted continuation)
- Resource accounting transparency (where tokens went, how efficient)

These don't make the model smarter, but each one directly affects real-world usability. Anthropic's recent versions have been chipping away at these, but progress is slow.

## The real model limits are elsewhere

One last observation: I think the actual ceiling on model capability is how to transition from stateless to stateful, and how to update weights during use.

Those are the genuine differences between humans and current AI.

Right now the harness layer is faking statefulness with engineering tricks: memory files, CLAUDE.md, auto memory, session JSONL. All of these are prosthetic memory systems bolted on from outside. The real breakthrough should be when the model itself can maintain state and learn continuously, rather than leaning on an external filesystem as a crutch.

But until that day comes, harness engineering is the public infrastructure project those of us in it for the long haul have to keep maintaining together.
