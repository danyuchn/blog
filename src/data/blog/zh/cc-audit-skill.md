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
description: 把我之前整理的一千多讚的省額度技巧全部做成 skill。丟給 Claude Code 安裝後，它會逐條檢查你的設定、近期 session、rules 膨脹、context 用量，給出可執行的修正清單。
---

Claude 最近額度亂搞，大家罵歸罵，Claude 還是得繼續用。前陣子我整理了一大串省額度的技巧發在 Threads 上，收穫一千多讚之後，有網友提議可以做成 skill。

所以我就做好放在這邊了：<https://github.com/danyuchn/cc-audit>

把連結丟給 Claude Code 請他幫你裝就好了。

## 它在做什麼

cc-audit 是一個健診 skill。觸發後它會跑四個步驟，最後給你一份結構化報告和可執行建議清單。

### Step 1：靜態設定審查

- 預設模型是不是設成 Sonnet（大部分情境 Sonnet 比 Opus 省很多，而且夠用）
- Hooks 設了哪些，有沒有失控的 post-hook 吃 token
- MCP server 清單，每個都是啟動時的固定開銷
- Rules 檔案每檔行數——看有沒有哪個 rule 膨脹到 >200 行需要拆分
- Skills 清單

### Step 2：JSONL Session 分析（近 5 個 session）

這一步是重點。它會撈你最近 5 個 JSONL 檔，逐條計算：

- **Context 使用率**：`(input_tokens + cache_creation + cache_read) / 200000`
- **快取類型**：從 `ephemeral_5m_input_tokens` 跟 `ephemeral_1h_input_tokens` 分辨你吃的是 Pro 的 5 分鐘快取還是 Team/Enterprise 的 1 小時快取
- **Compact 觸發次數**：`type=system` 訊息中有 `summary` 關鍵字代表觸發過 `/compact`
- **貼圖後的 cache miss**：用「user content 有 image type + 下一條 assistant cache_read < 500」組合偵測

跑完你會看到「這個 session 花了多少 token、有沒有 auto compact、有沒有被貼圖搞掉快取、context 用到 80% 還是 30%」——全部一目瞭然。

### Step 3：官方最佳實踐查詢

這一步它會 WebFetch 去抓 Anthropic 最新的 Claude Code 文檔，比對你目前的設定跟官方建議有多遠。我寫的這些建議會不會過時？不會，因為它每次跑都重新抓。

### Step 4：Rules path-specificity 檢查

檢查你的 rules 是不是應該加 `paths:` 條件載入，讓它只在相關檔案路徑出現時才吃 context。這一招省很多，很多人不知道。

## 為什麼不直接看 `/stats`？

Claude Code 內建的 `/stats` 只告訴你「這個 session 用了多少 token」，但沒告訴你：

1. 為什麼這麼多
2. 哪幾個設定是元兇
3. 下一步該改什麼

cc-audit 的輸出格式是可執行建議清單。每一條都對應到具體的檔案、具體的行數、具體的修改。你不用自己對照文檔猜。

## 養成習慣

我自己的用法是每週 Claude Max 重置那天跑一次 cc-audit，配合我前面寫過的 [Obsidian + Claude Code 工作流](/blog/posts/zh/obsidian-claude-code-workflow)——額度即將重置的那一天，你暫時變身「單日 token 富翁」的時候，正是你做這種重構的好時機。

之前我是手動對照文檔改，花三四十分鐘。做成 skill 後變成五分鐘全自動，還不會漏掉項目。

丟這個連結給 Claude Code：<https://github.com/danyuchn/cc-audit>

它會幫你裝好、驗證、然後你打 `/cc-audit` 就開始跑。
