# Animación 1-3-4-3 · Salida de balón + STOP BALL

Animación táctica de MISTER ÉLITE — Moisés Díaz reconstruida a partir del vídeo de
referencia que pasó el míster (espacio rectangular por zonas, azules en 1-3-4-3).

## Qué se respeta del vídeo original

| Elemento | En la animación |
|---|---|
| Espacio | Rectángulo dividido en **5 zonas** (líneas verticales discontinuas) + **2 carriles exteriores** (líneas horizontales discontinuas), con conos en cada cruce |
| Zona objetivo | Banda verde rayada **STOP BALL** pegada al fondo de ataque (solo entre los dos carriles) |
| Porterías | **3 minipoterías** en el fondo propio, una por central |
| Equipo azul | **10 jugadores en 1-3-4-3 sin portero**: 5-6-4 (centrales), 2 y 3 (carrileros), 8 y 10 (interiores), 7-9-11 (arriba) |
| Equipo rojo | **8 jugadores** en 3-3-2: 11-9-7 (1.ª línea), 10-6-8 (2.ª línea), 4-5 (pareja de cierre) |
| Sentido | El azul ataca hacia la **izquierda**; el rojo, a la contra, hacia las minipoterías |
| Jugadas | Las **dos secuencias completas** del vídeo, pase a pase (ver abajo) |

## Las dos jugadas

**Jugada 1 — salida por dentro y finalización por el carril izquierdo (10 pases)**

`6 → 4 → 3 → 6 → 5 → 10 → 8 → 2 → 9 → 11 → STOP BALL`

El carrilero 3 sube al carril exterior para recibir, se vuelve atrás cuando no hay línea
de pase, se cambia la orientación con 5 y se rompe la primera presión con el pase entre
líneas a 10. Después: asociación de interiores, carrilero 2 ya alto, balón al punta y
descarga a un toque para que 11 pare el balón en la zona.

**Jugada 2 — pérdida, contra roja y segunda salida (12 pases)**

`6 → 5 → 4 → 3 → 10 → 3 → ✕ PÉRDIDA → contra roja (8-6-10-11-9 + tiro) → recupera 6 →
5 → 6 → 10 → 3 → 11 → 7 → STOP BALL`

Misma estructura, otra decisión: el cambio largo de 5 a 4 pasa por detrás de 6, hay pared
entre 3 y 10, y el pase hacia dentro se pierde. El rojo sale a la contra hasta el tiro a
la minipoertía, 6 corta y el azul vuelve a salir, esta vez cambiando de carril (11 → 7)
para terminar por arriba.

## Archivos

| Archivo | Para qué |
|---|---|
| `animacion-1343-stopball.mp4` | Vídeo 1080×1080 (≈38 s). Para redes y para la plataforma |
| `animacion-1343-stopball.gif` | Versión ligera en bucle |
| `animacion-1343-stopball.html` | **HTML único autocontenido**: animación en SVG con play/pausa, velocidad y salto a cada jugada. Se sube tal cual a WordPress |
| `stills/*.png` | Pizarras fijas (tarea, sistema, jugada 1, jugada 2, claves) para el curso |
| `jugadas_1343.py` | Coreografía: zonas, posiciones y todos los pases (única fuente de verdad) |
| `lib/board.py` | Motor de dibujo de la pizarra (PIL) |
| `anim.py` | Genera MP4 + GIF + stills |
| `build_html.py` | Genera el HTML a partir de la misma coreografía |

## Regenerar

```bash
pip install pillow imageio imageio-ffmpeg     # dependencias
python3 anim.py             # MP4 + GIF + stills
python3 anim.py --stills    # solo las pizarras fijas (rápido)
python3 build_html.py       # HTML autocontenido
```

Si se cambia algo en `jugadas_1343.py` (posiciones, tiempos, textos), el MP4 y el HTML
se regeneran los dos desde ahí, así que nunca se descuadran entre sí.

---
MISTER ÉLITE — Moisés Díaz
