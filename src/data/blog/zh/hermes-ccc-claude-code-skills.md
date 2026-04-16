---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:00:00Z
title: "hermes-CCC：把 Hermes Agent 的 46 個能力全部裝進 Claude Code"
slug: zh/hermes-ccc-claude-code-skills
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - skills
description: 有人把 NousResearch 的 Hermes Agent 整套行為拆解成 46 個 Claude Code 原生 Skill。沒有 OAuth、沒有外部進程、重啟 CC 就能用。核心設計哲學是「procedures-as-prompt」：用結構化 markdown 指令稿驅動 AI 行為，不用寫一行程式碼。
---

Hermes Agent 是 NousResearch 做的一套 AI agent 執行環境——有自己的記憶系統、工具路由、跨 session 學習能力。原本的設計是讓它跑在獨立的 process 裡，有自己的 runtime。

[hermes-CCC](https://github.com/AlexAI-MCP/hermes-CCC) 的作者做了一件有意思的事：他說，**Claude Code 本身就已經是 agent 執行環境了，根本不需要再跑一個獨立的 process**。

所以他把 Hermes Agent 的每個能力拆解成 46 個 Skill，全部裝進 Claude Code 原生的 Skill 系統。沒有 OAuth、沒有額外帳號、沒有外部 process——重啟 Claude Code 就能用。

## Procedures-as-prompt

這個 repo 的核心設計哲學，值得單獨說一下。

每個 Skill 都是一份 `SKILL.md`，裡面用結構化自然語言寫明：觸發條件、執行程序、輸出格式、失敗模式與回復動作。Claude Code 讀 `description` 欄位決定要不要觸發，讀 `## Checklist` 逐步執行。

沒有程式碼、沒有 function call。**純靠 markdown 指令稿驅動 Claude 的行為。**

這不是偷懶，而是刻意的設計選擇。傳統的 agent 框架要寫 Python，要管依賴、要處理 API、要維護 runtime。procedures-as-prompt 把「行為規範」從程式碼層提到了文字層——任何人看得懂、任何人修得了，AI 本身也理解它在做什麼。

## 手動觸發 vs 自動觸發

使用這類 Skill 系統有一個很重要的心智模型要建立。

**手動觸發**：你直接打 `/hermes-route`、`/systematic-debugging` 等斜線指令，保證執行，沒有懸念。

**自動觸發**：每個 `SKILL.md` 的 frontmatter 有 `description` 欄位，Claude 在每次對話中讀完所有 Skill 的 description，自己判斷當前情境是否符合，符合就自動呼叫。這是「期望」，不是「保證」。

description 寫得越精準，自動觸發越可靠，但仍有漏判可能。LLM 的判斷在本質上不是確定性的。

**手動觸發是保證，自動觸發是期望。** 用 hermes-CCC 的時候要記住這一點，不然會對它的「自動化」程度有錯誤預期。

## 最值得看的幾個 Skill

46 個 Skill 不可能一一介紹，但其中幾個的設計思路特別值得看：

**`/hermes-route`：任務路由器**

每次任務前先分類，決定該怎麼打。輸出一個路由決策塊，包含任務類型（lightweight / standard / deep）、執行模式、先讀哪些檔案、可不可以拆子任務、推理深度需求。

核心在「評估走錯第一步的代價」——deep 任務的第一步走錯，修正成本遠高於 lightweight 任務。

**`/hermes-memory`：跨 session 記憶分層**

管理跨 session 的持久記憶，四種操作：Prefetch（工作前撈相關記憶）、Sync（工作後合併新知識）、Nudge（推薦值得存但不自動存的東西）、Compress（清理重複、刪過期）。

強制區分「持久知識」（架構決策、工具雷點、偏好）和「暫時狀態」（branch 名稱、單次任務進度）——這個區分很多人在手動管理 memory 的時候沒有做到位。

**`/hermes-compress`：context 壓縮萃取六桶**

當 context window 快滿時，把當前對話萃取成結構化摘要存進 memory，釋放 context 空間。六個桶：decisions（決策）、artifacts_created（產出）、problems_solved（解決的問題）、facts_learned（新知識）、open_issues（未解決）、next_steps（下一步）。

這個設計比一般人手動做 `/compact` 的方式更有組織——不是把對話濃縮成敘事，而是強制結構化。

## 這個 repo 的真正價值

hermes-CCC 值得看不只是因為你可以直接把 46 個 Skill 拿來用。

更重要的是，這個 repo 示範了一件事：**Skill 系統本身是可以做架構設計的。** 任務路由、記憶分層、context 管理、子 agent 分工——這些 agent 框架裡常見的設計模式，都可以用 SKILL.md 的語言來表達。

如果你在設計自己的 Skill 系統，hermes-CCC 是目前社群裡最完整的一份「如何設計 Skill 架構」的參考實作。

GitHub：https://github.com/AlexAI-MCP/hermes-CCC（安裝前建議先跑 `/security-scan`）
