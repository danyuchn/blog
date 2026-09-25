---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-24T04:00:00Z
title: "Opus 5.5 發布週：從重置卡到 Reddit 風向"
slug: zh/opus-55-launch-week-reddit-verdict
featured: false
draft: false
tags:
  - claude
  - ai-trends
  - model-comparison
description: 'Opus 5.5 發布夜的時間軸：重置卡與官方定價截圖、Reddit 對 Opus 5.5 與 GPT-6 Sol/Luna 的風向整理、Opus 該不該取代 Fable 的討論，以及 Kernion 談 Opus 為何不說人話。'
---

## 發布前後

9 月 21 日晚上，我發了一則貼文：我感覺 Opus 5 應該是被路由到新模型了。

為什麼會這樣說呢？因為他馬的我竟然看得懂他說的話了！

隔天晚上 11 點多，我覺得 Opus 5.5 應該是今晚發佈了。過不到二十分鐘：上了！

再過半小時，他們給了一張重置卡。

![Anthropic 官方公告截圖，中英對照：Opus 5.5 在預設設定下的典型工作負載成本比 Opus 5 少 40%，輸入與輸出價格為每百萬 token 4 美元與 20 美元，比 Opus 5 便宜 20%，快取讀取每百萬 token 0.2 美元，少 60%，輸出速度快 30% 以上](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-55-cost-speed.jpg)

![Anthropic 官方公告截圖：提高 Pro、Max、Team 方案的五小時用量上限，並提供訂閱用戶一次可自行保存、隨時使用的用量上限重置](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-55-rate-limit-reset.jpg)

![Anthropic 官方公告截圖：Sonnet 5.5 與 Haiku 5.5 將在未來幾週內推出](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-55-sonnet-haiku-coming.jpg)

同一個晚上兩邊都發新模型，這一次聲量誰贏？

## Reddit 風向

新模型大戰夜過去 12 小時，為大家整理一下模型界最嚴厲的老父親們：Reddit 網友群，現在的風向：

Claude Opus 5.5：
- 講話終於像樣了，跟 4.6 一樣可以溝通
- 用量消耗大幅下降（更省了）
- 長任務不容易跑偏
- 蛤那我還需要 Fable 嗎？
- 視覺生成有贏 Astra
- 安全護欄一樣亂殺
- 過幾天肯定會變笨

但總體來講是好評如潮，看來 A\ 是否極泰來（？

GPT 6 Sol / Luna：
- 降價就是正義
- Sol 6 根本就只是 Terra 換皮吧
- Luna 6 嚴重降智倒退
- Sol 6 會漏 Skill（5.6 不會）
- Opus 5.5 規劃 + Sol 6 執行最棒了
- 啊命名邏輯到底是啥？怎麼又再換

總體來講大家喜歡 GPT 降價，但是覺得不算是真正的迭代進步。

原文在這邊：<https://www.reddit.com/r/OpenAI/comments/1wnxg0n/luna_6_is_a_massive_downgrade_over_luna_56_misses/>

## Opus 5.5 還是 Fable？

Reddit 有一樣的討論（<https://www.reddit.com/r/ClaudeCode/s/SZnTlgAogt>），大家的共識是 Opus 不能取代 Fable。

有人同一個功能分別用 Opus 5.5 xhigh 和 Fable 5.1 high 實作，結果 Opus 做出「很可疑的架構決策」，Fable 一次就做好。這位的結論是範圍明確、上下文窄的任務交給 Opus，大型專案還是找 Fable。

有人說 Opus 過了大約 15 輪對話會忘記已經推翻的決定，Fable 在長對話裡不會這樣。

常見的分工是 Fable 當主控、Opus 當 subagent 執行。

Fable 最厲害的是架構能力跟洞見（unknown unknowns）。目前外網也有在講，Fable 做架構的能力還是比現在最新的 Opus 5.5 好，所以 Opus 是實作很強，但是整體架構的部分會給出很難理解的架構。

## 為什麼 4.6 之後的 Opus 常不說人話

在 A\ 負責做模型微調的 Jackson Kernion，回答網友為何 4.6 之後的 Opus 常常不說人話。

簡單來說就是：當模型訓練的重點變成理組至上，模型就會變得不善言辭（理工男症候群？），要在訓練獎勵中加上「人話更好」才可以。

![X 上 Shivam Kedia 提問為何 Opus 4.6 聽起來比較自然、之後的模型變差，Jackson Kernion 回覆說明原因](/blog/assets/posts/opus-55-launch-week-reddit-verdict/kernion-reply.jpg)

快笑死。

![五格素描肖像，依序是 Opus 4.6、4.7、4.8、Opus 5、Opus 5.5，前三格畫風正常，4.8 開始變得卡通化，Opus 5 是亂塗的崩壞小人，Opus 5.5 又回到正常寫實](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-portraits-meme.jpg)

<!--
新增非原文句子清單（忠實度自首）：
1. 「9 月 21 日晚上，我發了一則貼文：」— 類型：銜接（時間框架句，串接貼文 #38）
2. 「隔天晚上 11 點多，」— 類型：銜接（時間框架句，串接貼文 #55，依原始時間戳計算）
3. 「過不到二十分鐘，留言更新：」— 類型：銜接（時間框架句，串接貼文 #56，依時間戳 23:09→23:28 計算約 19 分鐘）
4. 「再過半小時，」— 類型：銜接（時間框架句，串接貼文 #58，依時間戳 23:28→23:56 計算約 28 分鐘，取整為半小時）
5. 「官方公告寫道，預設設定下 Opus 5.5 的典型工作負載成本比 Opus 5 少 40%，輸入／輸出價格是每百萬 token 4 美元與 20 美元，比 Opus 5 便宜 20%，快取讀取每百萬 token 0.2 美元，少 60%，輸出速度快 30% 以上。Pro、Max、Team 方案的五小時用量上限提高了，訂閱用戶還多一次可以自行保存、隨時使用的用量重置。Sonnet 5.5 與 Haiku 5.5 會在未來幾週推出。」— 類型：框架句（依三張官方截圖上的數字重述，銜接貼文 #58 的「重置卡」與截圖，未加入截圖以外的資訊）
6. 「隔天早上，」— 類型：銜接（時間框架句，串接貼文 #59）
7. 「原文在這邊。」— 類型：改寫（原貼文 #71 為「原文在這邊」，補上句號並改為完整句子承接前一則連結）
8. 原貼文 #70 結尾的「跟你的感想有一樣嗎？」已刪除 — 類型：刪除（Threads 互動句，部落格語境不成立）
-->

<!--
主對話回收：刪除第 5 條（官方數字重述段，與三張截圖重複、屬補述）；第 2、3 條改為「我覺得 Opus 5.5 應該是今晚發佈了。過不到二十分鐘：上了！」；第 6 條「隔天早上」刪除，#59 提問改為「這一次聲量誰贏？」；兩個 Reddit 連結改為內嵌句中。
-->
