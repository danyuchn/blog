---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-20T04:00:00Z
title: "Obsidian + Claude Code：我的日常知識管理工作流"
slug: zh/obsidian-claude-code-workflow
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - productivity
description: 把人生都放到 Obsidian，再讓 Claude Code 接入。日誌怎麼記、待辦怎麼管、為什麼本地 Markdown 勝過 Notion。
---

我的 Obsidian vault 裡面存放了日記、工作日誌、靈感、想法、各專案的連結、所有大大小小待辦事項。然後用 Claude Code 接入，讓 AI 能直接讀寫這些資料。

這不是什麼酷炫的架構，就是很樸素的「把東西放在一個地方，讓 AI 也看得到」。但效果出奇地好。

## 日誌：/obsidian log

`/obsidian` 的 log 功能非常好用。它可以把你在一個對話視窗中完整的工作打上時間標籤記錄到日誌裡。

平常工作完一個段落，打 `/obsidian log` 就自動記錄。每個禮拜把 daily log 彙整成週報，就可以清楚知道過去做了哪些事情。不用刻意寫日報，工作本身就是日報。

## 待辦：阻塞與非阻塞

把人生都放到 Obsidian，跟 Claude Code 接入的好處是：它可以隨時告訴我哪些是阻塞待辦（需要別的東西完成或別人配合才能做的），哪些是非阻塞待辦（現在馬上就能辦到的）。

然後在我跟 Claude Code 工作的間隙，它會自動處理非阻塞的項目。我常常問 Claude「今天我要做什麼」，它會從 vault 裡面撈出所有待辦，幫我排序，然後一邊聊一邊把能做的先做掉。

## 額度重置日的固定儀式

每週額度即將在一天內重置，你暫時變身「單日 token 富翁」的時候，趁這時開計畫模式：

一、開給它全電腦權限，掃描所有使用 Claude Code 的專案，給出過時和暫存檔案的歸檔清理建議。

二、用 claude-log CLI 讀取本週所有 session 的對話紀錄，找到跟 Claude Code 溝通不順的地方，然後用官方文檔的最佳實踐修正 Claude.md、rules、memory。

相信我，這會讓你接下來一週過得很愉快。

## 為什麼 Obsidian 勝過 Notion

一個字：本地。

資料都在本地 md 格式。哪天 Obsidian 消失了，資料還是會在。Notion 的資料在雲端，匯出格式有限，而且你永遠不知道他們什麼時候改 API、改定價、改政策。

更重要的是，本地 md 檔案可以直接被 Claude Code 讀寫，不需要任何中間層。Notion 需要 API 串接，多一層就多一個斷點。

簡單、可靠、不依賴任何服務商。這才是知識管理工具該有的樣子。
