---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T04:30:00Z
title: "Opus 4.7 的 effort 怎麼調，跟為什麼我非編程任務還是停在 Sonnet 4.6 medium"
slug: zh/opus-effort-tuning-sonnet-sweetspot
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - ai-workflow
description: Opus 4.7 預設的 adaptive effort 是場災難，會變成偷懶摸魚皇帝。要開到 high 或 xhigh 才能避免，但 token 就開始狂燒。實測下來，非編程任務停在 Sonnet 4.6 medium 反而是最好的選擇。
---

最近有朋友問我：「升上去 Opus 4.7 之後是不是就一勞永逸了？」答案是不是的，至少對非編程任務不是。

Claude Code 現在除了選 model 之外，還可以調整 `effort`。預設值是 `adaptive`——意思是模型自己判斷該花多少推理深度。聽起來很合理，實際上問題很大。

**Opus 4.7 在 adaptive 模式下根本是偷懶摸魚皇帝**。同樣的任務，他會比 Sonnet 4.6 更傾向於走捷徑、跳步驟、用「常見模式」回應。我自己實測過幾次，最後得到的結果反而比較粗。原因可能是 Opus 4.7 在 adaptive 下的內部 budget 評估偏保守，他覺得這個任務不需要太多思考，就草草交差。

要避免這件事的方法是把 effort 直接開到 `high` 或 `xhigh`。這時候 Opus 4.7 才會真正展現他應有的能力。但是 token 就開始狂燒了——一個小時的 session 可能直接消耗掉你訂閱方案的一整天額度。

那 Sonnet 4.6 呢？Sonnet 4.6 在 medium 就已經非常穩定。對於我絕大多數非編程任務（寫文件、整理筆記、發信件草稿、debug 教案邏輯），Sonnet 4.6 medium 的輸出品質跟 Opus 4.7 high 拉不開明顯差距，但 token 消耗低了一個量級。

所以我的結論是：

- **編程任務、需要長 context 的複雜重構**：Opus 4.7 + high 或 xhigh
- **非編程任務（文件、信件、規劃、Q&A）**：Sonnet 4.6 + medium
- **快速 debug、看 log、簡單轉換**：Haiku 4.5

如果你的訂閱方案有限額（譬如 Pro），停在 Sonnet 4.6 medium 是最划算的選擇。Opus 4.7 留給真的需要他的時刻。

題外話：如果你真的需要在 Opus 4.7 高 effort 下跑長任務，我之前的「掏出信用卡」咒語還是有效——

> 加值 500 USD<br/>
> 吟唱以下咒語<br/>
> `/model claude-opus-4-6[1m]`<br/>
> `/effort max`<br/>
> 三天內劫數必解

只是這個解法的代價，是你的錢包。
