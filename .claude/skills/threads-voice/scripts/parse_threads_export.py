#!/usr/bin/env python3
"""
threads-voice: 把 Meta 官方帳號資料匯出（Threads）解析成精簡語料 JSON。

取得匯出檔的步驟：
    1. 開啟 https://accountscenter.meta.com/info_and_permissions/dyi/（用你的 Threads 帳號登入）
    2. 選 Threads 帳號 -> Download or transfer information
    3. Some of your information -> 勾選 Threads 相關類別（至少要有 posts）
    4. Destination: Download to device；Date range: All time；Format: JSON
    5. 送出後等 email 通知（15 分鐘到 48 小時不等），下載 zip 並完整解壓縮

用法：
    python parse_threads_export.py --input /path/to/export/folder_or_file [--output threads_corpus.json]

改作自 akseolabs-seo/AK-Threads-booster 的 scripts/parse_export.py（MIT License，
見 ../NOTICE.md）。拿掉了 algorithm_signals / psychology_signals / metrics 等
成長分析用的欄位，只留寫作風格分析需要的最小欄位。
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    from html.parser import HTMLParser
except ImportError:
    pass


def find_threads_data(export_path: str) -> dict:
    """在 Meta 匯出資料夾裡找出 Threads 資料檔案。"""
    export_dir = Path(export_path)
    result = {"format": None, "posts_file": None}

    search_patterns = [
        "threads/threads_and_replies.json",
        "threads/posts_and_replies.json",
        "your_threads_activity/threads_and_replies.json",
        "threads_and_replies.json",
        "threads/threads.json",
        "threads.json",
        "your_activity_across_facebook/threads/threads_and_replies.json",
    ]

    for pattern in search_patterns:
        candidate = export_dir / pattern
        if candidate.exists():
            result["format"] = "json"
            result["posts_file"] = str(candidate)
            print(f"  找到 JSON 資料: {candidate}")
            return result

    for html_file in export_dir.rglob("*.html"):
        if "threads" in str(html_file).lower():
            result["format"] = "html"
            result["posts_file"] = str(html_file)
            print(f"  找到 HTML 資料: {html_file}")
            return result

    for json_file in export_dir.rglob("*.json"):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict) and any(
                k in data for k in ["threads", "text_post_threads", "thread_posts"]
            ):
                result["format"] = "json"
                result["posts_file"] = str(json_file)
                print(f"  在此檔找到 threads 資料: {json_file}")
                return result
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

    return result


def decode_meta_text(text: str) -> str:
    """解碼 Meta 匯出檔裡常見的錯誤編碼 escaped UTF-8。"""
    if not text:
        return ""
    try:
        return text.encode("latin-1").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        return text


def count_words(text: str) -> int:
    return len(text.split()) if text else 0


def count_paragraphs(text: str) -> int:
    if not text:
        return 0
    return len([chunk for chunk in text.splitlines() if chunk.strip()])


def extract_post_from_json(item: dict) -> Optional[dict]:
    text = ""
    for key in ["text", "post", "content", "title"]:
        if key in item and isinstance(item[key], str):
            text = decode_meta_text(item[key])
            break
        elif key in item and isinstance(item[key], dict):
            text = decode_meta_text(item[key].get("text", item[key].get("value", "")))
            break
        elif key in item and isinstance(item[key], list):
            for sub in item[key]:
                if isinstance(sub, str):
                    text = decode_meta_text(sub)
                    break
                elif isinstance(sub, dict):
                    text = decode_meta_text(sub.get("text", sub.get("value", "")))
                    break
            if text:
                break

    if not text:
        return None

    timestamp = ""
    for key in ["timestamp", "created_at", "creation_timestamp", "date"]:
        if key in item:
            val = item[key]
            if isinstance(val, (int, float)):
                timestamp = datetime.fromtimestamp(val, tz=timezone.utc).isoformat()
            elif isinstance(val, str):
                timestamp = val
            break

    is_reply = item.get("is_reply", False)
    if not is_reply:
        is_reply = any(k in item for k in ["parent", "in_reply_to", "reply_to"])
    if is_reply:
        return None

    return {
        "id": str(item.get("id", item.get("uri", f"export_{abs(hash(text))}"))),
        "text": text,
        "created_at": timestamp,
        "permalink": item.get("permalink", item.get("url", "")),
        "word_count": count_words(text),
        "paragraph_count": count_paragraphs(text),
    }


def parse_json_export(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    threads_data = None
    if isinstance(data, list):
        threads_data = data
    elif isinstance(data, dict):
        for key in ["threads", "text_post_threads", "thread_posts", "your_threads", "posts"]:
            if key in data:
                threads_data = data[key]
                break
        if threads_data is None:
            for _, value in data.items():
                if isinstance(value, list) and len(value) > 0:
                    if isinstance(value[0], dict) and any(
                        k in value[0] for k in ["text", "post", "content", "title"]
                    ):
                        threads_data = value
                        break

    if threads_data is None:
        print(f"  警告：在 {file_path} 找不到可辨識的 threads 資料結構")
        print(f"  頂層 key: {list(data.keys()) if isinstance(data, dict) else 'list'}")
        return []

    posts = []
    for item in threads_data:
        post = extract_post_from_json(item)
        if post:
            posts.append(post)
    return posts


class ThreadsHTMLParser(HTMLParser):
    """解析 Meta HTML 格式匯出檔。"""

    def __init__(self):
        super().__init__()
        self.posts = []
        self.current_text = ""
        self.current_timestamp = ""
        self.in_content = False
        self.in_timestamp = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get("class", "")
        if "pam" in cls or "content" in cls.lower():
            self.in_content = True
            self.current_text = ""
        if "timestamp" in cls.lower() or "date" in cls.lower():
            self.in_timestamp = True
            self.current_timestamp = ""

    def handle_endtag(self, tag):
        if self.in_content and tag in ("div", "p"):
            if self.current_text.strip():
                self.posts.append(
                    {"text": self.current_text.strip(), "timestamp": self.current_timestamp}
                )
            self.in_content = False
        if self.in_timestamp:
            self.in_timestamp = False

    def handle_data(self, data):
        if self.in_content:
            self.current_text += data
        if self.in_timestamp:
            self.current_timestamp = data.strip()


def parse_html_export(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    parser = ThreadsHTMLParser()
    parser.feed(content)

    posts = []
    for item in parser.posts:
        text = item["text"]
        if not text:
            continue
        posts.append(
            {
                "id": f"export_{abs(hash(text))}",
                "text": text,
                "created_at": item.get("timestamp", ""),
                "permalink": "",
                "word_count": count_words(text),
                "paragraph_count": count_paragraphs(text),
            }
        )
    return posts


def post_sort_key(post: dict):
    """讓時間字串排序在混合時區/空字串時也不會炸掉。"""
    ts = post.get("created_at") or ""
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError:
        return datetime.min.replace(tzinfo=timezone.utc)


def atomic_write_json(path: str, data: dict) -> None:
    """備份既有檔 -> 寫暫存檔 -> 原子改名，避免半寫壞掉語料。"""
    target = Path(path)
    if target.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = target.with_name(f"{target.name}.bak-{stamp}")
        backup.write_bytes(target.read_bytes())
        print(f"  既有檔已備份到 {backup}")

    tmp = target.with_name(f"{target.name}.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(target)


def main():
    parser = argparse.ArgumentParser(
        description="把 Meta Threads 官方資料匯出解析成 threads-voice 用的精簡語料 JSON"
    )
    parser.add_argument("--input", required=True, help="Meta 匯出資料夾（或直接指定 JSON/HTML 檔）路徑")
    parser.add_argument("--output", default="threads_corpus.json", help="輸出檔路徑")
    args = parser.parse_args()

    input_path = Path(args.input)
    print("[1/3] 尋找匯出檔中的 Threads 資料...")

    if input_path.is_file():
        ext = input_path.suffix.lower()
        if ext == ".json":
            file_info = {"format": "json", "posts_file": str(input_path)}
        elif ext in (".html", ".htm"):
            file_info = {"format": "html", "posts_file": str(input_path)}
        else:
            print(f"錯誤：不支援的副檔名 {ext}")
            sys.exit(1)
    else:
        file_info = find_threads_data(str(input_path))

    if not file_info["posts_file"]:
        print("錯誤：在匯出資料夾裡找不到 Threads 資料。")
        print("請確認是從 Meta Account Center 匯出、且有勾選 Threads 類別。")
        sys.exit(1)

    print(f"[2/3] 解析 {file_info['format'].upper()} 匯出檔...")
    if file_info["format"] == "json":
        posts = parse_json_export(file_info["posts_file"])
    else:
        posts = parse_html_export(file_info["posts_file"])

    if not posts:
        print("錯誤：匯出檔裡沒有解析到任何貼文。檔案可能是空的，或格式跟預期不同。")
        print("可以把檔案的頂層結構貼給 Claude，讓它手動調整 parser。")
        sys.exit(1)

    posts.sort(key=post_sort_key, reverse=True)
    print(f"  找到 {len(posts)} 篇貼文")

    print("[3/3] 寫入語料檔...")
    corpus = {
        "source": "meta_account_export",
        "posts": posts,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    atomic_write_json(args.output, corpus)
    print(f"\n完成！{len(posts)} 篇貼文已寫入 {args.output}")
    print("下一步：在 Claude Code 對這個專案說「分析我的 threads 語氣」觸發 threads-voice skill。")


if __name__ == "__main__":
    main()
