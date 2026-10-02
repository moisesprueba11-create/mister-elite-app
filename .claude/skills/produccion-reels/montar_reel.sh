#!/usr/bin/env bash
# Monta un Reel vertical 1080x1920 a partir de clips de animación (anim.py) + locución.
# Uso: montar_reel.sh salida.mp4 locucion.mp3 clip1.mp4 [clip2.mp4 ...]
# - Concatena los clips, los escala a ancho 1080 y los centra sobre fondo de marca (9:16).
# - Mezcla la locución; si la voz es más corta/larga que el vídeo, el vídeo manda (-shortest).
# - Añade marca MISTER ÉLITE — Moisés Díaz abajo.
set -euo pipefail
OUT="$1"; VOZ="$2"; shift 2
[ "$#" -ge 1 ] || { echo "faltan clips"; exit 1; }
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
: > "$TMP/lista.txt"
for c in "$@"; do echo "file '$(realpath "$c")'" >> "$TMP/lista.txt"; done
FONT="$(fc-match -f '%{file}' 'DejaVu Sans:bold' 2>/dev/null || true)"
DT=""
[ -n "$FONT" ] && DT=",drawtext=fontfile=${FONT}:text='MISTER ÉLITE — Moisés Díaz':fontcolor=0xD4AF37:fontsize=34:x=(w-text_w)/2:y=h-120"
ffmpeg -y -loglevel error -f concat -safe 0 -i "$TMP/lista.txt" -i "$VOZ" \
  -filter_complex "[0:v]scale=1080:-2:flags=lanczos,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0b0f14,fps=30${DT}[v]" \
  -map "[v]" -map 1:a -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest "$OUT"
echo "OK -> $OUT"
