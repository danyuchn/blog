#!/bin/bash
# PostToolUse hook (apply_patch|Write|Edit|MultiEdit): after a markdown file under
# src/data/blog is written, run scripts/validate-content.mjs and report only the
# errors that mention that file. Exit 2 puts the errors in front of Codex; otherwise 0.
# Codex track of .claude/hooks/validate-content.sh: apply_patch carries paths in the
# patch headers (`*** Add|Update File: <path>`), not in tool_input.file_path.
set -u
input="$(cat)"
files="$(printf '%s' "$input" | jq -r '
  (.tool_input | if type == "object" then (.file_path // empty) else empty end),
  ((.tool_input | if type == "string" then . elif type == "object" then (.patch // .input // "") else "" end)
    | split("\n")[] | capture("^\\*\\*\\* (Add|Update) File:\\s*(?<p>.+?)\\s*$").p? // empty)
' 2>/dev/null)"
[ -n "$files" ] || exit 0
root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$root" || exit 0
bases=""
while IFS= read -r f; do
  case "$f" in
    */src/data/blog/*.md|src/data/blog/*.md) bases="$bases$(basename "$f")"$'\n' ;;
  esac
done <<<"$files"
[ -n "$bases" ] || exit 0
out="$(node scripts/validate-content.mjs 2>&1)"
hits=""
while IFS= read -r base; do
  [ -n "$base" ] || continue
  h="$(printf '%s\n' "$out" | grep '^ERROR' | grep -F -- "$base")"
  [ -n "$h" ] && hits="$hits$h"$'\n'
done <<<"$bases"
if [ -n "$hits" ]; then
  printf 'check:content errors:\n%s' "$hits" >&2
  exit 2
fi
exit 0
