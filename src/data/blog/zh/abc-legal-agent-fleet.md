---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: ABC Legal 的代理人艦隊：把 AI 實驗變成可治理的生產系統
slug: zh/abc-legal-agent-fleet
featured: false
draft: false
tags:
  - case-study
  - enterprise-ai
  - ai-workflow
description: '整理 Anthropic 官方 ABC Legal 案例的六張圖卡：50+ 生產環境代理人、把 agent 當軟體放進 git、非工程師組成的 steering committee，以及「可信任，才自動化」的營運原則。'
---

以下六張圖卡整理自 Anthropic 官方 case study〈[How ABC Legal turned every employee into a builder with Claude-managed agents](https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents)〉，數據資料截至 2026 年 7 月。

## 01｜真正的突破不是讓 1,100 人學會寫程式

每個人都能成為 builder？ABC Legal 的真正突破，不是讓 1,100 人學會寫程式，而是把散落在個人電腦上的 AI 實驗，變成一支可治理、可觀測、持續運作的代理人艦隊。

左邊是原本的樣子：一群人、各自的筆電、各自的文件，用虛線鬆散地連著。右邊是現在的樣子：一個主 agent 分層掛著五個子 agent，每一個都帶著自己的人、筆電與文件。

數據是 50+ 生產環境代理人、約 310 名員工每天使用 Claude、部分任務成本最高下降約 50%。

![圖卡一：ABC Legal 案例首頁，左側是散落在個人電腦上的 AI 實驗、右側是分層的代理人艦隊，底部數據為 50+ 生產環境代理人、約 310 名員工每天使用 Claude、部分任務成本最高下降約 50%，資料截至 2026 年 7 月。](/blog/assets/posts/abc-legal-agent-fleet/1-card.jpg)

## 02｜把代理人當成軟體

Agent = structured text。prompt + tool list + schedule + credentials + memory，加起來就是一份可審查的設定。

全部放進 git repository。每次修改都走 pull request，因此每個 agent 都有版本歷史、code review、rollback、audit trail。

ABC Legal 的 starter kit 只有兩種：event-driven agents，有事件就啟動；scheduled agents，按小時、日、週執行。Builder 複製 template，用 Claude Code 描述任務，不必自己寫軟體。

![圖卡二：操作模型頁，說明 agent 等於 structured text（prompt、tool list、schedule、credentials、memory），全部放進 git repository 走 pull request，並列出 event-driven 與 scheduled 兩種 starter kit。](/blog/assets/posts/abc-legal-agent-fleet/2-card.jpg)

## 03｜真正的門檻，不是 AI，而是讓非工程師用 Git 與 pull request 工作

ABC Legal 集結 15 人 steering committee，來自 finance、marketing、operations、development，而且沒有任何人是 software developer。

流程是四步：15-person steering committee → 一週內，15 人全部做出可運作的 agent → 一個月內，約 50+ agents 在公司裡運行 → 50+ agents。

每個 agent 都有一個名字、一位 owner、一件工作。兩條起跑線：event-driven，新工作或文件回來就啟動；scheduled，按小時、日、週執行。先讓 builder 做出第一個，再讓他回團隊教下一個。

![圖卡三：橋接頁，標題指出真正的門檻是讓非工程師用 Git 與 pull request 工作，內容為 15 人 steering committee、一週內全員做出可運作 agent、一個月內 50+ agents 運行的四步流程。](/blog/assets/posts/abc-legal-agent-fleet/3-card.jpg)

## 04｜一支代理人艦隊，不是一個萬能 bot

每個 agent 只負責一件可量化的工作。

AI Code Reviewer：檢查 4 個 codebase 的每個 pull request，找 security bugs、performance regressions 與 committed credentials。

EvidenceChain™ Delivery Agent：每天抓出符合條件的資料、取得 PDF，再送到客戶的 FTP server。一位 account manager 約 1 小時做出第一版，而且過去從未自動化。

eFiling Rejection Diagnoser：法院退件後自動讀取工作細節與 court rules，約 1 分鐘把 diagnosis 貼到 Slack。

Charvis：檢查已完成的 service jobs，目前約 98% 的判斷與 compliance team 一致。

![圖卡四：專業艦隊頁，列出四個 agent——AI Code Reviewer 檢查 4 個 codebase 的 pull request、EvidenceChain™ Delivery Agent 每天送件到客戶 FTP、eFiling Rejection Diagnoser 約 1 分鐘貼出退件診斷、Charvis 約 98% 判斷與 compliance team 一致。](/blog/assets/posts/abc-legal-agent-fleet/4-card.jpg)

## 05｜harvest、tune、repeat——讓代理人變聰明，不靠重新訓練

Initial Agent 即時完成工作，記錄每一步的 audit trail。Harvester 每小時或每天掃描 Slack，把 thread replies 與 reactions 整理成 labeled data。Tuner 每週回看全部資料，只提出 prompt 或 config 的修改，並開一個 pull request。

接下來是整條迴圈裡唯一標紅的一步：人類審查並 merge。只有核准後的變更，才會進入 production。

在 deliveries-as-code 裡，一個 reaction 標記錯誤路由，一週內就能變成合併後的 routing rule。整個 loop 只有一個人工步驟：review。

![圖卡五：回饋迴圈頁，五步流程為 Initial Agent 記錄 audit trail、Harvester 掃描 Slack 整理 labeled data、Tuner 每週開 pull request、人類審查並 merge、進入 production，並註明整個 loop 只有一個人工步驟。](/blog/assets/posts/abc-legal-agent-fleet/5-card.jpg)

## 06｜可信任，才自動化

五條營運原則：

一，先讓 humans in the loop。每個 agent 先給建議，等它持續接近人類判斷後，才取得獨立行動的資格。

二，把 pull request 當控制面。決策要能逐行審查、核准、回滾，才適合交給 agent 參與。

三，用 feedback loop 持續改善。Slack 回覆與 reactions 可以變成 prompt、config、evals。

四，用 efficiency ratio 看價值。每次執行都回報 hours 與 dollars。很多 agent 先走一段 J-curve：初期成本高，之後靠 evals、更便宜的 model 與更少 tokens 轉為正收益。

五，不值得的任務，就不要做成 agent。推薦 → 自動化，中間隔著可驗證的信任。

右邊兩張圖分別畫了四階段軸——建議 → 審查與核准 → 受控執行 → 自主運作——以及 J-curve：先投資，後轉正；初期成本高（時間、人力、tokens），靠 evals、更便宜的 model、更少 tokens，轉為正收益，創造時間與金錢價值。

底下引用 ABC Legal 的 Brandon Fuller：「Every agent earns trust before it acts alone.」旁邊那句是：把企業規則變成 X-as-code，讓員工自由掌舵。

![圖卡六：營運原則頁，列出五條原則（humans in the loop、pull request 當控制面、feedback loop、efficiency ratio、不值得的任務不做成 agent），右側為建議到自主運作的四階段軸與 J-curve 圖，底部引用 Brandon Fuller 的「Every agent earns trust before it acts alone.」](/blog/assets/posts/abc-legal-agent-fleet/6-card.jpg)

<!--
新增非原文句子清單（忠實度自首）：
1. 「以下六張圖卡整理自 Anthropic 官方 case study〈How ABC Legal turned every employee into a builder with Claude-managed agents〉，數據資料截至 2026 年 7 月。」 — 類型：框架句（來源標註，依任務要求加入；連結出自原貼文回覆，日期註腳出自圖卡一）
2. 「左邊是原本的樣子：一群人、各自的筆電、各自的文件，用虛線鬆散地連著。右邊是現在的樣子：一個主 agent 分層掛著五個子 agent，每一個都帶著自己的人、筆電與文件。」 — 類型：改寫（圖卡一插圖的文字描述，內容不超出轉錄）
3. 「數據是 50+ 生產環境代理人、約 310 名員工每天使用 Claude、部分任務成本最高下降約 50%。」 — 類型：銜接（把圖卡一數據列串成句子，數值未改）
4. 「流程是四步：」 — 類型：銜接
5. 「兩條起跑線：」為圖卡原文，「每個 agent 都有一個名字、一位 owner、一件工作。」由圖卡「每個 agent 都有：一個名字、一位 owner、一件工作」改標點成句 — 類型：改寫
6. 「接下來是整條迴圈裡唯一標紅的一步：」 — 類型：銜接（描述圖卡五的視覺標記）
7. 「五條營運原則：」與「一，」到「五，」的序號詞 — 類型：銜接（圖卡六原為 1.–5. 編號）
8. 「右邊兩張圖分別畫了四階段軸——建議 → 審查與核准 → 受控執行 → 自主運作——以及 J-curve：先投資，後轉正；」 — 類型：改寫（圖卡六右上與右下兩張示意圖的文字描述）
9. 「底下引用 ABC Legal 的 Brandon Fuller：」與「旁邊那句是：」 — 類型：銜接（引言與右下標語的位置說明）
10. 全部 H2 節標題（「01｜真正的突破不是讓 1,100 人學會寫程式」等）— 類型：框架句（節標題由圖卡卡號與圖卡標題組成，圖卡標題逐字保留）
11. 六張圖片的 alt 文字 — 類型：框架句（依轉錄內容描述圖卡畫面，供看不到圖的讀者理解）
-->
