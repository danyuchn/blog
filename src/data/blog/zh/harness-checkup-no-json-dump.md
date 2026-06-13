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
---

不是，為什麼要給它上一個對話的上下文 JSON。

harness 有好幾種，AGENTS.md、rule、skill、hook 這些都能分擔，把前一個對話的重點總結成臨時文檔也很好。

純 session history 裡面含有太多 tool call、output、flag 是無用的，就連 auto compact 的時候這些都會被摘除。

建議先重新體檢 harness。
