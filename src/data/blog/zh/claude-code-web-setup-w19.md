---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "網頁版 Claude Code 環境設定的兩個世界"
slug: zh/claude-code-web-setup-w19
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - ai-workflow
description: 網頁版 Claude Code 有兩種環境——雲端 VM 跟 Remote-control。這篇整理我實測下來的設定訣竅、會踩到的小 bug，以及為什麼有些設定不能無腦丟到雲端。
---

iOS 版的 Claude App 實在太廢，加上官方更新的重點都在 Desktop App 跟網頁版，所以我手機上都改用網頁版 Claude Code。

實測下來，網頁版有一些訣竅跟小坑值得分享。

## 兩種環境，先搞清楚再說

網頁版 CC 有兩種完全不同的執行環境：

1. **雲端虛擬環境**：在雲端的 VM 上跑
2. **Remote-control**：連回你家不關機的電腦上的 CC session

### Remote-control 比較單純

就是把你家裡那台電腦的 session 換個介面呈現。`claude.md`、rules、hooks、memories、skills、MCP 全部照舊。

目前發現兩個小 bug：

- 打斜線只會出現官方預設指令跟 skill 提示，自己裝的自訂指令不會出現在提示選單。但你打入全名或口頭講要觸發，還是可以正常觸發。
- bypass 模式沒有正常顯示在網頁版切換按鈕，最多只給到 Auto。需要 bypass 請改用 CLI 或其他方式。

### 雲端虛擬環境就有學問了

啟動 VM 時會注入 system-reminder，包含 `claude.md`、rules、skills、mcp、環境資訊等等。但這些 `.claude/` 裡的東西，是從你的遠端倉庫拉的。所以你必須確保 `.claude/` 裡的這些東西沒有被 `.gitignore` 掉，遠端倉庫看得到。

但整個設定資料夾 commit 進去也不好——裡面有一大堆很臃腫的歷史對話紀錄 jsonl，這些應該被排除，不該進遠端倉庫。

幾個關鍵差異：

- **只有 project-level 的 `.claude/` 在雲端讀得到**。專案內的 `.claude/`（會 commit、可在雲端讀到）跟根目錄的 `~/.claude/`（user-level，不會 commit、雲端讀不到）差距很明顯。
- **只有遠端 MCP 會生效**，本機 server MCP 通通不能用。極大限制了遠端定期排程的可用性。
- **某些敏感環境變數依照正確資安觀念不該被 commit**，所以 Claude Code 網頁版可以設定虛擬環境的 env，同一也可以設定在虛擬環境啟動前載入哪些設定腳本。

## 實際感想

網頁版的兩個世界各有用處：Remote-control 適合「我電腦在跑、人在外面」的情境；雲端 VM 適合「乾淨環境跑某個專案」的情境。但要把 user-level 的設定遷移到雲端，要有心理準備——基本上等於重寫一份適合雲端的精簡版 `.claude/`。

實際的設定圖卡如下：

![網頁版 Claude Code 環境設定（一）](/blog/assets/posts/claude-code-web-setup-w19/web-setup-1.jpg)

![網頁版 Claude Code 環境設定（二）](/blog/assets/posts/claude-code-web-setup-w19/web-setup-2.jpg)
