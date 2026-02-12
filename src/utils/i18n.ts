import type { CollectionEntry } from "astro:content";

export type Lang = "en" | "zh";
export const DEFAULT_LANG: Lang = "zh";

/** Extract language from a post's filePath (e.g. "src/data/blog/zh/foo.md" → "zh") */
export function getLangFromPost(post: CollectionEntry<"blog">): Lang {
  const match = post.filePath?.match(/\/blog\/(en|zh)\//);
  return (match?.[1] as Lang) ?? DEFAULT_LANG;
}

/** Filter posts by language */
export function filterByLang(
  posts: CollectionEntry<"blog">[],
  lang: Lang
): CollectionEntry<"blog">[] {
  return posts.filter(post => getLangFromPost(post) === lang);
}

/**
 * Find the translation counterpart of a post.
 * Convention: zh/hello-world ↔ en/hello-world (same filename, different lang dir)
 */
export function findTranslation(
  post: CollectionEntry<"blog">,
  allPosts: CollectionEntry<"blog">[]
): CollectionEntry<"blog"> | undefined {
  const lang = getLangFromPost(post);
  const targetLang: Lang = lang === "zh" ? "en" : "zh";
  const filename = post.filePath?.split("/").pop(); // e.g. "hello-world.md"
  if (!filename) return undefined;

  return allPosts.find(p => {
    const pLang = getLangFromPost(p);
    const pFilename = p.filePath?.split("/").pop();
    return pLang === targetLang && pFilename === filename;
  });
}
