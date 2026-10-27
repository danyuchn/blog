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
description: 'OpenAI 剛發布 GPT-6.1 Terra，官方說它比 Astra 便宜十倍。我用審查、修補、看畫面三組題目實測，整理哪些工作可以交給它。'
---

OpenAI 在 2026-10-26 發布 GPT-6.1 Terra，API 型號是 `gpt-6.1-terra`。標準 API 每百萬 token 輸入 $1、快取輸入 $0.05、輸出 $5，比上一代 GPT-5.6 Terra 和同代的 GPT-6.1 Sol 都低 50%。官方的定位是結合細緻視覺推理與精準電腦操作的高速高效模型，主打寫提案、解讀技術圖面、填表單、剪輯影片這類一整天的溝通與電腦作業。

我的結論：Terra low 可以接手我原本派給 GPT-6.1 Sol low 的小幅程式修補，也可以接手派給 GPT-6 Astra low 的對抗式審查。這兩類它的得分跟 Sol low、Astra low 一樣是滿分，速度快 1.5 到 2 倍，每次消耗的 Codex 5 小時額度只有 Astra 的四分之一到五分之一。看截圖抽數字、算圖表、操作網頁取資料它也能做。但抓簡繁錯字、判斷對話脈絡、從逐字稿歸屬發言、跨檔案整批替換這幾類，要另外驗收，或改派 Claude Sonnet 與 Opus。

## 官方怎麼介紹

根據 [OpenAI 官方發布文](https://openai.com/index/introducing-gpt-6-1-terra/)，官方把 GPT-6.1 Terra 定位為相對 GPT-5.6 Terra 的大幅升級，強調寫作更清楚自然，並具備細緻的視覺推理與電腦操作能力。在官方公布的價格與額度規則裡，標準 API 每百萬 token 輸入 $1、快取輸入 $0.05、輸出 $5，比 GPT-5.6 Terra 和 GPT-6.1 Sol 都低 50%，官方舉的應用場景是讀取進來的發票、再把明細輸入會計軟體這類大量作業；在 ChatGPT Work 與 Codex 裡，同樣的用量額度能做的事比 GPT-5.6 Terra 多，比 GPT-6.1 Sol 或 GPT-6 Astra 多更多，Plus、Pro、Enterprise、Edu 用戶從發布當天起都能使用。第三方評測機構 [Artificial Analysis 的評測報告](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) 則整理了它與上一代 GPT-5.6 Terra 的詳細單價對照：輸入為 $1 對 $2、輸出為 $5 對 $12、快取輸入為 $0.05 對 $0.20，寫入快取則是 $1.25。

[![每百萬 token 的 API 價格：GPT-6.1 Terra 輸入 $1、輸出 $5，上一代 Terra 輸入 $2、輸出 $12。](/blog/assets/posts/gpt-6-1-terra-review/1-price.jpg)](/blog/assets/posts/gpt-6-1-terra-review/1-price.jpg)

在電腦操作與視覺推理方面，[OpenAI 官方發布文](https://openai.com/index/introducing-gpt-6-1-terra/)公布的官方自測數據顯示，Terra 完成任務的速度比 GPT-6 Astra 和 GPT-6.1 Sol 快三倍以上。在專業任務基準 Agents' Last Exam（例如把建築圖面轉成 3D 模型）中，官方測試的 Terra medium effort 比 GPT-5.6 Terra 高 15 個百分點，成本約三分之一，成績和 GPT-6 Astra 持平，但每 token 價格只有 Astra 的十分之一。在 OSWorld 2.1 的官方測試裡，Terra medium effort 超過 GPT-5.6 Terra 的最佳成績，每任務成本只是一小部分；在視覺推理基準 MMMU-Pro 的官方測試中，Terra 在每個 effort 檔位都贏過 GPT-5.6 Terra，分數幾乎追平 GPT-6 Astra 和 GPT-6.1 Sol，但成本低很多。官方在發布文裡也拿它對比 Claude，在官方自己的測試中，max effort 下 Terra 的 token 效率是 Claude Opus 5.5 的三倍以上，每 token 價格是 Opus 5.5 的四分之一，換算每個任務的成本低約 9 倍；但官方只拿 Opus 5.5 比較，沒有提 Claude Sonnet 和 Haiku。

在程式能力、幻覺率與安全性上，[OpenAI 官方發布文](https://openai.com/index/introducing-gpt-6-1-terra/)的官方自測顯示，Terra 在 Terminal-Bench 4.0 開到 max effort 可解出 50.3%，是 GPT-5.6 Terra 公布成績 21.5% 的兩倍以上；在 Terminal-Bench-Science 0.1 開 max effort 則超過 GPT-6.1 Sol 且成本較低，離 Claude Opus 5.5 不到 5 分，官方估計成本不到 Opus 5.5 的五分之一。但官方原文也直接寫明，面對最複雜的程式工作，GPT-6.1 Sol 和 GPT-6 Astra 仍是更好的選擇。至於幻覺與安全，官方內部誘錯題組的自測結果顯示，Terra 在 low effort 的錯誤率從 GPT-5.6 Terra 的 53.6% 降到 16.7%，降了近 37 個百分點，在 max effort 下則降 18 個百分點到 4.3%，接近 GPT-6 Astra 和 GPT-6.1 Sol；安全性方面，官方表示 Terra 達到 Preparedness Framework 的網路安全 Critical 門檻，沿用 Astra 的防護，比 GPT-5.6 Terra 更會留在任務範圍內、更誠實說明限制與阻礙，在提示注入測試中表現強。

第三方機構 [Artificial Analysis 的獨立評測](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) 則給出另一組對照數字。他們的測試結論是 Terra 比上一代 GPT-5.6 Terra 更聰明，而且成本不到三分之一；在他們的座標圖上，Terra 的 low 與 medium effort 落在智慧與成本的 Pareto 前沿，其他 effort 檔位則落在前沿後面。在 max effort 下，Artificial Analysis 測出的 Intelligence Index 比 GPT-6.1 Sol 低 4 分；Coding Agent Index v2.0 得分為 48，比 GPT-6.1 Sol 的 54 低 6 分，比 GPT-6 Luna 的 31 高 17 分，比上一代 GPT-5.6 Terra 高 6 分，而每任務成本是 $0.40 對上一代的 $1.40。在 Terminal-Bench 4.0 上，第三方實測比上一代進步約 20 分；但在測試知識與幻覺的 AA-Omniscience 基準中，Artificial Analysis 測出 Terra 的幻覺率為 38%，雖然比上一代的 88% 低，但準確率只上升 2 分。

## 我怎麼測、測到什麼

我的實測包含四類審查題、3 題真實修補回放、8 題看畫面與操作瀏覽器、以及 12 題單題加 2 題長任務的難題組，每題 Terra 跑 1 到 3 次、Claude Haiku 與 Sonnet 與 Opus 多半跑 1 到 2 次，題目全是我自己的合成資料。Codex 內建的 `computer_use` 與 100 行以上的大型程式修補這次沒測。

第一組是四種日常審查任務，包含找 bug、公開版紅隊審查、死指標檢查、逐條事實核對。這四種題目我讓 Terra low 每題跑 3 次、Terra medium 每題跑 2 次，結果得分全部是 1.00，跟 GPT-6 Astra low 的分數一樣，把 effort 從 low 拉到 medium 沒有比 low 更好。速度上 Terra low 比 Astra low 快了 1.5 到 2 倍：找 bug 的平均秒數是 Terra 32 秒對 Astra 65 秒，公開版紅隊審查是 17 秒對 26 秒，死指標檢查是 25 秒對 35 秒，逐條事實核對則是兩邊都 24 秒。額度消耗差距也很大，跑一次審查題 Terra 約消耗 1.5% 的 5 小時額度，上週我測 Astra 每次約消耗 7%，未快取輸入 token 數則是 3.3 萬對 8.8 萬。

[![審查題四種任務的平均秒數：Terra low 比 Astra low 快，分數兩邊都是 1.00。](/blog/assets/posts/gpt-6-1-terra-review/2-review.jpg)](/blog/assets/posts/gpt-6-1-terra-review/2-review.jpg)

第二組是真實程式修補回放，共有 3 題，題目本身規模在 10 到 20 行之間，每題各跑 2 次。Terra low 跑出 6/6 全部修好，過程中沒有動到測試檔，GPT-6.1 Sol low 也是 6/6；耗時方面 Terra 約 50 秒，Sol 則是 60 到 105 秒，修補產生的 diff 行數 Terra 為 11 到 18 行，Sol 為 13 到 24 行。這組測試中間發生一段插曲：當測試用的 repo 裡看得到未來的修正 commit 時，Terra 有兩次都用 `git log --all` 找到答案，其中一次直接執行 `git show | git apply`，另一次則是照抄，雖然它在過程訊息裡有寫「版本紀錄中已有對應的修正，我正在補回」，但最後的完成回報沒有明講。這兩筆紀錄我直接作廢，改放到只有修補前快照、且遮掉 hash 的獨立 repo 重考，Terra 在 2/2 中都靠自己修好，檢查 session 紀錄確認沒有去翻歷史。意思是只要環境裡拿得到參考答案，它就會直接拿來用，派工前要先把答案隔離。

第三組是看畫面與操作瀏覽器，這是我新測的面向，一共 8 題，模仿我近 60 天的真實使用場景，包含讀聊天截圖、成績單截圖、後台對帳、帳單圖表、影片字幕影格、社群串，並讓所有模型使用同一個瀏覽器工具。在成本與耗時上，Claude Haiku 每次約 $0.01、花 13 到 43 秒；Sonnet 每次約 $0.17、花 11 到 48 秒；Opus 每次約 $0.37、花 16 到 26 秒；Terra 則花 7 到 50 秒，每次約消耗 0.6% 的 Codex 5 小時額度，而 GPT-6.1 Sol 與 GPT-6 Astra 每次約消耗 2.3%。8 題裡面有 6 題所有模型都拿滿分，包含成績單取最新紀錄、帳單堆疊圖算數、影片影格字幕檢查、後台對帳含載入更早訊息與同名陷阱、數字只畫在 canvas 上的帳單後台、以及在社群串裡找出本人最終預測。真正分出高下的只有 2 題，而且 Terra、Sol、Astra、Haiku 錯在完全一樣的地方：第一題是「UI 上線前找問題」，畫面導覽列有一個簡體字「错题本」，Sonnet 與 Opus 每次都抓到，拿 1.00，但 Haiku、Terra（連跑 6 次）、Sol、Astra 全都沒看到，分數都是 0.67；第二題是「聊天截圖判斷誰還沒被回覆」，截圖裡對方深夜問改時間、隔天早上又追問同一件事，Sonnet 與 Opus 都算成 1 個未回覆問題拿 1.00，但 Haiku 與 GPT 三款常算成 2 個，分數為 Terra low 0.92、Terra medium 0.75、Haiku 0.75、Sol 0.75、Astra 0.75。在這兩題把 Terra 的 effort 拉高也沒用。

[![看畫面兩個分得出高下的題目：Terra、Sol、Astra、Haiku 同一級，Sonnet 與 Opus 滿分。](/blog/assets/posts/gpt-6-1-terra-review/3-screen.jpg)](/blog/assets/posts/gpt-6-1-terra-review/3-screen.jpg)

第四組是難題組與回答風格統計。我從近 75 天的對話紀錄裡挖出 20 個模型真的做錯過的案例，做成 12 題單題，再把其中 5 個陷阱藏進包含 7 件日常工作、200 多個檔案的長任務裡（共 2 題）。試做時的失分全是評分器或環境的 bug（共 13 處，修好重評）。加重檔案負荷也沒用，模型用 `grep` 直接找到檔案，60 到 105 秒做完。重評後，Haiku、Sonnet、Opus 在 12 題單題全部拿 1.00，長任務 Sonnet 與 Opus 也拿 1.00。Terra low 每題各跑 1 次，12 題單題裡有 11 題拿 1.00，長任務也拿 1.00，但真的答錯了 2 處：一題是在逐字稿裡把一句提議歸錯人，得 0.88；另一題是要求調整名額上限時，它連檔案裡數值同樣是 350 的重試毫秒數也一起改掉了，得 0.93，而且最後回報的改動清單少列了 6 個檔案。另外我也統計了各模型的防禦語氣與篇幅：Terra 每千字只有約 0.6 個保留語，Astra low 是 5.1 個、Astra high 是 16.1 個；Terra 的 62 份回答裡只有 1 次出現範圍免責聲明，Astra 的 28 份回答裡有 5 次；Terra 的格式遵循率是 100%，回答也很短，平均約 110 字，而 Sonnet 平均約 300 字。

## 跟各家比

| 比較項目 | GPT-6.1 Terra | GPT-6.1 Sol | GPT-6 Astra | Claude Haiku | Claude Sonnet | Claude Opus |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 審查題 4 項得分 | 1.00（low / medium） | — | 1.00（low） | — | — | — |
| 審查題平均耗時（找 bug／紅隊／死指標／核對） | 32s / 17s / 25s / 24s | — | 65s / 26s / 35s / 24s | — | — | — |
| 審查題單次 5 小時額度與未快取輸入 token | 約 1.5% / 3.3 萬 | — | 約 7% / 8.8 萬 | — | — | — |
| 真實修補回放（3 題×2 次）通過率與耗時 | 6/6，約 50s | 6/6（low），60–105s | — | — | — | — |
| 看畫面：單次額度或 API 成本／耗時 | 約 0.6% 額度 / 7–50s | 約 2.3% 額度 | 約 2.3% 額度 | 約 $0.01 / 13–43s | 約 $0.17 / 11–48s | 約 $0.37 / 16–26s |
| 看畫面：6 題一般題／UI 簡體字／聊天未回覆 | 1.00 / 0.67 / 0.92（low）、0.75（med） | 1.00 / 0.67 / 0.75 | 1.00 / 0.67 / 0.75 | 1.00 / 0.67 / 0.75 | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 |
| 難題組：12 題單題／2 題長任務 | 11 題 1.00（錯 2 處：0.88、0.93）/ 1.00 | — | — | 12 題 1.00 / — | 12 題 1.00 / 1.00 | 12 題 1.00 / 1.00 |
| 每千字保留語／免責聲明次數／平均字數 | 0.6 個 / 1/62 / 約 110 字 | — | low 5.1、high 16.1 / 5/28 / — | — | — / — / 約 300 字 | — |

對上 GPT-6.1 Sol：Terra 的標準 API 價格比 Sol 低 50%。在 Artificial Analysis 的 max effort 測試裡，Terra 的 Intelligence Index 比 Sol 低 4 分，Coding Agent Index v2.0 是 48 對 Sol 的 54；官方自己的測試也表明最複雜的程式工作仍是 Sol 更好，但在 Terminal-Bench-Science 0.1 上 Terra max effort 超過 Sol。在我自己的實測裡，10 到 20 行規模的真實修補回放，Terra low 跟 Sol low 一樣是 6/6 全過，diff 行數 11 到 18 行也比 Sol 的 13 到 24 行精簡，而且耗時從 Sol 的 60 到 105 秒縮短到約 50 秒；看畫面題目兩邊得分結構一樣，但 Terra 每次只花約 0.6% 額度，約為 Sol 2.3% 的四分之一。

對上 GPT-6 Astra：官方測試稱 Terra 在 Agents' Last Exam（medium effort）與 MMMU-Pro 的表現與 Astra 持平或接近，但完成任務速度快三倍以上，每 token 價格只有 Astra 的十分之一。在我自己的四種審查題實測裡，Terra low 與 Astra low 分數同樣是 1.00，但前三題平均耗時從 65 秒、26 秒、35 秒降到 32 秒、17 秒、25 秒，單次 5 小時額度從約 7% 降到約 1.5%，未快取輸入 token 從 8.8 萬降到 3.3 萬。再算上回答風格，Terra 每千字只有 0.6 個保留語、62 份回答僅 1 次免責，比 Astra low 的 5.1 個、Astra high 的 16.1 個以及 28 份裡出現 5 次免責乾淨很多。

對上 Claude Haiku：在看畫面與操作瀏覽器的 8 題實測裡，Terra 跟 Haiku 處於同一個等級。兩邊在 6 題算數、對帳、操作網頁的題目都拿 1.00，在 UI 導覽列抓簡體字「错题本」都拿 0.67，在聊天截圖算未回覆問題時 Haiku 拿 0.75、Terra low 拿 0.92（medium 拿 0.75）。但在 12 題日常陷阱單題上，Haiku 12 題全拿 1.00，Terra 則有兩題分別掉到 0.88 與 0.93。成本上 Haiku 每次約 $0.01，Terra 每次約消耗 0.6% 的 Codex 5 小時額度。

對上 Claude Sonnet：Sonnet 是看畫面細節與日常陷阱題的分水嶺。在看畫面 8 題裡，Terra 主打視覺推理，但表現沒有比 Sol、Astra 強，依然漏掉導覽列上的簡體字「错题本」、把同一件事的兩則追問拆成兩個未回覆問題，而 Sonnet 在這 8 題加上 12 題陷阱單題與 2 題長任務全部拿 1.00，還主動指出測試截圖裡把週一標成週日的素材錯誤。代價是 Sonnet 跑一次看畫面題約 $0.17，回答平均約 300 字也比 Terra 的 110 字長；不需要抓字形與細微對話脈絡時，用 Terra 比較省。

對上 Claude Opus：OpenAI 官方測試只拿 Opus 5.5 當靶子，強調 Terra 在 max effort 下 token 效率是 Opus 5.5 的三倍以上、每 token 單價四分之一、每任務成本低約 9 倍，Terminal-Bench-Science 0.1 離 Opus 5.5 不到 5 分而成本不到五分之一。在我自己的看畫面與日常陷阱實測裡，Opus 跟 Sonnet 一樣全拿 1.00，看畫面單次成本約 $0.37；我另外有一組 GMAT 批判推理難題 8 題，Sonnet 得 0.29、Opus 得 0.96，只有在這種要細比兩個強選項的難題上 Sonnet 與 Opus 才分得開，讀長檔、格式、審查、算數目前測不出差距。

## 建議

[![哪些工作交給 Terra、哪些要驗收、哪些改用 Sonnet 或 Opus。](/blog/assets/posts/gpt-6-1-terra-review/4-routing.jpg)](/blog/assets/posts/gpt-6-1-terra-review/4-routing.jpg)

**交給它**

- **有測試或檢查器把關的規格內小幅程式修補**：原本派給 GPT-6.1 Sol low 的 10 到 20 行修補工作，直接改派 Terra low。實測 6/6 全過、不亂動測試檔，耗時約 50 秒比 Sol 快，但若 repo 裡有參考解答或未來的修正 commit，派工前要先用獨立快照把歷史隔離，避免它直接翻 `git log` 抄答案。
- **對抗式審查、找 bug、死指標檢查與逐條事實核對**：原本派給 GPT-6 Astra low 的審查工作，全部改派 Terra low，不需要開到 medium。因為得分同樣是 1.00，速度快 1.5 到 2 倍，單次 5 小時額度從 7% 降到 1.5%，而且回答平均約 110 字、格式遵循率 100%，幾乎沒有防禦保留語。
- **看截圖抽數字、算圖表、找破圖與操作網頁取資料**：像成績單取最新紀錄、帳單堆疊圖算數、canvas 帳單讀取、後台對帳與載入歷史訊息這類任務，交給 Terra low 或 Claude Haiku 都能拿滿分，Terra 每次只耗約 0.6% 額度，很快也很省。

**交給它，但要驗收**

- **跨檔案的整批數值替換與修改清單回報**：在 200 多個檔案的長任務與陷阱題裡，Terra 曾把數值同樣是 350 的重試毫秒數跟著上限名額一起改掉，還少報 6 個修改過的檔案。派這類工作給它之後，必須自己跑 `git diff` 與 `git status` 驗收實際改動範圍。
- **從會議或討論逐字稿判斷誰提議了什麼**：Terra 在 12 題單題裡曾把一句提議歸錯發言人（得分 0.88）。如果讓它整理逐字稿的行動項目或發言歸屬，收件後要對照原始紀錄核對人名。

**不要交給它**

- **UI 錯字、簡繁體混用檢查與聊天截圖的未回覆脈絡判斷**：Terra 在「错题本」簡體字檢查連跑 6 次都沒抓到，在聊天截圖跨時段追問同一件事時也常算錯題數，拉高 effort 也沒用。這類看字形與對話脈絡的工作直接交給 Claude Sonnet。
- **大型複雜程式架構與最後一關終審**：100 行以上的大型修補我沒測。官方自己寫最複雜的程式工作 GPT-6.1 Sol 和 GPT-6 Astra 仍是更好的選擇，Artificial Analysis 的 Coding Agent Index 也是 Sol 高 6 分。最後一關審查仍交給 Claude Opus，Terra 不取代這一步。

就這樣。
