---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: 別人去韓國做醫美，我叫 Codex 數位醫美
slug: zh/ai-video-pipeline-codex-to-claude
featured: false
draft: false
tags:
  - video-production
  - codex
  - ai-workflow
description: '從推特上看到有人把 Codex、Hyperframes、IndexTTS2、HeyGen 串成一條自媒體流水線，拉下來實測、順手玩 b 站的本地 TTS，幾天後換 Claude Code 重做一支。'
---

下午看到推特上有人把 Codex + Hyperframes + IndexTTS2 + HeyGen 串在一起成為一條自媒體流水線，弄了一個有 50 幾個 SKILL 的 repo 開源分享，我就拉下來做做看（剛好 HeyGen 有我一年前做的 Avatar）。repo 是 Pluviobyte 的 rnskill，原作者的推文在[這裡](https://x.com/Pluvio9yte/status/2081328645524668636)。

沒想到效果出奇的好。嘴型都有對到，講話也很清楚，動畫更是做得驚艷。雖然口播還是有 AI 感，但好像我真人放慢速度念稿也是這個感覺（？）

而且說一句不好聽的，我看那些 IG Reel，感覺很多人不如請 AI 寫稿，請數位醫美過的 Avatar 上鏡，還比他們真人做得不尬⋯（我就是其中之一）

別人去韓國做醫美，我叫 Codex 數位醫美。

![Threads 貼文截圖，配著 AI 生成的 Avatar 影片畫面，文字寫著「別人去韓國做醫美，我叫 Codex 數位醫美」](/blog/assets/posts/ai-video-pipeline-codex-to-claude/codex-avatar.jpg)

之後考慮部分的概念分享或短口播用這個做。

## b 站的 Index TTS 2

這幾天又發現了本地開源模型好物：Index TTS 2。這是 b 站開發的語音合成模型，支援零樣本 voice clone，可以微調各種參數，呈現不同的情緒。我試過之後覺得非常擬真，重要的是我這台跑得起來。

b 站真的在以各種方式造福我，平常看知識型影片找 b 站、看課程中配找 b 站、現在用模型還是找 b 站⋯

後來有人推薦我別的 TTS，我也說等等拉來測看看。不過我個人覺得 IndexTTS2 中國音不重（還是我的聲音樣本台灣音太明顯？哈哈）。之前有考慮過 minimax API，但最大的缺點是中英交雜時英文變得很奇怪⋯

## 換一個模型接手

前幾天的 AI 流水線影片用 Codex 做，現在額度平衡一下（氣死，還不 reset），所以今天這部影片用 Claude Code 做。還好那個開源 repo 裡面的 workflow、skills、內建的 project-level harness 已經寫得夠好，跟我原本的 harness 也很相容，所以換了模型根本沒有障礙，Claude Sonnet 5 high effort 也是一次過。

所以 harness 的個人維護還是很重要的，這樣不管你切哪一個工具，模型都能夠迅速上手接管你的任務。狡兔三窟大概就是這個意思。

<!--
新增非原文句子清單（忠實度自首）：
1. 「repo 是 Pluviobyte 的 rnskill，原作者的推文在[這裡](https://x.com/Pluvio9yte/status/2081328645524668636)。」 — 類型：銜接（來源標註，事實由派工方提供）
2. 「別人去韓國做醫美，我叫 Codex 數位醫美。」 — 類型：改寫（原為獨立貼文，此處收攏為承接圖片的單行）
3. 「後來有人推薦我別的 TTS，我也說等等拉來測看看。」 — 類型：銜接（原為回覆別人的貼文，補上一句情境交代，用詞取自原文「我等等拉來測看看」）
4. H2 標題「b 站的 Index TTS 2」、「換一個模型接手」 — 類型：框架句（分節用）
-->
