#!/bin/sh
# Regenera el PDF de la presentación desde el HTML (mismo nombre, se sobrescribe).
set -e
DIR=$(cd "$(dirname "$0")" && pwd)
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
"$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --run-all-compositor-stages-before-draw --virtual-time-budget=8000 \
  --no-pdf-header-footer \
  --print-to-pdf="$DIR/presentacion-estrategias-estudio.pdf" \
  "$DIR/presentacion-estrategias-estudio.html"
