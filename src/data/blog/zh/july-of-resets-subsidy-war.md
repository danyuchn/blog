---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: 充滿 reset 的七月：一個 AI 輕量用戶的補貼大戰復盤
slug: zh/july-of-resets-subsidy-war
featured: false
draft: false
tags:
  - ai-economics
  - subscription
  - token-optimization
description: '七月一有 reset 就用好用滿，帳面發揮 57.5x 的價值；順便記下補貼大戰、Deepseek 漲價，和我對下一次重置的預測。'
---

AI 輕量用戶來復盤一下這個「充滿 reset 的七月」的狀況。

Claude、Codex 各訂 100，一有 reset 就用好用滿，如圖所示，發揮了 57.5x 的價值（計算價格已經排除掉裡面的本地模型 qwen 系列）。

![七月整月的 ccusage 用量表格截圖，全部合計 2.33 億 input tokens 與 6119 萬 output tokens，等值 11501.51 美元；其中 Claude 一列 7415.12 美元、Codex 一列 4086.39 美元](/blog/assets/posts/july-of-resets-subsidy-war/1-july-usage.jpg)

我蠻期待 OpenAI 或 Anthropic 任何一家上市，因為市場才有機會看到真實的 token 成本。

補貼大戰不知道會持續多久，GPT 昨天又宣布降價，Kimi／Deepseek 也在持續讓 benchmark 貼近、把價格打下來，局勢看得不是很明白，但看明白我們市井小民也不能改變啥。

## 個人已經在積極做的

把 harness 持續瘦身（這週減了 40% 常駐注入的 token）、部分非常單純的單發任務路由到本地模型夜間做，或者走量大管飽的 Gemini 訂閱方案（antigravity CLI）。

未來打算做的進一步分流：非敏感資訊，或者透過本地……

## Deepseek 那張圖可能要作廢了

之前盛傳「Deepseek CP 值斬殺線」的那張圖，可能很快就要作廢了。Deepseek 宣布即將大幅調漲 API 價格。

![X 上 Jukan 帳號的貼文截圖，內容為 DeepSeek 計畫近期全面調漲 API 價格且幅度顯著，下方附 DeepSeek 平台用量頁面的公告橫幅，以及餘額 19.75 美元、累計花費 0.24 美元的欄位](/blog/assets/posts/july-of-resets-subsidy-war/2-deepseek-price.jpg)

想像得到 Luna／Terra 在偷笑。

## 關於 reset 本身

經過我的（不專業）研究，OpenAI 給的重置沒有想像中大方：重置後七天窗口重新計算，Anthropic 則是七天窗口固定，後者其實是讓你在重置後用較短的窗口享有 100% 額度。而且觀察過去的重置宣布時間，都卡在之前發的 banked reset 快過期的時候。

所以我在此立帖為證，8/12-14 一定重置，到時候大家可以回來看。為什麼呢？因為 Tibo 很賊，都會選重置卡到期日故意重置，最後一張重置卡到期日是 8/13。

另外一個體感：Codex 100 USD 的週額度，好像比 Claude 100 USD 少。還沒有統計 token usage，所以這只是體感，有人跟我有一樣的感受嗎？不知道是因為 Opus 5 太耐用，還是因為 Codex 我用了太多瀏覽器跟電腦控制任務。

還有一件事順帶記一下：Anthropic 最新文章只並列 Fable、Opus、Sonnet，完全沒提 Haiku。Sonnet 看起來正在接手原本 Haiku 的位置，這也是一種不明說的漲價；Haiku 很可能停在 4.5。

Anthropic 摳死～

沒了額度就去 x 留言給 tibo 祈願，reset 了就 `/model sol max`，徹底沒了就掏出信用卡哭著刷 200。

<!--
新增非原文句子清單（忠實度自首）：
1. 「AI 輕量用戶來復盤一下這個「充滿 reset 的七月」的狀況。」 — 類型：改寫（原文為同句去掉句尾冒號）
2. 「## 個人已經在積極做的」 — 類型：框架句（原文第 4 點的條列開頭「個人已經在積極做的：」轉為小標）
3. 「## Deepseek 那張圖可能要作廢了」 — 類型：框架句（由該段內容生成的小標）
4. 「## 關於 reset 本身」 — 類型：框架句（純分節用小標）
5. 「所以我在此立帖為證」的「所以」 — 類型：銜接（原文為「我在此立帖為證」）
6. 「另外一個體感：」 — 類型：銜接
7. 「還有一件事順帶記一下：」 — 類型：銜接
8. 兩張圖片的 alt 描述句 — 類型：改寫（依圖片實際內容描述，非原貼文文字）
其餘句子皆為原貼文與既有 micro-notes 條目逐字或近逐字保留。第 5 點「非敏感資訊，或者透過本地」為原文截斷處，未續寫。
-->
