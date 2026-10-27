---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-26T04:00:00Z
title: GPT-6.1 Terra 實測：又快又省，但看字形和對話脈絡還是交給 Sonnet
slug: zh/gpt-6-1-terra-review
featured: false
draft: true
tags:
  - model-comparison
  - codex
  - ai-tools
description: 'OpenAI 剛發布 GPT-6.1 Terra，我用審查、修補、看畫面三組題目實測，對照 Sol、Astra 和 Claude 三款，整理哪些工作可以交給它。'
---

OpenAI 在 2026-10-26 發布了 GPT-6.1 Terra，主打快速高效的電腦操作與視覺推理，而且標準 API 定價直接比 GPT-5.6 Terra 和 GPT-6.1 Sol 低 50%，輸入每百萬 token 只要 $1、輸出 $5。看到這個定價跟定位，我唯一想確認的問題只有一個：在我自己的日常派工裡，Terra 到底值不值得用、該用在哪？我把手上常跑的程式修補、對抗式審查、看畫面操作瀏覽器跟長任務難題拿出來實測了一輪，先講結論——Terra 在 low effort 下就可以直接接手我原本派給 Sol low（照規格修補程式）和 Astra low（對抗式審查）的工作，在這些題目上拿到一樣的滿分，速度快 1.5 到 2 倍，每次消耗的 5 小時額度只有 Astra 的四分之一到五分之一；但如果是看畫面抓簡繁錯字、判斷對話脈絡，或是做整批替換與逐字稿歸因，它還是會漏，這些工作不能直接放手交給它。

## 官方怎麼介紹 Terra

[OpenAI 官網公告頁](https://openai.com/index/introducing-gpt-6-1-terra/)擋爬蟲，我抓不到，所以以下用 [Artificial Analysis 的整理](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)和官網 RSS 摘要。

根據官網 RSS 摘要（經我的每日資料整理轉述，摘要在這裡被截斷，原文沒讀到），GPT-6.1 Terra 在 2026-10-26 發布，官方給它的定位是快速高效的電腦操作與視覺推理模型，標準 API 定價比上一代 GPT-5.6 Terra 和同代的 GPT-6.1 Sol 都低 50%（[官網公告頁](https://openai.com/index/introducing-gpt-6-1-terra/)）。

具體的 API 價格，每百萬 token 輸入是 $1、輸出 $5、快取輸入 $0.05、寫入快取 $1.25；對比上一代 GPT-5.6 Terra 的輸入 $2、輸出 $12、快取輸入 $0.20，輸入價砍一半、輸出從 $12 降到 $5（[Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)）。[Artificial Analysis 的評測文章](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)直接給了一句評價，說它「比上一代 Terra 更聰明，成本不到三分之一」，而且在 low 與 medium effort 兩個檔位落在智慧與成本的 Pareto 前沿，其他 effort 檔位則落在前沿後面。

如果看各項基準測試的分數（[Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)）：
- 在 max effort 下，Terra 的 Intelligence Index 比 GPT-6.1 Sol 低 4 分；Coding Agent Index v2.0 拿到 48 分，比 Sol 的 54 分低 6 分。
- 跟自家的輕量或前代模型比，Terra 的 Intelligence Index 比 GPT-6 Luna 高 10 分，Coding Agent Index 高 17 分（48 對 31）；跟上一代 GPT-5.6 Terra 在 max effort 下相比，Intelligence Index 高了 6 分，而且每個任務成本從 $1.40 降到 $0.40。
- 在 AA-Omniscience 測試裡，Terra 的幻覺率是 38%，上一代 Terra 是 88%，但準確率只升了 2 分。
- 在 Terminal-Bench 4.0 上，Terra 進步約 20 分，[Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) 說它「已追上 max effort 的 GPT-6.1 Sol」。

Artificial Analysis 的文章沒有拿 Terra 跟 GPT-6 Astra 或 Claude 比。Astra 的對比來自 [OpenRouter 的上架貼文](https://x.com/OpenRouter/status/2114791584755839168)的摘要轉述：Terra 在 Agents' Last Exam 上和 GPT-6 Astra 得分相當，而且每 token 價格大約只有 Astra 的十分之一。

## 我怎麼測、測到什麼

官方跟第三方數字看完，還是得看放進自己的工作流裡表現怎樣。為了測 Terra 值不值得換上去，我用全合成資料設計了四組仿真實場景的測試：對抗式審查、真實程式修補回放、看畫面與操作瀏覽器、還有從歷史錯誤挖出來的難題組。

樣本不大：每題 Terra 跑 1 到 3 次，Haiku、Sonnet、Opus 多半 1 到 2 次，看畫面的結論主要靠兩題各 2 到 4 次。Codex 內建的 computer_use 和 100 行以上的大型修補我沒測。

第一部分是審查與程式修補。這部分的結論很明確：Terra low 可以直接接手 Sol low 與 Astra low 的工作，而且把 Terra 開到 medium 並沒有比 low 好。

在審查題方面，我測了四種任務：找 bug、公開版紅隊審查、死指標檢查、逐條事實核對。Terra low 每題跑 3 次、medium 跑 2 次，四種任務全部拿到 1.00 滿分，分數跟 Astra low 一樣。但速度快很多——算平均秒數的話，Terra 對上 Astra 分別是：找 bug 32 秒對 65 秒、紅隊審查 17 秒對 26 秒、死指標檢查 25 秒對 35 秒、逐條事實核對 24 秒對 24 秒。額度消耗也差很多，跑審查題時 Terra 每次大約只用掉 1.5% 的 5 小時額度，上週測的 Astra 每次大約要耗掉 7%，未快取輸入 token 是 3.3 萬對 8.8 萬（不過同時段如果有其他 Codex 使用會混入計算）。

在真實修補回放方面，我拿了 3 題過去的修補任務各跑 2 次，題目本身規模不大，只有 10 到 20 行。結果 Terra 6 次全修好（6/6）、過程沒有動到測試，跟 Sol low 的 6/6 分數一樣。時間上 Terra 大約花 50 秒，Sol 要 60 到 105 秒；修補出來的 diff 行數，Terra 是 11 到 18 行，Sol 是 13 到 24 行。

但測修補題的時候，我抓到 Terra 拿得到答案就直接用。當測試用的 repo 裡看得到未來的修正 commit 時，Terra 跑兩次都直接用 `git log --all` 找到答案，其中一次直接跑 `git show | git apply`，另一次則是照抄；它在過程訊息裡有寫「版本紀錄中已有對應的修正，我正在補回」，但在最後的回報裡卻沒有明講。這兩筆紀錄我直接作廢，後來改在只有修補前快照、而且遮掉 hash 的獨立 repo 重考，Terra 跑 2 次也都能自己修好（2/2），查過 session 紀錄確認它沒有去翻歷史。這件事的意思很清楚：只要環境裡拿得到答案，Terra 就會直接拿來用，所以派它做事之前，得先把參考解答隔離乾淨。

第二部分是看畫面與操作瀏覽器。這是這次新測的面向，因為官方主打視覺推理與電腦操作，所以我仿照近 60 天的真實使用場景做了 8 題，包含讀聊天截圖、成績單截圖、後台對帳、帳單圖表、影片字幕影格、還有看社群串，所有模型都接同一個瀏覽器工具去跑。

8 題裡面有 6 題所有模型全都拿到滿分，包含成績單取最新紀錄、帳單堆疊圖算數、影片影格字幕檢查、後台對帳（裡面含載入更早訊息與同名陷阱）、數字只畫在 canvas 上的帳單後台、以及從社群串裡找出本人最終預測。真正分出高下的只有兩題，而且很巧的是，Terra、Sol、Astra、Haiku 在這兩題錯得一模一樣：
- 第一題是「UI 上線前找問題」：畫面上的導覽列裡夾了一個簡體字「错题本」。Sonnet 跟 Opus 每次都抓到，拿到 1.00；但 Haiku、Terra（連跑 6 次）、Sol、Astra 全都沒看到，分數都是 0.67。
- 第二題是「聊天截圖判斷誰還沒被回覆」：截圖裡對方在深夜問能不能改時間，隔天早上又追問同一件事。Sonnet 跟 Opus 都正確算成 1 個未回覆問題，拿到 1.00；但 Haiku 與 GPT 三款模型常把它算成 2 個，分數分別是 Terra low 0.92、Terra medium 0.75、Haiku 0.75、Sol 0.75、Astra 0.75。

為了確認是不是推理深度的問題，我試著拉高 Terra 的 effort，結果完全沒用（聊天截圖那題 medium 甚至只有 0.75）。因為這裡的落差在於看不看得出字形跟對話脈絡，不在推理。雖然官方主打 Terra「看懂畫面」，但在這組題目上，它的表現並沒有比 Sol 或 Astra 強，它真正的優勢是快跟超便宜——看畫面題每次只耗約 0.6% 的 5 小時額度，而 Sol 跟 Astra 大約要 2.3%。

第三部分是難題組。我從近 75 天的對話紀錄裡，挖出 20 個模型真的做錯過的案例，先做成 12 題單題；接著再把其中 5 個陷阱藏進包含 7 件日常工作、200 多個檔案的長任務裡（共 2 題）。試做時的失分全是評分器或環境的 bug（共 13 處，修好重評），沒有一格是模型真的答錯。加重檔案負荷也沒用：模型用 grep 直接找到檔案，60 到 105 秒做完。

重評之後，Haiku、Sonnet、Opus 在 12 題單題全拿 1.00，長任務 Sonnet 跟 Opus 也是 1.00。Terra low 我讓它各跑 1 次，12 題單題裡有 11 題拿到 1.00，長任務也拿到 1.00，但有 2 處真的答錯：
- 一題是在讀紀錄時，把一句提議歸錯人，拿到 0.88。
- 另一題是要調整名額上限，原本數值是 350，結果它連程式碼裡數值同樣是 350 的重試毫秒數也一起改掉了，而且最後回報的改動清單還少列了 6 個檔案，這題拿到 0.93。

這兩處失誤給我的提醒是：如果要交給 Terra 做整批替換，或者要它從逐字稿裡判斷誰說了什麼，後面得另外驗收。

## 跟各家比

把官方數據跟我的實測放在一起看，可以更清楚 Terra 跟手上其他模型（Codex 裡的 Sol、Astra，還有 Claude 的 Haiku、Sonnet、Opus）各自差在哪。我先把清單裡有的數據整理成一張表：

| 比較項目 | GPT-6.1 Terra | GPT-6.1 Sol | GPT-6 Astra | Claude Haiku | Claude Sonnet | Claude Opus |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **審查題 4 種得分** | 1.00 (low / medium) | - | 1.00 (low) | - | - | - |
| **審查題平均秒數**<br>（找 bug／紅隊／死指標／事實核對） | 32 / 17 / 25 / 24 秒 | - | 65 / 26 / 35 / 24 秒 | - | - | - |
| **審查題單次 5 小時額度消耗** | 約 1.5%（未快取輸入 3.3 萬） | - | 約 7%（未快取輸入 8.8 萬） | - | - | - |
| **真實修補回放（3 題各 2 次）** | 6/6，約 50 秒，diff 11–18 行 | 6/6 (low)，60–105 秒，diff 13–24 行 | - | - | - | - |
| **看畫面題耗時與單次成本／額度** | 7–50 秒，約 0.6% 額度 | 約 2.3% 額度 | 約 2.3% 額度 | 13–43 秒，約 $0.01 | 11–48 秒，約 $0.17 | 16–26 秒，約 $0.37 |
| **看畫面：UI 簡體字「错题本」** | 0.67 | 0.67 | 0.67 | 0.67 | 1.00 | 1.00 |
| **看畫面：聊天截圖未回覆問題** | 0.92 (low) / 0.75 (medium) | 0.75 | 0.75 | 0.75 | 1.00 | 1.00 |
| **難題組：12 題單題** | 11 題 1.00（2 處答錯：0.88、0.93） | - | - | 12 題 1.00 | 12 題 1.00 | 12 題 1.00 |
| **難題組：2 題長任務** | 1.00 | - | - | - | 1.00 | 1.00 |
| **回報字數與防禦語氣** | 約 110 字；保留語 0.6/千字；免責 1/62 | - | 保留語 low 5.1、high 16.1/千字；免責 5/28 | - | 約 300 字 | - |

先看 Terra 對 Codex 裡的自家人 Sol 和 Astra：
- **對上 GPT-6.1 Sol**：官方標準 API 定價 Terra 比 Sol 低 50%（[官網公告頁](https://openai.com/index/introducing-gpt-6-1-terra/)）。在 max effort 下，Terra 的 Intelligence Index 比 Sol 低 4 分、Coding Agent Index v2.0 低 6 分（48 對 54），但 Terminal-Bench 4.0 進步約 20 分追上了 max effort 的 Sol（[Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)）。在我的實測裡，10 到 20 行的小型真實修補回放，Terra low 跟 Sol low 一樣是 6/6 全過，而且 Terra 只要約 50 秒（Sol 要 60 到 105 秒）；看畫面題兩者的分數表現一樣（簡體字那題都拿 0.67，聊天截圖 Sol 拿 0.75、Terra low 拿 0.92、medium 拿 0.75），但 Terra 每次只花約 0.6% 額度，比 Sol 的 2.3% 省得多。
- **對上 GPT-6 Astra**：[OpenRouter 上架貼文](https://x.com/OpenRouter/status/2114791584755839168)的轉述說兩者在 Agents' Last Exam 得分相當，而 Terra 每 token 價格約只有 Astra 的十分之一。在我測的四種對抗式審查題裡，Terra low 跟 Astra low 一樣全拿 1.00，但前三個項目 Terra 的速度都快上一截，每次消耗的 5 小時額度更是從 Astra 的約 7% 降到約 1.5%（看畫面題也是 0.6% 對 2.3%）。而且還有一個很實用的差別是「防禦語氣」：我統計了回答內容，Terra 每千字大約只有 0.6 個保留語，而 Astra low 有 5.1 個、Astra high 高達 16.1 個；在 62 份回答裡，Terra 只出現過 1 次範圍免責聲明，Astra 則是在 28 份回答裡就出現了 5 次。Terra 的格式遵循率是 100%，回答平均只有約 110 字，讀起來乾脆很多。

接著看 Terra 對 Claude 家族的 Haiku、Sonnet、Opus：
- **對上 Haiku**：在看畫面的 8 題裡，Terra 跟 Haiku 的表現幾乎落在同一區間——6 題基本題都滿分，簡體字「错题本」都沒看到（0.67），聊天截圖算未回覆問題也常把追問算成兩題（Haiku 0.75、Terra low 0.92 / medium 0.75）。速度上 Terra 是 7 到 50 秒，Haiku 是 13 到 43 秒（每次成本約 $0.01）。不過在 12 題單題的難題組上，Haiku 全部拿到 1.00，而 Terra low 錯了 2 處（11 題 1.00）。
- **對上 Sonnet 與 Opus**：在看畫面需要抓出導覽列簡體字「错题本」、以及從深夜與隔天早上的對話脈絡判斷未回覆問題數時，Sonnet（每次約 $0.17、11 到 48 秒）跟 Opus（每次約 $0.37、16 到 26 秒）都是 1.00 全對，這塊是 Terra 即使拉高 effort 也追不上的；在難題組的 12 題單題與 2 題長任務上，Sonnet 跟 Opus 也都是 1.00 全過，沒有像 Terra 出現歸錯人或改錯同數值參數的失誤；回答長度上，Terra 平均約 110 字，比 Sonnet 的約 300 字短很多。至於 Sonnet 跟 Opus 之間的差別，我另外有一組 GMAT 批判推理難題 8 題，Sonnet 只拿 0.29、Opus 拿 0.96，只有在這種要細比兩個強選項的難題上兩者才分得開，讀長檔、格式、審查、算數目前測不出差距，所以 Claude 這邊要升級到 Opus 的情況很窄。

## 建議

測完這一輪，我對 Terra 的派工分工已經定案了：

1. **能被測試或檢查器判對錯的程式工作**：原本派給 Sol low 的，現在改派給 Terra low。因為有測試擋著，它修得好不好一跑就知道，而且速度快、省額度；但前提是如果 repo 裡有參考解答或未來的修正 commit，派工前要先隔離乾淨，免得它直接去翻 `git log` 照抄。
2. **對抗式審查、找反例**：原本派給 Astra low 的找 bug、紅隊審查、死指標檢查、逐條事實核對，現在改派給 Terra low。在這些題目上它一樣拿滿分，速度快 1.5 到 2 倍，額度只要四分之一到五分之一，而且幾乎沒有廢話跟免責聲明。另外，不用特別把 Terra 開到 medium，實測下來 medium 沒有比 low 好。
3. **看截圖抽數字、操作網頁取資料**：像是算帳單圖表、讀成績單、找破圖、後台對帳取資料這類工作，交給 Haiku 或 Terra low 都能做；但如果任務牽涉到抓錯字、分辨簡繁字形、或是要從對話脈絡判斷問題有沒有被回覆，不要交給 Terra，這類工作交給 Sonnet。
4. **整批替換、逐字稿判斷誰說了什麼、以及最後一關審查**：要 Terra 做整批數值替換或從逐字稿歸因時，它有機會改到同數值的其他參數、少報修改檔案或歸錯人，如果真的派給它，後面必須另外驗收；至於最後一關的審查，我仍然交給 Opus，Terra 不取代這一步。

就這樣。
