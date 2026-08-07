---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: 我每天在用的 Skill 跟 Hook，開源了
slug: zh/harness-starter-kit-release
featured: false
draft: false
tags:
  - harness
  - skills
  - open-source
description: '把我每天都在用、不需要技術力、純邏輯導向的幾個 Claude Code Skill 跟 Hook 開源出來，最適合跟我一樣沒有編程背景的知識工作者。'
---

跟網路上的 Claude／Codex 大神相比，我還差得很遠，因為我技術力不高。

但是我有幾個相信你一定會喜歡的 Skill 跟 Hook，因為這些我每天都在用，不需要技術力，純邏輯導向，最適合跟我一樣無編程背景的知識工作者：

[harness-starter-kit](https://github.com/agentcrew-academy/harness-starter-kit)

你只需要把連結貼進 Agent，他就能帶你導覽，幫你裝好。

裡面的 hook 有兩個。第一個是 claim-guard hook：起因是我發現 Claude 喜歡說謊，沒驗證說驗了，沒查說查不到，這個 hook 只要偵測到 agent 有這樣聲稱，就會去檢查 tool call 是否有用到驗證／搜尋指令，沒有就直接提醒 AI 拿出證據，拿不出就回去老實做。

第二個是 no-emoji hook。我個人很討厭 emoji 在文件裡，這個 hook 會掃一遍 AI 寫入內容有沒有 emoji，有的話擋下來改。有一次它連我要編輯 hook 腳本自己的那次寫入都擋下來了。

Skill 的部分有五個：

1. `/explain`：Claude 常常不講人話，逼他把我當外行人高中生，不要用縮寫跟術語，跟我解釋清楚。
2. `/first-principles`：當我的思考邏輯卡關時，用馬斯克的「第一性原理」幫我質疑合理性，找到事情的本質再重新推理。每次整個被搞亂的時候我就會用它，往往都可以看破本質、刪去不必要的枝微末節。
3. `/checkpoint`：收工用，紀錄知識庫日誌、git commit push 以及檢查格式問題。
4. `/neat-freak`：審查是否有跨檔資訊不同步，避免未來 AI 吃到的上下文衝突。
5. `/polite`：教 AI 怎麼有禮貌地說話，最適合寫對外信。

其中 2、4 是魔改開源的，有附上 LICENSE。

下圖是使用範例：

![Claude Code 輸入框截圖，一句話裡串起五個 skill：請派 fable subagent 用 /first-principles 思考目前計劃的合理性，思考完後用 /explain 解釋，審核通過後 /checkpoint 紀錄進度並用 /neat-freak 審查跨檔內容，最後用 /polite 寫一封訊息通知甲方](/blog/assets/posts/harness-starter-kit-release/1-skills-demo.jpg)

<!--
新增非原文句子清單（忠實度自首）：
1. 「裡面的 hook 有兩個。第一個是 claim-guard hook：」 — 類型：銜接（原文為「裡面有：1. claim-guard hook：」，改成散文銜接）
2. 「第二個是 no-emoji hook。」 — 類型：銜接（同上，取代原文編號「2.」）
3. 「Skill 的部分有五個：」 — 類型：銜接（原貼文第一則與第二則之間的接縫，原文無此句）
4. 「其中 2、4 是魔改開源的，有附上 LICENSE。」 — 類型：改寫（原文為括號「（2, 4是魔改開源的，有附上LICENSE）」，去括號化為正文句）
註：原貼文第一則的 hook 清單在第 2 點後被截斷、第 3 點沒說完，未替作者補寫。第三則（YouTube／部落格／Threads 的 CTA）依 article-spec 改寫原則第 4 條刪除。
-->
