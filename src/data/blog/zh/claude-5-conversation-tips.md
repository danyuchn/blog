---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-23T00:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: 跟 Claude 5 對話的 7 個實用技巧：不發散、不話癆、不偷懶、不雞婆
slug: zh/claude-5-conversation-tips
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - skills
description: '一些最近跟朋友分享的，跟 Claude 5 代系列模型對話的實用小技巧：自製 explain skill 抓外星話、一次回完別讓對話發散、語音輸入配置、first-principles 剪枝、用 hook 治偷懶、CLAUDE.md 極簡化，以及治雞婆的幻影反駁。'
---

一些最近跟朋友分享的，跟Claude 5代系列模型對話的實用小技巧：

## 話講不清楚就 /explain

自己做一個explain skill，當模型開始講外星話的時候就打 /explain。社群上已經有/wait-what, /eli5 可以抓下來用，但我還是覺得自己的最好用。你也可以融合各家所長自己手搓一個。

<https://github.com/agentcrew-academy/harness-starter-kit/blob/main/skills/explain/SKILL.md>

## 一次把話說完，別讓對話發散

5代普遍話癆，除了可以在output style設定concise外，你也可以改變跟他溝通的習慣：不要看到什麼就直接回一句，專心把它列出的所有點都回完。舉個例子，如果他列出了123點，你看到1就回，那他下一次回應就會生出1-1, 1-2, 1-3，你回了1-1，他又會回1-1-1, 1-1-2...對話就會越來越發散。請一次把所有問題回完，並且在對話快要發散時主動說「我們的對話應該要收斂了，因為剛剛談論蠻多已經確定，或者是我沒有意見的東西，你就直接拿去更新，不需再提起。還值得討論的東西，你再把它提出來」

## 語音輸入：專注講一長串

為了專注回一大串，我會建議安裝語音輸入法。不用花大錢買typeless，這個就是我很喜歡的，台灣人做的BYOK平替，配Groq+Luna基本免費。

<https://github.com/chenjackle45/SayIt>

有時我也會用Mac內建的quicktime錄音（尤其是在審查長文件時），一次講個十幾二十分鐘，然後用配置 headless agy，直接吃Gemini原生語音轉錄，再請AI按照意見修改。配置方法我在這邊：

<https://www.agentcrew.cc/blog/posts/zh/voice-input-two-modes/>

## 對話真的亂了：first-principles 砍需求

如果真的不幸脈絡已經散開，你自己也被搞亂，explain也救不回來，那就用這個SKILL，請模型幫需求剪枝，挑戰假設，回歸本質：

<https://github.com/agentcrew-academy/harness-starter-kit/tree/main/skills/first-principles>

## 治「說到跟做到不一致」的偷懶病

Claude總有宣稱跟做的事情不符的通病。這需要用hook來治：只要偵測到模型跟你說「驗證完成/找不到」，就讓hook去翻工具鏈，如果發現模型根本沒用驗證或搜尋工具，就立刻叫模型拿證據，不然就老老實實去做。用這種方式可以解決不少偷懶問題：

<https://github.com/agentcrew-academy/harness-starter-kit/tree/main/hooks/claim-guard/claude-code>

## CLAUDE.md 極簡化

"CLAUDE.md" 極簡化。講道理而不是只給負向約束。我有一套自己的範本，你可以改成自己喜歡的。

<https://github.com/agentcrew-academy/harness-starter-kit/blob/main/claude-md-template/CLAUDE.md>

## 治雞婆：他在反駁我根本沒說過的東西

我不知道大家有沒有發現，Opus 除了愛說外星話之外，還有一個讓人覺得非常躁的點：雞婆。

什麼意思呢？比如我說「把這份報價單的付款條件改成分兩期，簽約先付一半，驗收後再付一半」。

啊這不就是改而已，有什麼好爭的？但是 Opus 會來給我這樣說話：

> 已經改好了。不過有一點我想溫和地提出：你可能會覺得分期付款一定對現金流比較友善，但實際上分期會延後你的入帳時間，而且增加了對方賴帳的風險窗口。值得你再想想。

馬的咧，我什麼時候說過分期一定對現金流比較好？

我超討厭這種為說而說，為了營造「回答結尾有獨立判斷力」而硬塞進去的東西。最重要的是，我最討厭有人來自以為聰明假裝猜我的心然後再反駁我根本沒說過的東西，這種人如果是我的朋友早就反手封鎖。

所以我後來設計了一個 SKILL 專門治他的語病。

<https://github.com/agentcrew-academy/harness-starter-kit/blob/main/skills/phantom-pushback/SKILL.md>

但必須要說這是治標不治本，因為 SKILL 只是事後注入的上下文，模型骨子裡的那個賤嘴會在對話變長後又原形畢露。希望下一代的模型可以解決這個問題。

目前想到的大概是這樣。歡迎補充。

原文發於 [Threads](https://www.threads.com/@dustin_gmat/post/DcXUX-oj6tA)。

<!--
2026-08-28 W36 主對話補記：新增第七節「治雞婆」，素材為 2026-08-21 13:59 Threads 貼文與其自回覆，逐字保留（含「馬的咧」「賤嘴」等原聲）。新增非原文句子僅小標一則「治雞婆：他在反駁我根本沒說過的東西」（框架句）。原文一處 emoji 依站台規範未保留。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 各段 `##` 小標（如「話講不清楚就 /explain」「一次把話說完，別讓對話發散」等六則） — 類型：框架句（依 Dustin 指示新增，供搜尋與導讀，非原文句子）
2. 「原文發於 Threads。」 — 類型：框架句（來源註記）
其餘句子皆為原 Threads 貼文逐字保留，僅將截斷連結還原為完整 URL、修正明顯 typo（如全形/半形混雜、缺空格處）。
-->
