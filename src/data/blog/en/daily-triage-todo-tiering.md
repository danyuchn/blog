---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "Claude Code To-Do Tiering: Auto / Review / Collaborate / Manual"
slug: en/daily-triage-todo-tiering
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - productivity
description: 'A small discovery from using Claude Code: sort to-dos by repo, then into four tiers — auto, review, collaborate, manual. Stuff that used to drag on all day now finishes in an hour.'
---

A small discovery from how I use Claude Code: to-do tiering.

I use it for non-coding work. My old habit was to list out all my to-dos and then do them one by one, in order. I'd open sessions for different repos, but really I was still pushing forward one point at a time inside each repo, and whenever something needed me to discuss or review it, I'd be stuck for ages. So my workdays were still on the long side, and my body started paying for it.

Yesterday I happened to hit my 5-hour quota cap, and with nothing to do while I waited, I started sorting my to-dos. I was thinking about which ones belonged to which repo, and which ones it could do on its own / needed me to review / needed me to actively help with / needed me to do by hand somewhere outside. I figured I'd hand them off the moment the quota reset. The fully automatic ones all go in one session, the review ones and the discuss-with-me ones each get their own session, and the manual ones I just go do myself.

Turns out the to-dos that used to drag on for a whole day were done in under an hour?

So I made a separate skill. It sorts my to-dos by repo, and after the repos, into four tiers: auto / review / collaborate / manual. It only lists the ones that are due today, overdue, or within the next seven days and not blocked, not waiting on someone else, not waiting on timing.

I hit one trap while designing it. The first version had the script guess the tier from keywords, but "follow up" carries an active meaning yet collides with the word "wait," and "track" looks automatic but actually needs data to pile up first. Single-word matching is bound to misjudge. So the script fell back to just facts (collect the to-dos, grab the context), and the judgment is left to the LLM reading the text plus context, item by item.

From now on I run this skill every morning, fire up a bunch of sessions, and wrap up once everything's verified. Less time on the computer, sleep earlier, take better care of yourself.
