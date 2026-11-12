import { getCollection } from "astro:content";
import getPostsByTag from "@/utils/getPostsByTag";
import getUniqueTags from "@/utils/getUniqueTags";
import { getListedPosts } from "@/utils/getSortedPosts";
import { filterByLang, type Lang } from "@/utils/i18n";

/** Same page size the mixed list used, so each language still paginates. */
export const LIST_PAGE_SIZE = 100;

// Astro's paginate() is only available inside getStaticPaths. Keep the helper loosely typed.
type Paginate = (data: unknown[], args?: Record<string, unknown>) => unknown[];

function otherLang(lang: Lang): Lang {
  return lang === "zh" ? "en" : "zh";
}

export async function postListPaths(paginate: Paginate, lang: Lang) {
  const posts = await getCollection("blog", ({ data }) => !data.draft);
  const listed = getListedPosts(posts);
  const mine = filterByLang(listed, lang);
  const otherCount = filterByLang(listed, otherLang(lang)).length;
  const otherPageCount = Math.max(1, Math.ceil(otherCount / LIST_PAGE_SIZE));
  return paginate(mine, {
    pageSize: LIST_PAGE_SIZE,
    props: { otherPageCount },
  });
}

export async function tagListPaths(paginate: Paginate, lang: Lang) {
  const posts = await getCollection("blog");
  const mine = filterByLang(posts, lang);
  const other = filterByLang(posts, otherLang(lang));
  return getUniqueTags(mine).flatMap(({ tag, tagName }) => {
    const tagPosts = getPostsByTag(mine, tag);
    const otherCount = getPostsByTag(other, tag).length;
    return paginate(tagPosts, {
      params: { tag },
      props: {
        tagName,
        otherCount,
        otherPageCount: Math.max(1, Math.ceil(otherCount / LIST_PAGE_SIZE)),
      },
      pageSize: LIST_PAGE_SIZE,
    });
  });
}