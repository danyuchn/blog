---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-17T04:00:00Z
title: knowledgeC.db 查出來的有趣數字
slug: zh/knowledgec-db-time-audit
featured: false
draft: false
tags:
  - ai-daily-use
  - personal
description: '叫 agent 讀 macOS 的 knowledgeC.db，查出近 14 天的 App 使用時間分布，Ghostty 跟 Chrome 幾乎打平。'
---

Mac 電腦的使用者，跟你的 agent 說：

```
look at ~/Library/Application Support/Knowledge/knowledgeC.db and tell me some interesting fact
```

你會發現有趣的東西。

![knowledgeC.db 查出來的使用時間統計](/blog/assets/posts/knowledgec-db-time-audit/knowledgec-stats.jpg)

近 14 天的資料（資料庫實際記到 2026-09-12，最早回溯到 7/16），幾個數字：Ghostty 與 Chrome 幾乎打平，各約 31.6hr／31.1hr，是這台機器上耗最多時間的兩個 App。Codex CLI（com.openai.codex）7.0hr、455 個 session，次數比 Chrome/Ghostty 少很多但單次都很短，符合 CLI 派工的模式。LINE 3.7hr，其餘 App（Typora、Preview、QuickTime、Finder）都在 1hr 以內。一天裡最活躍的時段是晚上 8 點（458 分鐘累計），其次是下午 15、上午 8、下午 14、晚上 19 點，沒有單一離群尖峰，工作時間分布相對均勻。

注意：這個資料庫受 TCC 保護，記錄的是裝置使用行為（非對話內容），純屬本機好奇心用途，沒有寫出或外傳。

<!--
新增非原文句子清單（忠實度自首）：
1. 「近 14 天的資料（資料庫實際記到 2026-09-12，最早回溯到 7/16），幾個數字：」— 類型：銜接（把圖中條列文字串成段落的引導句）
2. 「注意：這個資料庫受 TCC 保護，記錄的是裝置使用行為（非對話內容），純屬本機好奇心用途，沒有寫出或外傳。」— 類型：改寫（圖中原句照搬保留，未新增觀點）
-->
