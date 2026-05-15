---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T07:00:00Z
title: "Why Obsidian is something special to me, and why I only made this video now"
slug: en/obsidian-knowledge-base-personal
featured: false
draft: false
tags:
  - obsidian
  - knowledge-management
  - ai-workflow
description: I'd been wanting to make this video for a long time, but kept putting it off. Obsidian's flexibility is so high that it grows into a different shape in every person's hands. The payoff isn't immediate either—it's only after the vault has grown for a while that you realize you can't go back.
---

I'd been wanting to make this video for a long time, but kept putting it off until today.

Because Obsidian is something special to me. Its flexibility is so high that it grows into a different shape in every person's hands. And the payoff isn't immediate either—it's only after the vault has grown for a while that you realize you can't go back.

So I thought about how to shoot it for a long time. In the end I went with the most natural approach—

Just honestly share with you why I came to Obsidian, what my knowledge base looks like, how it grew slowly over time, and what your first step could be: building a simple, initial knowledge base for yourself with very basic commands.

## Why I came to Obsidian

I didn't pick Obsidian for a beautiful UI. Nor because some productivity YouTuber recommended it. I came to it after using Claude Code, when I realized one thing:

**The model's long-term memory can't live inside the model. It has to live with me.**

Everything I tell Claude Code every day—decisions made, mistakes hit, lessons learned—if it only lives in the current conversation's context, the next month when I open a new conversation the model has no idea what came before. I'd have to start over every single time.

Obsidian's answer: I write everything in markdown, stored locally, cross-linked with wikilinks. Claude Code reads a designated entry file (e.g. `MEMORY.md`) on every session start. That gives the model a "cross-session persistent memory"—but the ownership stays in my hands, not Anthropic's.

## What my knowledge base looks like

The main folders:

- `daily/YYYY-MM-DD.md`: daily notes. Things done, decisions, mistakes, lessons
- `weekly/YYYY-MM-DD.md`: weekly reviews
- `projects/`: one file per active project, tracking current state, todos, decision history
- `pillars/`: the main pillars of life (business, health, relationships, finance), one file each
- `bookmarks/`: things I read, tools worth remembering, book notes
- `decisions/`: contextual records of important decisions (not just the outcome, but "why this choice")
- `personal/`: private, related to therapy, my partner, family
- `archive/`: completed old tasks

Two arteries:

- **Time axis** (daily / weekly): what happened when
- **Topic axis** (projects / pillars / decisions): the latest state of each topic

Cross-reference: each daily note wikilinks the topics it touched that day; each topic file's "Related" section links back to relevant daily notes. From whichever side you enter, you can recover the full context.

## How it grew

I've used Obsidian for about a year and a half. At the start it was just `daily/` and `projects/`. There was no deliberate design—I just wrote daily, and opened new folders when new types emerged.

Turning points:

- **At 3 months**: noticed a lot of repetition across daily notes, so I opened `pillars/` to extract long-running themes
- **At 6 months**: started having Claude Code auto-read `MEMORY.md`. The vault entered an "AI-readable" stage
- **At 9 months**: cross-file wikilinks exploded (some files had outbound >50). Opened `weekly/` as an aggregation layer
- **At 12 months**: started doing "main file consistency scans" weekly (cross-checking the status line at the top of a project file against section headers below), catching two or three contradictions that had been silently festering for three weeks

The growth curve was **rolled out, not designed**. If you start by trying to design a perfect structure, you'll get stuck on "how should I categorize this" for three months without writing anything.

## Your first step

Don't start with a complex structure. In the first week, do just two things:

1. Make a `daily/` folder. Write a `YYYY-MM-DD.md` every day
2. When writing, wrap any proper noun (person, project, tool name) in `[[name]]`

You don't need to actively create the file behind that wikilink. Obsidian marks `[[ABC]]` as a "non-existent link." When you decide some day that ABC deserves its own topic file, you click the link and create it then.

The core of this workflow is: **write first, organize later. Don't design before writing.** After two months of writing, you'll see for yourself where structure is needed, which topics to extract, which duplications to merge.

## On the recent wave of "markdown is dead, HTML is the future"

There's been some discussion lately along the lines of "drop markdown, HTML is the future." Does shipping an Obsidian video at this exact moment count as going against the wind?

I don't think this is a wind direction question. Markdown and HTML each have their right place. Markdown is for "future me + AI to read together." HTML is for "other people to read." The first is the knowledge-base scenario; the second is the publishing scenario.

Putting them head to head is like asking "should I buy sneakers or dress shoes?"—it depends on whether your next step is to play basketball or go to a meeting.

I'll keep using Obsidian. And I'd love to see you start from your first daily note too.

> Video: <https://youtu.be/EhMKfG1dvnI>
