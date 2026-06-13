---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-09T04:00:00Z
title: "Don't Dump the Last Session's JSON — Check Your Harness First"
slug: en/harness-checkup-no-json-dump
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: 'No need to feed the whole context JSON from your last conversation: the harness has several layers — AGENTS.md, rules, skills, hooks — and raw session history is full of useless tool calls.'
---

Wait, why would you feed it the context JSON from the last conversation?

The harness comes in several kinds — AGENTS.md, rules, skills, hooks — and they can all carry the load. Summarizing the key points from the previous conversation into a temporary doc works well too.

Raw session history holds too many tool calls, outputs, and flags that are useless; even auto compact strips those out.

I'd suggest doing a fresh checkup on your harness first.
