/**
 * Content validator — blocking CI gate for src/data/blog.
 *
 * Enforces the machine-checkable rules from .claude/specs/:
 *   article-spec.md     — filename parity, slug, explicit frontmatter, past pubDatetime, image refs
 *   tags.md             — controlled tag vocabulary (parsed from the allowlist markers)
 *   micro-notes-spec.md — zh/en entry alignment, live-file cap
 * Also guards the byte-identity of .claude/content-workflow.md vs .codex/content-workflow.md.
 *
 * Usage: npm run check:content   (exit 1 on any error; warnings never block)
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { parse as parseYaml } from "yaml";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const BLOG = path.join(ROOT, "src/data/blog");
const LANGS = ["zh", "en"];
const MICRO_NOTES = [
  "ai-micro-notes.md",
  "ai-micro-notes-2026-archive.md",
  "ai-micro-notes-2025.md",
];
const MICRO_LIVE_CAP = 35;
const REQUIRED_EXPLICIT = ["author", "pubDatetime", "title", "slug", "featured", "draft", "description"];

const errors = [];
const warnings = [];
const err = (file, msg) => errors.push(`${file}: ${msg}`);
const warn = (file, msg) => warnings.push(`${file}: ${msg}`);

// --- tag allowlist from .claude/specs/tags.md ---
function loadAllowlist() {
  const specPath = path.join(ROOT, ".claude/specs/tags.md");
  const text = fs.readFileSync(specPath, "utf-8");
  const m = text.match(/<!-- tag-allowlist:start -->([\s\S]*?)<!-- tag-allowlist:end -->/);
  if (!m) {
    err(".claude/specs/tags.md", "tag-allowlist markers not found — format contract broken");
    return new Set();
  }
  const tags = new Set();
  for (const line of m[1].split("\n")) {
    const t = line.match(/^- `([a-z0-9-]+)`/);
    if (t) tags.add(t[1]);
  }
  if (tags.size === 0) err(".claude/specs/tags.md", "allowlist section parsed to zero tags");
  return tags;
}

function splitFrontmatter(raw, file) {
  const m = raw.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!m) {
    err(file, "no frontmatter block found");
    return null;
  }
  let data;
  try {
    data = parseYaml(m[1]);
  } catch (e) {
    err(file, `frontmatter YAML parse error: ${e.message.split("\n")[0]}`);
    return null;
  }
  return { data, body: raw.slice(m[0].length) };
}

const allowlist = loadAllowlist();
const now = new Date();
const files = {};
for (const lang of LANGS) {
  files[lang] = fs
    .readdirSync(path.join(BLOG, lang))
    .filter(f => f.endsWith(".md") && !f.startsWith("_"))
    .sort();
}

// 1. zh/en filename parity (translation pairing depends on identical filenames)
for (const [a, b] of [["zh", "en"], ["en", "zh"]]) {
  const other = new Set(files[b]);
  for (const f of files[a]) {
    if (!other.has(f)) err(`${a}/${f}`, `no ${b}/${f} counterpart — translation link will break`);
  }
}

// 2. per-file frontmatter + image refs
const microEntryCounts = {};
for (const lang of LANGS) {
  for (const fn of files[lang]) {
    const rel = `src/data/blog/${lang}/${fn}`;
    const parsed = splitFrontmatter(fs.readFileSync(path.join(BLOG, lang, fn), "utf-8"), rel);
    if (!parsed) continue;
    const { data, body } = parsed;
    const basename = fn.replace(/\.md$/, "");

    for (const field of REQUIRED_EXPLICIT) {
      if (!(field in data) || data[field] === null || data[field] === "") {
        err(rel, `missing explicit frontmatter field "${field}" (see .claude/specs/article-spec.md)`);
      }
    }
    if (data.slug && data.slug !== `${lang}/${basename}`) {
      err(rel, `slug "${data.slug}" must be "${lang}/${basename}"`);
    }
    if (data.pubDatetime) {
      const d = data.pubDatetime instanceof Date ? data.pubDatetime : new Date(data.pubDatetime);
      if (Number.isNaN(d.getTime())) {
        err(rel, `unparseable pubDatetime "${data.pubDatetime}"`);
      } else if (d > now) {
        err(rel, `pubDatetime ${d.toISOString()} is in the future — post gets silently filtered by postFilter.ts`);
      }
    }
    const tags = Array.isArray(data.tags) ? data.tags : [];
    for (const t of tags) {
      if (!allowlist.has(String(t))) {
        err(rel, `tag "${t}" not in .claude/specs/tags.md allowlist (add it there first, or pick an existing tag)`);
      }
    }
    if (tags.length < 2 || tags.length > 3) warn(rel, `${tags.length} tags (convention: 2–3)`);

    // image references must resolve to files under public/
    const refs = [...body.matchAll(/\]\((\/blog\/assets\/[^)\s]+)\)/g), ...body.matchAll(/src="(\/blog\/assets\/[^"]+)"/g)];
    for (const r of refs) {
      const publicPath = path.join(ROOT, "public", r[1].replace(/^\/blog\//, ""));
      if (!fs.existsSync(publicPath)) err(rel, `image reference ${r[1]} has no file at public/${r[1].replace(/^\/blog\//, "")}`);
    }

    if (MICRO_NOTES.includes(fn)) {
      microEntryCounts[`${lang}/${fn}`] = (body.match(/^\*\*.+\*\*\s*$/gm) ?? []).length;
    }
  }
}

// 3. micro-notes: zh/en entry alignment + live cap
for (const fn of MICRO_NOTES) {
  const zh = microEntryCounts[`zh/${fn}`];
  const en = microEntryCounts[`en/${fn}`];
  if (zh === undefined || en === undefined) continue; // parity check already reported
  if (zh !== en) {
    err(`src/data/blog/{zh,en}/${fn}`, `entry count mismatch zh=${zh} en=${en} — entries pair by index, edit both sides`);
  }
  if (fn === "ai-micro-notes.md" && zh > MICRO_LIVE_CAP) {
    err(`src/data/blog/zh/${fn}`, `live file has ${zh} entries (cap ${MICRO_LIVE_CAP}) — extract a cluster or archive stale entries`);
  }
}

// 4. dual-copy workflow doc must stay byte-identical
{
  const a = path.join(ROOT, ".claude/content-workflow.md");
  const b = path.join(ROOT, ".codex/content-workflow.md");
  if (fs.existsSync(a) && fs.existsSync(b)) {
    if (!fs.readFileSync(a).equals(fs.readFileSync(b))) {
      err(".claude/content-workflow.md", "diverged from .codex/content-workflow.md — copy the updated one over the other");
    }
  }
}

// --- report ---
for (const e of errors) console.error(`ERROR   ${e}`);
const shownWarnings = warnings.slice(0, 20);
for (const w of shownWarnings) console.warn(`warning ${w}`);
if (warnings.length > shownWarnings.length) console.warn(`warning …and ${warnings.length - shownWarnings.length} more warnings`);
console.log(`\ncheck:content — ${files.zh.length + files.en.length} posts, ${errors.length} error(s), ${warnings.length} warning(s)`);
if (errors.length > 0) process.exit(1);
