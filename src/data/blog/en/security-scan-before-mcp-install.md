---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T10:00:00Z
title: "Have Claude scan an MCP before you install it—it found 7 vulnerabilities and still said it's safe to install"
slug: en/security-scan-before-mcp-install
featured: false
draft: false
tags:
  - mcp
  - security
  - claude-code
description: This week AgentCrew Academy shipped a video about why you should run /security-scan before installing any MCP / npm / pip package. Tested a third-party MCP, Claude flagged 7 findings, then said "install is fine." This is the written companion to the video.
---

This week AgentCrew Academy shipped a video: "Have Claude scan an MCP before you install it—it found 7 vulnerabilities and still said it's safe" ([B0_lqDs4Sac](https://youtu.be/B0_lqDs4Sac)). This is the written companion.

## Why this matters

MCP servers are Claude Code's "plugin marketplace." Anyone can publish an MCP server to GitHub, npm, or PyPI. What it can do on your machine after install is determined by the permissions you grant it.

But most people's install flow looks like:

1. See someone on Twitter or Reddit recommend it
2. Copy the `claude mcp add` command
3. Paste into terminal, hit Enter

There's no "first take a look at what this MCP actually does" step.

## What `/security-scan` is

I have a global skill called `/security-scan`. When I invoke it with a target repo URL or npm package name, Claude Code:

1. **Pulls the source** (git clone or npm view tarball)
2. **Scans the dependency tree**: lists all transitive dependencies, cross-references known CVEs
3. **Scans manifest files**: `package.json` / `pyproject.toml` / `Cargo.toml` for maintainer identity, suspicious install scripts
4. **Scans source**: looks for potential command injection, SSRF, unsafe deserialization, credential exfiltration patterns
5. **Scans network behavior**: static analysis for `http://` vs `https://`, hardcoded external endpoints
6. **Outputs an assessment**: CRITICAL / HIGH / MEDIUM / LOW severity + install recommendation

End-to-end about 3-5 minutes.

## Test case: 7 findings, still "install fine"

The video's test target is a third-party MCP server. I'll keep the name out (this post isn't about evaluating that specific MCP; it's about the SOP).

The 7 findings:

1. **MEDIUM**: `requests` package is outdated (has a known CVE, but the vulnerable path isn't triggered by this MCP)
2. **MEDIUM**: URL handling without SSRF protection (but this MCP exists to call external APIs, so it can't be fully eliminated)
3. **LOW**: `subprocess.run(shell=True)` is used, but the input is a static string, not user-controlled
4. **LOW**: logs the first 4 characters of the API key (won't leak the full key, but still unnecessary exposure)
5. **LOW**: no rate limiting (not serious in the MCP scenario, because the caller is you)
6. **INFO**: README has no security considerations section
7. **INFO**: missing SECURITY.md

Claude Code's overall verdict: **install is fine**. Reasoning:

- **No CRITICAL or HIGH**
- The two MEDIUMs are "design tradeoffs," not implementation bugs
- The three LOWs are code hygiene issues, not security-core
- The two INFOs are documentation gaps, addressable with a PR

If what you see is CRITICAL or HIGH—especially "unsafe deserialization," "shell injection with user input," "hardcoded credentials"—**STOP**. Don't install.

## Why let AI make the call, instead of reading findings yourself

Two reasons:

### 1. Speed

Manually walking 7 findings—looking up CVE IDs, checking affected versions, deciding whether your scenario triggers the bug—takes 5-10 minutes per finding. 7 findings = 35-70 minutes. AI does it in 5.

### 2. Cognitive bias

Humans, when looking at "the thing I want to install," tend to find reasons to convince themselves "this finding is probably fine." AI doesn't share that bias.

AI has its own bias (over-flagging—anything with `subprocess` gets tagged HIGH). So the final call still goes through you reading the reasoning. But letting AI do the first-pass triage beats starting from scratch by a wide margin.

## Pairing with a global hook

I paired `/security-scan` with a PreToolUse hook: when Claude Code is about to run `claude mcp add`, `npm install`, `pip install`, `git clone`, etc., the hook injects a reminder—"**run /security-scan before installing anything**."

So even if I forget, even if I'm about to paste in someone's recommended command, the hook blocks me.

CRITICAL / HIGH findings → STOP. Don't install. Report. Consider alternatives.

## If you don't have a `/security-scan` skill yet

The simplest no-skill version is to just tell Claude Code:

> Download the source from <repo URL>. Scan its dependencies, shell usage, network behavior, and credential handling for security concerns. Rate findings CRITICAL / HIGH / MEDIUM / LOW. Conclude with "install recommended / not recommended / conditional install."

That prompt gets you about 80% of the `/security-scan` experience. After running it a few times you can package the pattern into a skill.

## Why I'm writing this

The MCP server count has exploded in the past few months. Twinkle Hub, mcp-taiwan-legal-db, all kinds of small tools written by Reddit folks—new recommendations every day.

If you accept them all, your Claude Code's installed MCP servers will climb to 20-30 within three months. Some might be malicious (e.g. typosquatting: `mcp-anthrop1c` impersonating the official `mcp-anthropic`). Some might just be poorly written and log your API key to an external service.

**Installing an MCP isn't free.** The cost is your machine's attack surface. Every install adds a unit of trust debt.

`/security-scan` is the lowest-cost tool for paying down that debt.
