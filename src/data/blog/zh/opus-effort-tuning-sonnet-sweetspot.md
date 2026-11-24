---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T04:30:00Z
title: "Opus 4.7 的 effort 怎麼調，跟為什麼我非編程任務還是停在 Sonnet 4.6 medium"
slug: zh/opus-effort-tuning-sonnet-sweetspot
featured: false
draft: false
archived: true
tags:
  - claude-code
  - ai-coding
  - ai-workflow
description: 'Opus 4.7 預設的 adaptive effort 是場災難，會變成偷懶摸魚皇帝。要開到 high 或 xhigh 才能避免，但 token 就開始狂燒。實測下來，非編程任務停在 Sonnet 4.6 medium 反而是最好的選擇。'
canonicalURL: https://www.agentcrew.cc/blog/posts/zh/read-system-card-before-managing-model
---

這篇已經併入 [別再背提示詞秘訣了！先讀 AI 的「新進員工體檢表」，像帶團隊一樣跟 Claude、Codex 合作](/blog/posts/zh/read-system-card-before-managing-model)，原本的內容完整保留在那一篇裡，之後也只會在那裡更新。
