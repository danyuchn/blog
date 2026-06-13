---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-10T04:00:00Z
title: "Testing Fable's Limits on a Professor Friend's Paper Repo"
slug: en/professor-fable-paper-writing
featured: false
draft: false
tags:
  - ai-tools
  - ai-trends
  - opinion
description: 'I woke up to Fei-bo (the guardrailed Mythos build) going live, so I borrowed a professor friend''s paper proposal, prompt, and workflow docs to probe its paper-writing limits.'
---

I woke up and Fei-bo (the guardrailed build of Mythos) was already live. I quickly pinged my professor friend and asked him to hand over the prompt and repo for the paper he's writing, so I could test where its limits are. Only a few days of subscription quota to play with — after that the API call pricing gets high enough to rival a Taiwan domestic-travel bill.

Completely from scratch, all he started with were three docs: a proposal, meaning the research topic pitch; a prompt, specifying how the model should do research and write the paper; and a workflow, turning the long list of mistakes he'd made writing past papers into negative constraints.

The result, in his own words: Opus would miss a few rules, Fable missed none and got it in one pass, and Gemini and GPT just weren't paying attention at all.

He's working on something federated-learning related, so it probably didn't run into any guardrails.

As for what effort level to set — someone on reddit said high isn't enough, only xhigh gives a clear boost. I'll leave that one to verify myself later.
