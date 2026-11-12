---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
modDatetime: 2026-09-24T04:00:00Z
title: "Cheap Models for Grunt Work, Flagship Models for Review: A Durable Division of AI Labor"
slug: en/gpt-5-6-luna-max-grunt-work
featured: false
draft: false
tags:
  - gpt
  - model-comparison
  - automation
description: 'Offload time-consuming browser scraping and bulk data entry to budget models, while saving flagship models for spec review. From pulling bank statements and hunting award seats to tagging customer profiles, here is a durable framework for dividing AI labor.'
tldr: 'When you need to scrape data from anti-scraping websites without APIs, avoid costly services or aggressive scripts. Set up a division of labor: let cheap models handle raw browser chores at human-like speeds overnight without getting blocked, and have advanced models review the final results.'
seoTitle: 'GPT-5.6 Luna Max: Browser Automation for Office Grunt Work'
---

When picking AI models, people love to dismiss smaller or cheaper options across the board. But in real-world workflows, a huge chunk of work is just mind-numbing, mechanical grunt work: pulling statements from bank portals that have no public API and aggressively block scrapers, clicking through dozens of date combinations on clunky airline systems to find award seats, or cross-referencing spreadsheets to copy customer notes into a backend sidebar one by one.

Often you just need some data once. You don't want to script an aggressive scraper that risks getting your IP banned, nor do you want to pay a third-party aggregator for a one-off pull. People who dismiss certain models out of hand are usually just showing a lack of imagination, dunking on tools to sound sophisticated. Every model has its place if you know what to do with it. Even Gemini has a role in my setup. The trick to handling grunt work is a clear division of labor: let budget models handle the slow, browser-based clicking and computer use, then bring in flagship models to run quality checks and push the goal across the finish line.

## The Pain Point of Grunt Work: Why Flagship Models Aren't the Answer

Grunt work in everyday workflows usually shares the same traits: no official API, tight anti-scraping defenses, endless retries and waiting, and brutal token consumption.

Historically, you had two ways to handle these scraper-hostile sites. You could have an AI install browser fingerprinting libraries and fight a cat-and-mouse game with anti-bot shields, risking an IP ban. Or you could buy access through a third-party API. But for low-frequency, ad-hoc tasks, neither makes sense—you don't want the hassle of fighting bot guards, and you don't want to pay for another subscription.

Budget models are a natural fit here. Take GPT-5.6 Luna Max, which I tested extensively when it came out: its killer feature is brute-force browser scraping. It drives an actual desktop browser session, matching human behavior in token footprint, browser fingerprint, speed, and click rhythm. I ran it daily without hitting a single 403. I could leave it running all night, wake up to find it had used maybe 5% of its allowance, and the job was finished.

In one test run, I assigned it to collect financial statements across multiple platforms. The agent drove a live browser, visited each bank and payment processor (after I logged in manually), and downloaded missing statements. I intentionally avoided APIs, MCP tools, or CLI utilities—everything relied strictly on clicking through the interface and visually confirming page state.

As the terminal screenshot below shows, once given the goal, the agent wrapped up in about 22 minutes (logged as "Worked for 21m 49s"), downloading four financial statements and verifying their dates and formats. Counting another task that had already been running for an hour in parallel, the weekly quota had dropped by just 1%—roughly $3.14 in equivalent token usage.

![Terminal output showing the agent completed the task, reporting four financial statements downloaded and verified against dates and formats, with "Worked for 21m 49s" at the bottom](/blog/assets/posts/gpt-5-6-luna-max-grunt-work/1-luna-max-goal.jpg)

At this price-performance ratio, comparing it to other premium models isn't even the point. It could pull users away from DeepSeek too, because when you look at token efficiency, agent execution, and computer/browser use, DeepSeek struggles to match GPT-5.6. To me, GPT-5.6 Luna is the reigning king of grunt work.

## Browser Scraping and UI Automation: The Natural Home for Cheap Models

Rote information retrieval and cross-checking are where budget agents shine. A few primary use cases stand out:

First, monitoring sentiment on social platforms. When scanning social feeds, it sidesteps anti-scraping defenses without triggering rate limits, perfect for occasional lookups where buying dedicated API access makes zero financial sense.

Second, hunting airline award seats. Anyone who has booked award travel on ANA knows how clunky their booking portal is, how convoluted the routing rules are, and that no public API exists for it. Searching for seats means mechanically clicking through dozens of date combinations, checking availability one by one, and logging the flight details for me to make the final call. Thanks to GPT-5.6 Luna Max, it snagged two business-class seats between Bangkok and Tokyo just the other day.

As shown below, the terminal steadily iterated through date combinations while Chrome on the right opened the calendar menu on ANA's Japanese reservation portal to check availability:

![Terminal testing BKK-KIX date combinations while Chrome on the right navigates the calendar menu on the ANA Japanese award booking page, with the "ChatGPT started debugging this browser" banner across the top](/blog/assets/posts/gpt-5-6-luna-max-grunt-work/2-ana-award-seats.jpg)

On a related note, my compliments to Cathay Pacific: your CAPTCHAs are sophisticated, but GPT Luna Max cracked them right in front of my eyes, one after another. In the image challenge below on Cathay's site, it correctly identified every single breakfast food item:

![Image CAPTCHA on the Cathay Pacific website asking to select all breakfast foods, with several boxes already checked](/blog/assets/posts/gpt-5-6-luna-max-grunt-work/cathay-captcha.jpg)

Third, comparing hotel rates and claiming Best Price Guarantees. A budget model understands price-match policies well enough to compare listings across booking engines and help file refund claims.

Fourth, relaying documents across messaging apps remotely. When I am out, I can message my agent from my phone: open LINE or Messenger, grab the requested document, hand it to Sol or Terra for processing, and have Luna send the finished file back on LINE. I have handled plenty of tasks this way on the go. The same logic applies to filtering job postings on 104 or cross-checking hotel rates across multiple sites—these are classic Luna Max territory. I demonstrated these workflows on video in episode 34 (<https://youtu.be/8Sxw1Mdcl8Q>).

## Moving Data Across Systems: Real-World Long Tasks

Beyond one-way web scraping, another massive time sink is shuffling data across fragmented systems and keeping formats in sync.

If you manage a LINE Official Account, you probably hate the contact sidebar as much as I do. Registration details live in a Google Drive spreadsheet, while individual client folders are scattered elsewhere across Drive. In the past, I had to open each record by hand, attach tags, and verify everything against my notes.

As shown below, the steps are fixed and the fields are tedious—pure mental drudgery:

![Customer sidebar in the LINE Official Account admin console: plan tags, assigned staff, and notes showing plan expiration dates and Google Drive folder links (customer details redacted)](/blog/assets/posts/gpt-5-6-luna-max-grunt-work/line-oa-sidebar.jpg)

Eventually I offloaded this to GPT-6 Luna Max. It tagged and synchronized over a hundred client records in about an hour, burning roughly 5% of a $20 five-hour bucket (about 1% of my weekly cap). It is undeniably cheap. Speed is its only bottleneck, and a quick verification pass with Opus confirmed zero missed records.

The same pattern applies to long-running environment sync tasks. For example, syncing harness configurations from Claude Code over to Codex (using a dedicated skill). Once given the `/goal` command, it ran steadily for an hour without falling apart.

Video production follows the same logic. Operating on the principle that every model has its superpower, I once produced a 20-minute long-form video entirely with a budget model paired with HyperFrames. In professional editing suites, hooking up DaVinci Resolve Studio with control protocols for a budget model turns it into an absolute powerhouse for post-production grunt work—unbeatable at repetitive timeline edits.

## The High-Low Pairing: A Two-Tier Model for Execution and Review

In long-form video experiments, things hold together fine as long as the pipeline enforces rigid specifications. But Luna Max tends to drift on scene specifications across cuts, requiring manual fixes. You see the same flaw elsewhere: give Luna a spec to write and it drifts. It genuinely excels at data collection and mechanical browser automation, not architectural consistency.

My takeaway after finishing that project: pairing it with a flagship model for final review makes the entire workflow vastly smoother. That is the core idea behind a two-tier division of labor:
- Budget models: Lead the charge, handling time-consuming, repetitive browser clicks, data collection, and asset transfers.
- Flagship models: Run final review and ensure the objective is completed without compromise.

I always tell people that GPT-5.6 Sol is like a rabid dog. When you hit it with `/goal` (I even queue up LISA's track in the background and hum along to the "gou-si, gou-si" soundalike), it locks onto the target and won't let go until the job is done.

For grunt work, 5.6 Terra high is top tier. Its computer and browser control is remarkably accurate, handling even intricate award-seat searches without breaking a sweat. Best of all, it barely dents your quota, freeing up Sol for tasks that actually require heavy lifting. Anyone who has used both GPT and Claude computer control MCPs will notice the contrast: one handles actions smoothly with careful self-checks, while the other fights for mouse control and gives up too easily.

Evaluating models is not just about raw intelligence; access pathways matter just as much. For example, direct HTTP requests to X or Threads often get blocked, forcing you to go through a browser session, whereas Gemini handles direct reads without friction. Reddit resists certain tooling while working cleanly in others. Knowing the entry points of each tool is what makes practical automation viable.

## Selection Criteria and Operating Boundaries for Grunt Work

When setting up everyday automation tasks, use these criteria to configure your models:

First, whenever a task lacks an API, blocks traditional scrapers, and burns through tokens, drive it via browser or computer control using Luna. It keeps quota usage negligible, preserving your flagship models for high-value reasoning.

Second, while Luna handles data gathering and mechanical browsing well, its spec compliance drifts easily. If drift becomes an issue, slot it into a tightly constrained pipeline or pair it with a flagship model for final verification.

Third, stop dismissing models across the board. Every model has a valid use case. Performance is not just raw benchmarks—entry points and interface control matter just as much. It comes down to having the imagination to put each tool where it belongs.

(Note: The first draft of this post was written in mid-2026; the GPT-5.6 Luna Max, Sol, Terra, and GPT-6 models mentioned reflect testing records from that period.)

## Appendix

Technical implementations and background details for the commands, tools, and protocols mentioned in this article include:

1. Goal-oriented commands: The `/goal` and `/loop` commands referenced in the text solve the vast majority of execution issues.
2. Development environment and workflow skill synchronization: The cross-environment sync described involves porting Claude Code's agent harness and skill specifications into a Codex environment.
3. Browser and computer control: Agents interact with live environments via Model Context Protocol (MCP) and Computer Use desktop interfaces, driving real browsers and operating systems (such as the "ChatGPT started debugging this browser" banner visible in the Chrome screenshot).
4. Video and post-production tooling: Long-form video production utilized HyperFrames, while editing was handled by DaVinci Resolve Studio driven by agent MCP protocols.

<!--
2026-08-28 W36 碎念併入：live 碎念「影片後製的神」逐字併入，該條講的正是本文的主題（Luna Max 幹雜活）。已從 zh/en live 檔刪除。零新增句子（小標即原碎念標題）。
-->

<!--
2026-08-28 W36 碎念併入：archive 碎念「兩個指令解決大部分問題」逐字併入，本文的兩個任務都是下 /goal。已從 zh/en archive 刪除。新增非原文句子僅小標一則（框架句）。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「此次分派的任務是兩個：一是⋯⋯；二是⋯⋯」 — 類型：改寫（原文為編號列點 1)/2)，改成句內序列，內容一字未增）
2. 「我最常用 LUNA 的場景有幾個。一是⋯⋯二是⋯⋯三是⋯⋯四是⋯⋯」 — 類型：改寫（原文為 1./2./3./4. 編號列點＋「理由：」標籤，改成連續句；理由文字原樣保留）
3. 「最近除了 5.6 Sol」的「最近」 — 類型：銜接（原碎念條目起手詞，保留）
4. 「我都跟別人說，GPT 5.6 Sol 是瘋狗⋯⋯不做完不罷休。」（整段逐字置入，無新增句） — 類型：併入碎念（GPT 5.6 Sol 是瘋狗，2026-08-14 週報併入）
-->

<!--
2026-09-24 W40 補記：2026-09-24 Threads 貼文（LINE 官方帳號客戶標註）與 2026-09-20 貼文（國泰人機驗證）逐字併入。新增非原文句子：小標（框架句）、「另外，」（銜接）。截圖中客戶姓氏已由主對話遮蔽。原文 emoji 依站台規範未保留。

2026-10-26 拼接順稿：
- 「在剪輯後製上也是一樣：」— 類型：銜接
結構調整：移除標題拼貼標記，將長片與後製整合為一節、國泰航空驗證碼移至 ANA 爬蟲後方、兩指令小節併入前文，並將相對於 pubDatetime 矛盾的「剛剛」修正為「後來」。
-->

<!--
2026-11-12 舊文盤點整篇重寫：將過期模型名稱定位為歷史實測案例，全文提煉為「廉價模型包辦瀏覽器雜活、高階模型審核」的長效選型判準，重整段落架構並將內部指令與技術細節收納至附錄。
-->