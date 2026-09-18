---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-17T04:00:00Z
title: The interesting numbers hiding in knowledgeC.db
slug: en/knowledgec-db-time-audit
featured: false
draft: false
tags:
  - ai-daily-use
  - personal
description: 'I told my agent to read macOS knowledgeC.db, and the 14-day usage breakdown showed Ghostty and Chrome nearly tied.'
---

If you're on a Mac, tell your agent:

```
look at ~/Library/Application Support/Knowledge/knowledgeC.db and tell me some interesting fact
```

You'll find something interesting.

![The usage time statistics pulled from knowledgeC.db](/blog/assets/posts/knowledgec-db-time-audit/knowledgec-stats.jpg)

From the last 14 days of data (the database actually logs through 2026-09-12, going back to 7/16), a few numbers stand out. Ghostty and Chrome are nearly tied at about 31.6hr and 31.1hr, the two apps eating the most time on this machine. Codex CLI (com.openai.codex) comes in at 7.0hr across 455 sessions, far fewer sessions than Chrome or Ghostty but each one short, which fits the CLI dispatch pattern. LINE is at 3.7hr, and everything else (Typora, Preview, QuickTime, Finder) stays under an hour. The most active hour of the day is 8pm (458 cumulative minutes), followed by 3pm, 8am, 2pm, and 7pm. No single outlier spike, just a fairly even spread across the working day.

One note: this database is TCC-protected and logs device usage behavior, not conversation content. This was purely out of personal curiosity, and nothing was written out or shared elsewhere.

<!--
新增非原文句子清單（忠實度自首）：
1. 「From the last 14 days of data (the database actually logs through 2026-09-12, going back to 7/16), a few numbers stand out:」— 類型：銜接（把圖中條列文字串成段落的引導句，對應 zh 版）
2. 「One note: this database is TCC-protected and logs device usage behavior, not conversation content. This was purely out of personal curiosity, and nothing was written out or shared elsewhere.」— 類型：改寫（圖中原句翻譯保留，未新增觀點）
-->
