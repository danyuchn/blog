---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-08T04:00:00Z
title: "What to Know Before Handling Sensitive Data with Claude"
slug: en/claude-sensitive-data-checklist
featured: false
draft: false
tags:
  - claude
  - security
  - enterprise
  - ai-tools
description: 'What to know before handling sensitive data with Claude: data retention windows, Enterprise contract protections, input minimization, coding agent controls, and alternative architectures.'
---

A few things to get straight before you hand sensitive data to Claude.

## Data Retention Windows

- After deletion, up to 30 days residual on the backend
- ClaudeCode API logs: 7 days
- Enterprise + ZDR: zero retention (must opt in)
- Helping improve Claude: de-identified, up to 5 years
- Policy-violating conversations: up to 2 years

## Enterprise Contract Protections

- Commitment to no storage, no training, auditable, breach is actionable
- ZDR does not apply to all features (e.g. CoWork)
- Uploaded files must be deleted via the Compliance API
- Can be compelled in litigation; not covered by attorney-client privilege

## Input Minimization

- No secrets/credentials pasted in — use placeholders
- Strip names, email, IDs, and logs from customer data first
- Give only the minimum information the task needs

## Coding Agent Controls

- Denylist `.env`, secrets, and credentials paths
- Use staging credentials, not production ones
- Human review of PR/diff before deploy
- Add a secret scanner and log scanner in CI

## Alternative Architectures

- AWS Bedrock: calls stay within your own cloud account
- Self-hosted local LLM: highest isolation, limited capability

<div class="video-embed">
<iframe src="https://www.youtube.com/embed/aSHfh5Vz1BA" title="YouTube video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
