---
name: produccion-reels
description: >-
  Produce los Reels y animaciones de tareas de MISTER ÉLITE de
  forma casi automática a partir del plan semanal de crecimiento: guion con
  gancho → animación táctica por código (anim.py) → locución (TTS) → montaje
  vertical 1080x1920 con marca → listo para publicar. Úsala cuando el usuario
  pida "hazme los reels de la semana", "produce el reel de X", "automatiza la
  producción", o desde la rutina semanal de crecimiento-instagram.
---

# Producción de Reels (casi automática)

Enlaza con `crecimiento-instagram`: allí se decide QUÉ publicar (plan semanal en
`.claude/skills/crecimiento-instagram/planes/`); aquí se PRODUCE.

**Regla de marca: en pantalla y en audio solo "MISTER ÉLITE". Nunca el nombre "Moisés Díaz"** (ni en la firma, ni en la locución, ni en el caption).

## Cadena
1. **Guion** (por pieza del plan): gancho elegido + 3-4 frases de locución (~2,5 palabras/seg) en
   el formato de `video-curso-1433/guion-locucion.md`. Cierre con CTA de comentario y de envío.
2. **Animación**: crear/reusar la escena con el motor `video-curso-*/anim.py` (`Scene`, `Actor`,
   `save_clip`; pizarra `lib/pitch.py`). Convención de dorsales/posiciones de `curso-tactico`.
   Dependencias: `pip install pillow cairosvg imageio imageio-ffmpeg numpy` (+ `ffmpeg`).
   Verificado en la nube: renderiza un clip de 54 frames en segundos.
3. **Locución**: TTS del guion → `locucion.mp3`. Proveedores:
   - ElevenLabs (el que ya usa Moisés): vía API key en secretos del entorno (`ELEVENLABS_API_KEY`) o
     generada en su chat y dejada en el repo.
   - Alternativas conectadas aquí: HeyGen `create_speech`, Higgsfield `generate_audio`.
   Usar SIEMPRE la misma voz (identidad de marca).
4. **Montaje**: `./montar_reel.sh salida.mp4 locucion.mp3 clip1.mp4 [clip2.mp4 …]` → 1080x1920, H.264/AAC,
   fondo de marca, firma "MISTER ÉLITE". Subtítulos: añadir como siguiente mejora.
5. **Revisión humana (1 min)**: Moisés mira el Reel, corrige si hace falta. Mientras no haya tasa
   de aprobación alta, NO se publica nada sin su visto bueno.
6. **Publicación** (cuando exista conexión válida de Instagram en Make): módulo `CreateAReelPost`,
   en horario 15:30-17:30 WEST, caption del plan (1ª línea ≤125 car., 1 CTA, 3-5 hashtags).
7. **Medición y aprendizaje**: los insights de cada pieza vuelven a `crecimiento-instagram`.

## Nombres de archivo (según CLAUDE.md)
Entregables de curso: nombres fijos, sin sufijos. Para Reels semanales usar `reel-AAAA-MM-DD-<slug>.mp4`
en `reels/` (no son entregables de curso; la fecha identifica cada pieza).

## Estado
- [x] Animaciones por código (existente) · [x] Montaje 1080x1920 (probado) · [x] Guion/plan
- [ ] Voz automática (falta conectar proveedor aquí) · [ ] Subtítulos quemados
- [ ] Publicación automática y lectura de insights (falta autorizar Instagram en Make)
