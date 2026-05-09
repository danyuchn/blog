---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-03T04:00:00Z
title: "Moving from Claude Code to Codex: I Built a Skill to Handle It"
slug: en/codex-migration-skill
featured: false
draft: false
tags:
  - claude-code
  - codex
  - ai-coding-tools
  - skills
description: Migrating an entire personal harness from Claude Code to Codex is not trivial — claude.md / agents.md, MCP, hooks, settings each need their own translation. I packaged the workflow as a Skill on GitHub. Plus a note on why I keep reaching for Codex these days.
---

The thing I actually got done this weekend was migrating my Claude Code personal environment over to Codex.

Honestly, I have been reaching for Codex more and more. Beyond the generous quota resets, GPT-5.5 has dropped that oily tone — work conversations feel grounded again. Meanwhile Opus 4.7 keeps making me want to slap it.

But moving an entire harness over is hard.

## The pain points

- Harness migration touches many configs and files; the workflow is tedious
- MCPs, hooks, and other key bits need manual handling, with high trial-and-error cost
- After future updates on either side, the two environments drift quickly
- Migrating a personal workflow end-to-end takes serious time and energy

## What the Skill does

I packaged the migration into a Skill:

- Produces a Claude Code → Codex migration plan in about half an hour
- Auto-handles `claude.md` / `agents.md`, Skills, and other base settings
- Helps with the trickier stuff like MCPs and hooks
- Provides a "maintenance mode" that diffs changes and syncs them across to Codex
- Reduces manual operations and try-and-fail risk

Repo: <https://github.com/danyuchn/claude-codex-harness-sync>

![Claude Code → Codex migration Skill](/blog/assets/posts/codex-migration-skill/codex-migration.jpg)

## A side gripe: Codex CLI still has gaps

After using Codex for a stretch, the most painful gap is the CLI — `/rewind` not being available is hard to forgive. On Claude Code, `/rewind` is daily survival. After migrating, the first time you make a wrong turn you realize there is no clean undo. Either git stash or rerun the whole conversation. Productivity hit is real.

Hoping OpenAI ships those CLI updates soon.

## A small accident with image generation

While generating images, I noticed something: **issuing image prompts directly inside Codex produces better results than having Claude Code hand them off to Codex.**

Why? Because Claude tends to issue over-constrained prompts, while GPT-image-2 actually shines with fewer constraints — its creativity lives in the negative space.

The more layers of intermediation, the more the original intent gets "polished" away. Worth thinking about for any cross-agent task handoff, not just image generation.
