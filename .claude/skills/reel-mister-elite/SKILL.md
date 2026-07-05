---
name: reel-mister-elite
description: >-
  Convierte un vídeo o animación de un ejercicio/tarea (pizarra táctica, rondo,
  jugada animada, grabación real de campo...) en un reel vertical 9:16 con la
  marca MISTER ÉLITE, sin deformar ni recortar el vídeo original: tarjeta de
  intro, franjas de marca/CTA arriba y abajo durante el vídeo, y tarjeta de
  cierre. Úsala cuando el usuario suba un vídeo y pida "conviértemelo en un
  reel", "móntame esto en un reel para Mister Élite", "hazme un reel de este
  vídeo/animación", etc.
---

# Reel MISTER ÉLITE a partir de un vídeo/animación

Toma un vídeo que te pasa el usuario (grabación real, o una animación de una app
de pizarra táctica tipo TacticalPad) y lo convierte en un reel vertical listo
para Instagram/TikTok/YouTube Shorts, con la identidad MISTER ÉLITE.

## 0) Entorno (una vez por sesión)

Este entorno normalmente NO trae `ffmpeg` de sistema ni las libs de Python.
No instales `ffmpeg` con `apt` (suele fallar por dependencias rotas de vídeo/audio
del sistema y es lento). Usa el binario estático de `imageio-ffmpeg`:

```
pip install imageio-ffmpeg cairosvg pillow imageio numpy
python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
```

Guarda esa ruta (`$FF`) y úsala en vez de `ffmpeg` a pelo.

## 1) Inspecciona el vídeo fuente

```
$FF -i "$SRC" 2>&1 | grep -E "Duration|Stream"
```

Extrae 1 fps a PNG y **lee 2-3 fotogramas con la tool `Read`** para ver de qué
ejercicio se trata (nº de jugadores, relación numérica, elementos como mini-porterías).
Esto te da el texto real para el título/subtítulo de las tarjetas — no lo inventes
sin mirar el vídeo.

## 2) Pregunta lo que sea genuinamente ambiguo (una vez)

Con `AskUserQuestion`, si no está ya claro por instrucciones previas del usuario:
- Formato: vertical 9:16 (recomendado, por defecto) / cuadrado 1:1 / mantener horizontal.
- Audio: mantener el original tal cual / silenciar / silenciar + música de fondo.
- Entrega: solo `SendUserFile` (el usuario lo guarda en su móvil) o también commitear
  al repo (en cuyo caso sigue la convención `video-curso-<slug>/reel-<slug>.mp4`,
  ver ejemplos existentes `video-curso-1433/reel-1433.mp4`, `video-curso-posesion/reel-posesion.mp4`).

No hace falta volver a preguntar si el usuario ya fijó estas preferencias en una
sesión anterior de este mismo hilo.

## 3) Genera las tarjetas + monta el vídeo

Copia `assets/build_reel.py` a un scratchpad, edita el `CONFIG` de arriba (textos,
ruta del vídeo fuente, nombre de salida) y ejecútalo. El script:
- Calcula el escalado a ancho completo (sin recortar/deformar) y centra el vídeo
  verticalmente sobre un lienzo navy 1080×1920.
- Genera con `cairosvg` tres PNG: `intro.png`, `outro.png` (tarjetas completas) y
  `overlay.png` (transparente, solo las franjas de marca arriba/abajo — el hueco
  central donde va el vídeo se deja SIN dibujar nada).
- Monta con un único `filter_complex` de ffmpeg: intro + (vídeo + overlay) + outro,
  concatenados con audio incluido.

### Gotcha crítico (ya nos pasó una vez — cuesta ~2 min de cuelgue descubrirlo)
Cualquier input de imagen con `-loop 1` que se use en un `overlay`/`concat` **debe**
llevar `-t <duración>` (o `-frames:v`) explícito. Sin duración, `image2`/`loop` es
infinito y el filtro `overlay` (con `shortest=0` por defecto) puede quedarse
esperando para siempre → ffmpeg nunca termina y el proceso queda colgado (revisa
con `ps aux | grep ffmpeg` y mata el proceso si esto pasa). El script de
`assets/build_reel.py` ya acota el overlay a la duración del vídeo fuente + margen,
y además pone `overlay=...:shortest=1` por seguridad — si tocas el filtro, mantén
ambas cosas.

## 4) Verifica antes de entregar

Extrae 1 fps del resultado final y **lee con `Read` al menos 3 fotogramas**
(intro, un fotograma central con el vídeo, y el de cierre). Comprueba:
- Que el vídeo no está recortado ni deformado (aspecto original intacto).
- Que el texto de marca es legible y no se solapa con el vídeo.
- **Que NO aparece el nombre personal del usuario en ningún sitio** — solo
  "MISTER ÉLITE" (ver regla de marca en `CLAUDE.md`). Repásalo también en los
  metadatos del mp4 si tienes dudas (`grep -a -o -i "mois[a-z]*" archivo.mp4`).

## 5) Entrega

`SendUserFile` del mp4 final. Si además pide copy para publicarlo, escribe
título + descripción + hashtags en español, tono MISTER ÉLITE ("del concepto al
campo", poca teoría/mucha práctica), y el CTA de enlace en bio si el usuario te
da su dominio/perfil.

## Paleta y estilo (fijos — no cambian entre reels)

| Elemento | Valor |
|---|---|
| Fondo | `#0c1b2a` (navy) |
| Acento / barras | `#f7c948` (dorado) |
| Marca / eyebrow | `#7fd0ff` (cian) |
| Títulos | `#ffffff` (blanco), peso 900 |
| Texto secundario / pie | `#8aa0b6` (gris azulado) |
| Fuente | DejaVu Sans (soporta acentos ES; disponible sin instalar nada) |

Coherente con la estética ya usada en `video-curso-1433/anim.py` (`title_card()`).
