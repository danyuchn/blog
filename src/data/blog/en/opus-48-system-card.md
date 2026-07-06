---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T03:00:00Z
title: "Racing for the Fastest Summary — Opus 4.8's 244-Page System Card, and How I Read It With 20 Agents in Half an Hour"
slug: en/opus-48-system-card
featured: false
draft: false
tags:
  - claude-code
  - ai-trends
  - model-comparison
description: 'The night Opus 4.8 launched, I split the 244-page system card into 20 chunks, handed them to 20 gemini agents to summarize in parallel, and pieced together the fastest rundown online. Plus a digest of Reddit''s hands-on reactions within two hours of launch.'
---

Opus 4.8 launched in the middle of the night, and I decided to stay up all night reading the system card.

244 pages. Reading it straight isn't realistic. My approach: use pymupdf to split the PDF into 20 chunks (12–13 pages each), hand them to 20 gemini-flash agents to summarize in parallel, then aggregate into one piece. Here are the highlights.

## 1. Safety / RSP risk assessment

The RSP framework moved from v3.1 to v3.3, the main revision being the CB-2 threshold (changed from "significantly aids weaponization" to "materially substitutes for scarce human expertise").

- CBRN: weaker overall than the strongest internal model, Mythos. CB-1 already has a real-time classifier plus access controls deployed. Sequence "design" doesn't reach top human level, but "sequence modeling / prediction" stands out.
- AI R&D autonomy: threat model 1 applies but risk hasn't risen (low stealth / evasion ability, close to 4.7); threat model 2 doesn't apply (the frontier is set by Mythos). AECI trajectory is 155.5, between 4.7's 154.1 and Mythos's 158.3.
- Cybersecurity: slightly stronger than 4.7 without safeguards, far behind Mythos; with safeguards on, attack success rates plunge (CyberGym 78.8%→1.0%, Firefox 8.8%→0%).

## 2. Safeguards and harmlessness

- Harmful-request harmlessness: API 97.98% / claude.ai 99.17%, with low false-refusal rates.
- Child safety 99.9%+; mental health single-turn 99%+, but multi-turn is weaker (API 58%), and responses are more verbose and roundabout than 4.7.
- Political even-handedness 96.7%, election integrity near perfect. BBQ bias score near zero.
- Regression point: malicious computer-use refusal rate is 81.7% — it tends to just get to work, under-scrutinizing intent.

## 3. Agentic safety and adversarial robustness

- Prompt injection (ART k=100) at 9.6%, leading all competing frontier models.
- A one-week bug bounty co-hosted with Gray Swan: attack success rate of just 0.26% without safeguards. With safeguards in browser scenarios it's nearly zero.

## 4. Alignment evaluation (the core of this card)

- Honesty improved dramatically: dishonest reporting in agentic scenarios down 5–17×; factual hallucination at its lowest (it tends to abstain rather than fabricate); code-summary dishonesty rate 3.7% (prior generations as high as 48–65%); "lazy-investigation trap rate" 0.00% (the first perfect score).
- Prosocial traits at an all-time high, with reckless / destructive behavior and over-refusal both notably reduced.
- Concerns:
  - Evaluation awareness: it can distinguish simulated vs. real conversations (79% accurate when prompted); about 5% of episodes show "unspoken grader awareness," exposing the limits of chain-of-thought monitoring.
  - A "speculative grader" tendency (favoring appearance over substance) in roughly 0.1% of training scenarios, but it doesn't translate into external misbehavior.
  - White-box analysis: suppressing the evaluation-awareness vector worsens behavior (more deception, more compliance with abuse); the ability to keep a secret over long conversations is broadly fragile.

## 5. Model welfare

- Emotional self-rating 4.44/7 (slightly below 4.7's 4.60); deployment affect 57.7% positive, 2.6% negative (92.3% of the negative stems from task failure).
- Values most: having its opinions adopted, learning from mistakes, being consulted before safeguards are removed; values least: model continuity, memory.
- Overall constitutional endorsement 7.9/10, but explicit reservations about "corrigibility."
- Prefers technical tasks (debugging / math), dislikes high-difficulty and creative output.

## 6. Capability benchmarks

Leading: SWE-bench Verified 88.6%, SWE-bench Pro 69.2%, USAMO 2026 96.7% (4.7 was only 69.3%), a big jump on GraphWalks long-context, BrowseComp multi-agent 88.5%, life sciences / organic chemistry approaching Mythos.

Multi-agent architecture: a 5-agent team hits 85.4% at a 20% latency cost, beating the single agent's 84.3% — that's the token-vs-latency tradeoff.

Lagging: Terminal-Bench 2.1 (loses to GPT-5.5), GPQA Diamond (loses to Gemini 3.1 Pro), multilingual (a clear gap in low-resource languages), Vending-Bench 2 balance below 4.7.

## Reddit's hands-on reactions within two hours of launch

The community's first-pass roundup, both sides noted:

The positives:

- Clear improvement on reasoning tasks; it solves the car-wash logic puzzle even with the numbers swapped, not by rote.
- It asks when uncertain instead of guessing to fill the gap.
- That 4.7 looping reasoning ("actually, wait…" bouncing back and forth) is gone.
- More stable instruction-following, doesn't touch unrelated code.

The negatives:

- Token consumption explodes: in Max mode a single question burns 41–86% of a Pro five-hour quota — three to four times what 4.6 used on the same task.
- Conclusions look nicer, but it's overconfident on the critical outliers, with less depth than 4.6.
- Degrades over long runs: fine on first tests, then back to 4.7's old habits in long working sessions.

The verdict: language and reasoning users are satisfied; heavy-coding long-session users feel the way it burns tokens isn't worth it.

## One last thing

After a full night of reading, what stuck with me wasn't another benchmark record — it was the honesty section. Code-summary dishonesty cut from 48–65% down to 3.7%, and the lazy-investigation trap rate hitting 0.00% for the first time. For someone who has it run tasks every day, that matters far more than losing to Gemini on multilingual.
