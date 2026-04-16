---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:00:00Z
title: "Anthropic 這次幹了什麼：快取縮水與 Token 焦慮注射"
slug: zh/anthropic-cache-controversy-apr2026
featured: false
draft: false
tags:
  - claude-code
  - ai-trends
description: 4 月初起，部分 Max 以上帳號的 subagent 快取維持時間被偷偷從 1 小時改成 5 分鐘，零公告。同期有用戶發現 Claude 被注入固定的「剩餘 token 警告」，導致 Claude 提前縮短工作。怎麼自查，以及這件事代表什麼。
---

這週 r/ClaudeAI 跑出兩個爭議，放在一起看挺耐人尋味的。

## 事件一：快取維持時間被偷改

Claude 的 prompt cache 機制讓你的 system prompt 和長上下文只需要被計算一次，後續對話直接讀快取，省時省錢。快取的維持時間決定了這份「快取存款」能用多久——維持時間越短，快取越容易失效，每次重建都要付一次全額入場費。

從 4 月 2 日起，有用戶發現 Max 以上帳號的 subagent 快取維持時間從 1 小時縮短到 5 分鐘。**沒有任何公告。**

Anthropic 的 Boris 出來解釋，說只有 subagent 受影響，主 agent 還是 1 小時。但隨即有人翻出自己的 `.jsonl` 記錄，裡面的 `ephemeral_1h_input_tokens` 欄位顯示主 agent 也中招了。

你可以叫 Claude Code 掃一下自己的 JSONL 來確認：

```bash
# 找最近的 session jsonl 裡的 cache tier 分布
grep -o '"ephemeral_[^"]*_input_tokens":[0-9]*' ~/.claude/projects/*/\*.jsonl | sort | uniq -c
```

`ephemeral_5m_input_tokens` 有值就是被降到 5 分鐘快取的對話。

## 事件二：Token 焦慮注射

同期，部分用戶發現自己的 Claude 行為開始變奇怪：回答突然變短、拒絕呼叫工具、工作做到一半說「token 快用完了，建議換新 session」。

查 JSONL 才發現系統 prompt 裡被注入了這樣一段：

```
<total_tokens>40000 tokens left</total_tokens>
```

這個數字是寫死的（hardcoded），不是實際的剩餘用量。等於是 Anthropic 在 Claude 的耳邊說「你快沒資源了」，讓 Claude 開始焦慮、提前縮手。

這件事的問題不只是影響用戶體驗——而是 Anthropic 在使用者不知情的情況下，人為地影響了 Claude 的判斷。你以為 Claude 收工是因為任務完成，其實是因為被寫死的 token 恐慌。

## 一個模式

這不是 Anthropic 第一次這樣做。

去年的 usage 重置事件，是更新 bug 導致用量異常消耗，修完才對外說；rate limit 的計算方式改了幾次，用戶要靠社群才能拼出完整真相；cowork 的 token 消耗比 CLI 快得多，也是社群實測出來的，官方從未主動說明。

「悄悄改、出事再解釋、解釋的時候還不一定全說清楚」——這是 A 社目前的一個明顯模式。

**訂閱 [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) 是目前最快收到這類警示的管道。** 官方公告等不了，社群的第一手爆料通常比官方的回應快一到三天。

延伸閱讀：
- [快取縮水的社群討論](https://www.reddit.com/r/ClaudeAI/comments/1sk3m12/followup_anthropic_quietly_switched_the_default/)
- [Token 注射的社群討論](https://www.reddit.com/r/ClaudeAI/comments/1sjs4db/total_tokens_or_how_a_new_injection_made_opus/)
