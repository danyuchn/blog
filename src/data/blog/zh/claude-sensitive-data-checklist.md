---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-08T04:00:00Z
title: "用 Claude 處理敏感資料前必知"
slug: zh/claude-sensitive-data-checklist
featured: false
draft: false
tags:
  - claude
  - security
  - enterprise
  - ai-tools
description: '用 Claude 處理敏感資料前該知道的事：資料保留時間、Enterprise 合約保障、輸入最小化、Coding Agent 控制與替代架構。'
---

把敏感資料丟給 Claude 之前，幾件事先弄清楚。

## 資料保留時間

- 刪除後最多殘留後端 30 天
- ClaudeCode API logs：7 天
- Enterprise + ZDR：零保留（需主動申請）
- 協助改善 Claude：去識別化最多 5 年
- 違規對話：最多 2 年

## Enterprise 合約保障

- 承諾不存儲、不訓練、可審計、違約可提告
- ZDR 不適用所有功能（如 CoWork）
- 上傳檔案需透過 Compliance API 刪除
- 訴訟中可被強制取得，不受律師保密特權保護

## 輸入最小化原則

- Secrets/credentials 禁止貼入，改用佔位符
- 客戶資料先移除姓名、email、ID、log
- 只給任務所需最小資訊

## Coding Agent 控制

- Denylist `.env`、secrets、credentials 路徑
- 用 staging 憑證，勿用正式憑證
- 部署前人工審查 PR/diff
- CI 加入 secret scanner 和 log scanner

## 替代架構

- AWS Bedrock：呼叫留在自家 cloud 帳戶
- 自架本地 LLM：最高隔離，能力受限

<div class="video-embed">
<iframe src="https://www.youtube.com/embed/aSHfh5Vz1BA" title="YouTube video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
