---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T15:00:00Z
title: "cc-audit：一個強迫你省 Claude Code 額度的 Skill"
slug: zh/cc-audit-skill
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - token-optimization
description: '把我之前在社群整理獲得一千多讚的省額度技巧做成健診 skill。丟給 Claude Code 安裝後，它會自動檢查設定、近期 session、rules 與 context 用量，產出可執行的修正清單。'
tldr: '看著 Claude Code 額度見底，內建的統計指令卻只給數字、看不出哪個設定在偷吃額度？安裝開源的 cc-audit 技能，五分鐘就能自動檢查預設模型、近期 5 個對話的快取狀態與規則載入條件，直接告訴你該改哪個檔案、哪一行。'
---

Claude 最近額度亂搞，大家罵歸罵，Claude 還是得繼續用。與其每天看著額度見底焦慮，更實在的作法是把背後偷吃 token 的設定與習慣徹底抓出來。前陣子我在 Threads 上整理了一大串省額度的技巧，收穫一千多讚之後，有網友提議可以做成 skill。

所以我就做好放在這邊了：<https://github.com/danyuchn/cc-audit>

這是一個專門幫 Claude Code 環境做健康檢查的 skill。把連結丟給 Claude Code 請它幫你安裝，就能直接上線執行健診。

## 為什麼不直接看內建的 /stats？

很多人的第一個疑問通常是：終端機裡不是本來就有 `/stats` 可以看用量嗎？

Claude Code 內建的 `/stats` 確實會告訴你「這個 session 用了多少 token」，但它回答不了最核心的三件事：

1. 為什麼會用這麼多？
2. 哪幾個設定才是吃額度的元兇？
3. 知道數字之後，下一步具體該改什麼？

`/stats` 只能量出體重，卻照不出病因。cc-audit 的定位是一份自動化健診，它的輸出不是單純的統計數字，而是結構化報告與可執行建議清單。清單上的每一條，都會具體對應到你的哪一個檔案、哪一行、該做什麼修改，完全不用自己翻文檔瞎猜。

## cc-audit 的四個健診面向

觸發 cc-audit 之後，它會跑四個步驟，全面盤點你的設定與近期用量：

**第一步：靜態設定審查**

它會先檢查你的底層環境組態：
- 預設模型是不是設成 Sonnet（大部分情境下 Sonnet 比 Opus 省很多，而且完全夠用）。
- Hooks 設了哪些，有沒有失控的 post-hook 會吃 token。
- MCP server 清單，每個 server 都是啟動時的固定開銷。
- Rules 檔案每檔行數，檢查有沒有哪個 rule 膨脹到 >200 行需要拆分。
- Skills 清單，盤點目前掛載的項目。

**第二步：JSONL Session 分析（近 5 個 session）**

這一步是整套健診的核心重點。它會撈出你最近 5 個 session 的 JSONL 紀錄，逐條進行深度解析：
- **Context 使用率**：計算公式是 `(input_tokens + cache_creation + cache_read) / 200000`；如果你使用的是 1M context window 的 session，分母則對應改成 `1,000,000`。算出來就能清楚知道你的 context 目前是用到了 80% 還是 30%。
- **快取時效與類型**：從 `ephemeral_5m_input_tokens` 跟 `ephemeral_1h_input_tokens` 辨識快取狀態。只要使用 Claude 訂閱、且在方案額度內，主對話享有的是 1 小時快取；如果是 subagent 或是吃額外用量的部分，快取時效則是 5 分鐘。
- **Compact 觸發次數**：偵測 `type=system` 訊息中是否有 `summary` 關鍵字，確認對話過程中是否曾觸發過 `/compact`。
- **貼圖後的 cache miss**：以「user content 有 image type + 下一條 assistant cache_read < 500」組合進行偵測，抓出快取是否被貼圖打掉。

跑完這一步，這個 session 花了多少 token、有沒有 auto compact、有沒有被貼圖搞掉快取、context 用到 80% 還是 30%，全部一目瞭然。

**第三步：官方最佳實踐查詢**

很多人會擔心這類檢查規則會不會隨時間過時。cc-audit 在這一步會透過 WebFetch 直接去抓 Anthropic 最新的 Claude Code 官方文檔，拿最新建議來比對你目前的設定差距。因為每次跑都重新線上抓取，給出的建議不會過期。

**第四步：Rules 的 path-specificity 檢查**

檢查你的 rules 檔案是不是應該加上 `paths:` 條件載入。透過這個機制，特定規則只會在相關檔案路徑出現時才載入吃 context，避免無關情境常態佔用。這一招能省下非常多額度，但很多人在設定時都不知道。

## 把健診變成固定的重構習慣

之前我是手動對照文檔逐項修改，常常要花三四十分鐘，還容易看漏。做成 skill 之後變成五分鐘全自動，所有項目一次檢查完畢。

如果你想把這套做法放進日常工作流，最好的時機是配合你的方案重置週期。可以參考我前面寫過的 [Obsidian + Claude Code 工作流](/blog/posts/zh/obsidian-claude-code-workflow)——在額度即將重置的那一天，你暫時變身「單日 token 富翁」，這時候額度最充裕，正是進行環境重構、拆分 rules 與清理設定的黃金時段。

丟這個連結給 Claude Code：<https://github.com/danyuchn/cc-audit>

它會幫你裝好、驗證、然後你打 `/cc-audit` 就開始跑。

<!-- 2026-11-12 舊文盤點整篇重寫：將文末後記對快取時效與上下文視窗公式的修正整合進步驟內文，把檢查流程改為連貫的四大面向，並以清楚的安裝指引作為全文唯一的收尾。 -->
