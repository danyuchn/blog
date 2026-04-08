---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T16:00:00Z
title: "Two HTML/PDF Rendering Traps: Chrome Print Margin and qlmanage's Single-Page Problem"
slug: en/html-pdf-rendering-traps
featured: false
draft: false
tags:
  - developer-experience
  - productivity
description: This week I exported a client proposal as HTML→PDF and split an internal report from PDF→images page by page. Both flows had a seemingly unsolvable trap. Each fix is one line of code, but tracking down that line cost me real time.
---

This week I exported a client proposal as HTML→PDF and split an internal report from PDF→images page by page. Both workflows had a trap that looked impossible at first. The fixes are one-liners, but tracking them down took real time. Writing them down so I don't forget.

## Trap 1: Blank Pages and White Borders in HTML→PDF

**Symptom**: Using Chrome headless to convert an HTML file to PDF, every real page had a blank page between it and the next, plus strange white borders around every page.

**Things I tried**:

- `--no-margins` flag: works sometimes, doesn't others. Unreliable.
- Setting CSS body margin to 0: no effect.
- Tweaking `.page` div's `min-height`: made it worse.

**Root cause**: Chrome's default print margin (`~12mm`) is not controlled by CSS body margin. It's only controlled by the `@page` rule.

My HTML had a `.page` div with `min-height: 297mm` simulating A4 height. Chrome's default print margin cut into the usable height, so a 297mm div overflowed into two pages, and the blank page was the overflow. The white borders were the print margin itself.

**Fix**: Add this at the top of your CSS:

```css
@page {
  margin: 0;
  size: A4;
}
```

`@page` is a print-media at-rule. Chrome headless reads it when printing to PDF, and setting `margin: 0` is the only way to fully control the layout. Adding `size: A4` explicitly tells it the paper size.

After this, blank pages gone, white borders gone. Far more reliable than `--no-margins`.

## Trap 2: qlmanage Only Gives You One Thumbnail

**Symptom**: You want to convert a multi-page PDF to PNGs page by page, for embedding into Obsidian or using as video assets. You try macOS's built-in `qlmanage`. It only gives you one thumbnail.

```bash
qlmanage -t -s 150 file.pdf -o /tmp/
```

The `-t` flag means "thumbnail"—it is literally a thumbnail tool. Whether your PDF has 10 pages or 100, it only outputs page 1.

**Correct approach**: Use PyMuPDF (`fitz` module), iterate through pages, and call get_pixmap:

```python
import fitz  # pip install pymupdf

doc = fitz.open("file.pdf")
for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2))
    pix.save(f"/tmp/page_{i+1:02d}.png")
```

`fitz.Matrix(1.2, 1.2)` is a scaling factor—1.2 is roughly 150 dpi, comparable to qlmanage's `-s 150`. Bump it to 2.0 for 300 dpi if you need sharper output.

This approach also has a bonus: you can filter pages in the same script, add watermarks, or pipe directly into OCR. qlmanage hands you a thumbnail and nothing more—you can't build anything else around it.

## Why These Are Worth Writing Down

Both traps are classic cases of "tool default behavior doesn't match your mental model."

Chrome's print margin defaults to 12mm, not 0, because the browser's PDF function was designed for printing web pages, not for "generating polished PDF reports." qlmanage's `-t` means thumbnail, not convert, because Quick Look was designed for Finder previews, not batch processing.

The design intent of a tool determines its defaults. As soon as you push a tool into a use case outside its original intent, defaults become traps.

I added both of these to `~/.claude/rules/common/tool-patterns.md`. I won't fall into them again.
