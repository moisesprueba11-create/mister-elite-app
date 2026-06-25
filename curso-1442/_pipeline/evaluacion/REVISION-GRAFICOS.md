# Revisión de gráficos — Curso 1-4-4-2

Revisor: control de calidad de pizarras tácticas.
Fecha: 2026-06-22.
Alcance: 21 diagramas SVG (`01`–`21`) en `curso-1442/graficos/`.
Estándar de referencia: `01-formacion-base.svg`.
Paleta canónica: propios `#1d6fb8` · rival `#c0392b` · oscuro/portero/cabecera `#1d3557` · acento `#ffd24a` · césped `#2e7d32`/`#2f8235` · líneas blancas.

Criterios por diagrama: corrección táctica, legibilidad, consistencia (paleta + convención de flechas + título/leyenda), validez (XML + viewBox).

> Nota de proceso: durante la revisión varios archivos (12, 16, 17, 19, 20, 21) fueron regenerados por el pipeline de creación. La evaluación final se hizo contra el contenido vigente y estable de cada archivo.

---

## 01 — formacion-base.svg
**Estado: OK**
- Formación base 1-4-4-2 plana, 11 posiciones rotuladas (POR + 4 DEF + 4 MED + 2 DC). Tags de rol ("6" ancla, "8" llegador, referencia/móvil) correctos.
- Paleta canónica, título y etiquetas de línea presentes. XML y viewBox correctos.
- Es la referencia del set; sin problemas.
**Puntuación: 10/10**

## 02 — variantes-plano-rombo.svg
**Estado: OK**
- Comparativa lado a lado plano vs. rombo, ambos con 11 jugadores coherentes. Rombo bien resuelto (MCD-INT-INT-MP) con polígono guía.
- Divisor, subtítulos y captions claros. Paleta correcta. XML/viewBox correctos (captions dentro de 700).
- Sin leyenda de flechas, pero el diagrama es puramente posicional (no usa flechas), así que no aplica.
**Puntuación: 9/10**

## 03 — bloques-altura.svg
**Estado: OK**
- Tres alturas (alto/medio/bajo) con última línea punteada, badge de metros y primer presionador por bloque; escala lateral de metros bien construida.
- Markers de flecha por color definidos y usados correctamente (`arrowAlto/Medio/Bajo`). Mini-leyenda presente.
- Usa una rampa de azules (claro→oscuro) para diferenciar bloques: desviación intencional y legible, dentro del espíritu de la paleta.
**Puntuación: 9/10**

## 04 — pressing-delanteros-sombra.svg
**Estado: OK**
- Presión de los 2 DC con carrera curva, cono de sombra tapando al pivote y pase forzado a banda. Coherente con el pedido.
- Tres tipos de flecha con markers (carrera, pase, cobertura). Leyenda completa. Paleta correcta. XML/viewBox correctos.
**Puntuación: 9/10**

## 05 — basculacion-bloque.svg
**Estado: CORREGIDO**
- Problema: amarillo fuera de paleta (`#ffd166`) en la zona "banda concedida" y en el swatch de la leyenda.
- Arreglo: reemplazado por el acento canónico `#ffd24a`.
- Táctica correcta (balón en banda derecha, LI a línea de 3, MI al carril central, banda lejana concedida). Leyenda con swatch blanco visible.
**Puntuación: 9/10**

## 06 — fuera-de-juego.svg
**Estado: OK**
- Subida coordinada de la línea de 4 ("persiana"), dos atacantes por debajo de la línea de FJ con banderines, central que ordena (callout). Coherente.
- Leyenda con swatches visibles (blanco/amarillo). Paleta correcta. XML/viewBox correctos.
**Puntuación: 9/10**

## 07 — solucion-2v3.svg
**Estado: CORREGIDO**
- Problemas: (1) amarillo fuera de paleta (`#ffd166`); (2) en la leyenda había dos flechas superpuestas en las mismas coordenadas (una azul oscura invisible sobre fondo navy + una blanca).
- Arreglos: `#ffd166` → `#ffd24a`; eliminada la flecha duplicada invisible y añadido marcador blanco (`arrowWhite`) para que el swatch de la leyenda tenga punta visible.
- Táctica correcta (pellizco del MI formando el 3 funcional MI+MC+MC frente al triángulo rival).
**Puntuación: 9/10**

## 08 — salida-3mas2.svg
**Estado: CORREGIDO**
- Problema: en la leyenda, el swatch de "movimiento" (flecha navy `#1d3557`) quedaba invisible sobre el panel de leyenda navy.
- Arreglo: añadido un "riel" blanco bajo el swatch para que la flecha navy contraste.
- Táctica correcta (descenso del "6" entre centrales → superioridad 3 vs 2, laterales altos, circulación de pases). Leyenda completa.
**Puntuación: 9/10**

## 09 — delanteros-apoyo-ruptura.svg
**Estado: CORREGIDO**
- Problema: swatch navy de "movimiento" invisible sobre panel navy en la leyenda.
- Arreglo: riel blanco bajo el swatch.
- Táctica correcta (DC apoyo baja entre líneas resaltado en amarillo, DC ruptura en diagonal a la espalda, descarga filtrada). Última línea rival punteada en rojo. Leyenda completa.
**Puntuación: 9/10**

## 10 — ataque-area-centro.svg
**Estado: CORREGIDO**
- Problema: swatch navy de "movimiento" invisible sobre panel navy en la leyenda.
- Arreglo: riel blanco bajo el swatch.
- Táctica correcta (centro desde banda derecha, ocupación de 1er palo / penalti / 2º palo / frontal por 2 DC + extremo lejano + MC llegador, cut-back resaltado). Tres markers de flecha. Leyenda completa.
**Puntuación: 9/10**

## 11 — desdoblamiento-lateral-extremo.svg
**Estado: CORREGIDO**
- Problemas: (1) elementos basura/vacíos (`<text x="500" y="0"/>` y varios `<rect width="0" height="0">`); (2) en la leyenda había una flecha "movimiento" duplicada, una de ellas sin etiqueta, y el swatch navy era invisible sobre panel navy.
- Arreglos: eliminados los elementos vacíos; consolidado a un único swatch de "movimiento" con riel blanco y etiqueta correcta.
- Táctica correcta (overlap: extremo fija dentro / lateral por fuera; underlap: extremo retiene fuera / lateral por dentro), dos paneles con línea rival punteada.
**Puntuación: 9/10**

## 12 — transicion-contraataque.svg
**Estado: CORREGIDO**
- (Versión regenerada durante la revisión.) Problema remanente: swatch navy de "carrera/movimiento" invisible sobre panel navy en la leyenda.
- Arreglo: riel blanco bajo el swatch.
- Táctica correcta y completa (robo en zona media → 1er pase vertical al DC apoyo → descarga al DC ruptura a la espalda; ED corre carril; MC "8" de tercer hombre; back four + POR de equilibrio). Última línea rival punteada.
**Puntuación: 9/10**

## 13 — transicion-repliegue.svg
**Estado: CORREGIDO**
- Problema: swatch navy de "repliegue" invisible sobre panel navy en la leyenda.
- Arreglo: riel blanco bajo el swatch.
- Táctica correcta (recomposición de las dos líneas de 4 hacia posiciones objetivo punteadas; el más cercano frena el balón central resaltado en amarillo; el resto repliega recto a su carril). Leyenda completa.
**Puntuación: 9/10**

## 14 — tarea-salida.svg
**Estado: CORREGIDO**
- Problema: swatch navy de "carrera" invisible sobre panel navy en la leyenda.
- Arreglo: riel blanco bajo el swatch.
- Táctica correcta (salida 4+2 vs 2: MC baja entre centrales para el 3 vs 2; laterales abiertos; comodines neutrales de banda; zonas-meta a ~40 m; cambio de orientación premiado). Cotas de dimensiones y leyenda completas.
**Puntuación: 9/10**

## 15 — tarea-basculacion.svg
**Estado: CORREGIDO**
- Problema: swatch navy de "basculación" invisible sobre panel navy en la leyenda.
- Arreglo: riel blanco bajo el swatch.
- Táctica correcta (dos líneas de 4 unidas por "cuerda" amarilla basculando al lado fuerte; lado débil cerrado; circulación rival en U lateral-central-lateral). Cotas y leyenda completas.
**Puntuación: 9/10**

## 16 — tarea-press-delanteros.svg
**Estado: CORREGIDO**
- (Versión regenerada durante la revisión.) Problema: swatch navy de "carrera de press" invisible sobre panel navy en la leyenda.
- Arreglo: riel blanco bajo el swatch.
- Táctica correcta (2 DC con carrera curva; cover-shadow tapa al pivote; segundo DC cubre al central libre; salida rival orientada a la zona-meta de banda). Cotas y leyenda completas.
**Puntuación: 9/10**

## 17 — tarea-gatillo-lateral.svg
**Estado: CORREGIDO**
- (Versión regenerada durante la revisión.) Problemas: dos swatches navy invisibles sobre panel navy en la leyenda ("carrera/salto" y "cadena de cobertura").
- Arreglos: riel blanco bajo ambos swatches.
- Táctica correcta (gatillo central→lateral; MD salta al lateral; DC cierra la vuelta; MC tapa el interior; lateral propio sube a vigilar al extremo; cadena de cobertura). Cotas y leyenda completas.
**Puntuación: 9/10**

## 18 — tarea-delanteros.svg
**Estado: OK**
- Táctica correcta (un DC apoyo baja, otro DC ruptura en diagonal; servicio de los MC; descarga al hueco; remate). Conos de línea rival, cotas 45x45 m.
- Leyenda con swatches visibles (carrera blanca / pase amarillo). Paleta correcta. XML/viewBox correctos.
**Puntuación: 9/10**

## 19 — tarea-contrapresion.svg
**Estado: OK**
- (Versión regenerada durante la revisión.) Táctica correcta (momento de la pérdida; 2-3 más cercanos saltan al balón; el resto cierra líneas de pase; reloj de 5 s; 4 mini-porterías; "el primer defensor es quien ha perdido").
- Leyenda con swatch blanco visible (sin el problema navy-sobre-navy). Paleta correcta. XML/viewBox correctos.
**Puntuación: 9/10**

## 20 — tarea-transicion-banda.svg
**Estado: OK**
- (Versión regenerada durante la revisión; la versión previa colocaba el extremo "MI" en la banda derecha de forma incoherente — corregida en la regeneración.) Táctica correcta (robo → 1er pase vertical/banda; extremo MI corre el carril izquierdo; dos DC apoyo/ruptura; centro/finalización; reloj máx 6 s / 5 pases; "gol por banda = doble").
- Leyenda con swatches visibles. Paleta correcta. XML/viewBox correctos.
**Puntuación: 9/10**

## 21 — tarea-zonas-puntos.svg
**Estado: OK**
- (Versión regenerada durante la revisión.) Campo zonificado en 3 carriles + 3 tercios, bandas resaltadas como zonas premiadas (robo +1 / progresión premiada); bloque 1-4-4-2 completo; basculación que orienta a banda; búsqueda de amplitud; cota "bloque < 35 m"; barra de puntuación.
- Leyenda con swatches visibles. Paleta correcta. XML/viewBox correctos.
- Detalle menor: el pedido sugería "estrellas de puntos"; esta versión usa etiquetas "+1" (equivalente funcional, igualmente claro).
**Puntuación: 9/10**

---

## Resumen

| Nº | Archivo | Estado | Punt. |
|----|---------|--------|------|
| 01 | formacion-base | OK | 10 |
| 02 | variantes-plano-rombo | OK | 9 |
| 03 | bloques-altura | OK | 9 |
| 04 | pressing-delanteros-sombra | OK | 9 |
| 05 | basculacion-bloque | CORREGIDO | 9 |
| 06 | fuera-de-juego | OK | 9 |
| 07 | solucion-2v3 | CORREGIDO | 9 |
| 08 | salida-3mas2 | CORREGIDO | 9 |
| 09 | delanteros-apoyo-ruptura | CORREGIDO | 9 |
| 10 | ataque-area-centro | CORREGIDO | 9 |
| 11 | desdoblamiento-lateral-extremo | CORREGIDO | 9 |
| 12 | transicion-contraataque | CORREGIDO | 9 |
| 13 | transicion-repliegue | CORREGIDO | 9 |
| 14 | tarea-salida | CORREGIDO | 9 |
| 15 | tarea-basculacion | CORREGIDO | 9 |
| 16 | tarea-press-delanteros | CORREGIDO | 9 |
| 17 | tarea-gatillo-lateral | CORREGIDO | 9 |
| 18 | tarea-delanteros | OK | 9 |
| 19 | tarea-contrapresion | OK | 9 |
| 20 | tarea-transicion-banda | OK | 9 |
| 21 | tarea-zonas-puntos | OK | 9 |

- Diagramas revisados: **21/21**.
- Corregidos: **13** (05, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17).  *(12 corregidos sobre archivos; nota: lista detallada arriba)*
- En OK sin tocar: 01, 02, 03, 04, 06, 18, 19, 20, 21.

### Problemas más comunes
1. **Contraste de leyenda (el más frecuente):** el swatch de "movimiento/carrera" se dibujaba con flecha azul oscuro `#1d3557` sobre el panel de leyenda navy `#1d3557`, quedando invisible. Corregido en 08, 09, 10, 11, 12, 13, 14, 15, 16, 17 añadiendo un riel blanco bajo el swatch (la flecha navy mantiene la convención y ahora contrasta).
2. **Amarillo fuera de paleta:** `#ffd166` en lugar del canónico `#ffd24a` (05, 07). Unificado.
3. **Elementos basura / duplicados:** elementos vacíos y una flecha de leyenda duplicada/sin etiqueta (07, 11). Limpiados.

### Validez
- Los 21 SVG son XML bien formados.
- Todas las referencias `url(#marker)` resuelven a un `<marker>` definido (sin flechas sin punta).
- Todos los viewBox son correctos; ningún contenido queda recortado fuera del lienzo.

## Veredicto global

**Puntuación media: 9,05/10**

**APTO para el curso.** Tras las correcciones, el set es tácticamente coherente con su spec (1-4-4-2 bien representado donde aplica), legible, consistente con la paleta canónica y la convención de flechas (continua = carrera/movimiento, ondulada/discontinua = pase, con markers válidos), y técnicamente válido. Las desviaciones restantes son menores e intencionales (rampa de azules en 03, swatches de carrera en blanco en algunas tareas, "+1" en 21).
