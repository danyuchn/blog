---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T16:00:00Z
title: "兩個 HTML / PDF 渲染陷阱：Chrome print margin 和 qlmanage 的 1 張縮圖"
slug: zh/html-pdf-rendering-traps
featured: false
draft: false
tags:
  - developer-experience
  - productivity
description: 這禮拜寫了客戶提案的 HTML→PDF 和內部報告的 PDF→圖逐頁拆分，兩個流程都有一個看似無解的陷阱。解法都是一行事情，但找到那一行花了我一小時。
---

這禮拜做客戶提案的 HTML → PDF 匯出，還有內部報告的 PDF → 圖逐頁拆分，兩個流程都踩到一個看似無解的陷阱。解法都是一行事情，但找到那一行花了我不少時間。留下來備忘。

## 陷阱一：HTML → PDF 空白頁 + 白框

**症狀**：用 Chrome headless 把一份 HTML 轉成 PDF 之後，每一頁之間都多出一頁完全空白的頁面，然後每一頁的四周還有奇怪的白邊。

**我嘗試過**：

- `--no-margins` flag：有時候生效有時候不生效，不穩定
- 把 CSS 的 margin 全部設 0：沒用
- 調整 `.page` div 的 min-height：越調越糟

**根因**：Chrome 印 PDF 預設會套上一個 `~12mm` 的 print margin，這個 margin 不受 CSS body margin 控制，只受 `@page` 規則控制。

我的 HTML 有一個 `.page` div 用 `min-height: 297mm` 模擬 A4 高度。Chrome 的預設 print margin 把可用高度切掉了，於是 297mm 的 div 溢出成兩頁，中間那一頁就是空白。白框就是 print margin 本身。

**解法**：在 CSS 最上面加這一段：

```css
@page {
  margin: 0;
  size: A4;
}
```

`@page` 是專門給列印媒介用的 at-rule。Chrome headless 印 PDF 的時候會讀它，設 margin: 0 才能完全掌控版面。加上 `size: A4` 告訴它紙張尺寸。

加完這段後空白頁消失、白框消失。比用 `--no-margins` flag 穩定太多。

## 陷阱二：qlmanage 只給你一張縮圖

**症狀**：想把一個多頁 PDF 每一頁轉成 PNG，方便內嵌 Obsidian 或是拿去做影片素材。用 macOS 內建的 `qlmanage`，結果只得到一張縮圖。

```bash
qlmanage -t -s 150 file.pdf -o /tmp/
```

這個指令的 `-t` 是 thumbnail——它就是縮圖工具，無論你的 PDF 有 10 頁還是 100 頁，它只輸出第 1 頁。

**正確做法**：用 PyMuPDF（`fitz` module），逐頁 get_pixmap：

```python
import fitz  # pip install pymupdf

doc = fitz.open("file.pdf")
for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2))
    pix.save(f"/tmp/page_{i+1:02d}.png")
```

`fitz.Matrix(1.2, 1.2)` 是縮放倍數，1.2 大約對應 150 dpi，跟 qlmanage 的 `-s 150` 差不多。要更清楚就調 2.0（300 dpi）。

這個方法還有一個附加好處：你可以在同一支 script 裡 filter 要的頁數、加浮水印、或直接送到 OCR——qlmanage 給你的只是縮圖，後續什麼都做不了。

## 為什麼值得記下來

這兩個陷阱都是「工具 API 的預設行為跟你的 mental model 不一致」的典型例子。

Chrome 的 print margin 預設是 12mm 不是 0，因為瀏覽器的 PDF 功能本來是給網頁列印用的，不是給「生成精美 PDF 報告」用的。qlmanage 的 `-t` 叫 thumbnail 不叫 convert，因為 Quick Look 本來就是給 Finder 預覽用的，不是給批次處理用的。

工具的設計意圖決定了預設行為。一旦你把工具拿到非設計初衷的場景用，預設就是陷阱。

我把這兩條寫進了 `~/.claude/rules/common/tool-patterns.md`，下次不會再踩。
