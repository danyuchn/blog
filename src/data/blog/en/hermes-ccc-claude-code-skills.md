---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:00:00Z
title: "hermes-CCC: Bringing All 46 Hermes Agent Capabilities into Claude Code"
slug: en/hermes-ccc-claude-code-skills
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - skills
description: Someone ported the entire NousResearch Hermes Agent into 46 native Claude Code Skills. No OAuth, no external processes, just restart CC and you're ready. The core philosophy is "procedures-as-prompt" — structured markdown instruction scripts drive AI behavior without writing a single line of code.
---

Hermes Agent is an AI agent runtime built by NousResearch — it has its own memory system, tool routing, and cross-session learning capabilities. The original design runs it as an independent process with its own runtime.

The author of [hermes-CCC](https://github.com/AlexAI-MCP/hermes-CCC) made an interesting observation: **Claude Code is already an agent runtime. There's no need to run a separate process.**

So they broke down every Hermes Agent capability into 46 Skills and loaded them into Claude Code's native Skill system. No OAuth, no extra accounts, no external processes — restart Claude Code and everything is available.

## Procedures-as-prompt

The core design philosophy here is worth examining on its own.

Each Skill is a `SKILL.md` file written in structured natural language that specifies: trigger conditions, execution procedures, output format, failure modes, and recovery actions. Claude Code reads the `description` field to decide whether to trigger, and reads the `## Checklist` to step through execution.

No code. No function calls. **Pure markdown instruction scripts driving Claude's behavior.**

This isn't laziness — it's a deliberate design choice. Traditional agent frameworks require Python, dependency management, API handling, and runtime maintenance. Procedures-as-prompt moves the "behavioral specification" from the code layer up to the text layer. Anyone can read it, anyone can modify it, and the AI itself understands what it's doing.

## Manual vs Automatic Triggering

There's an important mental model to establish when working with this kind of Skill system.

**Manual triggering**: You type `/hermes-route`, `/systematic-debugging`, or another slash command directly. Guaranteed execution, no ambiguity.

**Automatic triggering**: Each `SKILL.md` has a `description` field in its frontmatter. Claude reads every Skill's description on each conversation turn and decides whether the current context matches — if it does, the Skill triggers automatically. This is an expectation, not a guarantee.

The more precisely the description is written, the more reliable the automatic triggering. But LLM judgment is inherently non-deterministic.

**Manual triggering is a guarantee. Automatic triggering is an expectation.** Keep this in mind or you'll develop incorrect expectations about how "automated" the system actually is.

## The Most Notable Skills

With 46 Skills, I can't cover them all, but a few stand out for their design thinking:

**`/hermes-route`: Task Router**

Classifies each task before execution, determining how to approach it. Outputs a routing decision block including: task class (lightweight / standard / deep), execution mode, files to read first, whether parallelism is possible, and required reasoning depth.

The key insight is "evaluating the cost of getting the first step wrong" — for a deep task, a wrong first move costs far more to recover from than for a lightweight one.

**`/hermes-memory`: Layered Cross-Session Memory**

Manages persistent memory across sessions with four operations: Prefetch (pull relevant memories before work), Sync (merge new knowledge after work), Nudge (suggest things worth saving without auto-saving), Compress (clean up duplicates and delete stale memories).

It forces a distinction between "persistent knowledge" (architecture decisions, tool pitfalls, preferences) and "temporary state" (branch names, single-task progress) — a distinction most people miss when managing memory manually.

**`/hermes-compress`: Context Compression into Six Buckets**

When the context window is nearly full, it extracts the current conversation into a structured summary stored in memory, freeing up context space. Six buckets: decisions, artifacts_created, problems_solved, facts_learned, open_issues, next_steps.

This is more organized than manually running `/compact` — instead of condensing conversation into prose, it forces structure.

## The Real Value of This Repo

hermes-CCC is worth studying not just because you can use 46 Skills out of the box.

More importantly, this repo demonstrates something: **Skill systems can be architecturally designed.** Task routing, memory layering, context management, sub-agent coordination — all the familiar patterns from agent frameworks can be expressed in SKILL.md language.

If you're designing your own Skill system, hermes-CCC is currently the most complete reference implementation of "how to architect a Skill system" that the community has produced.

GitHub: https://github.com/AlexAI-MCP/hermes-CCC (run `/security-scan` before installing)
