#!/usr/bin/env python3
"""Crawl the live blog and report broken links and redirect problems.

Stdlib only. Usage:
  python3 scripts/check-links.py [--root URL] [--external] [--workers N] [--out FILE]

Reports:
  - internal pages/assets returning 4xx/5xx (with the pages that link to them)
  - redirect loops and chains longer than one hop
  - links that point at a second host for the same site (e.g. github.io from agentcrew.cc)
  - with --external: outbound links that fail (4xx/5xx/timeouts)
Exit code 1 if any broken internal link or redirect loop is found.
"""
import argparse
import concurrent.futures as cf
import http.client
import json
import sys
import urllib.parse as up
from html.parser import HTMLParser

UA = "Mozilla/5.0 (compatible; blog-link-check/1.0)"
MAX_HOPS = 10


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for key in ("href", "src"):
            v = a.get(key)
            if not v:
                continue
            if tag == "link" and a.get("rel") in ("preconnect", "dns-prefetch"):
                continue
            self.found.append(v)


def request(url, method="GET", timeout=20):
    u = up.urlsplit(url)
    conn_cls = http.client.HTTPSConnection if u.scheme == "https" else http.client.HTTPConnection
    conn = conn_cls(u.netloc, timeout=timeout)
    path = u.path or "/"
    if u.query:
        path += "?" + u.query
    conn.request(method, path, headers={"User-Agent": UA, "Accept": "*/*"})
    r = conn.getresponse()
    body = r.read() if method == "GET" else b""
    conn.close()
    return r.status, r.getheader("Location"), r.getheader("Content-Type") or "", body


def resolve(url, method="GET"):
    """Follow redirects by hand. Returns (final_status, chain, loop, ctype, body)."""
    chain, seen = [url], {url}
    cur = url
    for _ in range(MAX_HOPS):
        try:
            status, loc, ctype, body = request(cur, method)
        except Exception as e:  # network error / timeout
            return f"ERR {type(e).__name__}", chain, False, "", b""
        if status in (301, 302, 303, 307, 308) and loc:
            nxt = up.urljoin(cur, loc)
            if nxt in seen:
                chain.append(nxt)
                return status, chain, True, ctype, b""
            seen.add(nxt)
            chain.append(nxt)
            cur = nxt
            continue
        return status, chain, False, ctype, body
    return "TOO_MANY_HOPS", chain, True, "", b""


def norm(url):
    u = up.urlsplit(url)
    return up.urlunsplit((u.scheme, u.netloc, u.path, u.query, ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="https://www.agentcrew.cc/blog/")
    ap.add_argument("--alias", action="append", default=["danyuchn.github.io"],
                    help="other hosts serving the same site (flagged when linked)")
    ap.add_argument("--external", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out")
    args = ap.parse_args()

    root = up.urlsplit(args.root)
    prefix = root.path if root.path.endswith("/") else root.path + "/"

    def internal(u):
        s = up.urlsplit(u)
        return s.netloc == root.netloc and (s.path + "/").startswith(prefix)

    pages, queue, results = set(), [args.root], {}
    referrers = {}  # url -> set of pages linking to it
    external, alias_links = {}, []

    while queue:
        batch = [u for u in dict.fromkeys(queue) if u not in results]
        queue = []
        with cf.ThreadPoolExecutor(args.workers) as ex:
            for u, res in zip(batch, ex.map(resolve, batch)):
                results[u] = res
                status, chain, loop, ctype, body = res
                if status != 200 or "text/html" not in ctype:
                    continue
                final = chain[-1]
                if not internal(final):
                    continue
                pages.add(final)
                p = Links()
                try:
                    p.feed(body.decode("utf-8", "replace"))
                except Exception:
                    continue
                for href in p.found:
                    if href.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
                        continue
                    absu = norm(up.urljoin(final, href))
                    s = up.urlsplit(absu)
                    if s.scheme not in ("http", "https"):
                        continue
                    if any(s.netloc.endswith(a) for a in args.alias):
                        alias_links.append((final, absu))
                    if internal(absu):
                        referrers.setdefault(absu, set()).add(final)
                        if absu not in results:
                            queue.append(absu)
                    elif s.netloc != root.netloc:
                        external.setdefault(absu, set()).add(final)
                    else:
                        referrers.setdefault(absu, set()).add(final)
                        if absu not in results:
                            res = resolve(absu, "HEAD")
                            if res[0] in (403, 405, 501):  # servers that refuse HEAD
                                res = resolve(absu, "GET")
                            results[absu] = res
        print(f"crawled {len(results)} urls, {len(pages)} html pages", file=sys.stderr)

    broken, loops, chains = [], [], []
    for u, (status, chain, loop, _, _) in results.items():
        if loop:
            loops.append({"url": u, "chain": chain})
        elif len(chain) > 2:
            chains.append({"url": u, "chain": chain})
        if status != 200 and not loop:
            broken.append({"url": u, "status": status, "chain": chain,
                           "from": sorted(referrers.get(u, []))[:5]})

    ext_broken = []
    if args.external:
        urls = list(external)
        with cf.ThreadPoolExecutor(args.workers) as ex:
            for u, res in zip(urls, ex.map(lambda x: resolve(x, "GET"), urls)):
                status, chain, loop, _, _ = res
                bad = loop or not (isinstance(status, int) and status < 400)
                # many sites block bots with 403/429; report them separately
                if bad:
                    ext_broken.append({"url": u, "status": status, "loop": loop,
                                       "from": sorted(external[u])[:3]})

    report = {
        "root": args.root,
        "pages": len(pages),
        "urls_checked": len(results),
        "external_links": len(external),
        "broken_internal": broken,
        "redirect_loops": loops,
        "redirect_chains": chains,
        "alias_host_links": [{"from": f, "to": t} for f, t in alias_links][:50],
        "alias_host_link_count": len(alias_links),
        "broken_external": ext_broken,
    }
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(text)
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in report.items()},
                     ensure_ascii=False))
    sys.exit(1 if broken or loops else 0)


if __name__ == "__main__":
    main()
