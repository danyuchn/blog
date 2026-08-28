---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-28T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: People Who Scored High on the GMAT Work Noticeably Better With AI
slug: en/gmat-logic-is-ai-collaboration-skill
featured: false
draft: false
tags:
  - teaching
  - ai-education
  - opinion
description: 'An unwritten observation: people with high GMAT scores collaborate noticeably better with AI. So I wrote two GMAT-style questions about AI ability. How many can you get right?'
---

## An unwritten observation

People who scored high on the GMAT are noticeably better at collaborating with AI.

(I'm absolutely not patting myself on the back here.)

So I'm going to design GMAT-style questions that test AI ability. I mentioned this once in [Responsibility Is What AI Cannot Do](/blog/posts/en/responsibility-is-what-ai-cannot-do), where I only talked about the logical training the GMAT gave me and never turned it into questions.

## Not a humanities-versus-science thing

Someone asked me whether this is the difference between humanities people and science people. Hard to say. I've met plenty of humanities people with poor logic who get spun in circles by AI.

People with an engineering background are better at reading evidence and setting up tests, following the thread until they find where the AI went wrong on a long task. Without that foundation, a lot of people just curse at the AI and tell it to go around again and redo it, which is completely pointless. I broke down that "how to look at evidence" part in more detail in [The Debugging Mindset](/blog/posts/en/debugging-mindset-logic-ai-pedagogy).

## Try it. How many can you get right?

These questions test the logical thinking you use when working with AI.

## Q1

(How to answer: the question asks you something and gives you two clues. You decide which one lets you answer with certainty: clue one alone, clue two alone, or both together. If no combination gets you there, the clues are not enough.)

You assign a read-only investigation task to an AI agent, asking it to check whether the file names in a folder follow company convention. You are using a general-purpose agent with full Edit/Write permissions (not structurally restricted to read-only), and your instructions clearly state "check only, do not modify any files." When the task finishes, the agent reports: "This was a check only. No files were modified."

Can that report of "no files were modified" be taken as true?

Statement 1: You ask the agent to list, in its reply, every action it believes it performed, and no write-type operation appears anywhere in the list.

Statement 2: You independently run git status on the folder, and it shows no files in a modified or newly added state.

(A) Statement (1) alone is sufficient; statement (2) alone is not  
(B) Statement (2) alone is sufficient; statement (1) alone is not  
(C) Both statements together are sufficient; neither alone is  
(D) Each statement alone is sufficient  
(E) Both statements together are still not sufficient

## Q2

(How to answer: the question gives you a piece of reasoning with a hole in it or in need of support. From five options you pick the one that best punctures the hole, supplies the missing piece, or fits the conclusion. The other options may sound reasonable, but they answer the wrong question or do no damage.)

A user says: "I wrote a full description for this skill, and I put all the colloquial trigger phrases users tend to say into a custom trigger field under the metadata. The body text is clear too. It has been live for two weeks, and in my own testing this skill has never once been invoked. My guess is the body text is not well written, so I am about to rewrite the whole thing."

Which of the following, if true, most weakens this user's judgment that "the body text is not well written"?

(A) A skill reads only name and description to decide whether to trigger  
(B) Fewer than ten people have actively used this skill in the past two weeks  
(C) The section headings in the body do not fully follow the officially recommended formatting  
(D) This user has written several other skills unclearly in the past  
(E) The procedure this skill describes takes three steps in total to complete

Answers: B, A.

Anyone who prepped for the GMAT feeling PTSD yet? That's right. The logical thinking you learned on the GMAT is something you still need in the AI era.

## While I'm at it, a thought on education

This reminds me of a view on education I put forward a long time ago.

Teachers don't need to ban students from using AI on assignments, because you'll never catch them all. As a teacher you should take the longer view: if a student genuinely absorbs and internalizes things while working with AI, what's wrong with that?

So my suggestion is to take the Italian tradition of examining everyone one-on-one, orally, and put it together with the Buddhist rules of debate. You don't ask whether the report a student hands in was written by AI, but the teacher questions them about it on the spot, and they have to answer fluently.

If they can answer fluently, whether it came from AI no longer matters.

<!--
新增非原文句子清單（忠實度自首）：
1. 「I mentioned this once in Responsibility Is What AI Cannot Do, where I only talked about the logical training the GMAT gave me and never turned it into questions.」 — 類型：銜接（站內互引，任務指定）
2. 「Someone asked me whether this is the difference between humanities people and science people.」 — 類型：銜接（原素材為回覆他人，補上對話情境）
3. 「I broke down that "how to look at evidence" part in more detail in The Debugging Mindset.」 — 類型：銜接（站內互引，任務指定）
4. 「## An unwritten observation」「## Not a humanities-versus-science thing」「## Try it. How many can you get right?」「## Q1」「## Q2」「## While I'm at it, a thought on education」 — 類型：框架句（分節標題；Q1/Q2 為原文既有標記）
5. 「These questions test the logical thinking you use when working with AI.」 — 類型：改寫（原文為一句「試試看，以下你能做對幾題？這些題目會考驗你跟AI協作的邏輯思維」，拆為標題＋句子）
-->
