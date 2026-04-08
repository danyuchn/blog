---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T15:30:00Z
title: "挖 Claude Code 的 JSONL：手動算 context 用量、分辨快取類型、偵測 compact"
slug: zh/claude-code-jsonl-internals
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - developer-experience
description: Claude Code 的 `/stats` 只告訴你總 token 數，但 JSONL 檔案裡其實藏著更細的資訊——快取類型、compact 觸發、貼圖 cache miss 都能手動算。這是我最近做 cc-audit skill 時整理出來的幾個實用公式。
---

Claude Code 的 `/stats` 只告訴你「這個 session 花了多少 token」，但那是一個總數，藏了很多重要細節。我最近做 [cc-audit skill](/blog/posts/zh/cc-audit-skill) 的時候，把 JSONL 檔案整個翻過一遍，發現其實藏著一堆有用的指標，只要你知道去哪裡抓。

JSONL 檔案在 `~/.claude/projects/<project-name>/<session-id>.jsonl`。每一行是一個 JSON object，對應到一條訊息或系統事件。

以下是我整理出來的幾個實用公式。

## 1. Context 使用率公式

要看你這個 session 吃了多少 context window，不要只看 input_tokens——那只是「本次送進去的新內容」。要加上 cache 部分才是真正的厚度。

```
context_usage = (input_tokens + cache_creation_input_tokens + cache_read_input_tokens) / 200000
```

分子是 assistant 訊息 `usage` 欄位裡的三個值。分母 200000 是 Claude 目前的 context window 大小。

算出來接近 1 代表你快撞牆了，接下來要嘛 `/compact`、要嘛 `/clear`、要嘛開新對話。

## 2. 分辨快取類型：5 分鐘 vs 1 小時

Claude 的 prompt cache 有兩種有效期：Pro 訂閱是 5 分鐘，Team/Enterprise 是 1 小時。你可以從 JSONL 的 `usage` 欄位分辨：

```
cache_creation:
  ephemeral_5m_input_tokens: <number>   # Pro
  ephemeral_1h_input_tokens: <number>   # Team/Enterprise
```

如果你是 Pro 訂戶又看到 `ephemeral_1h_input_tokens` 有值，那就是官方給你的 bug（或隱藏福利，看心情）。反過來也一樣。

## 3. 偵測 `/compact` 有沒有被觸發

`/compact` 會留下痕跡：它會在 JSONL 產生一條 `type=system` 的訊息，裡面有 `summary` 關鍵字。用 grep 就能掃：

```bash
grep -c '"type":"system".*summary' session.jsonl
```

`/clear` 就比較麻煩了——它不會留任何痕跡，因為它直接開了一個新的 session 檔。如果你想統計「我今天 clear 幾次」，得從檔案系統層級去看「這個專案今天多了幾個新 JSONL 檔」，而不是看單一檔案。

## 4. 貼圖後的 cache miss 偵測

這是本週最實用的一條。大家都知道貼圖會把 cache 搞掉，但你怎麼確認「我這次 cache miss 就是因為剛貼了圖」？

組合兩個條件：

1. 上一條 `user` content 裡面有 `image` type 的 block
2. 下一條 `assistant` 訊息的 `cache_read_input_tokens` < 500

如果兩者都符合，幾乎可以確定是貼圖導致的 cache miss。500 是我抓的經驗值——正常 session 的 cache_read 通常幾千到幾萬，掉到 500 以下代表快取整包重建。

知道這個之後你可以做兩件事：一是避免把圖貼進長對話（重要的圖要貼就開新對話貼），二是事後撈 JSONL 統計「我這週貼了多少張圖、總共燒了多少重算成本」——我跑過一次，結果讓我決定以後截圖都先裁到最小再貼。

## 5. Session 開場的記憶體 vs 檔案系統陷阱

這條不是 JSONL 解析，是昨天我自己踩到的行為陷阱，一併記在這裡。

我有一個 session 連續漏掉 3 份 untracked 新檔（一份視訊會議紀錄、一份客戶提案 draft、一份 Slack DM 存檔），只讀了 memory index 就開始分析，結果分析得像在寫小說——因為 memory 是索引，會過期，檔案系統才是事實。

結論：**session 開場如果 `git status` 有 `??` 或 `M` 的檔案，必須先 Read 過才能動工**。這條已經寫進我的 `~/.claude/rules/common/task-execution.md` 當開場硬性規定。

memory 是 hint，不是 source of truth。這是一個很容易被忽略但會反覆踩到的坑。

## 結尾

`/stats` 只是入口。真正的細節在 JSONL 裡，而且都可以用 Python + jq 自己抓。我寫的 [cc-audit skill](/blog/posts/zh/cc-audit-skill) 已經把這些邏輯全部打包好，但你如果想自己 hack，以上五個公式應該夠你開始。

Claude Code 是一個開放的系統——所有資料都在你的硬碟上，格式是公開的 JSON。懂得挖這些，比只看 `/stats` 有用一百倍。
