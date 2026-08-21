---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-10T04:00:00Z
modDatetime: 2026-08-20T04:00:00Z
title: Do Not Grade AI by Its Own Summary
slug: en/dont-grade-ai-by-its-summary
featured: false
draft: false
tags:
  - ai-workflow
  - case-study
  - lessons-learned
description: 'I hit the same failure in several forms this week: an agent denied changing files, a commit message overstated the diff, and a transcript reassigned a speaker ID halfway through. A later batch added checks that never ran and still reported clean.'
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

## The checker was not checking, and reported everything fine

The most common shape of a later week: the check never compared anything and still returned a value that looked normal. `pytest` was not installed at all, and the output still read "0 failed OK." The morning brief's pending-branch scan only looked at `refs/heads/night-batch/*`, so five `review/*` branches opened the day before were invisible and the line printed "pending branches: none." The pain-point mining pipeline's validator exited 0 on zero quotes; its URL check used a loose substring comparison, so all 73 malformed URLs passed, because both sides of the comparison were malformed the same way.

Lesson: when a check reports "fine" or "none," first confirm that it is actually comparing something. If you expect a certain number of hits and get 0, run a sample you know should match to prove the checker moves before you trust the result.

## Exit code 0 and "I finished it"

`--draft-block-size 1` is an invalid setting: the `if bs <= 1: break` at `mtp.py:604` exits the loop on the first pass, so a real run emits one token, returns exit code 0, and warns about nothing. The smallest valid value is 2. The thumbnail generator's `compactTitle()` cuts anything past 22 characters without an error, so 36 thumbnails sat on YouTube for months with their sentences chopped in half and nobody noticed. `gh pr view` reports `state=CLOSED` for both "merged" and "closed," so two upstream fix PRs looked repaired until `mergedAt` came back null. Of five extraction agents I dispatched, two claimed they had written their files: one split the path wrong and wrote into a different directory, the other never wrote anything and left the content in its reply.

Lesson: check the artifact itself. Does the file exist, does its content read back, what is the field value. Not the exit code, not the status string, not the executor's own account. And any automation that can discard content should raise an error when something does not fit instead of dropping characters silently.

## Numbers that look like a score

Running `--only M8,M9` to skip levels printed a summary line of `a3b@m89 0/ 9`. That 0 was not a score. It came from the boundary counting up from level 1, and the per-cell data showed all four cells passing. In the same batch, hitting the token ceiling got recorded as the model's capability boundary, and results served from a warm cache got recorded as normal data. Another case was a database field: a student screenshot was stored in `webui.db` as `type:"file"` with an empty `inner data:{}`, which looked like vision never ran and no text was extracted, and I reported a concern on that basis. The real condition is the top-level `content_type`, and a bare file id is later converted to base64 and sent through. Comparing the original image against the reply confirmed that vision had worked the whole time.

Lesson: when a summary number contradicts the per-cell data, the per-cell data is the fact. A suspicious-looking field means following the pipeline to its exit before concluding anything, not stopping at what the storage layer happens to show.

## Before saying "there is no way to do X"

I said brew's plist setting had "no persistent fix," on the strength of one candidate, that the core tap runs in API mode and the formula is not editable. `brew services --help` spells out an `.env` mechanism. I nearly wrote up a fixable problem as a long-term defect that could only be caught by alerting. Search spelling is the same error in another form. Grepping Arabic numerals against a Chinese source, I reported that two numbers were absent from a student transcript when the source spelled them out in Chinese characters. Searching `result` and its Chinese equivalents, I concluded a client had never said "look at the output first," when the wording was `final output`, and I used that to accuse an agent of hallucinating. Repeating a subagent's negative claim goes the same way: a reviewer said the largest teaching community had not made the candidate list, and it was in fact among the 156 candidates, filtered out by a size ceiling I had set myself. The search had not failed. The rule was wrong.

Lesson: before saying "there is no way to do X," exhaust the tool's own `--help` and its official docs. To prove a string is absent from a document, search the Chinese spelling, the full-width forms, and the unit variants too. The adjacent error is inventing a mechanism to explain a number instead of reading the actual setting: I described an observed 32,770 as sharing across parallel slots when the log recorded `OLLAMA_NUM_PARALLEL:1`.

I later made a video on the same theme: <https://youtu.be/d5Ipmp6RSJ0>

<!--
Sentences added beyond the source material (fidelity disclosure):
None. Translation, deletion, and stitching only.
-->

<!--
2026-08-21 W35 merge additions (four sections) — sentences added beyond the source material:
1. "The most common shape of a later week: the check never compared anything and still returned a value that looked normal." — bridging sentence, rewritten from the 2026-08-16 daily note ("this shape appeared five times today" / "the common shape").
2. "Search spelling is the same error in another form." — bridging sentence linking the 2026-08-16 and 2026-08-20 cases.
Every other sentence is a translation, condensation, de-identification, or plain-language rewrite of the daily notes. No lesson or criterion was added that the author did not write.
De-identification: a named student's transcript became "a student transcript," and r/Teachers became "the largest teaching community."
The four new sections were passed through the humanizer skill; the pre-existing sections were left untouched.
-->

