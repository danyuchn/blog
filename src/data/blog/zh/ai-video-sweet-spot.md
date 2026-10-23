---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-20T13:32:00Z
title: AI 做影片的甜蜜點：自己出鏡，剪接和逐字稿交給 AI
slug: zh/ai-video-sweet-spot
featured: false
draft: false
tags:
  - ai-tools
  - video-production
description: '自己錄旁白出鏡、畫面動畫用 AI 輔助；Astra 配 DaVinci Resolve 剪六天 vlog 做掉最費工的 90%；逐字稿用 Qwen 3 ASR 就夠。'
---

我覺得還是自己錄旁白出鏡，但是畫面動畫用 AI 輔助，會是甜蜜點。

## 剪接最費工的 90%

用 Astra + DaVinci Resolve 剪六天的 vlog，素材是 iCloud 項目＋Google 地圖時間軸軌跡＋我的 email。他自己去猜我六天的行程長怎樣，自己寫文字、編排順序、匯入、找音樂。老實說已經把剪接最費工的 90% 都做完了吧，20 USD 月費的週用量大約花 40%。

之前在 [Luna Max 那篇](/blog/posts/zh/gpt-5-6-luna-max-grunt-work)也補記過：Davinci Resolve Studio 配 MCP 給 Luna Max 操控，就是新世界影片後製的神。

## 旅行回家的第一件事

所有手機、DJI 全部插 Mac mini，讓 Claude Code 自己去把旅行拍的抓出來，自己去重、自己做素材分類，然後也去幫我導出 Google Map 的 GPS 時間軸＋Gmail、行事曆的內容，交叉比對，最終目標是做出 vlog。然後我人就跑去拆行李洗衣服了。

![終端機截圖：Claude Code 趁 DJI 在背景複製時先讀 Google 時間軸排出行程，我提醒時間軸地點存疑時要以圖片為準，它改以照片的 GPS 和畫面內容為主，並對兩支手機的檔案跑 EXIF 分析](/blog/assets/posts/ai-video-sweet-spot/travel-vlog-timeline.jpg)

通常行李拆完的同時，vlog 也就做完了。

## 逐字稿其實不用買貴的

Qwen 3 ASR ＋ hotwords 自定詞庫 ＋ pyannote 說話者辨識，其實就非常夠用了。
