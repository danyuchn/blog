---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-30T04:00:00Z
title: "PII Guard TW：為台灣打造的個資去識別化工具"
slug: zh/pii-guard-tw
featured: false
draft: false
tags:
  - ai-tools
  - ai-security
description: 台灣的個資格式沒有現成的去識別化工具。所以我自己做了一個，讓機敏資料不離開你的電腦就能安全送 AI 處理。
---

最近在用 AI 處理客戶資料時，客戶明確希望機敏資料不該送去 AI 伺服器。但我在找去識別化工具時發現一個問題：台灣的個資格式——身分證、手機、統編——沒有現成的工具支援。

所以我結合了國外的開源套件跟本地化的修改，做了 [pii-guard-tw](https://github.com/danyuchn/pii-guard)。它可以把文件裡的個資自動替換成佔位符，讓你丟給 AI 處理完再還原回來。真實資料全程不離開你的電腦。

## 支援偵測的個資類型

- 身分證字號、居留證號、護照號碼
- 手機號碼（09 開頭 / +886）、市話
- Email、信用卡號
- 統一編號、車牌、出生日期、銀行帳號
- 人名、組織名、地名（透過 CKIP BERT 中研院模型辨識）

## 支援的檔案格式

- 純文字（.txt / .csv / .tsv）
- Excel（.xlsx）— 逐格處理，保留格式
- Word（.docx）— 段落加表格都處理
- PDF（.pdf）— 提取文字後處理

## MCP 整合

也有 MCP server 可以直接接 Claude Code，在你的工作流中無縫使用。

現在還是很草創，歡迎大家提 issue 跟 PR。

## 給 API / Enterprise 用戶的補充

Claude API 和 Enterprise 用戶可以參考官方的 ZDR（Zero Data Retention）政策，資料本來就不會留著。一般訂閱用戶除了用去識別化工具之外，也要記得去設定裡把「同意用我的資料訓練模型」關掉，這樣你的資料就只會在 Anthropic 存 30 天，而不是五年。
