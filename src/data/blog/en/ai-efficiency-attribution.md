---
author: Dustin Yuchen Teng
pubDatetime: 2026-11-25T01:00:00Z
title: "80% of Workers Say They Feel Faster, Yet 83% of Executives Report Zero Net Impact on Labor Productivity: Who Gets Credit for Enterprise AI Efficiency?"
slug: en/ai-efficiency-attribution
featured: false
draft: false
tags:
  - ai-trends
  - enterprise-ai
description: 'Nearly 80% of enterprises have adopted AI and 80% of respondents report higher personal productivity, yet 83% of executives report zero net impact on labor productivity over the past three years. Empirical research and modeling from 2002 to 2026 show that under a 50/50 split of complementary synergy, 65% to 80% of efficiency gains in low-to-medium maturity firms come from data governance and process redesign.'
---

80% of surveyed workers report higher personal productivity after using AI, yet 83% of corporate executives say AI has had zero net impact on their company's overall labor productivity (revenue per employee) over the past three years.

This stark contrast comes from two large cross-national surveys published in 2026:

- **80%**: A global survey released by McKinsey in August 2026, covering 1,719 respondents.
- **83%**: A large enterprise census revised in October 2026 by researchers from the Federal Reserve Bank of Atlanta, the Bank of England, other central banks, and Stanford University, published by the National Bureau of Economic Research (NBER Working Paper No. 34836). This census surveyed nearly 9,000 CEOs and CFOs across seven countries:
  - 78% of firms already use some form of AI;
  - Only 15% clearly see gains in labor productivity;
  - Across all firms, annualized productivity growth translates to just 0.2%.

Why do employees widely feel faster while company-wide output on the books barely moves? I synthesized long-term cross-national enterprise tracking data, controlled management experiments, central bank censuses, and software engineering telemetry from 2002 to 2026 to answer the question business owners and executives care about most: when an enterprise adopts AI, how much of the resulting efficiency gain actually belongs to AI, and how much comes from taking the opportunity to clean up data, streamline cross-team workflows, and write clear standard operating procedures (SOPs)?

**Download the full report:** [Why Do Employees Feel Faster While Company Financials Barely Move? (Decision-Maker Edition, PDF, English, 7 pages)](/blog/assets/posts/ai-efficiency-attribution/ai-efficiency-attribution-report-en.pdf)

## Without Buying Any AI, How Much Can You Gain Just by Cleaning Up Processes and Data?

To measure AI's true contribution, we first have to ask a counterfactual baseline question ("what if we had not bought AI"): if a company focused solely on cleaning up data, straightening out workflows, and establishing SOPs without buying any AI software or new machinery, how much would efficiency improve on its own?

Controlled experiments in management studies give a clear answer:

- **Indian textile plant experiment (Bloom et al., 2013)**: Researchers introduced 38 basic management practices to one group of factories, including setting SOPs, systematically tracking defect rates and inventory, and holding daily quality review meetings, without adding any new automation machinery or AI software. In the first year alone, overall operational efficiency (total factor productivity) rose by 17%, and product defect rates were cut in half (dropping about 50%).
- **U.S. Census Bureau collaborative study (2019)**: Simply raising basic management practices from the bottom tier (10th percentile) to the top tier (90th percentile) accounts for 18% of the overall productivity gap between top- and bottom-performing U.S. manufacturers.
- **Accumulated industry experience in data remediation**: For companies with immature governance, doing the basic work on data and processes without relying on AI typically yields 12%–20% efficiency growth (reaching 12%–22% depending on the depth of the overhaul).

Conversely, skipping the basics and forcing AI into place can make things worse in the short term. A 2025 tracking study of legacy manufacturing plants by McElheran et al. found:

- When factories first increased their AI usage, short-term productivity actually fell.
- Beyond work-in-progress bottlenecks on the production line, the bigger culprit was a drop in basic management discipline: assuming AI would handle everything, frontline teams paid less attention to key performance indicators (KPIs) and lost company-wide alignment on goals.
- This neglect of management and SOP discipline directly caused about one-third of the short-term overall efficiency loss; when combined with the erosion of existing team coordination and institutional assets, it accounted for two-thirds.

## Why Do Individual Time Savings Evaporate at the Company Level?

Task-level experiments do prove that generative AI can save writers 40% of their time and boost customer service agents' resolved cases per hour by 15%. So why do those time savings disappear across organizational layers when point tools are deployed inside real companies?

**First reason: the weakest-link (bottleneck) effect shifts the bottleneck downstream.** In engineering, Amdahl's law states that the speedup of an entire pipeline is limited by its slowest, unaccelerated stage.

- What AI does best, writing first drafts of text or code, typically accounts for only 15%–30% of total project delivery time.
- The remaining 70%–85% goes to cross-department alignment, waiting for manager sign-offs, and downstream review and rework.
- Software engineering analytics platform Faros AI tracked system telemetry from over 10,000 engineers in 2025 and roughly 22,000 engineers in 2026 (real-world workplace observational data), capturing a massive downstream traffic jam:
  - Pull requests (PRs) submitted for merge jumped 98%;
  - Peer code review duration stretched 91% longer;
  - Production incidents per merged PR surged 242.7%;
  - In the 2026 dataset, total production incidents reached 3.4 times the baseline.

The faster code is written upstream, the worse bug fixing and firefighting clog up downstream.

[![After adopting AI, engineers submitted 98% more pull requests, but code review time increased by 91% and production incidents per merged pull request jumped by 242.7%.](/blog/assets/posts/ai-efficiency-attribution/faros-en.jpg)](/blog/assets/posts/ai-efficiency-attribution/faros-en.jpg)

*Figure caption: Upstream output surges while downstream queues jam. Source: Faros AI telemetry (2025–2026), adapted from AgentCrew Academy Enterprise AI Evidence Report figure 2.*

**Second reason: the illusion of feeling faster, combined with hidden landmines from uneven AI capabilities.** Researchers call the latter the jagged technological frontier: AI answers some seemingly difficult problems in seconds, yet confidently fabricates nonsense on seemingly simple logic.

- **METR (2025)**: Ran a randomized controlled trial across 246 real tasks with experienced open-source software developers working in their own familiar repositories.
  - After finishing, developers firmly believed AI had made them 20% faster;
  - On the stopwatch, developers using AI were actually 19% slower than those working without it;
  - The gap between subjective perception and objective timing approached 40 percentage points.
  - In an expanded 2026 follow-up, confidence intervals for actual speed in both groups crossed zero, showing no consistent speed advantage either way, alongside a 30%–50% selection bias toward assigning easier tasks to AI.
- **Dell'Acqua et al. (2023)**: An experiment with 758 Boston Consulting Group (BCG) consultants found:
  - Inside AI's capability boundary, output quality rose by more than 40%;
  - Once a task stepped outside AI's boundary, consultants relying on AI were 19 percentage points less likely to produce a correct answer than those working without AI.

[![In the METR randomized controlled trial, developers predicted a 24% time savings before starting and estimated a 20% time savings after finishing, yet stopwatch timing showed they took 19% longer.](/blog/assets/posts/ai-efficiency-attribution/metr-en.jpg)](/blog/assets/posts/ai-efficiency-attribution/metr-en.jpg)

*Figure caption: The gap between perceived speed and stopwatch time. Source: METR randomized controlled trial (July 2025; 16 experienced developers, 246 real tasks), adapted from AgentCrew Academy Enterprise AI Evidence Report figure 3.*

## Splitting the Credit: 65%–80% Comes from Fundamentals, Plus Three Exceptions

To date, neither academia nor industry has run a four-arm randomized trial of comparable companies (process cleanup only, AI purchase only, both, and neither) that cleanly separates process governance from AI software at the corporate financial statement level. The widely cited BCG "10-20-70 rule" (10% algorithms, 20% technology and data backbone, 70% people and process transformation) is likewise a practitioner heuristic built on years of consulting experience rather than an econometrically estimated figure.

Still, we can draw on the complementarity model developed by economists Milgrom, Roberts, and Brynjolfsson (where pairing sound processes with capable tools generates supermodular gains neither achieves alone) to run a counterfactual decomposition for firms with weaker foundations, calibrated against historical data.

Suppose a low-to-medium maturity company completes an end-to-end AI workflow overhaul and achieves a +20% to +50% overall efficiency gain. Breaking down that total pie:

- **Standalone contribution from cleaning up data and SOPs without turning on AI**: 46%–62% of the total improvement.
- **Standalone tool contribution from bolting on AI without changing processes**: only 0%–14%.
- **Complementary synergy unlocked only when clean data workflows meet AI**: 35%–54%.

Who gets credit for the synergy that only appears when both sides come together? Using the standard game-theoretic approach of splitting joint surplus by marginal contribution, I divide that synergy 50/50 between process governance and AI tools (this modeling provides decision-making reference ranges rather than a rigid verdict for any single company). Across four common enterprise scenarios, the attribution breakdown looks like this:

| Baseline Company Maturity & AI Type Deployed | Total Process Efficiency Gain (Median) | Contribution from Data & Process Cleanup Alone | Contribution from Bolting on AI Without Process Change | Complementary Synergy Unlocked by Combining Both | Final Credit Split (Process Governance vs. AI Tools) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1. Weaker foundation + Traditional predictive AI | +20% to +32% (+26.0%) | +12 to +20 percentage points (16.0) | 0 to +2 percentage points (1.0) | 9.0 percentage points | **79% vs. 21%** |
| 2. Weaker foundation + Generative AI / copilots | +25% to +40% (+32.5%) | +12 to +20 percentage points (16.0) | +3 to +6 percentage points (4.5) | 12.0 percentage points | **68% vs. 32%** |
| 3. Weaker foundation + Multi-step autonomous agentic AI | +30% to +50% (+40.0%) | +15 to +22 percentage points (18.5) | -2 to +2 percentage points (0.0) | 21.5 percentage points | **73% vs. 27%** |
| 4. Mature foundation + Generative / agentic AI | +18% to +30% (+24.0%) | +3 to +7 percentage points (5.0) | +5 to +10 percentage points (7.5) | 11.5 percentage points | **45% vs. 55%** |

[![Credit attribution across four enterprise scenarios: process governance accounts for 68% to 79% of efficiency gains in firms with weaker foundations, while AI tools account for 55% in firms with mature foundations.](/blog/assets/posts/ai-efficiency-attribution/attribution-en.jpg)](/blog/assets/posts/ai-efficiency-attribution/attribution-en.jpg)

*Figure caption: Credit attribution across four enterprise scenarios. Source: AgentCrew Academy Enterprise AI Evidence Report figure 5 (modeled on complementarity theory and a 50/50 synergy split).*

Under a 50/50 split of the synergy bonus:

- For a typical firm with weaker operational foundations, roughly **65%–80%** of efficiency growth (the medians of the first three scenarios in the table are 68%–79%) belongs to data cleaning, workflow redesign, and SOP clarification; only about 20%–35% comes directly from AI technology itself.
- Today's much-discussed agentic AI (agents that execute tasks autonomously across systems) delivers roughly 0% standalone benefit when bolted onto an unreformed workflow; once paired with a cleaned-up process, however, the complementary synergy accounts for 53.8% of the total gain.

That does not make AI expensive wrapping paper. Empirical research from 2025 to 2026 identifies three boundary conditions where AI takes on the primary role.

**First, in high-maturity firms that have already nailed the basics, AI takes the lead.**

- As shown in row 4 of the table above: when a company's data backbone, field definitions, and lean SOPs are already well established, further manual process tuning leaves only 3%–7% room for improvement.
- Under the same attribution method, AI technology plus its share of synergy flips to account for roughly **55%** of the gain (falling in the 50%–60% range).
- A 2025 comparison of 152 enterprises by the MIT Center for Information Systems Research (MIT CISR) showed a similar pattern:
  - Companies stuck in Stage 2 (running scattered small-scale pilots) posted revenue growth 6.8 percentage points below industry peers and net profit margins 1.4 percentage points lower;
  - Companies advancing to Stage 3 (building standardized AI ways of working and shared platforms) beat industry peers by +0.8 percentage points in revenue growth and +4.7 percentage points in net margin;
  - Leading firms reaching Stage 4 (overhauling their core operational backbone) outperformed peers by +9.9 and +13.9 percentage points, respectively.
  - Note: This is a cross-sectional comparison of different companies at a single point in time rather than a before-and-after panel of the same firms, so part of the gap reflects stronger pre-existing fundamentals.

**Second, for self-contained tasks that require no cross-department handoffs and rely heavily on veteran intuition, deploying AI works right away.** Some jobs involve very little cross-team passing of the baton but depend heavily on tacit knowledge in veterans' heads that is hard to articulate or write into a manual. In those cases, introducing generative AI can pay off immediately without a major SOP overhaul.

- Brynjolfsson, Li, and Raymond (2025) tracked 5,172 customer support agents: without changing existing support SOPs, simply embedding a language-model assistant into the ticketing system raised average resolved issues per hour by 15%, while novice and low-tenure agents improved by 30%–36%.
- First key factor: text-based customer support runs almost entirely from intake to resolution inside a single chat window, without long queues for cross-department approvals.
- Second key factor: AI turns the tacit know-how of top veteran agents into real-time prompts, helping novices close the experience gap quickly.

**Third, AI acts as a two-way engine that converts veteran know-how into institutional assets, and as a political catalyst for internal reform.**

- A 2026 NBER study by Babina, He, and Jiang (Working Paper No. 35684) tracked 15 years of data on U.S. public companies: between 2018 and 2024, each one-standard-deviation increase in a firm's AI talent share growth corresponded to 6.2 percentage points higher revenue-per-employee growth and 7.5 percentage points higher overall revenue productivity over six years.
- Across that period, an average of 58% of U.S. AI job postings (and 66% of generative and agentic AI postings in 2024) focused not on inventing new algorithms, but on encoding human work methods into systems and rules to build durable organizational capital; moreover, only these institution-building AI roles actually drove firm-level productivity growth.
- During the business process reengineering wave of the 1990s, roughly 50%–70% of projects failed due to departmental resistance or lack of momentum. Today, "adopting AI" often serves as the best internal catalyst: unglamorous data cleanup and SOP overhauls that nobody normally wants to fund or touch suddenly win executive budget approval and cross-department cooperation once they are badged as an AI initiative.

[![Share of roles encoding human expertise into organizational capital: 31% for non-AI baseline roles, 58% across 2018–2024 for all AI roles, 66% for generative and agentic AI roles, and 79% for AI management and architecture leadership roles.](/blog/assets/posts/ai-efficiency-attribution/babina-en.jpg)](/blog/assets/posts/ai-efficiency-attribution/babina-en.jpg)

*Figure caption: Share of AI roles dedicated to encoding human experience into institutional assets. Source: Babina, He, and Jiang (2026, NBER Working Paper No. 35684), adapted from AgentCrew Academy Enterprise AI Evidence Report figure 6.*

## Four Steps to Take Before Buying Your Next AI Tool

Deloitte's 2026 global enterprise leadership survey (covering 3,235 leaders across 24 countries in the January release, later expanded to 3,500) found that while 81% of executives believe AI has sped up execution, only 40% of companies have built solid data management foundations, and just 15% have actually redesigned workflows and job roles. Before signing your next AI software purchase order or compute bill, walk through these four steps in order:

1. **Follow the four-step rule: Eliminate, Simplify, Standardize, Automate.**
   - Eliminate: First cut redundant approval layers that add no real quality control;
   - Simplify: Streamline cross-department handoffs to compress the waiting time that eats up 70%–85% of delivery schedules without being sped up by AI;
   - Standardize: Unify conflicting spreadsheet field definitions and exception-handling SOPs across departments;
   - Automate: Only bring in AI to automate at the final step.
2. **Measure real elapsed time in two stages instead of sending out surveys asking if people "feel faster."**
   - Before kicking off a project, use a stopwatch to baseline total end-to-end delivery time from intake to completion alongside the rework/rejection rate (as the METR experiment showed, employee self-assessments can diverge from actual clock time by nearly 40 percentage points).
   - Split project sign-off into "Stage 1: Data cleanup and SOP simplification" and "Stage 2: AI deployment," measuring each separately so you can see clearly how much improvement came from process housekeeping versus the net return bought by AI license fees.
3. **Spend your budget on encoding veteran know-how into systems rather than handing out scattered personal chat seats.**
   - Guided by the 10-20-70 rule and McKinsey's recommendation to pair every $1 spent on technology with $5 invested in people and process redesign, avoid scattering your budget on generic AI chat accounts for employees to figure out on their own.
   - Focus resources on one or two core business workflows, turning senior experts' decision criteria and historical work tickets into machine-readable institutional assets that the system can continuously update.
4. **Put acceptance standards in writing and set permission guardrails for AI.**
   - Define what counts as acceptable output quality in written SOPs;
   - Set tiered human review checkpoints for high-risk changes;
   - Assign a named human business owner to every AI-run workflow so someone is accountable when things go wrong, rather than blaming the AI.

Cut the wasted motion out of your workflows and align your data definitions first, then decide whether you need to buy the next AI tool.

**Download the full report:** [Why Do Employees Feel Faster While Company Financials Barely Move? (Decision-Maker Edition, PDF, English, 7 pages)](/blog/assets/posts/ai-efficiency-attribution/ai-efficiency-attribution-report-en.pdf)

## Appendix: Modeling Logic and Cited Research

- **Modeling logic**: The attribution percentages in this article are decision-reference ranges calibrated against historical data using economics complementarity models (Milgrom & Roberts, 1990; Brynjolfsson et al., 2021) and game-theoretic fair-attribution division (the Shapley value, splitting jointly generated synergy 50/50). They are not results from a single-firm four-arm randomized experiment. The BCG 10-20-70 rule and McKinsey's 1-to-5 investment ratio (2026 report) cited in the text are management consulting rules of thumb.
- **Primary cited studies**: McKinsey Global Survey (2026); NBER seven-country central bank enterprise census (Yotzov, Bloom, Davis et al., 2026, Working Paper No. 34836); Deloitte Global Leadership Survey (2026); Bloom et al. management experiment and census studies (2013 in *Quarterly Journal of Economics (QJE)*; 2019 in *American Economic Review (AER)*); McElheran et al. manufacturing AI tracking study (2025, *Industrial AI*); Faros AI software engineering telemetry analysis (2025–2026, commercial observational data); METR open-source developer randomized controlled trial (2025–2026); Dell'Acqua et al. consultant experiment (2023); MIT CISR enterprise maturity comparison (2025, cross-sectional observational comparison); Brynjolfsson, Li, and Raymond customer support AI study (2025, *QJE*); Babina, He, and Jiang organizational capital study (2026, NBER Working Paper No. 35684).
