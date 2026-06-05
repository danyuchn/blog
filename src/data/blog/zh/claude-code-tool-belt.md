---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "用 Claude Code 這幾個月，累積下來的周邊工具與學習資源"
slug: zh/claude-code-tool-belt
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - productivity
description: '把這幾個月散落在碎念裡的東西整理成一篇：看成本的 ccusage、查歷史對話的 claude-log-cli、系統性理解的 how-claude-code-works，再加上日常搭配的 Claude Extension。'
---

用 Claude Code 用了幾個月，除了 Claude Code 本身，慢慢也累積出幾個周邊工具跟學習資源。這些之前散落在碎念裡，這篇把它們收在一起。

## 日常搭配：Claude Extension

我最常用的：Claude Extension 搭配 Claude Code，效率高到飛起來。

## 看成本：ccusage

`!npx ccusage@latest monthly` 可以看詳細的 API 成本。用 Claude Code 的人推薦裝。

## 查歷史對話：claude-log-cli

30 天內的對話都存在 jsonl 裡面。你可以裝 <https://github.com/martinalderson/claude-log-cli> 快速找歷史對話，改參數可以把預設保留的天數拉長。

## 系統性理解：how-claude-code-works

最近減少看 Threads 的時間，開始認真讀這個網站：<https://windy3f3f3f3f.github.io/how-claude-code-works/>。系統性地吸收知識還是比碎片化好太多。
