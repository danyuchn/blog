"""
Classify Instagram/Threads AI-related posts using Gemini 2.5 Flash Lite.
Reads exported JSON, sends posts in batches for semantic classification,
outputs structured results.

Usage:
    python scripts/classify_posts.py
"""

import json
import os
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
EXPORT_DIR = Path("/tmp/ig_export")
THREADS_FILE = EXPORT_DIR / "your_instagram_activity/threads/threads_and_replies.json"
IG_POSTS_FILE = EXPORT_DIR / "your_instagram_activity/media/posts_1.json"
OUTPUT_FILE = Path(__file__).parent.parent / "scripts" / "classified_posts.json"

BATCH_SIZE = 30  # posts per Gemini request
MODEL_NAME = "gemini-2.5-flash-lite"

SYSTEM_PROMPT = """\
你是一個內容分類專家。你的任務是將社群媒體貼文進行語意分類。

## 分類規則

每則貼文請判斷：

1. **is_ai_related** (boolean): 這則貼文的「主要主題」是否與 AI/人工智慧相關？
   - true: 主要在討論 AI 工具、AI 技術、AI 趨勢、AI 應用、AI 開發、AI 觀點
   - false: 只是順帶提到 AI（例如「用 AI 檢討 GMAT 題目」主題仍是 GMAT）
   - 判斷標準：如果拿掉 AI 的部分，這則貼文還有沒有意義？如果沒有，就是 AI 相關

2. **category** (string): 如果 is_ai_related=true，分到以下類別之一：
   - "ai-coding-tools": AI 輔助寫程式（Claude Code, Cursor, Copilot, Vibe Coding, Windsurf, Replit 等）
   - "ai-models-comparison": AI 模型比較、評測、使用心得（Claude vs GPT vs Gemini 等）
   - "ai-education": AI 在教育領域的應用、AI 如何改變教學、教學者的 AI 轉型
   - "ai-product-building": 打造 AI 產品、RAG、知識庫、部署、API 串接、技術實作
   - "ai-trends-opinions": AI 產業趨勢、對 AI 時代的觀點、職涯影響、社會觀察
   - "ai-daily-use": 日常生活中使用 AI 的心得（理財、閱讀、寫作、生產力等）
   - "ai-misc": 不屬於以上任何類別的 AI 相關內容
   如果 is_ai_related=false，category 設為 "not-ai"

3. **topic_summary** (string): 用一句話（15字以內）摘要這則貼文的核心主題

## 輸出格式

嚴格輸出 JSON array，每個元素對應輸入的一則貼文（按順序）：
```json
[
  {"id": 0, "is_ai_related": true, "category": "ai-coding-tools", "topic_summary": "Claude Code 使用技巧"},
  {"id": 1, "is_ai_related": false, "category": "not-ai", "topic_summary": "GMAT 備考策略"}
]
```

不要輸出任何其他文字，只輸出 JSON。
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def fix_encoding(text: str) -> str:
    """Fix Meta's UTF-8-as-Latin-1 encoding."""
    if not text:
        return text
    try:
        return text.encode("latin-1").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return text


@dataclass
class Post:
    source: str
    text: str
    timestamp: int
    date: str
    length: int


def extract_posts() -> list[Post]:
    """Extract all posts with text content from Threads and IG exports."""
    posts: list[Post] = []

    # Threads
    with open(THREADS_FILE, "r") as f:
        threads = json.load(f)
    for item in threads["text_post_app_text_posts"]:
        for m in item.get("media", []):
            title = fix_encoding(m.get("title", ""))
            ts = m.get("creation_timestamp", 0)
            if title and len(title.strip()) >= 10:
                posts.append(Post(
                    source="threads",
                    text=title.strip(),
                    timestamp=ts,
                    date=datetime.fromtimestamp(ts).strftime("%Y-%m-%d"),
                    length=len(title.strip()),
                ))

    # IG Posts
    with open(IG_POSTS_FILE, "r") as f:
        ig_posts = json.load(f)
    for post in ig_posts:
        title = fix_encoding(post.get("title", ""))
        ts = post.get("creation_timestamp", 0)
        if title and len(title.strip()) >= 10:
            posts.append(Post(
                source="ig_post",
                text=title.strip(),
                timestamp=ts,
                date=datetime.fromtimestamp(ts).strftime("%Y-%m-%d"),
                length=len(title.strip()),
            ))

    posts.sort(key=lambda p: p.timestamp)
    return posts


def classify_batch(
    model: genai.GenerativeModel,
    posts: list[Post],
    start_idx: int,
) -> list[dict]:
    """Send a batch of posts to Gemini for classification."""
    # Build input: numbered list of posts
    lines = []
    for i, post in enumerate(posts):
        # Truncate very long posts to save tokens
        text = post.text[:800] if len(post.text) > 800 else post.text
        text = text.replace("\n", " ")
        lines.append(f"[{i}] [{post.date}] [{post.source}] {text}")

    user_prompt = f"請分類以下 {len(posts)} 則貼文：\n\n" + "\n\n".join(lines)

    response = model.generate_content(user_prompt)
    raw = response.text.strip()

    # Extract JSON from response (handle markdown code blocks)
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]  # remove first line
        raw = raw.rsplit("```", 1)[0]  # remove last ```

    results = json.loads(raw)

    # Validate length
    if len(results) != len(posts):
        print(f"  WARNING: Expected {len(posts)} results, got {len(results)}")

    return results


def main() -> None:
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=SYSTEM_PROMPT,
    )

    print("Extracting posts...")
    all_posts = extract_posts()
    print(f"Total posts with text: {len(all_posts)}")

    # Process in batches
    all_results: list[dict] = []
    total_batches = (len(all_posts) + BATCH_SIZE - 1) // BATCH_SIZE

    for batch_idx in range(total_batches):
        start = batch_idx * BATCH_SIZE
        end = min(start + BATCH_SIZE, len(all_posts))
        batch = all_posts[start:end]

        print(f"Batch {batch_idx + 1}/{total_batches} ({start}-{end-1})...", end=" ")

        try:
            results = classify_batch(model, batch, start)
            # Attach original post data
            for i, result in enumerate(results):
                post = batch[i]
                result["source"] = post.source
                result["text"] = post.text
                result["timestamp"] = post.timestamp
                result["date"] = post.date
                result["length"] = post.length
                result["global_id"] = start + i
            all_results.extend(results)
            print(f"OK ({sum(1 for r in results if r.get('is_ai_related'))} AI-related)")
        except Exception as e:
            print(f"ERROR: {e}")
            # Mark batch as failed, retry individually could be added
            for i, post in enumerate(batch):
                all_results.append({
                    "id": i,
                    "global_id": start + i,
                    "is_ai_related": None,
                    "category": "error",
                    "topic_summary": f"Classification failed: {e}",
                    "source": post.source,
                    "text": post.text,
                    "timestamp": post.timestamp,
                    "date": post.date,
                    "length": post.length,
                })

        # Rate limiting
        if batch_idx < total_batches - 1:
            time.sleep(1)

    # Summary
    ai_posts = [r for r in all_results if r.get("is_ai_related")]
    print(f"\n{'='*60}")
    print(f"Total classified: {len(all_results)}")
    print(f"AI-related: {len(ai_posts)}")
    print(f"Not AI: {sum(1 for r in all_results if not r.get('is_ai_related'))}")
    print(f"Errors: {sum(1 for r in all_results if r.get('category') == 'error')}")

    # Category breakdown
    from collections import Counter
    cats = Counter(r["category"] for r in ai_posts)
    print(f"\nAI Category breakdown:")
    for cat, cnt in cats.most_common():
        print(f"  {cat}: {cnt}")

    # Save results
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
