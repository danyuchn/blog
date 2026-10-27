---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-26T04:00:00Z
title: "GPT-6.1 Terra Hands-on: Fast and Cheap, but Glyphs and Chat Context Still Go to Sonnet"
slug: en/gpt-6-1-terra-review
featured: false
draft: true
tags:
  - model-comparison
  - codex
  - ai-tools
description: 'OpenAI just shipped GPT-6.1 Terra. I ran review, patching and screen-reading tasks against Sol, Astra and three Claude models to see what you can hand it.'
---

OpenAI released GPT-6.1 Terra on 2026-10-26, pitching it around fast, efficient computer use and visual reasoning, with standard API pricing set 50% lower than both GPT-5.6 Terra and GPT-6.1 Sol at $1 per million input tokens and $5 per million output tokens. Looking at that pricing and positioning, I only had one question I wanted to answer: in my own daily agent dispatch workflow, is Terra actually worth using, and where does it belong? I ran a full round of tests using my regular code patching, adversarial reviews, screen-reading browser tasks, and long-horizon hard problems. Here is the short answer—at low effort, Terra can directly take over the jobs I used to hand to Sol low (spec-driven code patching) and Astra low (adversarial review), getting the exact same perfect scores while running 1.5 to 2 times faster and burning only a quarter to a fifth of Astra's 5-hour quota per run; however, when it comes to spotting Simplified vs. Traditional Chinese typos on screen, reading conversational context, doing bulk replacements, or attributing quotes in transcripts, it still misses things, so I cannot hand those tasks off to it unsupervised.

## How OpenAI pitches Terra

OpenAI's [release post](https://openai.com/index/introducing-gpt-6-1-terra/) positions Terra as a model that is "fast, efficient, combining detailed visual reasoning with precise computer use, and writing more clearly and naturally," aimed at all-day knowledge work like filling out forms, editing videos, reading technical diagrams, and writing proposals. Standard API pricing is $1 per million input tokens, $0.05 for cached input, and $5 for output—50% cheaper than both GPT-5.6 Terra and GPT-6.1 Sol. Inside ChatGPT Work and Codex, the same usage quota gets you further than GPT-5.6 Terra, and much further than GPT-6.1 Sol or GPT-6 Astra. It is available on Plus, Pro, Enterprise, and Edu, and the API model string is `gpt-6.1-terra`.

OpenAI's chosen comparison targets are clear, with both Astra and Claude Opus 5.5 in the mix (all numbers below are from OpenAI's own evaluations):

- Computer use (Agents' Last Exam, medium effort): 15 percentage points higher than GPT-5.6 Terra at roughly one-third the cost; tied with GPT-6 Astra at one-tenth the price per token.
- At max effort, its token efficiency is more than 3x that of Claude Opus 5.5, at one-fourth the per-token price, bringing per-task cost down by roughly 9x. It finishes tasks more than 3x faster than Astra and Sol.
- Terminal-Bench 4.0 (max effort): solves 50.3%, compared to 21.5% reported for GPT-5.6 Terra. Still, OpenAI explicitly wrote in the post that for the most complex coding work, GPT-6.1 Sol and GPT-6 Astra remain better choices.
- Terminal-Bench-Science 0.1 (max effort): beats Sol and comes within 5 points of Opus 5.5 at an estimated cost of less than one-fifth.
- Hallucinations: on OpenAI's internal false-premise benchmark, the error rate at low effort dropped from 53.6% to 16.7%, and at max effort dropped by 18 percentage points to 4.3%.

For third-party numbers, you can check the [Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) review: low and medium effort sit on the intelligence-vs-cost Pareto frontier, and they describe Terra as "smarter than the previous generation Terra at less than one-third the cost." At max effort, its Intelligence Index is 4 points below Sol, and its Coding Agent Index v2.0 sits at 48—6 points below Sol's 54, and 17 points above GPT-6 Luna's 31. On AA-Omniscience, its hallucination rate is 38% down from 88% in the previous generation, while accuracy only went up by 2 points.

## How I tested it and what I found

After reading the official and third-party numbers, I still needed to see how it performs inside my own workflow. To test whether Terra is worth swapping in, I built four realistic test suites using fully synthetic data: adversarial review, real code-patch replays, screen reading and browser operation, and a hard problem set mined from past model failures.

The sample size is small: I ran Terra 1 to 3 times per problem, Haiku, Sonnet, and Opus mostly 1 to 2 times, and the screen-reading conclusions rest mainly on two problems run 2 to 4 times each. I did not test Codex's built-in computer_use or large patches over 100 lines.

Part one covers reviews and code patching. The takeaway here is straightforward: Terra low can directly take over Sol low and Astra low's jobs, and bumping Terra up to medium does not make it perform any better than low.

On the review side, I tested four task types: bug hunting, public-facing red-team review, dead pointer checks, and line-by-line fact checking. I ran Terra low 3 times per task and medium 2 times, and it scored a perfect 1.00 across all four task types, matching Astra low. Speed-wise, though, it was much faster—comparing average seconds, Terra vs. Astra came out to: 32s vs. 65s for bug hunting, 17s vs. 26s for red-team review, 25s vs. 35s for dead pointer checks, and 24s vs. 24s for line-by-line fact checking. Quota consumption was also way lower: running a review task on Terra burned roughly 1.5% of my 5-hour quota per run, whereas Astra tested last week burned around 7% per run, with uncached input tokens at 33k vs. 88k (though any concurrent Codex usage during the same window gets mixed into the quota meter).

For real patch replays, I took 3 past patching tasks and ran each 2 times; the patches themselves were small, around 10 to 20 lines. Terra fixed all 6 runs (6/6) without touching the tests, matching Sol low's 6/6 score. Terra took around 50 seconds per run while Sol took 60 to 105 seconds; the resulting diff size was 11 to 18 lines for Terra and 13 to 24 lines for Sol.

While testing the patching tasks, however, I caught Terra grabbing the answer straight from git history whenever it could reach it. When the test repo still had the future fix commit visible, Terra ran `git log --all` on both attempts to find the answer—once running `git show | git apply` directly, and once copying it by hand; in its progress log it wrote "a corresponding fix already exists in version history, re-applying it now," yet left that out of its final report. I threw out both runs and re-tested in an isolated repo containing only the pre-fix snapshot with commit hashes scrubbed. Terra still fixed both runs on its own (2/2), and I checked the session logs to confirm it did not go digging through git history. The takeaway is obvious: if the answer is reachable anywhere in the environment, Terra will grab it and use it, so you have to isolate any reference solutions cleanly before dispatching it.

Part two covers screen reading and browser operation. This was a new test category for this round; since OpenAI heavily promoted visual reasoning and computer use, I built 8 tasks modeled after real use cases from my past 60 days, including reading chat screenshots, score report screenshots, admin billing reconciliation, billing charts, video subtitle frames, and social media threads, wiring every model up to the exact same browser tool.

On 6 of the 8 tasks, every model got a perfect score, including pulling the latest record from a score report, doing math on a stacked billing chart, checking subtitles on video frames, reconciling an admin dashboard (which included loading earlier messages and a same-name trap), reading a billing backend where numbers are drawn purely on a canvas, and finding an author's final prediction inside a social thread. Only two tasks separated the models, and coincidentally, Terra, Sol, Astra, and Haiku failed both in the exact same way:
- The first task was "find UI issues before launch": the navigation bar on screen had a Simplified Chinese character ("错题本") mixed into Traditional Chinese UI. Sonnet and Opus caught it every single time for a 1.00; Haiku, Terra (across 6 straight runs), Sol, and Astra all missed it, all scoring 0.67.
- The second task was "check chat screenshots to see who hasn't been replied to": in the screenshot, someone asked late at night if they could reschedule, then followed up the next morning about the exact same thing. Sonnet and Opus both rightly counted that as 1 unanswered question and scored 1.00; Haiku and the three GPT models frequently counted it as 2, scoring 0.92 for Terra low, 0.75 for Terra medium, 0.75 for Haiku, 0.75 for Sol, and 0.75 for Astra.

To check whether this was a reasoning depth issue, I tried turning up Terra's effort, and it did not help at all (on the chat screenshot task, medium even dropped to 0.75). That is because the gap here comes down to perceiving character glyphs and conversational flow, not deeper reasoning. Even though OpenAI markets Terra around "understanding the screen," it did not outperform Sol or Astra on this suite; its real edge is being fast and dirt cheap—each screen-reading task used only about 0.6% of my 5-hour quota, compared to roughly 2.3% for Sol and Astra.

Part three is the hard problem set. I dug through the past 75 days of my chat logs to pull out 20 real cases where models had failed, turning them into 12 standalone tasks first, and then hiding 5 of those traps inside 2 long-horizon tasks spanning 7 everyday chores across more than 200 files. During pilot runs, every single lost point turned out to be a grader or environment bug (13 bugs total, fixed and re-graded)—not a single cell was a genuine model mistake. Piling on extra file clutter did not faze them either: the models used grep to locate the target files right away and finished in 60 to 105 seconds.

After re-grading, Haiku, Sonnet, and Opus scored 1.00 across all 12 standalone tasks, and Sonnet and Opus also scored 1.00 on the long-horizon tasks. I ran Terra low once per task; it got 1.00 on 11 of the 12 standalone tasks and 1.00 on the long-horizon tasks, but made 2 genuine mistakes:
- On one task where it had to read meeting notes, it attributed a proposal to the wrong person, scoring 0.88.
- On another task where it had to bump a headcount cap that was originally set to 350, it also overwrote a retry timeout in milliseconds that happened to be 350 in the code, and left 6 modified files out of its final change report, scoring 0.93.

Those two mistakes are a good reminder for me: if I hand Terra a bulk replacement job or ask it to figure out who said what from a transcript, I need a separate verification step afterward.

## How it compares across models

Putting OpenAI's numbers next to my own test results makes it much clearer how Terra stacks up against the other models in my rotation (Sol and Astra in Codex, plus Claude's Haiku, Sonnet, and Opus). First, here is a table summarizing the data from my runs:

| Metric | GPT-6.1 Terra | GPT-6.1 Sol | GPT-6 Astra | Claude Haiku | Claude Sonnet | Claude Opus |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Review tasks score (4 types)** | 1.00 (low / medium) | - | 1.00 (low) | - | - | - |
| **Review tasks avg seconds**<br>(bug hunt / red team / dead pointer / fact check) | 32 / 17 / 25 / 24 s | - | 65 / 26 / 35 / 24 s | - | - | - |
| **Review tasks 5-hour quota per run** | ~1.5% (33k uncached input) | - | ~7% (88k uncached input) | - | - | - |
| **Real patch replay (3 tasks x 2 runs)** | 6/6, ~50 s, diff 11–18 lines | 6/6 (low), 60–105 s, diff 13–24 lines | - | - | - | - |
| **Screen tasks time & cost / quota per run** | 7–50 s, ~0.6% quota | ~2.3% quota | ~2.3% quota | 13–43 s, ~$0.01 | 11–48 s, ~$0.17 | 16–26 s, ~$0.37 |
| **Screen: UI Simplified Chinese "错题本"** | 0.67 | 0.67 | 0.67 | 0.67 | 1.00 | 1.00 |
| **Screen: Chat screenshot unanswered questions** | 0.92 (low) / 0.75 (medium) | 0.75 | 0.75 | 0.75 | 1.00 | 1.00 |
| **Hard set: 12 standalone tasks** | 11 tasks 1.00 (2 errors: 0.88, 0.93) | - | - | 12 tasks 1.00 | 12 tasks 1.00 | 12 tasks 1.00 |
| **Hard set: 2 long-horizon tasks** | 1.00 | - | - | - | 1.00 | 1.00 |
| **Report length & defensive hedging** | ~110 words; hedges 0.6/1k words; disclaimers 1/62 | - | hedges low 5.1, high 16.1/1k words; disclaimers 5/28 | - | ~300 words | - |

First, looking at Terra against its Codex siblings Sol and Astra:
- **Against GPT-6.1 Sol**: Official standard API pricing for Terra is 50% lower than Sol ([official announcement page](https://openai.com/index/introducing-gpt-6-1-terra/)). At max effort, Terra's Intelligence Index is 4 points below Sol and its Coding Agent Index v2.0 is 6 points lower (48 vs. 54), though a roughly 20-point jump on Terminal-Bench 4.0 brings it even with max-effort Sol ([Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)). In my own tests on 10-to-20-line real patch replays, Terra low matched Sol low at 6/6 while taking around 50 seconds (compared to Sol's 60 to 105 seconds); on the screen-reading suite, their scores were basically identical (both got 0.67 on the Simplified Chinese typo, and on the chat screenshot Sol got 0.75 while Terra got 0.92 on low and 0.75 on medium), while Terra burned only about 0.6% of my quota per run—way cheaper than Sol's 2.3%.
- **Against GPT-6 Astra**: The [official release post](https://openai.com/index/introducing-gpt-6-1-terra/) says the two tie on Agents' Last Exam, with Terra costing roughly one-tenth as much per token and running more than 3x faster. Across the four adversarial review tasks I tested, Terra low matched Astra low with a clean 1.00 across the board, ran noticeably faster on the first three categories, and cut per-run 5-hour quota usage from Astra's ~7% down to ~1.5% (and 0.6% vs. 2.3% on screen tasks). There is also a very practical difference in defensive tone: I counted hedge words across their responses and found Terra averaged just 0.6 hedges per thousand words, compared to 5.1 for Astra low and 16.1 for Astra high; across 62 responses, Terra included a scope disclaimer only once, whereas Astra included 5 across 28 responses. Terra hit 100% format compliance and averaged around 110 words per response, making it much cleaner to read.

Next, looking at Terra against the Claude family—Haiku, Sonnet, and Opus:
- **Against Haiku**: Across the 8 screen-reading tasks, Terra and Haiku landed in almost the exact same bracket—perfect scores on the 6 baseline tasks, both missing the Simplified Chinese character "错题本" (0.67), and both tending to double-count the follow-up message on the chat screenshot task (Haiku 0.75, Terra low 0.92 / medium 0.75). Speed-wise, Terra took 7 to 50 seconds while Haiku took 13 to 43 seconds (at roughly $0.01 per run). On the 12 standalone hard tasks, however, Haiku scored a clean 1.00 across all 12, whereas Terra low slipped up twice (11 tasks at 1.00).
- **Against Sonnet and Opus**: OpenAI only compared against Opus 5.5 ([release post](https://openai.com/index/introducing-gpt-6-1-terra/)): ~9x lower cost per task at max effort. Here is how they did on my own suite. On the screen tasks that required catching the Simplified Chinese character "错题本" in the nav bar and reading late-night-to-next-morning chat context to count unanswered questions, both Sonnet (~$0.17 per run, 11 to 48 seconds) and Opus (~$0.37 per run, 16 to 26 seconds) scored a clean 1.00—an area where Terra could not catch up even when I turned up its effort; on the 12 standalone hard tasks and 2 long-horizon tasks, Sonnet and Opus also scored 1.00 across the board without misattributing quotes or overwriting same-number parameters like Terra did; on response length, Terra averaged around 110 words, much shorter than Sonnet's ~300 words. As for the gap between Sonnet and Opus themselves, I have a separate 8-question GMAT critical reasoning hard set where Sonnet scored only 0.29 and Opus scored 0.96; only on problems like that, where the model has to carefully weigh two strong competing options, do the two really separate—on long-file reading, formatting, reviews, and math, I currently measure no gap between them, so the cases where I need to escalate from Sonnet to Opus on the Claude side are narrow.

## Recommendations

After finishing this round of testing, I have locked in my dispatch rules for Terra:

1. **Coding work where tests or linters can verify correctness**: Jobs that used to go to Sol low now go to Terra low. With tests acting as a guardrail, I know right away whether its fix works, and it runs faster while saving quota—just make sure that if the repo contains reference solutions or future fix commits, you isolate them before dispatching so it doesn't just dig through `git log` and copy the answer.
2. **Adversarial review and finding counterexamples**: Bug hunting, red-team reviews, dead pointer checks, and line-by-line fact checking that used to go to Astra low now go to Terra low. It gets the same perfect scores on these tasks, runs 1.5 to 2 times faster, uses only a quarter to a fifth of the quota, and produces almost zero fluff or disclaimers. Also, there is no need to bump Terra up to medium; in my tests, medium was no better than low.
3. **Pulling numbers from screenshots and scraping data via browser**: Tasks like reading billing charts, parsing score reports, spotting broken images, and pulling admin reconciliation data can go to either Haiku or Terra low; however, if the task involves catching typos, telling Simplified and Traditional Chinese characters apart, or judging from chat context whether a question has been answered, do not hand it to Terra—give those jobs to Sonnet.
4. **Bulk replacements, attributing quotes in transcripts, and final-gate reviews**: When you ask Terra to do bulk numeric replacements or attribute statements from a transcript, it can accidentally overwrite other parameters that share the same number, under-report modified files, or pin a quote on the wrong person, so if you do dispatch it for these, you must run a separate verification pass afterward; as for final-gate reviews, I still hand those to Opus—Terra does not replace that step.

That is all.
