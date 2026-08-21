---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: Eleven HyperFrames Video Gotchas
slug: en/hyperframes-video-gotchas
featured: false
draft: false
tags:
  - video-production
  - gotchas
  - automation
description: 'Transition flicker, a worker-parallelism myth carried over from another framework, transcript format drift, slide sizing, and silently truncated thumbnails — eleven things that bit me on the HyperFrames video line in one week of August.'
---

The April post, [Nine video production bugs I hit in April 2026](/blog/posts/en/video-production-gotchas-2026), was about the Remotion setup. [The whole pipeline later moved to HyperFrames](/blog/posts/en/ai-video-pipeline-codex-to-claude), and the gotchas got replaced along with it. Here are the ones I hit in one week of August while building a hybrid piece (animated overlays plus screen-recording pass-through), one per section.

## 1. Transition flicker means the cut point isn't covered by the mask

The wipe was scheduled at `B-0.6～B`, so the red curtain had already slid away 0.3 seconds before the cut. That cut was bare, and the frame flickered. The fix is to move the cut point inside the fully-masked window: enter at `B-0.35`, hold at `B±0.05`, exit at `B+0.35`. The 0.10-second hold is what guarantees at least three fully covered frames at 30fps. Looking back at an earlier episode, it inherited the same bad timing.

## 2. "Pure animation must use a single worker" is a Remotion rule, not a HyperFrames one

Carrying that rule over from Remotion makes renders five to eight times slower. I measured it: with 8 workers, adjacent-frame comparison on static animation gives a pixel difference of 0. To confirm the checker wasn't just broken, I ran it in reverse against moving transition frames, and it did catch differences. 59,000 frames finished in about 22 minutes.

## 3. `.term` / `.codefile` silently cut off the last line

Both are flex children, so `scene-content` squeezes them, and with `overflow: hidden` on top the last line just gets eaten. On screen it only looks like the text is sitting flush against the bottom. Setting `flex-shrink: 0` fixes it, and once that's in, the scenes that are genuinely overfull start showing up. Also, `hyperframes check` only samples 9 frames, so it isn't guaranteed to catch this. Use `hyperframes snapshot --zoom "<selector>"` to blow up the element itself and check.

## 4. Don't make big edits while preview is running

While `hyperframes preview` is running it keeps injecting `data-hf-id` attributes into `index.html`, and your Edit old_string stops matching. Run `hyperframes preview --stop` before any large edit.

## 5. A render failure filter can't just grep for `error`

HyperFrames prints a log line that reads `static-frame dedup: disabled (... this is the safe fallback, not an error)`. Grepping for `error` reports it as a failure. The filter has to exclude lines containing `not an error`.

## 6. Chunked transcription output drifts in format between chunks

Out of 13 chunks, 5 came out as `**[MM:SS] Name**：` and the rest as `[MM:SS] **Name**：`. A regex that only recognizes one of those shapes made those 5 chunks silently return 0 lines. The merged result looked complete but was missing 40% of the content. Use a looser regex when merging (allow the leading `**`), and print the line count per chunk to check. A chunk returning 0 lines means the format didn't match, not that the chunk was empty.

## 7. exit 0 on a large download doesn't mean the file is complete

A 938MB recording hit a read timeout at 971MB and the command still exited 0. The symptom only surfaced at `ffprobe`: `moov atom not found`. The acceptance condition for a large download is that ffprobe can read a duration, not the exit code and not the file existing. Retry loops should treat ffprobe as the success test.

## 8. The official slideshow framework's present mode isn't usable right now

Its `present` is flagged by the project itself as a temporary workaround, and it requires the composition to expose a single `window.__timelines.root`. In practice all 25 slides failed to parse and the player sat on loading. I ended up borrowing only its visual language and its progressive-reveal pacing, and wrote the controller myself in 60 lines with no framework dependency.

## 9. Verify slide layout at the real projection size, not your current browser window

agent-browser defaults to a 577px-tall window, which measured 10 pages as overflowing. Switching to `style.height="720px"` to simulate 16:9 left 6, and it only got to zero after I dialed the type size down and measured again. Judge by the default window and you end up shrinking the layout far more than you need to. The type scale in `slides-tokens.css` is designed for 1080p, so a 1280×720 projection needs a proportional override.

## 10. Studio showing "Uploading 0%" doesn't mean the upload is stuck

The thing to check is whether the API's `uploadStatus` and `fileDetails.fileSize` match the local byte count. Don't go by the UI. This time 499MB went through resumable upload on the first try, which also killed the old note about a "257MB fails" threshold. That was a limit of the old chunked path.

## 11. Thumbnail titles were being silently truncated

`compactTitle()` strips punctuation, keeps only the first 22 characters, and then hard-splits into two lines at the midpoint. The result was half-sentences sitting on YouTube for months. 36 of them. Nobody noticed. I replaced it with hand-written short titles (a missing entry now fails the build outright), switched the type fitting to each template's real container width, added `word-break: keep-all` on the subtitle, and added `npm run lint:thumbnails` as a permanent gate. The rule: any automation that discards user content has to be changed to shrink or error out when things don't fit. No silent dropping of characters.

That's the week.
