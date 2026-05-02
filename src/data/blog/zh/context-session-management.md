---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T05:00:00Z
title: "1M Context 不是裝更多，而是管理更好：Claude Code Session Management 心法"
slug: zh/context-session-management
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-workflow
description: Claude Code 的 context window 從 200k 長到 1M，但更大不代表更好用。這篇整理五種 session 管理操作（Continue / rewind / clear / compact / Subagents）、四大策略、以及最容易踩的兩個坑。
---

![1M Context 不是裝更多，而是管理更好](/blog/assets/posts/context-session-mgmt/slide-1.jpg)

Context window 從 200k 長到 1M，大多數人的直覺是：太好了，可以塞更多東西進去了。

這個直覺是錯的。

更大的 context 代表更高的管理成本。注意力稀釋、舊資訊干擾新任務、模型悄悄跑偏——這就是 context rot（上下文腐化）。知道 1M context 怎麼「用對」，比知道它有多大更重要。

## 核心概念：Context ≠ 越大越好

![Context 不等於越大越好](/blog/assets/posts/context-session-mgmt/slide-2.jpg)

先定義清楚 context 是什麼：模型在一次對話裡「看到」的全部資訊，包含對話歷史、system prompt、tool outputs、讀過的檔案。

Claude Code 現在支援 1 million tokens 的 context window。這代表你可以把大量資訊塞進去。但隨著 context 增長，會發生三件事：

- **注意力被稀釋**：重要資訊淹沒在大量歷史紀錄裡
- **舊資訊干擾新任務**：三個任務前的決定持續影響現在的推理
- **模型表現下降**：這就是 context rot，本質不是 memory 不夠，而是「噪音變多」

當 context 快滿時，系統會自動 compaction：摘要歷史、開新 context window 繼續跑。但這是 lossy compression（有損壓縮），重要細節可能在這步被丟掉。

主動管理 context，比被動等系統壓縮，結果好很多。

## 五種操作，對應五種情境

![每一步都在選擇如何管理 context](/blog/assets/posts/context-session-mgmt/slide-3.jpg)

每次你決定「接下來怎麼繼續」，都是一個 context 決策。你有五種操作：

**1. Continue（繼續）**
保留全部 context，繼續同一個任務。適合：任務還在進行中，脈絡都還有用。

**2. /rewind（回溯）**
回到某個分叉點，丟掉錯誤路徑。適合：走錯路了，需要修正方向，但不想完全重來。

**3. /clear（開新 session）**
完全清空 context，自己撰寫 summary 帶進新 session。適合：要切換到完全不同的新任務。

**4. /compact（壓縮）**
讓模型幫你摘要歷史，保留 continuity（連續性）。適合：context 太肥，資訊太多開始混亂，需要精簡但不想完全清掉。

**5. Subagents（子代理）**
開一個獨立 context，完成任務後只回傳結論，不污染主 context。適合：需要處理高噪音或大量中間輸出的子任務，例如掃描大量檔案、驗證工作。

**關鍵判斷：你需要「過程」還是「結論」？** 如果子任務的過程不需要帶回主 context，就用 Subagent。

## 四大策略，讓 context 保持乾淨又高效

![4 大策略讓 context 保持乾淨又高效](/blog/assets/posts/context-session-mgmt/slide-4.jpg)

把五種操作整理成四個日常策略規則：

**策略 1：新任務 → 新 session**
任務切換時就開新 session，避免 context rot 和無關資訊干擾。不要讓上一個任務的「殘留脈絡」影響新任務的推理。

**策略 2：走錯路 → rewind，不是補 prompt**
走錯路時，不要試圖用更多 prompt 說明來「修正」，而是直接 rewind 到分叉點重走。保留有用 context，丟掉錯誤探索。

**策略 3：context 太肥 → compact 或 clear**
太多內容會讓注意力稀釋。用 compact（摘要）來瘦身；如果已經完全換任務，直接 clear。

**策略 4：大量中間輸出 → subagent**
把高噪音、耗資源的子任務交給子代理，只帶回結論，保持主 context 乾淨。

| 情境 | 最佳策略 |
|------|---------|
| 同一任務持續推進中 | Continue |
| 方向錯誤或嘗試失敗 | /rewind |
| 切換到新的目標 | /clear |
| 資訊太多、開始混亂 | /compact |
| 高噪音子任務 | Subagents |

## 兩個最容易踩的坑

![避免踩坑，保持 context 品質](/blog/assets/posts/context-session-mgmt/slide-5.jpg)

**坑 1：Bad compaction（壞的壓縮）**

發生原因：在方向不明的時候壓縮。例如前面在 debug，突然切去另一個問題，新問題被 summary 掉。

結論：方向不明時，模型壓縮容易出錯，重要脈絡可能被捨棄。在 compact 之前，先確認你下一步要做什麼。

**坑 2：Context rot 高峰期是最糟的壓縮時機**

直覺是「等 context 快滿了才 compact」，但這是最壞的時間點。原因：
- context 最大，注意力最分散
- summary 最不準
- 關鍵資訊最容易被丟掉

正確做法：在「一個小任務剛結束」就主動壓縮。不要等到快爆了才想到要 compact。

## 決策總表

![不同情境選擇最適合的 context 策略](/blog/assets/posts/context-session-mgmt/slide-6.jpg)

善用這五種操作，主動管理 context，Claude Code 就能持續保持高效與精準。

Context window 的大小只是上限，管理品質才是實際表現的決定因素。

---

Source: Anthropic 官方文章 [Using Claude Code Session Management and 1M Context](https://claude.com/blog/using-claude-code-session-management-and-1m-context)
