---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-12T04:00:00Z
title: Information Diet：我抓自己的 Chrome 瀏覽紀錄，做了一次注意力盤點
slug: zh/information-diet-attention-audit
featured: false
draft: false
tags:
  - productivity
  - opinion
  - claude-code
description: '現代人極度在意吃進口裡的每一塊食物乾不乾淨，卻毫不在乎上網吃到的一大堆 Dirty Info。所以我抓了自己的 Chrome 瀏覽紀錄 db，讓工具分析我的上網習慣，結果有幾段比我預期的難看。'
---

## Clean food 與 Dirty Info

Information Diet 實在是太重要了。我認為會是接下來幾年的顯學。

現代人：極度在意吃進口裡的每一塊食物是不是 Clean food，但卻毫不在乎自己上網吃到的一大堆 Dirty Info。

你不會一天三餐都吃洋芋片，因為知道身體會壞掉。但很多人一天滑三小時短影音、看幾十則吵架的脆，卻不覺得腦袋會壞掉。

講完這段之後，我做了兩件事：抓 chrome 瀏覽記錄的 db，然後分析我的上網習慣。以下是報告輸出的幾段，它是用第二人稱在跟我講話。

## Threads 的 2,357 次不是我想的那回事

![報告第一張截圖，把 Threads 的 2,357 次造訪依路徑拆開，指出 57% 是在看自己的通知與貼文，真正吸收外部資訊只佔 17%](/blog/assets/posts/information-diet-attention-audit/card-1-threads-feedback-loop.jpg)

> 二、但 Threads 的 2,357 次不是你想的那回事
>
> 我把路徑拆開看，這是整份報告最意外的一段：
>
> /activity（通知與互動）812 ／ /@dustin_gmat/post（自己的貼文）405 ／ /（首頁動態）314 ／ /@dustin_gmat（自己的個人頁）125 ／ /messages 105 ／ /search 38 ／ 別人的貼文（合計）~51
>
> 57%（1,347 次）是在看自己。通知、自己的貼文、自己的個人頁。
>
> 真正意義上的「吸收外部資訊」只有 403 次（首頁動態＋別人的貼文＋搜尋），佔 17%。
>
> 這個發現改變了問題的性質：
>
> 「你在 Threads 上的問題不是資訊過載，是回饋迴圈。」
>
> 資訊過載的解法是篩選來源；回饋迴圈的解法完全不同——那是「發完文之後每隔幾分鐘回去看有沒有人按讚」的行為，跟看什麼內容無關。近 30 天 812 次 /activity，等於平均每天 27 次點開通知頁。

## 攝取到落地：工具類

![報告第二張截圖，統計 30 個蒐集到的工具中已裝在用 6 個、明確不裝 12 個、評估中 1 個、懸而未決 11 個，並列出那 11 個的名稱](/blog/assets/posts/information-diet-attention-audit/card-2-tool-conversion.jpg)

> 三、攝取 → 落地：工具類
>
> 這是唯一能算出轉換率的類別（因為你有標狀態）。
>
> 蒐集了 30 個工具：已裝在用 6（20%）／明確不裝 12（40%）／評估中 1／懸而未決 11（37%）。結案率 60%。
>
> 先講好的：40% 明確剪枝掉，這個數字很健康。多數人蒐集了就放著，你會回頭標 parked，等於有在做南瓜計畫的剪枝動作。
>
> 問題在那 11 個懸而未決的——蒐集了、沒裝、也沒說不裝，就一直掛著：ultracode-harness-sweep-prompt、rapidapi-vs-apify-api-marketplace、ipad-remote-mac-mini-setup、financial-services-plugins、repowise-codebase-mcp、kaosensei-line-desktop-skill、vercel-agent-browser-vs-chrome-mcp、macos-screen-capture-permission-fix、microsoft365-cli-tools、james-ebook-library、claude-code-review-council-skill

## 三個零留存來源

![報告第三張截圖，列出小紅書 414 次、Instagram 251 次、Khaosod 175 次三個零留存來源，合計 840 次造訪但書庫裡沒有留下任何痕跡](/blog/assets/posts/information-diet-attention-audit/card-3-zero-retention.jpg)

> 三、純消費的部分：三個零留存來源
>
> 扣掉自我監看，真正的「攝取但零產出」是這三個：小紅書 414 次留存 0（其中 search_result 129、explore 102 → 是在主動搜，不是無腦滑）／Instagram 251 次留存 0／Khaosod 175 次留存 0（泰國本地新聞）。合計 840 次。
>
> 我不打算建議你砍這三個。理由：Khaosod 是你生活所在地的新聞，人住曼谷看當地新聞是基本盤，不需要有產出。Instagram 251 次、每天 8 次，以社群平台來說這是很低的量，不值得動。小紅書 414 次裡有 129 次是 search_result、102 次是 explore——這是在主動找東西的型態，不是被動滑。它可能在餵你某些東西（市場觀察？生活資訊？），只是產物沒進書籤庫。
>
> 這三個真正的問題不是「該不該砍」，是「它們完全沒有留下任何痕跡」。你花了 840 次造訪，vault 裡一個字都沒有。如果它們有價值，價值蒸發了；如果沒價值，你不知道自己在燒時間。兩種情況都需要一次判定，而不是砍或不砍。

## 我的一天長什麼樣

![報告第四張截圖，以曼谷時間逐小時列出近 30 天的活動量，凌晨一到五點為零，早上八點與晚上八點是兩個高峰](/blog/assets/posts/information-diet-attention-audit/card-4-daily-hours.jpg)

> 四、你的一天長什麼樣。近 30 天，曼谷時間：00:00 330／01-05 0（睡得很乾淨，這點很好）／06:00 144／07:00 393／08:00 1077（早晨高峰）／09:00 753／10:00 612／11:00 378／12:00 383／13:00 853／14:00 1045／15:00 1031／16:00 1069／17:00 755／18:00 696／19:00 856／20:00 1376（全日最高）／21:00 1034／22:00 965／23:00 442

## 注意力實際去向

![報告第五張截圖，把近 30 天 709 個 Claude Code session 依專案分佈列出，並歸類為經營自己的系統 59%、課程產品 24%、對客戶交付 9%](/blog/assets/posts/information-diet-attention-audit/card-5-session-split.jpg)

> 五、注意力實際去向（最戳人的一段）
>
> 近 30 天 709 個 Claude Code session 的分佈：knowledge-base 300（42.3%）／claude-course 133（18.8%）／.claude-automation 120（16.9%）／theplanb 37（5.2%）／tutor-claude 30（4.2%）／GMAT-skills 29（4.1%）／personal-finance 10（1.4%）／blog 9（1.3%）／PDT-learning 6（0.8%）
>
> 把它們歸類：經營自己的系統（knowledge-base + .claude-automation）= 59%；課程產品（claude-course + theplanb）= 24%；實際對客戶交付（tutor-claude + GMAT-skills + PDT-learning）= 9%。
>
> 近六成的注意力花在維護「用來做事的系統」上，不到一成花在「對付錢的人交付」上。

報告最後那句是自己的機器對自己講的，數字也是自己的。就這樣。

<!--
新增非原文句子清單（忠實度自首）：
1. 「講完這段之後，我做了兩件事：抓 chrome 瀏覽記錄的 db，然後分析我的上網習慣。」 — 類型：銜接（把原串兩則回覆「抓chrome瀏覽記錄的db」「分析我的上網習慣」串成一句敘述）
2. 「以下是報告輸出的幾段，它是用第二人稱在跟我講話。」 — 類型：框架句（提示讀者以下引文是工具產出、以「你」稱呼作者）
3. 「報告最後那句是自己的機器對自己講的，數字也是自己的。就這樣。」 — 類型：框架句（結尾收束，不代作者做任何行為承諾）
4. 各 H2 標題（「Clean food 與 Dirty Info」「Threads 的 2,357 次不是我想的那回事」「攝取到落地：工具類」「三個零留存來源」「我的一天長什麼樣」「注意力實際去向」）— 類型：框架句（多數直接沿用截圖小標，人稱由「你」改為「我」）
5. 五張圖的 alt 描述句 — 類型：改寫（依截圖內容摘述，數字皆取自原文）
-->
