---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-20T13:31:00Z
title: "The Wall That Was On by Default: Codex Sandbox, ENV_SCRUB, Vercel Protection, Official Connectors"
slug: en/default-guardrails-that-block-you
featured: false
draft: false
tags:
  - developer-experience
  - security
  - gotchas
description: 'An office NAS that won''t mount, AUTOMODE that won''t come back, outside visitors getting a 401, a cloud schedule that can''t send mail. None of them were bugs in my code; each was a protection switched on by default.'
---

What these traps have in common: the thing blocking you isn't a bug in your code, it's some protection that was on by default.

## Codex's sandbox

I was on site at a client's office running a Codex training, and the company's internal NAS mount just would not read. After every check had failed and I was getting desperate, it hit me: is the Codex sandbox doing this? Sure enough, once I verbally authorized it to try outside the sandbox, it read fine.

## Turn on ENV_SCRUB and AUTOMODE won't come back

Trivia: if `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` (the env-stripping setting is on), AUTOMODE can't become the default. The default will be manual.

## Vercel throwaway public pages

A fresh project's deploy URL ships with Deployment Protection (Vercel Authentication) on by default, so outside visitors get a 401. The other trap: the bare `<proj>.vercel.app` alias may be someone else's empty shell; your auto-updating prod alias is `<proj>-<team>.vercel.app`. curl and check the content before sending anyone the link.

## The cloud only accepts official connectors

Several of my clients were stuck wanting a cloud schedule that mails them a daily market brief or writes to a Google Sheet. Cloud servers only accept the official connector, and until now the most you could do was save a draft or create a brand-new file in Drive. The official MCP now sends mail and updates existing files.
