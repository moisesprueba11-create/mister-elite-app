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
4. **Montaje**: `python montar_reel.py salida.mp4 locucion.mp3 clip1.mp4 [clip2.mp4 …]` (multiplataforma, Windows incluido) → 1080x1920, H.264/AAC,
   fondo de marca, firma "MISTER ÉLITE". Subtítulos quemados automáticos si hay `locucion.txt`. Para decidir ganchos: publicar variantes como **Trial Reels** (solo no seguidores, 72 h).
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
- [ ] Voz automática en la nube (la pone el Claude del PC con ElevenLabs) · [x] Subtítulos quemados (desde locucion.txt)
- [ ] Publicación automática y lectura de insights (falta autorizar Instagram en Make)

## Reparto nube ↔ PC (flujo definitivo)
El Claude del **PC** tiene ElevenLabs; la **nube** (rutina del lunes) no. El repo es el buzón:

**3 versiones de gancho SIEMPRE** (ver `crecimiento-instagram/modos/ganchos-ab.md`): cada Reel sale como A/B/C, mismo cuerpo, distinto gancho, para probar como Trial Reels.

**Nube (automático, lunes):** por cada Reel del plan crea `reels/pendientes/AAAA-MM-DD-<slug>/` con:
- `guion.md` — guion con tiempos.
- `ganchos.json` — los 3 ganchos (A opinión, B resultado, C curiosidad) con texto de pantalla y locución; `cuerpo.txt` — locución del cuerpo.
- `locucion.txt` — solo si el Reel NO usa variantes: texto limpio de locución (sin acotaciones ni nombre personal).
- `clips.txt` — una ruta de clip MP4 por línea (los clips animados ya renderizados, en esa carpeta o en `video-*/clips/`).
- `caption.txt` — caption listo (1ª línea ≤125 car., 1 CTA, 3-5 hashtags).
- `manychat.txt` — palabra clave del Reel, respuestas públicas y mensaje directo para pegar en ManyChat (ver `planes/manychat-*.md`).
Commit + push. Nada se publica.

**PC (Claude con ElevenLabs):** al decir "produce los reels pendientes":
1. `git pull` de la rama.
2. Para cada carpeta de `reels/pendientes/`: con `ganchos.json`, generar con ElevenLabs `gancho_A.mp3`, `gancho_B.mp3`, `gancho_C.mp3` (desde cada `locucion`) y `cuerpo.mp3` (desde `cuerpo.txt`); sin `ganchos.json`, generar `locucion.mp3` desde `locucion.txt`
   usando **siempre la misma voz de marca** (la que ya usa Moisés; anotar su nombre en `voz.md` la 1ª vez) y guardar `locucion.mp3` en esa carpeta.
3. Ejecutar `.claude/skills/produccion-reels/montar_reel.py --pendientes`, es decir `python .claude/skills/produccion-reels/montar_reel.py --pendientes` → deja `reels/listos/reel-<slug>.mp4` + caption.
4. Commit + push y avisar a Moisés para su visto bueno (1 min). Publicación: manual o por Make cuando esté autorizado.
Requisitos PC: `ffmpeg` instalado.

## Modo PC completo (todo en el PC, sin nube)
Si Moisés pide "haz la semana completa" desde el PC, el Claude del PC ejecuta TODO en una sesión:
1. Skill `crecimiento-instagram` (ronda de investigación + plan en `planes/`).
2. Renderizar los clips animados de cada pieza (motor `anim.py`).
3. Voz con ElevenLabs (voz de `voz.md`) → `locucion.mp3` por pieza.
4. `python .claude/skills/produccion-reels/montar_reel.py --pendientes` → `reels/listos/`.
5. Commit + push. Publicación solo con visto bueno de Moisés.
Marca pública: solo "MISTER ÉLITE", nunca el nombre personal.
