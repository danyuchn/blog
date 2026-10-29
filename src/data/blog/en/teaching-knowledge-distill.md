---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-28T04:00:00Z
title: "Distilling Years of Teaching into a Knowledge Base AI Can Read: Checking Quotes with Code and Ruling on Contradictions"
slug: en/teaching-knowledge-distill
featured: false
draft: true
tags:
  - teaching
  - ai-education
  - ai-workflow
description: 'I gave AI over two hundred interview transcripts to distill into a teaching knowledge base. This post covers a model that reported all quotes correct while code found 6 wrong out of 44, how I rule when my own versions conflict, and a starter prompt you can paste to an AI.'
---

I recently distilled my GMAT teaching of more than ten years into a knowledge base an AI can read, using a batch of interview transcripts. Every claim carries my original words and a timestamp, so it can be checked, and where my own versions contradict each other, I make the ruling.

This post covers four things in order: where I was stuck, what I wanted the knowledge base to look like, the numbers from the actual run, and the instructions I gave in my own words. At the end there is a starter template you can paste to an AI. If you want the technical details of extraction and quote checking, jump to the [appendix: how it is built](#appendix-how-it-is-built).

## What was bothering me

The first problem was that I had plenty of material, but the AI could not read "how I teach." In this round I first turned all students' score reports and interview records on my cloud drive into transcripts. My expectation of the AI was simple: the transcripts could add to my teaching thinking and systematize the score reports. The interviews alone came to 202 transcripts, and once converted they were just a pile of files.

The second problem was that reading everything is expensive. I started with the most obvious approach: one subagent per transcript. After 20 of them, the total was about 2.57 million tokens (the unit AI uses to measure usage), roughly 130,000 per transcript. At that rate, all 202 would cost about 26 million tokens.

The third problem was that the AI said it was right and I could not trust it. I asked the cheapest model (Haiku) to extract diagnoses, prescriptions and estimates from one interview of about 62 minutes, with my original words attached to every item. It returned 44 items and wrote in its report that every quote was copied verbatim from the source. I wrote a small program to compare them. Of the 44 items, 6 quotes could not be found in the transcript, and 4 timestamps did not exist at all.

The fourth problem was that my own versions fight each other. On the same question, the 2024 me and the 2026 me say different things. For time allocation, the old version looked at the slope of percentile curves, and the new one looks at how many score levels each section is from its "sweet spot." On whether question position affects the score, the old and new versions say opposite things. The AI just lists everything it sees in the corpus. It does not know which one is the current me.

## What I wanted, and how it changed along the way

I wanted a teaching knowledge base the AI looks up when preparing lessons or answering questions, and it had to satisfy three things. First, every claim carries my original words and a timestamp that a program can check. Second, every claim shows how many interviews it appears in, so something said once is not treated as my method. Third, where versions contradict, I rule, the rulings sit at the very top of the document, and dropped old versions count as history only.

[![Six steps from transcripts to knowledge base: AI does extraction and synthesis, a program checks the quotes, I appear only at the ruling step, and afterwards it is wired to where it is used with an exit for retirement](/blog/assets/posts/teaching-knowledge-distill/1-pipeline-en.jpg)](/blog/assets/posts/teaching-knowledge-distill/1-pipeline-en.jpg)

The process went roughly like this, with the key turns concentrated on Oct 3.

**Oct 3, morning: a small pilot first.** I had three pilot runs (Haiku, Sonnet, and a long file) use the same extraction spec on the same transcript for comparison. Haiku's result is the 6 wrong items above. The spec was changed into two rules: a quote may not join two separate turns of speech, and the subagent must run a program itself and report what the program actually printed, never a verbal "all match."

**Oct 3, morning: switch to sampling.** After I saw that the full run would cost 26 million tokens, I stopped it and switched to a stratified random sample of 22 interviews, sampling until synthesis stopped producing new things. Questions that needed the whole corpus were answered with a keyword script instead.

**Oct 3: out-of-sample check and item-by-item rulings.** The AI grouped the 22 interviews into 464 clusters and wrote a teaching-system document. I then asked it to draw 12 more interviews it had not read, to see how much the document covered. After that I ruled on 22 contradictions in three batches, writing adopt or not adopt with a reason for each.

**Oct 7: the misuse-boundary column becomes "fill it when it is used."** A separate line of work is a "sticking-point prescription table" I built from one-on-one lesson transcripts. Its "misuse boundary" column has about 528 cells, and I could not review them all, so the rule became: whichever prescription a lesson plan cites, I fill in that one while reviewing the plan.

**Oct 18: one ruling withdrawn.** For math guessing, I had ruled that at least 0.5 minutes must be left. I later decided on no lower limit: guess and move on. That item was one I had ruled on myself, and I overturned it.

## What I measured

The scope is the interview corpus: a sample of 22 from 202 transcripts, 12 out-of-sample interviews, plus 1,028 cards from the prescription table. The baseline is the same spec and the same transcript run on different models, and the difference before and after program verification.

**Program-checked quotes catch errors that a model's self-report misses.** On the same transcript with the same spec, Haiku extracted 44 items. The program found 6 quotes that did not match and 4 timestamps that did not exist, and Haiku said everything matched. Sonnet extracted about 100 items and the program found 0 mismatches. The prescription table was bigger: 1,028 cards checked one by one, and 89 (about 9%) failed. They are kept, but may never carry a method alone. I also ran a misalignment control test, which put the false-match rate at about 6%.

[![Quote verification results: Haiku had 6 of 44 quotes not found and 4 timestamps that do not exist; Sonnet's roughly 100 items all passed; 89 of the prescription table's 1,028 cards failed](/blog/assets/posts/teaching-knowledge-distill/2-verify-en.jpg)](/blog/assets/posts/teaching-knowledge-distill/2-verify-en.jpg)

**Sampling is cheaper than the full run, and it can be tested.** The full run would cost about 26 million tokens, and 22 interviews were enough to yield 464 clusters. I tested with 12 out-of-sample interviews, and coverage fell between 65% and 80%. The extracting agent itself warned that its tagging ran wide, so real coverage may be somewhat lower.

**I rule on contradictions, and I often say no.** There were 22 items in three batches. In the last batch, when merging into the course materials, the AI gave me 10 suggested changes. I answered not adopt on 5, adopt with exceptions on 2, and adopted only 3 outright. The decision rules were derived by AI from cases: "when to start timing" drew on 43 cases and "which CR difficulty to practice" on 28, 71 case rows in total, each with the quote and timestamp. After reading them I corrected only one thing: that one was a student's slip of the tongue.

**After a ruling, wire it to where it is used.** The results of the 22 rulings went into 29 places in the course materials, and were synced to the knowledge base, the website and the handouts. The one-page exam-day cards also carry a retirement condition: if a question type is hit on time for 10 questions in a row with no looking back, the card retires, and it comes back if the error rate rises again two weeks later.

**A problem found.** In the score-report analysis on the same corpus, one agent treated "question order" as the table's row order, and 25% of the sessions were misaligned. After the fix, three conclusions flipped. The agent caught it itself on a re-run and reported it openly. So verification cannot stop at quotes. It has to check the assumptions about data structure too.

## The prompts I gave while building it

These are the words I used with the AI during this period, mostly from one conversation on Oct 3. After each one I add a line on how to adapt it.

**1. Do not run everything, sample first**

> You should be smart about this. Don't dispatch so many subagents.

> (translated from Chinese)

Adapt it: replace "subagent" with any job where a lot of files must be read, and ask first whether sampling would work.

**2. Ask how much it covers**

> So how much of my teaching method does this small set of transcripts cover? Can we spot-check from outside the sample?

> (translated from Chinese)

Adapt it: when the AI finishes synthesizing, do not trust it yet. Ask it to test against material it has not read, and see how much is covered.

**3. Make the checking cheap too**

> Go and actually spot-check outside the sample, but do you really need to dispatch six? Can't one agent just sample six sessions?

> (translated from Chinese)

Adapt it: when the AI's plan costs too much, ask directly for a cheaper one, for example one agent handling several files.

**4. Separate thinking from labor**

> You handle direction and verification. Subagents handle investigation and reading files. Anything that needs a lot of tokens goes to subagents, but you handle the key direction, thinking and verification. Okay?

> (translated from Chinese)

Adapt it: hand the heavy file reading to cheaper helpers, and keep the expensive model for planning and acceptance.

**5. Rule on an old version**

> The percentile-slope allocation has been dropped. Now it is all the sweet spot. I agree with the rest.

> (translated from Chinese)

Adapt it: when the AI lists old versions, say directly which one is dropped and what is used now, and cover the rest with "I agree."

**6. Write the condition when you say no**

> Not adopted | I rarely bring up quasi mock exams lately. Only if the student has six weeks do I schedule one week of quasi mock exams (in the second-to-last week before the test). If there are not six weeks, I take them out. I agree with the rest.

> (translated from Chinese)

This was my reply to one of the 10 suggested material changes the AI prepared. Adapt it: when you disagree, do not just say no. Write the condition under which you actually do it, because that sentence is what the knowledge base needs.

**7. Too many things to review**

> There are too many review pages. Cut them down and merge them. I can't review that many.

> (translated from Chinese)

Adapt it: your time is the most expensive. Ask the AI to filter first and leave only the items that need your judgment.

**8. What you make must connect to where it is used**

> Have the things you produced been connected to the existing spec? If they are not connected, they just become orphans and never get used.

> (translated from Chinese)

Adapt it: every time something new is produced, ask whether it has been connected to a place that actually gets read, such as lesson prep, Q&A or the syllabus.

## Starter prompt template

Paste this to an AI that can read your folder. It reads the files, counts and verifies, and you only look at the results and decide which items to carry out. Replace the parentheses with your situation:

```text
I want to distill (my folder of teaching transcripts / handouts / articles) into a teaching knowledge base that you will look up when preparing lessons and answering questions.

1. First count how many transcripts the folder holds and how long each is, and estimate how many tokens reading all of them would take. If that exceeds (my budget), switch to stratified random sampling and tell me how many you will sample and why that is enough.
2. Pick one to three transcripts for a pilot. Every extracted item must carry my original words (copied verbatim, 20 to 120 characters) and a timestamp, with fields for (diagnosis / method / explanation / estimate). When done, check with a program that each quote is a substring of the source, and report the mismatch count the program actually printed. Do not just say they match.
3. After the pilot passes, process the sampled transcripts with the same spec. Verify every item by program again. Drop any item whose quote does not match, and do not edit it.
4. When synthesizing, write only what the transcripts contain. Add no domain knowledge of your own and make no judgments of good or bad. After each claim, mark "appears in X of N files."
5. Turn contradictory versions (different years, different situations) into a ruling list: for each item, show both versions with their quotes and dates, and put the list at the top of the document. I will answer adopt or not adopt item by item. Record my reasons beside each in my own words, and mark dropped old versions "history only."
6. Then draw (a number of) transcripts you have not read to test coverage, and tell me which places the knowledge base should be wired into where I will use it (lesson prep, Q&A, syllabus), and under what condition an item should retire.
```

## Appendix: how it is built

This section is for people who want to build it themselves. The flow follows my actual extraction spec and verification script, and the code is a trimmed version.

### Extracting and verifying one transcript

An extraction agent reads a transcript and writes one JSON file, and a verification program then checks each item against the source. The order is:

[![Sequence for one transcript: the main thread dispatches an extraction agent, the agent reads the full text, writes JSON and runs a program itself, the main thread re-runs the verification program independently, only passing items go to synthesis and mismatched items are dropped](/blog/assets/posts/teaching-knowledge-distill/3-sequence-en.jpg)](/blog/assets/posts/teaching-knowledge-distill/3-sequence-en.jpg)

The extraction spec has five iron rules: every item carries a timestamp and a quote; a quote must sit inside a single turn of speech and never join two; anything the transcript does not say is left as an empty array, never guessed; category fields may use only pre-listed values; and the whole file is read before output. Transcripts are speech-recognition output, with misrecognized words and wrong speaker labels, so "who said it" is judged from the content and noted in a field.

The minimal structure of one item is:

```json
{
  "diagnoses": [
    {"section": "CR", "root_cause": "technique_gap",
     "summary": "One plain sentence: where the teacher judged the problem to be",
     "ts": "00:18:16", "quote": "A continuous passage copied verbatim from the transcript"}
  ]
}
```

The core of the verification program is three checks: whether the quote, with whitespace removed, is a substring of the source with whitespace removed; whether the timestamp exists among the turn headers; and whether the items are spread over the whole session instead of only the first half.

```python
import re

def squash(s):
    return re.sub(r"\s+", "", s)

def check(items, transcript):
    flat = squash(transcript)
    headers = {m.group(1) for m in re.finditer(
        r"^@\S+\s+(\d\d:\d\d:\d\d)\s*$", transcript, re.M)}
    bad_quote = [i for i in items if squash(i["quote"]) not in flat]
    bad_ts = [i for i in items if i["ts"] not in headers]
    return len(items), len(bad_quote), len(bad_ts)
```

The real script also checks whether a category field uses a value outside the list, and the share of timestamps past 60% of the session (below 15% is read as having read only the first half). A file fails if the mismatch rate exceeds 10%, if there is an enum error, or if the late share is too low. The spec also says that in the formal pipeline an item with a mismatched quote is dropped whole.

### How contradictions are ruled on

The synthesis step does one thing: group the versions found in the corpus and record how many sessions each appears in, plus the earliest and latest dates. When one topic has different versions, it does not pick one. It lists them all.

[![Decision flow for contradictions: when a topic has different versions, first check whether they are the same thing in different situations; if so, merge and mark the session count; if not, put it on the ruling list; I answer adopt or not adopt with a reason; adopted becomes the current rule, dropped is marked history only; a decision rule is derived by an agent from cases and then corrected by me](/blog/assets/posts/teaching-knowledge-distill/4-contradiction-en.jpg)](/blog/assets/posts/teaching-knowledge-distill/4-contradiction-en.jpg)

For decision rules that need a criterion (for example when to start timing), I first ask an agent to derive it from cases. Each case is one row with the student's data at the time, my prescription, the quote and the timestamp, so what I review is 71 rows of evidence.

### The states of one claim

Each claim in the knowledge base has a state, and only a claim that reaches the last stage is read during lesson prep and Q&A.

[![States of one claim: just extracted it is unverified; after a program checks the quote it has evidence; after grouping it shows a session count; if it conflicts with another version it waits for a ruling; after my ruling it is current or history only; a current claim is wired to where it is used; later it can be overturned back to awaiting ruling, or retired when its exit condition is met](/blog/assets/posts/teaching-knowledge-distill/5-claim-states-en.jpg)](/blog/assets/posts/teaching-knowledge-distill/5-claim-states-en.jpg)

### Build it yourself: the minimal version

1. An extraction spec in which every item has a quote and a timestamp.
2. A comparison program that drops any item whose quote is not a substring of the source.
3. A pilot on one to three files, then scale up once the spec is fixed; sample to saturation instead of running everything.
4. Synthesis that writes only what the corpus contains, with a session count on every claim.
5. A ruling list where you answer only adopt or not adopt, and write the reason.

That's it.
