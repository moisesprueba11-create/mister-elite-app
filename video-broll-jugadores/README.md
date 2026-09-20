# B-roll — Los cuatro jugadores aparecen en el campo

Clip de recurso: sobre el campo van apareciendo **de uno en uno** los cuatro
jugadores y se quedan, **lo más grandes que caben sin solaparse ni salirse de
cuadro**. El ritmo deja un hueco por jugador para nombrarlo en la locución.

## Entregables (nombres fijos, el build los sobrescribe)

| Archivo | Formato | Uso |
|---|---|---|
| `broll-jugadores.mp4` | 1080×1920, 30 fps, ~7,9 s | Reels / TikTok / Shorts (vertical) |
| `broll-jugadores-horizontal.mp4` | 1920×1080, 30 fps, ~7,9 s | YouTube / edición horizontal |
| `broll-jugadores-still.png` | 1080×1920 | Miniatura / portada |
| `broll-jugadores-horizontal-still.png` | 1920×1080 | Miniatura horizontal |

## Ritmo

| Tiempo | Qué pasa |
|---|---|
| 0,00–0,35 s | Solo el campo, con *push-in* lento |
| 0,35 s | Aparece el jugador 1 |
| 1,70 s | Aparece el jugador 2 |
| 3,05 s | Aparece el jugador 3 |
| 4,40 s | Aparece el jugador 4 |
| 4,85–7,85 s | Los cuatro en cuadro |

**1,35 s por jugador**: da para decir el nombre sin que se haga lento. Se ajusta
con `--paso` (p. ej. `--paso 1.6` si la locución va más pausada, `--paso 1.1` si
la quieres aún más rápida). Cada aparición dura 0,45 s: pequeño impulso hacia
arriba + fundido, sin cruzarse con los que ya están.

## Colocación

- **Vertical**: rejilla 2×2. El tamaño lo manda el ancho de media pantalla, así
  que los cuatro van a la misma altura, lo máximo que entra sin tocarse.
- **Horizontal**: los cuatro en línea, un cuarto de pantalla cada uno.

Las fotos están cortadas por la cintura, así que el corte inferior se difumina
y cada figura lleva sombra proyectada suave: no quedan torsos pegados sobre el
césped. El fondo se desenfoca y oscurece según entran, para que manden ellos.
Entra y sale a negro para encadenar con otros planos.

## Regenerar

```bash
python3 broll_jugadores.py                       # vertical 1080x1920
python3 broll_jugadores.py --formato h           # horizontal 1920x1080
python3 broll_jugadores.py --paso 1.6            # más tiempo por jugador
python3 broll_jugadores.py --nombres "Nombre1,Nombre2,Nombre3,Nombre4"
python3 broll_jugadores.py --escala 0.35 --fps 12   # prueba rápida de encuadre
```

Por defecto **no lleva rótulos**: el orden de aparición es el de los archivos
`assets/jugador-1.png` … `jugador-4.png`, que es el orden en que se enviaron las
fotos. Con `--nombres` se dibuja una placa con el nombre bajo cada jugador.

## Cambiar de jugadores

Las fotos de origen vienen con fondo oscuro o con un halo azul incrustado, así
que hay un paso previo de recorte:

```bash
python3 preparar_recortes.py foto1.jpg foto2.png foto3.png foto4.jpg
```

Segmenta la figura (`rembg`, modelo `u2net_human_seg`), rellena los huecos que la
máscara abre en el patrocinador del pecho, limpia el borde y guarda
`assets/jugador-N.png` en el orden de los argumentos. Para reordenar a los
jugadores basta con renombrar esos archivos.

Dependencias:

```bash
pip install pillow numpy scipy imageio imageio-ffmpeg "rembg[cpu]" onnxruntime
```

(`rembg`, `scipy` y `onnxruntime` solo hacen falta para `preparar_recortes.py`.)
