---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-13T04:00:00Z
title: "My Pre-Trip Remote Checklist: Leaving the Mac Mini as Home Base"
slug: en/mac-mini-as-home-base-remote-checklist
featured: false
draft: false
tags:
  - claude-code
  - codex
  - remote-work
description: 'Eight things I checked before flying out, to keep a home Mac Mini reachable as the base for Claude and Codex: Tailscale, Herdr, caffeinate, auto-reboot, and remote file access.'
---

Tomorrow is my first trip abroad since I bought the Mac Mini. Here's the remote setup checklist I ran through before leaving:

1. Made sure Tailscale had every device on the tailnet connected and handshaking, with both Mosh and SSH getting through
2. Kept the Mac Mini awake with a caffeinate command so it never sleeps
3. Set up auto-reboot in case of an unexpected shutdown
4. Kept Herdr running persistently, configured in machine mode so other devices on the LAN can connect into the same herdr server
5. Set up Finder on the laptop and the Files app on my phone to reach the Mac Mini's folders over the LAN
6. Refreshed the Claude/Codex login tokens ahead of time
7. Made sure the laptop and phone I'm carrying both have a remote desktop app installed, so I can connect home in an emergency
8. Tried to teach my girlfriend, who's staying home, how to reboot the computer and the router if something goes wrong (??)

Tested it the next day: tailscale plus herdr connected me back to the codex running at home, no problems at all. Genuinely a fun experience.

The reason for all this trouble: I'm heading out on a long trip, and my laptop doesn't have the storage for it — the harness and the scheduled jobs all live on the Mac Mini at home.

Unlike the [five-step SOP I wrote for letting Claude Code run in the background from a hotel room before dinner](/blog/posts/en/ipad-workflow-robustness), that one was a short backup plan for stepping out for dinner while still in Taiwan; this time I'm leaving the whole country, and the Mac Mini has to hold up as home base for days.

<!--
List of added non-original sentences (fidelity disclosure):
1. "Unlike the [five-step SOP I wrote for letting Claude Code run in the background from a hotel room before dinner], that one was a short backup plan for stepping out for dinner while still in Taiwan; this time I'm leaving the whole country, and the Mac Mini has to hold up as home base for days." — Type: framing sentence (the one framing sentence explicitly authorized by the dispatch instructions, pointing out the difference from the existing article and linking to it)
-->
