---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-02T04:00:00Z
title: "Teaching non-technical people AI: five things the tech world assumes everyone knows"
slug: en/teaching-non-tech-ai
featured: false
draft: false
tags:
  - ai-education
  - claude-code
  - teaching
description: One student was a seasoned HR consultant who managed all her files across several USB drives and had never heard of an API. Here are five knowledge gaps that show up constantly when teaching AI tools outside the tech world — and what actually works.
---

One of my students was a highly experienced enterprise HR consultant. Twenty-plus years of expertise. Day-to-day computer use: email, Word, Excel. File management: several USB drives. 

Before I started teaching her Claude Code, I assumed the learning curve would be the interface.

I was wrong.

The real barrier was earlier than that. Before she could learn how to use Claude Code, I had to deal with a set of things she didn't know she didn't know.

These five knowledge gaps show up constantly when teaching AI tools outside the tech world.

---

## 1. Habit of doing it yourself, not directing someone else to do it

Most common scenario: the moment a student hits any obstacle, their first move is to handle it themselves. Mouse drifts toward the window. They start clicking.

They don't realize this is something they could ask AI to do.

Their mental model: AI is something that answers questions. Not something that does things on their behalf.

**What works:** Interrupt at the moment they reach for the mouse. Say "wait — try asking AI to do that." Let them watch the result. Then open the tool call trace so they can see what happened. Not magic — a sequence of logical steps. This transparency matters. It shifts their relationship to AI from "something impressive I don't understand" to "something logical I can trust."

---

## 2. No confidence in their own instructions, no idea how to start

Many students stare at a blank input box.

It's not that they don't know what they want. It's that they're not sure if they're "saying it right," if AI will understand, if their question is too simple or too vague.

This hesitation stops a lot of people at step one.

**What works:** Ask them to describe their request to me out loud. Then type it into AI, word for word, the way they said it. Let them see that the way they talk to a colleague or a report is exactly how you talk to AI. Sometimes I just open voice input and let them speak directly — conversational language is more natural for them than typing, and it works.

---

## 3. Having only a vague idea, and concluding AI can't help

"I don't really know what I want to do, so AI probably can't help me yet."

This comes up constantly. They think AI needs a fully formed instruction, and since their own thinking isn't that clear yet, AI is temporarily useless.

That's backwards. This is exactly when AI is most useful.

**What works:** Have AI go online, ask a few clarifying questions, and produce a draft plan in planning mode. Seeing a concrete starting point gives them something to react to. The pattern — "let AI make your vague idea tangible" — is usually the first moment this kind of student actually sees the value.

---

## 4. Not knowing how to bring pre-AI skills into AI collaboration

This is the one worth the most detail.

Many experienced professionals outside the tech world have excellent judgment, management instincts, and communication skills. But they assume these are irrelevant to AI collaboration — that they need to learn a completely new set of skills from scratch.

They don't. The mental model maps almost directly.

**I translate AI collaboration into language they already speak:**

- "If you didn't have AI, how would you approach this? What's the first step?" — breaking down a task
- "How long would you give this to run? If it came back wrong after five hours, how would you feel?" — run a small test first
- "How do you get someone to understand your standards?" — give examples
- "Would you show this to a client before it's ready?" — test in a safe environment first

When they hear these, the usual response is: "This is just... management." Exactly. The underlying logic of AI collaboration is close to managing a capable new hire who needs clear direction. They already know how to do that.

---

## 5. Not knowing that computers and human tools work completely differently

This is the most foundational gap — and the least talked about.

Human interfaces (GUIs) are designed for humans: clicking, dragging, reading icons. But computers communicate with external services through APIs — structured formats, not visual interfaces.

A lot of what Claude Code can do comes from its ability to talk directly to external services through APIs. If a student doesn't have this baseline, they'll assume Claude Code can only do the small set of things they've seen it do in a demo. They have no sense of where its actual edges are.

An AI without tools is like a laptop in airplane mode. Functions limited, constantly running into walls.

**What works:** Don't explain what an API is. Instead, show them before and after: Claude with no tools connected vs. Claude with tools connected. Let them feel the difference through contrast rather than through theory.

---

These five things almost never get mentioned inside the tech world because everyone assumes everyone else already knows them. Outside the tech world, they represent the actual starting point for the majority of white-collar workers.

Teaching non-technical people AI doesn't start with the tools. It starts with helping them rethink their relationship to tools.
