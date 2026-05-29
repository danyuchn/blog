---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T02:30:00Z
title: "規則越加，Claude 越不聽話——派一隊 AI 重整設定，常態上下文省 36%"
slug: zh/harness-slim-down-36
featured: true
draft: false
tags:
  - claude-code
  - token-optimization
  - ai-workflow
  - harness
description: '半夜拿到 Opus 4.8、額度剛好重置，我做的第一件事是減肥我的 harness。一個 COO 學員把 1M 上下文用到 88% 的案例，讓我認真面對一件事：規則加越多，模型反而越不聽話。'
---

深夜拿到 Opus 4.8 新模型，Claude 的週額度也剛好重置。你做的第一件事是什麼？

我很慶幸我做的第一件事是：重整我的 harness。

## 一個把 1M 上下文用到 88% 的學員

會有這個念頭，是因為前一天跟一位 Claude Code 的深度用戶做訪談。這位學員是 COO，已經把 Claude Code 投入公司的日常營運。他花了二十分鐘詳盡解說他的工作環境：裝了很多 MCP、很多 Skill，還用 Obsidian 當知識庫，記下所有過往的決策重點跟錯誤教訓。

但實際運用上，他發現模型沒辦法很好地協同調用這麼多工具。

我聽他敘述時，心裡就在猜是上下文管理跟 harness 的問題，後來一一印證：

1. 我瞄到 App 右下角的小圓圈接近全滿，請他打開來看，發現他把 Opus 的 1M context 用到了 88%——而且往上翻，對話輪數其實沒幾輪。這非常不正常，通常到 60% 就該開始主動壓縮了。
2. 我馬上請他打 `/context`，果然發現系統內建的 memory files（`CLAUDE.md`、rules、skills、hooks、memory）佔比極少，幾乎沒在用。
3. 再瞄他的對話過程，原來是大量知識庫文檔的讀取佔滿了上下文。他強迫模型讀取所有他過去記下的「教訓」，但這些教訓大部分時候根本用不到；連長上下文任務也極少派 subagent 去做，全部塞在主 agent 的上下文裡。

在這種情況下，上下文窗口會快速腐爛，模型執行任務的連貫性、工具按需觸發的命中率都會迅速下降。這就是為什麼他覺得模型協同效率不好、又特別耗 token 的原因。

## 規則加越多，模型越不聽話

給他建議之餘，我自己的感觸是：上下文管理跟 harness 管理，對我們一般使用者來說真的太重要了。

很多人的直覺是反過來的——以為把所有規則、所有教訓都寫進去，模型就會更聽話。實際上恰恰相反。規則塞太多，常態注入把窗口撐爆，模型反而抓不到重點，連你最在意的那條都會漏掉。

所以當午夜 Opus 4.8 推出、額度意外重置，我做的第一件事就是減肥我的 harness。

## 我下的指令

我切到計畫模式，丟給它這段：

> 請你派儘可能多的 subagent，去調查我的 user-level、跟每個 project-level 的 `CLAUDE.md` / rules / hooks / memory / skills，找重複跟衝突，精簡常態注入，但以 harness 行為不變為最高原則。砍敘事脈絡（例子、人名、犯錯日期、範例），只留模型約束。

模型幫我規劃的流程是：

1. 派好幾個探索 agent，全局、專案各自徹底掃一遍，官方文檔也去查最佳實踐是什麼。（一定要好幾個 agent，才不會塞爆單一上下文導致調查失誤。）
2. 為每個 harness 文檔砍掉敘事脈絡、只留規則約束本身。拆成細粒度小步驟列成 to-do，避免跳步漏檔。
3. 精簡每個 Skill 的 description。
4. 把一些不需要 always 載入的文檔的 `@import` 引用語法改成純路徑，避免無端強制展開。
5. 重新派多個 subagent 審查每條規則：
   - 拿掉會不會犯錯？不會就拿掉。
   - 是否只有某些檔案或資料夾會用到？拿去下放，或做成 path-scope 規則檔。
   - 是否只跟某個特定工具或工作流相關？拿去跟 Skill 合併。
   - 是否重要到需要用 hook 擋住？是就轉成 hook。
6. 叫來 gemini-embedding 為 harness 中的每條約束上語意向量，直接做語意相似度比對，徹底消除重複注入、衝突注入。

以上每個步驟做完後，都會派一個不繼承上下文的 subagent 來獨立審查，過關才能進下一步。

## 結果

我的 harness 行數瘦身了 36%，常態注入的 token 省了一萬五千。

也因為這樣，我用到現在的 Opus 4.8 都沒有特別感覺耗 token，速度甚至比之前還快——因為我已經幫它留好一個相對乾淨的上下文窗口，注入給它的是不衝突、不重複的精煉規範。

完整流程跟我自己下 prompt、追加訊息的技巧都在這部影片裡：

<div class="video-embed">
  <iframe src="https://www.youtube.com/embed/OFAPR52Zwd4" title="如何管理自己的 Claude Code harness" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 給愛說「不如去用 Codex」的人

最後補幾句給喜歡路過補一句「搞那麼多有的沒的，不如來用 Codex」的人：

1. 我兩個都在常態使用，謝囉。
2. 不管用什麼模型，context 管理跟 harness 管理都是該學的事。不然幾百萬窗口終究會用盡，我也祝你活到徹底不需要考慮上下文窗口的那一天。
3. 你甚至可以用我的 harness 同步腳本，把 Codex 跟 Claude Code 兩邊定期做同步維護。

這個時代有人願意分享就不容易了。開卷有益，少點 troll，多點動手。
