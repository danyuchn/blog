---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-09T04:00:00Z
title: "別把上一個對話的 JSON 餵給它，先體檢 harness"
slug: zh/harness-checkup-no-json-dump
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: '不必把上一個對話的上下文 JSON 整包餵進去：harness 有好幾種，AGENTS.md、rule、skill、hook 都能分擔，純 session history 含太多無用的 tool call。'
canonicalURL: https://www.agentcrew.cc/blog/posts/zh/harness-slim-down-36
---

這篇已經併入 [規則越加，Claude 越不聽話——派一隊 AI 重整設定，常態上下文省 36%](/blog/posts/zh/harness-slim-down-36)，原本的內容完整保留在那一篇裡，之後也只會在那裡更新。
