---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: CLI 是親生的，其他都是後媽養的
slug: zh/cli-is-the-firstborn
featured: false
draft: false
tags:
  - claude-code
  - anthropic
  - developer-experience
description: '新功能和剛修好的 bug 都優先落在 CLI，remote control 要等猴年馬月。同一家公司的產品，更新頻率差很多。'
---

因為新的功能或者剛修的 bug 都會優先在 CLI，所以 CLI 是原生第一環境。remote control 要更新要等猴年馬月。

呃，我舉個例子。早期的 remote control 環境中，打斜線不會有提示 SKILL 選單，所以除非記得 SKILL 全名，不然叫不出來。這還是 remote control 推出三個月後才修復的。

他們全都是 Anthropic 原生，但親生的孩子也是有偏心。CLI 一天一更最頻繁（因為員工自己就在用），Desktop 以前很慢、後來大改版更新變勤了，其他的就都慢吞吞。看 CHANGELOG 打 remote control，你就可以看到跟他相關的修復頻率了。

那如果平常在家電腦都用慣 CLI 的情況下，直接讓 CLI 鏡像到移動設備不是最方便的嗎？

![手機上透過 mosh 連回 Mac mini 跑 CLI，畫面是 agent 正在把一批 gog CLI 的工具陷阱寫進文件的 diff](/blog/assets/posts/cli-is-the-firstborn/1-remote-control.jpg)

為什麼不用官方 Claude / Codex 的雲端控制手機 App？

因為他們不知道何時才會出 split pane⋯

![手機畫面上下同時開著兩個 pane，各自是一個獨立的 CLI session](/blog/assets/posts/cli-is-the-firstborn/2-no-split-pane.jpg)

還有一個非常奇怪的事情：以前一天一更的 Claude Code CLI，竟然已經 8 天沒有更新了。經過機器人強力去重後的 Issues 仍然穩定在五千上下，所以不代表沒 bug 可修。

![anthropics/claude-code repo 的 GitHub 頁面，Issues 顯示 5k+，最新 commit 標著 v2.1.220、committed last week](/blog/assets/posts/cli-is-the-firstborn/3-cli-no-update.jpg)

是不是在蹲一波什麼大的，還是內部發生了什麼劇烈的調整，目前未知。

跟他們之前大力宣傳的 AI 自我修復工作流，差別很大吧。只能說這家公司，說的跟做的要分兩套來看。

<!--
新增非原文句子清單（忠實度自首）：
1. 「還有一個非常奇怪的事情：」 — 類型：銜接（原文為「一個非常奇怪的事情：」獨立成則，此處加「還有」串接上一段）
2. 三張圖片的 alt 描述句 — 類型：銜接（依主對話提供的圖片內容說明改寫，非作者原文）
3. 標題「CLI 是親生的，其他都是後媽養的」與 description — 類型：框架句（由原文「親生的孩子也是有偏心」與首則貼文改寫）
其餘正文句子全部為原貼文逐字或僅做標點／全形空白調整。
-->
