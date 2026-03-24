---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-24T04:00:00Z
title: "Claude Code 五個成熟度等級：你不是選擇升級的，是被天花板逼的"
slug: zh/claude-code-five-levels
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: 從 Raw Prompting 到 Orchestration，Reddit 上 778 個讚的框架——每一層存在的原因，是因為上一層壞掉了。
---

很多人說 Claude Code 不穩定，有時候又準又快，有時候就自己亂做。我以前也這樣覺得。

後來看到一個 Reddit 貼文，才意識到問題不是 Claude Code 不穩定，是我一直卡在同一層的天花板沒升上去。

原帖作者 u/DevMoses 整理了五個成熟度等級，底下 157 條留言大量的人說「找到答案了」。

## 核心邏輯

「你不是自己決定升級的，是撞到天花板被迫升級。」

每一層存在的原因，是因為上一層在某個點開始壞掉了。

## 五個等級

| 等級 | 名稱 | 在做什麼 | 會壞在哪裡 |
|------|------|---------|-----------|
| L1 | Raw Prompting | 直接對話描述需求 | 專案變大，agent 開始忘記慣例、引入不一致的 pattern |
| L2 | CLAUDE.md | 在專案根目錄放 context 檔，寫 tech stack、命名規範、禁止事項 | 超過大約 100 行後合規度下降；長 session 品質也跟著衰退 |
| L3 | Skills | `.claude/skills/` 放 SOP 檔案，按需載入，教 agent 怎麼做特定任務 | Agent 照做，但沒人自動檢查品質，你仍是唯一的 QA |
| L4 | Hooks | 生命週期腳本：每次編輯後自動跑 typecheck、完成前設品質門檻、session 開始時載入 context | 仍是單一 agent、單一 session，超過 context window 容量就撐不住 |
| L5 | Orchestration | 平行 agents + isolated worktrees + 跨 session 狀態管理 + 協調層防同檔衝突 | 作者自己跑過 198 agents / 32 fleet sessions，merge conflict rate 3.1% |

每一層都真實有效，直到它撐不住為止。

## 幾個細節值得記

**CLAUDE.md 的天花板**是最多人共鳴的痛點。留言裡大量的人說同一件事：「感覺找到答案了，然後某個瞬間它就不管用了。」作者把自己的 CLAUDE.md 從 145 行縮到 77 行，情況才改善。

**跳級是災難。** 每一層的基礎設施是下一層的前提。從 L2 直接跳 L5，等著出亂子。

**Skills 不是零消耗。** Frontmatter 仍有少量 token 發現成本，不是完全免費的上下文。

**企業級 repo 可能不一樣。** 有幾個數十萬行程式碼的企業用戶說 CLAUDE.md 從未失效，可能跟使用方式和 repo 結構有關。

## 社群提出的 L6

有人在下面補了第六層：讓 Claude 替你打造客製化的 Claude 工作流，系統自我改善。

具體實作：SessionEnd hook 自動提取行為模式 → 夜間 agent 聚合成新的 skills → 測試通過後自動升級。

這已經超出大多數人的需求，但方向是對的——理想狀態是系統知道自己哪裡不夠好，然後自己補。

## 給非開發者

- L3 可以用 custom instructions 近似，不一定要開終端機
- L4 可以透過 prompt 內建手動檢查流程來模擬
- L5 目前幾乎只有開發者有辦法用

這個框架對非開發者的用處，不是要你把五層全走完，而是讓你知道：當 Claude Code 開始犯蠢，下一步要加的不是更多的聊天，是更好的結構。

## 對我的意義

我現在大概在 L3 和 L4 之間。CLAUDE.md 有了，Skills 架起來了，Hooks 只開了一部分。

L5 的 orchestration 我用過幾次，每次都在某個我沒預料到的地方壞掉。

但至少現在我知道，那不是 Claude Code 不穩定，是我的基礎設施還不夠。
