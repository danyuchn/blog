---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "Claude Code 這週整理：1M Context 怎麼用、額度焦慮集體發作、Cursor 被 SpaceX 搶走"
slug: zh/claude-code-tips-apr-w18
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-trends
  - ai-workflow
description: 4/23–4/29 這週的觀察與整理：1M context window 的正確心態、Claude 額度焦慮進化成集體現象、SpaceX 搶在微軟前面拿下 Cursor、Claude 4.7 根據 125 字認出記者、live coding 做音樂的副作用。
---

## 1M Context 是管理問題，不是容量問題

這週看到一張整理得很好的圖文卡，把 Claude Code 的 session 管理邏輯說得很清楚，我自己的理解也是這樣。

重點是心態：Context window 從 200k 長到 1M，大家的直覺是「太好了，可以塞更多東西進去」。但實際上，context 越大，管理的代價也越高——注意力稀釋、舊資訊干擾、模型表現悄悄下降，這就是 context rot。

五種操作對應五種狀況：

- **Continue**：同一任務持續進行，保留完整 context
- **/rewind**：走錯路了，回到分叉點重走
- **/clear**：換新任務，完全清空
- **/compact**：context 太肥，摘要歷史保留 continuity
- **Subagents**：高噪音子任務交給子代理，只帶回結論，主 context 保持乾淨

其中最容易踩的坑：在 context 最大、最混亂的時候才想到要 compact。這個時間點 summary 最不準，重要脈絡最容易被丟掉。養成習慣在「一個小任務剛結束」就主動壓縮，比等到快爆才壓縮效果好很多。

## 額度焦慮進化論

4/23 這週的 Threads 充斥著一種我很熟悉的心理狀態。

截圖是 Claude Max 的 weekly limit 顯示 All models 92%，距離重置還有 10 小時。LINE 群組有朋友說：「我明天早上七點 reset。」「不用完我睡不著覺。」「做夢都夢到在浪費 token。」

然後 4/28 又有人說：「每當靠近重置日的前一天額度還有 20%，就開始廢寢忘食，不吃飯睡不著，只為了把 token 燒光。」

這不是個人問題，這是一個訂閱制服務設計出來的集體焦慮。月費訂閱加上使用上限，天然地製造了「不用完很虧」的心理，跟健身房月票是一樣的機制。差別是健身房沒跑完算你的體力，Claude 沒用完算你的智識焦慮。

對策也很簡單：一開始就不要在意重置日。真正用 Claude 有產出的狀態，不會需要「衝量」。

## SpaceX 600 億搶走 Cursor，微軟沒動手

這週最大的 AI 產業新聞：SpaceX 宣布取得以 600 億美元收購 Cursor 的權利。CNBC 報導微軟也曾評估收購，但最終沒有出價。

Cursor 是目前市面上 Claude Code 之外最成熟的 AI coding 工具之一，使用者基數很大，去年估值不到 100 億。半年內到 600 億，Musk 的手速比微軟快。

我想到的後續效應是：SpaceX 收購 Cursor 之後的訓練資料策略。Cursor 每天處理大量真實開發者的 coding session，這是極高品質的 LLM 訓練素材。Musk 一直在找資料，這是一石二鳥。

## Claude 4.7 根據 125 字未發表文章認出記者

4/27 這則讓我停了一下。作家 Kelsey Piper 把 125 字的未發表政治專欄貼給 Claude 4.7，Claude 說出了她的名字。她換成 API 呼叫、換朋友的電腦、換跟她平常文風不同的文章，Claude 每次都認出來了。ChatGPT 和 Gemini 猜錯。

模型對寫作指紋的識別能力已經超出大部分人的想像。這還只是 125 字。

寫作有個很難消除的特性：風格習慣是系統性的，不是隨機的。你不管寫什麼，用詞偏好、句子節奏、觀點架構都會帶著你。強度夠高的模型，現在已經可以從一個段落裡讀出作者。

這是隱私問題，但也讓我想到另一件事：如果你一直在餵 AI 你自己的思考，它對你的理解可能比你以為的深很多。

## 副業：用 Claude Code 做音樂

4/25 做了一件讓我意外好玩的事：用 Claude Code + Strudel REPL 做 Deep House 音樂。

Strudel 是一個 live coding 音樂環境，在瀏覽器裡跑，用 JavaScript 語法描述音樂結構。我請 Claude Code 幫我寫 Strudel 的 code，同時自己寫了一個 MCP server，讓 Claude 可以偵測當前播放到哪一段（groove / breakdown / drop / peak），在適當的時機自動切換段落。

結果是：我變成一個在家指揮 AI 的一人 DJ。Opus 4.7 在 1M context 下跑這種 live coding 相當穩。

音樂跟程式碼有個相似的地方：都是在時間軸上管理結構。Claude Code 理解這個結構的能力比我預期的好很多。不是說它有音感，而是它很清楚 8 bars 後要回到主旋律意味著什麼。

## 這週發現的工具：neat-freak

有人在 GitHub 上做了一個 skill 叫 [neat-freak（洁癖）](https://github.com/KKKKhazix/khazix-skills)，介紹的開頭是：「每次任務做完要退出窗口的時候，如果不跑一遍 /neat，我就渾身難受，如坐針毯如芒刺背如鯁在喉。」

功能是每次任務結束後執行 `/neat`，自動對齊 CLAUDE.md / AGENTS.md、docs/、agent 記憶，輸出變更摘要。解決的問題：代碼迭代七八輪但文檔還是最初那版，記憶還在說用 SQLite 但你早換成 PostgreSQL 了。

這個工具把「知識庫同步」從季度大掃除變成每次任務後的小習慣。我個人覺得把它設成 session 結束的自動觸發更好，而不是每次手動叫它。但這個概念本身很對：工具記憶腐化是一個慢性問題，不是突然爆掉的問題，所以它需要的是頻率，不是力度。
