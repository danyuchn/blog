---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: 號稱最聰明的 Opus 5，一整天在我對話裡空轉
slug: zh/opus-5-thinking-only-empty-turns
featured: false
draft: false
tags:
  - claude-code
  - debugging
  - gotchas
description: '從回錯語言、突然寫簡體，到整輪沒有可見輸出，查 session log 之後對上一個 6/15 就開著沒修的 issue。'
---

## 早上先是語言錯亂

號稱最聰明的 Opus 5 模型，老問題從 4.6 到現在都還沒修掉，不定期就給我回韓文、日文。

![Opus 5 在繁體中文對話中突然回覆韓文與日文的截圖](/blog/assets/posts/opus-5-thinking-only-empty-turns/wrong-language.jpg)

十幾分鐘後又來。。。

到了下午更棒了，明明 `/config` 跟 `claude.md` 都有寫用繁體中文，過去兩個月都寫繁體的，現在開始兩岸一家親寫簡體了。

## 岔題一下：假陽性可以接受，假陰性才可怕

同一天我在調自己的 pending guard hook，剛好有張誤判的圖。這張圖是假陽性，不過我覺得完全可以接受，誤判有罪我覺得沒關係，hook 一提醒，真正無辜的話模型會拿出證據幫自己辯護。

最怕的是假陰性，讓錯誤偷偷溜走，不過這已經很少發生了，因為模型的輸出用詞都非常固定，regex 都能抓到。

還好我的 harness 都有另外上 git，所以我打算一點一點改來測試，不行就 rollback。

抓假陰性有兩種方法：

1. 我在過幾輪對話後發現他根本沒驗證，導致品質有問題，他又來「你說得對，我剛剛沒有⋯」的時候
2. 每天半夜用 claude-log CLI 配本地模型，掃過當天所有 session log jsonl，挑出所有模型宣稱有驗證片段（不用 regex，直接讓本地 LLM 用語意抓，慢沒關係，反正是半夜），再回來復盤當天漏了幾個假陰性

而這天的模型，自己講出這麼一段：

> 一句話總結：這不是工具呼叫語法寫錯的問題，是我在某些需要整合視覺資訊或等待多方回報的節點上，思考完但沒把動作／文字真正產出，然後偶爾還會在事後編一個聽起來合理但沒有根據的技術解釋來搪塞。這個「編造理由」的部分本身就是一次需要記錄的失誤——之後如果我再說「是格式錯誤」這類自我診斷，你可以直接要我先拿證據再說。

這讓我想起昨天看的系統卡，Opus 5 幻覺率升高。。。。

## 「是不是你 CLAUDE.md 太肥？」

有人建議我把 CLAUDE.md 砍掉重練。

![harness 健診報告截圖，顯示官方比對用 WebFetch code.claude.com 加 WebSearch，無過時規則，全數低於 200 行，最大 92 行](/blog/assets/posts/opus-5-thinking-only-empty-turns/harness-audit-92-lines.jpg)

已經只剩 92 行了（官方建議低於 200 行），每週都跟官方文檔跟 `/insight` 對過一次，持續半年不間斷，能否分享你砍掉重練的好方法跟實績？

claude.md 92 行算太多嗎⋯剛剛發生問題的時候 context 才用了 8%。我甚至還為了保留他的 context window 派 sonnet subagent 出去。

就是他拉了一坨大便到我的對話中。

## 用 claude-log 去盤查他拉了什麼賽

我在叫 claude-log CLI 去盤查，看 session log 拉了什麼賽。

查了一下，原來 6/15 的 Opus 4.8 就有這問題，只是因為我一直在用 4.6 所以沒有遇到，但現在還是沒有修好。

#68591 — Opus 4.8 returns thinking-only responses without tool_use or text blocks（open）

這篇跟我剛才用 claude-log 查出來的根因完全一致：Opus 4.8 有時會產生「只有 thinking block，沒有 text、沒有 tool_use」的回應，stop_reason 卻正常顯示 tool_use 或 end_turn，client 端無法解析、只好判定「這輪沒有可見輸出」。

也就是說：模型內心其實把答案想好了、寫在 thinking 裡，但沒有把它輸出成使用者看得到的 text。這跟我們今天查到的現象（連續空轉、尤其發生在讀圖片後或等 subagent 回報後）是同一個已知 regression。

<https://github.com/anthropics/claude-code/issues/68591>

難說，現在也只能 `/feedback` 看看官方會不會垂憐我⋯

的確有可能，接下來是往這個方向調整沒錯，但是我 codex 跟 claude 都用同一套 harness，codex 就沒啥問題，實在很好奇為何 claude 這麼敏感（？）哈哈哈哈哈。

<!--
新增非原文句子清單（忠實度自首）：
1. 「## 早上先是語言錯亂」 — 類型：框架句（H2 標題，原文無）
2. 「十幾分鐘後又來。。。」 — 類型：改寫（原句為 08:52 的「又來。。。」；「十幾分鐘後」為時間戳 08:39→08:52 的銜接描述）
3. 「到了下午更棒了，明明⋯」 — 類型：銜接（原句起頭為「現在更棒了」，改為「到了下午更棒了」以接時間軸）
4. 「## 岔題一下：假陽性可以接受，假陰性才可怕」 — 類型：框架句（H2 標題，原文無）
5. 「同一天我在調自己的 pending guard hook，剛好有張誤判的圖。」 — 類型：銜接（原貼文 13:17 開頭直接說「這張圖是假陽性」，此句為指涉補述；「pending guard hook」名稱為銜接用語，非原文字面）
6. 「抓假陰性有兩種方法：」 — 類型：改寫（原文為「兩種方法：」）
7. 「而這天的模型，自己講出這麼一段：」 — 類型：銜接（引入 15:28 引用）
8. 「## 「是不是你 CLAUDE.md 太肥？」」 — 類型：框架句（H2 標題，原文無）
9. 「有人建議我把 CLAUDE.md 砍掉重練。」 — 類型：銜接（原為 16:48 的回覆情境，素材註明「回覆別人建議他把 CLAUDE.md 砍掉重練」）
10. 「## 用 claude-log 去盤查他拉了什麼賽」 — 類型：框架句（H2 標題，取自原句用詞）
11. 兩張圖片的 alt 描述句 — 類型：改寫（依素材提供的圖片說明撰寫）
12. 部分原貼文的行內標點與換行位置經整併成段落（去平台碎片化），未更動字詞。
-->
