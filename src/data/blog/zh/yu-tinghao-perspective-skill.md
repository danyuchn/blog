---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "我做了一個「庭皓 SKILL」——把財經 YouTuber 的觀點蒸餾成 AI"
slug: zh/yu-tinghao-perspective-skill
featured: false
draft: false
tags:
  - claude-code
  - skills
  - ai-workflow
description: '用沒燒完的閒 token 做了一個庭皓 SKILL：蒸餾 17 部財經速解讀、3-4 輪盲測驗證，還發現 AI 跟人類講黃段子的邏輯不太一樣。'
---

前天 Claude 額度重置，但明天又要例行重置，好多 token 沒燒完，我決定讓他週末在家全職研究：

> 「投資朋友 歡迎收聽下午財經速解讀
> 現在是台北時間 2026 年 5 月 30 日 禮拜天 下午 4 點 57 分
> 大家午安我是庭皓 ...」

我做出了一個「庭皓 SKILL」。

目前蒸餾了 17 部早晨財經速解讀，經過 3-4 輪迭代盲測驗證，立場面、方向面、分析思維面高度一致。

黃段子與歇後語部分則因為皓哥儲備量過於浩瀚淵博，資料庫還在擴充建構中。

裝上這個 SKILL，你的 AI 也能變成皓哥。

做法上，是用 yt-dlp 把影片逐字稿抓下來，再交給 Gemini 整理，然後依 Anthropic 官方的 progressive-disclosure 原則拆成主檔加幾個參考檔。驗證方式是：根據 undistill 的影片逐字稿抽取未經解讀的 raw fact、data & news，請 SKILL 生成皓哥的觀點跟話術，然後再比對真實逐字稿皓哥是怎麼解讀的。

repo 放在 [github.com/danyuchn/yu-tinghao-perspective](https://github.com/danyuchn/yu-tinghao-perspective)，公開版有把逐字稿排除掉（版權考量）。如果不是這週意外重置我絕對沒有這種閒 token。歡迎大家 PR 補充。

玩下來最有意思的一點：感覺他的思維邏輯跟人類不太一樣。

為了解釋觀念才用黃段子（AI）；為了講黃段子再去找事件（人類）。

然後還是有點用力過猛了，沒有我們皓哥隱晦含蓄的東方語言美學。

給投資朋友做一些參考。如果喜歡我們節目，記得幫我們訂閱按讚加分享。那我們就明天早上八點半，財經速解讀再相見。祝各位投資朋友看盤順利、操盤愉快。
