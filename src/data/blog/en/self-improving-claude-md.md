---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-13T04:00:00Z
title: "I scanned 500 Claude Code sessions and the AI stopped making the same mistakes"
slug: en/self-improving-claude-md
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - productivity
description: "I used claude-log to scan 500+ Claude Code sessions across 6 projects, extracted every time I yelled at the AI, and turned those into CLAUDE.md rules. Here's what I found."
---

## The Problem with CLAUDE.md

If you use Claude Code, you know about `CLAUDE.md` — the instruction file you drop in your project root to tell the AI what rules to follow.

Here's the thing: you write it based on what you *think* the AI needs to know. But you can't remember every mistake it's made, and you're definitely not going to calmly update documentation every time it does something dumb.

So your `CLAUDE.md` ends up being "what you imagine AI should know." What AI actually keeps screwing up? You forgot about that three sessions ago.

## The Article That Started This

I stumbled on a blog post by London-based engineer Martin Alderson: [Self-improving CLAUDE.md files](https://martinalderson.com/posts/self-improving-claude-md-files/).

His idea is dead simple: every Claude Code conversation gets saved as JSONL files on your machine (`~/.claude/projects/`). Instead of relying on your memory, have the AI scan its own chat history, find the moments you got frustrated, and turn those lessons into `CLAUDE.md` rules.

He built a CLI tool called [claude-log](https://github.com/martinalderson/claude-log-cli) to make parsing those logs fast. C# AOT native binary, 3MB, 2ms startup. Install and go.

## My Experiment

I have 6 projects using Claude Code, totaling over 500 sessions. I figured: why not scan everything at once?

### Setup

```bash
# macOS Apple Silicon
curl -sL https://github.com/martinalderson/claude-log-cli/releases/latest/download/claude-log-osx-arm64 -o /tmp/claude-log
chmod +x /tmp/claude-log
cp /tmp/claude-log /usr/local/bin/claude-log
```

### The Key Commands

```bash
# List all projects
claude-log projects list

# Search for frustration keywords
claude-log sessions search "wrong" --path ~/my-project
claude-log sessions search "revert" --path ~/my-project
claude-log sessions search "unacceptable" --path ~/my-project
```

The trick is searching for **the words you use when you're mad at the AI**. Since I work in Chinese, I searched for things like「不對」(wrong),「改回來」(revert that),「不可接受」(unacceptable),「不要」(don't do that),「太複雜」(too complex).

English users might search for: "wrong", "revert", "undo", "stop", "that's not what I asked", "no", etc.

## What I Found

### GMAT Simulator (198 sessions)

My biggest project. The most findings too.

Searching "revert" turned up a good one: the AI modified a TPA question type's split-view display without looking at how practice mode already implemented it. The whole thing was wrong and I made it revert. That became a rule: read existing implementation before modifying anything.

Searching "unacceptable" was even better. The AI hit a Firestore permission error and instead of fixing the root cause, it used a fallback to bypass it. My exact words: "Unacceptable. This fallback approach is wrong. Roll back and fix the permission issue properly." New rule: fix root causes, no workarounds.

Searching "wrong" caught a database migration going the wrong direction. Two formats coexisting, old and new. The AI modified the *new* code to fit the *old* format. Completely backwards. I told it: "No, you should migrate the database to support the new format."

Bonus find: the CLAUDE.md stated the Elo unlock threshold was 30 attempts. The actual code uses 20. Documentation-code drift that you'd never catch without scanning the logs.

### GMAT Skills (211 sessions)

The worst offender. The word "don't" appeared **146 times** in my corrections.

Most common issue: wrong parameters and paths (typos in IP addresses, wrong model names, confusing permalink IDs with slugs). The AI also kept handling cases one-by-one instead of finding patterns. I had to tell it multiple times: "Don't fix these individually. Identify the pattern and design a rule."

### Video Translate (46 sessions)

Biggest find: the AI kept reading large log files directly into context, blowing up the session. The warning "don't read the log file directly" appeared 14 times.

### Personal Finance (33 sessions)

Interesting pattern: the AI used stale training data (like "US stock average volatility is 10%") instead of searching for current data. My exact words: "Did you actually search online? Don't rely on your own guesses."

### Crawler (12 sessions)

Searched for "wrong", "revert", "undo" — zero results across all sessions. The AI performed well here consistently, probably because the tasks are relatively straightforward (scraping + data processing).

## Running It at Scale

Doing this manually for each project is slow, so I had Claude Code automate it: I spawned 6 parallel agents, one per project, each responsible for scanning logs and updating that project's `CLAUDE.md`. Plus one more agent for the user-level `~/.claude/CLAUDE.md` (cross-project rules).

7 agents running in parallel. All done in about 5 minutes.

## The Results

After updating all the CLAUDE.md files, the AI genuinely feels more compliant.

That déjà vu of "I literally told you not to do this before" happens way less now. The AI isn't perfect, but those low-level repeated mistakes have dropped noticeably.

For example, the AI used to jump straight into editing without reading existing code. Now it reads related files first. It used to swallow errors with try-catch when encountering problems. Now it looks for root causes.

## A few notes if you try this

The search keywords matter a lot. Different people express frustration differently, and different languages have different correction phrases. Think about what you actually say when the AI does something dumb, and search for that.

Not every project will have findings. Projects with few sessions might turn up nothing, and that's fine. It might just mean the tasks are simple enough that the AI doesn't screw up.

`sessions tools` is also worth running. It shows tool usage stats across all sessions, and sometimes you notice odd things, like one tool being called thousands of times while another is barely touched.

I plan to run this monthly. And don't bother reading the JSONL files yourself. Just have Claude Code use claude-log to search, analyze, and update the CLAUDE.md. Automate the whole loop.

At the end of the day, your `CLAUDE.md` should come from actual screw-ups, not from sitting in a chair imagining what the AI might need. This tool just makes it easy to dig those lessons out of hundreds of sessions. Five minutes, maybe less.

---

**Links:**
- Article: [Self-improving CLAUDE.md files](https://martinalderson.com/posts/self-improving-claude-md-files/)
- GitHub: [martinalderson/claude-log-cli](https://github.com/martinalderson/claude-log-cli)
