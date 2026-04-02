---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-01T04:00:00Z
title: "Claude Code's Cache Crisis: Why Your Quota Burns So Fast"
slug: en/claude-code-cache-crisis
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
description: A Reddit user reverse-engineered two official bugs, and combined with the compounding effect of 1M-token context, your quota might be silently burning at 20x the expected rate.
---

About two weeks ago, the term "Claude Quota Crisis" started circulating online. People were discovering their quotas had shrunk dramatically—a few messages and they'd get locked out, to the point where the service was basically unusable. Anthropic's announcement about "reducing quotas during peak hours" only poured gasoline on the fire.

Then someone on Reddit spent an afternoon and dug out the truth.

## Two Bugs Eating Your Quota

**BUG 1: Cache String Corruption**

Normally, Claude Code conversations hit the context cache, which costs 10% of full price—no need to reprocess the whole thing. But the installed version has a piece of code that modifies content every time you send a message. It's only supposed to touch the system config section, but if your conversation history happens to contain certain technical strings, it grabs the wrong spot, mutates the conversation content itself, and invalidates the cache. Your tokens get billed at full price for the entire context. Costs explode.

When does this hit you? If your conversation mentions Claude Code internals or technical terms, if those strings happen to appear in your Claude.md, or if you've read or pasted Claude Code source code.

How to avoid it? Launch with `npx @anthropic-ai/claude-code` instead of running the locally installed version.

**BUG 2: Resume Reprocesses the Entire Context**

The official `--resume` flag lets you pick up a previous conversation. Great feature in theory, but starting from a certain version, every time you use it, the first message rebuilds the cache from scratch, reprocessing the entire conversation history. If the previous conversation was already long, that single resume could burn 10%+ of your quota before you've even done anything. Subsequent messages go back to normal caching, but you pay this "entry fee" every time you resume. Do it five or six times a day and you're done.

How to avoid it? The pragmatic approach is to skip resume entirely—start a new conversation and paste in a summary from the previous one.

The comment that really stung Anthropic: "You have the most advanced model in the world, and it took a random Reddit user one afternoon to find bugs you couldn't."

## The Compounding Effect of 1M Tokens

Beyond the bugs, there's a structural problem. Someone posted a data analysis on Reddit titled "Data analysis of million-token context consumption—the compounding effect of context growth plus cache misses."

Before the 1M context window, conversations would auto-compress around 160k tokens. After 1M launched, that ceiling disappeared, and conversations easily ballooned to 500k. At that scale, a single short reply burns 500k tokens. If the model makes three tool calls, that's 1.5M tokens actually consumed.

Cache has roughly a 5-minute TTL. After it expires, your next prompt reprocesses the entire context at 10x the cached price. The miss rate didn't change (still around 2.5%), but with a much thicker context, each miss costs over 3x more.

I ran the numbers on my four most active projects:

- Project A had a conversation that never compressed, letting context balloon to 454k. If a single prompt triggered three tool calls, actual consumption hit 1.39M.
- Project B had a cache miss rate of 4.3%. That project required frequent breaks of 5+ minutes, so every return meant the entire context got reprocessed.
- Project C started after the 1M launch and never auto-compacted once—a bad habit that gets more expensive over time.
- Project D had the most conversations with thick average context per session. The takeaway: new task, new conversation.

## The 2.1.89 Fix

Version 2.1.89, released on April 1st. Boris said this update addresses the recent quota anomalies. Here's what I can see:

1. Fixed the cascading compression loop. Previously, a compression would immediately fill up again, triggering back-to-back compressions that spiraled into an infinite loop, burning API calls nonstop.
2. Fixed long conversations losing cache. Tool schema bytes were changing mid-session, invalidating the cache.
3. Fixed Claude.md being injected multiple times in long conversations after reading many files.
4. `/stats` wasn't counting subagent token usage, so users thought they were using fewer tokens than they actually were. Now it reflects the real numbers.

A late fix. But at least the truth is out.
