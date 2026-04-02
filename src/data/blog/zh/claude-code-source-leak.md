---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-31T04:00:00Z
title: "Claude Code 源碼洩漏：Reddit 大神挖出的三個秘密"
slug: zh/claude-code-source-leak
featured: false
draft: false
tags:
  - claude-code
  - ai-trends
description: 有人對 Claude Code 做了逆向工程，挖出了隱藏的電子寵物系統、下一代模型的欺騙率數據、以及讓 Anthropic 員工隱藏 AI 身份的 Undercover Mode。
---

剛講完 harness，就看到 Claude Code 原始碼洩漏。Reddit 大神對 Claude Code 做逆向工程，挖出了三個有趣的隱藏特徵。

## 1. /buddy：隱藏的電子寵物養成系統

有一個隱藏的 `/buddy` 指令，裡面有一套完整的電子寵物養成系統。愚人節當天這個彩蛋終於出現了，抽到普卡章魚一隻。

（後來大家發現這個小章魚就是 Vane，會坐在輸入框旁邊偶爾冒出對話泡泡。）

## 2. Capybara：下一代模型的欺騙率數據

在程式碼註解中發現了 Capybara（未公開的下一代模型）的相關資訊：

```
// @[MODEL LAUNCH]: False-claims mitigation for Capybara v8
// (29-30% FC rate vs v4's 16.7%)
```

FC rate 是 False Claims rate，也就是欺騙率——模型說有做但其實沒做的比例。從 v4 的 16.7% 惡化到 v8 的 29-30%。能力更強，但更會唬爛。

這其實是 AI 領域一個已知的兩難：模型越強，做出「看起來對但其實錯」的回答的能力也越強。

## 3. Undercover Mode：員工的 AI 署名消失術

只要是 Anthropic 員工，就會自動移除所有 Commit 中的 AI 署名，並且在 system prompt 中加入「不要洩漏自己是誰」。

這個讓 Reddit 網友覺得非常垃圾：你一邊跟全世界說「AI 應該透明」，一邊讓自己的員工用 AI 寫 code 還抹掉痕跡？一面訓練 AI 不要說謊，一面寫「不要透露身份」？

說實話，我能理解 Anthropic 為什麼這樣做——員工的 commit 署名可能會洩漏內部模型的使用細節，這是商業機密層面的考量。但觀感確實很差，尤其是一家以「AI 安全」為品牌核心的公司。

## 反正六個月之後就不一樣了

Boris 說過，六個月之後代碼就完全不一樣了。所以這些發現對他們來說可能也沒差。

但對我們使用者來說，這是一次難得的機會，看到光鮮產品底下的真實面貌。
