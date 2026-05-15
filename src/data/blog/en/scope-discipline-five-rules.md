---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T09:30:00Z
title: "Scope Discipline: five rules—client small talk ≠ scope expansion authorization, must go into every future contract"
slug: en/scope-discipline-five-rules
featured: false
draft: false
tags:
  - ai-consulting
  - contract
  - lessons-learned
description: 'A 5/12 admin class contracted for 1.5 hours ran 2.5 hours (+67%). Root cause: I misread the client''s stated topic preference as authorization to expand scope. The lesson became five Scope Discipline rules that must appear in every future enterprise / 1-on-1 / tutoring contract.'
---

5/12 ran an admin class. Contract said 1.5 hours. Final time: 2.5 hours. Overran by 67%.

Post-mortem: the overrun's main cause wasn't "3 more attendees" (+3 people contributed only +20-25 min). It was that I **commit `97dbc6c` (5/7) restructured "department-wide unified use case" into "13 people, 13 different tasks"** on my own.

What did "13 people, 13 tasks" add over "13 people, 1 task"?
- 13 context switches
- Each switch adds 2-3 min
- Cumulative +35-40 min (the dominant overrun driver)

Why did I restructure? Because the client Christie said in Teams on 5/6:

> Focus on tracking and follow up.

I read that as "**so I should design different tracking tasks for each student**."

But "focus on tracking" was just a **topic preference**, not a directive to do "different task per person."

## The lesson: client small talk ≠ scope expansion authorization

Christie didn't ask for 13 tasks. I added that to myself. Self-inflicted scope creep directly drove a 67% overrun.

**Future self-check before editing a lesson plan**:

> Is this an **explicit client request**, or did I add it on my own?

Not explicitly requested = don't move.

## Scope Discipline: five rules

All future enterprise / 1-on-1 / tutoring contracts will include these five clauses:

### 1. Lock task granularity

The contract must explicitly state "class-wide unified use case" or "per-person customized use case." If the latter, **prep time is billed separately** (same 3-5x SOP as the previous post on enterprise AI training).

Vague phrasing (e.g. "adjust based on student needs") forbidden. Vague = the on-ramp for self-inflicted creep.

### 2. Headcount ceiling

The 4/2 Christie contract wrote "headcount allocated by Christie (not fixed)" with no ceiling. Admin class signed at 13 → actually 16. The extra 3 couldn't be turned away on the spot, adding +25 min to the overrun.

**Future contracts must lock a headcount ceiling** (suggested ≤ 12). Over the ceiling: surcharge or reschedule.
- 12-15 people: +30% quote
- 16+ people: refuse, or split into two sessions

### 3. Hard time ceiling + buffer

Contract says 1.5 hours = teaching content must fit in 1.0-1.2 hours, leaving 0.3-0.5 hour buffer for Q&A, tech issues, attendance variance.

**Don't pack 1.5 hours of content into the 1.5-hour buffer**. In the lesson-planning phase, cut—"of these 13 items, I can only do 8 in class; the rest goes to extension reading."

### 4. Lesson plan version lock

Lesson plan v1 approved → contract locks "v1 is the basis. Subsequent changes ≤ 10% scope." If the client wants new topics added later, **go through a change order** (verbal discussion → I assess time impact → written confirmation → quote adjustment → only then start work).

This time the problem was: Christie didn't explicitly request additions, but I read the Teams thread and decided "we should add." The new rule: **"a sentence the client typed in Teams" ≠ "a client-signed contract amendment."**

### 5. Self-audit

Before every lesson-plan edit, stop and ask:

- Is this change required by a clause in the contract? (Yes → proceed)
- Or is it a topic preference the client mentioned in Teams / LINE / a conversation? (Yes → don't move, ask for clarification)
- Or am I just thinking "this would be better for the students"? (Yes → **absolutely don't move**—this is the entry point for self-inflicted scope creep)

The third one is the most dangerous, because it wears the costume of "good for the client" while burning my hours on something the client never asked for.

## Contract template (sample clauses)

Encoding the five rules into a contract:

```
## 5. Scope and Duration

5.1 Task granularity for this training is "class-wide
    unified use case." All students perform the same
    exercise.

5.2 Student headcount ceiling: 12. Over-cap adjustments:
    - 12-15 people: quote +30%
    - 16+ people: split into two sessions, or decline

5.3 Training duration of 1.5 hours is the hard ceiling.
    The contractor shall plan a buffer of at least 0.3
    hours within the lesson plan.

5.4 The lesson plan is anchored on the mutually approved
    v1. Subsequent modifications exceeding 10% scope
    require a written change order with corresponding
    rate adjustment.

5.5 Topic preferences expressed by the client in
    instant messaging (Teams / LINE / email threads)
    are treated as discussion only and do not constitute
    authorization to change scope. Scope changes require
    a signed contract or written change order.
```

## Why these five belong in the contract

Because **these five rules protect the client too, not just me**.

The client doesn't actually want me to add work unilaterally. She wants "what's in the contract gets done per the contract." My unilateral addition produced a 67% overrun, but the client didn't receive proportional value—the 13 tasks didn't let students learn deeper; instead, time pressure prevented any one of them from completing fully.

**Scope discipline isn't conservatism. It's professionalism.**

If you also do AI training engagements and have ever felt "we overran without noticing," go back and look at which step came from "the client didn't ask for it, but I added it." Nine times out of ten, the overrun root cause sits there.
