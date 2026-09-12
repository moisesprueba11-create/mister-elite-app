#!/usr/bin/env bash
# montar-voz.sh — pega la locución definitiva sobre el reel mudo.
#
#   1) Descarga los dos WAV de la locución (enlaces en guion-locucion.md)
#      y déjalos en esta carpeta como  audio/voz-explicacion.wav  y  audio/voz-cta.wav
#   2) Ejecuta:  bash montar-voz.sh
#      -> genera  reel-7x4-final.mp4  (1080x1920, 20 s, con voz)
#
# Requiere ffmpeg. En Windows: instala ffmpeg y usa montar-voz.bat
set -euo pipefail
cd "$(dirname "$0")"
V=reel-7x4.mp4
A1=audio/voz-explicacion.wav      # locución 0–15 s
A2=audio/voz-cta.wav              # locución del cierre (15–20 s)
OUT=reel-7x4-final.mp4
MUS=${1:-}                        # opcional: pista de música de fondo

FILTER="[1:a]adelay=150|150[a1];[2:a]adelay=15250|15250[a2];[a1][a2]amix=inputs=2:normalize=0[voz]"
if [ -n "$MUS" ]; then
  ffmpeg -y -i "$V" -i "$A1" -i "$A2" -i "$MUS" \
    -filter_complex "$FILTER;[3:a]volume=0.12,atrim=0:20,afade=t=out:st=18.5:d=1.5[mus];[voz][mus]amix=inputs=2:normalize=0,aresample=48000[a]" \
    -map 0:v -map "[a]" -t 20 -c:v copy -c:a aac -b:a 192k "$OUT"
else
  ffmpeg -y -i "$V" -i "$A1" -i "$A2" \
    -filter_complex "$FILTER;[voz]aresample=48000[a]" \
    -map 0:v -map "[a]" -t 20 -c:v copy -c:a aac -b:a 192k "$OUT"
fi
echo "listo -> $OUT"
