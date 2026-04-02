---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-30T04:00:00Z
title: "PII Guard TW: A De-identification Tool Built for Taiwan"
slug: en/pii-guard-tw
featured: false
draft: false
tags:
  - ai-tools
  - ai-security
description: There's no off-the-shelf de-identification tool for Taiwan's PII formats. So I built one that keeps sensitive data on your machine while you send the rest to AI.
---

I was recently using AI to process client data, and the client was clear: sensitive information should not be sent to AI servers. But when I went looking for de-identification tools, I hit a wall—Taiwan's PII formats (national ID numbers, local phone numbers, tax IDs) aren't supported by any existing tool.

So I combined an open-source library with local adaptations and built [pii-guard-tw](https://github.com/danyuchn/pii-guard). It automatically replaces PII in your documents with placeholders, lets you send the sanitized version to AI for processing, and then restores the original data afterward. Your real data never leaves your machine.

## Supported PII Types

- National ID numbers, resident certificate numbers, passport numbers
- Mobile numbers (09xx / +886 format), landlines
- Email addresses, credit card numbers
- Tax ID numbers (統一編號, Taiwan's business registration number), license plates, dates of birth, bank account numbers
- Person names, organization names, location names (detected via CKIP BERT, a Mandarin NLP model from Academia Sinica)

## Supported File Formats

- Plain text (.txt / .csv / .tsv)
- Excel (.xlsx) — processes cell by cell, preserves formatting
- Word (.docx) — handles both paragraphs and tables
- PDF (.pdf) — extracts text first, then processes

## MCP Integration

There's also an MCP server so you can plug it directly into Claude Code and use it seamlessly in your workflow.

Still very early stage—issues and PRs are welcome.

## A Note for API / Enterprise Users

Claude API and Enterprise users can refer to Anthropic's official ZDR (Zero Data Retention) policy—your data isn't retained by default. For regular subscription users, besides using a de-identification tool, remember to go into your settings and turn off "Allow my data to be used for model training." That way your data is only stored by Anthropic for 30 days instead of five years.
