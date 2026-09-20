# B-roll — El entrenador sobre el campo

Clip de recurso (b-roll) para montar debajo de locución o rótulos: el entrenador
**sube desde abajo** sobre el campo hasta **centrarse y quedar protagonista**.

## Entregables (nombres fijos, el build los sobrescribe)

| Archivo | Formato | Uso |
|---|---|---|
| `broll-entrenador.mp4` | 1080×1920, 30 fps, 8 s | Reels / TikTok / Shorts (vertical) |
| `broll-entrenador-horizontal.mp4` | 1920×1080, 30 fps, 8 s | YouTube / edición horizontal |
| `broll-entrenador-still.png` | 1080×1920 | Miniatura / portada |
| `broll-entrenador-horizontal-still.png` | 1920×1080 | Miniatura horizontal |

## Cómo está animado

1. **0,0–0,5 s — establecimiento.** Solo el campo, con un *push-in* lento y continuo.
2. **0,5–3,7 s — entrada.** El entrenador entra desde fuera de cuadro (abajo) y sube
   con `ease-out` hasta su posición, creciendo de 0,90× a 1,00×: da sensación de
   acercarse a cámara, no de deslizarse.
3. **3,7–8,0 s — protagonismo.** Queda centrado en el eje del campo. El fondo se
   desenfoca (profundidad de campo), se oscurece un 14 % y la viñeta se cierra, de
   modo que la mirada va a él. Micro-movimiento (respiración + 1,035× de deriva)
   para que el plano no quede congelado.

Entra y sale a negro (0,4 s) para encadenar con otros planos en el montaje.

Detalles de acabado: el PNG original traía un reborde claro del recorte, así que el
script erosiona 1 px de alfa y descontamina el color del borde con el color interior;
además se compone una sombra proyectada suave para despegar la figura del césped.

## Regenerar

```bash
python3 broll_entrenador.py                    # vertical 1080x1920, 8 s
python3 broll_entrenador.py --formato h        # horizontal 1920x1080
python3 broll_entrenador.py --dur 12 --fps 30  # otra duración
python3 broll_entrenador.py --escala 0.35 --fps 12   # prueba rápida de encuadre
```

Dependencias: `pillow`, `numpy`, `imageio`, `imageio-ffmpeg`.

```bash
pip install pillow numpy imageio imageio-ffmpeg
```

Fuentes en `assets/`: `campo.jpg` (fondo) y `entrenador.png` (recorte con alfa).
Para cambiar de entrenador basta con sustituir `assets/entrenador.png` por otro PNG
con transparencia y volver a lanzar el script.
