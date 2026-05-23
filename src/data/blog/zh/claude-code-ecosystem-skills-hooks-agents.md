---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-23T05:00:00Z
title: "Claude Code 生態系盤點——Skill、Hook、Agent 全面開花"
slug: zh/claude-code-ecosystem-skills-hooks-agents
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - ai-tools
description: 'Claude Code 的生態系已經從單純的 CLI 工具長成一個完整的平台：Skill 各家都支援、Hook 攔截指令、Agent View 多工管理、fork subagent 繼承上下文。連社群都開始用 Skill 搞創意了。'
---

Claude Code 的生態系在過去幾個月長得很快，從單純的 CLI 工具變成一個有 Skill、Hook、Agent、Subagent 的完整平台。整理一下目前的全貌。

## Skill——各家都支援了

Skill 已經不是 Claude Code 的專利。Codex 支援、Gemini 也支援。但生態跟成熟度差距還是很大——Claude Code 的 Skill 生態目前最活躍，社群貢獻的 Skill 數量遠超其他平台。

社群的創意也很有趣。有人做了一個叫 `moyu` 的 Skill：離職前把自己寫的代碼轉成屎山，真正達到了「人走了，陰魂不散」的境界。還有人腦洞大開，想用 `/schedule` 排程每週一出門前自動生成週末假故事、每天出門前生成假成就，自動發到信箱，通勤時閱讀一分鐘，到公司就能跟同事胡吹。

玩笑歸玩笑，這些案例反映的是 Skill 的核心價值：把重複的工作流封裝成一個指令，不管內容是正經的還是搞笑的。

## Hook——攔截指令的守門員

Hook 是比 CLAUDE.md 更強制的機制。CLAUDE.md 寫的是建議，模型可以選擇忽略；Hook 是系統層級的攔截，模型繞不過去。

社群有人做了一個 vague-prompt-detection hook：掛上去之後，它會攔截每一個使用者送出的指令，判斷是否模糊。清晰的直接放行，模糊的就觸發 Skill 追問 1-6 個問題。對於常常語焉不詳的使用者來說很實用。

## Agent View——多工管理

Claude Code 推出的 Agent View 功能，可以一次管理好幾個 Session 協同完成任務。用法是升級到最新版 CLI，打 `claude agents` 啟動。

這解決了一個長期的痛點：以前要開多個終端機視窗分別跑不同 agent，現在有統一的介面管理。

## Fork Subagent——繼承還是隔離

實驗功能中的 fork subagent 可以繼承主 agent 的上下文。另一個實驗功能 Agent Team 則是主 agent 作為 manager 分派任務，跟 team member 對話。

用了 fork 之後要注意一件事：之後都要非常明確地跟主 agent 講要不要繼承上下文。不然它會一律用繼承上下文的 forked agent——可是有時候做 audit 就是不想讓它球員兼裁判。隔離上下文的獨立審查，反而更有價值。

## 生態系的意義

這些功能單獨看都是小工具，但組合起來就是一個完整的工作流平台。Skill 封裝流程、Hook 強制規則、Agent 分工協作、Subagent 決定隔離或繼承。

對於每天重度使用 Claude Code 的人來說，這些不是錦上添花，是基礎設施。
