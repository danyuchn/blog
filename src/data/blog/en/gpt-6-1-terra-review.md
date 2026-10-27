---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-26T04:00:00Z
title: "GPT-6.1 Terra Hands-on: Fast and Cheap, but Glyphs and Chat Context Still Go to Sonnet"
slug: en/gpt-6-1-terra-review
featured: false
draft: false
tags:
  - model-comparison
  - codex
  - ai-tools
description: 'OpenAI just shipped GPT-6.1 Terra and says it matches Astra at a tenth of the price. I ran review, patching and screen tasks to see what you can hand it.'
---

OpenAI released GPT-6.1 Terra on October 26, 2026. The standard API costs $1 per million input tokens and $5 per million output tokens, which is half the price of both the previous Terra and the same-generation Sol, focusing on fast, efficient visual reasoning and computer use.

My takeaway: Terra at low effort (low reasoning effort) can take over the code patches I used to send to Sol and the adversarial reviews I used to send to Astra, running faster and using less of my quota. However, catching simplified versus traditional Chinese typos on screen and reading conversation context still need to go to Claude Sonnet.

## How OpenAI presents it

[OpenAI's announcement](https://openai.com/index/introducing-gpt-6-1-terra/) positions Terra as a much improved fast model built for high-volume work like reading invoices and entering line items into accounting software. Plus, Pro, Enterprise, and Edu users can use it starting today; in ChatGPT Work and Codex, the same quota gets more done than the previous Terra, Sol, or Astra.

[![API pricing per million tokens: GPT-6.1 Terra costs $1 for input and $5 for output, while the previous generation Terra costs $2 for input and $12 for output.](/blog/assets/posts/gpt-6-1-terra-review/1-price-en.jpg)](/blog/assets/posts/gpt-6-1-terra-review/1-price-en.jpg)

Here are OpenAI's own tests alongside the third-party evaluation from [Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier):

| Comparison target | Claim |
| --- | --- |
| GPT-5.6 Terra | 15 percentage points higher on computer use at roughly one-third the cost |
| GPT-6 Astra | Matches computer use at one-tenth the unit price and finishes tasks more than three times faster |
| GPT-6.1 Sol | Lower cost and more than three times faster; OpenAI explicitly notes that Sol and Astra remain better for the most complex coding work |
| Claude Opus 5.5 | Roughly 9 times lower cost per task; OpenAI did not compare against Sonnet or Haiku |
| Third-party Artificial Analysis | Smarter than the previous Terra at less than one-third the cost per task |

See the [appendix](#appendix-technical-details) for benchmark names and scores.

## How I tested and what I found

All test items are synthetic data I built myself; I ran each item 1 to 3 times on Terra and mostly 1 to 2 times on Haiku, Sonnet, and Opus. I did not test Codex's built-in computer_use or large patches over 100 lines.

- **Adversarial review**: Four task types: bug hunting, red-team review, dead-pointer checks, and line-by-line fact-checking. Terra scored 1.00 across the board, tying Astra while running 1.5 to 2 times faster and using about one-quarter to one-fifth of Astra's quota per run. [technical details](#appendix-technical-details)

[![Average seconds across four review task types: Terra low is faster than Astra low, and both models score 1.00.](/blog/assets/posts/gpt-6-1-terra-review/2-review-en.jpg)](/blog/assets/posts/gpt-6-1-terra-review/2-review-en.jpg)

- **Code patching**: 3 real bugs patched 2 times each; both Terra and Sol fixed all 6 runs, with Terra taking about 50 seconds and Sol taking 60 to 105 seconds. However, if a reference solution is left in the repo, Terra will find and apply it directly. [technical details](#appendix-technical-details)
- **Screen reading and browser operation**: 8 tasks simulating my real usage over the past two months. All models got full marks on 6 tasks; on the 2 tasks that separated them, Terra, Sol, Astra, and Haiku made the exact same mistakes, while only Sonnet and Opus got everything right. Raising the effort level did not help. [technical details](#appendix-technical-details)

[![The two screen-reading tasks that separated the models: Terra, Sol, Astra, and Haiku are in the same tier, while Sonnet and Opus get full marks.](/blog/assets/posts/gpt-6-1-terra-review/3-screen-en.jpg)](/blog/assets/posts/gpt-6-1-terra-review/3-screen-en.jpg)

- **Past failures and long tasks**: 14 tasks built from real mistakes models made in the past. Terra got full marks on 12 tasks and missed 2: one misattributed a proposal to the wrong person, and one changed an unrelated value during a bulk replacement. [technical details](#appendix-technical-details)

## How it compares across models

| Metric | Terra | Sol / Astra | Haiku | Sonnet | Opus |
| --- | --- | --- | --- | --- | --- |
| Review score | 1.00 | Astra 1.00 | — | — | — |
| Review average seconds | 17–32 | Astra 24–65 | — | — | — |
| Patch tasks (6 runs) | All passed | Sol all passed | — | — | — |
| Screen reading: find simplified Chinese | 0.67 | 0.67 | 0.67 | 1.00 | 1.00 |
| Screen reading: count unreplied messages | 0.92 | 0.75 | 0.75 | 1.00 | 1.00 |
| Screen reading cost per run | ~0.6% quota | ~2.3% quota | $0.01 | $0.17 | $0.37 |

- **Sol**: Passes small patches just the same, while Terra is faster and uses about a quarter of Sol's quota on screen-reading tasks. Patches guarded by tests can move to Terra; save the most complex coding work for Sol.
- **Astra**: Ties on review tasks, while Terra is faster and cheaper. Terra's answers are also more direct, averaging about 0.6 hedging words per thousand words compared to 5.1 for Astra low.
- **Haiku**: Matches Terra on pulling numbers from screens and operating web pages, but Haiku got every past-failure task right, making it steadier than Terra.
- **Sonnet**: Details like simplified Chinese characters and conversation context need to go to Sonnet.
- **Opus**: Scored 100% just like Sonnet on this batch, so there is no need to use it day to day. I have a separate set of 8 hard GMAT critical reasoning questions where Sonnet scored 0.29 and Opus scored 0.96; you only see the gap on tough problems that require weighing two strong options closely.

## Recommendations

[![A routing guide showing which tasks go directly to Terra, which ones need verification, and which ones should go to Sonnet or Opus instead.](/blog/assets/posts/gpt-6-1-terra-review/4-routing-en.jpg)](/blog/assets/posts/gpt-6-1-terra-review/4-routing-en.jpg)

**Hand straight to Terra (at low effort):**
- Code patches where a test suite or linter can verify the result: switch these from Sol to Terra.
- Adversarial review, finding counterexamples, and fact-checking: switch these from Astra to Terra.
- Pulling numbers from screenshots, reading charts, finding broken images, and scraping data from web pages: both Terra and Haiku can handle these.

**Hand to Terra, but verify the output:**
- Bulk replacements and multi-file edits: it once changed an unrelated value that happened to match the target number, and its summary left out modified files, so check the actual diff.
- Figuring out who said what from a transcript: it once attributed a line to the wrong person, so check against the source text.
- Patches in a repo that contains a reference fix: isolate the repo first, or Terra will copy the answer directly.

**Do not hand to Terra:**
- Catching typos, distinguishing simplified from traditional Chinese, and reading conversation context: send these to Sonnet.
- Send the most complex coding work to Sol or Astra; send final-stage reviews to Opus.

## Appendix: technical details

### Review and patching

- **4 adversarial review tasks**: Includes bug hunting, public-release red-team review, dead-pointer checks, and line-by-line fact-checking. Terra ran 3 times per item at low and 2 times at medium, scoring 1.00 across the board to match Astra low; medium offered no improvement over low.
- **Review task average seconds (Terra low vs. Astra low)**: Bug hunting took 32 seconds vs. 65 seconds, public-release red-team review took 17 seconds vs. 26 seconds, dead-pointer checks took 25 seconds vs. 35 seconds, and line-by-line fact-checking took 24 seconds vs. 24 seconds.
- **3 real patch replays**: 2 runs per item, with each patch spanning only 10 to 20 lines (large patches over 100 lines were not tested). Terra low fixed 6/6 without touching the tests, and Sol low also went 6/6. Terra took about 50 seconds per run while Sol took 60 to 105 seconds; patch diffs were 11 to 18 lines for Terra and 13 to 24 lines for Sol.
- **Pitfall encountered (digging through git history for the answer)**: When the future fix commit was still visible in the patch test repo, Terra ran `git log --all` to find the answer on both runs, using `git show | git apply` on one and copying it by hand on the other; its progress log noted "the corresponding fix is already in the version history, I am restoring it," though its final report did not mention this. I threw out both runs and retested in an isolated repo containing only the pre-fix snapshot with commit hashes scrubbed; Terra fixed 2/2 on its own, and the session logs confirmed it did not search git history. In short, if it can reach the answer, it will use it, so isolate any reference solutions before dispatching the task.

### Screen reading

- **Test setup, cost, and time**: 8 tasks modeled on real usage from the past 60 days, with all models operating the same browser tool (Codex's built-in computer_use was not tested). Haiku cost about $0.01 and took 13 to 43 seconds per run; Sonnet cost about $0.17 and took 11 to 48 seconds; Opus cost about $0.37 and took 16 to 26 seconds; Terra took 7 to 50 seconds.
- **6 tasks where every model got full marks**: Pulling the latest score from a transcript screenshot, summing a stacked billing chart, checking subtitles on video frames, reconciling an admin dashboard (including loading earlier messages and handling duplicate names), reading a billing dashboard rendered entirely on a canvas, and finding an author's final prediction in a social thread; all models scored 1.00 on these 6 tasks.
- **2 tasks that separated the models**: Each ran 2 to 4 times, and Terra, Sol, Astra, and Haiku missed in the exact same way:
  - "Pre-launch UI check": The navigation bar had a simplified Chinese character in "错题本"; Sonnet and Opus caught it every time, while Haiku, Terra (across 6 runs), Sol, and Astra all missed it. Scores: Terra 0.67, Haiku 0.67, Sol 0.67, Astra 0.67, Sonnet 1.00, Opus 1.00.
  - "Chat screenshot: who still needs a reply": A contact asked to reschedule late at night and followed up on the same question in the morning; Sonnet and Opus counted 1 unreplied question, while Haiku and the three GPT models usually counted 2. Scores: Terra low 0.92, Terra medium 0.75, Haiku 0.75, Sol 0.75, Astra 0.75, Sonnet 1.00, Opus 1.00.
- **Impact of reasoning effort**: Raising Terra's effort did not help because the gap comes down to recognizing character shapes rather than reasoning. Visual understanding is a headline feature for Terra, but on this set it was no stronger than Sol or Astra; its advantage is speed and cost.

### Hard problem set

- **Task design**: I pulled 20 real mistakes models made over the past 75 days of conversations, turned them into 12 standalone tasks, and hid 5 traps inside 7 routine chores across a 200-plus-file repo for 2 long tasks.
- **Model scores**: Haiku, Sonnet, and Opus scored 1.00 on all 12 standalone tasks, and Sonnet and Opus scored 1.00 on the long tasks. Terra low ran once per item, scoring 1.00 on the long tasks and 1.00 on 11 of the 12 standalone tasks, with 2 real mistakes:
  - One task misattributed a suggestion to the wrong speaker, scoring 0.88.
  - Another task updating a quota cap of 350 also changed a retry timeout that happened to be 350 milliseconds, scoring 0.93 and omitting 6 modified files from its final report.
- **Environment calibration and limits**: During pilot runs, every lost point came from bugs in the grader or test environment (13 issues total, all fixed and re-scored) rather than model mistakes. Adding workload to this set did not make it harder because the models used `grep` to jump straight to the relevant files and finished in 60 to 105 seconds. Real mistakes happen when a conversation gets long, context gets compacted, and several tasks are running at once, which a single headless test run cannot reproduce.

### Quota usage and response style

- **5-hour quota and token counts**: On review tasks, Terra used about 1.5% of the 5-hour quota per run compared to about 7% for Astra, with uncached input tokens at 33k vs. 88k. On screen-reading tasks, Terra used about 0.6% while Sol and Astra used about 2.3%.
- **Hedging and word counts**: Terra averaged about 0.6 hedging words per thousand words, compared to 5.1 for Astra low and 16.1 for Astra high; Terra included a scope disclaimer in only 1 of 62 responses, while Astra included one in 5 of 28 responses. Terra followed formatting instructions 100% of the time and kept its answers short, averaging about 110 words compared to about 300 words for Sonnet.

### Official and third-party benchmarks

Here are the internal test numbers published in [OpenAI's official announcement](https://openai.com/index/introducing-gpt-6-1-terra/):

- **Agents' Last Exam** (a professional task benchmark, such as turning architectural drawings into 3D models): Medium effort beats GPT-5.6 Terra by 15 percentage points at roughly one-third the cost, and matches GPT-6 Astra at one-tenth the price per token.
- **Efficiency vs. Claude Opus 5.5**: At max effort, Terra is more than 3 times as token-efficient as Claude Opus 5.5 at one-quarter the price per token, bringing the cost per task down by roughly 9 times.
- **MMMU-Pro and OSWorld 2.1**: MMMU-Pro visual reasoning beats GPT-5.6 Terra at every effort level and nearly matches Astra and Sol at a much lower cost; OSWorld 2.1 at medium effort beats GPT-5.6 Terra's best score at a fraction of the cost per task.
- **Internal hallucination bait set**: At low effort, the error rate drops from 53.6% (GPT-5.6 Terra) to 16.7%, a reduction of nearly 37 percentage points; at max effort, it drops by 18 percentage points to 4.3%, close to Astra and Sol.
- **Terminal-Bench 4.0 and Terminal-Bench-Science 0.1**: Terminal-Bench 4.0 (max effort) solves 50.3%, more than double GPT-5.6 Terra (21.5%); Terminal-Bench-Science 0.1 (max effort) beats Sol at a lower cost and trails Opus 5.5 by less than 5 points at an estimated cost of less than one-fifth.
- **Safety threshold**: Meets the Preparedness Framework's Critical threshold for cybersecurity and carries over Astra's safeguards; OpenAI states that it stays within task scope better than GPT-5.6 Terra, states limits and blockers more honestly, and performs strongly on prompt injection tests.

Here are the numbers from the third-party [Artificial Analysis evaluation](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier):

- **Price per million tokens (GPT-6.1 Terra vs. GPT-5.6 Terra)**: Input is $1 vs. $2, output is $5 vs. $12, cached input is $0.05 vs. $0.20, and cache write is $1.25. Low and medium effort sit on the intelligence-vs-cost Pareto frontier, while the other effort tiers sit behind the frontier.
- **Intelligence Index and Coding Agent Index v2.0 (max effort)**: Intelligence Index trails Sol by 4 points; Coding Agent Index v2.0 scores 48, which is 6 points behind Sol (54), 17 points ahead of GPT-6 Luna (31), and 6 points ahead of the previous Terra at a per-task cost of $0.40 vs. $1.40.
- **AA-Omniscience and Terminal-Bench 4.0**: AA-Omniscience hallucination rate is 38% (down from 88% in the previous generation) while accuracy rises by only 2 points; Terminal-Bench 4.0 improves by about 20 points.

That is all.
