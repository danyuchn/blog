---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: Some of My Subagents Were Already Grandpas
slug: en/ccx-quota-surge-forensics
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - debugging
description: 'A CCX quota incident with no guardrails set: subagents bred recursively, one session burned 90% in half an hour, and here is the full forensics and fix.'
---

Yesterday I just didn't set this up, and the subagents bred like crazy. Some of them were already grandpas.

I was using CCX, my own alias for orchestrating multiple agents. In that session I hadn't turned off nested subagents, and I hadn't capped the total number of subagents either, so it kept spawning downward, one generation begetting the next, several generations stacked up. The result: one session burned 90% of my quota in half an hour.

Afterward I ran the forensics: it was recursive fan-out, Agent Teams, everyone running on the most expensive Sol, long context, plus an old proxy version, all multiplied on top of each other. Any single one of them might have been fine; put together, it blew up.

The fix was to bump CLIProxyAPI from 7.2.73 to 7.2.91, then add a few guardrails to `ccx()`: a cap on total subagents, a cap on parallelism, background execution, a retry count, and compression. I ran one test round — 2 Terra subagents, depth 1, zero nesting — and it ended normally, no runaway burn. `cc` and `cdx` I left alone.

That's the thing to watch out for. Besides setting the compaction window yourself, remember to turn off nested subagents and cap the total number of subagents.

<!--
Added-sentence disclosure (fidelity self-report), mirrors the zh file:
1. "I was using CCX, my own alias for orchestrating multiple agents." — Type: framing (tells the reader what CCX is; not spelled out in source A/B)
2. "In that session I hadn't turned off nested subagents, and I hadn't capped the total number of subagents either, so it kept spawning downward, one generation begetting the next, several generations stacked up." — Type: rewrite (unpacks source B's "some subagents were already grandpas" imagery into mechanism, adds no new claim)
3. "Any single one of them might have been fine; put together, it blew up." — Type: bridge (carries source A's "multiplied together" causality; minimal)
4. "I ran one test round" / "it ended normally, no runaway burn" — Type: rewrite (colloquial restatement of source A "verified... ended normally")
All other sentences (burned 90%, grandpas, recursive fan-out/Agent Teams/Sol/long context/old proxy, CLIProxyAPI version numbers, the five ccx guardrails, 2 Terra subagents depth 1 zero nesting, cc/cdx unchanged, turn off nested subagents cap the total, set the compaction window yourself) come directly from source A/B.
-->
