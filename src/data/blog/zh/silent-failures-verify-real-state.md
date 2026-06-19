---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-18T04:00:00Z
title: "沒拋錯不代表成功：AI 開發裡的五個靜默失敗陷阱"
slug: zh/silent-failures-verify-real-state
featured: false
draft: false
tags:
  - ai-tools
  - gemini
  - debugging
description: '工具沒報錯不等於成功。exit 0、200 response、空字串、被砍頭的值，全都是靜默失敗——回讀驗證真實狀態才是唯一可靠的手段。'
---

這半年累積的開發踩坑，事後回頭看有一條共同的線：最難抓的 bug 都不會拋錯。程式跑完了、API 回 200、CLI 給你 exit 0，結果卻是錯的或空的。我把這類「沒拋錯但失敗了」的陷阱叫做靜默失敗，從自己的程式碼一路到外部 API，每一層都有。

## 1. 你自己的程式碼：`includes('ai')` 把 failed 標成 AI

錯誤分類器用 `includes('ai')` 抓 AI 相關錯誤，結果 `failed` 跟 `available` 全被誤標——因為這兩個字裡都有 `ai`。沒有任何例外，分類數字看起來也很正常，只是全錯。分類關鍵字一律用 word-boundary regex：`/\bai\b/`。

## 2. 函式庫：dotenv 的 `\n` 陷阱砍掉 Resend key

RESEND_API_KEY 在 `.env.local` 裡值的結尾混了字面 `\n`（backslash 加 n 兩個字元，dotenv 的雙引號陷阱），key 被 regex 砍頭。程式不會報錯，要等到實際打 API 拿 401 才知道。SOP：用之前先 `curl GET /domains` 驗證 key 是乾淨的。

## 3. CLI：gemini 在未信任資料夾 exit 0 靜默掛掉

gemini CLI v0.28 之後，headless 模式在「未信任資料夾」會靜默失敗——exit 0 但無輸出，再包一層 `2>/dev/null` 看起來就像正常掛掉。真正的錯誤訊息是 `Gemini CLI is not running in a trusted directory`。修法：加 `--skip-trust`，或設 `GEMINI_CLI_TRUST_WORKSPACE=true`。debug 時先把 `2>/dev/null` 拿掉才看得到訊息。

## 4. API 回應：Gemini thinking budget 設無限回空字串

Gemini 2.5 Flash 一直回 `{}` 空回應，根因是 `thinking.budget_tokens: -1`（無限）——thinking 把整個 token budget 吃完，`content` 就變成 null。回應結構完整、HTTP 200，只是裡面沒東西。3.x 改用 `reasoning_effort`，不要再在 model config 裡帶 `thinking`。

## 5. API 狀態：Resend `scheduled_at` 不可信

設定 `scheduled_at` 排程後，batch 送出時的 response 不能信。回讀 `GET /emails/{id}` 才是真實狀態。如果欄位回讀 null，代表排程沒成功、信已經立刻寄出去了。

## 共同的結論

沒拋錯 ≠ 成功。這五個坑橫跨自己的程式碼、函式庫、CLI、API，唯一可靠的應對方式都一樣：不要相信「沒有錯誤」這個訊號，主動回讀或探測一次真實狀態再往下走。
