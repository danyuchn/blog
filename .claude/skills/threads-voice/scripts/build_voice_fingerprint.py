#!/usr/bin/env python3
"""
threads-voice: 把 threads_corpus.json 蒸餾成兩份給 Fable 讀的檔案：

    compiled/voice_fingerprint.md    — 純腳本算出來的量化統計摘要（幾 KB，Fable 一定要讀）
    compiled/voice_fingerprint.json  — 同一份統計的完整結構化版本（供程式化查詢/除錯用）
    compiled/qualitative_sample.json — 分層抽樣出的一小批「原文全文」（近期 + 最長 + 隨機各 N 篇，去重）

目的：語料量很大時，量化維度（句長分佈、口頭禪次數、開場/收尾模式、段落節奏）全部
用純 Python 計算，不用 Fable 的額度去「讀完全部貼文再自己數」；Fable 只在讀
voice_fingerprint.md 之後，針對真正需要判斷力的質化維度（語氣、幽默、認知層信念），
去讀 qualitative_sample.json 這一小份代表性樣本的原文，而不是整包 threads_corpus.json。

改作自 akseolabs-seo/AK-Threads-booster 的 scripts/build_voice_distillation.py（MIT
License，見 ../NOTICE.md）。因為 Meta 官方帳號匯出不含互動數據（讚數/瀏覽數/留言數），
拿掉了原版全部「engagement-weighted」（按互動數加權）的邏輯，改成：
    - 量化統計一律用「全部貼文」，不分「高互動 vs 一般」
    - 質化樣本的分層基準從「近期 + 高互動 + 隨機」改成「近期 + 最長 + 隨機」
      （最長的貼文通常資訊量最大，某種程度上補償沒有互動訊號可用的問題）

用法：
    python build_voice_fingerprint.py --corpus .claude/voice/threads_corpus.json
    python build_voice_fingerprint.py --corpus .claude/voice/threads_corpus.json \
        --output-dir .claude/voice/compiled --sample-size 15
"""

import argparse
import hashlib
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

WORD_RE = re.compile(r"[A-Za-z0-9_\-一-鿿぀-ヿ가-힯฀-๿]+")
LATIN_TOKEN_RE = re.compile(r"[A-Za-z0-9_\-]+")
CJK_CHAR_RE = re.compile(r"[一-鿿぀-ヿ가-힯฀-๿]")
SENTENCE_RE = re.compile(r"[^。！？!?.\n]+[。！？!?.]?")
EMOJI_RE = re.compile(
    "[" "\U0001F300-\U0001FAFF" "\U00002700-\U000027BF" "\U00002600-\U000026FF" "]+",
    flags=re.UNICODE,
)

JUDGMENT_MARKERS = [
    "我覺得", "我觉得", "我認為", "我认为", "我相信", "說白了", "说白了",
    "老實說", "老实说", "坦白說", "坦白说", "其實", "其实", "本質", "本质",
    "真正", "不是", "而是", "不只是", "不要", "不能", "應該", "应该",
    "必須", "必须", "最好",
    "honestly", "to be honest", "i think", "i believe", "the point is", "the key is",
]

AI_TEMPLATE_PATTERNS = [
    "總結來說", "总结来说", "綜上所述", "综上所述", "在這個快速變化的時代", "在这个快速变化的时代",
    "不僅如此", "不仅如此", "更重要的是",
    "moreover", "furthermore", "in today's world", "ultimately",
]

TRANSITION_CANDIDATES = [
    "但", "但是", "可是", "所以", "因為", "因为", "然後", "然后", "其實", "其实",
    "說真的", "说真的", "老實說", "老实说", "換句話說", "换句话说", "反過來說", "反过来说",
    "問題是", "问题是", "重點是", "重点是",
    "anyway", "honestly", "but", "so", "because",
]


def parse_iso(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed
    except ValueError:
        return None


def sort_key(post: Dict[str, Any]) -> datetime:
    return parse_iso(post.get("created_at")) or datetime.min.replace(tzinfo=timezone.utc)


def stable_rank_key(post_id: str) -> str:
    """跟 PYTHONHASHSEED 無關的穩定偽隨機排序鍵，讓「隨機抽樣」每次跑結果一致。"""
    return hashlib.sha256(str(post_id).encode("utf-8")).hexdigest()


def compact_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def summarize_text(text: str, limit: int = 140) -> str:
    compact = compact_space(text)
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1].rstrip() + "..."


def word_tokens(text: str) -> List[str]:
    """粗顆粒 chunk 化 token，用於口頭禪/慣用詞清單——刻意保留連續中文字整段當一個 chunk，
    效果類似抓「常用短句片段」而不是逐字拆，拿來統計口頭禪比逐字拆更有用。不要拿這個算字數。"""
    return [token.lower() for token in WORD_RE.findall(text) if token.strip()]


def length_units(text: str) -> int:
    """給句長/節奏統計用的「字數」：中文逐字算、Latin 逐詞算，貼近中文寫作者理解的字數概念。
    跟 word_tokens 刻意分開，因為 word_tokens 的整段 chunk 化會讓字數統計嚴重失真。"""
    return len(LATIN_TOKEN_RE.findall(text)) + len(CJK_CHAR_RE.findall(text))


def split_paragraphs(text: str) -> List[str]:
    return [p.strip() for p in re.split(r"\n\s*\n|\r\n\s*\r\n", text.strip()) if p.strip()]


def split_sentences(text: str) -> List[str]:
    sentences = [m.group(0).strip() for m in SENTENCE_RE.finditer(text) if m.group(0).strip()]
    return sentences or ([text.strip()] if text.strip() else [])


def percentile(values: List[int], pct: float) -> Optional[float]:
    if not values:
        return None
    values = sorted(values)
    if len(values) == 1:
        return float(values[0])
    position = (len(values) - 1) * pct
    low = math.floor(position)
    high = math.ceil(position)
    if low == high:
        return float(values[low])
    return values[low] + (values[high] - values[low]) * (position - low)


def stable_mean(values: Iterable[int]) -> Optional[float]:
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    return round(float(statistics.mean(clean)), 2)


def phase_name(index: int) -> str:
    return ("early", "middle", "recent")[index]


def phase_posts(posts: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    ordered = sorted(posts, key=sort_key)
    phases = {"early": [], "middle": [], "recent": []}
    if not ordered:
        return phases
    for idx, post in enumerate(ordered):
        bucket = min(2, int(idx * 3 / len(ordered)))
        phases[phase_name(bucket)].append(post)
    return phases


def classify_opening(text: str) -> str:
    first = split_sentences(text)[0] if text.strip() else ""
    lowered = first.lower()
    if "?" in first or "？" in first:
        return "question_opening"
    if re.search(r"\d+|[一二三四五六七八九十]+(個|个)", first):
        return "number_or_result_opening"
    if any(marker in lowered for marker in ("我", "最近", "昨天", "today", "i ")):
        return "personal_experience_opening"
    if any(marker in first for marker in ("不是", "不只是", "其實", "其实", "說白了", "说白了")):
        return "judgment_or_contrast_opening"
    if any(marker in lowered for marker in ("how to", "怎麼", "怎么", "如何")):
        return "how_to_opening"
    return "direct_statement_opening"


def classify_ending(text: str) -> str:
    last = split_sentences(text)[-1] if text.strip() else ""
    lowered = last.lower()
    if "?" in last or "？" in last:
        return "question_ending"
    if any(marker in last for marker in ("留言", "告訴我", "告诉我", "分享", "你覺得", "你觉得")):
        return "explicit_cta_ending"
    if any(marker in last for marker in ("不要", "別", "别", "記得", "记得", "可以先", "試試", "试试")):
        return "action_advice_ending"
    if any(marker in last for marker in ("。", ".", "！", "!")) and len(last) <= 28:
        return "clean_cut_ending"
    if any(marker in lowered for marker in ("honestly", "anyway", "that's it")):
        return "personal_aside_ending"
    return "soft_landing_ending"


def pattern_inventory(posts: List[Dict[str, Any]], classifier) -> List[Dict[str, Any]]:
    buckets: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for post in posts:
        text = post.get("text") or ""
        if not text:
            continue
        buckets[classifier(text)].append(post)
    inventory = []
    for pattern, bucket in sorted(buckets.items(), key=lambda item: (-len(item[1]), item[0])):
        examples = sorted(bucket, key=sort_key, reverse=True)[:3]
        inventory.append({
            "pattern": pattern,
            "count": len(bucket),
            "examples": [
                {"id": post.get("id"), "excerpt": summarize_text(post.get("text", ""), 120)}
                for post in examples
            ],
        })
    return inventory


def top_counter(counter: Counter, limit: int = 20) -> List[Dict[str, Any]]:
    return [{"value": key, "count": value} for key, value in counter.most_common(limit)]


def phrase_inventory(posts: List[Dict[str, Any]]) -> Dict[str, Any]:
    openers, closers, transitions, tokens, emoji, punctuation = (Counter() for _ in range(6))
    code_switch_posts = 0
    posts_with_emoji = 0
    for post in posts:
        text = post.get("text") or ""
        if not text:
            continue
        compact = compact_space(text)
        openers[compact[:18]] += 1
        closers[compact[-18:]] += 1
        for candidate in TRANSITION_CANDIDATES:
            count = text.lower().count(candidate.lower())
            if count:
                transitions[candidate] += count
        for token in word_tokens(text):
            if len(token) >= 2:
                tokens[token] += 1
        emojis = EMOJI_RE.findall(text)
        if emojis:
            posts_with_emoji += 1
        for chunk in emojis:
            for char in chunk:
                emoji[char] += 1
        if re.search(r"[A-Za-z]{3,}", text) and re.search(r"[一-鿿]", text):
            code_switch_posts += 1
        for mark in ("?", "？", "!", "！", "...", "…", "(", ")", "（", "）", ":", "："):
            punctuation[mark] += text.count(mark)
    total = max(len(posts), 1)
    return {
        "openers": top_counter(openers, 15),
        "closers": top_counter(closers, 15),
        "transition_words": top_counter(transitions, 20),
        "content_words": top_counter(tokens, 30),
        "emoji_usage": {
            "posts_with_emoji": posts_with_emoji,
            "usage_pct": round(posts_with_emoji / total * 100, 1),
            "top_emoji": top_counter(emoji, 15),
        },
        "punctuation": top_counter(punctuation, 20),
        "code_switching": {
            "posts_with_mixed_latin_cjk": code_switch_posts,
            "usage_pct": round(code_switch_posts / total * 100, 1),
        },
    }


def rhythm_stats(posts: List[Dict[str, Any]]) -> Dict[str, Any]:
    word_counts, paragraph_counts, sentence_counts, first_sentence_lengths = [], [], [], []
    single_line_paragraphs = 0
    total_paragraphs = 0
    for post in posts:
        text = post.get("text") or ""
        if not text:
            continue
        paragraphs = split_paragraphs(text)
        sentences = split_sentences(text)
        word_counts.append(length_units(text))
        paragraph_counts.append(len(paragraphs))
        sentence_counts.append(len(sentences))
        if sentences:
            first_sentence_lengths.append(length_units(sentences[0]))
        for paragraph in paragraphs:
            total_paragraphs += 1
            if "\n" not in paragraph and len(paragraph) <= 70:
                single_line_paragraphs += 1
    return {
        "word_count": {
            "avg": stable_mean(word_counts),
            "p25": percentile(word_counts, 0.25),
            "p50": percentile(word_counts, 0.5),
            "p75": percentile(word_counts, 0.75),
        },
        "paragraph_count_avg": stable_mean(paragraph_counts),
        "sentence_count_avg": stable_mean(sentence_counts),
        "first_sentence_word_count_avg": stable_mean(first_sentence_lengths),
        "single_line_paragraph_ratio": round(single_line_paragraphs / max(total_paragraphs, 1), 3),
    }


def belief_candidates(posts: List[Dict[str, Any]], limit: int = 60) -> List[Dict[str, Any]]:
    candidates = []
    for post in posts:
        text = post.get("text") or ""
        if not text:
            continue
        for sentence in split_sentences(text):
            lowered = sentence.lower()
            markers = [marker for marker in JUDGMENT_MARKERS if marker.lower() in lowered]
            if not markers or len(sentence) < 8:
                continue
            candidates.append({
                "id": post.get("id"),
                "created_at": post.get("created_at"),
                "markers": markers[:5],
                "sentence": sentence[:240],
            })
    candidates.sort(key=lambda row: row["created_at"] or "", reverse=True)
    return candidates[:limit]


def anti_voice_candidates(posts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    text = "\n".join(post.get("text") or "" for post in posts)
    total = len(posts)
    rows = []
    for pattern in AI_TEMPLATE_PATTERNS:
        count = text.lower().count(pattern.lower())
        if count <= max(1, math.floor(total * 0.02)):
            rows.append({
                "pattern": pattern,
                "observed_count": count,
                "candidate_rule": "疑似「非本人」用語候選，寫進 brand_voice.md 前要在使用者手動修正裡確認，或有足夠證據支持。",
            })
    return rows


def temporal_shift(posts: List[Dict[str, Any]]) -> Dict[str, Any]:
    phases = phase_posts(posts)
    result = {}
    for name, bucket in phases.items():
        openings = pattern_inventory(bucket, classify_opening)
        endings = pattern_inventory(bucket, classify_ending)
        result[name] = {
            "post_count": len(bucket),
            "top_opening": openings[0]["pattern"] if openings else None,
            "top_ending": endings[0]["pattern"] if endings else None,
            "rhythm": rhythm_stats(bucket),
        }
    stable = []
    for key in ("top_opening", "top_ending"):
        values = [result[name].get(key) for name in ("early", "middle", "recent") if result[name].get(key)]
        if values and len(set(values)) == 1:
            stable.append({"feature": key, "value": values[0]})
    return {"phases": result, "stable_signals": stable}


def qualitative_sample(posts: List[Dict[str, Any]], sample_size: int) -> List[Dict[str, Any]]:
    """分層抽樣：近期 N + 最長 N + 隨機 N（去重），給 Fable 讀全文用的小樣本。"""
    by_recent = sorted(posts, key=sort_key, reverse=True)[:sample_size]
    by_length = sorted(posts, key=lambda p: len(p.get("text") or ""), reverse=True)[:sample_size]
    by_random = sorted(posts, key=lambda p: stable_rank_key(p.get("id")))[:sample_size]

    picked: Dict[str, Dict[str, Any]] = {}
    for tier_name, tier_posts in (("recent", by_recent), ("longest", by_length), ("random", by_random)):
        for post in tier_posts:
            pid = post.get("id")
            if pid in picked:
                picked[pid]["sample_tiers"].append(tier_name)
            else:
                picked[pid] = {**post, "sample_tiers": [tier_name]}
    return sorted(picked.values(), key=sort_key, reverse=True)


def load_posts(corpus_path: Path) -> List[Dict[str, Any]]:
    corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
    posts = corpus.get("posts") if isinstance(corpus, dict) else corpus
    return [post for post in (posts or []) if isinstance(post, dict) and post.get("text")]


def build_fingerprint(corpus_path: Path, sample_size: int) -> Dict[str, Any]:
    posts = load_posts(corpus_path)
    return {
        "_meta": {
            "schema_version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "source_corpus": corpus_path.name,
            "posts_count": len(posts),
            "coverage_notes": "純腳本統計，無互動數據加權（Meta 官方匯出不含讚數/瀏覽數）。",
        },
        "rhythm": rhythm_stats(posts),
        "opening_inventory": pattern_inventory(posts, classify_opening),
        "ending_inventory": pattern_inventory(posts, classify_ending),
        "phrases": phrase_inventory(posts),
        "temporal_shift": temporal_shift(posts),
        "cognitive_layer_seed": {
            "belief_candidate_sentences": belief_candidates(posts),
            "instruction": "這些只是候選句，/threads-voice 要把它們歸納成核心信念、張力、判斷框架，並附原文佐證。",
        },
        "anti_voice_seed": {
            "candidate_not_me_phrases": anti_voice_candidates(posts),
            "instruction": "這些是低頻/缺席訊號，不是使用者確認前的硬規則。",
        },
        "qualitative_sample_seed": {
            "sample_size_per_tier": sample_size,
            "post_ids": [post["id"] for post in qualitative_sample(posts, sample_size)],
            "instruction": "全文樣本另外寫在 compiled/qualitative_sample.json，質化維度分析只需要讀那份小檔，不用讀完整 threads_corpus.json。",
        },
    }


def fmt(value: Any) -> str:
    if value is None:
        return "unknown"
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def render_inventory_table(items: List[Dict[str, Any]]) -> List[str]:
    lines = ["| Pattern | Count | Top evidence |", "|---|---:|---|"]
    for item in items[:8]:
        example = item.get("examples", [{}])[0] if item.get("examples") else {}
        lines.append(f"| `{item['pattern']}` | {item['count']} | `{example.get('id', 'unknown')}`: {example.get('excerpt', '')} |")
    return lines


def render_markdown(data: Dict[str, Any]) -> str:
    meta = data["_meta"]
    rhythm = data["rhythm"]
    lines = [
        "# Voice Fingerprint（純腳本統計，Fable 分析前先讀這份）",
        "",
        "```yaml",
        f"generated_at: {meta['generated_at']}",
        f"source_corpus: {meta['source_corpus']}",
        f"posts_count: {meta['posts_count']}",
        "```",
        "",
        "## 節奏基準",
        "| 平均字數 | P50 字數 | 平均段落數 | 平均首句字數 | 單行段落比例 |",
        "|---:|---:|---:|---:|---:|",
        f"| {fmt(rhythm['word_count']['avg'])} | {fmt(rhythm['word_count']['p50'])} | "
        f"{fmt(rhythm['paragraph_count_avg'])} | {fmt(rhythm['first_sentence_word_count_avg'])} | "
        f"{fmt(rhythm['single_line_paragraph_ratio'])} |",
        "",
        "## 開場模式庫",
    ]
    lines.extend(render_inventory_table(data["opening_inventory"]))
    lines.extend(["", "## 收尾模式庫"])
    lines.extend(render_inventory_table(data["ending_inventory"]))

    phrases = data["phrases"]
    lines.extend(["", "## 口頭禪與慣用詞（前 20）"])
    lines.extend([f"- `{item['value']}` x{item['count']}" for item in phrases["content_words"][:20]])
    lines.extend(["", "## 轉折詞"])
    lines.extend([f"- `{item['value']}` x{item['count']}" for item in phrases["transition_words"][:10]])
    lines.extend([
        "",
        "## Emoji / 中英混用",
        f"- 有用 emoji 的貼文比例：{phrases['emoji_usage']['usage_pct']}%",
        f"- 中英混用比例：{phrases['code_switching']['usage_pct']}%",
        "",
        "## 認知層信念候選句（前 20）",
    ])
    candidates = data["cognitive_layer_seed"]["belief_candidate_sentences"][:20]
    if candidates:
        lines.extend(["| Post | Markers | 候選句 |", "|---|---|---|"])
        for c in candidates:
            lines.append(f"| `{c['id']}` | {', '.join(c['markers'])} | {c['sentence']} |")
    else:
        lines.append("- 沒掃到明顯的信念標記句，這維度要靠質化樣本人工判讀。")

    lines.extend(["", "## 時期分佈（early / middle / recent）"])
    phases = data["temporal_shift"]["phases"]
    lines.extend(["| 時期 | 貼文數 | 主要開場 | 主要收尾 |", "|---|---:|---|---|"])
    for name in ("early", "middle", "recent"):
        p = phases[name]
        lines.append(f"| {name} | {p['post_count']} | {p.get('top_opening') or 'unknown'} | {p.get('top_ending') or 'unknown'} |")
    stable = data["temporal_shift"]["stable_signals"]
    if stable:
        lines.append("")
        lines.extend(f"- 跨三個時期都穩定：`{item['feature']}` = `{item['value']}`" for item in stable)

    lines.extend(["", "## 風格禁區候選（低頻 AI 套話掃描）"])
    for row in data["anti_voice_seed"]["candidate_not_me_phrases"][:12]:
        lines.append(f"- `{row['pattern']}` 出現 {row['observed_count']} 次。{row['candidate_rule']}")

    seed = data["qualitative_sample_seed"]
    lines.extend([
        "",
        "## 質化樣本",
        f"- 已抽出 {len(seed['post_ids'])} 篇代表性貼文全文，存在 `compiled/qualitative_sample.json`。",
        "- 質化維度（語氣切換、幽默、認知層信念歸納等）分析時**只讀這份小檔**，不要重讀整包 threads_corpus.json。",
        "",
        "## 使用提醒",
        "- 這份檔案是量化統計，涵蓋句構、開場/收尾、口頭禪、節奏、時期分佈。",
        "- 質化判斷（語氣、幽默、信念歸納）交給 `compiled/qualitative_sample.json` 的原文樣本 + threads-voice 的分析步驟。",
        "- 使用者在 brand_voice.md 手動修正的內容，永遠比這份檔案的任何統計都優先。",
    ])
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(corpus_path: Path, output_dir: Path, sample_size: int) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    posts = load_posts(corpus_path)
    data = build_fingerprint(corpus_path, sample_size)

    (output_dir / "voice_fingerprint.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (output_dir / "voice_fingerprint.md").write_text(render_markdown(data), encoding="utf-8")

    sample_posts = qualitative_sample(posts, sample_size)
    (output_dir / "qualitative_sample.json").write_text(
        json.dumps({
            "generated_at": data["_meta"]["generated_at"],
            "sample_size_per_tier": sample_size,
            "posts": sample_posts,
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser(description="把 threads_corpus.json 蒸餾成 voice fingerprint + 質化樣本")
    parser.add_argument("--corpus", required=True, help="threads_corpus.json 路徑")
    parser.add_argument("--output-dir", default=None, help="輸出資料夾，預設是 corpus 同層的 compiled/")
    parser.add_argument("--sample-size", type=int, default=15, help="質化樣本每個分層抽幾篇（近期/最長/隨機各抽這麼多，會去重）")
    args = parser.parse_args()

    corpus_path = Path(args.corpus).resolve()
    if not corpus_path.exists():
        raise SystemExit(f"找不到語料檔: {corpus_path}")

    output_dir = Path(args.output_dir).resolve() if args.output_dir else corpus_path.parent / "compiled"
    write_outputs(corpus_path, output_dir, args.sample_size)

    posts_count = len(load_posts(corpus_path))
    print(f"完成！{posts_count} 篇貼文已蒸餾到 {output_dir}")
    print("  - voice_fingerprint.md   （量化統計摘要，Fable 分析前先讀這份）")
    print("  - voice_fingerprint.json （同一份統計的完整結構化版本）")
    print("  - qualitative_sample.json（分層抽樣的原文全文，質化維度只讀這份）")


if __name__ == "__main__":
    main()
