---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: 最需要 CLI 的電腦，主人最不可能學會 CLI
slug: zh/cli-resource-paradox-local-models
featured: false
draft: false
tags:
  - teaching
  - non-engineer
  - ai-tools
description: '對資源有限的電腦來說 CLI 佔用是 GUI 的零頭，但電腦資源最不夠的族群也剛好最不可能學會 CLI；順帶聊本機模型的硬體門檻其實沒那麼高。'
---

其實對於資源有限的電腦來說，CLI 是最好的，佔用資源是 GUI 的零頭。

但是往往電腦資源最不夠的族群，也剛好最不可能學會 CLI。

以上非貶義，只是教學過程看過很多垃圾桶從未清過，桌面鋪滿截圖，甚至兩年前的安裝檔還躺在下載資料夾裡，然後整台容量只剩 1.8G，狂吃 SWAP 還很卡的電腦⋯

有人問跑本機模型要什麼硬體。看你的硬體如何吧，其實要求不會很高。reddit 上面就有人分享用 16GB RAM 跑通 deepseek V4 flash，速度還不錯喔！33 sec / tok（注意單位）。

更極端的例子，是前陣子的笑料承包：Google 工程師要跟高職學學 AI 正確姿勢，5000 跑本地大模型。如果這是真的話，那下禮拜台股、SK 海力士、三星還不繼續跌爛。

前幾天 Qwen 宣布下一批開放權重，期待！！！希望 27B 開放權重後可以有人出量化版，也希望之後能夠有 MOE 版本的小模型，畢竟 3.6 版的 27B 跟 35B A3B 已經被公認是性價比最高的本地小模型之一。

![Qwen 官方帳號在 X 上宣布 Qwen3.8-Max 的貼文，文中「下週將釋出 Qwen3.8-Max 的開放權重，Qwen3.8-27B 也將開放權重與大家見面」一句被反白標示，下方列出 autonomous coding、long-horizon mastery、native multimodal 等賣點與每百萬 token 輸入 $2.0、輸出 $6.0 的定價。](/blog/assets/posts/cli-resource-paradox-local-models/1-27b-open-weights.jpg)

沒那麼誇張，3.6 27B Q4 量化版 M4 Pro 48GB RAM 就能跑，速度大概 20-30 tok/s。

至於要不要為了這些買電腦——電腦絕對更貴。Mac mini M4 Pro 48GB RAM 五月買五萬多，現在去看九萬了。所以用了幾年還能保值這句話不是騙人的。而且電腦是生產力工具，家裡那台老破小是能有啥生產力，給他買吧。

<!--
新增非原文句子清單（忠實度自首）：
1. 「有人問跑本機模型要什麼硬體。」 — 類型：銜接（原為回覆語境，改為一句情境交代）
2. 「前幾天 Qwen 宣布下一批開放權重，」 — 類型：銜接（原貼文僅「期待！！！」加圖，補一句圖片來源交代）
3. 「至於要不要為了這些買電腦——」 — 類型：銜接（原為回覆他人購機討論，改為一句轉場）
4. 圖片 alt 文字 — 類型：改寫（描述截圖內容，非作者原文）
5. 「更極端的例子，是前陣子的笑料承包：」 — 類型：併入碎念（Google 工程師的正確姿勢，2026-08-14 週報併入）
-->
