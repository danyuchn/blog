---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T06:00:00Z
title: "給 LLM 更好的 context，勝過換更強的模型——repowise 的五層架構"
slug: zh/context-over-model-repowise
featured: false
draft: false
tags:
  - claude-code
  - mcp
  - agentic-coding
description: '看到 repowise 這個在 codebase 與模型之間插一層 context 的工具，想聊一個更大的觀念：模型改壞東西時，第一反應常常是換更強的模型，但真正的根因往往是 context 不夠。'
---

最近在 r/ClaudeAI 看到一個工具叫 repowise，順手研究了一下。它解決的問題我自己常踩，想藉這篇講一個更大的觀念。

## Claude Code 是逐檔閱讀的

它沒有整張架構地圖。常常在不知道依賴關係的情況下重寫一個模組，結果改 A 踩壞 B。

你大概也遇過：明明只是想動一個函式，Claude 卻把它整段重寫了，沒注意到另外三個檔案都在 call 它。不是它笨，是它根本看不到那張圖。

repowise 做的事，就是在 codebase 跟模型之間插一層 context，用 MCP 把這張地圖補上。

## 五層 context

它把 context 拆成五層，我覺得這個分法本身很有參考價值。

第一層 Graph：AST 依賴圖。改動之前先知道什麼依賴什麼。

第二層 Git：熱區（hotspots）、檔案所有者、co-change pattern（哪些檔常一起改）、bus factor。這層是從版本歷史挖出來的，純資料，不靠模型猜。

第三層 Docs：從程式碼自動生成可搜尋的 wiki。

第四層 Decisions：捕捉架構意圖。從 ADR、PR 描述、程式碼裡的 `# WHY:` 標記抓出來，防止 LLM「順手修掉」那些其實是刻意設計的東西。這層我覺得最有意思，因為它在補的是「為什麼」，而不是「是什麼」。

第五層 Code Health：十二個靜態分析指標，複雜度、重複、沒測試的熱區。注意這層也不靠 LLM，全是靜態分析。

## 數據看起來不錯

作者拿 Django（542 個檔案）做了一個 time-travel 實驗：少 49% 的 tool calls、少 89% 的 file reads、成本降 36%。

更有意思的是另一個數字：它標出的二十個最低分檔案裡，有十四個在後來六個月真的出現 bug。70% 的 precision。等於說，補上結構之後，連「哪裡會出事」都能提前看出來。

相容性方面，任何支援 MCP 的環境都能接（Claude Code、Codex、Cursor），支援多 repo workspace，也能做跨 repo 的 co-change 偵測。安裝就 `pip install repowise`，AGPL-3.0，GitHub 上一千九百多顆星。

## 也有要注意的地方

我不想當工具的業配，幾個限制照實講。

社群裡有一則負評，說「很爛」，但沒給具體理由，孤立一條，參考價值有限。

Decisions 那層很依賴 ADR 跟 PR 描述的品質。如果你的 repo commit 習慣很差，commit message 全是 "fix" "update"，這層基本榨不出東西。工具再好，餵進去的料還是要有。

授權是 AGPL-3.0。如果你要塞進商業閉源產品，授權合規要先想清楚，這不是小事。

## 真正想講的是這個

很多人一遇到 Claude 改壞東西，第一反應是「換更強的模型」。

但更常見的根因不是模型不夠強，是模型沒有足夠的 context 去理解這個 codebase 的結構跟意圖。你給它一張完整的依賴圖跟一份「為什麼這樣設計」的說明，普通模型也能做得不錯；你不給，再強的模型也是在黑箱裡瞎猜。

repowise 這類工具的價值，就是把這件事證明出來：給 LLM 更好的 context，往往比換更強的模型划算。

這其實跟我最近在做的 harness 精簡是同一個思路的兩面。一面是減少雜訊——把沒用的指令、過時的規則從上下文裡拿掉；一面是補上結構——把模型該知道的依賴跟意圖明確餵進去。前者減噪，後者加訊號，目標一樣：讓同一個模型表現更好。

下次 Claude 又改壞東西，先別急著換模型。先問一句：它到底有沒有看懂這個 codebase？
