---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-28T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: 只換外面那圈 loop
slug: zh/longhorizon-harness-outer-loop
featured: false
draft: false
tags:
  - ai-workflow
  - ai-tools
  - open-source
description: 'LongHorizon-Harness 架在 Claude Code、Codex 這些 agent 外面，不訓練模型也不取代你的 agent，只做迴圈，WeaveBench 完成率從 51.8 拉到 80.7。'
---

同一個模型、同一個後端，只換外面那圈 loop，WeaveBench 完成率 51.8 → 80.7。

LongHorizon-Harness 架在 Claude Code、Codex、OpenCode、DeepSeek Harness 外面，MIT 授權，上線二十天 1,100 星。它不訓練模型、不取代你的 agent，只做迴圈。

三個角色：Manager 從「原始目標＋已驗證進度＋失敗證據」重建下一步，Executor 用全新 context 只做那一步，Auditor 獨立查真實檔案與測試，不採信 Executor 自述。過查核的才算進度，被打回的只算證據；context 掉了就從最後一個 checkpoint 接上。等於把驗收做成角色，而不是提示詞裡一句叮嚀。

Executor 每步都拿全新 context 這件事，和我先前寫的[情境工程六規則](/blog/posts/zh/claude-5-context-engineering-six-rules)是同一個方向。

官方自報（Qwen 3.7-Plus ＋ Claude Code）：OSWorld 2.0 完全完成 2.8→8.3、Terminal-Bench 2.1 成功率 69.7→77.2 且少 24% token。

<https://github.com/AMAP-ML/LongHorizon-Harness>

<!--
新增非原文句子清單（忠實度自首）：
1. 「Executor 每步都拿全新 context 這件事，和我先前寫的[情境工程六規則](/blog/posts/zh/claude-5-context-engineering-six-rules)是同一個方向。」 — 類型：銜接（依任務指定加入站內回指，僅一句帶過，不展開論述）
其餘段落均為原貼文逐字保留，僅將裸連結改為 autolink 格式。
-->
