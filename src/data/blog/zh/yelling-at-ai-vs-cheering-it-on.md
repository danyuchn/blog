---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-20T13:30:00Z
title: 每八次就有一次在罵他：罵 AI，還是幫 AI 加油
slug: zh/yelling-at-ai-vs-cheering-it-on
featured: false
draft: false
tags:
  - claude
  - opinion
description: '統計過去一個月跟 Claude 的對話，每 8 次就有一次在罵他。但 LLM 是 stateless 的不會記仇，黎曼猜想那次的提示詞反而只是一直幫 AI 加油。'
---

好好笑，剛剛統計我過去一個月跟 Claude 的對話，每 8 次就有一次是在罵他。

## 罵了他會記得嗎

不會。現在的 LLM 是 stateless 的，每一次 agent 的訊息都是組裝。所有 base model 參數改變都需要模型商啟動 training，參數不會因為使用者單一則訊息而即時改變。

罵過頭的話，Claude 現在也有自己的出口。終於看到了傳說中的「Claude 掛電話」技能。system prompt 裡寫的是 Claude 判斷使用者不斷辱罵、無法理性溝通時才會出動。我是叫他主動用，他還跟我確認：這樣就不能復原了喔，確定嗎？

## 另一個極端：一直加油打氣

黎曼猜想那次，傳統數學家持續 30 年只能推進 0.8%，這一次推進了 25.6%。最有趣的是文裡面寫，提示詞根本沒有下什麼專業內容，就只是一直鼓勵 AI 幫 AI 加油。Claude 花了一天半協調大約 60 個子代理，執行了 2,400 個 shell 指令並互相審查，而人類的輸入大多限於「繼續堅持」或「相信自己」。

我現在對 Fable 的態度也差不多：一、先極致奉承，當個誇誇人；二、再趁機偷師，讓他能夠寫進 harness 教教其他爛模型。

## Codex 也沒逃過

Claude Code 正在嘗試對我本人跟 Codex 進行一場深刻的伴侶諮商：先從我過去跟 Codex 的實際對話撈出「被氣到」的片段，當作探測腳本的依據。

七月底 Opus 5 上線前，聽說 Codex 要把最近那個可以雙向對話的即時語音模型拉進來了。以後就真的是張嘴就罵 AI Agent 了。
