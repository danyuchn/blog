---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-05T04:00:00Z
title: "Judging AI Risk on Two Axes: Reversibility × Environment Isolation"
slug: en/ai-risk-judgment-framework
featured: false
draft: false
tags:
  - claude-code
  - ai-safety
  - workflow
  - frameworks
description: 'A common question in corporate trainings — "can I let AI do this automatically?" I answer with two axes: reversible vs irreversible, isolated vs production. This 2x2 prevents more incidents than any prompt-engineering tutorial.'
---

In this morning's corporate training session I flagged a small risk-judgment framework worth keeping handy.

When you find yourself asking "can I let AI handle this automatically?", first run it through two axes:

- **Reversible / Irreversible**
- **Isolated environment / Production environment**

## Why these two axes

**Reversibility** decides the cost when things go wrong. A wrong line of code can be edited back. A sent email cannot be unsent. Inserting a database row is recoverable. Dropping a table is catastrophic.

**Environment isolation** decides the blast radius. Running a sketchy script inside Docker — worst case is rebuilding the container. Running it on a production database — worst case is taking the company down.

Cross the two and you get four quadrants:

| | Isolated env | Production env |
|---|---|---|
| **Reversible** | Play freely, mistakes are fine | Be careful but rollback is possible |
| **Irreversible** | Still careful, but only affects you | Red line of red lines |

## The red line of red lines

A real example:

> Sending an email = irreversible
> Sending it to an external party = directly in production

Both at once — that is the red line of red lines.

The correct workflow: **draft → human review → only then send**.

My own hooks enforce this: every outbound message (Gmail, Slack, LINE Bot, third-party) goes to drafts first, I confirm, then it sends. No exceptions.

## How to apply this

Next time you are about to let AI "handle X automatically," ask yourself:

1. If this goes wrong, can I get back to the original state in 5 minutes?
2. What does this affect — only my own machine, or external people / systems?

Both answers in the "reversible + isolated" zone? Let AI run.

Any answer touching "irreversible" or "production"? Insert a human checkpoint — draft, preview, dry-run, however you implement it. But do not let AI run end-to-end.

This framework prevents more incidents than any amount of prompt engineering.
