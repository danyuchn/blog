---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-11T04:00:00Z
title: "Astra 探路、Luna Max 收工：反爬太徹底又太小眾的網站怎麼爬"
slug: zh/astra-scout-then-weak-model-crawl
featured: false
draft: false
tags:
  - ai-workflow
  - ai-coding
  - ai-tools
description: '反爬做得很徹底、又小眾到沒有第三方爬蟲公司 cover 的網站，先派 Astra 探路寫成 SKILL，再交給 Luna Max 自動批次跑的爬蟲心法。'
---

偷偷說，最近自己摸索出的 Astra 神級用法。

先講清楚前提：這篇講的是不需要登入的公開網站，跟我之前寫的[需要登入的網站別硬爬](/blog/posts/zh/your-machine-is-the-attack-surface)是兩回事，不衝突。

面對一些網站要爬蟲，對方的反爬做得很徹底，但是又太小眾，導致第三方爬蟲公司都沒有 cover 時：

1. 派 Astra 去探索網站，用他優秀的瀏覽器操控天賦小批量嘗試。
2. 把過程寫成詳細的技術文檔／SKILL，指明未來要給較弱的模型使用。
3. 切成 Luna Max + goal，讓他自己設定隨機批次隨機間隔，照著操作你的瀏覽器就對了。時間不是重點。

我已經用這個方法，一週內爬下了一個論壇的三千多個頁面，目前還沒有出事（出事再上來跟大家報告）。20USD 的週額度耗費不到 30%。

<!--
新增非原文句子清單（忠實度自首）：
1. 「先講清楚前提：這篇講的是不需要登入的公開網站，跟我之前寫的需要登入的網站別硬爬是兩回事，不衝突。」 — 類型：框架句（本篇唯一允許新增的觀點句，用於區隔立場相反的站內舊文）
-->
