---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "全英文授課的提詞器救星，以及我正在評估的開源 AI Meeting Copilot「Natively」"
slug: zh/english-teaching-ai-teleprompter
featured: false
draft: false
tags:
  - ai-tools
  - teaching
  - ai-education
description: '日常英文口語沒問題，但全英文授課講深度想法時就卡彈——提詞器救了我。順便整理我正在評估的開源 AI meeting copilot「Natively」。'
---

不知道有沒有人跟我一樣，日常英文口語對話沒問題，但是用全英文授課時因為是深度的想法，就會莫名卡彈，但是配上了提詞器後，就算不是照著念，也可以即興發揮非常流利順暢⋯

提詞器真的是我的救星。

不然我今天一整天都在煩惱，下禮拜開始要給日本韓國美國加拿大一共 30 人做全英文企業內訓該怎麼辦⋯

## 順著這個煩惱，我去查了一個工具

順著提詞器這條線，我最近在評估一個叫 **Natively** 的開源工具——一個 AI meeting copilot，課中即時提詞是它的使用場景之一。先講清楚：我還在評估，還沒實際拿它上過課，下面是調查筆記，不是使用心得。

## Natively 是什麼

它把自己定位成 Final Round AI / Cluely 的開源免費替代品。BYOK（自帶 API key），沒有訂閱費，授權是 AGPL-3.0。運作方式是擷取系統音訊加麥克風雙軌，邊聽會議邊給即時建議，可以接 Claude / GPT / Gemini，也可以完全跑本地的 Ollama。

GitHub 健康度看起來不錯：1,383 顆星，issue 關閉率 91%，最新版本 v2.6.0。repo 已經從個人帳號移轉到一個 org，算是有在維護的訊號。

評價裡有一句我覺得很到位：它是「copilot, not a coach」——沒有題庫、沒有 mock、沒有客服，目標族群本來就是有 API key、看得懂原始碼的工程師。

隱私上它資料全本地，對照之下 Cluely 在 2025 年中外洩過 8.3 萬筆使用者資料。

## 資源佔用與已知問題

我是 M2 Air 16GB，這部分我有特別查。

- 磁碟：macOS arm64 的 dmg 是 431 MB（裡面打包了本地 Whisper 模型）。
- RAM：API 模式約 400–600 MB；如果開本地 Whisper / Ollama 模型，再往上加 1–4 GB。

結論是：我這台 16GB 的機器，要用就用 API 模式，不要開本地模型——一邊開 Zoom 一邊跑本地推論會 thermal throttle。

已知的活 bug 也得記下來：麥克風／語音偵測失敗有多則回報、Windows 上有些詭異錯誤、偶爾會聽到問題卻不回答。這些上課前得先自己測過。

## 競品價格對照

順手把競品價格列一下，這也是我評估 Natively（免費 BYOK）划不划算的對照組：

| 工具 | 月費 |
|------|------|
| Natively | 免費（自帶 API key） |
| Cluely Pro | $20/月 |
| OphyAI | $9/月（credit 制，約 6 場） |
| LockedIn AI | $54.99/月（無限） |
| Final Round AI | $148/月（5 場） |

## 我打算怎麼用（如果評估通過）

兩個場景：課中即時提詞，課後復盤——把全程轉錄拉出來，比對 AI 當下建議的說法跟我實際講的差在哪。再進一步的話，可以把教材餵進本地 RAG，讓它的建議更貼我的課綱。

但這些都還是「打算」，等評估完再說。
