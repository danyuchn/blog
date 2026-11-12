---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: "The Resource Paradox: From Stalling Old Laptops to the Real Baseline for Local AI"
slug: en/cli-resource-paradox-local-models
featured: false
draft: false
tags:
  - teaching
  - non-engineer
  - ai-tools
description: 'Many put up with aging laptops down to 1.8 GB of storage churning through swap, while dreaming of running local LLMs on a NT$5,000 machine. A look at the resource paradox, realistic hardware baselines for modern local models, and how to weigh usable speed against machine upgrades.'
tldr: 'When older computers struggle with sluggish performance, users often consider running local AI models but hold unrealistic expectations about hardware. Smoothly running a mainstream medium model requires adequate resources, such as 48GB RAM for 20 to 30 characters per second; investing in necessary hardware upgrades is better than struggling with underpowered machines.'
---

Teaching tech skills turns up a fascinating contradiction. When a machine is choking on memory and storage, a command-line interface (CLI) is hands-down the best fix—it consumes a tiny fraction of the resources a graphical interface demands. Yet in practice, the people whose computers need that relief the most are precisely the ones least likely to ever touch a terminal.

I don't mean that disparagingly. It comes straight from seeing it over and over in the classroom: recycling bins that have never been emptied, desktops buried under a carpet of screenshots, two-year-old installers still sitting quietly in Downloads, and a hard drive clinging to its last 1.8 GB of free space. RAM is buried under swap thrashing, and the entire laptop crawls at a painful snail's pace.

And right when system resources hit rock bottom and the OS is gasping for air in swap hell, the question people turn around and ask is almost always the same: if I want to run AI models locally on my own machine, how beefy does my hardware actually need to be?

## The Myths and Wild Fantasies of Local AI Hardware

Ask what hardware you need to run local models, and the honest answer depends heavily on what you already own. Often the bar isn't nearly as high as people assume. But browse any online forum, and you'll find discussions immediately polarizing into two bizarre extremes.

The first extreme mistakes "it actually loaded" for "it runs well." Over on Reddit, someone proudly shared getting DeepSeek V4 Flash to run on 16 GB of RAM, claiming the speed was pretty decent—at 33 sec/tok (watch the units closely).

An even wilder take came from a recent viral joke in Taiwan: a post claiming Google engineers should learn the "proper way" to do AI from vocational high schoolers, supposedly running local LLMs on a NT$5,000 machine. If that were remotely true, Taiwan's stock exchange, SK Hynix, and Samsung would be cratering off a cliff next Monday.

## The Real Baseline for Everyday Local Models

Jokes aside, everyday local models don't require magic budget hacks, nor do they demand a server rack.

Right now, Qwen 3.6 27B and the 35B A3B MoE are widely regarded as some of the most cost-effective local models around. Take the 3.6 27B Q4 quantized build: an M4 Pro Mac with 48 GB of unified memory runs it comfortably at around 20 to 30 tok/s.

The open-weight ecosystem is moving fast, too. Just the other day, the Qwen team announced their next wave of open weights on social media, as shown in their post:

![Qwen official account on X announcing Qwen3.8-Max open weights, with the sentence "We will release the open weights of Qwen3.8-Max next week, and Qwen3.8-27B will also be released to meet everyone" highlighted, listing selling points below like autonomous coding, long-horizon mastery, native multimodal, along with pricing at $2.0 input and $6.0 output per million tokens.](/blog/assets/posts/cli-resource-paradox-local-models/1-27b-open-weights.jpg)

That upcoming 27B release is particularly exciting. Once those open weights land, hopefully the community quickly puts together quantized versions, and ideally we'll see compact MoE variants follow soon after.

## Computers Are Productivity Tools: Upgrade When It Counts

That brings us to the underlying question everyone ultimately faces: should you actually buy or upgrade a machine just to run local models?

As for buying a machine specifically for this—hardware is only getting pricier. An M4 Pro Mac mini with 48 GB of RAM was going for around NT$50,000 back in May; check today, and prices have shot closer to NT$90,000. Turns out that line about computers holding their value wasn't lying.

The real test is simpler: a computer is a productivity tool meant to get work done. If the machine on your desk is already a choked-up potato with an overflowing trash bin and 1.8 GB of free disk space, it's already failing you in day-to-day work, let alone running local AI. If you want a machine that won't choke on your daily work—and can actually run models locally—just buy the upgrade when you need it.

## Appendix

Here is a summary of the model speeds and hardware specifications mentioned above:

- Benchmark Cases and Speed Units:
  - DeepSeek V4 Flash on 16 GB RAM: Clocked at 33 sec/tok (33 seconds per single token—notice it is seconds per token, which is practically unusable).
  - The rumor of "running local LLMs on a NT$5,000 machine": The author dismissed this with, "If that were true, Taiwan stocks, SK Hynix, and Samsung would crater next Monday."
  - Qwen 3.6 27B Q4 quant on M4 Pro (48 GB RAM): Roughly 20–30 tok/s (generating 20–30 tokens per second, making it genuinely usable for daily workflows).
- Mainstream Models and Open-Weight Updates:
  - Qwen 3.6 27B and 35B A3B: Widely regarded as the sweet spot for cost-effective local deployments.
  - Official Qwen Announcement: Teased next week's release of open weights for Qwen3.8-Max and Qwen3.8-27B, highlighting autonomous coding, long-horizon mastery, and native multimodality, with reference API pricing at $2.0 per million input tokens and $6.0 per million output tokens.

<!--
新增非原文句子清單（忠實度自首）：
1. 「有人問跑本機模型要什麼硬體。」 — 類型：銜接（原為回覆語境，改為一句情境交代）
2. 「前幾天 Qwen 宣布下一批開放權重，」 — 類型：銜接（原貼文僅「期待！！！」加圖，補一句圖片來源交代）
3. 「至於要不要為了這些買電腦——」 — 類型：銜接（原為回覆他人購機討論，改為一句轉場）
4. 圖片 alt 文字 — 類型：改寫（描述截圖內容，非作者原文）
5. 「更極端的例子，是前陣子的笑料承包：」 — 類型：併入碎念（Google 工程師的正確姿勢，2026-08-14 週報併入）

2026-10-26 拼接順稿：
- 「說到電腦資源與 SWAP，大家接著最常問的就是：如果想在自己電腦上跑本機模型，硬體到底要多好？」— 類型：銜接
- 「開完玩笑，認真講主流模型的話：」— 類型：銜接
增加 H2 章節標題理順層次，並在接縫處以過渡句銜接資源吃緊與本機模型硬體討論。

2026-11-12 舊文盤點整篇重寫：
以電腦資源吃緊的認知悖論破題，串聯社群對本機模型的極端幻想與主流規格的真實門檻，將技術細節獨立收攏至附錄，形成連貫的硬體判準與生產力投資觀點。
-->