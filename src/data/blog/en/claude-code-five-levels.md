---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-24T04:00:00Z
title: "The 5 Levels of Claude Code: You Don't Choose to Upgrade, the Ceiling Forces You"
slug: en/claude-code-five-levels
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: From Raw Prompting to Orchestration — the 778-upvote Reddit framework where every level exists because the previous one broke.
---

A lot of people say Claude Code is unstable. Works great sometimes, then suddenly goes off the rails. I used to think the same.

Then I came across a Reddit post that reframed everything. The problem wasn't that Claude Code was unstable — I'd been stuck at the same level, hitting the same ceiling, over and over.

The author, u/DevMoses, mapped out five maturity levels. The thread got 778 upvotes and 157 comments, with a lot of people saying "this is exactly what I've been dealing with."

## The Core Logic

"You don't decide to upgrade — the ceiling forces you."

Each level exists because the one before it eventually breaks down.

## The Five Levels

| Level | Name | What It Does | Where It Breaks |
|-------|------|--------------|-----------------|
| L1 | Raw Prompting | Describe what you need in plain conversation | Project grows, agent starts forgetting conventions and introducing inconsistent patterns |
| L2 | CLAUDE.md | Context file in project root — tech stack, naming rules, what to never do | Compliance drops past ~100 lines; quality also degrades in long sessions |
| L3 | Skills | SOP files in `.claude/skills/`, loaded on demand, teaching the agent how to do specific tasks | Agent follows instructions, but nobody's checking quality automatically — you're still the only QA |
| L4 | Hooks | Lifecycle scripts: typecheck after every edit, quality gate before completing, load context at session start | Still a single agent, single session — can't handle projects that exceed the context window |
| L5 | Orchestration | Parallel agents + isolated worktrees + cross-session state + a coordination layer to prevent file conflicts | Author ran 198 agents across 32 fleet sessions; merge conflict rate: 3.1% |

Each level works until it doesn't.

## A Few Details Worth Noting

**The CLAUDE.md ceiling** is the most widely shared pain point. Comment after comment said the same thing: "I found the answer, then one day it just stopped working." The author cut his own CLAUDE.md from 145 lines down to 77 before things improved.

**Skipping levels is a disaster.** Each level's infrastructure is a prerequisite for the next. Jumping from L2 straight to L5 is asking for trouble.

**Skills aren't zero-cost.** There's a small token overhead in the frontmatter discovery process — it's not completely free context.

**Enterprise repos may behave differently.** A few users with codebases in the hundreds of thousands of lines said CLAUDE.md has never failed them. Probably related to usage patterns and repo structure.

## The Community-Proposed L6

Someone in the comments added a sixth level: have Claude build your customized Claude workflow for you — a self-improving system.

The implementation: a SessionEnd hook that extracts behavior patterns → a nightly agent aggregates them into new skills → they're automatically promoted once tests pass.

Most people won't need this. But the direction is right — ideally the system knows where it's weak and patches itself.

## For Non-Developers

- L3 can be approximated with custom instructions, no terminal required
- L4 can be simulated by building manual quality checks into your prompts
- L5 is currently only practical for developers

The value of this framework for non-developers isn't to push you through all five levels. It's to help you recognize: when Claude Code starts going wrong, the answer isn't more chat. It's better structure.

## Where This Leaves Me

I'm somewhere between L3 and L4. CLAUDE.md is there, Skills are set up, Hooks are partially running.

I've used L5 orchestration a few times. Each time it broke in a place I didn't anticipate.

But at least now I know — that's not Claude Code being unstable. That's my infrastructure not being ready.
