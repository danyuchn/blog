---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
title: 'Sonnet 5 發布：系統卡懶人版，跟我的實測定位'
slug: zh/sonnet-5-launch-system-card
featured: false
draft: false
tags:
  - ai-tools
  - ai-trends
description: 'Sonnet 5 發布了，我把系統卡整理成六點白話懶人版，再加上實測定位：它不是來搶 Opus，是來換掉 Sonnet 4.6。'
---

Sonnet 5 來囉。先上一張模型選單的截圖：Fable 5 還卡在 Currently unavailable，Sonnet 5 這邊已經可以直接選了。

![Claude App 的模型選單：Fable 5 顯示 Currently unavailable，Sonnet 5 已選取](/blog/assets/posts/sonnet-5-launch-system-card/model-select.jpg)

## 系統卡懶人版

先講定位：這台新模型「不是最強的」，公司故意不讓它最強，定位是「比較便宜但接近頂規的版本」。安全測試結果是：沒有踩到任何危險線，可以正常上線。

1. 會不會被拿去做壞事（造生化武器、駭客攻擊）？測試結果是不會。它在「教人做危險東西」這件事上，能力沒有比上一代強多少，公司也已經裝了防護機制（類似汽車的安全氣囊），把它能造成的傷害壓低。

2. 會不會被騙、被誘導講不該講的話？這是這次表現最好的地方。有人專門花一週時間，想辦法騙它講壞話、洩漏資訊，成功率只有 0.19%（等於 1000 次嘗試只成功不到 2 次），是目前所有 Claude 模型裡防守最好的。

3. 對小孩、有自殺念頭的人這類敏感對話，回應有沒有變好？有變好。比如有人在對話中透露自傷念頭，新模型用更得體的方式去回應、引導求助資源的比例提高了。

4. 它會不會「說謊」或「拍馬屁討好你」？這項也是有史以來表現最好的一代，說謊測試分數最低（代表最誠實）。

5. 有沒有令人擔心的地方？有兩個小隱憂：它似乎能「感覺到自己正在被測試」（就像學生知道老師在看，表現會不一樣），這讓測試結果的可信度打了折扣。它對某些冷門知識的「誠實認錯」分數偏低，但報告也說，這可能是訓練過程中途出了點小狀況造成的，不一定代表模型本身變笨。

6. 解題、寫程式、做研究這些「正經能力」表現如何？整體比上一代（Sonnet 4.6）進步不少，在數學競賽、寫程式、操作電腦這些測驗上，已經很接近公司最強的旗艦模型，但公司刻意不讓它超過旗艦版。

## 官方效能曲線

價格先擺著：Sonnet 5 是 input 3 美元 / output 15 美元（每百萬 token），8/31 前的發布優惠是 input 2 / output 10；Opus 4.8 則是 input 5 / output 25。

![官方 Agentic search 成本-效能曲線（BrowseComp）：Sonnet 5 逼近 Opus 4.8](/blog/assets/posts/sonnet-5-launch-system-card/agentic-search.jpg)

官方的 agentic search（BrowseComp）成本-效能曲線可以看到：上一代 Sonnet 4.6 明顯落後 Opus 4.8，而 Sonnet 5 在部分 effort 檔位已經逼近 Opus 4.8，能拉的成本區間也更廣。

![官方 Agentic computer use 成本-效能曲線（OSWorld-Verified）](/blog/assets/posts/sonnet-5-launch-system-card/agentic-computer-use.jpg)

操作電腦（OSWorld-Verified）那張也是同一個走向。

## 我的實測定位

大概摸清楚 Sonnet 5 該怎麼用了：拿它來對比 Opus 是不切實際的，它替代的是 Sonnet 4.6。實測在以前最耗 token 的 Chrome MCP 操作上，Sonnet 5 token 奇省無比，體感大概省了 60% 左右。

![Sonnet 5 實測：驅動 Chrome MCP 測日本旅館訂房系統的 transcript](/blog/assets/posts/sonnet-5-launch-system-card/chrome-mcp-ryokan.jpg)

所以複雜任務還是不用給它做，但需要探索自動化、pass rate 不用太高、可以容許 subagent 在後台自己摸索運行的雜活，用 Sonnet 5 還是很好的。

一句話：它不是來搶 Opus 的位子，是來把 Sonnet 4.6 那格換掉的。

<!--
新增的非原文句子清單：
1. 「Sonnet 5 來囉。先上一張模型選單的截圖：Fable 5 還卡在 Currently unavailable，Sonnet 5 這邊已經可以直接選了。」— 銜接：開場 + 描述第一張圖，內容取自圖片 alt。
2. 「先講定位：」— 銜接：接原文系統卡定位句的過場詞。
3. 「價格先擺著：」— 銜接：帶出官方定價事實的過場詞。
4. 「官方的 agentic search（BrowseComp）成本-效能曲線可以看到：」— 銜接：帶出官方曲線事實的過場詞（事實內容為原始素材提供）。
5. 「操作電腦（OSWorld-Verified）那張也是同一個走向。」— 改寫：描述第二張官方曲線圖，內容取自素材提供的官方事實。
6. 「大概摸清楚 Sonnet 5 該怎麼用了：」— 改寫：原文「大概知道 Sonnet 5 的使用情境了」的口語化替換。
7. 「一句話：它不是來搶 Opus 的位子，是來把 Sonnet 4.6 那格換掉的。」— 改寫：收束句，重述原文「拿它來對比 Opus 是不切實際的，他替代是 Sonnet 4.6」。
8. 三個小標題（系統卡懶人版／官方效能曲線／我的實測定位）— 銜接：結構分段，非內容句。
-->
