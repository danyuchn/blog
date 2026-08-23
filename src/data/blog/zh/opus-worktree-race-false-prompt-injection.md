---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-19T05:00:00Z
title: "Opus 4.8 搞烏龍報『提示注入攻擊』，Codex GPT-5.5 揪出 worktree race 真因"
slug: zh/opus-worktree-race-false-prompt-injection
featured: false
draft: false
tags:
  - claude
  - claude-code
  - security
  - ai-tools
description: 'Opus 4.8 在我忘開 worktree 的情況下誤報「提示注入攻擊」，叫我去查供應鏈、rotate API key，最後 Codex GPT-5.5 查 session log 才揪出真因只是 worktree race。'
canonicalURL: https://www.agentcrew.cc/blog/posts/zh/silent-failures-and-confabulated-tool-results
---

這篇已經併入 [沒拋錯不代表成功：靜默失敗、Opus 捏造工具輸出，以及一個擋得住的 hook](/blog/posts/zh/silent-failures-and-confabulated-tool-results)，原本的內容完整保留在那一篇裡，之後也只會在那裡更新。
