---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T03:30:00Z
title: "Love-Hate With Anthropic — Sneering at the Elitism While Devouring Their Engineering Blog"
slug: en/anthropic-love-hate
featured: false
draft: false
tags:
  - claude-code
  - opinion
  - ai-trends
description: 'I have a love-hate thing with Anthropic: I hate the smug elitism and the black-box token-burning, but their engineering blog is some of the best out there, especially the security and permissions stuff.'
---

Trust me, Claude has a hundred ways lined up for you to burn tokens in style, and a hundred excuses lined up to pin the burning on you, the user.

## A hundred ways to burn tokens in style

You can keep using the same session forever and never compact it. You can leave more than an hour between messages. You can talk to it in Hindi or Korean. You can ask it to spin up as many subagents as possible, the more the merrier. You can write every doc in HTML instead of Markdown.

Stack all of these and the token bill gets serious. But the official line is always the same: it's how you use it, not us.

## Those flex quotes

Anthropic has two fairly famous people. One I just call "the bald guy," the other is Thariq. Listening to these two, basically every sentence sounds like a flex.

"I only use Opus." "I run a dozen sessions at a time." "Each session has a bunch of subagents hanging off it." And the other one: "Bye-bye Markdown, hello HTML, HTML isn't more token-heavy." "The limits only affect under 10% of people." "Don't overthink the double usage, a gift is just a gift."

There was a source code leak a while back, and people found that Anthropic's internal employee accounts have a special flag. Turns out they're the privileged class. No wonder they talk so breezily.

## But I still read their engineering blog every day

After all that sneering, I have to be honest: it's a love-hate thing with Anthropic.

What I hate is the smug elitism, plus the black-box maneuvering dressed up as "educating the user." What I love is the technical writing they share. Among all the big model vendors, their engineering blog is some of the highest quality out there, and it works for everyone — outsiders can follow it, insiders can still spot the craft underneath.

I especially love the pieces on security and permissions.

## Why security

This goes back to when I was sitting at the peak of the Dunning-Kruger curve. Back then I was happily vibe coding and felt unstoppable. I had a friend who works in security, and he kept dropping these valuable reminders on me. Slowly it sank in: risk is positively correlated with functionality and convenience. The more convenient and open it is, the bigger the holes.

Later I accidentally leaked a key, took a financial hit, and only then did I start seriously revisiting all those lessons I'd been warned about, and actually take security and permissions seriously.

So these days what I read regularly is roughly: the official Claude blog, the official Claude Code docs, the system cards from every model release, and Thariq's posts on X.

## A fascinating spot to be wedged in

Read enough of it and you realize it's a fascinating world.

Anthropic is stuck between two forces. On one side, models that have a real chance of going off the rails and are hard to interpret. On the other, humans who are review-fatigued and prone to laziness. They have to use cold, rational logic to design a whole harness to control the model's behavior, while also fighting human inertia — and a lot of those humans are new users with no real training.

Those two-front design trade-offs are spelled out clearly across their technical posts. You can see how they weigh things, where they compromise, how they tug between safe and usable.

I'll keep ragging on the elitism. But the engineering blog, I genuinely recommend reading more of it. There's something to gain on every page.
