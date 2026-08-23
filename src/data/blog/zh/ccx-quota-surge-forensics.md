---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: 有些 subagent 都當阿公了
slug: zh/ccx-quota-surge-forensics
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - debugging
description: '一次 CCX 沒設好護欄的額度事故：subagent 遞迴繁殖，一個 session 半小時燒掉 90%，事後鑑識與修法全記錄。'
canonicalURL: https://www.agentcrew.cc/blog/posts/zh/claude-code-quota-incident-log
---

這篇已經併入 [額度是怎麼被燒掉的：Claude Code 快取 bug、Opus 4.7 的 2x 消耗、subagent 遞迴繁殖](/blog/posts/zh/claude-code-quota-incident-log)，原本的內容完整保留在那一篇裡，之後也只會在那裡更新。
