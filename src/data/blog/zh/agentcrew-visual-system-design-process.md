---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-16T04:00:00Z
title: "外行人選品牌視覺：AI 把提案做便宜了，難的變成你的品味"
slug: zh/agentcrew-visual-system-design-process
featured: false
draft: false
tags:
  - ai-workflow
  - agentcrew
  - non-engineer
description: '我不是設計師，這週用 Fable、GPT-image-2、GPT-5.6-sol 迭代出 AgentCrew Academy 的視覺系統，記下被否決的四個方向與最後套用到網站、投影片、文件的規格。'
---

我不是設計師，但這週花了不少時間幫 AgentCrew Academy 選一套視覺系統。

一開始是用 Fable 出提案，第一版就讓我眼睛一亮：白、墨、朱、黑，安靜，但有判斷。這是仍可開啟的原始 Fable artifact 畫面，不是事後重建的。

![Fable artifact 截圖顯示第一版視覺提案，白墨朱黑配色搭配「安靜，但有判斷」的標語，套用在 AgentCrew Academy 網站原型上](/blog/assets/posts/agentcrew-visual-system-design-process/1-first-proposal.jpg)

但一版不夠，我請它再大膽一點，於是有了 A 到 D 四個被否決的方向：藝廊白、暖紙誌面、墨黑封面、紺青專業，各自抓不同參考——NENDO 的排版夏令營、&PREMIUM 與 Kinfolk 的暖紙誌面、BRUTUS 與 SUPPOSE 的墨黑封面、Takram 與 SmartHR 的紺青專業。

![四個被否決的視覺方向 A 到 D 並排比較：藝廊白、暖紙誌面、墨黑封面、紺青專業](/blog/assets/posts/agentcrew-visual-system-design-process/2-rejected-directions.jpg)

後來我又嘗試了另外一種方式，這次不倚賴 Fable，而是直接請 GPT-image-2 產出 5-10 版風格圖讓我選，再把選中的風格圖丟回給 GPT-5.6-sol，請它做出 YouTube 封面的範例，順便給它我 YouTube 的首頁，讓它用 HTML 做一個「改版後的頻道長怎樣」的原型。等我選中之後，它再幫我做封面樣板，方便未來替換內容跟產出。目前頻道封面還沒正式換，因為想先跑一陣子 A/B Test 再決定。

跟 GPT 合作的這一次感覺也很不錯，所以我覺得兩條路都行得通。AI 時代原型的產出已經不花什麼時間，重點回到了使用者自己的 taste 跟選擇。

最後定案的規格不是 moodboard，是同一套語言落到三種真實產出：網站、上課投影片、A4 文件都由 HTML render，換風格後能共享同一套設計 token。

![同一套視覺語言分別套用在網站、線上工作坊投影片、HR 導入案例 A4 文件三種真實產出的並排截圖](/blog/assets/posts/agentcrew-visual-system-design-process/3-applied-system.jpg)

中間也測過琥珀色系的變體，套在網站、YouTube EP.32 縮圖跟 HR 導入案例文件上一起比較。

![琥珀色系網站變體、YouTube EP.32 縮圖與 HR 導入文件並排展示同一套視覺語言的不同應用](/blog/assets/posts/agentcrew-visual-system-design-process/4-amber-variant.jpg)

我打算把這一串「外行人選品牌視覺」的過程打包成 skill，之後釋放給大家用。

<!--
新增非原文句子清單（忠實度自首）：
1. 「我不是設計師，但這週花了不少時間幫 AgentCrew Academy 選一套視覺系統。」— 類型：框架句
2. 「但一版不夠，我請它再大膽一點，於是有了 A 到 D 四個被否決的方向」— 類型：銜接
3. 「跟 GPT 合作的這一次感覺也很不錯，所以我覺得兩條路都行得通。」— 類型：銜接（原文為「所以我認為Either way works」，改寫成中文銜接句）
4. 「最後定案的規格不是 moodboard，是同一套語言落到三種真實產出」— 類型：銜接（呼應圖卡原文「規格不是 MOODBOARD」標語）
5. 「中間也測過琥珀色系的變體，套在網站、YouTube EP.32 縮圖跟 HR 導入案例文件上一起比較。」— 類型：銜接
-->
