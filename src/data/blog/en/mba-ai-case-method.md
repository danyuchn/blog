---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T08:30:00Z
title: "MBA × AI Case Method—avoiding HBS licensing risk, finding open case materials, training seed instructors"
slug: en/mba-ai-case-method
featured: false
draft: false
tags:
  - ai-education
  - case-study
  - course-design
description: 2026-05 investigation into doing case-based AI teaching for business courses. HBS / HBR cases carry licensing risk. Maps the open alternatives (UBC Open Case Studies, OpenCaseStudies.org, World Bank), what's off-limits, and the direction of training MBA-background seed instructors.
---

I've been planning case-based teaching for a business AI course. Initially I assumed buying HBS / HBR cases would just work. Reading the licensing terms revealed a minefield. This is the 2026-05 investigation.

## Cannot use

| Source | Why |
|--------|-----|
| Harvard / HBS / HBR cases | Need HBP coursepack or licensing; personal purchase ≠ permission to distribute to students; HBP terms also restrict using AI to generate derivative works |
| MIT Sloan Teaching Resources Library | The index page mentions Creative Commons, but spot-checking individual PDFs reveals `CC BY-NC-ND` (with NonCommercial + NoDerivatives); unsuitable for paid courses, can't be modified and redistributed |
| Stanford GSB free cases / The Case Centre free cases | Free ≠ open source; without case-by-case confirmation of commercial usability, don't use them in a commercial course |
| GitHub case repos with no LICENSE | Default to "all rights reserved" under law |

"Free" and "commercially usable" are completely different things. I had this wrong.

## Usable open sources

| Source | Background | License | Best fit |
|--------|------------|---------|----------|
| [UBC Open Case Studies](https://cases.open.ubc.ca/) | University of British Columbia cross-departmental OER, since 2015 | `CC BY 4.0`—commercial use OK, modifications OK, attribution required | Sustainability, public policy, education, social issues; some business cases |
| [OpenCaseStudies.org](https://www.opencasestudies.org/) | Teams affiliated with Johns Hopkins Bloomberg School of Public Health | Most repos `MIT` or `CC BY 4.0`, confirm per repo | AI / data workflow demos; real data analysis, statistics, dashboards, ML |
| [World Bank Open Knowledge Repository](https://openknowledge.worldbank.org/) | World Bank | Most content `CC BY` or `CC BY 4.0`, confirm per item; watch out for third-party charts | Public-data-driven policy / business / development cases |

### UBC Open Case Studies

UBC = University of British Columbia, a top public research university in Vancouver, Canada. Open Case Studies is not exclusive to Sauder Business School—it's a cross-departmental open educational resource. Around 69 pages, mostly on sustainability, public policy, education, and social issues. Pure MBA finance / strategy cases are sparse.

**Verdict**: good as an "open case" base, but the topics aren't pure MBA finance / strategy. Course designers need to add business decision frameworks on top.

### OpenCaseStudies.org

Not an MBA case library, but an open data science case library. Official positioning: students learn statistics and data science from real data. Used by Johns Hopkins Bloomberg, Harvard, Harvard T.H. Chan, UC Berkeley, Smith College. 2024 education paper: *Open Case Studies: Statistics and Data Science Education through Real-World Applications*.

**Verdict**: great for AI-course demos of "real data → analysis → AI-assisted interpretation → decision recommendation." To get the feel of an MBA case, you need to wrap it in a managerial decision scenario.

## Market signals for MBA × AI Case

- **NUCB Business School**: [Case Education Using Generative AI](https://mba.nucba.ac.jp/en/news/entry-23016.html)—2025 workshop with Harvard Business Publishing and AAPBS on AI-era case-based instruction
- **Newcastle University Business School**: [LOV AI Co-Creation Approach](https://microsites.ncl.ac.uk/casestudies/2025/09/01/the-lov-ai-co-creation-approach-creating-business-teaching-cases-with-deep-research-ai/)—using ChatGPT o3 Deep Research + instructor verification to produce an extended case for a Finance and Investment MBA module, claiming case development compressed from weeks to about four hours, but the core is lecturer oversight and verification
- **Hunet MBA AI Case Study** (Korea, 2026): AI coach adapts case analysis lens to student's industry / function
- **Noyes AI**: positioned as an AI case study platform, immersive scenarios, decision-making practice, references a Kellogg MBA student testimonial
- **LiveCase**: turns static cases into AI simulation / role-play / assessment, referenced by Harvard Business Impact and INSEAD

The signal: MBA × AI case method is being seriously explored by multiple business schools, but there's no mature open-source skill or framework ready to fork.

## Existing GitHub skill evaluation

2026-05-10 search across "MBA case study skill," "Claude skill case study," etc. Conclusion: **no mature open-source skill specifically built for MBA case method teaching**. Drawable references split into two clusters—consulting case analysis, and marketing/customer case-study writing.

| Repo / Skill | License | Type | Verdict |
|--------------|---------|------|---------|
| [DogInfantry/claude-skill-management-consultant-B1](https://github.com/DogInfantry/claude-skill-management-consultant-B1) | `Apache-2.0` | Management consulting / case interview / business problem solving | Closest to MBA case analysis. Has issue tree, hypothesis-driven thinking, MECE, Pyramid Principle, profitability / market entry / M&A worked cases |
| [travisjneuman/.claude — case-interview-practice](https://github.com/travisjneuman/.claude/blob/main/skills/case-interview-practice/SKILL.md) | `MIT` | Consulting case interview practice | profitability, market sizing, market entry, M&A, pricing, operations, growth strategy frameworks; CASE method flow |
| [snzeeee/claude-skill-case-study-builder](https://github.com/snzeeee/claude-skill-case-study-builder) | `MIT` | Freelancer / portfolio case study | Not MBA. Turns interviews into Challenge-Solution-Results |
| [gtmagents/gtm-agents — case-studies](https://github.com/gtmagents/gtm-agents/blob/main/plugins/content-marketing/skills/case-studies/SKILL.md) | `Apache-2.0` | GTM / customer story | CHIC: Challenge → Hypothesis → Implementation → Change |

## What `mba-ai-case-method` could look like

If I were to build one, the positioning is **not "write marketing case studies," but "turn open cases into AI-assisted MBA discussion classes."** Modules:

- **Case Intake**: load open cases from UBC / OpenCaseStudies / World Bank, confirm licensing, source provenance, modification scope
- **Teaching Note Builder**: produce case synopsis, learning objectives, discussion questions, board plan, debrief points
- **MBA Lens Selector**: pick the analytical lens (strategy, finance, marketing, operations, org behavior, ethics)
- **AI Task Designer**: break the case into AI tasks—data cleaning, competitive analysis, financial modeling, decision memo, presentation, negotiation role-play
- **Instructor Guardrail**: require fact verification, mark AI inferences, prohibit generating unlicensed derivatives of HBS/HBR cases
- **Assessment Rubric**: grade decision quality, evidence use, tradeoff reasoning, AI collaboration process—not whether the answer looks polished

## Direction for AgentCrew Academy

### Why train seed instructors first, not students directly

- I personally don't have MBA training. I shouldn't pretend to fully teach the MBA case method
- Seed instructors with MBA frameworks can attach AI workflows to strategy, finance, organization, marketing knowledge structures
- My strength is training them to convert their domain expertise into AI collaboration flow: data prep, case restructuring, prompt design, discussion facilitation, decision memo

### Course prototype

```
Open case material → Seed instructor restructures with MBA frame → AI collaboration task design
→ Students analyze case with AI → Instructor facilitates discussion → Decision memo / deck / model
```

### Potential products

- MBA Case × AI Seed Instructor Track
- AI Case Method Co-Creation Workshop
- Coaching service for converting open cases into AI teaching plans
- Public course series built on UBC / OpenCaseStudies / World Bank as base material

## Attribution template

When using `CC BY 4.0` material, the footer can read:

> Adapted from UBC Open Case Studies, licensed under CC BY 4.0. Changes were made for classroom use.

---

The core finding of this investigation: **HBS / HBR cases face growing licensing restrictions in the AI era, but the open ecosystem hasn't matured yet.** Whoever first packages UBC / OpenCaseStudies / World Bank into "AI-ready MBA case material" and trains a cohort of seed instructors will be positioned for the next wave of business education.
