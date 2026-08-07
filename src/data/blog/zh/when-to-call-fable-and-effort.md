---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: 何時派工 Fable？三個時機，還有別開 ultracode
slug: zh/when-to-call-fable-and-effort
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - token-optimization
description: '最貴的模型不是拿來全程跑的。三個我體感最好的 Fable 派工時機，以及為什麼 Opus 5 我最多開到 med。'
---

何時派工 Fable？個人體感最好的三個時機：

1. 主 agent 用 Fable 做整體架構規劃，實作用 subagent，最後回來給 Fable 驗收。（這也是被最多人建議的）

2. 主 agent 用 Opus 或 Sonnet，做的過程中有卡關或者需要對抗審查、拓展思維，叫單個 Fable subagent 來當一次性顧問。（我後來更常用這個）

3. 明天就是週重置，還有好多額度沒用完的時候。（A\ 佔不到你一點便宜）

那天有人問我要不要開 ultracode。

為何要開 ultracode（？想要享受千軍萬馬奔騰的感覺嗎。更不用說 ultracode 的 xhigh 模式在 Opus 5 上會有 overthink 的壞毛病，他在腦子裡左右互搏就是狂燒你的 token。

關掉 ultracode，Opus 5 最多開到 med。其實大部分的 subagent Sonnet 就好。重點是要想清楚聰明的模型在什麼節點參與——是規劃／協調／臨時顧問，還是驗收。

<!--
新增非原文句子清單（忠實度自首）：
1. 「那天有人問我要不要開 ultracode。」 — 類型：銜接（把第二則貼文的回覆情境交代出來，原文為回覆他人提問，無此敘述句）
-->
