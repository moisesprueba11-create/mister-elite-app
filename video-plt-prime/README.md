# Reel PLT Prime — recortes sin tomas a cámara

Se han despiezado los dos reels verticales (1080×1920, 30 fps, ~22 s) y se han
**eliminado todas las tomas en las que el entrenador sale mirando a cámara**, tanto las
que llevan cartel/rótulo superpuesto («DEL MINUTO 70 AL MINUTO 90») como las limpias,
sin cartel. Lo que queda son únicamente las tomas de entrenamiento en el gimnasio.

## Mapa de tomas

### `reel_plt_prime.mp4` (v1) — 22,15 s

| Toma | Rango | Contenido | Acción |
|------|-------|-----------|--------|
| 1 | 0,000 – 1,300 | Entrenador a cámara **con cartel** | ❌ fuera |
| 2 | 1,300 – 5,033 | Sala de jaulas, plano general | ✅ clip 01 |
| 3 | 5,033 – 7,333 | Entrenador a cámara **con cartel** | ❌ fuera |
| 4 | 7,333 – 10,100 | Sentadilla, corrección del entrenador | ✅ clip 02 |
| 5 | 10,100 – 12,700 | Entrenador a cámara **con cartel** | ❌ fuera |
| 6 | 12,700 – 20,133 | Hinge / peso muerto rumano | ✅ clip 03 |
| 7 | 20,133 – 22,150 | Entrenador a cámara **con cartel** | ❌ fuera |

### `reel_plt_prime_v2.mp4` (v2) — 22,00 s

| Toma | Rango | Contenido | Acción |
|------|-------|-----------|--------|
| 1 | 0,000 – 3,000 | Entrenador a cámara **sin cartel** | ❌ fuera |
| 2 | 3,000 – 4,000 | Entrenador a cámara **con cartel** | ❌ fuera |
| 3 | 4,000 – 11,500 | Jaula, asistencia en sentadilla | ✅ clip v2-01 |
| 4 | 11,500 – 14,300 | Entrenador a cámara **con cartel** | ❌ fuera |
| 5 | 14,300 – 20,000 | Sentadilla frontal | ✅ clip v2-02 |
| 6 | 20,000 – 22,000 | Entrenador a cámara **sin cartel** | ❌ fuera |

Los cortes son limpios (cortes duros, sin fundidos): se midió la luminancia fotograma a
fotograma en los bordes y no hay transiciones que arrastren rótulo ni oscurecimiento.

## Entregables

### Recortes sueltos — `clips/`

| Archivo | Duración |
|---------|----------|
| `reel-plt-prime-01-jaulas-plano-general.mp4` | 3,73 s |
| `reel-plt-prime-02-sentadilla-correccion.mp4` | 2,80 s |
| `reel-plt-prime-03-hinge-peso-muerto.mp4` | 7,43 s |
| `reel-plt-prime-v2-01-jaula-asistencia-sentadilla.mp4` | 7,50 s |
| `reel-plt-prime-v2-02-sentadilla-frontal.mp4` | 5,70 s |

### Montajes

| Archivo | Contenido | Duración |
|---------|-----------|----------|
| `reel-plt-prime-SIN-camara.mp4` | v1 sin las tomas a cámara | 13,99 s |
| `reel-plt-prime-v2-SIN-camara.mp4` | v2 sin las tomas a cámara | 13,22 s |
| `reel-plt-prime-TODAS-las-tomas.mp4` | los 5 recortes seguidos | 27,19 s |

## Notas técnicas

- Codificación: H.264 `libx264`, CRF 18, `yuv420p`, perfil High, 30 fps, `+faststart`.
  Formato vertical 1080×1920 intacto, apto para Reels / TikTok / Shorts.
- Se conserva el audio original (cama musical continua, AAC 160 kb/s). Si los recortes se
  van a usar como *b-roll* bajo otra locución, basta con silenciarlos al montar.
- Los cortes son exactos al fotograma, con reencodificación (no *stream copy*), así que no
  hay fotogramas de arrastre de la toma anterior.

---
MISTER ÉLITE — Moisés Díaz
