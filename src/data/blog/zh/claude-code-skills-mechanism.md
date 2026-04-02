---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-01T04:00:00Z
title: "Claude Code Skills 機制解密：按需載入與觸發率真相"
slug: zh/claude-code-skills-mechanism
featured: false
draft: false
tags:
  - claude-code
description: Skills 不會把全部提示詞預設注入上下文。它是一層一層按需載入的。但被動觸發率只有 30-50%，打 slash 才是最保險的。
---

常看到有人擔心：裝了一堆 skill，會不會把全部 skill 的提示詞預設注入上下文，導致記憶力稀疏？

不會。

## 按需載入的機制

Skills 的誕生，原始就是為了解決「上下文窗口被某些特定場景才會用到的提示詞佔滿」的問題。

每個 skill 前面都有一段 YAML frontmatter，裡面放了一段短的 description，說明這個 skill 的用途跟觸發時機。只有這個 description 會注入上下文。當模型根據 description 判斷這個 skill 需要用到後，才會進一步載入 skill 主檔 SKILL.md。然後再按照裡面的索引，按需載入 `/reference` 裡面的子情境 md，或者是 skill 裡面包好的腳本。

所以就是一層一層按需載入，不會有「把全部 skill 的所有提示詞預設注入上下文，導致記憶力稀疏」的問題。

在 Claude Code 裡面打 `/context`，你會看到每個 skill 注入的 description 大約就 100 token 而已。

## 但被動觸發率只有 30-50%

機制設計得很好，但有一個現實問題：description 的被動觸發率只有 30-50%。

也就是說，你明明在做一件某個 skill 可以幫上忙的事，但模型有一半的機率不會自動觸發它。尤其是當你注入的 memory、rules 越多，模型的注意力就越稀疏，觸發率更低。

所以打 `/` 手動呼叫 slash command 是最保險的。別指望模型每次都聰明到自己知道該用哪個 skill。

## 怎麼提高觸發率

根據經驗，幾個做法可以幫助：

1. **Description 寫得精準**：觸發關鍵字要明確。不要寫「處理各種任務」，要寫「當使用者提到 PPTX、簡報、投影片時觸發」。
2. **不要裝太多 skill**：每個 skill 的 description 都會佔上下文，裝 50 個 skill 就是 5000 token 的常駐開銷，注意力會被稀釋。
3. **養成打 slash 的習慣**：確定要用的 skill，直接 `/skill-name` 呼叫。被動觸發當作 bonus，不要當作主要依賴。
