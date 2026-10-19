---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-19T04:00:00Z
title: I Asked My AI "Now What?" 41 Times in Two Weeks
slug: en/progress-asks-status-board
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - harness
description: 'Letting an AI run long jobs in the background is easy. Knowing where it got to when you come back is not. I counted two weeks of my own messages and found I was missing a status board, not more monitoring.'
---

I often leave Claude working while I'm away from my desk. I once jotted down my four tricks for that: dispatch more subagents, use the history-find skill to dig up old sessions, set a /loop 30m tick so it polls on its own, and check /status to see where each session's tokens went. In rainy season I even had Codex watch the Bangkok city weather office's page, and ping me whenever it judged a 50%+ chance of rain within the hour, so I could run out and bring the laundry in.

Getting the AI to keep working on its own is easy now. When I come back, though, I often have no idea how far it got.

## How many times I actually asked

A few days ago I had Claude go through every message I typed over two weeks and count what I kept repeating. From October 1 to 19, I typed 1,053 messages myself. 41 of them asked about the progress of background work.

32 of those were under 20 characters. "Now what?" "How's it going?" "Has it stalled?" "Now what? Why aren't you tracking it yourself?"

The funny part: 12 of them came after I had already told it to set up monitoring.

## Push notifications got fixed, the asking didn't stop

On October 15 I fixed a push notification bug. My two machines shared one push ID and kept kicking each other off, so completion notices often never arrived. After the fix, the "I never saw your report" complaints stopped completely.

The progress questions didn't drop. Before the fix I asked 2.07 times a day. After, 2.4.

When I split them up, I was asking three things: when will it finish, has it stalled, and where's the report. Notifications only answer the last one. There was nowhere to look for the first two.

## What I was missing was a status board I could read myself

So I built a tiny job registry. Every long-running job checks in when it starts, again after each batch, and once more when it ends. When I want to know what's going on, I run one command and get one line per job: how many items done, estimated finish time, and how many minutes since it last checked in.

If the process dies or goes quiet for too long, the registry marks it as stuck and sends one notification, then stays quiet. A broken registry is not allowed to take the real job down with it either. If a write fails, it skips silently.

Monitoring is the AI watching things for itself. I can't see what it's watching, so I keep asking. A status board is something I can read. Next I'll hook it up to the batches I run most, then count again and see if I still ask.

That's it.

<!--
AI-added sentences (faithfulness disclosure): same list as the zh version. Source material is the author's two micro-notes (four tricks for leaving the desk; radar-echo watch), the author's own message quotes, and counted figures from the 2026-10-19 repeat-work audit.
1. "Getting the AI to keep working on its own is easy now. When I come back, though, I often have no idea how far it got." (framing)
2. "The funny part: 12 of them came after I had already told it to set up monitoring." (transition; figure is counted)
3. "When I split them up, I was asking three things ... nowhere to look for the first two." (rewrite; categories from the audit)
4. The "So I built a tiny job registry" section (rewrite; describes what jobreg.py actually does)
5. "Monitoring is the AI watching things for itself ... A status board is something I can read." (framing; core claim, marked as inference in the audit)
6. "Next I'll hook it up to the batches I run most, then count again and see if I still ask." (framing; the registry is not wired in yet, which is true)
-->
