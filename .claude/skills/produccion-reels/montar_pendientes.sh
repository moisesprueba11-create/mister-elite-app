#!/usr/bin/env bash
# Para el PC (o cualquier sitio con ffmpeg): monta todos los Reels de reels/pendientes/*
# que ya tengan locucion.mp3 y los mueve a reels/listos/. Idempotente.
# Uso (desde la raíz del repo): .claude/skills/produccion-reels/montar_pendientes.sh
set -euo pipefail
RAIZ="$(git rev-parse --show-toplevel)"; cd "$RAIZ"
MONTAR=".claude/skills/produccion-reels/montar_reel.sh"
mkdir -p reels/pendientes reels/listos
shopt -s nullglob
for d in reels/pendientes/*/; do
  slug="$(basename "$d")"
  [ -f "$d/locucion.mp3" ] || { echo "· $slug: falta locucion.mp3 (pendiente de voz)"; continue; }
  [ -f "$d/clips.txt" ] || { echo "· $slug: falta clips.txt"; continue; }
  mapfile -t clips < <(grep -v '^\s*$' "$d/clips.txt")
  "$MONTAR" "reels/listos/reel-$slug.mp4" "$d/locucion.mp3" "${clips[@]}"
  cp "$d/caption.txt" "reels/listos/reel-$slug.caption.txt" 2>/dev/null || true
  mkdir -p reels/hechos; mv "${d%/}" "reels/hechos/$slug"
done
