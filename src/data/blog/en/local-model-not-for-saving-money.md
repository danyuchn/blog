---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: Running Local Models Won't Save You Money
slug: en/local-model-not-for-saving-money
featured: false
draft: false
tags:
  - ai-tools
  - opinion
  - ai-economics
description: 'If you''re buying hardware to run local models just to save money, do the math with me first: capable rigs start at NT$100k, commercial models are priced to the bone, and privacy is the only irreplaceable edge left.'
tldr: 'Buying hardware to run AI at home just to save money rarely pays off. Capable setups cost at least NT$100,000 plus electricity, while commercial cloud AI is far cheaper—save local hardware strictly for stripping sensitive data before sending work to the cloud.'
---

If you're an individual consumer looking at buying hardware to run local models just to save money, take a pause. Let me do the math with you first.

## The Real Cost of Running Agentic Models on Consumer Hardware

If you want consumer hardware to handle local models with general agentic capabilities, you first have to accept sluggish speeds and a noticeable drop in intelligence. Hardware alone will easily set you back at least NT$100,000, not to mention ongoing electricity costs. Put plainly: how is a home setup supposed to out-compute a dedicated data center?

This needs to be separated from what I wrote in [The Machines That Need the CLI Most Belong to People Least Likely to Learn It](/blog/posts/en/cli-resource-paradox-local-models). That post was about the baseline for running small-parameter models, and that bar really isn't high. This post is about how much money you have to sink to run models with general agentic capabilities. Those are two completely different problems.

## The Extreme Value of Commercial Cloud Models

If your goal is just having models handle everyday grunt work, there have long been far cheaper options on the market. Commercial providers have already fought their way to rock-bottom prices.

Take the market when I jotted this down: GPT 5.6 Luna was the cheapest and excelled at browser and computer-use tasks. Gemini 3.7 Flash felt slightly stronger to me than Sonnet 5 at half the price, came with native audio and video multimodality, and the quota was essentially a freebie bundled with cloud storage. You could never burn through it all, and running it all night wouldn't hurt your wallet. At these price points, I didn't even see a reason to chase cheaper Chinese providers.

![The launch announcement for Gemini 3.7 Flash, already integrated into Claude Code](/blog/assets/posts/local-model-not-for-saving-money/1-gemini-37-flash-release.jpg)

This screenshot shows the announcement when Gemini 3.7 Flash launched and hooked into terminal tools, demonstrating that models at the time were already capable enough for production work. (Postscript, 2026-10-20: This model has since been deprecated; check Google's official page for the latest lineup.)

## A Hybrid Architecture for Local and Cloud Work

The only truly irreplaceable advantage of a local model is protecting confidential data.

If you genuinely have that need, buying hardware that just barely handles a small redaction model is more than enough.

Let confidential data get scrubbed by a local model while your computer sits idle overnight, hand it off to commercial cloud AI during the workday, and restore it locally afterward. That is the setup that actually pays off.

If you need data redaction, take a look at this open-source project: <https://github.com/danyuchn/pii-guard>. The idea is simple: use pattern rules to strip out most common personal data first, then let a small local model sweep for whatever slipped through. Even if hardware constraints keep you from running a massive frontier model, this combo is plenty to get the job done cleanly.

## Three Data Traps When Benchmarking Local Models

While running side-by-side benchmarks on local models over the past few days, I stumbled into three pitfalls in a row. They all pointed to the same issue: you think you're benchmarking a local model, but you're actually misreading the numbers.

The first trap is comparing mismatched older columns. If you compare benchmark runs from different batches just because the column names match, you miss the fact that the underlying test questions changed between runs. That single mistake overturned six separate conclusions in my own tests—including falsely believing two models were dead even on total throughput (one was actually 16.5% faster), and thinking another model was 3.2x slower (the real gap was only 4%).

The second trap is treating the maximum value as an overall capability score. If a benchmark column records the peak score across a run, it silently skips over earlier questions that failed entirely. One model's recorded score of "5" only had a single clean run behind it; comparing that 5 against other models ended up reporting a full round of fake numbers. On the flip side, if you use a ladder approach that halts at the very first failure, a single snag will skip all subsequent questions and severely underestimate the model. To fairly evaluate capability, you have to fill out the grid completely on both sides. Filling out only one side is a double standard.

The third trap is misjudging real compatibility with simple endpoint probes. If you only send test requests with system prompts, tool definitions, and streaming outputs to an endpoint, a normal response might make you think an earlier compatibility issue was fixed. But once you run it inside an actual workflow with a tool-calling loop, you find out the bug only triggers on the specific code path that auto-generates a tool parser—a path a simple endpoint probe never touches. The only compatibility check that counts is a real, end-to-end run.

Before you decide whether to drop NT$100,000 on new hardware, take a cold, hard look at whether the numbers behind your decision are even real. Keep your hardware budget for your true privacy perimeter, and leave daily workloads to high-value commercial cloud models. That's how you avoid the self-hosting money pit.

I later broke down the math in a short video, "Buying Hardware to Run Local Models Doesn't Actually Save Money": <https://youtube.com/shorts/8TP4HssU0Ow>

(The first draft of this article was compiled from test logs and reflections in August 2026. Specific commercial model names mentioned were market examples at the time.)

## Appendix: Technical Implementation Details for Benchmark Verification and Redaction Tools

Here are the specific technical details behind the benchmark fixes and redaction setup mentioned in the post:

- Baseline question version verification: When comparing different models side by side, if the prompt token counts for shared cells don't match, reject the comparison outright. Because both models share the same tokenizer, the token count for the exact same prompt cannot differ; mismatched numbers mean the question set was altered.
- Endpoint compatibility verification: Compatibility only counts in production runs, not curl probes. In practice, you have to execute the complete workflow using `claude -p` with an active tool loop to verify whether the abnormal path for auto-generating a tool parser gets triggered.
- Hybrid redaction mechanism: The redaction tool at <https://github.com/danyuchn/pii-guard> combines regex with a small local model. Regex handles the bulk of the redaction first, leaving the small local model to catch any edge cases that slipped through. Even if hardware limits keep the model from being exceptionally capable, this setup easily accomplishes the task.

<!--
新增非原文句子清單（忠實度自首）：
1. 「這裡要跟我之前寫的〈最需要 CLI 的電腦，主人最不可能學會 CLI〉分開看。那篇講的是跑得動小模型的門檻——那個門檻確實沒那麼高。這篇講的是跑得動有綜合 agentic 能力的模型要花多少錢，是兩個不同的問題。」 — 類型：框架句（依編輯指示明確區分兩篇語境，避免製造矛盾）
2. 「我這幾天在做本機模型的橫向評測，連續踩到三個坑，全部指向同一件事：你以為在評測本地模型，其實在讀錯數字。」 — 類型：框架句（把三條日誌速記接上本篇主線）
3. 「第一個坑是舊欄位。」／「第二個坑是我拿來當「能力值」的那個欄位，其實取的是最大值。」／「第三個坑是我用 curl 打端點驗相容性。」 — 類型：銜接（日誌條目改寫為可讀段落的引導句）
4. 「兩個模型共用同一套 tokenizer，同一題的 token 數不可能不同，數字對不上就必然是題目被改過。」 — 類型：改寫（日誌原文「兩模型共用 tokenizer…數字不同必然是題目不同」的白話化）
5. 「三個坑加起來的意思是：在你決定要不要花十萬塊之前，先確認你手上那組決定要不要花錢的數字是真的。」 — 類型：框架句（收束，把評測節接回硬體成本論點，不新增結論）
其餘段落逐字或近逐字保留自 Threads 原貼文（2026-08-14 15:59 與 16:01 兩則）。

2026-10-26 拼接順稿：
無新增過渡句。
（將 Gemini 3.7 Flash 的淘汰後記移至對應章節圖片說明下方，並移除文末短片連結的「補記：」字樣）

2026-11-12 舊文盤點整篇重寫：
重組為以「隱私而非省錢」與「混合架構」為核心的架構專文，將具體過期模型轉為當時範例，並將評測避坑與去敏實作之技術細節收納至附錄。
-->
