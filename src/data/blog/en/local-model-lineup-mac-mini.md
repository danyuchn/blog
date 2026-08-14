---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: My Local Model Lineup on a Mac mini, Plus Three Bad Habits I'm Owning Up To
slug: en/local-model-lineup-mac-mini
featured: false
draft: false
tags:
  - ai-tools
  - model-comparison
  - open-source
description: 'Ten days of offline models on a 48GB Mac mini M4 Pro — the picks, the task split, a terrifying swap write rate, and three bad habits I admit to.'
---

## I Announced the Lineup in Classical Chinese

On the morning of 25 July I posted my local-model verdict on Threads, written in Classical Chinese. Here is the post exactly as it went out:

> 今宣鄙見，歷旬試諸離線文模，較其短長；蘋果迷你機 M4 強化之軀，四十八吉內存之器，眾模紛陳，實用首推通義千問三點六三十五億參數三壓縮本。
> 預載文辭，百三十七字流於一息；逐句推演，五十字出於片時。速率從容，尚可容受。單獨之務可憑，數標滌清可仗，圖文辨字無礙，夜間批運相宜，淺層自主循環，一應雜功咸洽。
> 若夫裁章構筆，鋪辭抒翰，則羽禽三十五億之模，文氣渾融，語態天籟，遲速與前型相埒，故置為次選，以備緩急。
> 至若聲音轉錄，離線辨言，純漢之語，取通義千問三代聲識之型；漢英相參之響，用跨語辨聲之術。
> 其圖像甄別、聲音寫錄、數據整標諸役，不關密隱，悉付星圖輕捷雲模。值廉算力豐，繁瑣細務，一皆委託。此類素材本無私忌，縱取中土文模商用接口，亦無妨礙，特以私衷所好，遂擇此雲端之器而已。

In plain terms: the machine is a Mac mini M4 Pro with 48GB of memory. After about ten days of trying offline models from various vendors, my daily driver is the 3-bit quantized build of Qwen3.6-35B-A3B. Prefill runs at 137 tokens per second, token-by-token generation at 50. That speed works for me.

What it can carry: single tasks, data cleaning and labeling, OCR, overnight batch jobs, shallow autonomous loops, all the odd jobs. When I need to write an article or work on prose, I switch to Ornith-35B. The writing flows better, the voice sounds more natural, and the speed is about the same as the first one, so it sits as the backup pick.

## Which Model for Which Job

Speech transcription splits two ways: Qwen3 ASR for pure Chinese, and a cross-lingual recognition setup when Chinese and English are mixed.

As for image recognition, speech-to-text, and data cleanup and labeling, none of which touch privacy, I hand all of it to Gemini Flash in the cloud. Cheap, plenty of compute, and the tedious stuff gets outsourced. This kind of material has no privacy concerns to begin with, so even a commercial API from a Chinese model house would be fine. I just happen to prefer this cloud option.

Someone asked what local models are actually good for. My list: speech transcription, periodic knowledge-base cleanup and link repair, OCR, data de-identification, video generation (very challenging, still trying), and music and image generation (far better than I expected).

There's also one trick on the model-selection side. Gemini is the strictest about recitation errors (the guardrail that halts generation when a model starts reciting copyrighted content), and Qwen is the loosest. So running Qwen through a US-based provider on OpenRouter is the best answer: deployed in a US data center, so the data never goes to China, and the model only blocks politically sensitive content, not copyright.

## The Real Bottleneck Isn't Model Choice

Over the last days of July I kept writing the same conclusion into my dev log. I ran three head-to-head tests of A3B against Ornith and ended up sticking with the original pick. The methodological takeaway: the bottleneck is the quality of the evidence you feed in, not which model you pick.

The same batch of logs holds two other trip-ups. One: qwen3-coder:30b was already retired, but its schedule was still running every night, and it took three consecutive nights of zero-score output before I noticed. Two: qwen3.6:27b is also retired, and separately, setting num_predict too small truncates the thinking trace.

## Hardware and Cost, Realistically

On the morning of 31 July I was watching swap. The day before I'd accidentally loaded two models at once, burned through a pile of swap, and the SSD was writing at 1TB/H. Scared the life out of me. Now I watch swap usage strictly.

The Mac mini M4 Pro migration did hand me one pleasant surprise. Machine-to-machine transfer with Migration Assistant carried the TCC permissions across, which saved me re-authorizing everything one by one.

On the cost of the machine itself: Mac mini M4 Pro with 48GB. I paid a bit over NT$50,000 in May including AppleCare, and that was pre-price-hike plus employee pricing. Go look now and it's over NT$90,000. A computer is a production tool, and the line about still holding its value after a few years turns out to be true.

If anyone asks whether they should run local, here's my advice. For cloud models, 8GB is enough. For local models it depends on your specs. But first be clear about why you want local. For privacy, that's reasonable. To save money, not so much, because getting local output comparable to a commercial model means spending on hardware first. Don't overthink local at the start. Get fluent with the ordinary closed-source models first.

## Three Bad Habits

On the night of 30 July I confessed on Threads what these two weeks had turned me into. The original post, in Chinese:

> 這兩週 弄來Mac Mini + 開始玩本地模型 + Anthropic/OpenAI 大玩重置後，才發現我身上有三大劣根性：
>
> 1. 慣老闆：
> 半夜睡覺也要操Mac，設了一堆本地模型排程讓他處理任務。如果有空檔？那就去擁抱臉拉幾個下來跑Benchmark測試
>
> 我女友問說書房怎麼比以前熱，我不知道是不是該回他因為一直在跑模型
>
> 2. 免費蕭貪仔：
> 反正拉開源模型不花錢，儘量拉儘量測！反正Mac Mini的耗能少到可以忽略...
>
> 3. 吃到飽不吃撐不甘心：
> 重置給我的額度沒用完我會遺憾到錘心肝，所以一reset就開始猛用，這個月token假設用API算已經破萬美金...
>
> 以上三個劣根性，反省中

For English readers, the three habits are: (1) 慣老闆, the sweatshop boss: I work the Mac even while I sleep, with a pile of local-model schedules handling tasks; if there's an idle slot, I go pull a few more models off Hugging Face to benchmark. My girlfriend asked why the study is hotter than it used to be, and I'm not sure whether I should tell them it's because models are running non-stop. (2) 免費蕭貪仔, the freebie glutton: open-source models cost nothing to pull, so pull as many as possible and test as many as possible; the Mac mini's power draw is negligible anyway. (3) 吃到飽不吃撐不甘心, the all-you-can-eat compulsion: if I don't use up the quota a reset hands me, I regret it enough to 錘心肝 (pound my chest); so the moment it resets I go hard, and this month's tokens would have passed ten thousand US dollars on API pricing. Reflecting on all three.

A few days back someone brought up small models under one of my posts, and I replied: smart. Everyone's racing on big models right now, but small models are what blooms everywhere in the future.

<!--
新增非原文句子清單（忠實度自首）：
1. 「On the cost of the machine itself:」 — 類型：併入碎念（The Mac Mini Holds Its Value, No Joke，2026-08-14 週報併入）
-->

