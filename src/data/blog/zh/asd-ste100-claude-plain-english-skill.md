---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: 讓 Claude 說人話：一套飛機維修手冊的簡化英文標準
slug: zh/asd-ste100-claude-plain-english-skill
featured: false
draft: false
tags:
  - claude
  - ai-tools
  - skills
description: 'Claude 從 4.7 起就不說人話，我一度以為是自己英文太差，直到上 Reddit 才發現老外也在抱怨；後來我把飛機維修手冊在用的簡化英文標準 ASD-STE100 做成 skill，終於看得懂它的英文了。'
---

前陣子才在抱怨，Claude 從 4.7 起就不說人話。我一度以為是我英文太差，後來上 Reddit 一看才發現老外也在抱怨。

但你聽過 ASD-STE100 嗎？它是一套國際通用的簡化英文標準，最早是用在飛機維修手冊，目的是讓非母語人士也能清楚理解英文技術文件的內容。文法簡化、規範用詞，避免單字量有限的讀者誤解。

舉個例子：

> The valve should be rotated and tested before continuing.

會被改成：

> Turn the valve. Do a test of the valve. Continue the procedure.

所以我就把它做成 skill，每次 Claude 又在吊書袋的時候就給它催下去，從此之後我終於看得懂它的英文了。

<https://github.com/danyuchn/asd-ste100-skill>

<!--
新增非原文句子清單（忠實度自首）：
零新增。全篇逐字沿用原 Threads 貼文，僅將平台短段落織成部落格段落、把 before/after 例子改為 blockquote 呈現、裸連結改為 autolink。無任何 AI 新增的句子或論點。
-->
