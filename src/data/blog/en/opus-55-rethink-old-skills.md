---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-02T01:00:00Z
title: "After Using Opus 5.5, Many of My Old Skills Need a Rewrite"
slug: en/opus-55-rethink-old-skills
featured: false
draft: false
tags:
  - claude
  - skills
  - ai-workflow
description: 'With no Skill and no open-source project, Opus 5.5 one-shotted a fully animated video, then translated and subtitled a Vietnamese stand-up special. Weekly quota barely moved, and the Skill details I wrote to rein in older models all need a second look.'
---

After using Opus 5.5, I found that a lot of the Skills I wrote in the past need to be adjusted.

Models used to be less creative and less capable. In many places I could only rely on past experience, trial and error again and again, and then add restrictions one by one.

This time, on a whim: I'd seen a lot of people online one-shotting videos with Opus 5.5, so I just asked Opus 5.5 to use its own creativity, effort set to high. I gave it the raw audio of my voiceover and told it to make a video it thought was impressive.

This is what came out. I used to open CapCut and cut the filler words and pauses myself. Now it did all of that, and built extremely detailed animation too. Version one is what it came up with on its own (it didn't read my old SKILL). Version two is the same video with our brand visual guidelines applied.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/tpDFj6VKtsc" title="The three data security questions bosses ask most" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

Here's the prompt I gave it:

> /goal 我允許你用你自己的方法幫忙剪接去贅字、講錯的口誤跟停頓（我臨場發揮的內容不算），動畫也不一定要用hyperframe/remotion跟我們的視覺風格，也不用遵從我們原本的腳本所寫的動畫長相，請你發揮創意用你自己最強的能力創造你覺得最厲害的動畫，不需要受 SKILL約束。做出影片後放到下載資料夾才算目標完成。

That used 2% of my 100 USD weekly quota (???). I can't imagine how much it would cost on Codex.

Honestly:

1. The animation really is stunning (look closely and there are still a few tiny problems, but very few now)

2. All those Skill details and passed-down experience I wrote to constrain the model in the past: I think everyone needs to re-examine them in the Opus 5.5 era

There's a famous saying, "if you learn slowly, you don't have to learn anything." It works on people, and apparently it works on AI too (?

The next day, Opus 5.5 did it again.

To repost translated videos, I used to go find an open-source pipeline plus a SKILL somebody shared on GitHub. This time I tried giving it no SKILL and no open-source project. I told it, one-shot, to translate the video, burn in subtitles, and produce a one-minute highlight cut of the funniest bits. I deliberately picked Vietnamese stand-up comedy, full of local slang and in-jokes, some of which you can only get by reading the text on screen.

Oh my god, oh my god, oh my god.

Opus 5.5 really is a god-tier model. One-shot, done in 10 minutes. The 100 USD weekly quota didn't even move 1%, API-equivalent 2.74 USD. The translation is natural and spot on, and the vertical highlight cut for social media looks properly made.

Once again this shows a lot of SKILLs can be slimmed down. And even if you don't slim them down, they need a major overhaul. Opus 5.5 is unreasonably strong.

The original video is here: <https://www.youtube.com/watch?v=tOO28YF4g60>. It's hilarious.

One more thing: I suggest using Opus 5.5 over the next few days to take stock of your commonly used workflows and write them up as specs. That way, if it gets dumbed down someday, you at least still have a good spec to work from.

<!--
新增非原文句子清單（忠實度自首）：
1. 「用了 Opus 5.5 之後，過去寫的 Skill 都要重新調整」（title，en 為在地化翻譯） — 類型：改寫
2. 「提示詞是這樣下的：」（en: Here's the prompt I gave it:） — 類型：銜接
3. 「隔天，Opus 5.5 神奇再一波。」（en: The next day, Opus 5.5 did it again.） — 類型：改寫
4. 「原影片來源在這裡：」（en: The original video is here:） — 類型：改寫
5. 「順帶提一句：建議趁最近幾天…」 — 類型：改寫（去掉原文「然後」）
6. description 整句 — 類型：框架句
註：原文的換行段落在文中合併為較長段落（僅合併，不增減字句）；其餘句子皆為作者原文的翻譯。
-->
