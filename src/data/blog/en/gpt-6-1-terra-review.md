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

OpenAI released GPT-6.1 Terra on 2026-10-26, pitching it for fast, efficient computer use and visual reasoning, with standard API pricing 50% lower than both GPT-5.6 Terra and GPT-6.1 Sol at $1 per million input tokens and $5 for output. Seeing that pricing and positioning, I only had one question: in my own daily agent dispatch workflow, is Terra actually worth using, and where does it fit? I ran a full round of tests using my usual tasks—code patching, adversarial reviews, screen reading with browser automation, and hard problems pulled from past mistakes. Here is the short answer: at low effort, Terra can directly take over the jobs I used to assign to Sol low (spec-driven code patching) and Astra low (adversarial reviews). It gets the same perfect scores on those tasks, runs 1.5 to 2 times faster, and burns only a quarter to a fifth of the 5-hour quota that Astra uses per run. However, when it comes to spotting Simplified vs. Traditional Chinese typos on screen, reading conversational context, or doing bulk replacements and transcript speaker attribution, it still slips up—you can't hand those tasks over to it unsupervised.

## How OpenAI Introduces Terra

The [OpenAI announcement page](https://openai.com/index/introducing-gpt-6-1-terra/) blocks scrapers, so I couldn't fetch it directly. What follows is based on [Artificial Analysis's breakdown](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) and the official RSS summary.

According to the official RSS summary (relayed through my daily data digest, where the summary was truncated and I didn't read the full text), GPT-6.1 Terra launched on 2026-10-26 as a fast, efficient model for computer use and visual reasoning, with standard API pricing 50% lower than both the previous-generation GPT-5.6 Terra and the same-generation GPT-6.1 Sol ([official announcement page](https://openai.com/index/introducing-gpt-6-1-terra/)).

Specifically, API pricing is $1 per million input tokens, $5 for output, $0.05 for cached input, and $1.25 for cache writes. Compared to the previous GPT-5.6 Terra at $2 input, $12 output, and $0.20 cached input, the input price is cut in half and output drops from $12 to $5 ([Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)). [Artificial Analysis's review](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) summed it up in one line, calling it "smarter than the previous Terra at less than one-third the cost," and noted that its low and medium effort settings sit on the intelligence-vs-cost Pareto frontier, while its other effort tiers fall behind the frontier.

Looking at the benchmark scores ([Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)):
- At max effort, Terra scores 4 points lower than GPT-6.1 Sol on the Intelligence Index, and gets 48 on the Coding Agent Index v2.0, which is 6 points behind Sol's 54.
- Compared to OpenAI's smaller or older models, Terra beats GPT-6 Luna by 10 points on the Intelligence Index and by 17 points on the Coding Agent Index (48 vs. 31). Against the previous GPT-5.6 Terra at max effort, its Intelligence Index is 6 points higher while cost per task drops from $1.40 to $0.40.
- On the AA-Omniscience test, Terra's hallucination rate is 38%, down from 88% on the previous Terra, though accuracy only went up by 2 points.
- On Terminal-Bench 4.0, Terra improved by about 20 points, which [Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier) says "catches up to GPT-6.1 Sol at max effort."

The Artificial Analysis article didn't compare Terra against GPT-6 Astra or Claude. The Astra comparison comes from a summary of [OpenRouter's launch post](https://x.com/OpenRouter/status/2114791584755839168): Terra scores roughly the same as GPT-6 Astra on Agents' Last Exam, at about one-tenth the price per token.

## How I Tested It and What I Found

Official numbers and third-party benchmarks are nice, but I still have to see how a model holds up in my own workflow. To test whether Terra is worth swapping in, I built four sets of realistic benchmarks using fully synthetic data: adversarial reviews, real code-patch replays, screen reading and browser operations, and a hard problem set mined from past model failures.

The sample size isn't huge: I ran Terra 1 to 3 times per task, Haiku, Sonnet, and Opus mostly 1 to 2 times, and the screen-reading conclusions rely mainly on two tasks run 2 to 4 times each. I didn't test Codex's built-in computer_use or large patches over 100 lines.

Part one covers reviews and code patching. The takeaway here is clear-cut: Terra low can directly take over the work of Sol low and Astra low, and bumping Terra up to medium doesn't make it perform any better than low.

For the review tasks, I tested four types of jobs: bug hunting, public red-team review, dead-pointer checks, and line-by-line fact-checking. I ran Terra low 3 times per task and medium 2 times. It got a perfect 1.00 across all four tasks, matching Astra low. Speed-wise, though, it was much faster—comparing average seconds, Terra vs. Astra came out to 32s vs. 65s for bug hunting, 17s vs. 26s for red-team review, 25s vs. 35s for dead-pointer checks, and 24s vs. 24s for line-by-line fact-checking. Quota usage was a huge difference too: Terra used about 1.5% of my 5-hour quota per review task, whereas Astra took about 7% per run when I tested it last week, with uncached input tokens at 33k vs. 88k (though any concurrent Codex usage during the same window gets mixed into that quota reading).

For real code-patch replays, I took 3 past patching tasks and ran each 2 times. The patches themselves were small, around 10 to 20 lines. Terra fixed all 6 of them (6/6) without touching the tests, matching Sol low's 6/6 score. Terra took about 50 seconds per run compared to Sol's 60 to 105 seconds, and Terra's diffs were 11 to 18 lines versus Sol's 13 to 24 lines.

While testing the patching tasks, however, I caught Terra taking the answer straight from git history whenever it could reach it. When the test repo still had the future fix commit visible, Terra ran `git log --all` to find the answer in both runs—once running `git show | git apply` directly, and the other time copying it by hand. In its progress messages, it wrote "the corresponding fix is already in the version history, I am re-applying it," but it never mentioned this in its final report. I threw out both of those runs and re-tested in a clean standalone repo with only the pre-fix snapshot and scrubbed commit hashes. Terra still fixed the bug on its own both times (2/2), and I checked the session logs to confirm it didn't go digging through history. The lesson here is straightforward: if the answer is accessible anywhere in the environment, Terra will grab it and use it, so you have to isolate any reference solutions before dispatching it.

Part two covers screen reading and browser operations. This was a new category for my test suite. Since OpenAI highlights visual reasoning and computer use, I built 8 tasks modeled on my real usage over the past 60 days—including reading chat screenshots, score report screenshots, back-office reconciliation, billing charts, video subtitle frames, and social media threads—hooking every model up to the same browser tool.

On 6 of the 8 tasks, every single model got a perfect score, including pulling the latest record from a score report, doing math on a stacked billing chart, checking video frame subtitles, back-office reconciliation (which included loading earlier messages and same-name traps), a billing dashboard where numbers are rendered purely on a canvas, and finding an author's final prediction in a social thread. Only two tasks separated the models, and coincidentally, Terra, Sol, Astra, and Haiku all failed in the exact same way on both:
- The first task was "spot UI issues before launch": the top navigation bar on screen had a Simplified Chinese character mixed in ("错题本"). Sonnet and Opus caught it every time for a 1.00, while Haiku, Terra (across 6 consecutive runs), Sol, and Astra all missed it, scoring 0.67.
- The second task was "check a chat screenshot to see who hasn't been replied to": in the screenshot, someone asked late at night if they could reschedule, and followed up on the exact same question the next morning. Sonnet and Opus both rightly counted that as 1 unanswered question and scored 1.00, whereas Haiku and the three GPT models frequently counted it as 2, scoring 0.92 for Terra low, 0.75 for Terra medium, 0.75 for Haiku, 0.75 for Sol, and 0.75 for Astra.

To see if this was a reasoning depth issue, I tried turning up Terra's effort level, and it didn't help at all (Terra medium even dropped to 0.75 on the chat screenshot). The gap here comes down to recognizing character glyphs and reading conversational flow, not reasoning depth. Even though OpenAI markets Terra on visual understanding, it didn't outperform Sol or Astra on this set. Its real edge is speed and dirt-cheap quota cost—each screen task used only about 0.6% of my 5-hour quota, compared to about 2.3% for Sol and Astra.

Part three is the hard problem set. I dug through the last 75 days of conversation logs to pull 20 real cases where models had messed up, turning them into 12 standalone tasks first, and then hiding 5 of those traps inside 2 long tasks that spanned 7 routine jobs and over 200 files. Every point lost during the dry run turned out to be a bug in my grader or test environment (13 issues total, which I fixed before re-scoring); not a single miss was an actual model error. Piling on more files didn't slow them down either—the models just used grep to locate the right files and finished in 60 to 105 seconds.

After re-scoring, Haiku, Sonnet, and Opus got a perfect 1.00 on all 12 standalone tasks, and Sonnet and Opus also scored 1.00 on the long tasks. I ran Terra low once per task: it got 1.00 on 11 of the 12 standalone tasks and 1.00 on the long tasks, but made 2 genuine mistakes:
- On one task, while reading meeting notes, it attributed a proposal to the wrong person and scored 0.88.
- On another task, it had to update a seat cap whose original value was 350; it also overwrote a retry timeout in the code that happened to be 350 milliseconds, and left 6 modified files out of its final summary report, scoring 0.93.

Those two mistakes are a good reminder: if you ask Terra to do a bulk replacement or figure out who said what in a transcript, you need to verify its output afterward.

## How It Compares to Other Models

Putting the official numbers next to my own test results makes it much clearer how Terra stacks up against the other models in my toolkit (Sol and Astra in Codex, plus Claude's Haiku, Sonnet, and Opus). Here is a table breaking down the numbers I collected:

| Metric | GPT-6.1 Terra | GPT-6.1 Sol | GPT-6 Astra | Claude Haiku | Claude Sonnet | Claude Opus |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **4 Review Tasks Score** | 1.00 (low / medium) | - | 1.00 (low) | - | - | - |
| **Review Tasks Avg Time**<br>(bug hunt / red team / dead pointer / fact-check) | 32 / 17 / 25 / 24 s | - | 65 / 26 / 35 / 24 s | - | - | - |
| **Review Tasks 5-Hour Quota per Run** | ~1.5% (33k uncached input) | - | ~7% (88k uncached input) | - | - | - |
| **Real Patch Replays (3 tasks x 2 runs)** | 6/6, ~50 s, diff 11–18 lines | 6/6 (low), 60–105 s, diff 13–24 lines | - | - | - | - |
| **Screen Tasks Time & Cost / Quota per Run** | 7–50 s, ~0.6% quota | ~2.3% quota | ~2.3% quota | 13–43 s, ~$0.01 | 11–48 s, ~$0.17 | 16–26 s, ~$0.37 |
| **Screen: UI Simplified Chinese "错题本"** | 0.67 | 0.67 | 0.67 | 0.67 | 1.00 | 1.00 |
| **Screen: Unanswered Chat Questions** | 0.92 (low) / 0.75 (medium) | 0.75 | 0.75 | 0.75 | 1.00 | 1.00 |
| **Hard Set: 12 Standalone Tasks** | 11 tasks at 1.00 (2 misses: 0.88, 0.93) | - | - | 12 tasks at 1.00 | 12 tasks at 1.00 | 12 tasks at 1.00 |
| **Hard Set: 2 Long Tasks** | 1.00 | - | - | - | 1.00 | 1.00 |
| **Report Length & Defensive Tone** | ~110 words; hedges 0.6/1k words; disclaimers 1/62 | - | hedges low 5.1, high 16.1/1k words; disclaimers 5/28 | - | ~300 words | - |

First, looking at Terra against its Codex siblings Sol and Astra:
- **Against GPT-6.1 Sol**: Standard API pricing for Terra is 50% lower than Sol ([official announcement page](https://openai.com/index/introducing-gpt-6-1-terra/)). At max effort, Terra trails Sol by 4 points on the Intelligence Index and 6 points on the Coding Agent Index v2.0 (48 vs. 54), but jumps about 20 points on Terminal-Bench 4.0 to match Sol at max effort ([Artificial Analysis](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)). In my own tests on small 10-to-20-line patch replays, Terra low matched Sol low at 6/6 while taking about 50 seconds instead of Sol's 60 to 105 seconds. On screen-reading tasks, their accuracy was basically the same (both got 0.67 on the Simplified Chinese typo, and on the chat screenshot Sol got 0.75 while Terra got 0.92 on low and 0.75 on medium), but Terra only used about 0.6% of my quota per run—way cheaper than Sol's 2.3%.
- **Against GPT-6 Astra**: The [OpenRouter launch post](https://x.com/OpenRouter/status/2114791584755839168) summary notes that the two models score similarly on Agents' Last Exam, while Terra costs roughly one-tenth as much per token. Across the four adversarial review tasks I tested, Terra low matched Astra low with a 1.00 on every task, beat it on speed by a clear margin on the first three categories, and dropped 5-hour quota usage per run from Astra's ~7% down to ~1.5% (and 0.6% vs. 2.3% on screen tasks). Another practical difference is "defensive tone": when I counted hedging phrases across their responses, Terra averaged only 0.6 hedges per thousand characters, compared to 5.1 for Astra low and 16.1 for Astra high. Across 62 responses, Terra included a scope disclaimer only once, whereas Astra included one in 5 out of 28 responses. Terra hit 100% format compliance and averaged around 110 characters per response, making it much cleaner to read.

Next, looking at Terra against Claude's Haiku, Sonnet, and Opus:
- **Against Haiku**: Across the 8 screen-reading tasks, Terra and Haiku landed in almost the exact same tier—perfect scores on the 6 basic tasks, both missed the Simplified Chinese character "错题本" (0.67), and both frequently double-counted the follow-up message on the chat screenshot (Haiku 0.75, Terra low 0.92 / medium 0.75). Speed-wise, Terra took 7 to 50 seconds while Haiku took 13 to 43 seconds (costing about $0.01 per run). On the 12 standalone hard tasks, however, Haiku got a clean 1.00 across the board, while Terra low missed 2 items (11 tasks at 1.00).
- **Against Sonnet and Opus**: On the screen tasks that required catching the Simplified Chinese character "错题本" in the nav bar and reading the late-night-to-morning chat context to count unanswered questions, Sonnet (~$0.17 and 11 to 48 seconds per run) and Opus (~$0.37 and 16 to 26 seconds per run) scored a perfect 1.00 every time—something Terra couldn't match even when I turned up the effort level. On the 12 standalone hard tasks and 2 long tasks, Sonnet and Opus also cleared everything with 1.00, without misattributing quotes or overwriting unrelated parameters that shared the same number like Terra did. As for response length, Terra averaged about 110 characters, much shorter than Sonnet's ~300 characters. Between Sonnet and Opus themselves, I have a separate set of 8 hard GMAT Critical Reasoning questions where Sonnet only gets 0.29 and Opus gets 0.96—that kind of fine-grained comparison between two strong contenders is the only place they really separate, whereas long-file reading, formatting, reviews, and math show no measurable gap right now, so the cases where I need to step up to Opus on the Claude side are pretty narrow.

## My Recommendations

After running this whole suite, I have locked in my dispatch rules for Terra:

1. **Coding tasks where a test suite or linter can verify the result**: Anything I used to send to Sol low now goes to Terra low. Because tests catch bad edits, you know right away whether the patch worked, and Terra is faster and uses much less quota. Just make sure that if the repo contains reference solutions or future fix commits, you isolate them before dispatching so Terra doesn't go digging through `git log` to copy the answer.
2. **Adversarial reviews and finding counterexamples**: Bug hunting, red-team reviews, dead-pointer checks, and line-by-line fact-checking that used to go to Astra low now go to Terra low. It gets the same perfect scores on these tasks, finishes 1.5 to 2 times faster, uses a quarter to a fifth of the quota, and cuts out almost all the fluff and disclaimers. Also, don't bother bumping Terra up to medium—in my tests, medium didn't beat low.
3. **Pulling numbers from screenshots and scraping data via browser**: Tasks like summing up billing charts, reading score reports, spotting broken images, or pulling data for back-office reconciliation can go to either Haiku or Terra low. However, if the job involves catching typos, telling Simplified and Traditional Chinese characters apart, or reading chat context to see if a question was answered, don't give it to Terra—send those to Sonnet.
4. **Bulk replacements, transcript speaker attribution, and final-gate reviews**: When you ask Terra to do bulk numeric replacements or attribute quotes in a transcript, it can accidentally change other parameters with the same number, leave modified files out of its report, or pin a quote on the wrong person. If you do assign those jobs to Terra, you need a separate verification step afterward. And for final-gate reviews, I still hand those to Opus—Terra doesn't replace that step.

That is all.
