---
author: Dustin Yuchen Teng
pubDatetime: 2026-11-23T22:00:00Z
title: "Tired of AI Dumping Endless Multiple-Choice Lists in Chat? I Built a One-Page Review Page to Click Only Exceptions, Not Rubber-Stamp"
slug: en/review-page-decide-by-clicking
featured: false
draft: true
tags:
  - ai-workflow
  - productivity
  - non-engineer
description: 'Every time you ask AI to organize data, does it flood the chat with a long multiple-choice quiz asking if you want A or B? I replaced those to-decide lists with a one-page interactive review page: filter into two buckets first, cap each page at 7 items, let unmarked items follow the recommendation, and spend my time writing only the exceptions.'
---

This morning (2026-11-24), I asked AI to audit 229 Chinese articles on my blog and decide whether each one should be kept, merged into another post, or hidden from Google search. After AI ran the initial sorting, 74 posts were flagged as "Pending Author Decision."

If you use ChatGPT or Claude regularly, you know what usually happens next: the chat window gets flooded. AI spits out a massive list and asks you to pick A or B for every single item. You end up scrolling up and down to match your answers to the questions, typing out replies one by one, and burning out halfway through.

Instead, what landed on my screen this morning was an interactive web page trimmed down to 7 items. Out of those 74 posts, only 7 made it onto the page for my final call. The rest had clear-cut answers under our existing rules, so AI handled them directly and reported the counts afterward (the top of the page lists what it will go ahead and do). This web page is a homegrown tool I have been using for the past month: a Review Page. From 2026-10-27 to 2026-11-23, I opened 33 review pages and made 256 decisions.

## Stop Answering Multiple-Choice Quizzes in Chat. Click on a Page Instead

One of my earliest uses for the Review Page came up while I was organizing the teaching rules for our one-on-one tutoring sessions (that project started when 51% of 15 classes ran overtime, which I covered in [my earlier post on distilling a teaching spec from transcripts](/blog/posts/en/teaching-spec-from-transcripts)). Back then, one AI read the transcripts to draft the rules, a second AI independently checked for errors, and my only job was to make the final call. When the AI initially dumped a long list of multiple-choice questions into the chat, I replied straight back:

> Turn this into a review page. I'll decide inside the review page.

What I called a decision page there is the Review Page. I wrote a strict rule into my tool instructions: whenever there is a list of candidates that needs my item-by-item decision, always generate an interactive web page that opens in the browser, never a static table with no input controls where I cannot leave feedback. Every item on the page has three fixed parts:

1. **A single-proposal title**: No A-or-B quizzes or multiple-choice questions allowed. State the title directly as "Adopt A (instead of B)."
2. **Why a decision is needed**: In 2 to 3 complete, plain-language sentences explaining cause and effect, spell out where things are stuck right away and what changes if we make the switch. If it is a trade-off, state what each side gains and loses, with no cryptic shorthand that only the AI understands. Even without reading the earlier chat, I should be able to decide just from reading this box.
3. **The AI's recommendation**: Clearly mark whether it recommends "Adopt" or "Reject," ordered with "the items I am most likely to push back on at the top" rather than in file order.

Underneath each item sit three buttons: "Adopt," "Adopt with exceptions," and "Reject." Picking "Adopt with exceptions" requires typing a note in the comment box. The single biggest time-saver on the whole page is this rule: **Unmarked = Follow recommendation**.

When I agree with a recommendation, I do not even have to click. And because leaving an item unmarked means following the recommendation, the AI cannot play neutral and fill in a throwaway guess; it has to commit to a real recommendation. The page saves my clicks locally in the browser, so my progress is still there if I close the tab and reopen it. Once I finish reading, clicking "One-click copy" at the bottom copies only my exceptions and notes so I can paste them back to the AI. Looking back across those 33 pages and 256 decisions, my final call matched the AI's recommendation on 163 items (about 64%), and I only had to type out custom notes on 77 items.

## Even the Best Interface Turns into a Rubber Stamp If You Send Up Too Many Items

Buttons alone were not enough. When I revised that GMAT teaching spec, it took two rounds of decisions. The first review page had 17 items, and the notes I wrote sparked 4 follow-up questions that required checking our data first. After checking the data, the second round still had 11 items (one of them, "Course activation delay," turned out to be entirely cases where students had picked their own start dates, so we closed it on the spot). Over the next few sessions, the review pages kept creeping up in length again. Every extra row on the page was more of my time. I pushed back on the AI directly:

> Are you sure you need to put this many items in front of me to decide?

Once a list gets too long, you cannot review it carefully and you turn into a rubber stamp. The problem was that the bar for putting an item on the page was too low. Because the Review Page exists to collect item-by-item judgments, I added a filtering rule: before building the page, sort all candidates into two buckets. Only Bucket 2 gets onto the Review Page.

- **Bucket 1 (Do it directly, don't send for review)**: Has a clear recommendation, does not conflict with past decisions, can be verified or easily rolled back, and crosses no red lines. The AI executes these right away and lists them at the top of the page under "Already Handled" so I can spot-check afterward (if there are more than 5 items, the header only shows the total count and a category summary).
- **Bucket 2 (Send for review)**: Involves a value trade-off, affects real people, goes out to external recipients, cannot be undone, overturns an earlier decision of mine, or changes copywriting tone. When in doubt about which bucket an item belongs in, the test is simple: "Would he have an opinion if he saw this?" If not, it goes into Bucket 1.

Items that make it into Bucket 2 get compressed further: mechanical edits on the same topic or linked changes are merged into a single row with the number of occurrences noted inside. Informational notices that require no decision, like "Leave the other 60 items unchanged," belong only in the top summary and never take up a row of their own.

Finally, there is a **hard cap of 7 items**. If multiple reviewing AIs agree and no red line is crossed, that counts as consensus and goes straight into Bucket 1. If more than 7 items remain after filtering, the AI sends only the 7 items I am most likely to overrule, carries out the remaining reversible items as recommended, and logs them under "Already Handled." Only when red-line items alone exceed 7 is the AI required to send them in batches rather than acting on its own. That is how 229 blog posts and 74 pending items this morning came down to just 7 rows on my screen.

## The Next Step: Check How I Ruled in the Past Before Asking Me Again

Even after capping each page at 7 items, I occasionally spotted questions I had already settled weeks ago. Earlier, while reviewing the teaching spec on how to log class prep hours, I had jotted down a quick one-line rationale:

> The standard has to reflect actual prep time. The goal is to shorten prep time, not undercount it.

That single line ended up deciding how several related rules were written later, because the reasoning behind a choice travels to new situations much better than a bare A-or-B pick. Since I had already written 77 custom notes across 256 decisions, on top of my regular decision logs, I added a "Taste Judge" right before the Review Page. Before Bucket 2 items are rendered into a web page, they are checked against my past written precedents, and each item receives one of three verdicts:

1. **Precedent found**: I have ruled on the same kind of question in my written logs before, complete with the source file path and a verbatim quote. A script mechanically checks the quote word-for-word against the original file; if it does not match, the item is downgraded to a new question.
2. **Flawed question**: The premise is wrong, it bundles two questions into one, it asks something the AI could verify on its own, or it misses an obvious option. It gets kicked back immediately to be rewritten.
3. **New question**: No clear precedent exists, so it goes to me for a decision.

Among the 7 items on my review page this morning, the Taste Judge matched 3 against past precedents I had written (with sources attached) and marked 4 as new questions.

To be honest, it cannot make decisions on my behalf yet. I set a strict threshold before turning on auto-decisions: at least 20 precedents with an agreement rate of 90% or higher. As of today's tally, across 68 questions that had matching precedents, the judge's call matched my final decision on only 18 of them, an agreement rate of 26.5%. Because it is nowhere near the bar yet, I keep it in "Annotate only, don't auto-decide" mode: every item still comes to me for review, with a "Precedent: ..." tag right next to it. Once I paste my decisions back, another step logs them into the decision history. Every time I overrule the judge, that ruling becomes the precedent for next time.

## A Ready-to-Use Prompt for Your AI, Plus Where the Boundaries Are

The next time AI dumps a long multiple-choice quiz into your chat window, tell it to redo the output in three steps: filter the list into two buckets and cap pending items at 7, rewrite A-or-B questions into single proposals backed by the current pain point and a clear recommendation, and package them into an interactive web page with three buttons per row where "Unmarked = Follow recommendation" and the bottom copy button grabs only exceptions and notes.

A few practical boundaries are worth keeping in mind. A Review Page works best for deciding across multiple independent candidates, like rule trade-offs, proposed edits, or pricing options. If you are reviewing a full article, a lesson plan, or a complete proposal draft, reading the continuous text straight through is much easier than chopping it into rows. When you are already at your keyboard and just want to reply quickly in text, you can skip generating the web page and still have the AI filter the list by the two-bucket rule right inside the chat. Finally, once you set the rule that unmarked items follow the recommendation, remind the AI that it cannot fill in lazy guesses, and that whenever red-line items involving real people, external messages, irreversible actions, or overturning past decisions exceed 7, it must send them in batches rather than acting on its own.

If you want to take home the working Review Page template, the Taste Judge, and the precedent log toolkit, join my two-hour live Zoom small-group workshop on 11/28 (Sat) from 10:00–12:00 Taiwan time: "[Teach AI Your Taste: Building a Decision System Workshop](https://www.agentcrew.cc/events/ai-taste-1128)" (NT$1,600). In two hours, we will build three hands-on pieces together: your personal system card, your review system, and your precedent-based decision system, putting into practice the old imperial ideal where "memorials to the throne come with drafted rescripts, so you stop working yourself to death like the Yongzheng Emperor."

## Appendix

Here are the underlying implementation details for anyone who wants to build a setup of their own:

- **Template structure and safeguards**: Each review page is copied from a fixed HTML template, replacing only the title (in 3 places), subtitle, header summary, and the data block at the bottom of the file. Alongside the ID, title, explanation, and recommendation, each item can optionally carry a basis tag (marked strictly as "Read" or "Inferred," never a percentage or confidence score). Before writing the JSON block, `<` characters are escaped so question text cannot prematurely close the script tag. When generating a second revision of a page, original item IDs are preserved so the browser's local storage does not wipe out selections you already clicked. For reviewing social media promo drafts, there is a dedicated side-by-side template that places 1:1 or 4:5 image cards next to the source text and the copy for each platform; each post is sent for review only once, supporting three actions: approve or reject, paste a self-written version, or cancel scheduled auto-posting.
- **Vector pre-filtering and quote verification**: The precedent corpus is roughly 3,600 lines long. Before sending anything to the language model, a local embedding model pre-filters the corpus down to the 25 closest lines for each question (pulling 1 line of context before and after each match), shrinking the window to roughly 150 lines. If the pre-filter misses a line, the item simply defaults to a new question rather than slipping through unreviewed. Whenever the model claims a precedent exists, a script checks the verbatim quote against that exact line in the source file within a ±3-line window; if the quote does not match word-for-word, the verdict is automatically downgraded to a new question. Files inside private directories are never indexed into the corpus.

<!--
[Author Quotes & Quoted Phrases Source Mapping]
1. "Pending Author Decision" (「待作者裁決」): from 04-facts.md (line 15)
2. "Turn this into a review page. I'll decide inside the review page." (「改裁決頁，我在裁決頁裡決定」): from 03-earlier-article-teaching-spec.md (line 83)
3. "Adopt A (instead of B)" (「採用 A（而非 B）」): from 01-review-page-tool-instructions.md (line 53)
4. "Adopt", "Adopt with exceptions", "Reject" (「採納」、「採納但有例外」、「不採納」): from 04-facts.md (line 21) and 01-review-page-tool-instructions.md (lines 3, 41)
5. "the items I am most likely to push back on at the top" (「我最可能有意見的排前面」): from 01-review-page-tool-instructions.md (line 54, adapted from third-person to first-person)
6. "Unmarked = Follow recommendation" (「未標記＝照建議」): from 01-review-page-tool-instructions.md (line 55)
7. "One-click copy" (「一鍵複製」): from 01-review-page-tool-instructions.md (lines 3, 40) and 04-facts.md (line 23)
8. "Course activation delay" (「課程開通延遲」): from 03-earlier-article-teaching-spec.md (line 65)
9. "Are you sure you need to put this many items in front of me to decide?" (「要我裁的你確定要寫那麼多嗎」): from 03-earlier-article-teaching-spec.md (line 91)
10. "Already Handled" (「已照辦」): from 01-review-page-tool-instructions.md (lines 20, 24, 56)
11. "Would he have an opinion if he saw this?" (「他看到這條會不會有意見？」): from 01-review-page-tool-instructions.md (line 26)
12. "Leave the other 60 items unchanged" (「其餘 60 條不動」): from 01-review-page-tool-instructions.md (line 25)
13. "The standard has to reflect actual prep time. The goal is to shorten prep time, not undercount it." (「標準就是要反映真實準備時間，方向是把準備時間縮短，不是少算」): from 03-earlier-article-teaching-spec.md (line 107)
14. "Annotate only, don't auto-decide" (「只標註、不代決」): from 04-facts.md (line 11)
15. "Precedent: ..." (「先例：……」): from 04-facts.md (line 11) and 01-review-page-tool-instructions.md (line 32)
16. "Teach AI Your Taste: Building a Decision System Workshop" (「把你的品味教給 AI：打造裁決系統工作坊」): from 04-facts.md (line 27)
17. "memorials to the throne come with drafted rescripts, so you stop working yourself to death like the Yongzheng Emperor" (「奏摺附票擬，不再當過度勤政的雍正」): from 04-facts.md (line 29)
18. "Read", "Inferred" (「讀過」、「推測」): from 01-review-page-tool-instructions.md (line 41)

[Numbers Source Mapping]
1. 2026-11-24 (this morning / stats date): from 04-facts.md (lines 1, 9, 13)
2. 229 Chinese articles: from 04-facts.md (line 14)
3. 74 posts flagged as "Pending Author Decision": from 04-facts.md (line 15)
4. 7 items (trimmed count on this morning's review page): from 04-facts.md (lines 16, 17)
5. 2026-10-27 to 2026-11-23 (recorded period): from 04-facts.md (line 4)
6. 33 review pages: from 04-facts.md (line 5)
7. 256 decisions: from 04-facts.md (line 5)
8. 15 classes, 51% overtime: from 03-earlier-article-teaching-spec.md (lines 12, 13, 21, 41, 57)
9. 2 to 3 sentences (2-3 complete cause-and-effect plain-language sentences): from 01-review-page-tool-instructions.md (line 52)
10. 3 buttons (three buttons): from 04-facts.md (line 21)
11. 163 items matched AI's recommendation, about 64%: from 04-facts.md (line 6)
12. 77 items with custom written notes: from 04-facts.md (line 7)
13. Two rounds of decisions, 17 items in round one, 4 follow-up data questions, 11 items in round two, 1 item "Course activation delay": from 03-earlier-article-teaching-spec.md (lines 55, 65, 67)
14. Two buckets (Bucket 1, Bucket 2): from 01-review-page-tool-instructions.md (lines 10, 18, 20, 21)
15. More than 5 items (when Already Handled exceeds 5 items, header shows only count and category summary): from 01-review-page-tool-instructions.md (line 56)
16. Leave the other 60 items unchanged: from 01-review-page-tool-instructions.md (line 25)
17. Hard cap of 7 items (max 7 items per page): from 01-review-page-tool-instructions.md (line 24)
18. Three verdicts (Taste Judge's three outcomes): from 02-taste-judge-readme.md (line 5)
19. 3 items with precedents, 4 new questions (matching results for this morning's 7 items): from 04-facts.md (line 17)
20. At least 20 precedents, 90% or higher agreement rate (auto-decision threshold): from 04-facts.md (line 11) and 02-taste-judge-readme.md (line 17)
21. 68 questions with matching precedents, 18 matched, 26.5% agreement rate: from 04-facts.md (line 10)
22. 11/28 (Sat) 10:00–12:00 Taiwan time (two hours), NT$1,600, three parts: from 04-facts.md (lines 28, 29)
23. Replace title in 3 places: from 01-review-page-tool-instructions.md (line 42)
24. Social promo drafts with 1:1 or 4:5 image cards, sent for review only once (1 time), 3 actions (three things): from 01-review-page-tool-instructions.md (lines 64, 72, 80)
25. Roughly 3,600 lines shrunk to roughly 150 lines, top 25 closest lines per question (plus 1 line before and after), ±3-line window: from 02-taste-judge-readme.md (lines 7, 42)

[Key Factual Narrative Source Notes]
1. This morning's 74 pending posts trimmed to 7 items, with the rest handled directly by AI under clear rules and counts reported afterward (top of page lists what it will do directly): from 04-facts.md (lines 15–16)
2. Recorded period 2026-10-27 to 2026-11-23 totaling 33 review pages and 256 decisions (roughly one month of stats, not daily): from 04-facts.md (lines 4–5)
3. One-on-one tutoring teaching spec incident (AI dumped long multiple-choice list in chat, author replied "Turn this into a review page. I'll decide inside the review page."): from 03-earlier-article-teaching-spec.md (lines 15, 81–83); general rule "generate interactive HTML, not a static table with no input interface for feedback": from 01-review-page-tool-instructions.md (line 8)
4. After receiving pasted decisions, run one more step (record.py) to log them into decision history, and overruled items become precedents for next time: from 01-review-page-tool-instructions.md (line 35)
-->
