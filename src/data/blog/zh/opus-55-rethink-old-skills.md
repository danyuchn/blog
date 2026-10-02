---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-02T01:00:00Z
title: 用了 Opus 5.5 之後，過去寫的 Skill 都要重新調整
slug: zh/opus-55-rethink-old-skills
featured: false
draft: false
tags:
  - claude
  - skills
  - ai-workflow
description: '不給 Skill、不給開源專案，Opus 5.5 one-shot 剪出整支動畫影片，又把越南語單口喜劇翻譯壓字幕。週額度幾乎沒動，過去為了規範模型寫的 Skill 細節都該重新審視。'
---

用了 Opus 5.5 之後，我發現過去寫的很多 Skill 都要重新調整了。

以前模型不夠有創意、也不夠強，很多地方只能靠過去的經驗不斷試錯，再一條一條加上限制。

這次靈機一動，因為看到網路上很多人用 Opus 5.5 one-shot 做影片，我就直接請 Opus 5.5 發揮自己的創意，effort 開到 high，把我的口白原始音檔給他，做一支它自己覺得厲害的影片。

做出來就是這個樣子。以前我還會去剪映自己剪掉贅字停頓，現在他全幫我做了，還幫我做超級細緻的動畫。第一版是它自己發揮的成果（沒讀之前的SKILL），第二版是套上我們品牌視覺規範之後的版本。

<div class="video-embed"><iframe src="https://www.youtube.com/embed/tpDFj6VKtsc" title="老闆最常問的三個資料安全問題" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

提示詞是這樣下的：

> /goal 我允許你用你自己的方法幫忙剪接去贅字、講錯的口誤跟停頓（我臨場發揮的內容不算），動畫也不一定要用hyperframe/remotion跟我們的視覺風格，也不用遵從我們原本的腳本所寫的動畫長相，請你發揮創意用你自己最強的能力創造你覺得最厲害的動畫，不需要受 SKILL約束。做出影片後放到下載資料夾才算目標完成。

100USD 週額度耗費2%（？？？不敢想像如果是Codex會耗費多少。

老實說：

1. 動畫效果真的很驚艷（細看還是有一些很微小的問題，但已經很少了）

2. 過去為了規範模型寫的那些 Skill 細節跟經驗傳承，我想接下來在Opus 5.5 時代，大家都要重新審視一次了

果然有一句名言「只要你學得慢，就什麼都不用學」，不只對人有用，對AI好像也有用（？

隔天，Opus 5.5 神奇再一波。

以前搬運翻譯影片都需要上網找Github上面有人分享的開源流水線+SKILL。我這次試著不給任何SKILL或者開源專案，直接one-shot叫他翻譯影片壓字幕＋出一分鐘笑點精華版。並且我故意選的是有很多在地隱語梗的越南語單口喜劇，有些還要看影片中銀幕上的字才知道意思。

天哪 天哪 天哪

Opus5.5 果真是神之模型，one-shot 10分鐘到位。100USD 週額度連1%都沒動到，API等值 2.74USD。翻譯非常自然到位、直板精華版社群影片也做得有模有樣。

再次證明很多SKILL都可以精簡化了，就算不精簡化，也要大修一遍。Opus 5.5 真的強的不像話。

原影片來源在這裡：<https://www.youtube.com/watch?v=tOO28YF4g60>，有夠好笑。

順帶提一句：建議趁最近幾天用 Opus 5.5 把常用的工作流大盤點規格化一下，這樣未來萬一降智至少還有一套好的spec可以用。

<!--
新增非原文句子清單（忠實度自首）：
1. 「用了 Opus 5.5 之後，過去寫的 Skill 都要重新調整」（title） — 類型：改寫
2. 「提示詞是這樣下的：」 — 類型：銜接
3. 「隔天，Opus 5.5 神奇再一波。」 — 類型：改寫（原文為「Opus 5.5 神奇再一波」，加「隔天，」並移除標題式斷行）
4. 「原影片來源在這裡：」 — 類型：改寫（原文為「原影片來源：」）
5. 「順帶提一句：建議趁最近幾天…」 — 類型：改寫（原文為「然後順帶提一句：」，去掉「然後」）
6. description 整句 — 類型：框架句
註：原文的換行段落在文中合併為較長段落（僅合併，不增減字句）；其餘句子皆為作者原文。
-->
