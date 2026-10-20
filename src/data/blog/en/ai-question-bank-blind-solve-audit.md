---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-20T00:10:00Z
title: I Had a Second AI Blind-Solve My Entire Question Bank
slug: en/ai-question-bank-blind-solve-audit
featured: false
draft: false
tags:
  - ai-workflow
  - case-study
  - ai-education
description: 'My question bank is AI-generated, so I did not let the same AI check it. A second AI re-solved every sampled question without seeing the answer key, and people judged whatever did not match.'
---

I run a GMAT practice platform called PDT, and most of its question bank is AI-generated. In the early-September backup, the Critical Reasoning (CR) section alone had 2,662 questions, and 2,624 of them had IDs starting with ai_gen.

If an AI wrote the questions, who checks them? I asked a second AI to solve each one from scratch without seeing the answer.

## Why the AI that wrote the questions can't check them

I wrote earlier about [the blind spot in AI self-verification](/blog/posts/en/ai-self-audit-blindspot). When an AI looks back over its own work, it uses the same context that produced the mistake, so the blind spot gets copied intact.

It's worse for question writing. The AI already knew which option was meant to be right. Hand the question back for a check, and it tends to go looking for reasons to support that answer. So the checker can't know the key, and can't inherit the context from when the question was written.

## How the blind solve works

First, split the questions into two files. One has only what a student sees: the stem and the options. The other has the answer key and the explanation. The solving AI only gets the first.

For each question, it writes down its answer and a runner-up option. Only after all of them are done does anyone open the key and compare.

When something doesn't match, I don't just call it a wrong key. The solver rereads the stem and the explanation, writes out why the key holds or fails and why its own answer holds or fails, and then sorts the case: the key is really wrong, two options both work (or none does), there's a formatting or content flaw, or the solving AI simply got it wrong.

For sampling, I deliberately over-sampled the small question types. The 200 CR questions in one round were stratified by subtype (weaken, strengthen, explain, assumption, evaluate and so on), with the smaller types getting a relatively larger quota.

## What it caught

The result first. Across the samples (250 Problem Solving questions, 250 Data Sufficiency questions, 200 CR questions and 240 reading comprehension sub-questions), the number of questions with a wrong answer key was 0.

I expected the blind solve to mostly catch wrong answers. The problems looked different.

The first kind is a stem and a key that contradict each other. One CR question asks how to weaken the claim that a modified corn plant reduces caterpillars. The stem says the chemical the plant releases only becomes a wasp-attracting scent after it meets caterpillar saliva. The key's option says that when wind damages the plant it releases the chemical too, so wasps keep flying to nothing and learn to ignore the signal. But wind damage means no caterpillar, so no scent, so the wasps are never drawn in. The solving AI picked that same answer too, but said it was only the option with the fewest contradictions, not a clean answer. That question had 9 attempts and an 11% correct rate.

The second kind is small enough that a human eye would miss it. In one reading passage, the sub-question's answer is E, but the passage-level answer string says B. In the full-bank structure scan, that's the only record with this mismatch. Another CR question has only 4 options, the only one in the bank that doesn't have 5. And one question translated "tap water" as "still water", which means water without bubbles, so the whole argument reads strangely.

The third kind is leftover damage from batch generation. In 38 DS questions, the closing question was replaced with the text of option A, so students read a sentence that looks like it's giving the answer. For 10 of them the key happened to be A. They all came from the same generation batch.

The fourth kind can't be seen on any single question; you have to look at the whole bank. Across 2,662 CR questions, the correct answer is C 48% of the time, B 38%, D 5%, E 1%. Always picking C gets you nearly half right, which inflates students' scores and teaches a habit that doesn't help on the real exam. Shuffling the options later fixed part of this: of the 4,766 CR questions live on October 20, C is the key about 32% of the time, still not even.

## The blind solver gets things wrong too

The solving AI is not a judge.

On a DS question, the only one out of 250 where the solver first disagreed with the key, the solver had missed that "cost can't be negative". Once it re-solved the question, the key was correct. On a CR question, the solver first picked D, then on a second pass agreed the key C held up but D could also be defended, so the question was still filed as "two options both work".

One case is more interesting. Take the reading question I mentioned, where the sub-question and the group answer string disagree. The blind solve on 10/18 picked E, matching the sub-question. Another independent blind solve on 10/20 picked B. The same question got different answers on different runs, and that alone is a sign the question may be ambiguous. So the call goes to a person who sits down with the question.

One caveat: the blind solver across these rounds was the same model, so it may share blind spots. And finding zero errors in a sample doesn't mean there are none. Zero wrong keys in 112 questions only puts the 95% upper bound at about 2.7%. Across three combined CR rounds, 0 in 319 brings it down to 0.94%. A bigger sample lowers the bound, but it never reaches zero.

After I fixed questions, I ran one more check. I packaged 13 revised questions with no question numbers, answer keys or explanations, and gave them to a solver that had never seen the keys. All 13 matched the keys, but for three of them it rated its own confidence as only medium. I went ahead with the plan, and if answer data later shows an odd distractor pick rate on one of them, I'll go back and fix it.

## If you use AI to write questions too

Whether you're generating exams, practice sets or teaching material, the approach is about the same.

Don't ask the chat that wrote the content to check it. Open a second AI and give it only what a student would see. Have it answer first, then name a runner-up, and only then show it the key. When something doesn't match, don't rush to call the key wrong. Sort it first: is the question ambiguous, is the formatting broken, or did the solving AI get it wrong? And when two blind runs on the same question give different answers, or the solver says both options work, hand it to a person.

When a sample is too small, you can also scan the whole bank with code for structural problems: option counts, how answer letters are distributed, whether fields line up. A human reading question by question won't notice those.

AI can write the questions, and it can help me check them, but signing off can't be outsourced. When this bank goes live, the name on it is still mine.

That's it.
