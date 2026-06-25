---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-25T04:00:00Z
title: "The Client Says They Want Training, But Deep Down They Want a System"
slug: en/bd-letting-go-training-vs-system
featured: false
draft: false
tags:
  - consulting
  - business
description: 'A post-mortem on letting go in a BD deal: the client drifted toward "give me an artifact" three times, and I changed one phrase from "after the training" to "if the priority is to build the hub" — and handed the ball back.'
---

Kevin works at a multinational logistics company. These past few days he reached out on his own, said he agreed that Claude is indeed the stronger option, and casually asked how to enable Copilot Cowork. It looked like a smooth training engagement: the client's sold, the client wants to use it, the client's asking about the operations. But he immediately tacked on a counter-question: "What if even Cowork can't be enabled — what's the fallback then?"

That question landed with me. On the surface it's a question about tools, but underneath it was actually pulling the premise out from under the whole engagement for me — if I tie the training to "waiting until some tool is confirmed usable," then the moment the tool stalls, the engagement stalls with it.

I used first-principles to cut away that inherited assumption. "Wait until the tool is confirmed before training" is a completely unnecessary coupling. Tool deployment is one track and capability building is another, and those two can run in parallel from the start — they don't need to wait on each other. Once I'd thought that through, I drafted a three-track plan for him: C is going through Claude inside the company cloud (Bedrock or Vertex, running in their own cloud environment); A+B is using a personal account plus mock data, which can be practiced right now, with zero dependence on whether the company enables the tool; D is on-prem Qwen, as a safety net, parked for now and not pushed.

The second drift was in his next follow-up. He said: "their system can't access Claude — won't this limit the possibilities? I'm even thinking of building a webapp myself to serve as a hub."

At this point my read of the situation became clear. First, he's half-skeptical about the value of "building the muscle" — he doesn't quite believe that merely developing capability will be useful. Second, this was his third time drifting toward "give me an artifact." The first time was wanting AI to help make a PPT, the second was that agentic stuff in Q2, and this time it's a webapp hub. He's a builder by temperament; his hands keep itching for something tangible to hold, rather than an invisible set of capabilities on his person.

When I replied, I did three things: first, asked back exactly which layer the blockage was at; then argued for training first; and as for the webapp hub, I was honest — building apps isn't my strength, I won't force the engagement, but I can refer him to someone.

The real letting-go move was hidden in a single changed phrase. What I'd originally written was "after the training" — we train first, then look at the hub later. I later changed it to "if the priority is to build the hub" — if your priority is to get the hub built first.

What's the difference? "After the training" is me sequencing it for him: training first, hub second, which means I'm still holding onto control and also presupposing that this is a training engagement. After changing it to "if the priority," I removed the entire sequence coupling and handed the ball back to him. It's a qualifying move: how he chooses directly determines the nature of this engagement. If he picks training first, it's a training engagement; if he picks building the hub first, it's a referral engagement, and I refer out the development part. Either outcome, I don't lose.

Getting it to this point, I wasn't quite at ease, so I sent in two subagents to review it — one /minimalist-entrepreneur, one /street-smarts. They picked out three blind spots. First, my quote and the client's true intent weren't aligned at all, and if it kept going like this I'd likely hand over a hallucinated quote — quoting for training when what he wants is a system. Second, the free referral amounts to giving away, for nothing, a cash flow bigger than the main engagement — the development job's pie is far bigger than training, and I was planning to give it away free. Third, my timing for letting go was a step too early, and it was laced with emotion too.

Then Kevin came back with the blockage layer: it's a network block, the strictest of the three layers.

That answer actually converged the situation. Reading it technically: A+B training is completely unaffected by the network block and can run as-is; and for the webapp hub under this kind of block, the only compliant path is a cloud backend plus a webapp frontend. In other words, the hub he wants and the only compliant architecture turn out to be the same path. What had looked like mutually exclusive — "he wants a system" and "I can deliver compliantly" — got forced into the same direction by this strictest constraint.

For the next round I plan to lay it on the table: talk about "system vs. capability" openly; turn the referral into a paid supervisory advisory role, quoted separately, no more giving it away free; and then run a 30-minute demo for him using mock data.

Looking back at this whole thing, the most crucial part wasn't which plan was technically prettiest, but that changed phrase. Swapping "after" for "if the priority" is essentially admitting that I can't control his sequence, and that I shouldn't pretend this is necessarily a training engagement. The rest is left to his choice — however he chooses, however I quote, I don't lose.
