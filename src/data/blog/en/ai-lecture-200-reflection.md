---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T07:30:00Z
title: "From Chatbots to Autonomous Agents: What a 200-Person Workshop Revealed About Modern Workflows"
slug: en/ai-lecture-200-reflection
featured: false
draft: false
tags:
  - teaching
  - ai-education
  - personal
description: 'Most workplace AI anxiety isn''t about knowing how to write prompts—it''s about knowing how to direct. Core takeaways from a 200-person workshop: the shift to autonomous agents, a 3-step automation demo, and the decision-making mindset non-engineers need.'
---

Last Sunday morning, I hosted a free online workshop on AI.

Over 450 people registered, and roughly 200 showed up live—about a 45% attendance rate. Even though the session overlapped directly with Mother's Day lunch, the Zoom analytics showed an average retention rate above 75%. The Q&A was so lively that we ended up extending it by thirty minutes.

It took me back to the physical classroom near Da'an Station ten years ago. We used to pack 100 students into a room, and I would lecture on the GMAT for four hours straight. Students sat from 10:00 AM to 2:30 PM with a single break; I would grab a quick sip of water and keep going.

That same intense focus showed up online this weekend. Only this time, the topic wasn't business school admissions exams—it was how non-technical knowledge workers can actually change how they work with AI.

## The Real Anxiety Behind the Audience Questions

Usually after a demo and a few case studies, Q&A sessions are quiet. People drop a thumbs-up and leave. But during this thirty-minute Q&A, attendees from across industries lined up with specific questions.

The attendee list included sales reps, product managers, marketers, researchers, data analysts, designers, accountants, software engineers, and even test-prep center owners.

Their questions came from very different angles:
A sales rep asked: "Will clients bypass me and just generate quotes with AI?"
A PM asked: "Will the PRDs I write get replaced?"
An accountant asked: "Is our accounting firm going out of business?"
A designer asked: "Is my portfolio still worth anything?"

Each person asked about their own domain, but underneath ran the same anxiety: Has AI already changed the workplace? And am I ready?

This anxiety doesn't come from a lack of exposure. Looking at our registration data, more than half of the attendees rated their familiarity with AI at level 4 or 5, and the vast majority were non-engineers. Nobody was stressed about how to chat with a bot. The real concern was: once machines start working autonomously, where do we fit?

## Moving from Conversational AI to Autonomous Execution

The core premise of the workshop was this shift: AI has moved past basic conversational generation and into autonomous agentic execution.

Over the past year, most industry investment has poured into agentic AI rather than chat generation. That shift mirrors my own day-to-day work: moving from treating AI as an assistant to treating it as an autonomous collaborator.

In the US, this is already reality. Major corporations are mandating AI adoption across the board, setting up training programs, workshops, and productivity KPIs. When companies measure AI impact, they track token usage, logged hours saved, and real-world headcount replacement. Anthropic's tools are already handling work once assigned to junior associates at law firms or handled by specialized enterprise software, sending ripples through software stocks on Wall Street.

The more critical shift is how widely this has reached non-engineers. AI is no longer reserved for engineering teams; it has become leverage for professionals in every field to rebuild how they work.

## A 3-Step Automation Chain from a Single Command

To show the difference between conversational chat and autonomous execution, I ran a fully automated workflow during the presentation.

It was a 60- to 90-second pre-recorded demo (to avoid relying on live API calls during a talk), feeding the 294 real signup entries from that very workshop directly into the pipeline.

I gave the terminal tool Claude Code just one instruction: "Check who attended today, create a realistic profile for each persona, and tailor a resume for the company they're most likely targeting." Without any manual intervention along the way, the system completed a three-step chain on its own:

Step 1: Read the signup data in the spreadsheet and tally the professional backgrounds of the attendees.
Step 2: Generate three representative fictional personas based on the breakdown—a sales rep, a data analyst, and an operations project manager.
Step 3: Run the resume tailoring workflow for each persona against matching job openings, outputting three polished, fully formatted PDF resumes—Salesforce for the sales rep, McKinsey for the data analyst, and Google for the operations PM.

This is what ChatGPT physically cannot do in a regular chat window: read data across external tools, execute multi-step evaluations, generate finished files, and do it all without human intervention.

## Tools Change, but the Logic of Direction Stays the Same

After recording over thirty Claude Code tutorials over the past six months, one realization kept surfacing: tools will change, but the underlying thinking doesn't.

Giving clear instructions takes real discipline. It's not about which button to click or which prompt to copy; it's about the logic of directing the work—breaking tasks down, planning verification, assigning responsibilities, and managing risk.

This framework is identical to what I taught a decade ago in that Da'an classroom for the GMAT. The GMAT trains you to make optimal decisions under tight time limits and scarce resources. Directing Claude Code requires the exact same mental muscle. The only difference is that my students traded their pencils for Sonnet 4.6.

## Boundaries and Advice for Real-World Rollout

Take how I handle attendee lists after a workshop: when dealing with brand-new contacts, the leads are cold. Build trust first—through community interaction or sharing the workshop recording—instead of jumping straight into business pitches.

## Appendix: Technical Details and Architecture

- Claude Code: A CLI-based AI tool with read/write access to the local environment, shell command execution, and tool-use capabilities. It runs multi-step tasks autonomously and outputs final deliverables directly.
- Agentic Architecture: The evolution from conversational chatbots to autonomous agents capable of querying external tools, chaining multi-step decisions, and writing files to disk.
- 3-Step Automation Pipeline: Reads the Google Sheets spreadsheet (294 registration records), analyzes attendee background distribution, generates three representative mock personas, and runs job-tailor for each to produce three customized PDF resumes.
- Sonnet 4.6: The large language model referenced in contrast to the pencils used a decade ago.

Looking back at that packed classroom near Da'an Station, the medium shifted from a blackboard to a terminal window, but teaching itself hasn't changed. As tools change around us, what keeps you grounded isn't chasing every new feature release. It's your ability to break down problems, define boundaries, and make decisions. With a clear framework for directing the work, no matter how fast tools iterate, you keep control of the rhythm.

<!-- 2026-11-12 舊文盤點整篇重寫：將原本僅記錄人數與心情的課後感言，重構成以「對話 AI 到自主 Agent」為核心的實戰文章，納入講座的三步自動化 Demo、美國職場觀察、底層指揮思維，並將技術機制收納於附錄。 -->
