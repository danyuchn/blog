---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "看清外面、想清裡面：兩個 Claude Skill 的分工"
slug: zh/competitive-analysis-skills
featured: false
draft: false
tags:
  - claude-code
  - skills
  - ai-workflow
  - competitive-analysis
description: 偶然看到一個競品賣得很好，第一反應是焦慮。但焦慮之前，我想先搞清楚它到底是什麼。最近用兩個 Claude Skill 把這件事做透——橫縱分析法看外面，第一性原理看裡面。
---

最近用 Claude Code 做了兩件事。

## 第一步：把讓我不安的東西研究透

偶然看到一個競品賣得很好，第一反應是焦慮。但焦慮之前，我想先搞清楚「這個東西到底是什麼」。

我用的是一個叫「橫縱分析法」的 Skill：

- **縱向**：它是怎麼一步步走到現在這個樣子？
- **橫向**：它跟同類產品比，差異在哪？

這兩個維度做完，焦慮就被替換成資訊。我會知道對方是「真的厲害」還是「行銷做得好」，知道我跟它的差距是哪些 gap、哪些不需要追。

## 第二步：把自己想清楚

把外面看清楚之後，下一步是回頭看自己。

這時候我用第一性原理 Skill：

- 我在做的事情，最底層的「為什麼」是什麼？
- 哪些是真的不能動的核心，哪些只是因為「大家都這麼做」？

很多時候焦慮的來源不是對方做得好，而是我自己沒想清楚。

## 兩個 Skill 的關係

- 一個幫你看清外面
- 一個幫你想清裡面

分開用都有效，但一起用才完整。

兩個 Skill 都公開在 GitHub，Claude 用戶可以直接裝：

- 橫縱分析法：<https://github.com/KKKKhazix/khazix-skills>
- 第一性原理：<https://github.com/danyuchn/first-principles-skill>

## 一個用法上的細節

這兩個 Skill 我都不會在「正式工作」的 session 裡用——而是在 plan mode 之前，先用它們做一輪研究跟思考，把資料跟結論收進筆記。等到要動手時，再開新 session、把整理好的結論帶進去。

把「研究」跟「執行」分開，避免了 context 過長導致的注意力稀釋。
