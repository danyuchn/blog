// Block publishing when a post contains a private person's or client's name.
// The denylist lives OUTSIDE this public repo (a list of client names would itself be a leak).
// Locally the list is required: missing list = exit 1, so the check can never silently pass.
// In CI (no list available) it is skipped with a notice.
import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join } from "node:path";
import { homedir } from "node:os";

const LIST =
  process.env.BLOG_PRIVATE_NAMES ||
  join(homedir(), "knowledge-base/reference/data/blog-private-names.txt");
const ROOT = "src/data/blog";

if (!existsSync(LIST)) {
  if (process.env.CI) {
    console.log(`check:private skipped in CI (no denylist at ${LIST})`);
    process.exit(0);
  }
  console.error(`check:private FAILED: denylist not found at ${LIST}`);
  process.exit(1);
}

const patterns = readFileSync(LIST, "utf8")
  .split("\n")
  .map(l => l.trim())
  .filter(l => l && !l.startsWith("#"))
  .map(l => new RegExp(l)); // case-sensitive: names are capitalised, so TAM/SAM/SOM does not trip "Sam"

const hits = [];
for (const lang of readdirSync(ROOT, { withFileTypes: true }).filter(d => d.isDirectory()).map(d => d.name)) {
  for (const f of readdirSync(join(ROOT, lang)).filter(n => n.endsWith(".md"))) {
    const path = join(ROOT, lang, f);
    readFileSync(path, "utf8")
      .split("\n")
      .forEach((line, i) => {
        // HTML comments are published in the page payload too, so they are scanned.
        const p = patterns.find(re => re.test(line));
        if (p) hits.push(`${path}:${i + 1}  [${p.source}]  ${line.slice(0, 100)}`);
      });
  }
}

if (hits.length) {
  console.error(`check:private — ${hits.length} hit(s); replace names with role descriptions:`);
  hits.forEach(h => console.error("  " + h));
  process.exit(1);
}
console.log(`check:private — ${patterns.length} patterns, 0 hits`);
