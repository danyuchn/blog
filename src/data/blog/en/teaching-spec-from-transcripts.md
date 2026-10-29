---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-28T04:00:00Z
title: "Turning Lesson Transcripts into a Teaching Spec: One AI Drafts, Another Finds Faults, I Only Decide"
slug: en/teaching-spec-from-transcripts
featured: false
draft: true
tags:
  - ai-workflow
  - teaching
  - ai-education
description: 'My one-on-one lessons ran 51% over schedule. I went back to the lesson transcripts, had one AI write up my teaching rules and another hunt for faults, and only made decisions on a single checklist myself. The method, the numbers, what I actually told the AI, and a prompt you can paste.'
---

I teach one-on-one lessons. Recently I had an AI write down "how I actually teach" as a set of rules, so that whenever an AI helps me prepare a lesson or write the notes afterwards, it follows them. I call it my teaching spec. The spec grew out of lesson transcripts: one AI goes back to the transcripts, rebuilds what really happened in class and drafts the spec; a second AI only hunts for faults; and I only make decisions, item by item, on a single checklist. Once written, the spec can still be overturned and rewritten by the next lesson.

This post covers four things in order: where I was stuck, how I wanted the spec to grow, the numbers I measured, and what I actually told the AI along the way. A starter prompt you can paste to an AI comes last. If you want the flow charts and the mechanics, jump to the [appendix: how it is built](#appendix-how-it-is-built).

## Where I was stuck

The first problem was overtime. I pulled the transcripts of 15 one-on-one lessons and compared the times: 1,320 minutes scheduled, about 1,990 minutes actual. That is 51% over, about 11 hours unbilled. The cause was that the lesson time itself had no protection at all: nobody checked before the lesson whether the student was ready, what we had agreed to cover got pushed aside, I filled the time with my own demonstrations, nobody checked whether anything was learned, and there was no contact between one lesson and the next.

The second problem was that the spec said one thing and the lessons did another. Some time after the spec was set, I noticed my actual practice and the written clauses drifting apart. This is what I told the AI at the time ("spec" is this spec):

> 自從定了 spec 以來飄移蠻多

> (translated from Chinese)

Checking showed that some clauses had never happened in a lesson, and things I did all the time were missing from the spec.

The third problem was letting an AI write the spec directly. What comes out is an ideal lesson that does not match mine. Without "go back to the raw record first and see what actually happened" and "have a second AI hunt for faults independently", the AI's first draft goes wrong. Once, while tidying an appendix, an AI quietly dropped real steps and invented a command that does not exist.

The fourth problem was my own time. My time belongs on making decisions, not on writing clauses by hand. The AI lists what I need to decide as a web page, one item per row; I will call it the review page. That review page keeps getting longer too. I complained more than once that it was too long, and every item on it is time I have to spend.

## What I wanted, and how it changed

The division of labor I wanted: pulling the key points out of transcripts, drafting, and fault-finding all go to AI, split across different AIs so that no AI writes and reviews its own work. I appear only at the decision step, on a single page, one decision per row.

[![The seven steps from transcripts to a spec and who does each: measure the problem, see what really happened, draft, another AI finds the flaws, I decide, write it into the rules, use it in the next lesson; only step five is mine](/blog/assets/posts/teaching-spec-from-transcripts/1-loop-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/1-loop-en.jpg)

The key turns, by date:

**8/29, measure first.** I went through the transcripts of 15 one-on-one lessons and found that 51% overrun. The spec was on its third version then, and that version started from this number, not from "what an ideal lesson should look like".

**9/25, the measurement overturned itself.** I recomputed where the lesson time went, over 8 lesson transcripts. The first pass said the time I spent "taking the topic off on my own tangents" was 34%. With a new criterion, only 15.6% remained. My own recount overturned the first result, and I recorded the new number in my lesson-prep notes.

**9/26, a round of corrections after class.** That day I edited six places in the lesson notes the AI had written for me, then asked it to look back:

> 回顧這次我改了哪裡、規格有沒有涵蓋、你會怎麼修

> (translated from Chinese)

The AI produced a table of suggested changes, I confirmed it, and it went straight to editing the spec, along with the instructions it follows whenever it writes lesson notes.

**10/8, version five.** I felt practice and spec had drifted too far apart again, so I opened 4 AIs at once to read in parallel, each reading a whole transcript of 110,000 to 160,000 characters. The AI pulling it all together picked out the timestamp for every conclusion and checked it against the source before accepting it, and in passing caught one after-lesson review that still used the standard from before it was relaxed. The AI sorted the changes into three groups: remove outright, right purpose but wrong wording so change the phrasing, and things I always did that the spec never said. I answered with a single message: "all three groups agreed".

## Measured results

What I measured is how the spec grew. I teach two kinds of one-on-one lessons: one teaches people to use AI, the other prepares students for the GMAT (the exam used for business school admissions), and each has its own spec. Within two months the spec went from version three to version five, and the GMAT spec went through two rounds of decisions. The baseline is what actually happened in the transcripts.

[![Two sets of numbers computed from transcripts: 15 lessons scheduled 1,320 minutes, actual about 1,990 minutes, 51% over; lesson density 34% under the first criterion, 15.6% recomputed with the new one](/blog/assets/posts/teaching-spec-from-transcripts/2-numbers-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/2-numbers-en.jpg)

**Measurements overturn themselves.** The lesson-time number came out at 34% the first time and 15.6% under the new criterion. Without the recount against the transcripts, that 34% would have gone straight into the spec.

**Independent fault-finding catches real errors.** The draft of the GMAT spec went to the strongest AI model available for review: 17 items, 15 accepted, 2 partly accepted, and the spec's appendix records how each was handled and why. For the documents students read, I had an AI play a non-technical student in each round and walk through them from the start: the first round found 25 rough spots, 7 of which would stop a student completely.

**More review rounds do not make it better; change the structure.** Reviewed this way, every round of the student documents turned up about 6 new blockers, and it was still happening in round five. Digging in found three structural causes: one fact was spread across 5 documents, 2 languages and 12 cross-references; the reviewing AI remembered nothing from the previous round; and "would a beginner be confused" has no natural end. The fix was to keep a single template as the master copy and generate the other documents from it automatically, add an automatic check that blocks mistakes as they are written, distill about 100 review findings into a checklist that is rerun every time, and agree on a pass condition: zero blockers passes, minor issues do not block. It settled down by round seven. Another example: after-lesson reviews were sorted by file name, so the automatic check missed some; after switching to sorting by content, the checked set grew from 11 files to 21, and all 21 turned out to be missing three required fields.

**My time goes to making decisions.** The GMAT spec had two rounds of decisions, with review pages of 17 and 11 items. The second round was not scheduled in advance; it grew out of the comments I added in the first. Four of those comments raised questions that needed research before they could be decided, and the answers became the 11 items of round two. One of them, "delayed course activation", turned out to be all activation dates the students had chosen themselves, so it was closed on the spot. For version five I replied with one message. The first version of the review page used too much jargon; after I questioned it, the AI rewrote it in plain language.

[![Review page schematic: 17 items in round 1; my notes raised four questions to check, which became the 11 items of round 2; each row is adopt, adopt with exceptions, or reject, with a one-line reason; items that need no call from me stay off the page](/blog/assets/posts/teaching-spec-from-transcripts/6-review-page-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/6-review-page-en.jpg)

The figure above is rebuilt from the real review-page format.

**Automatic checks need testing in reverse too.** One check blocks anything containing internal codes that have not been explained. Before launch I verified it in reverse with seven cases: all four kinds that should be blocked were blocked, and all three that should pass passed.

After the spec went live, whether lessons run closer to time and whether students improve are two things I have not measured yet. What I have measured is whether the spec matches what I actually do.

## What I told the AI along the way

Below are a few things I told the AI during this process, in my own words. After each one, a line on how to adapt it to your situation.

**1. Do not decide in the chat; move it to a page**

The AI had been throwing a long list of questions at me in the chat, and I answered (the "ruling page" is the review page above):

> 改裁決頁，我在裁決頁裡決定

> (translated from Chinese)

Adapt it: when an AI throws a long list of questions at you to answer in the chat, tell it to turn them into one page, one decision per row, and decide on the page.

**2. Ask directly when it is too long**

When the review page grew long again, I asked:

> 要我裁的你確定要寫那麼多嗎

> (translated from Chinese)

Adapt it: when the review page is longer than you are willing to read, ask this. Items should be filtered first, keeping only what needs your judgement.

**3. Decide in batches**

This is the 10/8 round above: the AI had sorted the changes into three groups, and I replied:

> 三類都同意

> (translated from Chinese)

Adapt it: ask the AI to sort the changes into groups and state the purpose and reason for each. If the grouping is good, you can answer everything in one message.

**4. Add one line of why**

One item was about how my lesson-prep hours should be recorded, and when I decided it I added:

> 標準就是要反映真實準備時間，方向是把準備時間縮短，不是少算

> (translated from Chinese)

Adapt it: add a reason when you decide. That sentence later shaped how several clauses on "how prep hours are recorded" were written; the reason travels to the next situation better than "which option" does.

**5. Ask for a review after you edit**

> 回顧這次我改了哪裡、規格有沒有涵蓋、你會怎麼修

> (translated from Chinese)

Adapt it: after you edit an AI's output, ask it to compare your changes against the current spec and add whatever the spec does not cover.

**6. Ask directly when you are unsure about your own practice**

> 我的教學方法是不是還沒成形？

> (translated from Chinese)

Adapt it: put this question to an AI and ask it to answer against your records. The answer I got was that the teaching itself was stable; what changed were the spec, the course plans and the kinds of students, and what was still undecided was "does it work" and "did I deliver what I promised students". On the spot, that produced a new list just for tracking what I promised students and whether it was done.

## Starter prompt

To grow a spec from your own lesson records, start from this, replace the parentheses with your situation, and paste it to an AI that can read the files on your computer:

```text
I want to turn my lesson transcripts into a teaching spec (a set of teaching rules written for an AI to follow). The transcripts are in (folder location).

1. Measure first, do not write the spec yet. Read (how many) transcripts and compute (the symptom I want to improve, e.g. minutes of overtime, how many times an agreed thing was not done). Attach the file name and location for every number. If you cannot compute it, tell me what data is missing.
2. Rebuild "how I actually teach now" from the transcripts. Every item carries a verbatim quote and timestamp; anything backed by only one lesson goes in a separate "to verify" list, not the main text.
3. Open a separate AI that has not seen the conclusions so far as the attacker: do not assume the results are correct, check every quote against the transcript, report only errors and things you cannot decide; stop when you find nothing new.
4. Draft the spec from the checked results: direction only, no scripted wording, no minute-by-minute limits; mark each item with the number of lessons backing it.
5. Turn the items that need my judgement into one review page, one decision per row, with options and a comment box. Handle the items that do not need my judgement yourself and keep a log; do not send them up. The reasons I add are written beside the clause in my own words.
6. Once the spec is settled, mark it "first use" and remind me on (date) to check back: look at whether it actually runs, not whether it is written down.
```

## Appendix: how it is built

This section is for people who want to build one themselves; the technical terms, file shapes and rules are all here.

### Technical terms behind the plain wording

- "A set of rules written for an AI to follow": the teaching spec, the rules file the AI reads before preparing a lesson or writing notes.
- "The instructions it follows whenever it writes lesson notes": a Claude Code skill.
- "Opened 4 AIs at once to read in parallel": 4 parallel sub-agents.
- "The AI pulling it all together": the lead, meaning the session you are talking to.
- "A second AI only hunts for faults": the attacker below, opened as a separate session without earlier conclusions.
- "The strongest AI model available": drafting and attacking use a stronger model; extraction can use a cheaper one.
- "An automatic check that blocks mistakes as they are written": hooks and lint checks that run before a write.
- "Lesson-prep notes": the asset file where measurement results are recorded.

### The overall flow: who hands what to whom

One round of spec generation has six roles: the read-only transcripts, an extractor (can be a cheaper model), a drafter and an attacker (each a stronger model), the lead (your conversation), and me. The three AI roles are dispatched in three separate runs, not merged into "write it and check it yourself".

[![Sequence of one round of spec generation: the extractor reads the transcripts, passes extract files with quote and location to the lead, the lead spot-checks timestamps and gives only the extract files to the drafter, the draft goes to an attacker that has no earlier conclusions, the attacker reports errors and undecidable items, the lead hands me the filtered review page, I return a ruling and one line of why, and the lead turns it into a mechanism marked first use](/blog/assets/posts/teaching-spec-from-transcripts/3-sequence-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/3-sequence-en.jpg)

The drafter reads only the extracted results, and the attacker is opened separately, without the conclusions of earlier rounds.

### Extracting from transcripts

Extraction uses one fixed set of questions, and every item must carry a verbatim quote and a location. For the GMAT spec, a cheaper model read the records of 47 students and 14 consultation contacts in 11 batches and produced 61 extract files, and then a stronger model wrote the spec reading only those extract files.

The first line of the extraction spec says: every item carries `quote` (20 to 120 characters, verbatim) and `pos` (timestamp or line number). When the lead receives the files, a program checks that each `quote` really is a substring of the original. Any item whose quote does not match is discarded in full. The smallest version looks like this:

```python
import json, sys

def norm(s):
    return "".join(s.split())

def check(extract_path, transcript_path):
    transcript = norm(open(transcript_path, encoding="utf-8").read())
    items = json.load(open(extract_path, encoding="utf-8"))
    bad = [i for i in items if norm(i["quote"]) not in transcript]
    print(f"{len(items) - len(bad)} / {len(items)} quotes found in the transcript")
    for i in bad:
        print("NOT FOUND:", i["quote"][:40])

if __name__ == "__main__":
    check(sys.argv[1], sys.argv[2])
```

Run `python3 -I verify_quotes.py extract.json transcript.txt`. This script only checks that the quote is there; it cannot tell whether the sentence was misunderstood, so the lead still spot-checks timestamps against the source to read the context. That is what was done for version five, and it caught the retrospective that used the pre-relaxation standard.

Every rule needs at least two cases behind it, so the rule table gets an extra column, "number of supporting cases", and any row below 2 moves to "to verify".

### Drafting and attacking

The drafter reads only the extract files. The attacker is opened separately, without earlier conclusions and without the drafter's reasoning. The attacker's instructions must state that it may not assume the results are correct, that it reports only errors and things it cannot decide, and a pass condition, or it will always find something new. An example follows, with parentheses for you to fill in:

```text
You are the attacker. Below are a spec draft and the matching transcript.
Do not assume the draft is correct. Check it item by item against the transcript.
Report only two kinds of things: errors, and things you cannot decide.
Pass condition: (for example: zero blockers). Stop once it is met; do not list minor issues.
```

The attacker's role can also be swapped for the reader: ask a stronger model to play a non-technical student in each round and walk through the student documents step by step.

### The review page and the ruling log

Not every item should reach me. They are filtered before they are sent up:

[![Decision flow for one item left after the attack: backed by only one case goes to to-verify; needs a lookup becomes a verification question for the next round; if it needs no judgement from me the AI handles and logs it; what remains becomes a review-page row, I rule, the reason is written beside the clause in my words, dated with who decided, marked first use with a review date](/blog/assets/posts/teaching-spec-from-transcripts/4-decision-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/4-decision-en.jpg)

Each row on the review page is one decision: with options (accept, accept with exceptions, reject) and a comment box, and at the bottom only the items with exceptions, copied back into the chat with one click. I generate the page with a skill called `review-page`. When a ruling is written back into the spec, the ruling log has four fixed columns:

| Ruling | Added reason (my words) | Done | To do |
|---|---|---|---|
| Accepted | The line I added in passing | Which clause changed | What needs a later check |

Every revision carries a date and who decided it. A clause that has been overturned is marked "void" and stays in the ruling log; it is not silently deleted.

### The life of a rule

A new rule is not final right away. Mark it "first use, watching" and attach a dated follow-up. At the review, look at whether it actually runs, and drop it if it does not. A practice that departs from the spec is first recorded as a "known variant", and promoted only after a third occurrence or once it is proven useful.

[![State diagram of one rule: a draft rule that passes the ruling becomes first use, watching, with a review date; if the review shows it runs it is settled, if not it is dropped; a known variant is promoted to settled after a third occurrence or once proven useful; a settled rule overturned by actual practice becomes void and stays in the ruling log](/blog/assets/posts/teaching-spec-from-transcripts/5-state-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/5-state-en.jpg)

Enforcement has three levels: gates that block a write (hooks, lint, fields owned by a script), after-the-fact reminders, and written rules with a periodic re-check. Whatever can be automated should be made to block the wrong write at the moment it happens, and once a gate is written it needs a reverse test proving that what should be blocked is blocked and what should pass passes. When the same kind of problem shows up a third time, stop and ask "what structure keeps producing it", and put the answer in the commit message.

### Build it yourself: the smallest version

1. One symptom and one number you can compute (minutes of overtime, how many times an agreed thing was not done).
2. One extract file, each item with `quote` and `pos`, checked with the script above.
3. Dispatch drafting and attacking once each; the attacker does not see earlier conclusions, and its instructions state the pass condition.
4. Turn the items that need your judgement into one page, one decision per row, and keep the reason you add beside the clause in your own words.
5. Mark a settled rule "first use" and set a review date.
