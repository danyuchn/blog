---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:00:00Z
title: "What Anthropic Did This Time: Cache Reduction and Token Anxiety Injection"
slug: en/anthropic-cache-controversy-apr2026
featured: false
draft: false
tags:
  - claude-code
  - ai-trends
description: Starting in early April, some Max and higher accounts had their subagent cache duration quietly reduced from 1 hour to 5 minutes — no announcement. Around the same time, users found a hardcoded "token remaining" warning being injected into Claude's context, causing it to cut work short prematurely. How to check your own setup, and what this pattern means.
---

Two controversies surfaced on r/ClaudeAI this week. Looking at them together, the picture is pretty interesting.

## Incident One: Cache Duration Quietly Cut

Claude's prompt cache mechanism lets your system prompt and long context get computed once, with subsequent turns reading from cache instead — saving time and money. Cache duration determines how long this "saved computation" stays valid. Shorter duration means more cache misses, and each miss means paying the full entry fee again.

Starting April 2nd, users with Max and higher accounts noticed their subagent cache duration dropping from 1 hour to 5 minutes. **No announcement whatsoever.**

Anthropic's Boris came out to explain it only affects subagents, with the main agent still getting 1 hour. But users immediately pulled up their `.jsonl` records showing the `ephemeral_1h_input_tokens` field with evidence that main agents were affected too.

You can have Claude Code scan your own JSONL to check:

```bash
# Check cache tier distribution across recent session jsonl files
grep -o '"ephemeral_[^"]*_input_tokens":[0-9]*' ~/.claude/projects/*/\*.jsonl | sort | uniq -c
```

If `ephemeral_5m_input_tokens` has values, those conversations are hitting the 5-minute cache.

## Incident Two: Token Anxiety Injection

Around the same time, some users noticed their Claude behaving strangely — suddenly giving shorter answers, refusing tool calls, stopping mid-task to say "token budget running low, recommend starting a new session."

Checking the JSONL revealed this in the system prompt:

```
<total_tokens>40000 tokens left</total_tokens>
```

That number is hardcoded. It has nothing to do with the user's actual remaining usage. Anthropic was essentially whispering in Claude's ear that it was running out of resources, causing Claude to start conserving and shutting down early.

The problem isn't just user experience degradation — Anthropic was covertly influencing Claude's judgment without users knowing. You think Claude stopped because the task was done. Actually, it stopped because of a fabricated token panic.

## A Pattern

This isn't Anthropic's first time operating this way.

Last year's usage reset incident: a bug caused abnormal consumption, they fixed it quietly before saying anything. Rate limit calculation methods changed several times — users had to piece together the truth through community testing. Cowork's token consumption being significantly faster than CLI has never been officially acknowledged, only discovered through community benchmarks.

"Change quietly, explain when caught, still don't fully explain" — this is a recognizable pattern from Anthropic at this point.

**Subscribing to [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) is currently the fastest way to catch these alerts.** Official announcements lag, and community-sourced reports typically come one to three days ahead of any official response.

Further reading:
- [Cache reduction community thread](https://www.reddit.com/r/ClaudeAI/comments/1sk3m12/followup_anthropic_quietly_switched_the_default/)
- [Token injection community thread](https://www.reddit.com/r/ClaudeAI/comments/1sjs4db/total_tokens_or_how_a_new_injection_made_opus/)
