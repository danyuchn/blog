---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-16T00:01:00Z
title: "The Dumb-User Benchmark: Why Scores and Real Use Feel So Different"
slug: en/benchmark-vs-real-use-dumb-user-test
featured: false
draft: false
tags:
  - model-comparison
  - opinion
description: 'A model''s benchmark score and what users actually experience can be wildly different. Three reasons, the "dumb-user benchmark" I want someone to build, and how GPT 6 has felt in real use.'
---

Why is the gap between a model's benchmark score and what users actually experience sometimes so huge?

I think there are a few reasons:

1. In real work, people don't write tidy, standard prompts. They ramble, skip the parts they should say, leave out a ton of context, and can't fully spell out what they want.
2. A big part of benchmark scoring is "one-shot completion rate." But real-world development isn't always about getting it right in one step. It's about adjusting as you go, the "point and it hits" feeling, and a pure score can't measure that.
3. In a benchmark the context is clean and the harness is as tidy as a cleanroom. A real user's harness is usually a mess, and the context can get polluted or contradict itself. How well a model holds up against messy context matters a lot.

And I think these three points are exactly what separates GPT 6 from Claude.

## The dumb-user benchmark

Someone should design a dumb-user benchmark. Take the beginner who is worst at writing prompts, give them the messiest job, and see whether the model can still make them go "Wow! You actually knew that's what I wanted." That model is the god-tier one. Right now Opus 5.5 has reached that standard (as long as it isn't nerfed).

## How GPT 6 actually feels

Here's how GPT 6 has felt to me.

I don't know how much longer I can last on these 28 days. I feel like I'm out of options.

I'm genuinely curious whether the base model was trained badly or the codex harness is just terrible. How do you end up with a coward of a model with no taste, painfully mediocre, no opinions of its own, timid, stuck splitting hairs, stubbornly literal, swallowing the user's judgment, and full of blame-dodging talk? And on top of that, it's slower than my local model.

GPT 6 is just a very dull model:

- Defensive writing that drives you crazy
- Too focused on local correctness, ignoring the big picture
- Completely afraid to show its own opinion or make a call
- It even swallows the user's judgment and business logic

This video says exactly what I feel: [【GPT 6 Astra：一个平庸、沉闷、没有品味的模型-哔哩哔哩】](https://b23.tv/jI8mILu)

I also wrote a separate post on why GPT 6 feels dumb: [Why GPT 6 Sol / Luna Feel So Dumb](/blog/posts/en/why-gpt6-sol-luna-felt-dumb/).

One more thing: the subscription Astra today and the Astra at launch are two different things. Someone on X measured the juice value (thinking budget). Astra through the API: 700-something. The subscription: 20-something. So my advice: cancel and switch to Claude...

For anyone who connects the API to a third-party coding agent, come share: how do the external Astra / Sol perform?

I've been reduced to asking Opus to clean up the mess...

<!--
新增非原文句子清單（忠實度自首）：
1. 「蠢人 benchmark：跑分跟實際體驗為什麼差那麼多」（標題，英文為在地化翻譯） — 類型：框架句
2. description 一句 — 類型：框架句
3. 「## 蠢人 benchmark」「## GPT 6 的實際體驗」兩個小標（英文：The dumb-user benchmark / How GPT 6 actually feels） — 類型：框架句
4. 「下面是我自己用 GPT 6 的感受。」（Here's how GPT 6 has felt to me.） — 類型：銜接
5. 「另一篇專門聊 GPT 6 為什麼讓人覺得笨：[連結]。」（含自擬連結標題） — 類型：框架句
6. 「還有一件事：」（One more thing:） — 類型：銜接
7. 「所以我的結論是，退訂改 Claude⋯」（原文僅「退訂改claude⋯」；前綴為新增） — 類型：銜接
8. 改寫：原貼文 (3) 的換行句改為條列；(2)(3)(4) 順序重排並併入同一段落流；移除 emoji；「出來分享」提問移到文末前。 — 類型：改寫
-->
