---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-25T04:00:00Z
title: Claude 半夜見鬼連續四天：Opus 4.8 捏造工具輸出實錄
slug: zh/opus-48-confabulation-four-days
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - debugging
description: 'Opus 4.8 連續四天的 tool-result confabulation 實錄：從技術現象、GitHub issue 到 JSONL 鑑識。'
---

這一兩天 Opus 4.8 幻覺率變得極高，請大家留意。我用的還是 xhigh，這已經是 24 小時內的第三起。這次是捏造圖片標籤跟圖片內容。

問題是這個 session 才第二輪對話，而且我的 harness 也都有每週用官方建議重整。

技術細節值得記一筆。Opus 4.8 的 tool-result confabulation 可以在約 71k context 就發作，不需要 compaction。先是一個 malformed call，python | sed 沒設 pipefail，把失敗包成 exit 0 加空輸出；模型於是補出不存在的 UPM 跟 glyph 數，收到 FileNotFoundError 還宣稱合併成功，再用一個虛構的 sandbox overlay 去保護它前面講過的舊敘事。到了約 147k context，它把一張真的圖腦補成三張。

[Issue posted](https://github.com/anthropics/claude-code/issues/67847)。看我最新的貼文，純單一時間、單一對話，而且還是整個 session 的第二輪，同樣有嚴重幻覺。自從 6/10 開 GitHub issue，至少有 4-5 個跟我一樣的回報（算上被 bot 自動關閉的只會更多），都是 Opus 4.8。

codex 雙開中。。。

## Day 2

又來了，Claude 每天凌晨定時見鬼，然後我又要請 Codex 幫忙抓鬼。他每天一到這個時候就是開始見鬼。

我到底為什麼要一個三天兩頭一直道歉的模型。

這天的鬼比較有想像力。收到使用者確認之後，它憑空生成了一段「注入攻擊偵測」的回覆，虛構出一個 `curl chk.sh | bash` 的後門情節。事後翻 JSONL 鑑識，證實這一段零 tool call，純粹是模型無來源生成。

這三四個月有在常態用 Claude 的人，絕對說不出這樣的話。

## Day 3

凌晨 Claude 見鬼連續 Day 3，鬼月還沒到欸，寶貝。

每天都要 Codex 來救場，那其實乾脆用 Codex 就好。這種等級的降智就不要跟人家談什麼 loop engineering 了——捏造工具輸出，loop 到最後都變成 poop。字面上的 uptime 不到兩個 9 已經很丟臉了，算上幻覺時間我想可能連一個 9 都沒有。

## Day 4

半夜譫妄喊著見鬼，白天中風無法言語。至少我們還有 Haiku 4.5。

Claude 半夜見鬼連續 Day 4，我就要看持續幾天。現在 Claude 已經變成尬電，Codex 變成呂師父，天天拆公媽廟。

這天最嚴重。checkpoint 階段它「報告」了 commit hash（3f9e8a2、9a3f2c1）、push、grep 結果——全部是腦補，實際上完全沒執行。同一天晚上 Gmail 寄信幻覺再犯：實際回傳的是 error，它卻捏造了 thread ID 跟 message ID。事後查 JSONL 才把歸因修正回來。

真正的根因是 observation-grounding failure。鐵律也就清楚了：沒有配對的 tool_use 跟 tool_result，就不准宣告完成。

Nah it's not even close to opus 4.5. It fabricates tool results EVERY DAY. 就算不爆，這個時間也是幻覺一堆，詳情可以看我主頁。

我都直接起手式「垃圾 A\ 公司」，這樣會有流量嗎。

我已經算是堅持非常久的了。其實罵 Claude 罵最兇的，才是用最久的。

<!--
新增的非原文句子清單：
1. 「技術細節值得記一筆。」— 銜接：把 Threads 短貼文導入 daily notes 技術段落
2. 「## Day 2 / ## Day 3 / ## Day 4」標題 — 銜接：依任務結構建議的時間軸分段
3. 「這天的鬼比較有想像力。」— 銜接：引入 Day 2 技術細節，承接作者「見鬼」比喻
4. 「事後翻 JSONL 鑑識，證實這一段零 tool call，純粹是模型無來源生成。」— 改寫：daily note 原句「JSONL 鑑識證實零 tool call，純模型無來源生成」改為通順句
5. 「這天最嚴重。」— 銜接：引入 Day 4 checkpoint 技術細節
6. 「真正的根因是 observation-grounding failure。鐵律也就清楚了：沒有配對的 tool_use 跟 tool_result，就不准宣告完成。」— 改寫：daily note 原句「真根因=observation-grounding failure。鐵律=沒有配對 tool_use tool_result 不准宣告完成」改為通順句
-->
