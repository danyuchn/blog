---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "See the Outside, Think the Inside: Two Claude Skills That Pair"
slug: en/competitive-analysis-skills
featured: false
draft: false
tags:
  - claude-code
  - skills
  - ai-workflow
  - competitive-analysis
description: I saw a competitor selling well and my first reaction was anxiety. But before letting anxiety win, I wanted to actually understand what it was. Lately I have been pairing two Claude Skills for this — H/V analysis to see the outside, first-principles to see the inside.
---

I have been doing two things with Claude Code lately.

## Step 1: Research the thing that bothers me

I saw a competitor selling well. First reaction: anxiety. But before giving anxiety the wheel, I wanted to figure out what the thing actually is.

I used a Skill called "H/V analysis":

- **Vertical** — how did it walk step by step to its current shape?
- **Horizontal** — compared to its peers, where are the differences?

Once these two dimensions are filled in, anxiety gets replaced with information. I now know whether the competitor is "actually strong" or "good at marketing", and which gaps I should care about versus which ones I can ignore.

## Step 2: Get clear about myself

After seeing the outside clearly, the next step is looking back at myself.

This is where I use the first-principles Skill:

- The thing I am doing — what is the bottommost "why"?
- Which constraints are real, and which are just "everyone else does it this way"?

A lot of the time, the source of anxiety is not that the competitor is good. It is that I have not thought my own thing through clearly.

## How the two Skills relate

- One helps you see the outside
- The other helps you think the inside

Used separately, both work. Used together, they complete each other.

Both are public on GitHub, and any Claude user can install them:

- H/V analysis: <https://github.com/KKKKhazix/khazix-skills>
- First principles: <https://github.com/danyuchn/first-principles-skill>

## A workflow detail

I do not use these Skills inside a "real work" session. I use them in a research-only session before plan mode, then collect the conclusions into notes. When it is time to actually do the work, I open a new session and bring the polished conclusions in.

Separating "research" from "execution" prevents the long-context attention dilution problem.
