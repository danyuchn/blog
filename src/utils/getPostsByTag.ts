import type { CollectionEntry } from "astro:content";
import { getListedPosts } from "./getSortedPosts";
import { slugifyAll } from "./slugify";

const getPostsByTag = (posts: CollectionEntry<"blog">[], tag: string) =>
  getListedPosts(
    posts.filter(post => slugifyAll(post.data.tags).includes(tag))
  );

export default getPostsByTag;
