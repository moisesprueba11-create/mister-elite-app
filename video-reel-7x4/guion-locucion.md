# Reel — JUEGO DE POSICIÓN 7x4 · MISTER ÉLITE — Moisés Díaz

Reel vertical **1080x1920, 30 fps, 20 s exactos**: **15 s de explicación + 5 s de CTA**.

| Archivo | Qué es |
|---|---|
| `reel-7x4.mp4` | **Máster mudo** (vídeo limpio, listo para ponerle tu voz o la locución) |
| `reel-7x4-voz-provisional.mp4` | Mismo vídeo con una **voz robótica de guía** (solo para comprobar la sincronía; **no publicar**) |
| `portada-7x4.png` / `cierre-7x4.png` | Miniatura y fotograma de cierre |
| `reel_7x4.py` + `lib/board.py` | Motor de la animación (reproducible y editable) |
| `montar-voz.sh` / `montar-voz.bat` | Pegan la locución definitiva al máster mudo |

---

## 1 · Locución (voz en off)

Texto exacto, grabado a ~2,4 palabras/s. La animación está **clavada a estas marcas**:
cada rótulo entra con su palabra.

### Bloque 1 — explicación (0 → 15 s)

> «**Juego de posición, siete contra cuatro: cuatro zonas y dos porterías.
> Laterales, medio centro y medias puntas.
> Trabajamos salida de balón y mantenimiento.
> Si la pierden, presión tras pérdida: recuperar en cinco segundos.**»

| s | Voz | Qué pasa en pantalla |
|---|---|---|
| 0,2 – 1,2 | «Juego de posición,» | entra la cabecera y se dibuja el cuadrado de 4 zonas |
| 1,5 – 2,4 | «siete contra cuatro:» | aparecen los **7 rojos** y, detrás, los **4 azules** |
| 3,0 – 4,7 | «cuatro zonas y dos porterías» | se iluminan ZONA 1-4 y las **dos porterías** |
| 5,2 – 7,6 | «Laterales, medio centro y medias puntas» | salen las etiquetas de posición |
| 8,1 – 10,1 | «Trabajamos salida de balón y mantenimiento» | **circulación**: central → lateral → medio centro → media punta → cambio de orientación |
| 10,5 – 11,1 | «Si la pierden,» | el azul **roba** y sale (rótulo rojo «¡Pérdida!») |
| 11,3 – 12,4 | «presión tras pérdida:» | **tres flechas rojas** convergen sobre el balón |
| 12,9 – 14,6 | «recuperar en cinco segundos» | **cuenta atrás** alrededor del balón y «RECUPERADA» |

### Bloque 2 — CTA (15 → 20 s)

> «**Curso completo de juego de posición en Mister Élite, con Moisés Díaz.**»

En pantalla: MISTER ÉLITE · Moisés Díaz · *Juego de posición / Rondos / Sistemas de juego* ·
botón **CURSO COMPLETO** · «PDF + web · del concepto al campo».

---

## 2 · Cómo ponerle la voz definitiva

La locución ya está generada con voz española profesional (HeyGen, *Carlos Claro –
Broadcaster*, es-ES). **Este entorno no puede descargar los WAV** (el proxy de red bloquea
el dominio de HeyGen), así que se descargan desde tu navegador:

- Explicación (14,8 s):
  https://resource2.heygen.ai/text_to_speech/31bb9eb930c645b2a5d4657a8946cfa1/398936ac428244c6966feefe6d151c6a/id=b3554d96-34df-46a8-b2f6-ecf78a7c089f.wav
- CTA (4,4 s):
  https://resource2.heygen.ai/text_to_speech/31bb9eb930c645b2a5d4657a8946cfa1/398936ac428244c6966feefe6d151c6a/id=69844926-9ae8-4206-820f-a418c1c5ffe7.wav

> Los enlaces de HeyGen caducan con el tiempo: si dan error, se regeneran en un momento.

Después:

1. Guarda los dos archivos en `video-reel-7x4/audio/` como `voz-explicacion.wav` y `voz-cta.wav`.
2. Ejecuta `bash montar-voz.sh` (o doble clic en `montar-voz.bat` en Windows).
   Opcional con música: `bash montar-voz.sh musica.mp3` (la deja a -18 dB bajo la voz).
3. Sale `reel-7x4-final.mp4`, listo para publicar.

**Mejor todavía: grábalo con tu voz.** El texto es corto y las marcas de arriba te dan el
ritmo exacto; tu voz da marca. Mismo montaje con el mismo script.

---

## 3 · La tarea, para el campo

**JUEGO DE POSICIÓN 7 vs 4 · salida de balón, mantenimiento y presión tras pérdida**

- **Espacio**: 30x25 m dividido en **4 zonas** iguales, con **portería pequeña en cada fondo**.
- **Jugadores**: 7 atacantes + 4 defensores (uno por zona) + porteros si los hay.
- **Posiciones de los 7**: 2 centrales en la línea de fondo (salida), 2 laterales en las
  bandas sobre la línea central, 1 medio centro en el cruce de las cuatro zonas y
  2 medias puntas en la línea de arriba.
- **Normas**:
  1. Cada jugador **vive en su posición**; solo el medio centro se mueve entre zonas.
  2. **Máximo 2 toques** por fuera, **libre** el medio centro.
  3. Se empieza **siempre desde los centrales** (salida de balón).
  4. **Punto**: 8 pases seguidos, o pase interior al medio centro + cambio de orientación.
  5. **Al perderla: presión tras pérdida**. Si no la recuperan en **5 s**, los 4 defensores
     finalizan en cualquiera de las dos porterías.
  6. **Rotación**: el que pierde el balón entra a defender.
- **Puntos de coaching**: perfil abierto antes de recibir · fijar al defensor antes de pasar ·
  buscar al hombre libre entre líneas · cambiar de orientación cuando la presión se acumula ·
  reacción de los tres más cercanos al perderla.
- **Variantes**: 7v4 con comodín exterior · limitar a 1 toque a los de fuera ·
  premiar doble el gol tras recuperación en 5 s.

---

## 4 · Copy para el post

> **Juego de posición 7x4** 🟨
> Cuatro zonas, dos porterías y un objetivo: salir jugando, mantener y —si la pierdes—
> apretar en 5 segundos.
> Laterales, medio centro y medias puntas: cada uno en su posición, cada uno en su zona.
> Guárdalo y llévatelo al entrenamiento. ⚽️
>
> MISTER ÉLITE — Moisés Díaz · del concepto al campo
>
> #juegodeposicion #entrenadoresdefutbol #futbolbase #tacticafutbol #misterelite
> #entrenamientofutbol #presióntrasperdida #salidadebalon

---

## 5 · Reproducir o retocar la animación

```bash
cd video-reel-7x4
python3 reel_7x4.py          # regenera reel-7x4.mp4 + portada + cierre
```

Todo el guion visual vive en `reel_7x4.py`: los tiempos (`T_BUILD`, `T_LOSS`, `T_PRESS`…),
el recorrido del balón (`BALL_KF`), los movimientos de los defensores (`DEF_KF`) y los
rótulos (`caps`). `lib/board.py` es el motor de dibujo (césped, porterías, zonas, discos,
flechas, chips y cierre de marca) y sirve para los siguientes reels.
