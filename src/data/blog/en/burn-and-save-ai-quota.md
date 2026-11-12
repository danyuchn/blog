---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-21T04:00:00Z
title: "Burning and Saving AI Quota: How I Audited, Allocated, and Spent My Compute"
slug: en/burn-and-save-ai-quota
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - ai-workflow
description: 'An audit of seven AI quota pools: burning expiring credits on self-verifiable tasks while using surplus compute to build long-term token savings. Combines a terminal dashboard and routing scripts to dispatch tasks dynamically and refine rules from logs. Includes complete tables and reusable prompts.'
---

Most people paying for AI subscriptions hit the same two frustrations: either you burn through your quota in the middle of a busy workday, or you watch the weekly countdown reset while a stack of bundled credits quietly expires.

I live in Bangkok. After transitioning from teaching GMAT to building AI workflows, I spend around $125 a month on three subscriptions: Claude Max 5x, Codex Plus (ChatGPT Plus), and Google AI Pro. But what really made me stop and audit my accounts wasn't the monthly bill. It was realizing I had seven different quota pools with conflicting rules, loaded with bundled freebies, regular weekly resets, and expiring credits. Left alone, they expired every week. But dispatching busywork just to keep them from going to waste meant the models generated low-value filler that demanded manual review—effectively paying subscription fees to give myself unpaid overtime.

To fix this, over the past two weeks I tackled the problem from two opposite yet closely linked angles:

The first was "burning quota": dumping near-expiring compute entirely into tasks where the machine can verify its own output, running them while I sleep.

The second was "saving quota": using this surplus compute to refactor my workspace, slim down rules, and set up automations so future sessions consume fewer tokens.

By November, this evolved from static, pre-benchmarked assignments into a dynamic setup driven by a terminal dashboard and routing scripts that dispatch work based on real-time quota balances. This article covers the whole playbook: the audit checklist, decision filters, overnight batch tactics, structural token-saving techniques, and the dynamic dispatch logic, with ready-to-copy prompts at the end.

## Auditing My Seven Quota Pools

My fixed monthly subscription spend is about $125:

- Claude Max 5x: $100
- Codex Plus (ChatGPT Plus): $20
- Google AI Pro: $4.99 (promotional rate)

What actually got me auditing was the bundled extras. Max 5x includes a $100 monthly Console API credit, claude.ai handed out $250 in cloud session credits, and Google AI Pro comes with 200 Colab compute units (CUs) per month. Every pool operates under different rules: some expire with the billing cycle, some are one-offs, and others expire after 90 days.

The audit itself was straightforward. I had Claude Code open a browser, check each settings and billing page, and pull the balance, reset cadence, expiration date, and supported tools into a table. I ran the first check on October 10 and re-audited all seven pools on October 20:

| Quota Pool | Reset Cadence / Expiration | Best Used For |
|---|---|---|
| Claude Max 5x subscription | Rolling 5-hour window, plus weekly cap resetting Sunday | Primary chat, subagents, overnight batches |
| Claude Cloud credits ($250) | One-time, expires Nov 5 | Cloud sessions only; isolated from local files and credentials |
| Console API promo ($100) | Monthly per billing cycle, expires at cycle end, no rollover | API calls, Agent SDK, scheduled `claude -p` jobs with API key |
| Codex Plus | Rolling 5-hour plus weekly limits, often resets early | Coding tasks, adversarial reviews |
| agy (Google AI Pro) | Three model tiers, each with weekly and 5-hour caps | Long document summaries, transcription, second opinions |
| Colab CUs | 200 per month, each batch expires in 90 days | Training and heavy batch jobs beyond local machine capacity |
| Local models (Mac mini) | Free; constrained only by available time windows | Overnight idle batches, sensitive data that cannot touch the cloud |

![Seven AI quota pools arranged by reset cycle, ranging from rolling five-hour subscription windows to one-time cloud credits, highlighting expiring pools](/blog/assets/posts/burn-and-save-ai-quota/1-quota-pools.jpg)

Finally, I had Claude write a small CLI command so I could check most balances in a single line. Cloud credits and Console promos aren't exposed through the CLI, so those still require checking the web UI.

## Three Decision Filters: What Deserves the Compute

Before my weekly quota reset on October 16, I still had over half of it left. I asked Claude to search Reddit and the web for how people spend excess compute meaningfully, then match those ideas against my own setup.

A thread on r/ClaudeCode about wasted Max quotas had a spot-on comment: if an output requires manual review, you are just manufacturing work for yourself.

That led me to settle on three sequential filters:

1. **Does it expire soon?** Use what expires first. Cloud credits, the current billing cycle's Console promo, and weekly caps near their reset window take priority.
2. **Can the output verify itself?** Let the machine judge whether test suites pass, answer keys match, or videos render cleanly. Anything requiring line-by-line reading goes to the back of the line.
3. **Does it leave an enduring asset?** Build tools, rules, and reusable scripts that save effort on future runs. One-off reports come last.

![Three decision filters for spending compute: does it expire, can it verify itself, and does it leave a lasting asset, prioritizing tasks that pass all three](/blog/assets/posts/burn-and-save-ai-quota/2-decision-flow.jpg)

With the filters set, I assigned clear responsibilities to each quota pool. Here is the division of labor Claude and I configured on October 20:

| Quota Pool | Assigned Work | Guardrails |
|---|---|---|
| Claude subscription | Primary chat, judgment-heavy work, final decisions | Every fallback path ultimately routes back to Claude |
| Cloud credits | Large batches not requiring local credentials | Push to branch and open draft PR; auto-merge forbidden; one-time pool |
| Console promo | Daily automated schedules | Falls back to subscription when exhausted |
| Codex | Coding tasks verified by tests/linters, adversarial reviews | Falls back to Claude when limits are hit or tests fail |
| agy | Long doc summaries, transcription, second opinions | Reserve 10% weekly for manual use; stop dispatching at 90% |
| Colab | Training, heavy batches beyond local hardware | Spent by priority; burn expiring units first |
| Local models | Early morning idle window, resumable batches, sensitive data | Runs only 02:15–05:45, guarded by memory and swap limits |

## Burning Quota Overnight: Machine-Verifiable Tasks Only

When burning compute, the cardinal rule is letting the model run complete batches while I sleep.

Before heading to bed on the night of October 19, I told Claude: feel free to open multiple terminal tabs and work in parallel without stopping to ask me questions—disturb me as little as possible. It ran from 11:00 PM until around 6:00 AM, automatically pausing once it hit half of my weekly quota.

Most of the overnight work involved my GMAT practice platform. The prime example: checking all 18,000+ questions across the platform to ensure not a single question marked a student wrong when their answer was correct.

Next, it called in a second model to re-solve nearly a thousand Critical Reasoning questions. It surfaced only the items where both models disagreed, narrowing the pile down to just eight questions that actually needed my review.

When I woke up, Claude had distilled everything requiring my decision into ten numbered points. I cleared them in one pass and deployed what was ready.

I applied the same logic to the rest of my expiring marginal compute:

**One-time cloud credits:** Auditing course materials. The $250 credit worked only in cloud sessions and did not recur. I used it to audit my Claude Code course syllabus, comparing each section against official documentation to catch errors and outdated references. It caught 11 issues, which I reviewed and fixed. Because the cloud environment cannot access my local files or credentials, I felt comfortable letting it run wide-ranging checks.

**Monthly API promotional credits:** Running daily recurring reports. Every morning, an AI generates my daily briefing and gathers newsletter material—tasks that used to eat into my subscription quota. I moved them over to the $100 monthly API promo bundled with Max. Running those schedules costs roughly $36 a month, and spot-checks confirmed output quality held up. That keeps my interactive subscription quota open for daytime work.

**Bundled Colab compute:** Training local models. I burned Google's Colab credits training small models to see if they could replace paid services on my local machine. The speech-to-text model succeeded and went into daily use. A model meant to imitate my writing voice lost a blind test against my prompt setup, so I deleted it. I also tested an open-source AI video model and put together a 44-second dialogue clip.

**Testing new models on real tasks:** When Haiku 5.5 came out, I built a 13-question benchmark using my actual day-to-day tasks, spending about $15 in compute. For error-checking tasks, Haiku performed just as well as the flagship models at roughly one-tenth the cost. From then on, I routed all routine verification to it.

## Using Surplus Compute to Build Permanent Token Savings

Burning expiring quotas is just the tactic; the real payoff is using that extra compute to build assets that permanently reduce future token consumption.

**Hand cheap work to cheap models:** Verification goes to Haiku, coding and bug-finding go to Codex, long documents go to Google's models, and anything runnable locally runs overnight on the Mac mini. Whichever route gets stuck rolls back to Claude.

**Trim what the AI reads on every turn:** Before each turn, the model reads through instructions, background context, and project rules—and the more it reads, the more it costs. I tackled this in two ways: first, setting long conversations to auto-compact earlier, which reduced tokens read per turn by about 30%; second, splitting task-specific rules into on-demand skills loaded only when needed. In my public starter kit, the baseline instructions read on every prompt dropped by more than 80%.

Looking at the numbers over two 11-day windows, setting automatic compaction for Opus 5.5 at 400k produced these results:

![Table: Opus 5.5 costs across two 11-day periods (Oct 8 to Oct 19); actual post-change total was $1,007 to $1,234 versus an estimated $1,293 to $1,462 without compaction, saving $228 to $286 (16% to 22%), primarily on cache reads, projecting to $620-$780 in 30-day savings](/blog/assets/posts/burn-and-save-ai-quota/compact-400k-cost.jpg)

![Table: Comparing 11 days before and after, compaction frequency jumped from 1.6 to 10.0 per 100 messages, correction rates showed no significant difference (2.4 vs 1.4), post-compaction correction rates matched baseline, and manual /compact calls dropped from 12 to 1](/blog/assets/posts/burn-and-save-ai-quota/compact-400k-metrics.jpg)

Here is why this saves so much: every call resends the entire conversation context. Once 1M context arrived without an automatic compaction ceiling, a conversation stretching to 500k tokens meant even a brief reply consumed 500k tokens. I wrote up the full backstory in my [quota incident log](/blog/posts/en/claude-code-quota-incident-log).

I find 400k to be the sweet spot.

**Piling on rules slows things down:** On October 21, I felt Opus was getting sluggish, so I asked Claude to review the day's transcripts. The model hadn't degraded; my own new rule ("outsource whenever possible") was clashing with existing guidelines. I dropped that rule and replaced it with a simpler directive: "If I am waiting on it, finish it the fastest way possible."

**Stop configuration drift:** Because I use Claude Code and Codex side by side, their configuration files easily drift apart. Similarly, knowledge-base notes often documented the same topic in two places, leaving one updated and the other stale. Now, automated schedules run weekly diffs, reconcile changes, and automatically roll back if an edit breaks.

**Automate daily recurring tasks:** I currently have 17 scheduled jobs running on my machine every day, such as:

- Drafting Reddit replies each morning, so I only have to pick which ones to post
- Generating a diagnostic deck the moment a student's new score report arrives
- Writing a bug fix automatically when my platform throws an error, queued for review
- Automatically resuming long tasks paused by quota limits once the window resets, notifying my phone on completion
- Picking unattended tasks to run automatically before the Sunday reset if excess quota remains

These jobs only take things to "ready for review." Anything sent outward or published still waits for my confirmation.

**Identify repeated instructions:** I had Claude analyze over a thousand prompts I sent across two weeks to pinpoint instructions I kept repeating. It surfaced eight workflows worth automating, which I have been implementing one by one.

**Never trust an AI claiming "I checked it":** In one scheduled run, the model claimed it verified every link when it hadn't executed a single check. Now, automated verification scripts handle those checks directly; if an AI claims it validated something without leaving a log, the pipeline blocks it.

Taken together, these adjustments produced these structural results:

| Outcome | Plain English | Current Status |
|---|---|---|
| Cheaper routine work | Verification shifted to budget models, cutting cost to about one-tenth | Tested in production |
| AI reads less per turn | Context read reduced by ~30% per interaction, saving over $600/month equivalent | Verified before/after |
| Preserving daytime quota | Daily reports shifted to monthly API promotional credits (~$36/month) | Running smoothly for days |
| Less to remember | Reddit replies, newsletters, score diagnostics drafted automatically | Active in production |
| Shorter backlog | "Someday/maybe" tasks pruned from 61 items to 1 actionable task | Active in production |
| Aligned tools | Configuration drift between Claude Code and Codex reduced to zero | Fully reconciled |

![Before and after token savings: baseline startup instructions reduced by over 80%, per-conversation reading dropped about 30%, verification costs cut to one-tenth, and the actionable backlog pruned from 61 items to 1](/blog/assets/posts/burn-and-save-ai-quota/3-before-after.jpg)

Some payoffs take time to show up. I scheduled review check-ins for October 29, November 6, and November 18, tracking two metrics: is token spend actually dropping, and are tasks I am waiting on finishing faster? If numbers don't improve, I iterate.

## From Static Benchmarks to Dynamic Quota-Based Dispatching

By November 2026, my approach to task delegation and quota allocation went through another evolution.

Inside the terminal tool I use to manage multiple AI tabs, I put together a simple quota dashboard. I am not open-sourcing it because it is dead simple—show the screenshot to any model and it can build it in five minutes.

But the visual dashboard is just the front end; what matters is the routing script plugged into it. When delegating tasks, the primary orchestrating AI checks real-time quota balances alongside benchmarked model strengths to decide who gets the job and how much reasoning effort to dial in.

Which makes it hard to understand why people love trashing the CLI to praise desktop apps. Terminal setups give you the highest customizability, keep your hands on the keyboard, and use fewer resources. Any new feature lands on the CLI first before desktop apps catch up. Desktop apps are fine for ease of use and clean aesthetics, but there is really no need to play favorites and tear down the alternative.

Still, after running that benchmark-driven routing for a few days, I decided to scrap it.

My original method was turning my daily tasks into a benchmark suite, testing every tier whenever a model updated, and setting dispatch rules based on quota consumption, execution speed, and output quality. But that approach ran into two problems:

1. Models iterate so quickly now that re-running benchmarks every time simply isn't cost-effective.
2. Quotas across providers still weren't getting fully utilized before their reset windows.

That sparked a new idea:

1. Drop the benchmarks and predefined roles altogether, and route purely on quota availability. Dispatch first to whatever model has remaining quota closest to its reset window, with the primary orchestrator handling final verification. That makes full use of every provider's allowance.
2. Because reset windows rotate on different schedules, active usage naturally distributes tasks across models, building up a balanced dataset over time.
3. At the end of the week, review the conversation logs to measure each model's actual success rate, token consumption, and runtime. That gives you an empirical view of which model fits which task, letting you write grounded dispatch rules. Anything that lacked data becomes the focus for the following week.

This feels like the kind of insight only Anthropic's flagship Fable model would dream up! (Flattering myself here.) Human creative thinking still matters most after all.

## Reusable Prompts to Copy

Every step above was handled through conversational prompts with Claude Code without custom software. Below are the core prompts you can adapt to your own workflow.

**Step 1: Audit.**

> Open a browser, visit the usage and billing pages for each of my AI subscriptions, and summarize the remaining balance, reset cadence, expiration date, and supported tools into a table. If a metric cannot be found, mark it as "Not available" instead of guessing. Finally, highlight any quota expiring within the next 30 days.

**Step 2: Decide what to run.**

> Categorize my backlog and long-term projects against three questions: 1. Will the allocated quota expire soon? 2. Can the output be verified automatically by tests or linters without me reading every line? 3. Does completing it leave reusable tools or rules for future work? Prioritize tasks that pass all three questions, and list them for me to choose from.

**Step 3: Let it run autonomously.**

> Run this batch on your own while I sleep. Do not pause to ask me questions. Rules: Stop once weekly quota usage reaches 50%. Self-verify each task upon completion; if verification was not run, explicitly mark it as "Not verified." Do not perform any outbound messaging, data deletion, or billing changes—queue those for my review. Keep all changes on isolated branches; do not merge.

**Step 4: Morning review.**

> List everything completed overnight. For each item, include how you verified it, the test results, and any pending decisions that require my sign-off. Number each pending decision so I can review and approve them in a single reply.

**Step 5: Cut ongoing consumption.**

> Scan my conversation history from the past two weeks, identify tasks I repeated more than three times, and rank the top five best candidates for automation, noting roughly how many manual interventions each would eliminate.

> Review my persistent configuration files (CLAUDE.md, system rules) and identify sections only relevant to specific tasks. Move them into on-demand skills, leaving behind only a single-line pointer in the persistent rules.

> I want to route verification tasks to cheaper models. Create 10 benchmark test cases drawn from my actual daily work, and run both the budget and flagship models through them. Only switch if scores match; if quality drops, keep the original routing.

> Ensure every scheduled automation has an alerting mechanism on failure. For automations using external models, automatically fall back to Claude once quotas are exhausted.

## Practical Guardrails and Boundaries

When running this system, keep several practical boundaries in mind:

First, managing leftover balances:

- **Console promo:** Three scheduled jobs consume roughly $40 a month, leaving about $60 to expire each cycle. Before November 9, I check the balance and burn the remainder on batch jobs using the Batch API.
- **Colab CUs:** Around 135–185 CUs expire by November 18. Following my priority queue, I first re-transcribe older recordings using the newly trained speech model, then offload synthetic queries for retrieval models onto Colab.
- **Cloud credits:** Expiring November 5, this is a one-time pool, so I won't build permanent automations around it. When local quota runs tight, I use it for large batch jobs that don't need local credentials.
- **Codex:** Because it resets unpredictably, I don't micromanage the balance—I just use it whenever available. The hard rule is that outputs must be verifiable by tests or reviewed by Claude.
- **Local idle window:** The 02:15–05:45 early morning block runs rough transcription processing, document classification, and de-identification—resumable batches that will get a second human review later anyway.

Second, avoid subscription anxiety. I never spend compute just to hit zero. Rushing to max out usage before a reset is usually a trap built into subscription pricing, which I covered in [how to pick a subscription](/blog/posts/en/claude-code-plan-picker). If no tasks qualify under the decision filters, let the quota expire.

Finally, maintain strict safety guardrails for automation. Any task running autonomously overnight or in the background must work on an isolated branch and open a draft PR—automatic merging is banned. Any outbound messages, emails, social posts, data deletion, or billing changes require explicit human approval; the AI must stop at "ready for review."

That's it.

## Appendix

Details regarding the internal tools and technical environment referenced in this article:

- **Terminal multiplexer and dashboard:** The "terminal tool for running multiple AI tabs" refers to Herdr. The custom quota dashboard pulls real-time window balances from each model provider for backend routing scripts to read.
- **Dispatch and orchestration architecture:** The "primary commanding AI" refers to the main interactive session; "reasoning effort" corresponds to each model's native reasoning budget. All code generated by external dispatches runs on isolated branches and undergoes test validation before final acceptance by the main session.
- **Models and environment guardrails:** Fable refers to Anthropic's flagship reasoning model; Google AI Pro quota is called via a dedicated CLI tool (agy); local models running overnight batches (02:15–05:45) on a Mac mini use memory and swap guardrails to prevent resource exhaustion from freezing the host.

<!--
2026-10-26 拼接順稿：
- 「具體算一下前後 11 天的帳：我把 Opus 5.5 的自動壓縮設在 400k，前後各 11 天比較下來是這樣：」— 類型：銜接
移除「補充：自動壓縮改 400k」拼貼標題，將前後 11 天數據段落移至「拿來省額度的那一半」的「讓 AI 每次少讀一點東西」底下。

2026-11-12 併入：
- 「到了 2026 年 11 月，這套額度分工跟派工方式又改了一輪。」— 類型：銜接
- 「我在自己用來開多個 AI 分頁的終端機工具裡」「負責指揮的主要 AI」「思考強度要開多少」— 類型：定義（將 Herdr、主線、effort 改為白話）
- 「不過這套靠 benchmark 決定分工的做法，跑沒幾天我就決定改掉了。」— 類型：銜接
- 「這種靈感是 Anthropic 最頂級的 Fable 模型才會想出來的吧！（自誇）」— 類型：定義（補充 Fable 為 Anthropic 最頂級模型）
在收尾提示詞章節前新增「額度儀表板接上路由腳本，再從預跑 benchmark 改成按額度派工」H2 章節，依時序串接 P13 額度儀表板與路由腳本、P118 捨棄預跑 benchmark 改按剩餘額度派工與事後統計紀錄。

2026-11-12 整篇重寫：
重構全文敘事主軸，將零散拼貼的貼文融為一體，以額度盤點、夜間燃燒、結構性省額度、動態派工演進貫穿，並將技術細節抽離至附錄。
-->
