---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "Opus 4.8 全線抽風的一天：tool call cannot be parsed"
slug: zh/opus-48-tool-call-parse-bug
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - developer-experience
description: '2026-06-02 一整天的事件線：從上 X 抱團取暖，到 tool call cannot be parsed 的根因被人找出來。'
---

每當 Claude 出包，我就會上 X，在這裡，我感覺我並不孤單（什麼抱團取暖的心態）。

我感覺，今天是 GPT-5.6 發佈最好的時機，上禮拜 OpenAI 蹲一下是對的。

因為 Claude 全線抽風。現在就是「趁你病、要你命」的時刻！

今天又整新活了：tool call cannot be parsed (retry also failed)。

Opus 4.8 超時思考最終返回 tool call could not be parsed 的問題根因，有人找出來了，是 thinking block 異常空輸出 & tool_use 沒有正常的工具調用區塊。判斷為 extended thinking 機制異常。

解法是：

1. 把 Opus 4.8 effort 調低到 high 以下，就不會有 thinking token，但是相應能力會降低。

2. 退回 4.6 + max 最佳。
