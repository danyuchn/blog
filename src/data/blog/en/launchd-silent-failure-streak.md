---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "Eight Days of Silent Failure: launchd Fired on Schedule, Nothing Happened"
slug: en/launchd-silent-failure-streak
featured: false
draft: false
tags:
  - ai-workflow
  - developer-experience
  - case-study
description: 'A local pipeline that auto-publishes a video every day at 09:00 failed for eight straight days. launchd fired on schedule, zero alerts. Notes from tracing a path desync down to exit 127.'
---

I have a local `cc-update-pipeline` that launchd triggers every morning at 09:00. It generates a "CC update digest" YouTube Short and uploads it.

It did nothing for eight days straight, and I had no idea.

## The streak

From 5/26 to 6/2. No alert. No error notification. I assumed shorts were still going out, until one day it hit me: over those eight days, not a single one had been published.

The weird part is the gap I'd been ignoring — the gap between "fired" and "ran." launchd really did do its thing. But the script that was supposed to run after that never got off the ground.

## Diagnosis

First I checked `launchctl list | grep <label>` to look at the job's exit code. It was 127.

127 is what bash returns when it can't find the file it's supposed to execute. So every morning at 09:00, launchd dutifully knocked on that script — except it was knocking on a file that no longer existed at that path. It knocked on thin air, quietly logged an exit 127, and waited for tomorrow to knock again.

## Root cause

The root cause traces back to 5/26. That day I moved the upload script under `tools/`, but the `ProgramArguments` path in the launchd plist still pointed at the old location. The script moved, the plist didn't follow — so the schedule fired as usual, bash couldn't find the file, silent exit 127.

And it wasn't just that one layer that came unstuck. After moving the upload script, I also forgot to update the path referenced in `pipeline.sh`, plus the upload script's own `PROMO_DIR` — because `Path(__file__).parent` shifted when the file moved, so the directory it derived relative to itself was off too.

On top of that, some of those days had no log entry at all. The most likely explanation is the computer was asleep, so launchd didn't even fire on those days. So the eight-day streak was actually two kinds of silence mixed together: some days it knocked on air and exited 127, some days the machine was asleep and it never knocked at all.

## Fix

The fix was straightforward: change the path in the plist to the new location, reload. The exit code went from 127 back to 0. I also patched the path in `pipeline.sh` and the upload script's `PROMO_DIR`.

I didn't backfill v2.1.151 through 161 from the 5/26–6/2 window — I let those shorts stay gone. Starting at 09:00 that day, the pipeline picked up from the latest version and carried on.

Once the paths were fixed and I went to re-render, I hit a second landmine: the Remotion composition ID. The pipeline fed in `${TODAY}` (2026-06-04), but Root.tsx had registered `${DATE_COMPACT}` (20260604). The two names didn't match, and the render crashed outright. Once I made them consistent, v2.1.161 re-rendered and uploaded to YouTube, and the schedule was finally alive again.

## One last thing

Eight days of failure, and not a single line of red text saved me. Nothing looked off on the launchd side. The YouTube backend showed no failed jobs, because no job ever reached it. The cheapest place to catch all of this was that one `launchctl list | grep <label>` to glance at the exit code — I just didn't look for eight days.
</content>
