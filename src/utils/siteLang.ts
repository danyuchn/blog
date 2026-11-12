import { SITE } from "@/config";
import type { Lang } from "@/utils/i18n";
import { withBase } from "@/utils/withBase";

/** English listings live under /en/. Post URLs stay /posts/zh and /posts/en. */
export function langFromPathname(pathname: string): Lang {
  const path = pathname.replace(/\/+$/, "") || "/";
  const rest = path.replace(/^\/blog(?=\/|$)/, "") || "/";
  if (rest === "/en" || rest.startsWith("/en/")) return "en";
  if (rest === "/posts/en" || rest.startsWith("/posts/en/")) return "en";
  return "zh";
}

export function homePath(lang: Lang): string {
  return lang === "en" ? "/en/" : "/";
}

export function postsPath(lang: Lang, page = 1): string {
  const base = lang === "en" ? "/en/posts" : "/posts";
  return page > 1 ? `${base}/${page}/` : `${base}/`;
}

export function tagsPath(lang: Lang): string {
  return lang === "en" ? "/en/tags/" : "/tags/";
}

export function tagPagePath(lang: Lang, tag: string, page = 1): string {
  const base = `${lang === "en" ? "/en" : ""}/tags/${tag}`;
  return page > 1 ? `${base}/${page}/` : `${base}/`;
}

export function absoluteSiteUrl(sitePath: string): string {
  const url = new URL(withBase(sitePath), SITE.website);
  if (!url.pathname.endsWith("/") && !/\.[a-z0-9]+$/i.test(url.pathname)) {
    url.pathname += "/";
  }
  return url.href;
}

/** zh-Hant, en, and x-default (zh) for a listing pair. Paths omit the /blog base. */
export function hreflangAlternates(zhPath: string, enPath: string) {
  const zh = absoluteSiteUrl(zhPath);
  const en = absoluteSiteUrl(enPath);
  return [
    { hreflang: "zh-Hant", href: zh },
    { hreflang: "en", href: en },
    { hreflang: "x-default", href: zh },
  ];
}
