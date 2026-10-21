#!/bin/bash
# PostToolUse hook (Write|Edit): after a markdown file under src/data/blog is
# written, run scripts/validate-content.mjs and report only the errors that
# mention that file. Exit 2 puts the errors in front of Claude; otherwise 0.
set -u
input="$(cat)"
file="$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)"
[ -n "$file" ] || exit 0
case "$file" in
  */src/data/blog/*.md) ;;
  *) exit 0 ;;
esac
root="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$root" || exit 0
base="$(basename "$file")"
out="$(node scripts/validate-content.mjs 2>&1)"
hits="$(printf '%s\n' "$out" | grep '^ERROR' | grep -F -- "$base")"
if [ -n "$hits" ]; then
  printf 'check:content errors for %s:\n%s\n' "$base" "$hits" >&2
  exit 2
fi
exit 0
