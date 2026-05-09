---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-08T04:00:00Z
title: "追蹤 Anthropic 動態的三條管道"
slug: zh/anthropic-tracking-channels
featured: false
draft: false
tags:
  - anthropic
  - ai-trends
  - claude
  - resources
description: 從 2026 年 3 月開始我陸續記了一些追 Anthropic 的方法——官方來源、員工帳號、第三方拆解。整理成一篇，順便聊近期的 Mythos 系統卡爭議跟員工社群媒體沉寂的訊號。
---

從 2026 年 3 月開始，我陸續在 Threads 上記過一些追 Anthropic 動態的方法。這幾個月累積下來，可以整理成三條管道。

## 管道 1：官方一手來源

最直接但最容易被忽略的是**Anthropic 官網的 research 欄位**——建議每出一篇都要讀一下。Claude Code 的 official documentation 也建議時不時閱讀。他們家寫的東西真的詳細又容易理解，不像很多 AI 公司只會發 marketing blog。

特別重要的是**系統卡（System Card）**。

4 月官方發了下一代 Claude Mythos Preview 的系統卡，244 頁。我把覺得是重點的地方另外 highlight 起來供大家參考。原檔在 <https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf>。

讀系統卡真的是比讀 marketing blog 有用多了，該有的招數跟不該有的陷阱都在裡面。安全測試結果、模型限制、紅隊實驗、refusal 行為——這些東西不會在發表會的 keynote 上出現，但都在系統卡裡。

## 管道 2：員工社群媒體帳號

除了 Anthropic 自己的官網部落格外，我也喜歡去追蹤 Anthropic 員工的社群媒體帳號。

比如 Claude Code 的主要維護者 Thariq，他的文章都非常有價值——常常會講一些「我們為什麼這樣設計」、「下個版本要做什麼」的內幕，比官方 changelog 早很多。

但員工社群媒體也是一種**訊號感應器**。最近就出現一個有意思的訊號：

> 好好笑，平常很愛在推特上發文的 Anthropic 各家員工，這幾天都沉寂，感覺有點非比尋常——是不是要在開發者大會蹲一波大的。

當員工集體沉默，通常代表「有大事要發布、被打招呼不要劇透」。這比看官方倒數計時還準。

## 管道 3：第三方拆解與實測

第三方反而是最能戳破宣傳的管道。

**cchistory.mariozechner.at** 是我推薦的第一個——它把 Claude Code 每一版的 system reminder 都記錄下來。如果你想知道某個行為是哪一版開始改變、Anthropic 在 prompt 上動了什麼手腳，這個網站是必備。

更進階的話，可以看前陣子源碼洩漏後的大量網路拆解——Reddit 跟 Hacker News 上有不少「我反編譯了 Claude Code 內部運作」的長文。

還有就是**獨立的反駁與實測**。Claude Mythos「自主發現零日漏洞」的宣傳出來後，Hugging Face CEO Clem 馬上拿出實測：小型開源模型也能做到同樣的事。他們拿了 8 個模型跑 Anthropic 宣傳的漏洞，8 個都復現了，其中一個只要 $0.11/M token。

中文自媒體一片吹捧，英文技術圈直接開嗆。來源：[AI Cybersecurity After Mythos: The Jagged Frontier](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)

## 三條管道一起用

我自己的習慣是：

- **官方**：看清楚 Anthropic 自己怎麼說
- **員工**：看清楚他們真正在意什麼、下一步往哪走
- **第三方**：看清楚實際表現跟宣傳之間的落差

只看其中一個管道，要嘛太天真，要嘛太憤世。三條一起用才能保持判斷力。

順便提一個輕鬆的觀察：Claude 官方帳號最近又開始整活，弄了一個 Lo-Fi Music 直播。能在嚴肅的安全研究跟 Lo-Fi 之間自由切換，也算是這家公司的特色之一了。
