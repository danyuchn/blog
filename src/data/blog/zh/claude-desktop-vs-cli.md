---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:00:00Z
title: "Claude Desktop App 改版了——以及我為什麼還是用終端機"
slug: zh/claude-desktop-vs-cli
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: Claude 推出了改版的桌面應用程式，設計更漂亮、對新手更友善。但如果你問我要用哪個，答案還是 CLI。不是情懷，是功能差距和資源效率的問題。
---

Anthropic 這週更新了 Claude 的桌面應用程式，設計改版了，更漂亮，介面也更友善。終端機本來就會嚇跑不少人，有個漂亮的 GUI 入口確實降低了門檻。

![Redesigning Claude Code on desktop for parallel agents](/blog/images/claude-desktop-redesign.jpg)

但如果你問我日常用哪個，答案還是終端機。

## 更新節奏的差距

Claude Code CLI 現在幾乎每天有 1 到 2 個版本更新。桌面版 App 的更新週期大概是 2 到 4 週。

這個差距不只是版本號的問題。幾乎所有的新功能、性能修復、行為改善，都會先在 CLI 上線，桌面版往往要等好幾個禮拜才跟上。

上週的 2.1.100，修掉了大型檔案 JSON 跳脫導致 token 虛耗的問題，還修掉了長 session 記憶體暴增的 bug。這兩個問題我在 CLI 這邊當天就拿到修復，桌面版用戶還得再等一段時間。

如果你認真用 Claude Code 做工作，這個落差是切實的代價。

## 資源效率的差距

我的主力機是 M2 MacBook Air。開著 Claude Desktop App 做其他事會明顯感到卡頓，整台機器的反應明顯遲鈍。

終端機的 Claude Code CLI 幾乎沒有這個問題。我現在平常開著 3 個 Ghostty 視窗，每個視窗裡有 3 到 4 個 pane，跑 5 到 6 個 Claude session 同時工作，系統沒什麼負擔。

純 terminal 應用本來就住在電腦底層，對 GUI 那層的開銷是零。

## 一個很多人不知道的問題

桌面版 App 跟 CLI 讀的是**完全不同的設定檔**，而且兩邊不互相繼承。

| 環境 | 設定檔位置 |
|------|-----------|
| Claude Code CLI | `~/.claude.json` |
| Claude Desktop App | `~/Library/Application Support/Claude/claude_desktop_config.json` |

這代表你在 CLI 裝的 MCP server、設定的環境變數、配置的 PATH，桌面版 App 一概不知道。

桌面版 App 有一個額外的限制：它不繼承 shell 的 PATH 環境變數。所以如果你在設定檔裡填 `uvx` 這種命令，桌面版找不到，要填完整路徑（例如 `/Users/danyuchn/.local/bin/uvx`）。

每次裝新 MCP 都要記得兩邊都設定一遍。這件事本身沒有什麼大不了，但如果你不知道這個差異，在桌面版裡找不到某個 MCP，很可能會繞很久才發現根本原因只是設定檔不同。

## 建議

Desktop App 對入門者來說是一個很好的起點。它降低了「我還沒習慣終端機」這個心理門檻，設計確實也比黑底白字的終端機友善多了。

但如果你已經用 Claude Code 做正式工作，長期來說搬到 CLI 是對的。更新節奏快、資源效率好、設定靈活度高——這些加起來每天都有感。
