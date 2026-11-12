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
description: 'Claude Code 已從單純的 CLI 演進為具備 Skill、Hook 與多代理協同的完整平台。了解如何透過架構組合流程與控制上下文，能讓日常自動化更加穩固。'
tldr: '只把 Claude Code 當成單純對話工具，常會遇到規則被忽略、開好幾個視窗難以管理，或讓 AI 自我審查卻陷入球員兼裁判的盲區。善用封裝重複流程的技能模組、強制攔截模糊指令的系統守門機制、統一管理多工的 Agent View，並在獨立審查時關閉預設繼承前文的設定，就能建立穩定的自動化體系。'
---

很多人剛接觸 Claude Code 時，只把它當成一個在終端機裡幫忙寫程式碼的 CLI 工具。但在短短幾個月內，它的形態已經完全不同——從最初單純的命令列對話，迅速演變為具備 Skill、Hook、Agent View 到 Subagent 的完整架構。

這不再只是一個單點輔助工具，而是一套可以自訂規則、封裝流程、甚至派發多代理協同作戰的工作流平台。整理這套生態的全貌，有助於看清這些組件如何互相搭配，成為日常工作流的骨幹。

## Skill——各家都支援了

Skill 已經不再是 Claude Code 的專利，目前 Codex 支援，Gemini 也支援。但在生態豐富度與成熟度上，彼此差距依然明顯——Claude Code 的 Skill 生態依舊最為活躍，社群貢獻的 Skill 數量遠超其他平台。

部落格裡幾個我自己在用的 Skill，可以看出它實際能做什麼：[cc-audit](/blog/posts/zh/cc-audit-skill) 逐條檢查你的設定、近期 session 與 context 用量，列出省額度的修正清單；[ASD-STE100 與 ISO 24495 兩個 skill](/blog/posts/zh/plain-language-skills-asd-and-iso) 讓 AI 改用簡明語言回話；[Remotion Skill](/blog/posts/zh/remotion-claude-code-videos) 從口白討論到剪輯渲染，半小時做出一支教學影片；[文檔審查 SKILL](/blog/posts/zh/review-loop-my-context-window) 讓 agent 先出完整提案、我錄音審查、它再改版。

這些案例共通的是 Skill 的核心價值：把重複的工作流封裝成一個指令，需要時才載入（載入機制見 [Claude Code Skills 機制解密](/blog/posts/zh/claude-code-skills-mechanism)）。

## Hook——攔截指令的守門員

如果說 Skill 負責擴充能力，Hook 扮演的角色就是系統底層的守門員。

很多人習慣把規則寫在 CLAUDE.md 裡，但 CLAUDE.md 寫的本質上是給模型的建議，模型在某些情況下依然可能選擇忽略。Hook 則是系統層級的攔截，模型繞不過去。

例如社群中有人開發了 vague-prompt-detection hook。掛載上去之後，它會即時攔截使用者送出的每一個指令並評估清晰度：清楚的指令直接放行；若判定過於模糊，就會主動觸發 Skill 追問 1 到 6 個問題。對於常常指令語焉不詳、導致模型產出不如預期的使用者來說，這種防護非常實用。

## Agent View——多工管理

這解決了一個長期的痛點：以前要開多個終端機視窗分別跑不同 agent，現在有統一的介面管理。

Claude Code 推出的 Agent View 功能，只要升級到最新版 CLI，在終端機輸入 `claude agents` 即可啟動，一次管理好幾個 Session 協同推進工作。

除了介面整合，另一項實驗功能 Agent Team 則更進一步，由主 agent 擔任 manager 的角色負責拆解並分派任務，直接跟底下的 team member 展開對話與合作。

## Fork Subagent——繼承還是隔離

過去處於實驗階段的 fork subagent，核心特色在於可以完整繼承主 agent 的上下文。然而，繼承上下文是一把雙面刃。在需要連續上下文的開發場景中雖然方便，但當我們需要進行 audit 或獨立審查時，如果子代理全盤接收主 agent 的思維與背景，很容易陷入球員兼裁判的盲區。在這種情境下，隔離上下文的獨立審查，反而更有價值。

值得注意的是，這項機制從 2026 年 8 月的 v2.1.232 起就已經脫離實驗階段，變成系統的預設行為。這意味著現在每個人調度子代理時，都必須非常明確地對主 agent 說明這次到底要不要繼承上下文；若未特別指定，系統一律會自動啟動繼承上下文的 forked agent。如果你的工作流需要徹底停用這項 fork 行為，也可以將環境變數 `CLAUDE_CODE_FORK_SUBAGENT` 設成 `0`。

## 生態系的意義

單獨檢視 Skill、Hook、Agent View 與 Subagent，它們看起來只是各司其職的獨立組件。但當這些機制組合在一起時，工具的層次就徹底改變了。

你可以用 Skill 沉澱高頻流程，用 Hook 在底層守住操作原則，透過 Agent View 掌握多工進度，並依據任務性質在 Subagent 之間切換繼承與隔離的資訊邊界。對於每天高度依賴 Claude Code 工作的人來說，這些架構設計不再只是錦上添花的小功能，而是維繫整個自動化體系穩定運作的基礎設施。

<!-- 2026-11-12 舊文盤點整篇重寫：將文末後記之子代理預設開啟行為與環境變數設定完整整合至子代理小節，消除雙重收尾，並優化各章節論述與銜接。 -->
