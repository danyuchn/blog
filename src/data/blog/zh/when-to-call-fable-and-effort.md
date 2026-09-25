---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
modDatetime: 2026-09-24T04:00:00Z
title: 何時派工 Fable？三個時機，還有別開 ultracode
slug: zh/when-to-call-fable-and-effort
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - token-optimization
description: '最貴的模型不是拿來全程跑的。三個我體感最好的 Fable 派工時機、為什麼 Opus 5 我最多開到 med，以及我後來變成週一到週四效率王、週五到週日 Fable 模式的那個循環。'
---

何時派工 Fable？個人體感最好的三個時機：

1. 主 agent 用 Fable 做整體架構規劃，實作用 subagent，最後回來給 Fable 驗收。（這也是被最多人建議的）

2. 主 agent 用 Opus 或 Sonnet，做的過程中有卡關或者需要對抗審查、拓展思維，叫單個 Fable subagent 來當一次性顧問。（我後來更常用這個）

3. 明天就是週重置，還有好多額度沒用完的時候。（A\ 佔不到你一點便宜）

那天有人問我要不要開 ultracode。

為何要開 ultracode（？想要享受千軍萬馬奔騰的感覺嗎。更不用說 ultracode 的 xhigh 模式在 Opus 5 上會有 overthink 的壞毛病，他在腦子裡左右互搏就是狂燒你的 token。

關掉 ultracode，Opus 5 最多開到 med。其實大部分的 subagent Sonnet 就好。重點是要想清楚聰明的模型在什麼節點參與——是規劃／協調／臨時顧問，還是驗收。

## 補記：後來變成一週兩種模式

好好笑，我發現我自己已經不知不覺變成：

週一到週四：效率王，處理例行事務效率拉滿（開 Sonnet 搭配已經設計好的 skill＋pipeline＋本地模型＋5.6 Luna／Gemini routing，再加上夜間自動化）。

週五到週日：突然發現前幾天額度實在太省了，還有一堆沒用完，直接開 Fable，變身創造力爆發遠見模式，對未來做長期探索、規劃、優化 harness 跟設定邊界護欄。

週日下午五點：變回懦弱模式，重新開始循環。

![手機上的額度面板：目前 session 用掉 92%、全模型週限額用掉 97%、Fable 專屬額度只用掉 47%](/blog/assets/posts/when-to-call-fable-and-effort/1-weekly-rhythm.jpg)

所以我客戶都是週一到週四聯絡的，新的交付都是週五到週日出的。

你也跟我是一樣的嗎？

## 補記：兩種模型混搭法

換模型有 cache miss 問題，最常用的是 subagent。路徑還不明確時，主 agent 用聰明的、雜活丟給低階的臨時 subagent；路徑已經明確、只剩少部分困難點時反過來，主 agent 用低階的，臨時叫聰明的 subagent 來當一次性顧問或驗收。

## 補記：派 subagent 的兩道 hook

有一次 Fable 給我派 Fable subagent ×3（不指定模型直接繼承主 agent 等級），額度瞬間燒乾。從此之後我就加了這個 hook。

![Claude Code 的 PreToolUse hook 擋下沒有指定模型的派工：錯誤訊息要求顯式指定 haiku、sonnet、opus 或 fable，不准繼承主 agent 的預設](/blog/assets/posts/when-to-call-fable-and-effort/subagent-model-hook.jpg)

想要你的 CC 也有這樣的防護嗎？很簡單，這張圖複製下來丟給你的 CC，叫他照著設置就好了。

另外 nested subagent 要去改設定關掉。然後建議設置 hook，我設置的就是 subagent 同時最多兩個，三個以上 hook 會攔下來要我回答 Yes/No。我也在 rules 的派工段落上寫原則是兩個，有要派多請說明理由。

簡單來說就是當員工在管——跟員工說：原則就是怎樣，多了要報給我簽核。

## 補記：effort 每往上一級要多花多少

Reddit 上有人從 Claude Code 裡挖出一張各模型、各 effort 等級的 token 成本表，還自己實測了一輪（[原文](https://www.reddit.com/r/ClaudeAI/comments/1wjr89j/claude_code_ships_a_permodel_table_of_what_each/)）：

![Reddit 貼文截圖：Claude Code 內建的各模型 effort 成本表，以 high 為 1。Opus 5 從 high 到 xhigh 多 60%，xhigh 到 max 只再多 6%](/blog/assets/posts/when-to-call-fable-and-effort/effort-cost-table.jpg)

![同一篇貼文的實測：8 個 Opus 5 agent 在同一個 repo 跑兩個真實任務、四種 effort，xhigh 與 max 的輸出 token 幾乎一樣](/blog/assets/posts/when-to-call-fable-and-effort/effort-cost-measured.jpg)

<!--
2026-08-28 W36 碎念併入：live 碎念「兩種模型混搭法」逐字併入，該條與本文前兩個派工時機是同一組判準。已從 zh/en live 檔刪除。新增非原文句子僅小標一則（框架句）。
-->

<!--
2026-08-28 W36 主對話補記：把 2026-08-23 11:00 的 Threads 貼文併入本文成為第三節，而非另開新文——該貼文的「用時間決定派誰」與本文第 3 個派工時機是同一個邏輯，素材量也撐不起獨立一篇。全文逐字保留，新增非原文句子僅小標一則（框架句）。原文 emoji 依站台規範未保留。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「那天有人問我要不要開 ultracode。」 — 類型：銜接（把第二則貼文的回覆情境交代出來，原文為回覆他人提問，無此敘述句）
-->

<!--
2026-09-24 W40 補記兩節：① 2026-09-24 Threads 貼文（Fable 派 3 個 Fable subagent 燒乾額度→加 hook）與 2026-09-23 留言回覆（nested subagent、同時最多兩個、當員工在管）逐字併入；② 2026-09-19 貼文轉貼 r/ClaudeAI effort 成本表（原貼文僅圖片＋連結）。新增非原文句子：兩個小標（框架句）、「另外」（銜接）、「Reddit 上有人從 Claude Code 裡挖出……還自己實測了一輪」（框架句，內容取自截圖）。原文 emoji 依站台規範未保留。
-->
