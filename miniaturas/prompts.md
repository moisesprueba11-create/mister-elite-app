# Prompts — Miniaturas «1-4-3-3 vs 1-4-4-2: ¿qué sistema le conviene a tu equipo?»

> **Estado:** Higgsfield **no estaba disponible** en este entorno (sin conector/MCP). No se ha
> generado ninguna imagen con IA, ni hay `job_id`, ni se han gastado créditos.
> Los PNG entregados (`miniatura_01..03.png`) son **composiciones gráficas vectoriales**
> (SVG + HTML renderizado con Chromium a 1280×720) creadas con `_build/build.js`.
> Sirven como maqueta exacta de composición, texto y tácticas. Los prompts de abajo son los
> que se deben lanzar en Higgsfield para generar el **fondo fotográfico**. Después se superpone
> la capa gráfica de `build.js` (texto, fichas, líneas), que es la que garantiza la precisión.

## Parámetros comunes (para Higgsfield)

- Modelo: **pendiente**. Hay que elegirlo con `models_explore` (no se adivina el identificador).
  Buscar un modelo text-to-image fotorrealista que admita 16:9.
- Relación de aspecto: 16:9. Salida mínima de 1280×720 (reescalar o recortar a 1280×720 exactos).
- Antes de cada generación: `get_cost`. Presupuesto máximo total: 80 créditos. Plan: 3 generaciones
  iniciales y, como mucho, 1 o 2 iteraciones por concepto mientras el coste lo permita.
- Negativo (si el modelo lo admite): `text, letters, numbers, logos, club crests, jerseys with sponsors, famous players, faces, watermark, stadium crowd, match broadcast graphics, video game, cartoon`.
- **Nunca pedir al modelo texto, números ni fichas tácticas.** Todo eso se añade en la composición.

---

## Concepto 1 · El duelo táctico — `miniatura_01.png`

**Prompt de fondo (Higgsfield):**
```
Cinematic top-down aerial photograph of an empty, freshly cut football training pitch at dusk,
alternating dark green mowing stripes, crisp white lines, a thin strip of black shadow running
vertically through the exact center of the frame splitting it into two halves, left half slightly
brighter, right half slightly darker, subtle vignette, moody professional sports look,
black green and white color palette, no people, no text, 16:9
```

**Capa gráfica (composición, `build.js › concept1`):**
- Dos campos verticales esquemáticos con **11 fichas cada uno, portero incluido**.
  - Izquierda, fichas blancas: 1-4-3-3 (portero, 4 defensas, pivote + 2 interiores, 3 delanteros).
  - Derecha, fichas verdes #18c25a: 1-4-4-2 (portero, 4 defensas, 4 centrocampistas en línea, 2 delanteros).
- Encima de cada campo: «1-4-3-3» (blanco) y «1-4-4-2» (verde), en Nunito Black a 112 px con contorno oscuro.
- Medallón central «VS» verde con borde blanco.
- Texto principal: **«¿CUÁL ELIGES?»** (1 línea, 98 px) sobre una franja negra translúcida.
- Marca «MISTER ÉLITE» pequeña, abajo a la izquierda.

## Concepto 2 · La elección del entrenador — `miniatura_02.png`

**Prompt de fondo (Higgsfield):**
```
Cinematic photograph from behind of an adult football coach seen only as a dark silhouette,
back to camera, head and shoulders in the lower-left third of the frame, standing in front of a
large dark green tactical whiteboard in a dim locker room, the board is blank and clean with no
drawings, soft green rim light on the coach's shoulders, shallow depth of field, black and deep green
tones, realistic, no face visible, no text, 16:9
```
*(Si se quiere usar a Moisés: sustituir la silueta genérica por sus fotos de referencia de `inputs/cara/`.
Esa carpeta no existía en esta sesión, así que se ha dejado una silueta anónima sin rostro.)*

**Capa gráfica (`build.js › concept2`):**
- Sobre la pizarra, dos campos con **11 fichas cada uno** (1-4-3-3 blanco / 1-4-4-2 verde) con su etiqueta encima.
- Entre ambos, un «¿?» verde grande.
- Texto principal en **2 líneas**: **«¿CUÁL TE / CONVIENE?»** (84 px), abajo a la derecha, sin tapar la pizarra.
- En la versión con fotografía, la silueta del entrenador procede del fondo generado.
  En la maqueta es una silueta vectorial.

## Concepto 3 · La batalla del centro — `miniatura_03.png`

**Prompt de fondo (Higgsfield):**
```
Cinematic low-angle wide photograph of the center circle and halfway line of an empty football
training pitch at night under floodlights, dark green grass with subtle mowing stripes, the center
circle area slightly brighter than the surroundings, heavy vignette toward the edges, a few orange
training cones out of focus in the far background, black green and white palette, realistic, no people,
no text, 16:9
```
*(Alternativa más legible: vista cenital del círculo central, igual que la maqueta.)*

**Capa gráfica (`build.js › concept3`):**
- **Detalle parcial** (no una formación completa): zona central resaltada con un rectángulo verde translúcido.
  - 3 fichas blancas = mediocampo del 1-4-3-3 (pivote + 2 interiores).
  - 2 fichas verdes = doble pivote del 1-4-4-2.
  - Etiquetas «3» y «2» sobre cada grupo. El resto de jugadores aparece muy atenuado, solo como contexto.
- Cabecera: «1-4-3-3 vs 1-4-4-2» (70 px).
- **Una única flecha** blanca, curva y gruesa, que señala la zona central.
- Texto principal: **«LA CLAVE ESTÁ AQUÍ»** (1 línea, 96 px).
- Nota táctica: el «3 vs 2» describe la **ocupación** del carril central cuando ambos sistemas se
  enfrentan. No afirma que un sistema sea superior: el 1-4-4-2 compensa con sus dos bandas
  y sus 2 puntas contra los centrales.

---

## Tipografía y estilo comunes

- Fuente: **Nunito Black (900)**, redondeada y gruesa (Google Fonts, incrustada en base64).
- Color del texto: blanco #FFFFFF, con contorno oscuro #050A07 de 7–9 px (`paint-order: stroke fill`).
- Paleta: negro #07110B, verde #18C25A, blanco.
- Texto principal: 2–3 palabras y como máximo 2 líneas. Sin párrafos ni listas de ventajas.

## Regenerar

```bash
NODE_PATH=$(npm root -g) node miniaturas/_build/build.js
```

---

## Variantes con avatar (concepto 1 elegido) — `miniatura_avatar_01..03.png`

Se usa la figura de Moisés Díaz **recortada, sin el fondo de la foto**. El recorte está en `inputs/cara/avatar_recorte.png`
y se hizo a partir de `inputs/cara/avatar.png` con rembg y el modelo `birefnet-portrait`, en local.
No se retoca el rostro: solo se añade una luz de contorno blanca y verde y una sombra para integrarlo.
Todas mantienen las dos formaciones completas (11 + 11) y el texto «¿CUÁL ELIGES?».

- **01 · Centro:** Moisés entre los dos campos, con el «VS» sobre la cabeza y la pregunta en una franja inferior.
- **02 · Presentador + pizarra:** Moisés a la izquierda y las dos formaciones en una pizarra a la derecha, con el texto abajo a la derecha.
- **03 · Primer plano:** Moisés grande a la derecha, la pizarra a la izquierda y la pregunta arriba.

Regenerar: `NODE_PATH=$(npm root -g) node miniaturas/_build/build_avatar.js` (0 créditos, sin IA generativa de imagen).

---

## Estilo «presentador + dos tarjetas» (referencia de Moisés) — `miniatura_estilo_01..03.png`

- Moisés recortado en el centro y una tarjeta inclinada por sistema a cada lado (formación completa de 11 y su número).
- Fondo partido en dos brillos con rayos y chispas, y titular de dos partes arriba (la segunda parte en color).
- **01:** dorado frente a verde, con «2 SISTEMAS. 1 ELECCIÓN.».
- **02:** naranja frente a verde (la más parecida a la referencia), con «2 SISTEMAS. ¿CUÁL ELIGES?».
- **03:** blanco frío frente a verde, con «¿1-4-3-3 O 1-4-4-2?».
- Limitación: el recorte solo incluye cabeza y hombros, así que las tarjetas «flotan» y no las sostiene con las manos.
  Para que las sujete habría que generar una pose nueva con IA (Higgsfield), usando su foto como referencia.

Regenerar: `NODE_PATH=$(npm root -g) node miniaturas/_build/build_estilo.js`
