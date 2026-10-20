---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-20T13:31:00Z
title: 卡住你的是預設開著的那道牆：Codex 沙盒、ENV_SCRUB、Vercel 保護、官方 connector
slug: zh/default-guardrails-that-block-you
featured: false
draft: false
tags:
  - developer-experience
  - security
  - gotchas
description: '內網 NAS 讀不到、AUTOMODE 回不去、外部訪客拿到 401、雲端排程寄不了信，四個坑都不是程式寫錯，是預設開著的保護。'
---

這幾個坑的共通點是：卡住你的不是程式寫錯，是某個預設開著的保護。

## Codex 的沙盒

去客戶公司現場做 Codex 培訓，公司內網 NAS 掛載磁碟讀不到就是讀不到。各種排查都沒用很絕望時，突然想起：是不是 Codex 的沙盒在搞鬼？果然，口頭授權在沙盒外面嘗試，就讀到了。

## ENV_SCRUB 打開，AUTOMODE 就回不去

冷知識：如果 `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1`（變數剝離這個設定打開），AUTOMODE 就無法變成 default，default 會是 manual。

## Vercel 臨時公開頁

新 project 部署出來的 URL 預設開著 Deployment Protection（Vercel Authentication），外部訪客拿到 401。另一坑：`<proj>.vercel.app` 裸別名可能是別人佔走的空殼，自家自動更新的 prod 別名是 `<proj>-<team>.vercel.app`。發連結前先 curl 驗內容。

## 雲端只吃官方 connector

之前好幾位客戶就是卡在想設置雲端排程寄每日市場週報、或寫入 Google Sheet 表單——雲端 server 只吃官方 connector，以前最多只能寫草稿或在 Drive 創立全新檔案。現在官方 MCP 開放了寄送信件跟更新現有檔案。
