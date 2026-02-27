---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-27T04:00:00Z
title: "claude-work-timer：讓 Claude Code 自動算工時"
slug: zh/claude-work-timer
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - open-source
description: "用 Claude Code 接案按時計費，甲方要看工時怎麼辦？寫了一個開源外掛自動算。"
---

## 問題

用 Claude Code 的人越來越多，也越來越多開發者拿它來處理客戶的專案（包括我）。但有一個需求一直沒被滿足：怎麼精確記錄 Claude Code 的工時？

按時計費的案子，甲方隨時都會要工時紀錄。厲害的人用 Claude Code 通常都是好幾個視窗分割，同時並行四五個專案。你要怎麼準確算出某個專案實際花了多少時間——包括對話、讀取、寫入、工具調用——扣掉中間去喝咖啡或回訊息的閒置時間，然後拿給甲方看？

找了一圈，沒人做這個。所以我自己寫了一個。

## claude-work-timer

[claude-work-timer](https://github.com/danyuchn/claude-work-timer) 是一個開源的 CLI 工具，安裝後會自動讀取你的 Claude Code session 歷史紀錄，計算精準的對話時間跟工具調用時間。

做的事很簡單：

- 讀取 session 的 JSONL 歷史紀錄
- 計算每一輪對話和工具調用的實際耗時
- 超過 5 分鐘的閒置時間自動扣除
- 剩下的就是你真正的工時

支援按專案篩選，所以就算你同時開了五個專案，也能分別算出每個專案的工時。

## 安裝跟使用

最簡單的方式：把 GitHub 連結丟給 Claude Code，請他幫你裝、幫你查某個專案的工時，他就會自動搞定。

或者手動安裝：

```bash
npm install -g claude-work-timer
```

查看工時：

```bash
claude-work-timer --project /path/to/your/project
```

GitHub repo：[github.com/danyuchn/claude-work-timer](https://github.com/danyuchn/claude-work-timer)
