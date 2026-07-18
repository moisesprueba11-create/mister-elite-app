#!/usr/bin/env bash
# Descargar un YouTube Short en buena calidad con yt-dlp
# Uso: ./descargar-short.sh "https://youtube.com/shorts/XXXXXXXXXXX"
set -euo pipefail

URL="${1:-https://youtube.com/shorts/gccGKqb3LKM}"

# Asegura yt-dlp actualizado
command -v yt-dlp >/dev/null || { echo "Instala yt-dlp: pip install -U yt-dlp"; exit 1; }

# 1) Ver formatos disponibles
echo "== Formatos disponibles =="
yt-dlp -F "$URL"

# 2) Descargar la mejor calidad (video+audio, salida mp4)
echo "== Descargando en mejor calidad =="
yt-dlp -f "bestvideo+bestaudio/best" --merge-output-format mp4 \
  -o "short_video_hd.%(ext)s" "$URL"

echo "Listo: short_video_hd.mp4"
