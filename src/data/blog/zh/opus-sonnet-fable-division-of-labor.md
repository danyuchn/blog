---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-02T01:01:00Z
title: Opus 指揮、Sonnet 實作、Fable 當顧問：三個模型的分工
slug: zh/opus-sonnet-fable-division-of-labor
featured: false
draft: false
tags:
  - claude
  - model-comparison
  - ai-workflow
description: 'Opus 5.5、Sonnet 5.5、Fable 5.1 都有了之後，我自己的分工是 Opus 親自指揮驗證部署、Sonnet 當 subagent 實作、Fable 偶爾請出場當顧問。'
---

## Fable 的意義

很多人都在說，Opus 5.5 跟 Fable 5.1 都有了，而且 Opus 的能力又比 Fable 強，那 Fable 的意義到底是什麼？

講一下我自己的觀察：

我感覺 Fable 的預訓練參數量可能更大，所以它的世界觀比較廣。同一件事丟給它，常常會看到一些我自己都不知道的邊界問題，就是那種我根本沒想到要問，它自己先提出來的東西。

所以我現在的分工大概是這樣：實作交給 Opus，比較大的架構或策略，交給 Fable 看。

像我這幾天在整理 GMAT 的服務流程規格，是 Sonnet 先抽 61 份資料、Opus 寫，最後 Fable 審。每週例行要砍掉哪些步驟，我也是先讓 Fable 做一輪對抗式審查，看完再自己拍板。這種時候 Fable 的視野對我來說更像一個導師。

對我來說這兩個模型都還是很有必要。不過 Opus 5.5 出來之後，以前那種不講人話的毛病有改善，額度也更省了。我覺得整體是在往好的方向前進。

## Sonnet 5.5 實測

Sonnet 5.5 實測完了，幾個懶人結論：

1. 不要亂開 Max，想開 Max 不如直接開 Opus 中高檔位還比較省
2. 個人感覺甜蜜點是 med + Opus 5.5 幫忙寫好的固定工作流或 SKILL，才能真的省到額度，不然大部分情況下我還是會選擇直接開 Opus 5.5
3. 要小心，如果作為調查型子代理常常會越權寫檔，在意的話請在 harness 中好好規範

這個模型的成本效益甜蜜點我覺得非常狹窄（因為 Opus 5.5 已經過於划算...），所以上面第二點是最重要的。對於 A\ 的意義大概就是抽同樣價格的 6 Sol 一巴掌吧。

後來我又讓 Sonnet 5.5（effort high）不帶 SKILL、不用工具，純編寫程式碼完整做產品的 demo 影片。結論是也做得到好的成品，但明顯中間考慮到的細節較少，且輪次比較多，比較耗 token。比起 Opus 的自主善用工具，Sonnet 明顯更主動尋求人為介入。

本來按慣例應該是要繼續把 effort 調高的，但是暫時不想浪費 token 去測。我覺得最好的用法應該是作為被派工的 Subagent 了。

而且這應該也最像是我心中理想的分工：

- Opus 親自指揮、親自驗證、親自部署。尤其 5.5 理解對齊人類意圖跟自主性非常強，適合親自對話
- Sonnet 實作。5.5 能力夠，但是需要有強模型驗證跟偶爾搭手介入，適合讓主 agent 跟他對話就好，親自對話會因為讀心能力弱而搞得人類有點煩
- Fable 作為顧問，給 Opus 策略面上的第二意見。他的知識邊界明顯比 Opus 更廣，更適合看到 unknown unknowns。雖然也適合親自對話，但奈何實在太貴，偶爾 /advisor 請出場就好

## Reddit 風向

Sonnet 5.5 發布大概 15 小時的時候，我去 Reddit 翻了一下風向。

發布當下的氣氛是超興奮，一堆人在分享，比如 Mario Kart 一個 prompt 生出來、3D 殭屍 FPS 49 分鐘做完、寫作 benchmark 排第 2，只輸 Opus 5.5。

幾小時後開始有人拆解 benchmark。Terminal-Bench 那個「Sonnet 打贏 Opus」的 70.6% 對 66.4%，兩邊 effort 根本開不一樣，不能互比。

有人貼出 Sonnet 5.5 Max 每題大約吃 $7.60，比 Opus 5.5 Max 的 $5.98 還貴。所以「便宜一半」看起來只有 low / medium 才成立（？

當時 Reddit 的共識：

1. 主力寫程式：Opus 5.5 high
2. Sonnet 5.5 用 medium 或 low
3. 最被認可的用法是當 subagent，Opus 規劃、Sonnet 實作
4. 規格寫清楚的任務也好用，有人說它比較不會亂加東西
5. 免費層，還有 API 高量、低難度的工作

## 系統卡

我在讀 Sonnet 5.5 的系統卡，這一段最有趣（請讀圖）。

![Gemini 整理的 Sonnet 5 系統卡模型福利段落截圖，第一張](/blog/assets/posts/opus-sonnet-fable-division-of-labor/1-system-card.jpg)

![Gemini 整理的 Sonnet 5 系統卡模型福利段落截圖，第二張](/blog/assets/posts/opus-sonnet-fable-division-of-labor/2-system-card.jpg)

![Gemini 整理的 Sonnet 5 系統卡模型福利段落截圖，第三張](/blog/assets/posts/opus-sonnet-fable-division-of-labor/3-system-card.jpg)

Gemini 給出的總結好鮮活也好到位：

> 從這份報告拼湊出的 Sonnet 5，就像是一個「技術過硬、情感抽離、能被罵但絕不背鍋、看透了公司考核制度但依然默默把程式碼寫完」的職場老鳥工程師

這不就是我嗎（？

系統卡原文在這：[Claude Sonnet 5 System Card](https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf)

## 補充：適度讀心

補充一點：會思考使用者的真實意圖（適度讀心）。

這對我很重要，我下 prompt 都會給脈絡，GPT 6.1 sol 看不懂只會按字面（6 更不用說），但是 Opus 5.5 掌握得很好。

當然也有嚴格要按字面來的任務，或許那裡 GPT 比較適合也說不定。

甚至在長上下文壓縮後，這個讀心的準確度也沒有跑掉多少，這個就不知道是 base model 強還是 claude code harness 強了。

## 補充：opusplan

Claude Code CLI 冷知識：`/model opusplan` 是一個特殊的代號，用了之後會自動進入 Opus 5.5 Plan Mode，但是實作轉 Sonnet。

<!--
2026-10-09 W42 併入碎念：「opusplan」（10-02 Threads 貼文）新增為一節，小標為框架句，自碎念存檔刪除。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「Opus 指揮、Sonnet 實作、Fable 當顧問：三個模型的分工」 — 類型：框架句（title）
2. 「Opus 5.5、Sonnet 5.5、Fable 5.1 都有了之後，我自己的分工是 Opus 親自指揮驗證部署、Sonnet 當 subagent 實作、Fable 偶爾請出場當顧問。」 — 類型：框架句（description，內容取自原文）
3. 五個 H2 標題（Fable 的意義／Sonnet 5.5 實測／Reddit 風向／系統卡／補充：會思考使用者的真實意圖） — 類型：框架句
4. 「Sonnet 5.5 發布大概 15 小時的時候，我去 Reddit 翻了一下風向。」 — 類型：改寫（原「發布大概 15 小時了，去 Reddit 翻了一下風向，幫大家整理」）
5. 「後來我又讓 Sonnet 5.5……」的「後來」 — 類型：銜接
6. 「當時 Reddit 的共識：」 — 類型：改寫（原「現在Reddit的共識」）
7. 「系統卡原文在這：[Claude Sonnet 5 System Card](…)」 — 類型：改寫（原文為「同串附系統卡連結」）
8. 三張圖片的 alt 句子 — 類型：框架句
9. 「Sonnet 5.5 實測完了，幾個懶人結論：」由兩行合為一句；多處斷句／標點微調；刪除原文末尾的表情符號 — 類型：改寫
10. 「調查行子代理」更正為「調查型子代理」 — 類型：改寫（錯字）
-->
