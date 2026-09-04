---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-11T04:00:00Z
modDatetime: 2026-09-04T04:00:00Z
title: 派更多 subagent 不會讓你更快
slug: zh/more-agents-wont-make-you-faster
featured: false
draft: false
tags:
  - ai-workflow
  - claude-code
  - opinion
description: '從想派 13 個 subagent 代聊、一個人操控 1000 個，到面對面互審代碼的荒謬幻想——真正的瓶頸是人類這個 main agent，解法是先去重去衝突再派工。'
---

## 好想派 13 個 subagent 代聊

好想派出 13 個 subagent 代聊，節省人類這個 main agent 的 context window。

這句話是玩笑，但它其實把問題講完了。派 subagent 出去的當下，感覺像是把工作量分出去了；可是那 13 條線最後都要回到同一個地方收斂，而那個地方是我。

## 一個人操控 1000 個

一個人操控 1000 個 subagent；大家都來寫 HTML 當文檔取代 markdown 吧。

這是同一個荒謬往上乘。13 個已經收不完了，1000 個只是把「收不完」放大到看得見的規模。

## 面對面不說話

我需要一個社交 agentic AI 俱樂部：面對面不說話，用我手中的 Claude Code 跟對面的 Codex 吵架，互相審查代碼撕逼。門票要收。

這是第三種變形。前兩個是把 agent 往外派，這個是把人聚起來，然後讓 agent 在人與人之間互相攻擊。兩個人坐在一起，誰都不開口，桌上兩台機器吵得不可開交。門票我還是想收。

## 瓶頸不在模型

這三件事其實是同一件事的三種畫法。派 13 個、派 1000 個、把兩邊的 agent 放在同一張桌子上，共同的假設都是「agent 多一點就快一點」。但增加的每一個 agent，都會生出更多需要我裁決的東西。模型可以無限開下去，我的 context window 不行，我在單位時間內能做的判斷更不行。

這跟額度燒掉是不一樣的問題。額度那次是 subagent 遞迴繁殖，[有些 subagent 都當阿公了](/blog/posts/zh/claude-code-quota-incident-log)，燒的是錢。這次燒的是我自己。

## 多代理帝國，你真的用得起嗎

最近在 Reddit 上看到的一則很有趣的討論。Anthropic 工程師 Daisy 秀操作，被網友批「不食人間煙火，何不食 token」。

![圖卡一：多代理帝國，你真的用得起嗎？一位 Anthropic 工程師說，她只用 30-50 次 prompts 就能讓數十個 agents 跨 8-10 個專案自主工作](/blog/assets/posts/more-agents-wont-make-you-faster/card-1-multiagent.jpg)

她的說法是：只用 30 到 50 次 prompts，就能讓數十個 agents 跨 8 到 10 個專案自主工作。真正的問題不是能不能啟動，而是能不能信任、追蹤、負擔。

![圖卡二：架構圖，兩個 lead agents 管理整座代理組織，分成 lead、project lead、IC agent 三層](/blog/assets/posts/more-agents-wont-make-you-faster/card-2-multiagent.jpg)

架構是三層。第一層兩個 lead agents 互相監督，任一失敗就由另一個重啟。第二層 8 到 10 個 project leads，各自掌握一個專案的目標與進度。第三層每案 5 到 10 個 IC agents 執行具體任務，可自主工作兩三天。agents 之間用 SendMessage 直接溝通。

![圖卡三：展示得出來，不等於你能重現。內部展示與一般使用者在額度、成本、重工上的三點落差對照](/blog/assets/posts/more-agents-wont-make-you-faster/card-3-multiagent.jpg)

最大的落差在這裡：展示得出來，不等於你能重現。內部展示是數十個 agents 並行、可長時間自主執行、失敗後彼此恢復；一般使用者是受訂閱額度限制、並行越多 token 消耗越快、失敗重工會再次付費。留言區的主流質疑就是缺少公開成本與可複製證據。

![圖卡四：真正難題不是啟動更多 agents，而是避免一起犯錯，列出狀態、驗證、恢復、成本四層](/blog/assets/posts/more-agents-wont-make-you-faster/card-4-multiagent.jpg)

真正的難題不是啟動更多 agents，而是避免一起犯錯。狀態：誰做過什麼、現在進度在哪。驗證：誰能獨立找出其他 agent 的錯誤。恢復：失敗後如何重啟又不重複錯誤。成本：token、重工與人工審查是否划算。沒有這四層，並行只會放大混亂。

![圖卡五：可複製的縮小版，先把治理做小再把 agents 做多，列出五個步驟](/blog/assets/posts/more-agents-wont-make-you-faster/card-5-multiagent.jpg)

可複製的縮小版是先把治理做小，再把 agents 做多。主線只管目標與驗收，每個 agent 只負責一個明確範圍，固定寫 action log 與 handoff，關鍵事實回查 live source，失敗必須 loudly fail。縮小並行範圍，才能看見成本、錯誤率與真實產能。

![圖卡六：結論，agents 越多不代表產能越高，先問狀態是否能追溯、錯誤是否獨立驗證、失敗是否會大聲回報](/blog/assets/posts/more-agents-wont-make-you-faster/card-6-multiagent.jpg)

所以結論還是那句：agents 越多，不代表產能越高。先問三件事——狀態是否能追溯、錯誤是否獨立驗證、失敗是否會大聲回報。能回答，才有資格擴張；不能回答，只是在放大 token 成本與錯誤速度。真正值得複製的，不是數十個 agents，而是一條可信任的工作流。

## 先去重去衝突，再派 agent team

真正有用的順序是這樣的：先提供材料，切分段落使用語意向量比對，來做去重跟衝突化解（我來裁決），然後再根據去重去衝突後的材料派 agent team（可以互相溝通的 agent）討論結構跟順序，最後再由我來定奪做微調。

重點在前半段。去重跟衝突化解發生在派工之前，這一步把要裁決的量壓下去了，後面的 agent team 才有意義。順序反過來——先派一堆 agent，再回頭處理它們各自帶回來的重複與矛盾——就是前面那三種幻想的下場。

裁決權還是在我手上，兩次：中間一次，最後一次。這件事沒有辦法外包。

## Fable 5.1 一分鐘燒光 5 小時額度

一大早看到這篇文章，忍不住笑出來。Fable 5.1 才剛出，就有人用 Ultracode，結果一次被派出大概 300 個 subagent，而且全部都繼承主 agent 的模型種類（也就是全部都是 Fable）。5 小時額度一分鐘被幹光，週額度馬上被幹到剩 43%。

如果你也有這困擾，原討論串裡大家都分享了解法，具體來說就是改 config、加 hook、改 frontmatter。<https://www.reddit.com/r/ClaudeAI/comments/1w52pbu/gone_in_60_seconds/>

<!--
新增非原文句子清單（忠實度自首）：
1. 「這句話是玩笑，但它其實把問題講完了。」— 類型：銜接
2. 「派 subagent 出去的當下，感覺像是把工作量分出去了；可是那 13 條線最後都要回到同一個地方收斂，而那個地方是我。」— 類型：改寫（把原句「節省人類這個 main agent 的 context window」的反諷展開，未加入原文沒有的論點）
3. 「這是同一個荒謬往上乘。13 個已經收不完了，1000 個只是把『收不完』放大到看得見的規模。」— 類型：銜接
4. （已刪除）原稿曾對「1000 個 subagent」那則的後半句（改用 HTML 寫文檔）加了一句心態解讀，屬 AI 代作者延伸，主對話回收時已移除。
5. 「這是第三種變形。前兩個是把 agent 往外派，這個是把人聚起來，然後讓 agent 在人與人之間互相攻擊。」— 類型：框架句
6. 「兩個人坐在一起，誰都不開口，桌上兩台機器吵得不可開交。」— 類型：改寫（原句「面對面不說話⋯互相審查代碼撕逼」的畫面重述）
7. 「這三件事其實是同一件事的三種畫法。派 13 個、派 1000 個、把兩邊的 agent 放在同一張桌子上，共同的假設都是『agent 多一點就快一點』。」— 類型：框架句
8. 「但增加的每一個 agent，都會生出更多需要我裁決的東西。模型可以無限開下去，我的 context window 不行，我在單位時間內能做的判斷更不行。」— 類型：框架句（核心論點，延伸自原句自陳的 main agent context window）
9. 「這跟額度燒掉是不一樣的問題。額度那次是 subagent 遞迴繁殖，有些 subagent 都當阿公了，燒的是錢。這次燒的是我自己。」— 類型：銜接（站內既有文章交叉引用）
10. 「真正有用的順序是這樣的」— 類型：銜接
11. 「重點在前半段。去重跟衝突化解發生在派工之前，這一步把要裁決的量壓下去了，後面的 agent team 才有意義。」— 類型：改寫（原句流程順序的重述與強調）
12. 「順序反過來——先派一堆 agent，再回頭處理它們各自帶回來的重複與矛盾——就是前面那三種幻想的下場。」— 類型：框架句
13. 「裁決權還是在我手上，兩次：中間一次，最後一次。這件事沒有辦法外包。」— 類型：改寫（原句「我來裁決」「由我來定奪做微調」兩處的重述收束）
其餘句子（13 個 subagent 代聊、1000 個 subagent 與 HTML 取代 markdown、社交 agentic AI 俱樂部全句含門票要收、去重去衝突派 agent team 全流程句）皆逐字來自原碎念條目。
-->

<!--
2026-08-28 W36 主對話補記：本週 Threads 素材（08-23 18:08 Reddit Daisy 討論貼＋作者自製 6 張品牌圖卡）論點與本文同源，故併入本文而非另開新文。新增非原文句子：「她的說法是：」「架構是三層。」「最大的落差在這裡：」「所以結論還是那句：」四處銜接，其餘均逐字取自貼文與圖卡文字。
-->

<!--
2026-09-04 週例行補記：新增「Fable 5.1 一分鐘燒光 5 小時額度」一節，素材取自 09-03 Threads 貼文。新增句：小標（框架句）。其餘逐句改寫自原貼文，未新增原文沒有的論點或結論。
-->
