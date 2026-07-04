---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
title: Fable 5 回歸一週：把最貴的模型變成 Skill Distillation 引擎
slug: zh/fable-5-return-skill-distillation
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: 'Fable 5 限時回歸一週，我沒拿去做日常小事，而是拿去做高槓桿判斷、蒸餾成便宜模型可照做的 skills。'
---

Fable 5 從明天起回歸一週，所以我要用 Sonnet 5 保護我的週額度，其他全部灌給 Fable。

![Anthropic 官方公告：Fable 5 與 Mythos 5 出口管制解除，7/1 起回歸](/blog/assets/posts/fable-5-return-skill-distillation/announcement.jpg)

官方公告的重點是這樣：截至 6/30，Fable 5 和 Mythos 5 的出口管制已解除；Fable 5 從 7/1 星期三起，在 Claude 全平台、Claude.ai、Claude Code、Claude Cowork 開放；Pro / Max / Team 和部分 Enterprise 方案，Fable 5 會算進每週使用量上限的最高 50% 以內，直到 7/7 為止，之後改由使用額度提供。看到這個，我就開始想怎麼把它用好用滿。

還好我第一天就把 Fable 額度用好用滿了，美國政府之後再封我，我也無怨無悔（？）。

這禮拜交給 Fable 的主要任務，是 ULTRACODE 優化這個資料夾的檔案結構、根據官方文檔優化 project-level 的 harness（SKILL、memory、rules、claude.md）、把過舊的內容 archive、保持主檔精簡、有衝突就化解。關鍵在分工：為了保留 Fable 的算力，我要它本人只做規劃跟驗證，執行交給 Sonnet 5 的 subagent，每個 subagent 專注在範圍明確的小任務，確保 context window 乾淨。目的是為未來的 Opus / Sonnet 打好這個專案資料夾的規矩。這個做法我也參考了 Reddit r/ClaudeAI 上「讓 Fable 5 寫 skills」的討論。

做完這一輪，我把整套做法沉澱成一個方法論，我叫它 Skill Distillation。一句話講完：最貴的模型不該拿去做日常小事，而是把最貴的判斷，蒸餾成便宜模型可以重複照做的工作規範。

![圖卡：高價模型，不該拿來做日常小事](/blog/assets/posts/fable-5-return-skill-distillation/card-1-expensive-model.jpg)

怎麼做？讓 Fable 先讀 repo 不先寫——README、測試、CI、docs、git history、失敗紀錄全看過——再問 5 個 repo 看不出來的問題，最後產出一批 Opus / Sonnet 可以照做的 skills，跑三輪 review。步驟細節我整理在卡片上，讓卡片自己講。

![圖卡：Skill Distillation 怎麼做](/blog/assets/posts/fable-5-return-skill-distillation/card-2-skill-distillation.jpg)

分工的原則是：Fable 當 architect，負責 spec、架構審查、失敗分析、研究彙整；Opus / Sonnet 當 executor，照 plan 實作、日常 coding、小修小補、反覆迭代；人負責決定什麼時候值得燒 Fable、給完整 brief、驗收輸出。兩條鐵則：大 brief 一次給，先審 spec 再寫 code。

![圖卡：Fable 當 Architect，Opus/Sonnet 當 Executor](/blog/assets/posts/fable-5-return-skill-distillation/card-3-architect-executor.jpg)

我也把那段 prompt 骨架做成一張卡：請高階模型扮演一個即將退休的 principal architect，把專案判斷轉成 durable skills，而且只准寫 skill / runbook，不准動 source code。

![圖卡：Skill Distillation 的 Prompt 骨架](/blog/assets/posts/fable-5-return-skill-distillation/card-4-prompt-skeleton.jpg)

真實驗證來自一個在寫論文的朋友。他早上借用我的帳號，說 Fable 寫出來的數學證明既自然又簡潔優雅，而且一次過完全不會錯，他從無到有寫了兩篇，已經準備投出去，折合 API 成本 200 USD。這次我們是所有 subagent 都用 Fable，也就是故意開到滿；但事後討論，其實最佳搭配應該是 plan / architecture / final verification 用 Fable，寫 transcript 用 Opus 4.8，跑實驗寫 code 用 composer 2.5，畫圖用 gpt-image-2。他說 100 USD 寫一篇其實真的不貴，所以就算未來用 API 也划算。

一週的限時額度，我沒拿去做小事。把最貴模型的判斷，變成便宜模型的工作規範——這是我這一週真正留下、之後每天還在用的東西。

<!--
新增的非原文句子（AI 最小銜接，非作者原文）：
1. 「官方公告的重點是這樣：」— 引入公告內容的銜接句
2. 「看到這個，我就開始想怎麼把它用好用滿。」— 貼文2「我的反應：開始思考如何用好用滿」的忠實改寫
3. 「關鍵在分工：」— 引入 Fable 規劃/Sonnet 執行分工的銜接短語
4. 「這個做法我也參考了 Reddit r/ClaudeAI 上『讓 Fable 5 寫 skills』的討論。」— 依素材附註改寫為承接句
5. 「做完這一輪，我把整套做法沉澱成一個方法論，我叫它 Skill Distillation。」— 引入方法論段落的銜接句
6. 「步驟細節我整理在卡片上，讓卡片自己講。」— 指向圖卡的銜接句（避免複述卡面文字）
7. 「真實驗證來自一個在寫論文的朋友。」— 引入論文朋友段落的銜接句
8. 「一週的限時額度，我沒拿去做小事。把最貴模型的判斷，變成便宜模型的工作規範——這是我這一週真正留下、之後每天還在用的東西。」— 收束句，改寫自卡1核心論點，非喊話式小結
-->
