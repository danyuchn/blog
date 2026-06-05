---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "The Day Opus 4.8 Went Haywire: tool call cannot be parsed"
slug: en/opus-48-tool-call-parse-bug
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - developer-experience
description: 'A one-day timeline from 2026-06-02: from hopping on X for moral support, to someone finally pinning down the root cause of tool call cannot be parsed.'
---

Every time Claude breaks, I hop on X. Over there, I feel like I'm not alone (some kind of huddling-together-for-warmth mentality).

I feel like today is the perfect time to ship GPT-5.6. OpenAI was right to hold back last week.

Because Claude is going haywire across the board. This is the "kick a man while he's down" moment!

New trick today: tool call cannot be parsed (retry also failed).

Someone found the root cause of Opus 4.8 thinking past the timeout and ending up returning tool call could not be parsed: the thinking block returns an abnormal empty output, and tool_use has no proper tool-call block. The diagnosis is that the extended thinking mechanism is misbehaving.

The fixes:

1. Turn Opus 4.8 effort down below high, and there won't be any thinking tokens — but the capability drops accordingly.

2. Falling back to 4.6 + max works best.
