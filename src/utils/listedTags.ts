import { getCollection } from "astro:content";
import getUniqueTags from "@/utils/getUniqueTags";
import { filterByLang, type Lang } from "@/utils/i18n";

// Tags used only by archived posts get no tag page; callers render them unlinked.
const cache = new Map<Lang, Promise<Set<string>>>();

export function listedTagSet(lang: Lang): Promise<Set<string>> {
  let hit = cache.get(lang);
  if (!hit) {
    hit = getCollection("blog").then(
      posts => new Set(getUniqueTags(filterByLang(posts, lang)).map(t => t.tag))
    );
    cache.set(lang, hit);
  }
  return hit;
}
