import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import { getPath } from "@/utils/getPath";
import getSortedPosts from "@/utils/getSortedPosts";
import { SITE } from "@/config";

export async function GET() {
  const posts = await getCollection("blog");
  const sortedPosts = getSortedPosts(posts);
  const siteWithBase = import.meta.env.BASE_URL
    ? `${SITE.website}${import.meta.env.BASE_URL}`.replace(/\/$/, "")
    : SITE.website;
  return rss({
    title: SITE.title,
    description: SITE.desc,
    site: siteWithBase,
    items: sortedPosts.map(({ data, id, filePath }) => ({
      link: `${siteWithBase}${getPath(id, filePath)}`,
      title: data.title,
      description: data.description,
      pubDate: new Date(data.modDatetime ?? data.pubDatetime),
    })),
  });
}
