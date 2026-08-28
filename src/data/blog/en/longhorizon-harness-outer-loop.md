---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-28T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: Just Swap the Outer Loop
slug: en/longhorizon-harness-outer-loop
featured: false
draft: false
tags:
  - ai-workflow
  - ai-tools
  - open-source
description: 'LongHorizon-Harness wraps around agents like Claude Code and Codex. It does not train the model or replace your agent, it only runs the loop, and WeaveBench completion went from 51.8 to 80.7.'
---

Same model, same backend. Swap only the loop wrapped around it, and WeaveBench completion goes 51.8 → 80.7.

LongHorizon-Harness wraps around Claude Code, Codex, OpenCode, and DeepSeek Harness. MIT licensed, 1,100 stars twenty days after launch. It doesn't train the model and it doesn't replace your agent. It only runs the loop.

Three roles: the Manager rebuilds the next step from the original goal plus verified progress plus evidence of failure. The Executor takes a fresh context and does only that step. The Auditor independently checks the real files and tests, and doesn't take the Executor's word for anything. Only what passes the check counts as progress; what gets bounced counts as evidence. If context is lost, you pick up from the last checkpoint. It turns acceptance into a role instead of one line of nagging in a prompt.

The Executor getting a fresh context on every step points in the same direction as the [six rules of context engineering](/blog/posts/en/claude-5-context-engineering-six-rules) I wrote about earlier.

Their own reported numbers (Qwen 3.7-Plus plus Claude Code): OSWorld 2.0 full completion 2.8→8.3, Terminal-Bench 2.1 success rate 69.7→77.2 with 24% fewer tokens.

<https://github.com/AMAP-ML/LongHorizon-Harness>

<!--
新增非原文句子清單（忠實度自首）：
1. 「The Executor getting a fresh context on every step points in the same direction as the [six rules of context engineering](/blog/posts/en/claude-5-context-engineering-six-rules) I wrote about earlier.」 — 類型：銜接（依任務指定加入站內回指，僅一句帶過，不展開論述）
其餘段落均為原貼文逐字翻譯，僅將裸連結改為 autolink 格式。
-->
