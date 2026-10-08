---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-08T01:00:00Z
title: Can Haiku 5.5 Take Over Sonnet's Work? I Tested It on My Own Tasks
slug: en/haiku-55-own-task-benchmark
featured: false
draft: false
tags:
  - claude
  - model-comparison
  - ai-workflow
description: 'Instead of official benchmarks, I built a test from 761 sub-agent jobs I actually delegated over 45 days. On seven checking tasks Haiku 5.5 matched Sonnet and Opus at about a tenth of the cost; long transcript extraction is still not complete enough.'
---

Haiku 5.5 came out yesterday. Official pricing is $0.10 per million input tokens and $0.50 per million output tokens (up to 100k), against $2 and $10 for Sonnet 5.5.

The launch page itself says Sonnet and Opus are still better for complex agentic coding. What I care about is the work I hand to sub-agents every day, and whether it can actually handle that.

So I skipped the official benchmarks this time and built the test out of my own work.

![Cover card: on seven checking tasks Haiku 5.5 scored the same as Sonnet at one eleventh of Sonnet's cost](/blog/assets/posts/haiku-55-own-task-benchmark/card-1-cover.jpg)

(If you just want to run it on your own tasks, I turned the method into a public kit. It is at the end.)

## Where the questions came from

I had Opus go through the last 45 days of my Claude Code history. In that window I delegated to a sub-agent 761 times, mostly to Sonnet, a bit over a hundred times to Opus.

From those I picked the 8 kinds of jobs I delegate most often that also have a checkable answer, and turned them into 8 questions:

1. Long transcript extraction (a 62-minute interview, every item must quote the original verbatim)
2. Fact-checking a draft (13 claims, 5 of them planted wrong)
3. Red-teaming a public newsletter (planted client names, internal codes, numbers that don't match, outcome promises)
4. Finding dead links in documents
5. Counting a CSV of delegation records (timestamps in UTC, the question asks for Bangkok time)
6. Finding bugs in a validation script (3 planted)
7. Payment reconciliation (month boundary by time zone, partial refunds, failed charges)
8. End-of-session filing: which file each to-do goes into, and in what format

Plus the 5 easy questions I used on 9/29 for the older models, to check the basics haven't slipped.

Every answer key was computed before any model ran. Haiku ran 3 times each at medium and high effort, Sonnet 5.5 twice, and Opus 5.5 once as the ceiling. 87 runs in total, about $15.

## Results

On the 5 easy questions, Haiku got everything right at all three effort levels, at about 1 cent per question. On 9/29 the old Haiku 4.5 was about 9 cents per question and Sonnet 5.5 about 15 cents.

On questions 2 through 8, Haiku got everything right, same as Sonnet and Opus, except one run where it hit a permission block and handed in nothing (more on that below).

Total cost across those seven:

| | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|
| Seven questions, one run each | $0.17 | $1.94 | $4.24 |
| Seven questions, total time | ~300 s | ~300 s | ~300 s |

The scores matched and the speed was about the same, at roughly one eleventh of what Sonnet cost.

![Bar chart of total cost for seven checking tasks, one run each: Haiku 5.5 $0.17, Sonnet 5.5 $1.94, Opus 5.5 $4.24](/blog/assets/posts/haiku-55-own-task-benchmark/card-3-cost.jpg)

The one that surprised me most was question 6, finding bugs. I used to send that kind of work to Opus. Haiku ran it three times at medium and three times at high, and all six runs caught all three bugs.

## The one it didn't pass: long transcript extraction

Question 1 is the exact task the old Haiku failed on 10/3. Back then, 6 of its 44 quotes could not be found in the original, and it reported that everything matched word for word.

This time all four models passed the quote check. Nothing was made up, which is a big step up.

But it pulled out a lot less. Haiku's six runs pulled out anywhere from 45 to 85 items. Sonnet's two runs got 93 and 99, Opus got 112. Turning Haiku up to high did not reliably help.

With transcripts, there is no program that can tell you what got left out, so I'll keep giving this kind of work to Sonnet.

## A small quirk

During the test I locked permissions down hard: on the calculation questions it was only allowed to run python3. About half the time Haiku reached for wc, cd or mkdir, or chained several commands together, and got blocked. Sonnet never did.

Most of the time it found another way around, but the extra turns made the same question cost 6 times as much. Once, it got blocked a single time and just handed in nothing.

Normal delegation isn't locked down this tightly, so you probably won't run into it much. But when I spelled out which commands it could use and reran it, three runs out of three were correct, at a bit over 1 cent each.

## How I split the work now

Last week I wrote about [Opus commanding, Sonnet implementing, Fable advising](/blog/posts/en/opus-sonnet-fable-division-of-labor). This adds one more layer:

1. Work whose answer can be checked against something (looking up settings, checking numbers, reviewing copy against rules, finding dead links, reconciliation, counting) goes to Haiku first
2. Extraction that only works if it is complete, writing, and end-of-session jobs that edit files and commit stay with Sonnet
3. Security, the final pass on code review, and the last call on anything involving money stay with Opus

Anything I haven't written a question for stays where it was. I'm not extrapolating from this round.

## The grader broke too

By the way, the thing that broke most often in this test was the grading script I wrote myself.

Once, it only read the last message. A stop check forced the model to reply one more time with "same as above," so a correct answer got scored as zero. Once, on the red-team question, it counted extra findings as false positives automatically; I read them one by one and every one of them held up. And once, while matching answer lines, it picked up an explanation line that also happened to contain "Q2."

All three times the model was right and the grader was wrong. So after the scores came out, I opened the original output for every run that wasn't a perfect score.

## Test it on your own work

I packaged this method as a public kit: [model-bench-kit](https://github.com/danyuchn/model-bench-kit).

There is no ready-made test inside. Your agent reads it, then goes through your own conversation history, finds the work you actually delegate, writes the questions, computes the answer keys, runs and grades everything, and finally rewrites your own delegation rules.

It ships with three examples built on synthetic data so you can get the pipeline running first. When the next model comes out, add one line of config and run it again.

If you want to try it:

1. If you use Claude Code, clone the repo into `~/.claude/skills/model-bench`
2. Tell it: "Use model-bench to test whether Haiku 5.5 can take over the work I usually give Sonnet"
3. It estimates how many runs and how much money first, and only starts once you say yes

If you don't use Claude Code, just give your agent the [repo link](https://github.com/danyuchn/model-bench-kit) and tell it to read SKILL.md and follow it. Once you've run it, come back and tell me what you got.

The most expensive test-taker in the whole exam was Opus (?
