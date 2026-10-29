---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-27T04:00:00Z
title: "Turning Lesson Transcripts into a Teaching Spec: One AI Drafts, Another Finds Faults, I Only Decide"
slug: en/teaching-spec-from-transcripts
featured: false
draft: false
tags:
  - ai-workflow
  - teaching
  - ai-education
description: 'My one-on-one lessons ran 51% over schedule. I went back to the lesson transcripts, had one AI write up my teaching rules and another hunt for faults, and only made decisions on a single checklist myself. The method, the numbers, what I actually told the AI, and a prompt you can paste.'
---

I teach one-on-one tutoring sessions regularly. Recently, I asked an AI to organize how I actually teach into a set of rules. Moving forward, I follow these rules whenever I prep for class or write post-class notes. I call this my teaching spec. This spec was extracted directly from lesson transcripts. One AI looked back through the transcripts, reconstructed what actually happened in class, and drafted the rules. A second AI focused entirely on catching mistakes. My only job was to go down a web checklist and make decisions line by line. Even once a rule is set, it is never carved in stone. If something comes up in the next class, we might toss it out and rewrite it on the spot.

This post walks through where I was originally stuck, how this spec evolved, the numbers I measured, and the exact words I used with AI. At the end, I also included a starter prompt you can paste directly into an AI. If you want to see the flowcharts and technical details, feel free to jump straight to [Appendix: Technical Approach](#appendix-technical-approach).

## Where I Was Stuck

The most obvious issue was that my classes ran over time. I pulled up transcripts from 15 one-on-one sessions to check the actual time spent: 1,320 minutes scheduled, roughly 1,990 minutes delivered. That was 51% over schedule, meaning about 11 unbilled hours. When I looked into why, I realized my class time had zero protection. I never checked before class whether the student was ready. Topics we had agreed to cover got pushed aside. Whenever I demonstrated something, I ended up taking up all the time. Nobody checked whether the student actually understood the material. Between sessions, the student and I had no contact at all.

Another issue was that even with a spec written down, classes continued as usual. After the spec had been in place for a while, my actual teaching drifted further and further from the written rules. Here is what I told the AI at the time (the "spec" mentioned here refers to this teaching spec):

> Things have drifted quite a bit since we set the spec.
> (translated from Chinese)

When I compared them side by side, I found that some rules in the spec had never once happened in class. Meanwhile, things I did constantly never made it into the spec.

If you simply ask an AI to write a spec, it usually describes an "ideal class" that bears no resemblance to how you actually teach. Without two crucial steps—first reading the original records to see what actually happened, and bringing in a second AI to independently poke holes—the AI's initial draft always runs into trouble. For example, when the AI was compiling an appendix once, it quietly omitted real steps and even hallucinated a command that never existed.

Finally, there was the issue of my own time. My time belongs on making decisions. I should not spend it drafting rules myself. The AI would list items requiring my decision on a web checklist, one item per row, which I call the review page below. Still, this review page kept growing longer and longer. Several times I pushed back because it was simply too long and had too many items. The more items listed there, the more of my time it took up.

## What I Wanted, and How It Evolved

The division of labor I wanted was actually very simple. Extracting key points from transcripts, drafting rules, and catching mistakes should all be handled by AI. These tasks had to be split across different AIs so that the same AI was never drafting and grading its own work. I should only step in at the decision-making stage, opening a web checklist and making one decision per row.

[![The seven steps for turning transcripts into a spec and who handles each step: measure the problem first, review transcripts to see what actually happened, draft, have a second AI catch errors, I make decisions, codify into rules, and apply in the next class, with only step five handled by me](/blog/assets/posts/teaching-spec-from-transcripts/1-loop-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/1-loop-en.jpg)

Here are the key turning points, arranged by date:

**8/29: Measure first.** I went through transcripts from 15 one-on-one sessions and measured that 51% overtime mentioned above. The spec was on its third version at the time. This version started directly with this number. It did not start from an ideal picture of what a class should look like.

**9/25: The measurement overturned itself.** I took transcripts from 8 sessions and recalculated where class time went. The first calculation showed that time spent on tangents I initiated accounted for 34%. After switching to a new criterion and recalculating, that dropped to 15.6%. Since the initial result was overturned, I recorded the new figure in my lesson prep materials.

**9/26: A post-class revision cycle.** That day, the AI drafted class notes for me. I manually made changes in 6 places, and then immediately told it to review:

> Review what I changed this time, check whether the spec covers it, and suggest how you would revise it.
> (translated from Chinese)

The AI generated a table of proposed revisions. Once I approved them, it updated the spec directly, along with the operational guide it usually follows when writing notes.

**10/8: Moving to the fifth version.** I felt my actual teaching had drifted too far from the spec again. So I ran 4 AIs in parallel, having each read an entire transcript of 110,000 to 160,000 characters. The coordinating AI matched each finding to its timestamp, verifying it sentence by sentence against the source before adopting it. Along the way, it even caught that one post-class review had used old criteria before they were relaxed. In the end, the AI sorted the changes into three categories: items to remove outright, items with the right intent that needed rephrasing, and things I did constantly that were missing from the spec. I replied with a single message: "I agree with all three categories."

## Real-World Testing

What I measured here was how the spec grew. I teach two types of one-on-one classes: one on using AI, and one for the GMAT (the exam for business school admissions). I maintain a separate spec for each. Over two months, the specs moved from version three to version five, with the GMAT spec going through two thorough rounds of decisions. Every single baseline was aligned directly with what actually happened in the transcripts.

[![Two sets of numbers calculated from transcripts: 15 sessions scheduled for 1,320 minutes took roughly 1,990 minutes, 51% over schedule; class density was 34% under the initial criteria, dropping to 15.6% after recalculating with new criteria](/blog/assets/posts/teaching-spec-from-transcripts/2-numbers-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/2-numbers-en.jpg)

**Measurements can overturn themselves.** For the class time figures, the first calculation came out to 34%. After recalculating under the new standard, it dropped to 15.6%. If I had never gone back to the transcripts to recalculate, that 34% would have been written straight into the spec.

**Independent critique actually catches mistakes.** When the draft of the GMAT spec was reviewed by the strongest current AI model, it flagged 17 items at once. In the end, 15 were adopted and 2 were partially adopted. How each item was handled and the reasoning behind it are fully documented in the spec's appendix. For the student-facing guide, I asked the AI to roleplay a non-technical student in each round and follow the steps from scratch. The first round alone uncovered 25 friction points, 7 of which would have left a student completely stuck.

**Running more review rounds will not fix the issue; you need to change the structure.** When reviewing student documents this way, about 6 new blockers popped up in every round, continuing all the way through the fifth round. Looking deeper, I found three structural root causes: the same information was scattered across 5 documents, 2 languages, and 12 cross-references; the reviewing AI had no memory of previous rounds; and asking whether a beginner might get confused has no natural end. The eventual solution was keeping just one master template from which all other files are automatically generated, backed by an automated check that blocks errors immediately. I also consolidated about 100 review findings into a single checklist to rerun every time, while setting clear exit criteria: pass when critical blockers hit zero, without blocking on minor issues. As a result, the findings converged by the seventh round. Another example was the post-class reviews: previously categorized by filename, some were missed by automated checks. Once categorized by content, the scope expanded from 11 files to 21 files, immediately revealing that all 21 were missing three required items.

**My time went toward making decisions.** The GMAT spec went through two decision rounds, with review pages containing 17 and 11 items respectively. The second round was not scheduled in advance. It grew out of comments I added in round one: four questions required factual lookups before deciding, and those lookups yielded the 11 items for round two. One item was "delays in course access." Checking the records showed that every single case was on a date requested by the student, so we closed it immediately. By the time we reached the fifth version, I completed the update with a single message. The first version of the review page contained too much jargon. After I pushed back, the AI rewrote it using plain language.

[![Review page layout: 17 items in round one spawned four lookup tasks from my feedback, which became 11 items in round two; each row lets you choose adopt, adopt with exceptions, or reject, with a one-sentence rationale; items that do not require my judgment never enter the review page](/blog/assets/posts/teaching-spec-from-transcripts/6-review-page-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/6-review-page-en.jpg)

The graphic above was reconstructed from the actual review page format.

**Automated checks also need reverse testing.** One check specifically catches content containing unexplained internal code names. Before putting it into production, I tested it with 7 test cases: all 4 cases that should have been blocked were blocked, and all 3 cases that should have passed were allowed through.

Once the spec went live, whether classes ran more punctually and whether students improved are two things I honestly have not started measuring yet. What I have actually measured so far is simply whether the spec aligns with how I teach in practice.

## Exact Words I Said to AI Along the Way

Below are a few exact quotes I said to AI throughout this process. After each quote, I added a line explaining how to adapt it to your own situation.

**1. Move decisions out of the chat and onto a page**

Originally, the AI sent long strings of multiple-choice questions right inside the chat. I pushed back immediately (the "ruling page" mentioned here is the review page described above):

> Move this to a review page. I'll make my decisions there.
> (translated from Chinese)

For your own situation: When an AI dumps a long list of multiple-choice questions for you to answer in chat, tell it to build a web page instead, with one decision per row so you can just click through it.

**2. Push back if it gets too long**

Whenever the review page grew too long, I asked:

> Are you sure I really need to rule on this many items?
> (translated from Chinese)

For your own situation: When the review page exceeds what you are willing to read, ask this question. Items presented to you should be filtered beforehand, keeping only those that actually require your judgment.

**3. Decide in batches**

This was the 10/8 update mentioned earlier, where the AI grouped changes into three categories. I replied:

> I agree with all three categories.
> (translated from Chinese)

For your own situation: Ask the AI to group proposed changes into categories, clearly stating the purpose and rationale for each. When grouped cleanly, you can resolve everything with a single reply.

**4. Add a quick reason why**

During a discussion on how to log my lesson prep hours, I added a quick rationale while deciding:

> The standard must reflect actual prep time. The goal is shortening preparation time, rather than counting fewer hours.
> (translated from Chinese)

For your own situation: Add an extra line explaining your reasoning when you make a choice. That single sentence later shaped multiple rules on how prep hours are recorded. The reasoning carries over to future scenarios far better than a simple choice.

**5. Tell it to review after you make edits**

Every time I manually edit something the AI generated, I send this line:

> Review what I changed this time, check whether the spec covers it, and suggest how you would revise it.
> (translated from Chinese)

For your own situation: After you tweak an AI's output, tell it to compare your edits against the current spec and fill in whatever was missing.

**6. Ask directly when unsure about your own practice**

Whenever I was uncertain about my approach, I asked directly:

> Is my teaching methodology still not fully formed?
> (translated from Chinese)

For your own situation: Feed this question to an AI and ask it to answer based on your actual records. The answer I got was that my teaching methods were stable. What kept changing were the specs, lesson packages, and student profiles. What remained unverified was whether the methods were effective and whether promises to students were kept. So we created a dedicated checklist on the spot to track what I promised each student and whether it was delivered.

## Starter Prompt Template

If you want to grow a spec out of your own class records, you can start with this prompt. Replace the bracketed text with your own details, and paste it directly into an AI that can access your local files:

```text
I want to turn my lesson transcripts into a teaching spec—a set of teaching rules for an AI to follow when prepping classes and writing post-class notes. The transcripts are in (folder path). Please read (number) transcripts first, calculate (the symptom I want to improve, such as how many minutes classes ran overtime or how many times promised tasks were skipped), reconstruct how I actually teach from the transcripts, and draft a set of rules. Flag anything uncertain, and organize items requiring my input into a single list. Give me a plan first, and I will review it before you begin.
```

## Appendix: Technical Approach

This section is for anyone looking to build a similar setup themselves. Technical terms, file formats, and rules are gathered here.

### Plain-Language Terms and Their Technical Equivalents

- "A set of teaching rules for AI": The teaching spec—the rule file an AI reads before prepping classes or drafting notes.
- "The operational guide it follows when writing notes": A Claude Code skill.
- "Running 4 AIs in parallel to read transcripts": 4 parallel subagents.
- "The coordinating AI": The main session—the conversation you are actively interacting with.
- "A second AI dedicated to catching mistakes": The attacker described below, run in a separate session without prior conclusions.
- "The strongest current AI model": High-tier models for drafting and attacking; extraction can use inexpensive models.
- "Automated checks that block errors immediately": Pre-write hook and lint checks.
- "Lesson prep materials": Asset files recording measurement results.

### Overall Workflow: Who Hands What to Whom

One spec generation cycle involves 6 roles: the read-only transcripts, an extractor (which can use an inexpensive model), a drafter and an attacker (each using a high-tier model), the main session (your active chat), and myself. The 3 AI roles are dispatched in three separate steps, avoiding the trap of letting an AI draft and review its own work in one go.

[![Sequence diagram for one spec generation cycle: transcripts are read by the extractor; extraction files with verbatim quotes and locations are handed to the main session; after spot-checking timestamps, the main session passes only extraction files to the drafter; the draft goes to an attacker free of prior conclusions; the attacker reports errors and undetermined areas; the main session delivers a filtered review page to me; I return decisions with a one-sentence rationale; the main session codifies the rules and flags them for initial trial](/blog/assets/posts/teaching-spec-from-transcripts/3-sequence-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/3-sequence-en.jpg)

The drafter reads only extraction results. The attacker runs in a fresh session, carrying zero conclusions from earlier rounds.

### Transcript Extraction

Extraction uses a standardized questionnaire where every entry must include a verbatim quote and its exact location. For the GMAT spec, an inexpensive model ran in 11 batches, reading records from 47 students and 14 consultation clients to generate 61 extraction files. A high-tier model then drafted the spec by reading only those extraction files.

The first rule in the extraction spec states: every entry must include a `quote` (verbatim, 20 to 120 words) and a `pos` (timestamp or line number). Upon receiving the entries, the main session runs a script to verify that `quote` is an exact substring of the original text. Any entry with a mismatched quote is discarded entirely. Here is the minimal version:

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

Run `python3 -I verify_quotes.py extract.json transcript.txt`. This script verifies whether the quote is present. It cannot detect whether a statement was taken out of context. For that reason, the main session must also spot-check timestamps to inspect context in the original text. That is how we caught a post-class review using old criteria before they were relaxed during the version five update.

Every rule must be backed by at least 2 real cases. Therefore, the rule table includes a column for "Supporting Case Count." Any row with fewer than 2 cases is moved to "Pending Verification."

### Drafting and Attacking

The drafter reads only extraction files. The attacker runs in a separate session without prior conclusions, completely blind to the drafter's reasoning. The attacker's instructions must explicitly forbid assuming the draft is correct, restrict reporting to errors and undetermined areas, and state the exit criteria. Otherwise, it will keep finding new issues forever. Here is an example, with brackets left for you to fill in:

```text
You are the attacker. Below are the draft spec and the corresponding transcripts.
Do not assume the draft is correct. Check each item against the transcripts.
Report only two categories: actual errors, and areas you cannot determine.
Exit criteria: (for example: zero critical blockers). Stop once achieved; do not list secondary issues.
```

Alternatively, the attacker role can be swapped for a reader: ask a high-tier model to roleplay a non-technical student in each round, walking step-by-step through the student documentation.

### Review Pages and Decision Logs

Not every item belongs in front of me. Everything is filtered before reaching my screen:

[![Decision tree for an item surviving the attack: items backed by only one case move to pending verification; items requiring lookups turn into verification tasks for the next round; items needing no judgment from me are resolved by AI with a log entry; remaining items become a row on the review page for my decision, with verbatim reasoning recorded next to the rule, tagged with date, author, first-trial status, and review date](/blog/assets/posts/teaching-spec-from-transcripts/4-decision-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/4-decision-en.jpg)

Each row on the review page represents a single decision, complete with options (Adopt, Adopt with Exceptions, Reject) and a comments box. The bottom lists only items with exceptions, allowing one-click copying back into the chat. I generate this page using a skill called `review-page`. When decisions are written back to the spec, the decision log uses four fixed columns:

| Decision | Added Rationale (Verbatim) | Completed | Todo |
|---|---|---|---|
| Adopt | My offhand remark | Rule updated | Items for follow-up review |

Every amendment includes a date and an author tag. Overruled rules are marked as "deprecated" and retained in the decision log, rather than silently deleted.

### The Lifecycle of a Rule

New rules are never treated as final right away. They are tagged as "Initial Trial: Under Observation," accompanied by a scheduled follow-up task with a due date. During follow-up, we check whether the rule is actually functioning. If it fails in practice, we drop it. Teaching practices that drift from the spec are logged as "known variations," promoted to official rules only after appearing three times or proving effective.

[![State diagram of a rule: an approved draft becomes an initial trial under observation with a review date; it becomes finalized if running smoothly on review, or dropped if impractical; known variations are promoted to final rules upon appearing three times or proving effective; finalized rules overturned by actual practice become deprecated, preserved in the decision log](/blog/assets/posts/teaching-spec-from-transcripts/5-state-en.jpg)](/blog/assets/posts/teaching-spec-from-transcripts/5-state-en.jpg)

Rule enforcement falls into three levels: write-blocking gates (hooks, linter checks, script-owned fields), post-hoc reminders, and written rules paired with periodic audits. Anything that can be automated should be built to block errors the moment they happen. Once a gate is configured, reverse testing verifies that it catches what it should catch and allows what it should allow. When the same type of issue surfaces for the third time, stop and ask what structural flaw causes it to keep appearing, then record that answer in the commit message.

### Building It Yourself: The Minimal Version

1. One symptom, paired with a measurable number (how many minutes classes ran overtime, or how many times promised tasks were skipped).
2. One extraction file, where every entry has a `quote` and a `pos`, verified using the script above.
3. One round each of drafting and attacking, with the attacker blind to earlier conclusions and given explicit exit criteria.
4. One review page collecting items that require your judgment, one decision per row, keeping your verbatim rationale next to each rule.
5. Tag finalized rules as "Initial Trial" and set a follow-up review date.
