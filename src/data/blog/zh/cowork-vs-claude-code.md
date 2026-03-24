---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-24T05:00:00Z
title: "為什麼 Cowork 幾小時就頂到限額，Claude Code 整天都沒事？"
slug: zh/cowork-vs-claude-code
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - developer-experience
description: 同樣是 Max 方案，Cowork 和 Claude Code CLI 的 token 消耗差距可以到十倍以上。這篇解釋為什麼，以及什麼時候用哪個。
---

有 Max 方案的人常問這個問題：用 Claude Code 在終端機跑整天開發，用量從不超過一半；但切換到 Cowork 做幾小時的小專案，就頂到限額。

同樣是 Max，同樣是 Claude，怎麼差這麼多？

## 結論先說

Cowork 消耗 token 的速度遠高於 Claude Code CLI。一個 Cowork session 做複雜的檔案操作，消耗的 quota 相當於幾十條普通聊天訊息。Max 5x 的「225+ 條訊息」換算成 Cowork，大概只能做 10 到 20 個實質操作。

原因有三層，分別來自 Cowork 的架構設計。

## 第一層：Cowork 的隱藏 token 開銷

Cowork 跑在 sandboxed VM 裡。每次操作背後看不見的東西：

- **截圖 + 圖片處理**：Vision token 非常貴，遠比純文字貴
- **多次 AI 推理呼叫**：一個「任務」可能觸發 5 到 10 次 API call
- **整檔讀入 context**：不像 CLI 可以精準控制只載入需要的部分
- **完整歷史疊加**：每一步都帶著前面所有步驟的歷史，context 只增不減

你以為在做一件事，背後其實跑了十幾個 API 呼叫。

## 第二層：Claude Code CLI 天生省 token

CLI 有幾個 Cowork 沒有的優勢：

**Prompt caching。** System prompt、CLAUDE.md、工具定義這些重複出現的內容會被快取，不重複計費。每次新的 session，這些不用重新算錢。

**精準 context control。** 你可以控制只讀哪些檔案、只載入哪些 skill。好的 CLAUDE.md 架構用 on-demand loading，比一次全塞進去省很多。

**沒有視覺處理。** 純文字互動，不需要截圖或圖片辨識，直接省掉 vision token 這整塊開銷。

## 第三層：速度問題造成惡性循環

Cowork 極慢。Claude Code 5 分鐘能完成的任務，Cowork 可能要跑 40 分鐘。

慢不只是慢而已——慢等於更多 context 累積，等於更多 token 消耗。任務拖越長，每一步帶的歷史越多，計費越高。這是惡性循環。

## 社群怎麼說

這不是個人感受，有 GitHub issues 記錄：

- [#16856](https://github.com/anthropics/claude-code/issues/16856)：用戶回報 token 消耗速度比以前快 4 倍以上
- [#23318](https://github.com/anthropics/claude-code/issues/23318)：多人確認用量異常，懷疑計算方式改變
- [#33120](https://github.com/anthropics/claude-code/issues/33120)：Cowork 專屬的 rate limit 問題

Zvi Mowshowitz 寫過一篇專文比較兩者差異，結論跟這裡一致：差距主要來自 context control。Threads 上也有開發者說「Burns limits way faster than Claude Code」、「5min task in CC → 40min in Cowork」。

## 額外觀察：為什麼 Opus 在 CLI 裡「感覺更聰明」

這是我自己的體感，但有合理解釋。

CLI 的 context 更乾淨、更聚焦，模型能把算力花在真正的問題上，而不是處理 sandbox 環境的雜訊。同樣的模型，input 品質不同，output 自然不一樣。

## 什麼時候用哪個

**Claude Code CLI 適合：** 開發工作、長時間 session、需要精準控制的任務。Token 效率最高，適合每天大量使用。

**Cowork 適合：** 需要圖形操作、瀏覽器互動、或者不熟悉終端機的情境。代價是 quota 消耗快很多。

有 Max 方案的人，如果主要工作是寫程式，大部分時間都不需要碰 Cowork。
