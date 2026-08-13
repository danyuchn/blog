"""
Scan YouTube subscriptions or a public channel for new videos in the past N days.

Reuses the yutu OAuth credentials at ~/.credentials/yutu/. Refreshes the
access token automatically via the stored refresh_token — no browser step
needed as long as the refresh_token is still valid.

Usage:
    python scripts/youtube_weekly_scan.py           # past 7 days
    python scripts/youtube_weekly_scan.py --days 14
    python scripts/youtube_weekly_scan.py --output /tmp/yt-week.json
"""

import argparse
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

CRED_DIR = Path.home() / ".credentials" / "yutu"
CLIENT_SECRET = CRED_DIR / "client_secret.json"
TOKEN_FILE = CRED_DIR / "youtube.token.json"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube",
]
YOUTUBE_ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}


def recent_public_uploads(channel_id: str, after: datetime) -> list[dict]:
    """Read the official public YouTube Atom feed; requires no OAuth scope."""
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    request = urllib.request.Request(url, headers={"User-Agent": "AgentCrew weekly scan/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        root = ET.fromstring(response.read())

    videos = []
    for entry in root.findall("atom:entry", YOUTUBE_ATOM_NS):
        published = datetime.fromisoformat(
            entry.findtext("atom:published", namespaces=YOUTUBE_ATOM_NS).replace("Z", "+00:00")
        )
        if published < after:
            continue
        video_id = entry.findtext("yt:videoId", namespaces=YOUTUBE_ATOM_NS)
        link = entry.find("atom:link", YOUTUBE_ATOM_NS)
        videos.append(
            {
                "video_id": video_id,
                "title": entry.findtext("atom:title", namespaces=YOUTUBE_ATOM_NS),
                "published_at": published.isoformat(),
                "url": link.attrib["href"] if link is not None else f"https://youtu.be/{video_id}",
            }
        )
    return videos


def load_credentials():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials

    client = json.loads(CLIENT_SECRET.read_text())
    web = client.get("web") or client.get("installed")
    token = json.loads(TOKEN_FILE.read_text())

    creds = Credentials(
        token=token.get("access_token"),
        refresh_token=token.get("refresh_token"),
        token_uri=web.get("token_uri", "https://oauth2.googleapis.com/token"),
        client_id=web["client_id"],
        client_secret=web["client_secret"],
        scopes=SCOPES,
    )

    if not creds.valid:
        creds.refresh(Request())
        # Persist refreshed access_token back so yutu and future runs reuse it
        token["access_token"] = creds.token
        if creds.expiry:
            delta = int((creds.expiry - datetime.utcnow()).total_seconds())
            token["expires_in"] = max(delta, 0)
        TOKEN_FILE.write_text(json.dumps(token, indent=2))

    return creds


def list_subscriptions(youtube) -> list[dict]:
    subs = []
    page_token = None
    while True:
        resp = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=page_token,
        ).execute()
        subs.extend(resp.get("items", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return subs


def recent_videos_for_channel(youtube, channel_id: str, after_iso: str) -> list[dict]:
    """Use search.list filtered by channelId + publishedAfter. 1 quota unit per ~100 items."""
    try:
        resp = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            publishedAfter=after_iso,
            order="date",
            type="video",
            maxResults=10,
        ).execute()
    except Exception as e:
        return [{"_error": str(e)}]
    return resp.get("items", [])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--output", type=Path, default=Path("/tmp/youtube-weekly-scan.json"))
    ap.add_argument(
        "--own-channel-id",
        help="Read this public channel's official RSS feed instead of OAuth subscriptions.",
    )
    args = ap.parse_args()

    after = datetime.now(tz=timezone.utc) - timedelta(days=args.days)
    after_iso = after.strftime("%Y-%m-%dT%H:%M:%SZ")

    if args.own_channel_id:
        videos = recent_public_uploads(args.own_channel_id, after)
        result = {
            "source": "youtube-public-atom",
            "channel_id": args.own_channel_id,
            "after": after_iso,
            "videos": videos,
        }
        print(f"Public channel {args.own_channel_id}: {len(videos)} new video(s) after {after_iso}")
        for video in videos:
            print(f"- [{video['published_at'][:10]}] {video['title']}\n  {video['url']}")
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print(f"Saved to {args.output}")
        return

    creds = load_credentials()
    from googleapiclient.discovery import build

    youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)

    print(f"Listing subscriptions...")
    subs = list_subscriptions(youtube)
    print(f"Found {len(subs)} subscriptions. Scanning videos published after {after_iso}...\n")

    all_results = []
    for i, sub in enumerate(subs, 1):
        snip = sub["snippet"]
        channel_id = snip["resourceId"]["channelId"]
        channel_title = snip["title"]
        vids = recent_videos_for_channel(youtube, channel_id, after_iso)
        real_vids = [v for v in vids if "_error" not in v]
        if real_vids:
            print(f"[{i}/{len(subs)}] {channel_title}: {len(real_vids)} new")
            for v in real_vids:
                s = v["snippet"]
                print(f"    - [{s['publishedAt'][:10]}] {s['title']}")
                print(f"      https://youtu.be/{v['id']['videoId']}")
            all_results.append({
                "channel_id": channel_id,
                "channel_title": channel_title,
                "videos": [
                    {
                        "video_id": v["id"]["videoId"],
                        "title": v["snippet"]["title"],
                        "published_at": v["snippet"]["publishedAt"],
                        "description": v["snippet"]["description"][:300],
                    }
                    for v in real_vids
                ],
            })

    print(f"\n{'=' * 60}")
    print(f"Channels with new videos: {len(all_results)}")
    print(f"Total new videos: {sum(len(c['videos']) for c in all_results)}")

    args.output.write_text(json.dumps(all_results, ensure_ascii=False, indent=2))
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
