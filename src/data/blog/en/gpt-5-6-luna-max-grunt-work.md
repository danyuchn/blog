---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: GPT-5.6 Luna Max Is the New King of Grunt Work
slug: en/gpt-5-6-luna-max-grunt-work
featured: false
draft: false
tags:
  - gpt
  - model-comparison
  - automation
description: 'Using Luna Max for grunt work after the price cut: statements pulled in 22 minutes, brute-force scraping all night, and two ANA business class award seats from Bangkok to Tokyo.'
---

I just tried using the post-price-cut GPT-5.6 Luna MAX for grunt work, and it's fucking good.

I handed it two jobs. One: use the browser to go to every bank and payment platform (after I logged in for it) and pull down the statements I was missing — deliberately no API, no MCP, no CLI. Two: sync the harness from the Claude Code side over to Codex (a SKILL already exists for this). I ran `/goal` on both. The first one finished cleanly in 22 minutes; the other has been running for an hour and is still going, in good order. So far it's burned 1% of the weekly quota — converted to API pricing by tokens, that's roughly 3.14 USD.

![Terminal showing the agent reporting four financial statements downloaded and cross-checked for format and dates, with Worked for 21m 49s at the bottom](/blog/assets/posts/gpt-5-6-luna-max-grunt-work/1-luna-max-goal.jpg)

At this price-performance ratio, it's not even a question of comparing it to A＼ anymore. I think DeepSeek's users might all get pulled away. On token efficiency, on agent ability, on computer/browser use, DeepSeek is going to have a hard time going up against GPT-5.6. I'm calling it: GPT-5.6 Luna is the new king of grunt work.

What it's best at is brute-force browser scraping, going after sites with no API that love to block crawlers. Before, you either had the AI download a pile of packages and scripts and hack away at it, or you went and paid a third-party API for the data. But sometimes I just want to scrape something once. I don't want to force it and risk getting banned, and I don't want to pay a third party for the data either. So I fire up Luna Max + goal, let it run all night, wake up down only 5% HP, job done.

For this kind of thing it drives your real browser directly. Tokens, fingerprint, speed, frequency all look human. I scrape every day and haven't been 403'd yet. Just leave it running overnight. Whatever tier of GPT 5.6 you use, its browser control and computer control are far ahead of Claude. On accuracy and efficiency of browser control, Claude really loses to GPT by a wide margin.

LUNA is for grunt work specifically. Take the jobs that traditionally eat tokens: sites with no API that block crawlers, where you have no choice but to scrape through a browser MCP. Or being out of the house and remotely driving your computer with computer use. Luna is the only choice.

A few scenarios where I use LUNA most. One: scraping social media posts to monitor sentiment. Reason: I don't want to risk going head-to-head with anti-scraping, I only check occasionally, and I don't want to specially buy third-party API data. Two: having it find award seats on airline sites. Mechanically clicking through dozens of date combinations, glancing at whether a seat exists, copying down the availability and flight info for me to make the final call, and there's no API that does this. Three: having it compare prices across accommodation platforms, even filing best-price-guarantee refund claims. Same reason as above, plus it's now smart enough to understand best-price-guarantee rules and terms. Four: being out somewhere and telling LUNA from my phone: go open LINE/Messenger, download the file the other person wants, have Sol/Terra process it, then send it back to them on LINE. I've already gotten a fair amount done remotely this way. Same goes for filtering job listings on 104, checking hotel prices across a pile of platforms. All my favorite Luna Max scenarios. Feels like I should shoot a video demoing this? (Update: I did, EP.34 <https://youtu.be/8Sxw1Mdcl8Q>)

![Terminal testing BKK-KIX dates one by one, with Chrome on the right showing ANA's Japanese award booking calendar and a ChatGPT started debugging this browser bar at the top](/blog/assets/posts/gpt-5-6-luna-max-grunt-work/2-ana-award-seats.jpg)

Thank you GPT 5.6 Luna Max. Two days ago it snagged me two business class award seats, Bangkok to Tokyo. Only people who've used ANA know how bad their award system is and how complicated the rules are.

People who sit around trashing some model "across the board" just have too narrow an imagination, and want to look knowledgeable by putting models down. Every model has use cases it fits. It depends on whether you have the imagination. In my eyes, even Gemini has its place.

I tell everyone GPT 5.6 Sol is a mad dog. Give it the /狗死 (dog-die) command, and I usually play LISA's "dog-die~dog-die~" alongside it, and it clamps onto the target and won't let go until the job's done.

Lately, besides 5.6 Sol, my favorite is 5.6 Terra high. It's the top pick for grunt work. Still very accurate at driving the browser and the computer, and it even handles complicated award-seat searches for me. The key thing is how little quota it uses, so I can save Sol for more important things. After using both GPT's and Claude's computer control MCP, anyone would be surprised at how big the gap has gotten: one operates smoothly and checks its work carefully, the other yanks your mouse around and gives up easily.

For social sites like X and Threads, direct WebFetch from Claude and Codex often gets blocked and you have to route through a browser, while Gemini can just read them. Reddit is especially unfriendly to Claude; Codex and Gemini go through fine. Models aren't only competing on how smart they are. It also comes down to what data they can get in the door.

<!--
新增非原文句子清單（忠實度自首）：
1. 「此次分派的任務是兩個：一是⋯⋯；二是⋯⋯」/「I handed it two jobs. One: … Two: …」 — 類型：改寫（原文為編號列點 1)/2)，改成句內序列，內容一字未增）
2. 「我最常用 LUNA 的場景有幾個。一是⋯⋯二是⋯⋯三是⋯⋯四是⋯⋯」/「A few scenarios where I use LUNA most. One: … Two: … Three: … Four: …」 — 類型：改寫（原文為 1./2./3./4. 編號列點＋「理由：」標籤，改成連續句；理由文字原樣保留）
3. 「最近除了 5.6 Sol」/「Lately, besides 5.6 Sol」的「最近」 — 類型：銜接（原碎念條目起手詞，保留）
4. 「I tell everyone GPT 5.6 Sol is a mad dog... until the job's done.」（整段逐字置入，僅把破折號插語改為逗號連接） — 類型：併入碎念（GPT 5.6 Sol Is a Mad Dog，2026-08-14 週報併入）
-->
