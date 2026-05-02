---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "Three design mistakes I keep seeing in enterprise AI training"
slug: en/enterprise-ai-training-design
featured: false
draft: false
tags:
  - enterprise-training
  - ai-course
  - teaching-design
  - agentcrew
description: "After running AI adoption training for several companies — manufacturing to services, 20 to 100+ people — three mistakes come up almost every time."
---

Over the past six months I've run AI tool adoption training for a handful of companies — manufacturing to services, 20 to 100+ people. Almost every RFP and kickoff call comes with the same request: "We want the whole company using AI to do XX."

Sounds reasonable. In practice, it almost always goes sideways.

## The biggest mistake: confusing "unified task" with "unified method"

I ran a training where the client wanted everyone using AI for weekly reports. Built the materials, made examples, ran through it in class — all smooth. Two weeks later, fewer than 20% of people were still using it.

The reason wasn't that people didn't want to. It's that everyone's weekly report looks different. Different formats, different data sources, different things their managers actually care about. The example I gave them was "someone else's report," not theirs.

I changed the approach: in class, teach only one thing — how to make AI understand what you want it to do. The actual task? Everyone brings their own real work.

The results were noticeably different. One person tested it on a procurement contract. Another on customer complaint records. Another on shipping summaries. Same method, applied to materials each person already knows. Leaves class actually usable.

So now the first principle in my enterprise course design is: **unify the method, not the task content.** The hard part of AI adoption isn't finding one good use case — it's getting each person to find their own.

## Second mistake: open-ended pre-training surveys

Standard practice: send a questionnaire before the training, ask about daily work, use it to make the course more relevant. For a while I was asking things like: "Describe the main activities in your typical week."

The answers were almost useless. "Handle customer issues." "Coordinate across departments." "Organize data." Nothing specific enough to design around.

I switched to structured options:

- Do you spend more than an hour per week consolidating or summarizing text?
- Do you regularly produce a fixed-format document? (reports, meeting notes, status updates, etc.)
- Do you have recurring cross-team coordination processes?

Each question followed by: "If yes, roughly how much time does this take?"

That format gives me data I can actually prioritize — which tasks are most time-consuming, which have the most substitution potential. The course gets built around those specific points.

Non-technical contacts aren't unwilling to give useful information. Open-ended questions are just too abstract for them. **Designing a survey works the same way as designing an AI prompt: structure the question first, and you get structured answers.**

## Third mistake: ending the course at "follow along"

Most common training flow: instructor demonstrates a scenario, students replicate it, class ends.

The problem: when students follow along, they're working with instructor-prepared materials. What they learn is how to complete that specific task, not how to apply the approach to their own work.

I now build in a third block: **after the demo and the follow-along, students switch to their own real work and run through it again.**

This looks like just 15 extra minutes. It's actually the most important part of the session. This is where students hit their actual problems — wrong format, unexpected output, no idea how to phrase the prompt. The instructor handles those live. That's when real learning happens.

Skip this step and the odds of people using AI after they leave are low. They never had a chance to fail safely.

## Hardware vs. office companies need different curricula

After running training for a manufacturing client, I realized I couldn't just reuse my service-sector curriculum.

Office work is heavy on text and data processing. Almost every function has tasks where AI is genuinely fast. Hardware and manufacturing work includes a lot of physical operations and on-the-floor judgment calls — things AI can't help with yet.

For a hardware company, the course objective isn't "everyone finds an AI task." It's "everyone learns how to evaluate which tasks are worth trying." Instead of forcing everyone to bring home a use case, teach them a decision framework: Is the input for this task text or a physical action? Does it have a clear output standard? If yes to both, AI can probably help.

Push hardware employees to find AI uses when none fit and you'll end up with people who think AI is useless — which is worse than where you started.

## One small thing: remind people about screen privacy before demos

Not a curriculum design issue, but worth noting.

Once I asked participants to demo their actual work. Someone accidentally shared personal financial information on screen. Awkward.

Now I say this at the start of every session: "We'll be sharing work materials shortly — please check that any files you open don't contain anything you'd rather keep private. If they do, prepare a test version with dummy data beforehand."

One sentence. Prevents a lot of problems.

---

Three questions worth answering before you design an enterprise AI training:

1. Is my training task "something everyone does together," or "material each person uses to practice the method"?
2. Will someone without a technical background know how to answer my pre-training survey?
3. Is there time in the session for participants to run through their own actual work?

If any of those are hard to answer, the course design needs another pass.
