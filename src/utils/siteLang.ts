import type { Lang } from "@/utils/i18n";

/** English listings live under /en/. Post URLs stay /posts/zh and /posts/en. */
export function langFromPathname(pathname: string): Lang {
  const path = pathname.replace(/\/+$/, "") || "/";
  const rest = path.replace(/^\/blog(?=\/|$)/, "") || "/";
  if (rest === "/en" || rest.startsWith("/en/")) return "en";
  if (rest === "/posts/en" || rest.startsWith("/posts/en/")) return "en";
  return "zh";
}
