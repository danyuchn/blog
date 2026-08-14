---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-11T04:00:00Z
title: "My Client's Chat Blew Up: Three Questions in One Prompt, and Claude Just Drifted Along With Him"
slug: en/client-scope-explosion-two-skills
featured: false
draft: false
tags:
  - case-study
  - skills
  - ai-workflow
description: 'One prompt asked about revenue, a dashboard, and strategy all at once. The AI answered all of it in one go and my client could not follow a word. Two skills, /explain and /first-principles, pulled the conversation back.'
---

I used to think I was the only one who hits information overload talking to Claude and stops understanding what it's saying. Today I found out I'm not alone. My client has the same problem.

Today we opened up his very long conversation with Claude about the company's internal monthly report, and that's when we found the problem. His very first message asked: how much revenue do we need by the end of this year to not lose money. He also dumped in a pile of data and ideas. I skimmed it and thought, well, that's a pretty detailed prompt.

But scroll down one or two rounds and the AI is already discussing with him whether to restart the ad spend.

Me: ??????

Scrolling back up, I found three things jammed into that one long prompt: a question about revenue, a question about whether he would also need a dashboard later, and a question about whether this business strategy was correct. So he had stuffed data, metrics, and decisions all into the same stretch of conversation. And when the AI answered all of it at once, the scope was too spread out and the information density was too high, and he just BLEW. RIGHT. UP. Couldn't understand a word of it.

But his response to blowing up was to change the subject and go ask whether there were other metrics. That only let the scope keep spreading, and Claude drifted right along with him, without the courage to pull him back in and tell him "you're drifting." Claude got dragged off course too.

So right there I installed two skills for him, the two I use myself every day.

The first is `/explain`. The moment you feel lost, use this skill. It re-explains what was just said in plain language a high schooler would get. If you don't get it, use it. No pretending you do.

The second is `/first-principles`. Use it when your own thinking is stuck and you're lost. It applies Elon Musk's first principles, starting with "what happens if we remove this," cutting whatever can be cut, challenging every built-in assumption, and then rebuilding the reasoning from the most fundamental facts. We ran it over the whole conversation, and the conclusion was that half of the precise numbers he wanted weren't needed at all, that a lot of the reports the AI was walking him through existed only for the sake of existing, and that the things that actually shape the nature of his operation hadn't been touched yet.

After using those two skills on the spot, I asked him, "do you agree? Does the discussion feel like it's converging?"

He came back with a loaded line:

> Now I finally understand why my old employees said "working with me is exhausting."

What I gave him today was a skill that gives the AI the courage to pull his scattered thinking back.

If you want to try the same skills: <https://github.com/agentcrew-academy/harness-starter-kit>

<!--
新增非原文句子清單（忠實度自首）：
1. 「第一個是 /explain。」「第二個是 /first-principles。」對應之 "The first is /explain." "The second is /first-principles." — 類型：改寫（原文為編號清單，改為段落式序數句以符合純段落格式，語意未增減）
2. 原文句尾的一個笑臉 emoji 依站規移除，未以文字補償。
3. 原文「AI帶她做的那些報表」的「她」與全文其他處的「他」不一致，判為錯字，英文統一為 him。
4. 其餘全文為原貼文逐句翻譯；「爆！掉！了！」以 "BLEW. RIGHT. UP." 對應、「我：？？？？？？」以 "Me: ??????" 對應，未新增任何框架句、銜接句或論述展開。
5. en 版已過 humanizer：只動散文句的縮寫（it is → it's 等）與一句「他回了我一句意味深長的話」的譯法（改為 "He came back with a loaded line:"，更貼原文的「意味深長」）。frontmatter、連結、blockquote 引言未動。
-->
