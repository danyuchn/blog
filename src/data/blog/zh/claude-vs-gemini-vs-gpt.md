---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T02:00:00Z
title: "Claude vs Gemini vs GPT：一個重度使用者的模型體感實錄"
slug: zh/claude-vs-gemini-vs-gpt
featured: false
draft: false
tags:
  - ai-models
  - claude
  - gemini
  - gpt
description: 同時使用三大 AI 模型半年多的真實體感記錄。Claude 的穩定、Gemini 的自我懷疑、GPT 的退場，以及我最後的訂閱選擇。
---

過去半年，我幾乎每天都在同時使用 Claude、Gemini、GPT 這三家的模型。不是跑 benchmark，不是看別人的評測影片，而是拿來做正事：寫程式、重構資料庫、部署產品、整理教學內容。以下是我的真實體感。

## GPT：曾經的王者，現在只剩兩招

GPT 曾經是我的主力。但到了 2025 下半年，我的感受是：**GPT 只剩 Deep Research 跟繪圖有優勢，其他功能都已經不行了。**

最讓我受不了的是 ChatGPT 的回覆方式。每次對話結尾一定要來一句：

> 「若你需要，我也可以幫你……告訴我，我們馬上開始！」

幹正事就好，屁話那麼多幹嘛。

不過說句公道話，OpenAI 爬資料的能力確實強。他的 Deep Research 跟網路搜尋，其他家找不到的東西，他都找得到。但單論模型本身的推理跟執行能力，我最後還是把 GPT 的訂閱退掉了。

## Gemini：內心戲最多的模型

Gemini 3.0 Pro 是我用過最讓人崩潰的模型。

打開它的思維鏈看，你會發現它的內心戲有夠多：不斷在自我懷疑、搞砸、自責、重來又搞砸一次。有時候還會瘋狂跳針，重複輸出 `EXECUTE IT` 上千次。

我一開始是為了 Gemini 才裝了 Google Antigravity。結果用了之後才發現，Gemini 3.0 Pro 是真的不行：

- 會自己一直鬼打牆
- 在 Chrome 裡看網頁的時候，會突然跟我道歉說「我搞砸了」
- 時不時冒出「我只是個語言模型，幫不上忙」

我有一次同時開 Gemini 3.0 Pro 跟 Claude Opus，交代好幾種不同的任務。Claude 全部完成了，Gemini 還在鬼打牆，一直自我懷疑跟重複同一個字跳針。

不過 Gemini 也不是完全沒用。辦正事的時候，尤其是讀文獻，Gemini 的超長上下文窗口確實有優勢，不會偷懶漏東漏西。用對場景的話，它還是能幫上忙。

## Claude：最後的贏家

說到這裡大概可以猜到我的結論了。

在命令行裡，Claude 贏過 Gemini 真的不是一點半點。穩定度、遵循度都非常高。少了 IDE 的束縛，在 CLI 裡調用工具明顯靈活很多。

**Antigravity 最大的功勞，就是讓我發現 Claude 用得不夠，然後跑去訂閱了 Claude Max。**

Claude Max 是我人生中最貴的一次訂閱，但也是最值的。200 美金，體感上可以用出 2000 甚至更高的價值。換算下來大約 7000 台幣，做到的事情可能要花 7 萬請一個人。

當然，重度使用也有代價。我兩天 extra usage 就花了 20 美金，加購額度又燒了 20，最後想說乾脆直接升級算了。

## 其他觀察

市場上還有一些值得關注的動態：

- **Codex**：聽說除錯很強，但很慢。適合複雜問題，不適合日常開發
- **ASI**：Threads 上一度很紅。號稱「超越一切 LLM」。看看就好
- 模型迭代速度越來越快，但**不是每次迭代都是進步**。有些模型越更新越退化，幻覺率反而更高

## 我現在的配置

- **主力**：Claude Code（CLI）+ Claude Max 訂閱
- **文獻 / 長文處理**：Gemini
- **Deep Research / 網路搜尋**：GPT（免費額度就夠）
- **繪圖**：GPT

與其在一個平台上 all-in，不如搞清楚每個模型的強項，按場景搭配。
