---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:30:00Z
title: "Claude Code 訂閱怎麼選：從 Pro 到 Max 的真實落差"
slug: zh/claude-code-subscription-guide
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: Pro 的額度到底有多少？Max 值不值？Cowork 為什麼很燒 token？週額度的「雙倍」到底是哪個雙倍？這些問題我都被問過不只一次，用這篇把幾個月來的觀察整理清楚。
---

Claude Code 對我來說不是「偶爾用的工具」，是每天開機就在跑的工作環境。所以 Rate Limit 到了之後，那種落寞感是真實的——比網路斷線還難受，因為工作真的就停在那裡了。

這種依賴程度讓我非常在意額度。以下是幾個月下來摸清楚的事。

## Pro 的額度其實很少

很多人買 Pro 以為就夠用了。我的觀察是：如果你只是偶爾問問題，Pro 完全夠。但如果你開始跑 agent、讓 Claude 自主完成多步驟工作，Pro 的週額度很快就見底。

「雙倍用量」期間（Anthropic 曾推出活動），很多人以為週額度真的是 2 倍。實際上社群實測的結論是：只有前 5 小時是 4 倍量，其餘時間才是 2 倍。跟很多人的預期有落差。

我自己在摸清這件事之前，兩天 extra usage 就燒了 20 USD，補購又燒了 20，最後直接升級了。

## Max 到底值不值

Pro 到 Max，差距不只是額度量，是用起來的「質感」完全不同。Pro 下你會一直在算還剩多少，Max 下幾乎不需要想這件事。

我自己是先開 20x，覺得用量跟不上（AI 跑的時候我也在同時思考怎麼驗收、怎麼給下一個指令，並不是真的能 20x），後來退回 5x。大部分用 Sonnet，小部分用 Opus 做需要更深推理的任務。

100 美的 Max，平攤到每個工作天，對我來說是合理的工具成本。

## Cowork 很燒 token，別用它替代 CLI

Cowork 是 Claude 的沙盒介面版本。它的 token 消耗比直接用 CLI 快很多，社群有人實測，差距相當明顯。原因有幾層：介面本身的 wrapper overhead、預設的 safety 注入、以及 context 管理的方式不同。

如果你在用 Cowork 然後覺得 Pro 根本不夠燒，切換到 CLI 之後會發現同樣的任務省很多。Cowork 的定位應該是入門體驗，不是正式工作環境。

## 訂閱 cache reads 不計費

這個很多人不知道：**只有 API 計費才會對 cache reads 計費，訂閱方案的 cache reads 免費。**

所以如果你有一份很長的 system prompt 或 CLAUDE.md，你的訂閱方案不會因為它被快取讀取而扣費。API 用戶就不一樣了——每次 cache hit 還是有小額的 read 費用。

## 幾個實用工具

**ccusage**：`!npx ccusage@latest monthly` 可以看詳細的 token 用量分析。如果你想知道自己的 token 花在哪，這個必裝。

**Rate Limit Statusline**：Claude Code 2.1.80 版本後，可以把 rate limit 剩餘顯示在 statusline（終端機底部的狀態列）。不用一直打 `/usage` 查了，用量一目瞭然。

有了這兩個工具，你對自己的用量節奏會有清楚很多的感知。當你知道距離下次重置還有多少時間、還剩多少額度，要不要踩油門心裡就有數。

## 一個管理心態

最後是比較偏哲學的一個想法：訂閱額度是有限的資源，但它的稀缺感不應該影響你的工作判斷。

我見過有人因為怕超量，把本來應該給 Claude 做的事情手動做，結果省了 token 卻浪費了自己的時間。額度買來是讓你節省時間的，不是讓你計算哪些任務「值不值得」消耗的。

剩 5 分鐘就重置但還有 10% 沒用完？趕快燒完。重置前你的額度是你的，不燒就浪費了。
