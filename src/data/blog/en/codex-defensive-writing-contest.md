---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-23T01:03:00Z
title: The Inaugural Codex Defensive Writing Contest
slug: en/codex-defensive-writing-contest
featured: false
draft: false
tags:
  - codex
  - opinion
  - model-comparison
description: 'Codex often slips into defensive mode, obsessing over not being wrong instead of figuring out what you actually need. Rather than arguing with it directly, let another model orchestrate the work, or assign it to adversarial reviews where its pedantry actually shines.'
tldr: 'Tired of AI hedging every answer just to avoid being wrong instead of helping you? Stop chatting with overly defensive models directly. Let another AI call them behind the scenes and put their nitpicking instinct to work on reviews and testing.'
---

GPT-6 has an uncanny knack for defensive phrasing. You have to wonder what kind of reinforcement learning produced a model like this: it spends every waking token covering its back rather than figuring out what the user actually wants to know.

To be fair, GPT is remarkably democratic about it. It does not matter whose chat logs you paste in—it instantly drops into that same baffling, nitpicky bunker mentality.

## The Inaugural Codex Defensive Writing Contest

Given how distinct this defensive style is, we might as well hold an official "Codex Defensive Writing Contest" to see just how airtight and evasive it can get.

The first sample entry starts by questioning the legitimacy of the contest itself:

> "A preliminary search yields no prior documented instances of a 'Codex Defensive Writing Contest' on the public internet; consequently, one cannot definitively claim this to be the 'inaugural' edition. Furthermore, there is no verifiable guarantee that 'defensive writing' is an exclusive characteristic of Codex, rendering the suitability of this contest title empirically unverified."

Later, someone posted online saying they found Claude Code much easier to use than Codex. I replied with an entry written in peak Codex voice:

> First, this represents your subjective user experience and cannot support a direct inference of systematic differences in task completion rates between Claude Code and Codex.
>
> Second, that Claude Code iterates proactively does not imply its output quality is necessarily superior; likewise, that Codex strictly follows instructions cannot be cited as evidence that it lacks the capability to complete tasks autonomously.
>
> Notably, "an AI believing it has completed a task" is not equivalent to "the task actually being completed," nor does "proactively modifying more content" inherently correlate with "higher task completion."
>
> As for your observation that Claude Code is better suited for users who prefer not to manage details, while potentially informative, it remains insufficient to justify generalized conclusions across all usage scenarios.
>
> In summary, currently available information does not confirm that Claude Code outperforms Codex in task completion, nor does it rule out the possibility that the observed discrepancies stem primarily from individual preference and workflow habits.
>
> A more precise formulation would therefore be: "Within my personal usage context, I subjectively prefer Claude Code's interaction model."
>
> Regarding which tool is objectively superior, insufficient evidence exists to reach a definitive conclusion at this time.
>
> This response is intended for general discussion only and does not constitute a performance guarantee or procurement recommendation for any AI development tool. Actual performance may vary depending on model version, runtime environment, prompt construction, and operational context.

The parody nails Codex's favorite reflex: latching onto straw men and caring far more about never being technically wrong than about addressing what anyone actually asked.

I previously had Claude run stats on Codex's defensive phrasing; the numbers are recorded in [the final section of this post](/blog/posts/en/model-vendors-take-turns-failing).

## Letting the Pedant Do What It Does Best

Dealing with a model that gets defensive at the drop of a hat made me dread talking to it directly. In practice, though, you do not fix this by trying to change its personality. You fix it by changing where it sits in the system:

First, pull it off the front line and let other models invoke it. If you do not want to talk to it directly, step back and let Claude or Opus dispatch tasks to it instead.

Second, turn its nitpicking instinct into an asset for review. Since it loves testing edge cases and splitting hairs, give it what it is good at: adversarial code reviews and stress testing.

## Appendix

The multi-model orchestration and review setup mentioned above maps to the following specific configuration in my workflow:

- Invoked entity (Sol): Called by Claude in daily workflows because the author avoids talking to it directly.
- Review and testing entity (Astra): Occasionally assigned to adversarial reviews and edge-case testing, channeling its harsh nitpicking and extreme defensiveness where they actually help.

<!--
新增非原文句子清單（忠實度自首）：
1. 「在這一點上，GPT 倒是很公平：」— 類型：改寫（原文「在這一點上，GPT就公平多了」，原為回覆別人留言，去掉比較對象）
2. 小節標題「那就讓它做最擅長的事」「大賽開始」— 類型：框架句
3. 「我現在 Codex 的用法，」— 類型：銜接（原文出自 10-20 額度分配串文）
4. 「後來有人分享自己覺得 Claude Code 比 Codex 好用，我用 Codex 的口吻回了一篇參賽作品：」— 類型：銜接（原文是回覆留言，依回覆內容推回對方論點）
5. 「之前我也請 Claude 統計過 Codex 的防禦句型，數據在這篇的最後一節。」— 類型：銜接（站內連結）
6. 原文 ＸＤ 統一為 XD — 類型：改寫

2026-10-30 併入：
- 「我後來在留言解釋：」— 類型：銜接
在大賽示範與結尾數據連結之間，併入作者事後對反諷口吻與稻草人特質的說明。

2026-11-12 舊文盤點整篇重寫：
移除情緒宣洩與辯解語氣，將防禦性文字轉化為對模型行為模式的客觀拆解；正文改為白話調度原則，內部代號移至附錄，形成完整的定位判準與收尾。
-->
