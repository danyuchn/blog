#!/bin/zsh
# usage: render.sh in.html out.jpg [width=720]
# Shoots in.html at 2x with headless Chrome, trims bottom whitespace, saves jpg under ~400KB.
set -e
K=${0:A:h}
IN=${1:A}; OUT=${2:A}; W=${3:-720}
TMP=$(mktemp -d)
cp "$K/base.css" "${IN:h}/base.css" 2>/dev/null || true
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=$W,2400 --virtual-time-budget=8000 \
  --screenshot="$TMP/shot.png" "file://$IN" >/dev/null 2>&1
uv run -q --with pillow python3 -I "$K/crop.py" "$TMP/shot.png" "$OUT" 80
