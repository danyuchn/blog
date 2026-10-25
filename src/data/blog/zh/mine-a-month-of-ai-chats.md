---
author: Dustin Yuchen Teng
modDatetime: 2026-10-25T04:00:00Z
pubDatetime: 2026-10-23T01:01:00Z
title: 讓 Claude 翻我自己一個月的 AI 對話：挖出的習慣、Mod 和自動模式規則
slug: zh/mine-a-month-of-ai-chats
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - harness
description: '請 Claude Code 讀我過去一個月三百多場對話紀錄，挖出四個值得照抄的習慣、三句口頭禪做成可切換的 auto／out／wrap 模式，也能拿來改寫 auto mode 的規則。'
---

我請 Claude Code 翻了我自己過去一個月、三百多場的 AI 對話紀錄，找我一直在做、但身邊很多人好像不知道的習慣。同一批紀錄，我後來又拿來做了兩件事。

## 四個習慣

挑了四個做成一支短片：

1. AI 說「信寄了」，我會叫它把寄件紀錄找出來給我看，找不到就直說找不到，不要用猜的。
2. 寫的 AI 跟驗的 AI 分開。另一個 AI 負責挑毛病，再丟回給原本那個逐條查證，有道理的才改。
3. 能自己判斷的讓它直接做，要我拍板的全部留到最後，列成編號附上建議，我只回編號就好。
4. 它說「下次會注意」我不收，叫它把以後的做法寫進專案指示，寫完貼給我看。

翻紀錄的時候還翻到我對 AI 講過「你說之後也只是嘴上說說吧」，現在看有點兇 XD

短片在這：<https://youtube.com/shorts/5g1jYJ3DZRE>

## 把口頭禪寫成可切換的 Mod

我把最常跟 AI 講的三句口頭禪（不要問我、多外派、準備收尾）做成可以切換的 auto／out／wrap 模式。後來整理成完整的一篇，包含一週實測和開發時下的提示詞：[用一個指令切換 AI 的工作模式](/blog/posts/zh/work-mode-ai-working-modes)。

之前做過的另外兩個 Mod 在這：[錄課遮罩與暖快取](/blog/posts/zh/claude-mods-mask-and-warm-cache)。

## auto mode 一直擋你，也是翻紀錄

有人抱怨 auto mode 的自動審查一直擋，這個我之前也覺得很煩。所以我建議讓它去讀過去一個月的 session log jsonl，找出所有自動審查拒絕的案例，然後幫你改寫 auto mode 規則，你手動套用一次。以後問題就很少了。

<!--
新增非原文句子清單（忠實度自首）：
1. 「同一批紀錄，我後來又拿來做了兩件事。」— 類型：銜接（串起三則貼文）
2. 「短片在這：」— 類型：銜接（YouTube 自家 10-21 短片連結）
3. 「之前做過的另外兩個 Mod 在這：」— 類型：銜接（站內連結）
4. 「有人抱怨 auto mode 的自動審查一直擋，」— 類型：銜接（原文是回覆別人抱怨的留言，補上下文）
5. 原文 emoji 改為 XD — 類型：改寫（全域禁 emoji）
6. 圖片 alt — 類型：描述（原貼文附圖）
7. 本段原有的口頭禪清單、模式選單截圖與機制說明，2026-10-25 併入〈用一個指令切換 AI 的工作模式〉，改為一句摘要加連結 — 類型：刪減（避免兩篇重複）
-->
