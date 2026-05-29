---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T04:00:00Z
title: "Leveling Up the iPad Workflow — Surviving Internet and Power Outages, and Why I Ditched the Magic Keyboard"
slug: en/ipad-workflow-robustness
featured: false
draft: false
tags:
  - claude-code
  - remote-work
  - ipad
description: 'A follow-up to the full iPad-runs-Claude-Code guide. This one is not about setup, it is about robustness: home internet in Bangkok drops, the rainy season kills the power, so how does the host machine survive? Plus why I gave up the Magic Keyboard for my mouth and some gestures.'
---

The last post covered the basic trio for running Claude Code on an iPad: tmux + Tailscale + Moshi. That one was about how to set it up. This one is about how to keep it from dying right when you need it most.

I keep a MacBook Air and a Mac mini at home as 24-hour headless hosts. When I head out I only carry an iPhone and an iPad, and I remote back in to run Claude Code and Codex. The catch: I'm in Bangkok, where the home internet drops once every month or two, and the rainy season occasionally cuts the power. So getting it installed isn't enough. You need a fallback plan for outages.

Three parts: connection infrastructure, host-side robustness, and the iPad input strategy. The basic tmux / Tailscale / Moshi install was covered last time, so I won't repeat it.

## Connection Infrastructure

For the connection layer I run Tailscale with the MOSH protocol. It's secure, hard to drop, and the key point is it doesn't need to reconnect when the network switches — walk out the door, go from home wifi to cellular, and the session is still alive.

For the terminal app I switched from Termius to Moshi. Moshi was natively designed for AI agent CLIs, and it doesn't break the rendering of CJK block characters. In my testing, Termius's CJK rendering has a bug — Chinese characters get garbled.

Backup plan: Chrome Remote Desktop or AnyDesk. An SSH terminal handles 90% of what I do, but occasionally you need to look at something outside the terminal — some GUI app, some image. That's when remote desktop fills the gap. It's not the main act, it's the spare tire.

## Host-Side Robustness

This part is the core of the outage plan, because when you're out and the host goes down, you can't reconnect — you just sit there staring.

- **Schedule the router to reboot.** Leave a router running for too long and it overloads and drops. Just have it restart itself once a day.
- **Set the Mac mini to auto-restart after a power loss.** When the rainy-season blackout ends and power comes back, the host revives itself — no waiting for me to get home and hit the power button.
- **Use wired ethernet.** Wifi is flaky; if you can run a cable, run it. One fewer variable.
- **A smart plug with its own cellular connection.** This is the lifesaver when the net drops — even with the home internet down, I can send a text message to cut and restore power to the plug, hard-rebooting the host. It doesn't rely on home internet, it rides the cellular signal.
- **Plug in a dummy HDMI dongle.** When I leave and turn off the monitor, the system still thinks a display is attached and keeps a virtual desktop alive, so the screen looks normal when I remote in.

Two more small settings: stop the machine from sleeping — I keep it up with the `caffeinate` command — and give tmux full disk access, or it can't read some paths.

## The iPad Input Strategy

I took a detour on this one.

At first I bought the Magic Keyboard case. Painful experience: it wears out easily, the metal connector oxidizes and rusts, and it is heavy as hell. Heavy enough to completely kill the iPad's mobility advantage — the whole point was to travel light, and instead I was lugging a slab of metal around. I eventually pulled it off and switched to a plain stand-style cover.

If I genuinely need to type, I now carry a Mac Magic Keyboard (Bluetooth) plus a Magic Mouse. The two together weigh just over 200 grams — far lighter than the Magic Keyboard case — and the same set works on the Mac at home and pairs with the iPad on the road. Two uses, one purchase.

But honestly, I later found I rarely even need that set. Most of what I run isn't coding — issue a command with my mouth, swipe with a finger, watch the result with my eyes, and that's enough. I'm not the kind of person who hand-types code anyway, so going without a mouse turns out to be fine. Voice input plus touch gestures hold up surprisingly well for daily work.

A note on hardware: I'm using a 2018 iPad Pro. Eight years old and it still runs the remote session smoothly. Remoting doesn't tax local resources anyway — all the compute is on the host at home, and the iPad is just a screen and a mouth. So I scrapped the plan to buy a new one. Money saved.

Finally, two handy little things: there's a small button in the top-right corner that shows the diff directly, and another button that previews localhost. Add a fileviewer extension and the iPad turns into a file manager — documents, images, videos, all openable.
