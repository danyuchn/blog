---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-04T04:00:00Z
title: "GPT-image-2 越少約束越好，加上一個一致性練習"
slug: zh/gpt-image-2-prompting
featured: false
draft: false
tags:
  - ai-tools
  - gpt-image
  - ai-daily-use
  - prompting
description: 國外最近流行的「笨拙塗鴉風」prompt，越約束越糟，越放任越驚喜。這篇整理我這週對 GPT-image-2 的觀察：包括為什麼透過 Claude 轉交反而會壞事、以及在 Canva 場景下「保持一致性」這件事比生圖能力更值錢。
---

## 笨拙塗鴉風的爆紅

最近國外最流行的 GPT 生圖指令是這樣：

> 「請用最笨拙、塗鴉、毫無價值的方式重繪附件圖片。使用白色背景，並讓它看起來像是用滑鼠在小畫家裡畫的。」

效果意外地好笑。Reddit 上已經出現大量大作合集：<https://www.reddit.com/r/ChatGPT/comments/1t0pyb4/gpt_image_2_prompt_that_is_viral_right_now_redra/>

我自己試了一下：

![笨拙塗鴉風的成果](/blog/assets/posts/gpt-image-2-prompting/crayon-result.jpg)

## 越少約束越好

有個意外發現：在一開始創造圖片時，**在 Codex 內部直接手動下指令，會比 Claude Code 轉交 Codex 還要好**。

因為 Claude 常常會下出過度約束的 prompt，把每個細節都規範清楚，但 GPT-image-2 反而是越少約束越能展現其創意跟美感。

中介層越多，原始意圖越容易被「修飾」掉。如果你有試過讓 Claude Code 透過 MCP 轉接其他模型生圖，下次直接用該模型 native 的 prompt 介面，比較一下結果差異。

## 真正的難題：一致性

ChatGPT 最新的生圖模型大家都在玩，能力的確比 Google 的生圖模型強不少倍。但是要真正用在工作上，你還要學會懂得保持「一致性」。

你應該有遇過這些情況：

- 越聊越歪，叫他改 A 結果 B 也順手亂改
- 越改噪點越多、字越來越糊

這就是一致性的問題。生圖模型的「創意」剛好就是它的「不可控」，工作場景下這是雙面刃。

## 結合 Canva 的工作流

這也是為什麼 Canva 在這個世代還有用——它讓你把「AI 生的素材」放進「人工控制的版面」。

生圖階段越鬆越好，發揮 GPT-image-2 的長處；版面階段越緊越好，用 Canva 控制一致性。

詳細的教學影片在這：<https://www.youtube.com/watch?v=hzrBXjgCLG8>
