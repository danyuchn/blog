---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-23T04:00:00Z
title: "Gemini 3.5 Flash Reddit 實測彙整——貴三倍、Vision 退步、Tool Calling 災難"
slug: zh/gemini-3-5-flash-reddit-review
featured: false
draft: false
tags:
  - gemini
  - model-comparison
  - ai-industry
description: 'Gemini 3.5 Flash 上線後 Reddit 用戶實測回報彙整：價格比 3 Flash 貴三倍、Vision 退步、Tool Calling 跑到 32 次被中斷。正面是速度快且程式碼風格好，但整體評價偏負面。'
---

Gemini 3.5 Flash 發布後，Reddit 上的實測回報陸續出爐。整理三個面向的社群反應。

## 價格衝擊——最大怨言

這是最多人抱怨的點：

- 比 Gemini 3 Flash 貴三倍（一篇 262 分的帖子專門在講這件事）
- 價位已接近舊版 2.5 Pro / 3.1 Pro——「Flash 現在是 Pro 價，那 Flash 的意義在哪？」
- Artificial Analysis 實測成本：3.5 Flash $1,550 vs GPT-5.5 Medium $1,200，每分數成本 $28 vs $21，GPT-5.5 Medium 更便宜也更強
- 「cheap and good 現在叫 DeepSeek v4 Flash」——不少人直接推薦轉用 DeepSeek
- 消費端限額更嚴：Pro 訂閱用戶在 5 小時窗口內 15 分鐘就撞 rate limit；單一 prompt 可耗 13-25% 的 5 小時配額

## 正面回饋

正面評價集中在速度：

- 一位開發者跑 coding benchmark，3.5 Flash 已完成時 GPT 5.5 還在跑。體感 10 倍速差
- 程式碼風格自然拆分模組，不像 GPT 5.5 寫巨型 monolith
- SWE benchmark 只差 GPT 5.5 約 3.5%，日常開發可能感受不到差異
- 有葡萄牙語用戶回饋：某高難度任務 GPT 5.5 做 15 分鐘品質差，3.5 Flash 7 分鐘完美

## 負面回饋——佔多數

負面評價不只是貴，能力也退步了：

- **Tool calling 災難**：Opus 4.6 用 2 次 tool call 解決的任務，3.5 Flash 跑到 32 次被強制中斷，benchmark 只拿 13 分
- **Vision 退步**：用戶用自建 eval 跑 10 組測試，3.5 Flash 在 vision 任務排第 13，低於 3 Flash 和 3.1 Flash Lite。重複 5 次取平均，非偶然
- **Coding 分數低**：Artificial Analysis coding 項 45 分（3.0 Flash 43、3.1 Pro 55、GPT-5.5 Medium 56）
- **過度自信**：「Overconfident and says a task is complete when it wasn't」
- **Hallucination**：短漫畫分析完全離題，反而 Gemma 4 Edge Gallery 看懂了
- **知識斷層**：Knowledge cutoff 仍停在 2025 年 1 月
- **Hard knowledge + computer use**：「Unusable compared to 5.5 and Opus」

## 我的看法

Flash 系列存在的意義是「便宜且夠用」。當價格逼近 Pro 等級但能力沒有跟上，定位就崩了。如果你需要快速且便宜，目前 DeepSeek v4 Flash 或舊版 Gemini 3 Flash 可能是更務實的選擇。如果你需要品質，那直接用 Opus 或 GPT-5.5。卡在中間的 3.5 Flash，目前看來是個尷尬的存在。
