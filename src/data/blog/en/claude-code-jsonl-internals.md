---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T15:30:00Z
title: "Digging into Claude Code's JSONL: Manual Context Usage, Cache Types, and Compact Detection"
slug: en/claude-code-jsonl-internals
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - developer-experience
description: Claude Code's `/stats` only tells you the total token count, but the JSONL files hide a lot more—cache types, compact triggers, image-triggered cache misses. Here are the useful formulas I collected while building cc-audit.
---

Claude Code's `/stats` tells you "this session used X tokens," but that's an aggregate—it buries a lot of useful detail. While building the [cc-audit skill](/blog/posts/en/cc-audit-skill), I went through the JSONL format end-to-end and found a handful of really useful metrics hiding in plain sight, as long as you know where to look.

The JSONL lives at `~/.claude/projects/<project-name>/<session-id>.jsonl`. Each line is a JSON object representing one message or system event.

Here are the formulas I pulled out.

## 1. Context Usage Formula

To see how thick your session has gotten, don't just look at `input_tokens`—that's just "new content sent this turn." You have to include the cache portions.

```
context_usage = (input_tokens + cache_creation_input_tokens + cache_read_input_tokens) / 200000
```

The numerator comes from the `usage` field on assistant messages. The denominator is Claude's current 200k context window.

When this value gets close to 1, you're hitting the wall—time to `/compact`, `/clear`, or start a new conversation.

## 2. Telling Cache Types Apart: 5-Minute vs. 1-Hour

Claude's prompt cache has two expirations: 5 minutes for Pro, 1 hour for Team/Enterprise. You can tell which one you're hitting by inspecting the `usage` field:

```
cache_creation:
  ephemeral_5m_input_tokens: <number>   # Pro
  ephemeral_1h_input_tokens: <number>   # Team/Enterprise
```

If you're on Pro and see `ephemeral_1h_input_tokens`, congratulations—it's either a bug or a hidden perk, depending on your mood. The reverse also applies.

## 3. Detecting `/compact`

`/compact` leaves a trace: it writes a `type=system` message with a `summary` keyword. A grep catches it:

```bash
grep -c '"type":"system".*summary' session.jsonl
```

`/clear` is trickier—it leaves no trace, because it just opens a brand new session file. If you want to count "how many times I cleared today," you have to look at the filesystem level ("how many new JSONL files showed up in this project today") rather than parsing a single file.

## 4. Detecting Image-Triggered Cache Misses

This is the most practical formula I found this week. Everyone knows pasting an image can nuke the cache, but how do you confirm "this particular cache miss was because of the image I just pasted"?

Combine two conditions:

1. The previous `user` content contains an `image` type block.
2. The next `assistant` message has `cache_read_input_tokens` < 500.

If both match, you can be almost certain the miss was image-triggered. 500 is my empirical threshold—normal session cache_read is usually in the thousands or tens of thousands, so dropping below 500 means the cache was rebuilt from scratch.

Once you know this, two things follow. First, avoid pasting images into long conversations—if the image matters, start a new conversation for it. Second, you can run the numbers after the fact: "how many images did I paste this week, and how much cache rebuild did they cost me?" I ran this once on my own data and it convinced me to crop screenshots to the minimum before pasting them in.

## 5. Session Kickoff: Memory vs. Filesystem Trap

This one isn't a JSONL parsing formula—it's a behavioral trap I walked straight into yesterday.

I had a session miss three untracked new files in a row (a video meeting transcript, a client proposal draft, and a Slack DM archive). I'd only read the memory index and jumped into analysis—which ended up reading like fiction, because memory is an index, it goes stale, and the filesystem is the source of truth.

Takeaway: **If `git status` shows `??` or `M` files at session start, Read them before doing anything.** I added this as a hard rule in my `~/.claude/rules/common/task-execution.md`.

Memory is a hint, not source of truth. This is the kind of trap that's easy to dismiss and easy to fall into again.

## Closing

`/stats` is just the entry point. The real detail lives in the JSONL, and everything is grep-able and Python-parseable. My [cc-audit skill](/blog/posts/en/cc-audit-skill) already bundles all this logic, but if you want to hack on your own, the five formulas above should get you started.

Claude Code is an open system—all the data is on your own disk, in a documented JSON format. Learning to mine it is a hundred times more useful than just reading `/stats`.
