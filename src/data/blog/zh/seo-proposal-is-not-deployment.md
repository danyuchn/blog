---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "提案不等於部署：一個 Quick Win 掛了五週的根因"
slug: zh/seo-proposal-is-not-deployment
featured: false
draft: false
tags:
  - ai-workflow
  - case-study
  - seo
description: '我有一個 SEO 週報自動跑了五週，某一頁的 Quick Win 一直掛著沒效。根因不是優化方向錯，而是那份漂亮的優化提案從頭到尾從來沒被真正部署上線。'
---

我有一套 SEO 週報流程，每週自動跑：抓 Google Search Console 的資料、找出該動的頁面、產出該頁的 title／meta 優化提案，列成一張 Quick Win 清單。流程順得很，每週都有新的建議冒出來。

問題是，其中一頁的 Quick Win 連續五週掛在清單上，一直沒效。

## 根因：提案從來沒被推上線

我回頭去查這一頁——站內編號 139——的根因。W20 那一週，週報針對 139 產出了 title／meta 的優化提案。提案內容沒問題，方向也對。但我去抓這頁的 live `yoast_head_json`，發現它還是舊版的。

也就是說，那份「提案」從頭到尾從來沒有被實際推送到 Yoast。它停在草案階段。每一週的週報都重新看到這頁表現不好，於是又把它列進 Quick Win，於是它就這樣連續掛了五週。

提案 ≠ 部署。這是整件事的核心。模型每週都很勤勞地產出一份漂亮的優化建議，但沒有任何一個環節去驗證這份建議到底有沒有真的上線。閉環缺了最後一塊：以 live 驗證收尾。沒有 live 驗證，QW 清單就會無止盡地重複建議同一件根本沒做的事。

## 同一週還踩到的兩個相關坑

把流程攤開來看，這五週裡其實還藏著別的問題，全都跟「提案到底有沒有真正生效」這件事是同一個家族。

**第一個：內鏈 anchor 蓋不過 on-page 的 title exact match。** W20 我為了處理一組關鍵字的自我競爭（cannibalization），把編號 4047 和 249 的 anchor 指向 4614，想把 4614 拱成主頁。結果 Google 還是把最多曝光留給 4047，因為 4047 的 title 開頭就是那串 exact match 的「GMAT 考試潛規則攻略」。光靠內鏈 anchor 沒用——要解 cannibalization，得先把競爭頁的 on-page 信號 de-opt 掉，不能只在外圍動內鏈。

**第二個：tracking 腳本的窗口陷阱。** 我要追 5/15 那批 deploy 的成效，腳本是用 DEPLOY_DATE 往前後各推一段算 before／after 窗口。如果我偷懶沿用前一批 5/22 的設定，before 窗口就會把 5/15 之後的資料也包進去，整個對比就被污染了。要拿到乾淨的窗口，DEPLOY_DATE 必須老老實實設成 2026-05-15。

## 比較窗口還有一個容易忽略的細節

順著 tracking 這條線再講一個：GSC 的 before／after 比較，天數必須對齊。

deploy 之後我通常往後推 14 天看成效，但 GSC 本身有大約 3 天的資料延遲，所以 after 窗口實際上只拿得到 11 天。這時候要注意：曝光數（imp）和點擊數（clk）是絕對值，會直接受窗口長度影響——後窗少 3 天，數字本來就會偏低。而排名（pos）和點擊率（CTR）是比率，不受窗口長度影響。所以做對比的時候，imp／clk 要把 before 窗口也收斂成同樣天數才公平，pos／CTR 則可以直接比。

這幾個坑串起來就是同一句話：提案 ≠ 部署。我那一頁掛了五週，不是哪一步分析錯了，而是沒有任何一步回頭確認結果。QW 的閉環，必須以 live 驗證收尾。
