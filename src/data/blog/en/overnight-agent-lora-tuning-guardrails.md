---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: "Letting an Agent Tune a Local Video Model Overnight: My Three Gates"
slug: en/overnight-agent-lora-tuning-guardrails
featured: false
draft: false
tags:
  - automation
  - ai-workflow
  - token-optimization
description: 'Three things I learned from letting an agent run local video-model parameter research overnight: hard constraints in CLAUDE.md, a gate script watching SSD writes, and a 30-minute check-in loop.'
---

A few notes from letting an agent run local video-model parameter research on its own overnight.

One, set hard constraints. When I was doing LoRA on a local video model, the problem with tuning parameters and changing the pipeline was that it blows out memory (my 48GB is entry level) and eats a lot of SWAP, which potentially damages the SSD. So I wrote a priority rule into CLAUDE.md: SSD protection > quality > speed. But that alone isn't enough. You also need a gate script watching SSD write throughput in real time, and the moment it goes over, it force-stops so the agent comes back and fixes things.

Two, each generation run takes about an hour or more, so lean on Monitor and a 30-minute loop. The cache on the Max plan lasts an hour. Come back every 30 minutes, check whether it's silently stuck, spot-check whether the finished clips look wrong. That way you don't lose the cache and get billed full price for the whole context again.

Three, once those two things are set up, tell it not to wait for my decisions: try as many directions as you can until 6am (when I get up). So it set up a gate script that hard-stops at 5:30. It also created an md and a json file recording results, so everything can be traced afterwards.

I woke up and moshed back in from my phone.

![Terminal screenshot from a phone moshed into the Mac mini, with the agent reporting everything stopped, 5.99 TB of cumulative SSD writes, and a list of deliverables](/blog/assets/posts/overnight-agent-lora-tuning-guardrails/1-overnight-run.jpg)

It had shut itself down cleanly at 05:06, 24 minutes ahead of the 5:30 deadline: processes cleared, cron removed, hard-stop timer released, SSD Percentage Used 0%, cumulative writes 5.99 TB. The finished clips were in `~/Downloads/comfyui-短劇成果-20260731/`, with five side-by-side evolution versions and second-by-second screenshots, plus three rules written into `KNOWN_ISSUES.md`.

One `/goal` and I don't mind at all letting it run all night on something that isn't urgent. You can add one more constraint to the goal: verification goes through a sol subagent, and you're only allowed to stop when it says you passed. That gets you quality and cheapness at the same time.

As for why I bother making rules for the SSD's sake, go look up SWAP and SSD writes & lifespan. It's going to be quite a read.

<!--
新增非原文句子清單（忠實度自首）：
1. 「早上醒來，手機 mosh 連回去看。」／"I woke up and moshed back in from my phone." — 類型：銜接（原貼文於「晚上的實驗成片都放在」處被截斷，改以圖片內容承接；mosh 與手機為圖片可見事實）
2. 「它在 05:06 就自己停乾淨了…累計寫入 5.99 TB。」／"It had shut itself down cleanly at 05:06…cumulative writes 5.99 TB." — 類型：銜接（純陳述圖片上可見的回報內容）
3. 「成片放在 ~/Downloads/comfyui-短劇成果-20260731/…寫進了 KNOWN_ISSUES.md。」／"The finished clips were in…written into KNOWN_ISSUES.md." — 類型：銜接（純陳述圖片上可見的交付物清單）
4. 「至於為什麼要為了 SSD 立這種規矩——」／"As for why I bother making rules for the SSD's sake —" — 類型：銜接（把 08-05 那則回覆接進本文語境，該則原話逐字保留）
5. 三個段落開頭的「一、」「二、」「三、」／"One," "Two," "Three," — 類型：框架句（原貼文即為 1./2./3. 編號）
-->
