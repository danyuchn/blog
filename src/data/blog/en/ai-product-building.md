---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T07:00:00Z
title: "Building AI Products from Scratch: A Non-Engineer's Four-Generation Evolution"
slug: en/ai-product-building
featured: false
draft: false
tags:
  - ai-product
  - developer-experience
  - opinions
description: A teacher-turned-builder shares the real story of four generations of AI tool development—RAG, platform architecture, cross-border deployment, and open-source strategy, with all the pitfalls along the way.
---

I'm not an engineer by training. But over the past two-plus years, I've built four generations of AI products from scratch, and the number of pitfalls I've stumbled into outnumbers the lines of code I've written. This isn't a tutorial. It's a field diary of everything that went wrong.

## The Four Generations

Looking back, my AI products roughly fall into four generations:

**First gen: sharing prompt instructions.** In late 2023, GPT opened up custom Agents. I immediately built a sentence-parsing tool for complex English sentences. Basically, I took the teaching SOP in my head, wrote it into a structured prompt, and let GPT follow it step by step. At the time I thought I was ahead of the curve. Looking back now, it was kindergarten-level stuff.

**Second gen: small-scale chatbots.** Purpose-built for specific skills—logical chain reasoning, practice question generation. I started learning how to use system prompts to control behavior, and also started running into the wall of GPT just not listening.

**Third gen: a knowledge-trained AI clone of myself.** I took all my course videos, articles, and lecture notes, ran them through RAG, and loaded them into a knowledge base. This was the turning point. I remember the day I finished—I tested it, and it could perfectly replicate my problem-solving approach. My mind went completely blank. I started questioning my own reason for existing.

**Fourth gen: realistic UI + AI tutor.** I embedded the AI clone directly into a mock-exam interface, creating a "your teacher becomes your personal tutor, walking you through each problem" experience. Students' reaction: "This looks better than the real exam."

## The RAG Revelation

The third generation was the most critical step. I fed all my lecture notes, public course videos, and paid course videos into RAG, and the AI could perfectly replicate my problem-solving approach.

This made me realize two things. First, an expert's tacit knowledge can be structurally extracted. Second, when RAG is done right, the AI clone's output isn't hallucination—it's actually grounded in your experience and knowledge, not made up.

Later I started building these for other teachers. The feedback was solid—everyone said it replicated about 80-90% of their teaching and problem-solving approach. All it takes is one sample, like a one-hour teaching video, and it can directly replicate the teaching methodology, handling most of the routine Q&A on the teacher's behalf.

## Architecture Choices and Pitfalls

I took plenty of wrong turns on platform architecture. Frontend on OpenWebUI, LiteLLM in the middle for API routing and usage monitoring. Backend database started on Firebase.

Why self-host instead of just using off-the-shelf ChatGPT? Because self-hosting lets you: give teachers a backend to track student-AI conversations and monitor learning progress; protect teachers' intellectual property so their core methods don't leak out; and control costs.

Speaking of costs—I once asked other teachers: if there were a tool that could perfectly replicate your thinking, answer students' questions 24/7, and it cost $15-20 a day to run, would you pay for it? Most teachers nearly fainted when they saw the bill. But I think the trade-off—freeing teachers from repetitive Q&A—is worth it.

## The Cross-Border Deployment Disaster

The most painful episode was trying to bring the product to Chinese customers. After talking with a partner, I discovered: all three major AI model families can't be used inside mainland China—you have to swap to domestic models like Qwen; Firebase is a Google product, so it's a no-go—you have to migrate to Alibaba Cloud; and China has data sovereignty regulations that prevent user data from leaving the country, so you need traffic splitting and two separate databases.

I initially figured this kind of major engineering overhaul would take a month or two. Claude Code knocked it out in a day. The rest was just me, the human amateur, learning, reviewing, and manually testing.

## n8n Automation and Quality Verification

One workflow I'm particularly proud of: using n8n to take user-submitted exam recall reports and automatically generate practice questions based on the test-design principles I'd mapped out. The key is dual independent verification—is the answer correct? Does it meet the design criteria? Only after passing both checks does it get automatically added to the bank.

I ended up applying this "AI generation + dual verification" pattern everywhere. No matter what content you're generating, you need an independent validator sitting in the middle. I've personally witnessed the disaster of automated posting gone wrong, so this step is non-negotiable.

## The Three-Day Recitation Error Nightmare

One of the most painful bugs in AI product development: the recitation error. In plain terms, the API refuses to output original source text. But my entire use case requires users to see the original question text while solving problems. This roadblock ate three days of my life.

This kind of thing isn't a code bug—it's an API-level restriction. You can only work around it or switch approaches. If you've never hit this kind of wall, you probably can't understand why "building AI products" and "using AI" are on completely different levels.

## Open Source and the Product Mindset

I open-sourced a Teaching Copilot. Rate limiting set up (I'd been burned by API abuse before), deployed on Google Cloud Run.

The old me always thought: my stuff is clearly this good, so why don't people care when I pitch it? Why the lukewarm reactions? I'd quietly blame everyone else.

Eventually I figured it out: the product just wasn't good enough yet that people had to come find me. No need to sit there silently guilt-tripping anyone. Just go back to polishing the product. Polish it until people are amazed. Polish it until it speaks for itself—"the peach and plum trees don't talk, but a path forms beneath them." That's enough.

## Sentiment Analysis Tool: An Accidental Side Product

Along the way, I accidentally built a social media sentiment analysis tool. It turned something that used to require a whole team plus expensive software subscriptions into an automated engineering pipeline. It saves the labor cost of manually collecting data, the annotation cost of manually tagging positive/negative sentiment, the time spent writing reports, and the licensing fees for commercial sentiment tools that easily run tens to hundreds of thousands of dollars.

The most straightforward takeaway: it doesn't make you "way better at analysis." It lets you "do roughly the same thing at 1/10 the original cost."

## Next Up: Vectorization and Fine-Tuning

I'm currently exploring two directions. One is vectorizing the content in my database—tagging topics and logical semantics—so that natural-language queries can precisely extract relevant content. The other is fine-tuning open-source models so I'm no longer entirely dependent on big-model APIs.

How exactly I went from being a teacher to ending up here, I honestly can't explain. All I know is my vocabulary gets nerdier by the day—de-contextualization, grid search, fine-tune are now part of my daily speech.

But when I think about it, isn't this just what building products is like? You try whatever comes to mind, write down the pitfalls when you hit them, and try to hit fewer next time.
