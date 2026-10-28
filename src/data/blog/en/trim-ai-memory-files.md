---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-28T04:00:00Z
title: My AI's Memory Files Kept Growing, So I Deleted 101 and Added a Gate
slug: en/trim-ai-memory-files
featured: false
draft: false
tags:
  - case-study
  - harness
  - claude-code
description: 'After a few months with Claude Code, the memory files it wrote for itself had piled up past four hundred, mostly running logs and client status. Here is how I sorted them, cut them to just over three hundred, and put a write gate in front to stop the regrowth.'
---

Claude Code writes the things it thinks are worth remembering into small files under each project, and loads them automatically next time. After a few months of use, these memory files had grown past four hundred. One day I opened the index and found that quite a lot of what it had saved didn't belong there.

If you use ChatGPT's memory, Claude's project knowledge, or keep your own notes for an AI to read, the same approach works.

## The memory files had become a junk drawer

Once I looked through them, the contents fell into a few kinds:

- Where a particular client or student currently stands and what happens next. That's status, and it goes stale in two weeks.
- The full steps of something I did once, only relevant to one type of task.
- Running logs of amounts and dates.
- Old conclusions that no longer hold.

Kept in a place that loads in every conversation, these cause two problems. They take up room at the start of each session, so the model reads a pile of things unrelated to the job at hand. And they go out of date, yet still get read in as fact. It's the same principle as [the more rules I add, the less the model listens](/blog/posts/en/harness-slim-down-36), only this time the target is memory.

## Decide where each one belongs, then delete

I didn't judge each file as keep or delete. I asked where it should live.

- Methods and pitfalls that matter only for one type of task moved into the matching skill, which loads only when needed. About 56 files.
- Client, student and project status went into my knowledge-base main files. I checked that no fact was lost, then deleted the memory file. 38 files.
- Anything out of date was simply deleted. 9 files.

In the end memory keeps only three kinds of things: who I am, my preferences and judgment rules; approaches I corrected and confirmed; and where an outside resource lives and how to look it up.

## The numbers

After the cleanup I counted the files:

- Across all projects, memory files went from 403 to 302, 101 fewer.
- In the project I use most, from 118 to 65.
- That project's index file went from 6,532 bytes to 4,900, a quarter smaller.
- The commit removed 4,382 lines and added 383. Most of the additions are the gate in the next section.

## Why a gate

Cleaning once doesn't last. Left alone, the model writes client status, money logs and whole procedures back into memory, and the index grows back within a day.

So I added a write gate. Every time the model writes or edits a memory file, the change goes through a few checks. If it fails, it's blocked, and the model is told where that content should go instead.

- Every new file needs a name, a one-line description and a type.
- No new "project" memories. Status belongs in the knowledge base.
- A "correction" memory must say why, and how to apply it later.
- Three or more distinct dates, three or more money amounts, or a to-do list in the text counts as a log and gets blocked.
- A new file over 2.5KB is blocked. Either split it, or it's really a procedure and belongs in a skill.

If there's a real need, one line in the content lets it through, and the reason is logged.

Before switching the gate on, I rewrote every existing memory file as-is to test it. Not one was blocked by mistake.

## How to use this on your own AI notes

You don't need to write code, and you don't need to sort anything by hand. Let an AI scan it. These are the rules it works from:

1. For each item, ask: is this who I am, my preferences, something I've corrected, or where an outside resource is? If not, it needs to move.
2. Put client and project status back where you already track clients, such as a spreadsheet or CRM. Let the AI read it when it needs to, instead of baking it into its memory.
3. Write a multi-step method as its own standalone instruction sheet, and feed it to the AI only for that kind of task.
4. For each preference you keep, add one sentence on why. A rule without a reason gets applied rigidly even when an exception comes up.
5. Ask the AI to scan again once a month for new logs growing back.

Paste the block below into an AI that can read your files, such as Claude Code, and fill in the brackets. It reads everything, sorts it, and lists what to move or delete. You only look at the table and decide which items to go ahead with:

```text
Check all the memory files you have saved about me (location: (path to the memory folder or the exported file)).
Read every one yourself first, including the index file. Don't ask me what's in them.
Put each file into one category:
A. Who I am, my preferences or judgment rules
B. Approaches I corrected or confirmed (must have a reason)
C. Where an outside resource is and how to look it up
D. None of the above. Then decide which it is: client or project status, steps for a type of task, or expired
Then give me a table: file name, category, suggested action, one-line reason.
The suggested action can only be one of four: keep, move to (where I track clients), rewrite as a standalone instruction sheet, delete.
Before moving or deleting anything, make sure no fact in it would be lost.
This step is a list only. Don't touch any file. After I review the table and tell you which items to carry out, do those, then report what you actually changed.
```

That's it.
