---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-03T04:00:00Z
title: "從 Claude Code 搬家到 Codex：我做了一個 Skill 自動處理"
slug: zh/codex-migration-skill
featured: false
draft: false
tags:
  - claude-code
  - codex
  - ai-coding
  - skills
description: 把整套個人 harness 從 Claude Code 遷移到 Codex 不容易——claude.md / agents.md、MCP、hooks、settings 各自要對齊。我把流程包成一個 Skill 放在 GitHub，順便聊聊為什麼最近越來越常用 Codex。
---

這個週末成功做的事情就是把 Claude Code 的個人環境遷移到 Codex 身上。

說真的，現在越來越習慣用 Codex，除了額度重置大方之外，還因為 GPT-5.5 講話已經沒有那種油膩味，工作溝通起來很踏實，反而是 Opus 4.7 我時不時想要給他巴蕊。

但是要把整套 harness 遷移過去，挺困難的。

## 痛點

- harness 遷移涉及多項設定與檔案，流程繁瑣
- MCP、hooks 等關鍵設定需要手動處理，試錯成本高
- 未來環境更新後，兩邊容易不同步
- 遷移整套個人工作流，往往耗時又耗力

## SKILL 做了什麼

我把這些流程包成一個 Skill：

- 協助在半小時內完成 Claude Code → Codex 的遷移計畫
- 自動處理 `claude.md` / `agents.md`、SKILL 等基礎設定遷移
- 協助整理 MCP、hooks 等較複雜的遷移項目
- 提供「維護模式」，自動比對變更並同步到 Codex
- 降低人工操作與試錯風險，提升遷移效率

Repo 在這：<https://github.com/danyuchn/claude-codex-harness-sync>

![Claude Code → Codex 遷移 SKILL](/blog/assets/posts/codex-migration-skill/codex-migration.jpg)

## 額外收穫：Codex CLI 還有改進空間

用 Codex 一段時間後最不能忍的是 CLI——光是 `/rewind` 沒得用就很不能讓人理解。Claude Code 那邊 `/rewind` 已經是日常救命招式，遷過去之後一試錯就回不去了，要靠 git stash 或重跑整段對話，效率明顯掉。

希望 OpenAI 那邊更新快一點。

## 順便講一個生圖的意外發現

在一開始創造圖片時，在 Codex 內部直接手動下指令，會比 Claude Code 轉交 Codex 還要好。因為 Claude 常常會下出過度約束的 prompt，而 GPT-image-2 反而是越少約束越能展現其創意跟美感。

中介層越多，原始意圖越容易被「修飾」掉——這個觀察應該不只適用生圖，所有跨 agent 的任務轉交都該想想這件事。
