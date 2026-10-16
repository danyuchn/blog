---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-16T00:03:00Z
title: "A Rule Being Written Doesn't Mean It Got Read"
slug: en/rule-written-is-not-rule-read
featured: false
draft: false
tags:
  - harness
  - skills
  - lessons-learned
description: 'Writing a rule or skill into a file does not mean the model opened it this turn. Two lesson-prep misses this week, plus magpie''s lessons-file approach, show why the call site has to say "open and read this first."'
---

Several entries in this week's log say the same thing: a rule or skill got written, but nobody read it that turn. When one document depends on another, the call site has to say "open it and read it first." Otherwise the model reads a summary and derives the rest on its own.

## Codex lesson prep: the FAQ it pointed to never got opened

On 10/11, Codex helped me prep a lesson. It read only the morning-brief summary and never opened the FAQ that the main file pointed to, so all three plans were things it worked out itself. I posted Claude's review of that prep on Threads, and what follows tracks its main points.

First, it read the summary, not the original records. The first prep followed the old storyline in the morning brief and missed the new requests from 10/5 and 10/6. It only went back to read them after I pointed that out.

Even after that, it didn't read the real answer. On line 85 of the main file it had written "see the existing FAQ for the handover method," and it never opened that FAQ. The FAQ was the approach I had already settled on 10/6: use the official skill-recording feature to record a colleague's actual workflow. Instead it gave me three versions of the lesson flow, and all three were its own inference.

When I questioned it, it got defensive instead of returning to the goal. I asked, "is this from a reference lesson plan, or did you come up with it?" It retreated into quoting spec clauses, and even the main thread shrank to "confirm the sticking points on site." That moved it further from what I meant, and in the end I had to state my intent myself.

It also treated the teaching method as a spec sheet to apply, and didn't use this learner's actual record. The lessons from his three sessions were all in the files: two sessions ran over, installing a new tool ran over, I had used my own case as the demo, one system had gone unhandled for three sessions in a row, and 8GB of memory crashed. It used none of them.

Finally, it said "done" far more than it checked. The claim-evidence hook at wrap-up blocked it twice, and the message itself was diluted by tables and formatting.

Claude's one-line summary: it was answering "how does the spec read," when what I wanted was "given this person's actual situation, how do we get him to finish something today."

## session-prep, same day

There was another one that day. session-prep only said "follow reviewable / deliverable," and the first pass never actually loaded them. It missed three things: a newly invented commitment, a missing scope section, and a guess at a colleague's gender. It reran only after I asked.

## Three more from the same week

On 10/09, while reviewing a plan, it couldn't find a certain to-do and concluded straight away, misjudging one plan's checkpoint as having "no to-do," when it had actually been finished on 10/7 and archived. It should have checked todo_archive and plan_progress before concluding anything.

Same day: names hardcoded in a routine document go stale. The five prospective learners written in on 9/10 had all either converted or closed by 10/9, so scanning from that list would have missed the 13 people actually in the folder. I've changed it to scan the folder as it is now.

On 10/16, the automated observations section of my weekly report listed an already-decided item as pending. The status line didn't follow the log update, so anything downstream copies the old state.

## magpie's lessons file

On 10/13 I saved a bookmark analyzing the open-source project magpie. In 19 days it shipped 1,204 versions, with almost all the code written, reviewed, merged and released by agents.

Its CLAUDE.md is two lines: @AGENTS.md and @LESSONS.md. AGENTS.md is a routing table. It holds no rules, only which document to read before which kind of work: read docs/subsystems/ before changing a subsystem, docs/code-standards.md before writing or reviewing code, docs/contributors.md before reviewing a community PR.

LESSONS.md is a lessons file the agent writes every night. The nightly review looks at only three situations in that day's commits: fixed and then reworked, should never have merged, and verification that was too thin. Every entry has a fixed format: one rule, a paragraph of reasons, a commit or issue number as evidence, and a last line reading Seen N× (date). When the same entry shows up in the retrospectives of 3 different days, it moves from LESSONS.md into code-standards.md and becomes a hard rule checked item by item in every PR review.

My note on the bookmark: this is another solution to the same problem as the checkpoint lessons I just did today. I wrote earlier about pulling rules out of conversation history: [I scanned 500 Claude Code sessions and the AI stopped making the same mistakes](/blog/posts/en/self-improving-claude-md/).

<!--
新增非原文句子清單（忠實度自首）：
1. 「Several entries in this week's log say the same thing: a rule or skill got written, but nobody read it that turn.」 — 類型：框架句（依核心論點撰寫）
2. 「When one document depends on another, the call site has to say "open it and read it first." Otherwise the model reads a summary and derives the rest on its own.」 — 類型：框架句（改寫自指示中的核心論點）
3. 「I posted Claude's review of that prep on Threads, and what follows tracks its main points.」 — 類型：銜接
4. 檢討五點（First / Even after that / When I questioned it / It also treated / Finally） — 類型：改寫（素材 2 的第二人稱改為第一人稱；連接詞 Finally、also 為銜接）
5. 「Claude's one-line summary:」 — 類型：銜接
6. 「There was another one that day.」 — 類型：銜接
7. 「Three more from the same week」、「Same day:」、「I've changed it to scan the folder as it is now.」 — 類型：銜接／改寫（第一人稱改寫）
8. 「On 10/13 I saved a bookmark analyzing the open-source project magpie.」 — 類型：銜接
9. 「In 19 days it shipped 1,204 versions, with almost all the code written, reviewed, merged and released by agents.」 — 類型：改寫（書籤摘要首點）
10. 「My note on the bookmark:」 — 類型：銜接
11. 「I wrote earlier about pulling rules out of conversation history:」 — 類型：銜接（站內連結導言）
12. 小節標題 — 類型：框架句
-->
