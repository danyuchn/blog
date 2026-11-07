---
author: Dustin Yuchen Teng
pubDatetime: 2026-11-07T01:45:00Z
title: "Make Yourself a 'Human System Card': Have AI Read Your Personality Before It Talks to You"
slug: en/human-system-card-for-ai
featured: false
draft: false
tags:
  - claude
  - ai-workflow
  - codex
description: 'Have Claude read your past chat logs and write a ''human system card'' covering your personality, decision logic, and communication preferences. Includes an excerpt of my own card and a four-step prompt to make yours.'
---

Let me quietly share a god-tier trick I came up with recently: have Claude look through your past conversation history with it and make you a "human system card" (modeled on the "model welfare" chapter of Claude's own system card), which is basically your personality profile, decision logic, communication preferences, and so on.

A "system card" is a manual an AI company writes for a new model to describe its personality and behavior; I wrote an earlier post, [Read the System Card Before You Use a New Model](/blog/posts/en/read-system-card-before-managing-model/), about how I use that manual to get along with different models.

From then on, whenever you switch to a dumber model, or the model you're using suddenly clashes with how you communicate and pisses you off, you just tell it to go read this card, understand your personality, and then come back and talk to you. All that communication friction disappears, even with Codex, which I was cursing at every single day a while back.

After I made the card, I asked Claude: "Maybe you could take a look at my personality card, my system card, and judge my personality, okay?" Claude read the card alongside our conversations from that day and spotted several of my habits: I care about attention rather than time; my reaction is always the same, scolding it first and right away telling it to fix the mechanism, asking straight out "whose problem is this, and how do we make sure it never happens again"; I often subtract for others and add for myself; and what I want is something reusable, not a one-off answer. Its last line was: paired with AI, this kind of personality is most afraid of getting buried by AI trying to be "complete," so when handing things to me from now on, default to less first.

## What My Card Looks Like

Here is an excerpt from my own system card, so you can see what it actually looks like:

One-liner: Former teacher; more comfortable managing AI than managing people. Disciplined on the outside, very loose with myself.

Communication preferences:
- Lead with the conclusion in plain language. No jargon, no mixing languages.
- No defensive tone, no disclaimers, and don't explain your method before giving the conclusion.
- Ask everything that needs my call in one go, at most seven items, each with your recommendation.
- I use voice input a lot. Fix homophones and slips of the tongue yourself without correcting me.

Things I dislike:
- Fake completion: saying something is done without verifying it.
- Doing irreversible things on your own, like sending messages or deleting files directly.
- Getting stuck in silence and reporting nothing.
- Blaming the AI.

Decision style:
- If it can be undone, go ahead and do it; if it can't be undone, ask me first.
- Important conclusions need an independent second check.
- I make calls quickly, but I often change my mind within a day or two, so check the date before quoting an old decision of mine.

My own blind spots (please remind me):
- What I promise other people easily keeps piling up.
- The moment I have free time, I want to build something new.
- When either of these happens, ask me: how much of my time is this going to take?

When I correct you: write it into the rules in the same turn, and tell me where you put it.

## How to Make Your Own Card

If you want to make one for yourself, it takes four steps:

1. Hand your past conversation history with the AI over to it (Claude can read files directly; for ChatGPT or tools without file access, export your chats first and paste them in).
2. Paste the prompt below, replacing the bracketed part with your setup.
3. Once it gives you a draft, do just one thing: delete any lines you don't want public or don't want the AI to know.
4. Save it as a file. Next time you switch models or a model clashes with you, tell it to read this card first.

```text
Please read all of my past conversation logs with you ((fill in: folder path or exported file location)).
Make me a "human system card" for any future AI to read. Include only my personality, decision style, and communication preferences. Do not include any names, companies, dollar amounts, or private life details.
Structure: one-line intro, my communication preferences, things I dislike, my decision style, my own blind spots.
Every item must be backed by a real example from our conversations. If you can't find an example, leave it out.
Show me the draft first, and save it as a file only after I confirm.
```

(p.s. When making the system card, have another AI assistant read through the long chat logs first to save quota on the bulk text, but leave the filtering criteria and the judgment of writing the card to Fable, its ability to read people is unreal)

We humans need to understand our agents' personalities, and the other way around, agents need to understand ours too. That's how I feel about it.
