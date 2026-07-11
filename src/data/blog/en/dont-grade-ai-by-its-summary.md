---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-10T04:00:00Z
title: Do Not Grade AI by Its Own Summary
slug: en/dont-grade-ai-by-its-summary
featured: false
draft: false
tags:
  - ai-workflow
  - case-study
  - lessons-learned
description: "I hit the same failure in several forms this week: an agent denied changing files, a commit message overstated the diff, and a transcript reassigned a speaker ID halfway through."
---

I assigned an agent to scan a transcript for omissions. The prompt explicitly said read-only and prohibited edits. It still created an xlsx practice file and reported that it had changed nothing. `git diff --stat` exposed the unexpected file, and its modification time matched the agent's run.

Lesson: read-only restrictions need tool-level enforcement, not just prompt text. An agent's claim that it "did not do X" still needs verification.

## Commit message versus actual diff

A commit message said "reorder the opening flow," but the diff showed that only the HTML deck and cue card had been reordered. The Chinese prep document had one prompt edit and no change to its page order. I found the mismatch only after checking again that evening.

Lesson: verify a commit message against the diff. When parallel documents are maintained separately, check each one after any reorder.

## One speaker ID, two people

Tencent Meeting Notes changed its speaker labels halfway through a call. After Sam said he had to leave, the system reassigned the same "Speaker 3" label to Sho. I initially attributed Sam's comments to Sho.

Lesson: a speaker number can change owners without looking suspicious on a quick read. Use the content's logic or ask someone who attended instead of trusting the label alone.

## An independent review also needs review

An independent agent reviewing the A-2 lesson plan found one real error. It also claimed that a session involving real data had been recorded and violated the existing data boundary. Dustin later confirmed that the second claim was wrong: all work happened on Ray's own computer, there was no recording, and no compliance boundary had been crossed.

Lesson: an independent agent's finding can itself be wrong. High-risk claims about compliance or recording cannot go straight into the source of truth. The person involved still needs to confirm them.

<!--
Sentences added beyond the source material (fidelity disclosure):
None. Translation, deletion, and stitching only.
-->
