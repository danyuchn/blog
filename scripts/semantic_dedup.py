#!/usr/bin/env python3
"""Semantic near-duplicate finder for the blog.

Embeds every article (and optionally each micro-note entry) with Google's
``gemini-embedding-2`` model, then reports the most semantically similar
pairs so they can be reviewed for merging / deduplication.

Why this exists: as the weekly roundups pile up, articles and micro-notes
drift toward overlapping themes. Keyword search misses paraphrased overlap;
embeddings catch it.

Usage:
    export GEMINI_API_KEY=...        # blog/.env key was expired (2026-05-30);
                                     # use a working key from another project
    uv run scripts/semantic_dedup.py                 # articles only
    uv run scripts/semantic_dedup.py --micro          # also split micro-notes
    uv run scripts/semantic_dedup.py --threshold 0.82 --top 40

Notes:
- Same-filename zh/en pairs are translations, not duplicates, and are
  excluded by default (use --keep-translations to see them).
- Concurrency defaults high (the API tolerates large fan-out); lower it with
  --concurrency if you hit rate limits (HTTP 429).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

MODEL = "gemini-embedding-2"
ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/"
    f"models/{MODEL}:embedContent"
)
BLOG_ROOT = Path(__file__).resolve().parent.parent
ZH_DIR = BLOG_ROOT / "src" / "data" / "blog" / "zh"
EN_DIR = BLOG_ROOT / "src" / "data" / "blog" / "en"
# A fixed output dimensionality keeps vectors comparable across runs.
OUTPUT_DIM = 1536


@dataclass
class Unit:
    """A piece of content to embed and compare."""

    uid: str           # stable id, e.g. "zh/foo" or "zh/ai-micro-notes#3"
    lang: str          # "zh" | "en"
    base: str          # filename stem, used to spot translation pairs
    title: str
    text: str
    vec: list[float] = field(default_factory=list)


def strip_frontmatter(raw: str) -> tuple[dict, str]:
    """Return (frontmatter-ish dict, body). Only `title` is parsed."""
    fm: dict = {}
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            block = raw[3:end]
            body = raw[end + 4 :]
            m = re.search(r'^title:\s*"?(.*?)"?\s*$', block, re.MULTILINE)
            if m:
                fm["title"] = m.group(1)
    return fm, body


def split_micro_entries(base: str, lang: str, body: str) -> list[Unit]:
    """Split a micro-notes file into one Unit per `**bold title**` entry."""
    units: list[Unit] = []
    # Entries look like:  **Title**\n> body...   (until next ** or ## or EOF)
    pattern = re.compile(r"^\*\*(.+?)\*\*\s*\n((?:(?!^\*\*|^## ).*\n?)*)", re.MULTILINE)
    for i, m in enumerate(pattern.finditer(body)):
        title = m.group(1).strip()
        content = re.sub(r"^>\s?", "", m.group(2), flags=re.MULTILINE).strip()
        if not content:
            continue
        units.append(
            Unit(
                uid=f"{lang}/{base}#{i}",
                lang=lang,
                base=f"{base}#{title}",  # micro entries never pair as translations here
                title=title,
                text=f"{title}\n{content}",
            )
        )
    return units


def collect_units(include_micro: bool) -> list[Unit]:
    units: list[Unit] = []
    for lang, d in (("zh", ZH_DIR), ("en", EN_DIR)):
        for path in sorted(d.glob("*.md")):
            base = path.stem
            raw = path.read_text(encoding="utf-8")
            fm, body = strip_frontmatter(raw)
            is_micro = base.startswith("ai-micro-notes")
            if is_micro:
                if include_micro:
                    units.extend(split_micro_entries(base, lang, body))
                continue
            title = fm.get("title", base)
            # Collapse whitespace; keep it lightweight for the embedder.
            text = re.sub(r"\s+", " ", f"{title}\n{body}").strip()
            units.append(Unit(uid=f"{lang}/{base}", lang=lang, base=base, title=title, text=text))
    return units


def embed(text: str, api_key: str) -> list[float]:
    payload = {
        "model": f"models/{MODEL}",
        "content": {"parts": [{"text": text[:20000]}]},
        "outputDimensionality": OUTPUT_DIM,
    }
    req = urllib.request.Request(
        f"{ENDPOINT}?key={api_key}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    return data["embedding"]["values"]


def normalize(v: list[float]) -> list[float]:
    s = sum(x * x for x in v) ** 0.5
    return [x / s for x in v] if s else v


def cosine(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--threshold", type=float, default=0.80, help="min cosine to report")
    ap.add_argument("--top", type=int, default=50, help="max pairs to print")
    ap.add_argument("--concurrency", type=int, default=256, help="parallel embed calls")
    ap.add_argument("--micro", action="store_true", help="also split micro-notes into entries")
    ap.add_argument("--keep-translations", action="store_true", help="don't hide zh/en same-file pairs")
    ap.add_argument("--cross-lang", action="store_true", help="compare across languages too")
    ap.add_argument("--json", type=Path, default=None, help="also write pairs to this JSON file")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: set GEMINI_API_KEY (the blog/.env key is expired).", file=sys.stderr)
        return 2

    units = collect_units(args.micro)
    print(f"Embedding {len(units)} units with {MODEL} (dim={OUTPUT_DIM})…", file=sys.stderr)

    def work(u: Unit) -> Unit:
        u.vec = normalize(embed(u.text, api_key))
        return u

    done = 0
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = {ex.submit(work, u): u for u in units}
        for fut in as_completed(futs):
            u = futs[fut]
            try:
                fut.result()
            except urllib.error.HTTPError as e:
                print(f"  ! {u.uid}: HTTP {e.code} {e.read()[:120]!r}", file=sys.stderr)
            except Exception as e:  # noqa: BLE001
                print(f"  ! {u.uid}: {e}", file=sys.stderr)
            done += 1
            if done % 25 == 0:
                print(f"  …{done}/{len(units)}", file=sys.stderr)

    units = [u for u in units if u.vec]
    pairs = []
    for i in range(len(units)):
        for j in range(i + 1, len(units)):
            a, b = units[i], units[j]
            if not args.cross_lang and a.lang != b.lang:
                continue
            if not args.keep_translations and a.base == b.base and a.lang != b.lang:
                continue
            sim = cosine(a.vec, b.vec)
            if sim >= args.threshold:
                pairs.append((sim, a, b))

    pairs.sort(key=lambda p: p[0], reverse=True)
    print(f"\n{len(pairs)} pair(s) ≥ {args.threshold}:\n")
    for sim, a, b in pairs[: args.top]:
        print(f"  {sim:.3f}  {a.uid}  ⇄  {b.uid}")
        print(f"          “{a.title}”")
        print(f"          “{b.title}”")

    if args.json:
        args.json.write_text(
            json.dumps(
                [
                    {"sim": round(sim, 4), "a": a.uid, "b": b.uid,
                     "a_title": a.title, "b_title": b.title}
                    for sim, a, b in pairs
                ],
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"\nWrote {len(pairs)} pairs to {args.json}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
