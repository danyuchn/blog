---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-13T04:00:00Z
modDatetime: 2026-10-02T01:00:00Z
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

## Postscript: Field Results and Pitfalls After Leaving

Test numbers from a random hotel Wi-Fi in Taiwan, connecting straight through Tailscale to the host in Bangkok: no noticeable lag in actual use. After checking from both Hanoi and Taipei, I'm confident that keeping the Mac mini at home in Bangkok and reaching it over mosh/ssh plus the Tailscale network is the stable, correct call. Extra data point: a Louisa Coffee in Taipei started out routed through a Hong Kong relay, then went direct after 1-2 minutes, with round-trip latency of 87-92 ms, about 89 ms on average.

The remote rehearsal before leaving also turned up a few pitfalls, all of which went into the runbook:

- The Mac mini has FileVault on: a power cut, an automatic update, or `sudo reboot` leaves it stuck at the disk-unlock screen, and Tailscale, SSH, and AnyDesk all go dark. The only safe remote restart is `sudo fdesetup authrestart`, which lands at the login screen, where you log in through AnyDesk, and AnyDesk takes a minute or two before it will connect.
- After a restart, SSH sessions can't read the login keychain (`User interaction is not allowed`): git push asks for credentials, the gh token shows as invalid, and Claude Code wants a fresh /login. Running `security unlock-keychain` from my phone brought all three back, so it's now a required step after every restart.
- Remote typing from the laptop was laggy, and the mini's Wi-Fi showed a latency spike of about 0.4 seconds every second. Turning off AirDrop and Handoff on the mini dropped the average from 130ms to 3.6ms on the spot.
- Over SSH I couldn't read Desktop, Documents, or Downloads until I turned on "Remote Login → Allow full disk access for remote users."

<!--
2026-10-02 W41 postscript: one new section. The first paragraph merges two Threads posts (09-30 21:33 and 10-01 12:29); the list is trimmed from the author's 09-28 work-log pitfalls (internal addresses removed). Added non-original sentences: the subheading (framing) and "The remote rehearsal before leaving also turned up a few pitfalls, all of which went into the runbook:" (connective).
-->

<!--
List of added non-original sentences (fidelity disclosure):
1. "Unlike the [five-step SOP I wrote for letting Claude Code run in the background from a hotel room before dinner], that one was a short backup plan for stepping out for dinner while still in Taiwan; this time I'm leaving the whole country, and the Mac Mini has to hold up as home base for days." — Type: framing sentence (the one framing sentence explicitly authorized by the dispatch instructions, pointing out the difference from the existing article and linking to it)
-->
