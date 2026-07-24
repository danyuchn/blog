---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: 第二次 harness 減肥：全域 skills 58 砍到 40
slug: zh/skills-58-to-40-second-diet
featured: false
draft: false
tags:
  - claude-code
  - harness
  - productivity
description: '接續 harness 減肥系列，半年後做了第二輪更大規模的整理，把全域 skills 從 58 個砍到 40 個的完整過程。'
---

上次寫 harness 減肥，是把自己的 Claude Code 個人配置瘦身了 −36%。半年後，我又做了第二輪，這次規模更大：全域 skills 大合併，從 58 個砍到 40 個。

做法是先派兩個 Sonnet subagent 去盤點現況，一個掃 user level 的 58 個、一個掃 project level 的 66 個，盤完我自己親判執行。

12 支直接下架進 `~/.claude/skills/_archived/`：meeting-debrief、slack、teach-impeccable、frontend-slides、job-tailor、browser-routing、third-party-quotas、obsidian-markdown、obsidian-bases、obsidian-cli、polite-biz、humanizer-zh。6 本商業書的 skill 合併成一個統一路由的 `biz-books`。幾組功能重疊的直接合併：darwin 併入 skill-creator、explore-unknowns 併入 first-principles、humanizer 中英合一、polite 雙模式合一。artist-sentiment 搬去 crawler 專案。兩個降轉成更輕量的形式：browser-routing 降轉成常駐 `rules/common/`、third-party-quotas 降轉成 memory 裡的 reference。

最後補了 9 支 skill 的口語觸發詞，全部跑過完整 YAML 格式與 ≤200 字元驗證通過，交叉引用也全數修正：CLAUDE.md、tool-patterns、error-recording，還有 pdf、obsidian、social-card、threads-voice、launch-kit。

就這樣。

<!--
新增非原文句子清單（忠實度自首）：
1. 「上次寫 harness 減肥，是把自己的 Claude Code 個人配置瘦身了 −36%。」 — 類型：框架句（依據 team-lead 提供的背景：接續 harness 減肥系列第二輪、前一篇 −36%）
2. 「半年後，我又做了第二輪，這次規模更大：全域 skills 大合併，從 58 個砍到 40 個。」 — 類型：框架句（依據背景「半年後又做了第二次更大規模的瘦身」＋素材數字 58→40）
3. 「做法是先派兩個 Sonnet subagent 去盤點現況，一個掃 user level 的 58 個、一個掃 project level 的 66 個，盤完我自己親判執行。」 — 類型：改寫（素材「雙 Sonnet subagent 盤點（user level 58＋project level 66）後親判執行」）
4. 「就這樣。」 — 類型：銜接（短促收束，非原文語意）
-->
