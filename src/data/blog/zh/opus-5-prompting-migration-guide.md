---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: 舊 prompt 搬到 Opus 5：九張卡的遷移指南
slug: zh/opus-5-prompting-migration-guide
featured: false
draft: false
tags:
  - claude
  - prompting
  - ai-workflow
description: '讀完 Anthropic 官方的 Opus 5 提示指南後整理的九張卡：回答長度、代理敘述、任務邊界、子代理委派、自我修正，還有關掉 thinking 的副作用。'
---

讀完 Anthropic 官方的 Opus 5 prompting 指南，我把它整理成九張卡。重點不是「Opus 5 有多強」，而是舊 prompt 要怎麼搬過來——長任務代理工作更強了，但提示策略也要跟著重新調校。

![卡片一：Claude Opus 5 的提示設計重點，副標為長任務代理工作更強，但提示策略也要重新調校](/blog/assets/posts/opus-5-prompting-migration-guide/card-01.jpg)

這份指南整理的，是 Claude Opus 5 在實務上最常需要微調的行為：回答長度、代理敘述、任務邊界、子代理委派、自我修正，以及關閉 thinking 時的輸出副作用。四個總結：先重跑評測，不要沿用舊模型的預設；effort 主要控制思考量，不直接控制可見字數；Opus 5 會更主動敘述、驗證與委派，需要明確節制；關閉 thinking 可能帶來輸出偽工具呼叫與 XML 標籤外漏。

## 能力升級：先重跑評測

![卡片二：能力升級先重跑評測，列出 agentic coding、code review、vision、long context、multi-agent 五項提升](/blog/assets/posts/opus-5-prompting-migration-guide/card-02.jpg)

與 Opus 4.8 相比，Claude Opus 5 在多檔案 coding、code review、長上下文、視覺理解與多代理協作上都有明顯提升。因此不要直接沿用既有的 effort 設定、驗證流程與 workaround，先用自己的 evals 重新測一輪。

五項提升分別是：Agentic coding 更擅長完整完成長任務；Code review 找 bug 更準，低 effort 也有效；Vision 在圖表、文件、UI 複製上更強；Long context 的 1M token 視窗穩定；Multi-agent 的 writer / verifier 協作更成熟。

## 回答長度：用明示控制，不靠 effort

![卡片三：回答長度用明示控制不靠 effort，說明 effort 控制的是思考量而非可見字數](/blog/assets/posts/opus-5-prompting-migration-guide/card-03.jpg)

Claude Opus 5 的預設回覆通常比過去更長。若你想控制對使用者可見的輸出長度，最有效的方法不是調低 effort，而是在 prompt 中直接寫出你要的簡潔程度。

四點：預設更長，回覆常比舊版 Opus 冗長；effort 的作用主要影響 thinking 與成本；做法是直接要求 focused、brief、concise；補強是在 system prompt 結尾再放一句短提醒。

effort 到底該開多大，我自己的用法是這樣：

> 官方甚至建議
> 如果能調低表現不錯就不需要調高
> 但是thinking一定要開

> effort開多大？high以上很容易過度思考，官方的建議是如果medium/low thinking可以完成任務，就不要往上開

## 代理敘述：三段式進度更新

![卡片四：代理敘述三段式進度更新，分為開始前、進行中、結束時三格](/blog/assets/posts/opus-5-prompting-migration-guide/card-04.jpg)

Opus 5 在 agentic 工作中更愛敘述自己要做什麼。若你想讓它少說但不失去透明度，最好的做法是明確定義更新節奏，而不是籠統地叫它「少講話」。

三段式：開始前先用一句話說明要做什麼；進行中只有在找到重點或改變方向時更新；結束時第一句先回答結果，再補細節。正向示例通常比「不要怎樣」更有效。

## 文件長度：校準 written deliverables

![卡片五：文件長度校準 written deliverables，列出 filler sections、redundant summaries、boilerplate 三種常見膨脹](/blog/assets/posts/opus-5-prompting-migration-guide/card-05.jpg)

除了對話本身，Opus 5 寫到磁碟上的報告、摘要與 Markdown 文件也常比前代更長。對話短，不代表落地文件也會自動變短。如果你的產品會產出文件，記得另外為 written deliverables 設定長度與密度。

容易出現的三種膨脹是 filler sections、redundant summaries、boilerplate。建議的指令是：「覆蓋重點即可，不要用填充段落、重複摘要或樣板內容撐長。」原則兩點：文件長度要跟任務需求匹配；把「完整」與「冗長」分開管理。

## 任務邊界：避免過度驗證與 scope creep

![卡片六：任務邊界避免過度驗證與 scope creep，列出該刪掉的舊指令與該補上的邊界](/blog/assets/posts/opus-5-prompting-migration-guide/card-06.jpg)

在 Opus 5 上，舊有的「再驗一次」「最後再核對」常會讓成本升高卻沒有品質收益。同時，它也更可能自行補做你沒要求的事，因此窄任務要把邊界說清楚。

該刪掉的舊指令：double-check your answer、final verification step、use a subagent to verify。該補上的邊界：deliver what was asked、不同解讀才 check in、若有更好方法先說一句再照做。目標是減少無效驗證，同時防止任務默默變形。

## 子代理：只在大且獨立的工作才委派

![卡片七：子代理只在大且獨立的工作才委派，分列適合與不適合委派的情境](/blog/assets/posts/opus-5-prompting-migration-guide/card-07.jpg)

Opus 5 比前代更願意啟動 subagents。這在真正獨立、可平行的大任務上很有幫助，但如果任務很小，或只是要 double-check，就只會放大時間與成本。委派是槓桿，不是預設動作。

適合委派的：wide multi-file investigation、彼此獨立的平行工作流、一個代理難以同時處理的大片段工作。不適合委派的：少量 tool calls 就能完成的小任務、只是驗證自己的工作、能用一個 subagent 解決卻開很多個、沒有明確分工的雜亂拆解。原則是能少就少，能一個就不要多個。

## 自我修正：只在必要時說明

![卡片八：自我修正只在必要時說明，引言為 State corrections plainly and briefly, then continue](/blog/assets/posts/opus-5-prompting-migration-guide/card-08.jpg)

Opus 5 很會自己抓錯並修正，但它也更常把修正過程講出來。對使用者介面來說，最好的做法不是禁止修正，而是限制「什麼情況值得明講」。

三點：不要再加「double-check」「re-verify」這類提示；只有錯誤會影響 code、結論或決策時才明白更正；不影響使用者的小 slip 直接修掉就繼續。官方的原話是「State corrections plainly and briefly, then continue.」

## 關閉 thinking：風險與緩解

![卡片九：關閉 thinking 的風險與緩解，列出工具呼叫變成文字與內部 XML 標籤外漏兩種風險](/blog/assets/posts/opus-5-prompting-migration-guide/card-09.jpg)

Opus 5 預設開啟 thinking。若把 thinking 關掉，可能出現兩種可見的輸出副作用：工具呼叫變成文字，也就是 tool call 寫進回覆卻沒有真正執行；以及內部 XML 標籤外漏，例如可見的 internal tags 混進輸出。

官方建議的主要緩解方式，是保留 thinking，改用 low effort 或 medium effort 壓低成本。若能不關，就用低 effort 控成本，而不是直接關 thinking。真的必須關閉時，明確要求它可先說一句、無合適工具就直說、不要輸出 internal tags。

九張卡就這樣。

<!--
新增非原文句子清單（忠實度自首）：
1. 「讀完 Anthropic 官方的 Opus 5 prompting 指南，我把它整理成九張卡。」 — 類型：框架句（依據素材背景：作者讀完官方指南後做的整理卡，共 9 張）
2. 「重點不是「Opus 5 有多強」，而是舊 prompt 要怎麼搬過來——長任務代理工作更強了，但提示策略也要跟著重新調校。」 — 類型：框架句（前半句為 AI 新增的定調，後半句為卡 01 副標逐字）
3. 「四個總結：」「五項提升分別是：」「四點：」「三段式：」「容易出現的三種膨脹是」「三點：」 — 類型：銜接（把圖卡的條列轉成行文的引導語，無新增語意）
4. 「effort 到底該開多大，我自己的用法是這樣：」 — 類型：銜接（引出素材 B 兩句原文引言）
5. 「官方的原話是」 — 類型：銜接（引出卡 08 的英文引言）
6. 「九張卡就這樣。」 — 類型：銜接（短促收束，非原文語意）

其餘所有內容均為九張圖卡的逐字或最小改寫轉述；素材 B 兩段引言逐字保留（含原始斷行與無標點）。未新增任何技術解釋、案例或數據。
-->
