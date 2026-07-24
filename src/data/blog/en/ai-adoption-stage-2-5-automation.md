---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: I'm Stuck at Stage 2.5 of AI Adoption
slug: en/ai-adoption-stage-2-5-automation
featured: false
draft: false
tags:
  - ai-workflow
  - claude-code
  - productivity
description: 'After watching Boris Cherny break down the stages of AI adoption, it hit home: I''m stuck at stage 2.5, where limited attention plus low trust becomes a vicious cycle. This week I used late-night schedules, a morning dashboard, and herdr auto-spawning sessions to cut a 4-5 hour workflow down to 1-2 hours.'
---

Last week I watched the bald guy from Claude Code talk about "the different stages of AI adoption," and it really struck a chord. I'm sitting right at stage 2.5. I run 5-10 agents at once, but I've already run into two bottlenecks.

## Two bottlenecks

First, my attention is limited. When 5-6 of them take turns asking me to review their work, I get too involved and can't keep up.

Second, I don't trust them enough. I can't bring myself to just let them all run on their own, so I still set a lot of human-intervention checkpoints.

Put those two together and you get a vicious cycle.

## What I started changing this week

So this week I started trying to change things.

First, I set up several late-night schedules that scan my knowledge base every day for overdue todos and things due the next day, knock them all out, and leave branches for me to review in the morning. What's actually running in the background includes the upkeep of my "nightly trio": I cranked up the difficulty on all five gym quiz questions and switched every answer over to program-based verification; I swapped the debate club's judge from gemma3:4b to Gemma 4, because gemma3:4b kept getting the gym's own logic questions wrong yet was the one judging logic debates, which made it hard to trust; and while I was at it I fixed the ffmpeg snag that had been keeping the radio station from producing audio. This isn't just talk. There's genuinely stuff running through the night.

Second, at 6am it auto-generates a dashboard that lists the branches waiting for my review, the items that are outward communication rather than file changes, and a briefing to get me up to speed.

Third, I have an agent read that dashboard, then use herdr's "agent auto-controls the terminal" feature to automatically open a session for each item that needs human review, and I go interact with those sessions.

In practice, work that used to take 4-5 hours of collaborating with agents now gets resolved in 1-2 hours. And the quality of what ships out hasn't dropped.

The next step should be to push automation and trust even further, let them each dispatch their own subagents, and raise the efficiency of getting things done in parallel.

<!--
新增非原文句子清單（忠實度自首）：
1. "What's actually running in the background includes the upkeep of my "nightly trio": I cranked up the difficulty on all five gym quiz questions and switched every answer over to program-based verification; I swapped the debate club's judge from gemma3:4b to Gemma 4, because gemma3:4b kept getting the gym's own logic questions wrong yet was the one judging logic debates, which made it hard to trust; and while I was at it I fixed the ffmpeg snag that had been keeping the radio station from producing audio." — 類型：佐證（取自 2026-07-23/24 daily note night-fun 維運紀錄，非 Threads 原文；作為深夜排程的具體實例）
2. "This isn't just talk. There's genuinely stuff running through the night." — 類型：銜接（承接上句佐證，收束回原貼文的深夜排程論點）
-->
