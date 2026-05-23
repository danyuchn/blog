---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-23T04:10:00Z
title: "別一味貶低 Gemini——四個其他家打不過的 Use Case"
slug: zh/gemini-unbeatable-use-cases
featured: false
draft: false
tags:
  - gemini
  - model-comparison
  - ai-tools
description: '最近 Codex 跟 Claude 搶盡風頭，Gemini 好像被嫌棄了。但 Gemini 有四個其他模型打不過的場景：Flash Lite 性價比、音訊多模態、影片理解、書籍掃描 OCR。'
---

最近 AI agent 圈子好像都是 Codex 跟 Claude 的戲，但凡用 agent 的都會或多或少嫌棄 Gemini。

但 Gemini 有四個其他家真的打不過的 Use Case。

## 1. 大量資料清洗——Flash Lite 性價比之王

長文本、大量資料清洗用 Flash Lite，是中國以外的閉源模型中性價比最高的。如果信不過中國 API 端點、不想用 OpenRouter 的第三方、又無力架本地模型，Gemini 是最好的選擇之一。

## 2. 音訊多模態——聽得懂旋律

Gemini 的音訊處理不只是語音轉文字。它可以處理多講者、辨識語氣，甚至能「聽懂」音樂旋律中副歌和過門的準確位置。

我曾經玩過用 Strudel 接歌，讓 Gemini 辨識音樂素材中的段落切換點，準確度極高。這個能力目前 Claude 和 GPT 都做不到。

## 3. 影片理解——一步到位

有個學員的需求是從大量家族出遊影片中，把有家人的片段撈出來，捨棄純風景跟路人的部分。

如果交給 Claude 做，只能逐幀擷取圖片再辨識，流程冗長。但 Gemini 可以一步到位看懂影片內容，直接標記哪些段落有目標人物。

## 4. 書籍掃描 OCR——圖文座標回傳

另一位學員要把掃描的書籍數位化。Claude 對拉丁字母外的語言辨識度較差，附圖的辨識也差強人意。

Gemini 不只能準確辨識圖片中的文字，還可以回傳圖片在圖檔中的座標，供程式碼擷取。這在做書籍數位化的 pipeline 時非常實用。

## 結論

一味貶低 Gemini 的人，通常是 use case 看得不夠多。每個模型都有自己的甜蜜點，選工具不是選陣營。
