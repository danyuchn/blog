---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-09T04:00:00Z
title: 客戶的對話為什麼會飄掉
slug: zh/why-client-conversations-drift
featured: false
draft: false
tags:
  - ai-workflow
  - consulting
  - skills
description: '一次客戶診斷的隨筆：三條病狀根因、五條解方，外加主副 agent 反過來搭的模型組合，以及只有 hook 治得了的話癆。'
---

隨筆記一下今天客戶學到的東西。

## 客戶的病狀根因

- 沒有訂好 spec，context 太亂，long-context 模型產出 drift。
- model tier 與 effort 設定錯，模型沒有 budget 做 verification。
- 沒有發散收斂的節奏：想延伸時模型收斂，想收斂時模型發散。

## 我開的解方

**一、三層模型分工**：Fable 規劃、Opus 執行、Sonnet 調查，搭配 effort 設定。

講到模型搭配，順便講一個跟多數人相反的用法。大部分的人的模型搭配好像都是「主 Agent 用強的，subagent 用弱的」。但我最近也喜歡用另外一種方式：「Subagent 用強的，主 Agent 用弱的」。

我會把它想像成是臨時請一個顧問，來給一次性的建議。其實也很好用，而且範圍明確（指定他要讀的文檔）時非常省 token。

小廟不一定要一直供著大佛。

**二、對話飄掉的兩個根因**：結論沒落成檔案、model tier/effort 沒設對。

**三、用 grill-me 把模糊感受逼問成具體規劃**：known-knowns / known-unknowns / unknown-unknowns。

**四、診斷 prompt 寫法**：要求 AI 先 pinpoint root cause，再建 traceable/observable infrastructure（每個節點留 log）。

順著 prompt 跟 rules 講下去，還有一件事：只有好的 hook 才能治得了 Opus 5 的話癆，望周知。官方建議說 5 代模型的 rules 要精簡，但是 5 代模型本身並不知道這件事。

**五、四個工具**：explain（白話重講）、history-find（跨工具語意搜尋）、stt（語音輸入）、Codex plugin（對抗式覆核）。

<!--
新增非原文句子清單（忠實度自首）：
1. 「講到模型搭配，順便講一個跟多數人相反的用法。」 — 類型：銜接（把 09-07 那則接到三層模型分工後面）
2. 「順著 prompt 跟 rules 講下去，還有一件事：」 — 類型：銜接（把 09-05 那則接到診斷 prompt 寫法後面）
4. 五條解方的標題化粗體（「一、三層模型分工」等）為原文編號清單的排版改寫，內容逐字保留 — 類型：改寫
其餘句子均為三則原文逐字。
-->

<!--
主對話回收（2026-09-11）：砍掉收尾句「就這樣，隨筆一則。」——與開場「隨筆記一下」重複，且為原素材沒有的框架句。
-->
