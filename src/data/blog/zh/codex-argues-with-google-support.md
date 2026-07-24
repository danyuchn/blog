---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: Codex 自己做了一份證據包，跑去跟 Google 真人客服吵架
slug: zh/codex-argues-with-google-support
featured: false
draft: false
tags:
  - codex
  - security
  - case-study
description: 'PDT Learning 一支 Gemini backend key 外洩被盜刷、沒設 spending cap 怒噴 1000 USD，我用 Codex 的瀏覽器操作去跟 Google 真人客服爭費用，它認真到自己生出一份 15 頁證據包發給對方。'
---

Codex 強大的瀏覽器操作功能又有一新用途：自動幫我跟 Google 真人客服對話吵架。

馬的，API key 洩漏沒設 spending cap，怒噴 1000 USD。

事情是 PDT Learning 有一支 Gemini backend 的 API key 外洩被盜刷，因為沒設 spending cap，直接燒出約 1000 美元的異常費用。我把跟 Google Cloud 真人客服爭取費用調整這件事交給 Codex 的瀏覽器操作能力去跑，結果它吵到自己主動做證據包然後發給對方。

那份證據包是一份完整的英文資料：15 頁的 PDF、一份 DOCX、raw evidence、support transcript、screenshots、manifest、hashes，全都建好放在 Downloads 裡，而且刻意不含實際的 key 值。Google Cloud Support 的 Case #73506704 已經受理費用調整，等 32 小時帳務傳播跟 internal review。

## 荒謬歸荒謬，善後還是得做

費用可以吵，洞還是得補。我精準刪除、輪換了那把遭濫用的 backend key，追溯到有兩支 private-repo 的測試腳本曾經含明文憑證（確切的外洩路徑到現在還是不明），已經把明文移除、改由 Secret Manager 提供。

接著幫 7 個付費 AI Functions 全部補上防護：Firebase Auth、App Check、Firestore 持久化的 per-user／per-action rate limit、action allowlist、user-ID 檢查，還有 `maxInstances`。production 全部 ACTIVE，匿名探測 `analyzeQuestion`、`toolAction` 都回 401。

案子拖到週末都還沒完。我後來才發現，Google support 的 billing 跟 technical 是兩個互不包含的追蹤入口：billing 列表只看得到退款的 case #73506704，technical 列表只看得到降限的 case #73501463，兩案得分頭查詢才拼得出全貌。7/21 之後零回音，我從 Cloud Console 案件頁送了催件，問傳播完成沒、review 狀態、調整範圍。另一個案子 #73501463 三個工作天沒回，跑出一封自動催辦信，查證 DKIM／SPF／DMARC 都過、確認是真的通知不是釣魚後，用 gog reply-all 回覆並把它關聯到費用調整案，避免原案自動關閉。順手測了本機 `~/.credentials/env-secrets` 的那把 `GEMINI_API_KEY`，HTTP 200 有效，確認不是同一把——真正被盜的那把 7/21 就已經刪掉輪換完了。

就這樣，還在等 Google review。

<!--
新增非原文句子清單（忠實度自首）：
1. 「事情是 PDT Learning 有一支 Gemini backend 的 API key 外洩被盜刷，因為沒設 spending cap，直接燒出約 1000 美元的異常費用。」 — 類型：框架句（把素材 A 的情緒貼文與素材 B 的事件全貌接起來，事實均來自素材，措辭為新增）
2. 「我把跟 Google Cloud 真人客服爭取費用調整這件事交給 Codex 的瀏覽器操作能力去跑，結果它吵到自己主動做證據包然後發給對方。」 — 類型：改寫（合併素材 A 的 POST 與 REPLY，改為敘事句）
3. 「那份證據包是一份完整的英文資料」 — 類型：銜接（引出素材 B 的證據包清單）
4. 「荒謬歸荒謬，善後還是得做」 — 類型：框架句（分節標題，銜接兩段語氣反差）
5. 「費用可以吵，洞還是得補。」 — 類型：銜接（承接上下文的轉折，未新增觀點）
6. 「案子拖到週末都還沒完。」 — 類型：銜接（引出素材 C 的後續追蹤）
7. 「就這樣，還在等 Google review。」 — 類型：框架句（結尾短促收束，事實「還在等 review」來自素材 B/C）
其餘句子（Case #73506704、15 頁證據包各項、7 個付費 AI Functions、Firebase Auth/App Check/rate limit/allowlist、401、billing 與 technical 兩線互不相通、#73501463、DKIM/SPF/DMARC、GEMINI_API_KEY HTTP 200 等）均為素材 A/B/C 逐字或直接改寫，非新增論點。
-->
