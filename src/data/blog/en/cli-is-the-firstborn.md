---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: The CLI Is the Firstborn
slug: en/cli-is-the-firstborn
featured: false
draft: false
tags:
  - claude-code
  - anthropic
  - developer-experience
description: 'New features and fresh bug fixes land in the CLI first. Remote control waits forever. Same company, wildly different update cadence.'
---

New features and freshly fixed bugs all land in the CLI first, so the CLI is the native, first-class environment. Remote control? You'll be waiting until the cows come home for an update.

Uh, let me give an example. In the early days of the remote control environment, typing a slash didn't bring up the SKILL menu, so unless you remembered a skill's full name, you couldn't call it. That only got fixed three months after remote control shipped.

They're all Anthropic-native, but parents play favorites even among their own kids. The CLI updates most often, roughly daily (because the staff use it themselves). Desktop used to be slow, then the big revamp came and updates picked up. Everything else just crawls. Search the CHANGELOG for remote control and you'll see how often anything related to it gets fixed.

So if you're already used to the CLI on your machine at home, isn't mirroring that CLI straight to a mobile device the most convenient thing?

![A phone connected back to a Mac mini over mosh, running the CLI; on screen is an agent writing up a batch of gog CLI gotchas into a doc](/blog/assets/posts/cli-is-the-firstborn/1-remote-control.jpg)

Why not use the official Claude / Codex cloud control apps on the phone?

Because who knows when they'll ever ship split pane...

![A phone screen with two panes stacked top and bottom, each one a separate CLI session](/blog/assets/posts/cli-is-the-firstborn/2-no-split-pane.jpg)

And here's another odd thing. The Claude Code CLI, which used to update daily, has now gone 8 days without an update. Issues are still holding steady around five thousand even after the bot's aggressive deduping, so it's not like there are no bugs left to fix.

![The GitHub page for the anthropics/claude-code repo, Issues showing 5k+, the latest commit tagged v2.1.220 and marked committed last week](/blog/assets/posts/cli-is-the-firstborn/3-cli-no-update.jpg)

Are they sitting on something big, or did something drastic shift internally? No idea at this point.

Quite a gap from the AI self-healing workflow they were promoting so hard. With this company, what they say and what they do are two separate accounts.

<!--
Added non-original sentences (faithfulness disclosure):
1. "And here's another odd thing." — type: connective (original was a standalone post opening "A very odd thing:"; "another" added to link to the preceding paragraph)
2. Alt text on all three images — type: connective (written from the image descriptions supplied by the main thread, not the author's words)
3. Title "The CLI Is the Firstborn" and description — type: framing (derived from the author's "even your own kids get treated unevenly" and the opening post)
All other body sentences are verbatim from the original posts, with only punctuation adjustments.
-->
