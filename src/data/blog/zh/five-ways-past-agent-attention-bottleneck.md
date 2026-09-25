---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-24T04:00:00Z
title: 同時開 5 個以上 Claude Code／Codex，我的五個注意力瓶頸解法
slug: zh/five-ways-past-agent-attention-bottleneck
featured: false
draft: false
tags:
  - ai-workflow
  - claude-code
  - productivity
description: '同時開超過 5 個 Claude Code／Codex 視窗時會遇到注意力瓶頸，一直 context switching 真的很累。分享目前跳脫這個瓶頸的五個做法：多窗口管理器、語音輸入、夜間排程、reviewable skill、定期做減法。'
---

當我同時管理 5 個以上的 Claude Code／Codex 時，就會遇到注意力瓶頸，一直 context switching 是真的會很疲累。

分享我目前跳脫這個瓶頸的五個做法：

1. 用一個好的多窗口管理器，例如 herdr，窗口之間可以互相管理進度，agent 可以控制 agent，讓它們彼此溝通。

   用 herdr 的好處是可以直接叫左邊的 Opus 去看一下右邊的 Sonnet 是不是正在做蠢事，如果是的話叫停他，自己接手來做。（雖然 Claude Code 最近也推出 sendMessage 功能支援跨 session 對話，但感覺還是不如 herdr 成熟。）

   ![herdr 左右兩個窗格，左邊是 Opus、右邊是 Sonnet](/blog/assets/posts/five-ways-past-agent-attention-bottleneck/herdr-opus-sonnet.jpg)

   派更多 subagent 會不會讓你更快，[之前寫過](/blog/posts/zh/more-agents-wont-make-you-faster)。

2. 裝一個好用的語音輸入法，用講的來輸入。另外也要有可以把長音檔轉成文字的（我推薦 agy），這樣比較長的審閱意見可以專心錄成音檔再請 AI 一次修改。

   語音下指令的兩種習慣，[之前寫過細節](/blog/posts/zh/voice-input-two-modes)。

3. 學著放手，把任務交給自動化排程：我自己有一個夜間排程，晚上讓 AI 自己去找不用等時機不用等人的待辦來做，白天再開 PR 給我審閱。

4. 做一個 reviewable skill，讓 AI 知道要給我審的東西，要用什麼格式、什麼邏輯敘事、符合我哪些習慣，目的是讓我審閱的時候不用花太多精力。

5. 學會做減法，定期請 AI 盤點有哪些不必要的業務流程，不必要就移除，然後觀察移除後的結果，如果移除之後沒有影響，那這個流程就沒有存在的必要。

<!--
新增非原文句子清單（忠實度自首）：
1. 「派更多 subagent 會不會讓你更快，之前寫過。」— 類型：銜接（連站內文 more-agents-wont-make-you-faster）
2. 「語音下指令的兩種習慣，之前寫過細節。」— 類型：銜接（連站內文 voice-input-two-modes）
-->
