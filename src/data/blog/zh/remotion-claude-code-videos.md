---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T14:30:00Z
title: "用 Remotion Skill 半小時拍一支 Claude Code 教學影片"
slug: zh/remotion-claude-code-videos
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - productivity
description: Remotion skill 我下載好一陣子了，一開始只是玩玩。最近開始錄 Claude Code 免費教學系列才發現真的太好用——從口白討論到剪輯渲染，半小時出一支 15 分鐘影片，不 NG 也不費力。
---

Remotion skill 我下載好一陣子了，一開始只是玩玩，沒有放在心上。最近開始想把我使用 Claude 的心得錄成免費教學系列分享出來，才發現這個 skill 真的太好用了。

## 我的工作流程

我是先跟 Claude Code 用對話的方式跑一次：

1. **討論口白腳本**：我說想講什麼主題，Claude 起草腳本，我來回修幾次。
2. **我自己錄口白**：我喜歡親自錄，不喜歡電腦模擬音。用手機或 RØDE 就夠。
3. **Claude 根據口白做 Remotion 影片**：它會告訴我哪幾段需要錄製螢幕做示範。
4. **我錄好銀幕示範**：照它列的時間點跟內容錄。
5. **Claude 插入影片、渲染匯出**：交回給它接起來。

以上流程跑順一次之後，我就請 Claude Code 根據這個流程去修改 skill 本身，客製成我想要的形式。後面產一部精美的 15 分鐘教學短影片，從構思腳本到實際錄製只要半小時，不費力也不 NG。

Ep8「授權 vs 監督的平衡」就是這樣做的：9 幕純 Remotion 動畫，包含 2×2 可逆/不可逆矩陣、四種 Permission Mode 模擬終端機。橫版 22MB、直版 20.9MB 一次渲染完成，上傳 YouTube 直接發（<https://youtu.be/Nf6hCFhDOXQ>）。

Ep10「為什麼他是辦公室的最強助手」更進階一點：我把一份亂七八糟的會議原料丟給 CC，要它示範生出三種不同產出（決策備忘錄、報價比較表、週報補完），384 秒螢幕錄影加 intro/outro 配音一共 8:13，1080p 橫版 82MB（<https://youtu.be/B_ztF6QWhx4>）。

## 實戰踩坑：遮蔽像素要從 composition frame 量

合成階段有一個很容易翻車的坑。Ep8 做完後我要在螢幕錄影上加上馬賽克遮蔽（遮一些不想給人看到的檔案名跟路徑），結果遮蔽位置永遠對不上。

**原因**：Chrome download panel 各項目的 y 座標不能從原始錄屏座標推算，因為 letterbox 縮放後有偏移。必須從 composition frame 直接量。

**做法**：用 ffmpeg 把 composition 裁出一條細橫條再放大，逐 y 值掃描確認文字位置：

```bash
ffmpeg -i comp.mp4 -vf "crop=W:H:X:Y,scale=..." strip.png
```

以本次為例，合約那一段在 comp y=212–287、JSON 那一段在 y=82–210，兩者以 y=210 為界。弄清楚後遮蔽就一次到位。

## 為什麼 Remotion + Claude Code 特別搭

傳統的剪輯軟體（Premiere、DaVinci、Final Cut）你得手動對齊時間軸、手動調動畫參數、手動寫字幕。你會的越多，越被卡住——因為每個決定都要你自己下。

Remotion 是 React 元件，時間軸用秒數控制，動畫用 props 控制。這東西天生就是給程式碼生成的。Claude Code 可以一口氣生出 9 幕場景、對齊 SRT 時間戳、插入螢幕錄影的 videoSrc、渲染輸出——全程不需要開任何 GUI。

而且改東西很快。Ep10 我錄完螢幕後重構 composition，從「決策備忘錄」單一示範改成「一份原料→三種產出」的三段式，只花了一小時。用 Premiere 搞這種結構性重構，一個下午都未必做完。

## 給想錄教學影片的朋友

這個工作流對非編程背景的人特別友善。你不用學 React，不用學 Remotion 的語法，不用會剪輯。你只需要：

1. 想清楚要講什麼
2. 敢開口錄自己的聲音
3. 願意跟 Claude Code 來回對話幾次

剩下的它會處理。

如果你還在用 Canva/CapCut 做 AI 教學影片，試試這個方案吧。一個週末就能把你的 skill 建立起來，接下來每支影片都是半小時內搞定。
