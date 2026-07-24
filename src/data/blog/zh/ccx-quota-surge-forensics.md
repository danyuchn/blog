---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: 有些 subagent 都當阿公了
slug: zh/ccx-quota-surge-forensics
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - debugging
description: '一次 CCX 沒設好護欄的額度事故：subagent 遞迴繁殖，一個 session 半小時燒掉 90%，事後鑑識與修法全記錄。'
---

昨天我就是沒有設置這個，結果 subagent 瘋狂繁殖。有些 subagent 都當阿公了。

我用的是 CCX，我自己包的多 agent 編排別名。那個 session 我沒把巢狀 subagent 關掉、也沒限制 subagent 的總個數，於是它一路往下衍生，一代生一代，好幾代疊上去。結果一個 session 半小時內燒掉了 90% 的額度。

事後我把原因鑑識出來：是遞迴 fan-out、Agent Teams、全員都掛最貴的 Sol、長 context，再加上一個舊版的 proxy，全部疊乘在一起。單獨一項可能都還好，湊在一起就爆了。

修法是把 CLIProxyAPI 從 7.2.73 升到 7.2.91，然後幫 `ccx()` 補上幾道護欄：subagent 總數上限、並行上限、背景執行、重試次數，還有壓縮。實測跑了一輪，2 個 Terra subagent、深度 1、零巢狀，正常結束，沒再爆量。`cc` 跟 `cdx` 沒動。

要小心的就是這個。除了壓縮窗口要自己設置之外，記得要關掉 nested subagent、限制總 subagent 的個數。

<!--
新增非原文句子清單（忠實度自首）：
1. 「我用的是 CCX，我自己包的多 agent 編排別名。」— 類型：框架句（向讀者交代 CCX 是什麼，素材 A/B 未明講）
2. 「那個 session 我沒把巢狀 subagent 關掉、也沒限制 subagent 的總個數，於是它一路往下衍生，一代生一代，好幾代疊上去。」— 類型：改寫（把素材 B「有些 subagent 都當阿公了」的畫面感展開為機制描述，未加入原文沒有的論點）
3. 「單獨一項可能都還好，湊在一起就爆了。」— 類型：銜接（承接素材 A「疊乘」的因果，最小銜接）
4. 「單獨一項可能都還好」屬輕度推論，若嚴格則視為銜接句。
5. 「實測跑了一輪」「正常結束，沒再爆量」— 類型：改寫（素材 A「實測…並正常結束」的口語化重述）
其餘句子（燒掉 90%、當阿公、遞迴 fan-out/Agent Teams/Sol/長 context/舊 proxy、CLIProxyAPI 版本號、ccx 五道護欄、2 個 Terra subagent 深度 1 零巢狀、cc/cdx 未改、關 nested subagent 限總數、壓縮窗口自己設置）皆直接來自素材 A/B。
-->
