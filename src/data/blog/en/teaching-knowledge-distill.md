---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-28T04:00:00Z
title: "Turning Years of Teaching into a Knowledge Base AI Can Look Up: Catching AI's Fake Quotes with Code, and Settling My Own Contradictions"
slug: en/teaching-knowledge-distill
featured: false
draft: true
tags:
  - teaching
  - ai-education
  - ai-workflow
description: 'I gave AI over two hundred transcripts of recorded student interviews and had it build a teaching knowledge base it looks up when preparing lessons. The AI said every quote was exact; a small program found 6 of 44 did not match. This post covers how I caught the errors, how I settle it when my own advice contradicts itself, and a starter prompt you can paste straight to an AI.'
---

I have taught the GMAT (the English-language test for applying to business school) for more than ten years. Recently I handed a batch of recorded student-interview transcripts to an AI and had it build a knowledge base it will look up later when preparing lessons and answering students' questions. Every statement in it carries my original words and the timestamp in the recording, so it can be checked, and where my own advice contradicts itself over the years, I make the call.

This post covers four things in order: where I was stuck, what I wanted the knowledge base to look like, the numbers from the actual run, and the exact words I said to the AI. At the end there is a starter template you can paste straight to an AI. If you want to build it yourself, the technical details are in the [appendix: how it is built](#appendix-how-it-is-built).

## What was bothering me

The first problem was that I had plenty of material, but the AI could not read "how I teach." I first turned all students' score reports and interview recordings on my cloud drive into transcripts. My expectation of the AI was simple: the transcripts could fill in my teaching thinking and make the score-report analysis more systematic. The interviews alone came to 202 transcripts, and once converted they were just a pile of files.

The second problem was that reading everything is expensive. I started with the most obvious approach: one AI helper per transcript. After 20 of them, the total was about 2.57 million tokens (the unit AI uses to measure usage), roughly 130,000 per transcript. At that rate, all 202 would cost about 26 million tokens.

The third problem was that the AI said it was right and I could not trust it. I asked the cheapest AI model to go through one interview of about 62 minutes and pull out my judgments about the student, the practice I recommended, and my estimates, with my original words attached to every item. It returned 44 items and wrote in its report that every quote was copied verbatim from the source. I wrote a small program to compare them. Of the 44 items, 6 quotes could not be found in the transcript, and 4 timestamps did not exist at all.

The fourth problem was that my own advice fights itself. On the same question, the 2024 me and the 2026 me say different things. For how much prep time each section should get, the old advice looked at how many percentile points one more score point buys in each section, and the new advice looks at how many score levels each section is from its "sweet spot." On whether a question's position affects the score, the old and new advice say opposite things. The AI just lists everything it sees in the transcripts. It does not know which one is the current me.

## What I wanted, and how it changed along the way

I wanted a teaching knowledge base the AI looks up when preparing lessons or answering students, and it had to do three things. First, every statement carries my original words and a timestamp that a program can check. Second, every statement shows how many interviews it appears in, so something said once is not treated as my method. Third, where advice contradicts itself, I make the call, the calls sit at the very top of the document, and dropped old advice is kept only as a record.

[![Six steps from transcripts to knowledge base: AI does extraction and synthesis, a program checks the quotes, I appear only at the ruling step, and afterwards it is wired to where it is used with an exit for retirement](/blog/assets/posts/teaching-knowledge-distill/1-pipeline-en.jpg)](/blog/assets/posts/teaching-knowledge-distill/1-pipeline-en.jpg)

The process went roughly like this, with the key turns concentrated on Oct 3.

**Oct 3, morning: a small pilot first.** I had three different AI setups follow the same set of extraction rules on the same transcript for comparison. The cheapest model's result is the 6 wrong items above. So two rules were added: a quote may not join two separate turns of speech into one, and the AI must run a program itself and report the mismatch count the program actually printed, never just say "all correct."

**Oct 3, morning: switch to sampling.** After I saw that reading everything would cost 26 million tokens, I called it off and switched to a random sample of 22 interviews, sampling until nothing new turned up. Questions that truly needed every transcript were answered with keyword search instead.

**Oct 3: checking against unread interviews, then deciding item by item.** The AI grouped what was said in the 22 interviews into 464 groups and wrote an overall summary of my teaching method. I then asked it to draw 12 more interviews it had not read, to see how much the summary covered. After that I went through 22 places where I contradicted myself, in three batches, writing adopt or not adopt with a reason for each.

**Oct 7: "when not to use this" gets filled in only when needed.** Separately, I had built a table from my one-on-one tutoring transcripts: "where the student gets stuck, and how I handle it." Every row has a column for "when not to use this move," which came to about 528 cells, too many for me to review. So the rule became: whichever row a lesson handout uses, I fill in that one while reviewing the handout.

**Oct 18: overturning myself once.** For guessing on math questions when time runs out, my rule had been "leave at least 0.5 minutes." I later decided on no lower limit: guess and move on. That rule was one I had settled myself, and I overturned it.

## What I measured

The scope is the interview transcripts: a sample of 22 from 202, 12 unread interviews drawn for checking, plus 1,028 rows from the tutoring table. The comparison is the same rules and the same transcript run on different AI models, and the difference before and after the program checks.

**A program checking the quotes catches errors the AI says are not there.** On the same transcript with the same rules, the cheapest model produced 44 items. The program found 6 quotes that did not match and 4 timestamps that did not exist, while the model said everything matched. The next model up produced about 100 items and the program found 0 mismatches. The tutoring table was bigger: 1,028 rows checked one by one, and 89 (about 9%) failed. They are kept, but none of them can carry a teaching method on its own.

[![Quote verification results: the cheapest model had 6 of 44 quotes not found and 4 timestamps that do not exist; the next tier up had roughly 100 items that all passed; 89 of the tutoring table's 1,028 rows failed](/blog/assets/posts/teaching-knowledge-distill/2-verify-en.jpg)](/blog/assets/posts/teaching-knowledge-distill/2-verify-en.jpg)

**Sampling is cheaper than reading everything, and you can check it afterwards.** Reading everything would cost about 26 million tokens, and 22 interviews were enough to produce 464 groups. I checked against 12 unread interviews, and coverage fell between 65% and 80%. The AI doing the work warned me itself that its standard for "covered" was loose, so real coverage may be somewhat lower.

**I make the calls on contradictions, and I often say no.** There were 22 items in three batches. In the last batch, as things went into the course materials, the AI gave me 10 suggested changes. I answered not adopt on 5, adopt with exceptions on 2, and adopted only 3 outright. Some rules need a criterion first, so I had the AI work backwards from past student cases: "when to start timed practice" drew on 43 cases and "which difficulty to practice for critical reasoning (CR) questions" on 28, 71 cases in total, each with the quote and timestamp. After reading them I changed only one thing: that one was the student's own slip of the tongue.

**After a call, put it where it will actually be used.** The 22 calls improved 29 places in the course materials, and were synced to the knowledge base, the website and the handouts. The one-page cards students take into the exam also say when they can be put away: if a student gets 10 questions of one type in a row right within time, with no going back to recheck, the card is put away, and it comes back if the error rate rises again two weeks later.

**A problem found.** In the score-report analysis on the same material, one AI helper treated the question numbers on the score report as the order of rows in a table, so 25% of the sessions were lined up wrong. After the fix, three conclusions flipped completely. It found this itself on a re-run and reported it on its own. So checking cannot stop at quotes. It also has to check the AI's assumptions about what the data looks like.

## The prompts I gave while building it

These are the words I used with the AI during this period, mostly from one conversation on Oct 3. Some words in them are shorthand I use with the AI, so I give the background before each one, and after each I add a line on how to adapt it.

**1. Do not read everything, sample first**

An AI can send out many small helpers to read files in parallel (the "subagents" in the quote are these helpers). It planned to send one per transcript, and I told it to change course:

> You should be smart about this. Don't dispatch so many subagents.

> (translated from Chinese)

Adapt it: for any job that means reading a lot of files, first ask the AI whether sampling would work.

**2. Ask how much it covers**

> So how much of my teaching method does this small set of transcripts cover? Can we spot-check from outside the sample?

> (translated from Chinese)

Adapt it: when the AI finishes summarizing, do not trust it yet. Ask it to check against material it has not read, and see how much is covered.

**3. Make the checking cheap too**

The AI proposed sending six helpers to read one interview each, and I asked whether it could be cheaper:

> Go and actually spot-check outside the sample, but do you really need to dispatch six? Can't one agent just sample six sessions?

> (translated from Chinese)

Adapt it: when the AI's plan costs too much, ask directly for a cheaper one, for example one helper handling several files.

**4. Separate thinking from labor**

"Tokens" here is the AI usage unit from earlier:

> You handle direction and verification. Subagents handle investigation and reading files. Anything that needs a lot of tokens goes to subagents, but you handle the key direction, thinking and verification. Okay?

> (translated from Chinese)

Adapt it: hand the heavy file reading to cheaper helpers, and keep the expensive model for planning and the final check.

**5. Settle an old piece of advice**

The background is the prep-time contradiction from earlier: "percentile slope" is the old advice and "sweet spot" is the new one:

> The percentile-slope allocation has been dropped. Now it is all the sweet spot. I agree with the rest.

> (translated from Chinese)

Adapt it: when the AI lists old advice, say directly which one is dropped and what is used now, and cover the rest with "I agree."

**6. Write the condition when you say no**

This was my reply to one of the 10 suggested material changes from the AI. A "quasi mock exam" is a full practice run done to the real test's format before the exam:

> Not adopted | I rarely bring up quasi mock exams lately. Only if the student has six weeks do I schedule one week of quasi mock exams (in the second-to-last week before the test). If there are not six weeks, I take them out. I agree with the rest.

> (translated from Chinese)

Adapt it: when you disagree, do not just say no. Write the condition under which you actually do it, because that sentence is what the knowledge base needs.

**7. Too many things to review**

The AI turns items it needs me to confirm into web pages I tick through, and the "review pages" in the quote are those:

> There are too many review pages. Cut them down and merge them. I can't review that many.

> (translated from Chinese)

Adapt it: your time is the most expensive. Ask the AI to filter first and leave only the items that need your judgment.

**8. What you make must go where it will be used**

The "spec" in the quote means the lesson-prep rules I wrote for the AI to read:

> Have the things you produced been connected to the existing spec? If they are not connected, they just become orphans and never get used.

> (translated from Chinese)

Adapt it: every time something new is produced, ask whether it has gone into a place that actually gets read, such as lesson prep, answering students or the syllabus.

## Starter prompt template

Paste this to an AI that can read folders on your computer. It does the reading, counting and checking; you only look at the results and decide which items to carry out. Replace the parentheses with your situation:

```text
I want to turn (my folder of teaching transcripts / handouts / articles) into a teaching knowledge base that you will look up when preparing lessons and answering students' questions.

1. First count how many transcripts the folder holds and how long each is, and estimate how many tokens reading all of them would take. If that exceeds (my budget), switch to stratified random sampling and tell me how many you will sample and why that is enough.
2. Pick one to three transcripts for a pilot. Every item must carry my original words (copied verbatim, 20 to 120 characters) and a timestamp, with fields for (my judgment / method / explanation / estimate). When done, check with a program that each quote appears word for word in the source, and report the mismatch count the program actually printed. Do not just say they match.
3. After the pilot passes, process the sampled transcripts with the same rules. Check every item by program again. Drop any item whose quote does not match, and do not edit it.
4. When summarizing, write only what the transcripts contain. Add no expertise of your own and make no judgments of good or bad. After each statement, mark "appears in X of N files."
5. Turn contradictory advice (different years, different situations) into a list for me to decide: for each item, show both versions with their quotes and dates, and put the list at the top of the document. I will answer adopt or not adopt item by item. Record my reasons beside each in my own words, and mark dropped old advice "kept as a record only."
6. Then draw (a number of) transcripts you have not read, check how much the knowledge base covers, and tell me which places it should go into where I will use it (lesson prep, answering students, syllabus), and under what condition an item should be removed.
```

## Appendix: how it is built

This section is for people who want to build it themselves. The flow follows my actual extraction spec and verification script, and the code is a trimmed version.

### Technical terms the main text leaves out

- The "AI helpers" and "small helpers" in the main text are subagents: other AI instances sent out by the AI I am talking to, each reading files and reporting back. The "main thread" in the diagram below is the AI that sends them out.
- The three pilot setups were Claude Haiku, Claude Sonnet, and one especially long transcript. "The cheapest model" is Haiku; "the next model up" is Sonnet.
- The sampling was stratified random sampling; questions that needed the whole corpus were answered with a keyword script.
- The "where the student gets stuck, and how I handle it" table is what I call the sticking-point prescription table internally. Each row is a card, and the "when not to use this move" column is the misuse boundary.
- Besides checking each card's quote, I ran a misalignment control test, which put the false-match rate at about 6%.
- Checking against unread interviews is an out-of-sample check; the overall summary of my method is a teaching-system document.

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
