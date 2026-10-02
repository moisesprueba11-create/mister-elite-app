# MISTER ÉLITE — Puesta en marcha en el PC (una sola vez)

Todo el sistema de crecimiento en Instagram + producción de Reels vive en este repo.
En el PC lo ejecuta el Claude que ya tiene ElevenLabs conectado.

## 1) Requisitos (Windows)
- Git, Python 3.10+ y ffmpeg:
  `winget install Git.Git Python.Python.3.12 Gyan.FFmpeg`  (cierra y reabre la terminal después)
- Claude Code (instalador oficial) con tu cuenta, y el conector de ElevenLabs activo.
- Dependencias de las animaciones:
  `pip install pillow cairosvg imageio imageio-ffmpeg numpy`
  (cairosvg en Windows necesita las librerías Cairo; si falla, pide a Claude que lo resuelva.)

## 2) Traer el proyecto
```
git clone https://github.com/moisesprueba11-create/mister-elite-app.git
cd mister-elite-app
git checkout ccr-aa605ed2-scpywy
claude
```
(Cuando se fusione la rama a `main`, bastará con `git pull` en `main`.)

## 3) Qué decirle a Claude en el PC
- Producir lo que dejó preparado la nube el lunes:
  > "git pull y produce los reels pendientes"
- Hacerlo todo en el PC (investigación + plan + animaciones + voz + montaje):
  > "Haz la semana completa de Instagram con las skills crecimiento-instagram y produccion-reels"
- Solo investigar y mejorar la estrategia:
  > "Haz una ronda de crecimiento-instagram"

## 4) Reglas
- En contenido público solo la marca **MISTER ÉLITE** (nunca el nombre personal).
- La voz es siempre la misma (ver `.claude/skills/produccion-reels/voz.md`).
- Nada se publica sin tu visto bueno.
- Los datos reales de la cuenta están en `.claude/skills/crecimiento-instagram/conocimiento/`.
