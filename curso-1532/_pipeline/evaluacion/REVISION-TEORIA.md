# REVISIÓN DE CALIDAD — Diagramas de TEORÍA (16)

> Curso "Sistema 1-5-3-2" · MISTER ÉLITE — Moisés Díaz
> Revisor de calidad de pizarras tácticas · estándar producto "top"
> Fecha: 2026-06-22 · Lote: `graficos/teoria-*.svg` (16 diagramas)
> Método: render PNG (cairosvg, 680 px ancho), lectura visual + cotejo con `PEDIDOS.md`, `CONVENCION.md` y el módulo correspondiente.

## Resumen

| Severidad | Nº |
|---|---|
| OK | 12 |
| MENOR | 4 |
| BLOQUEANTE | 0 |

**Puntuación media: 8,4 / 10.**

Conclusión global: lote sólido y coherente con la convención (carrileros = CAR 2/3, línea de 5 = 3-6-5-4-2, líbero 5, pivote 8 + interiores 7/10, 2 puntas 9/11, sin extremos). No hay errores tácticos ni de nomenclatura. Los defectos detectados son de **legibilidad** (solapes texto/flecha, etiqueta tapada por la leyenda) y un par de matices de completitud. Ninguno bloquea la publicación, pero hay 4 retoques recomendados para alcanzar el acabado "top".

---

## Tabla de evaluación

| Archivo | Punt. | Sev. | Defecto concreto | Corrección precisa |
|---|---|---|---|---|
| `teoria-01-estructura-1532.svg` | 9 | OK | Línea de 5 (3-6-5-4-2), medio de 3 (10-8-7), 2 puntas (9-11), POR 1. Coherente con M01 §intro. Etiqueta "MC int/MC pivote" roza el círculo central pero legible. | Sin acción. Opcional: bajar 2 px las etiquetas "MC int" de 10 y 7 para que no toquen la línea media. |
| `teoria-01-doble-funcion.svg` | 8 | MENOR | Comparativa correcta: izq. 1-5-3-2 con línea de 5 completa (3-6-5-4-2 baja), der. 1-3-5-2 con 3/2 subidos (flechas "sube") y línea de 5 media (3-10-8-7-2). El carrilero 3 del panel derecho está en cx≈396,8 (divisoria en x=340): casi pegado a la línea central de separación, y su flecha "sube" (x=396,8) nace sobre la divisoria. | Desplazar el 3 del panel CON balón y su flecha a cx≈410-420 para despegarlo de la divisoria punteada (x=340); así no parece invadir el panel izquierdo. |
| `teoria-01-distancias.svg` | 7 | MENOR | Cotas correctas (10-12 m entre líneas, 8-10 m entre centrales, 30-35 m bloque). PERO el texto de cota "10-12 m" (izq., y≈683) y "10-12 m"(der.) quedan ATRAVESADOS por la línea de la flecha de medida; "30-35 m" se solapa con la flecha cian. | Añadir un rectángulo de fondo (fill #15202b, opacity .85) detrás de cada etiqueta de cota, o desplazar el texto 10-12 px lateralmente fuera del trazo de la flecha. |
| `teoria-01-principios.svg` | 7 | MENOR | Dos estados correctos (izq. ofensivo 1-3-5-2, der. defensivo 1-5-3-2 con zona "centro denso"). DEFECTOS: (1) el POR "1" del panel izquierdo queda parcialmente TAPADO por el cuadro de LEYENDA (esquina inf. izq.); (2) el texto "salida 3+8" se solapa con la flecha de conducción cian. | (1) Subir el POR izquierdo ~20 px o reubicar la LEYENDA al lado derecho inferior; (2) separar la etiqueta "salida 3+8" del trazo de conducción o ponerle fondo. |
| `teoria-01-variantes.svg` | 8 | OK | Esquema en 4 cuadrantes: líbero (5 detrás cubriendo) vs 3 en línea (marcaje, sube) y 10 alto vs doble pivote (8+7). Coherente con M01 §6. Uso correcto de ficha rival (rojo) para los DC marcados. | Sin acción. Opcional: rotular el cuadrante inferior-izq. "LÍBERO" y sup.-izq. "3 EN LÍNEA" con el mismo tamaño para simetría. |
| `teoria-02-roles-defensivos.svg` | 9 | OK | Línea de 5 (3-6-5-4-2) con etiquetas 1v1 banda / salta / líbero-cubre; medio 10-8-7 (escolta/ancla/escolta); 9 "orienta" y 11 "cubre pivote" escalonados (nunca en paralelo); POR "+1 líbero". Limpio, sin solapes. Coherente con M02 §1. | Sin acción. |
| `teoria-02-paso-3-a-5.svg` | 8 | OK | Carrileros 3 y 2 "alto" con flechas largas "repliega" a conos formando la "línea de 5" con 6-5-4; medio 10-8-7; puntas 9-11. Conos de referencia presentes. Transmite el movimiento; PEDIDOS pedía "dos fotogramas" y se resuelve con un fotograma + flechas (válido y más limpio). | Sin acción. Opcional para fidelidad literal a PEDIDOS: añadir mini-fotograma o fantasma de la posición inicial de 2/3. |
| `teoria-02-gatillo-carrilero.svg` | 7 | MENOR | Concepto correcto: BAL al carrilero rival, 2 "salta", 7 "desliza/cubre carril", 4 deslizando, zona "línea en 4 temporal" con 3(pinza)-6-5, 8 "tapa centro". DEFECTO: zona del cluster 7/4 con flechas cruzadas y etiquetas "desliza"/"cubre carril" muy juntas; el 4 (que forma la línea de 4) se dibuja FUERA de la zona sombreada, lo que confunde quién compone esa línea de 4. | Reposicionar el 4 dentro/al borde de la zona "línea en 4 temporal" (la línea de 4 = 3+6+5+4), o aclarar con etiqueta que el 4 desliza hacia ella. Separar las etiquetas "desliza" y "cubre carril" ~10 px. |
| `teoria-02-basculacion.svg` | 8 | OK | Escalera diagonal de la línea de 5 correcta: 2 "aprieta" arriba, 4 "cobertura" detrás, 5 "hombre libre", 6 deslizando, 3 "pinza dentro" lado débil; medio 10-8-7; RIV con balón. Coherente con M02 §5. Etiquetas "libre/hombre libre" apiladas pero legibles. | Sin acción. Opcional: fusionar las dos etiquetas "libre" + "hombre libre" en una sola línea junto al 5. |
| `teoria-03-salida-3-pivote.svg` | 9 | OK | Rombo de salida correcto: 5 conduce, 4 y 6 abiertos a altura de área, 8 "se ofrece" al frente; 2 DC rivales; carrileros 3 y 2 "amplitud" altos; POR "+1"; pases 6→8, 4→2, conducción de 5. Coherente con M03 §1. | Sin acción. Detalle: la flecha "ATAQUE" superior-der. queda cortada en el borde sup.; alargar el lienzo o bajar la flecha 8 px. |
| `teoria-03-mutacion-1352.svg` | 9 | OK | Cinco carriles marcados (franjas verticales) + "5 carriles ocupados"; línea de 5 media 3-10-8-7-2; 3 DFC atrás (6-5-4); puntas 9-11; POR 1. Réplica exacta de PEDIDOS y M03 §2. | Sin acción. |
| `teoria-03-ocupacion-area.svg` | 8 | OK | Centro del carrilero 2; 9 "1er palo", 11 "penalti", 10 "2do palo", 8 "frontal/rechace", 3 "rechace" (carrilero contrario). Cumple la regla de remate de M03 §3. Etiquetas "1er palo" y "centra/centro" rozan fichas pero legibles. | Sin acción. Opcional: separar 3-4 px la etiqueta "1er palo" del 9 y unificar "centra/centro" en un solo rótulo. |
| `teoria-03-desdoblamiento.svg` | 7 | MENOR | Concepto correcto: 7 "arrastra dentro" al LAT rival, 2 "desborda por fuera" en el "espacio liberado" sombreado, pase a 9 "1er palo", 11 "penalti". DEFECTO: las dos flechas blancas de carrera (arrastre del 7 y regate) salen muy juntas y se cruzan/entrelazan en el centro del campo, restando claridad a qué trayectoria es de quién. | Separar las dos trayectorias blancas: dar más curvatura a la del 7 (hacia dentro) y dejar recta y diferenciada la del 2 (por fuera, dentro de la zona). Etiquetar cada flecha ("arrastra" / "desborda"). |
| `teoria-04-transicion-da.svg` | 8 | OK | Transición ofensiva: 5 "roba" → pase vertical; 9 "apoyo/pie", 11 "a la espalda" (pase 9→11); 10 y 7 acompañan; 2 "lanzado/por fuera" con centro; 8 "ancla". Coherente con M04 §1. Etiqueta "vertical" y "a espalda" rozan trazos pero legibles. | Sin acción. Opcional: fondo a "vertical" y "a la espalda" para despegarlas de las flechas. |
| `teoria-04-transicion-ad.svg` | 9 | OK | Transición defensiva: 8 "frena" (corte rojo al balón RIV); 2 "repliega/recompone L5" (flecha larga); 4 "sale provisional" a banda; 5 "cubre hueco"; 7 "seguro banda"; línea provisional 3-6-5+4. Réplica de M04 §2. Claro. | Sin acción. |
| `teoria-04-corner-favor.svg` | 8 | MENOR | Córner correcto: 10 saca, rematadores 6(1er palo)-4(2do palo)-5(penalti)-9(desvío) = "3 DFC + 9"; 8 "frontal/rechace"; seguros 3 + 7; 11 "referencia contra". Carreras cruzadas. DEFECTO menor de completitud: el 2º carrilero (2) NO aparece en la pizarra; PEDIDOS pide "2 puntas como referencia" y solo se muestra el 11 (el 9 ataca, correcto según M04). | Añadir la ficha del carrilero 2 como segundo seguro/referencia atrás (PEDIDOS: "carrilero + 1 DFC de seguro"), o al menos completar los 10 de campo. Verificar que el seguro sea coherente con el texto (carrilero + DFC; aquí es carrilero 3 + interior 7). |

---

## Lista priorizada de acciones

**BLOQUEANTES:** ninguno.

**MENORES (4) — orden de impacto en legibilidad:**

1. `teoria-01-principios.svg` — POR "1" izquierdo tapado por la caja de LEYENDA + etiqueta "salida 3+8" sobre la flecha de conducción. (El jugador tapado es lo más visible). Reubicar leyenda o subir el POR; poner fondo a la etiqueta.
2. `teoria-01-distancias.svg` — textos de cota "10-12 m" y "30-35 m" atravesados por las flechas de medida. Añadir fondo o desplazar lateralmente.
3. `teoria-02-gatillo-carrilero.svg` — el 4 que forma la "línea de 4 temporal" se dibuja fuera de la zona sombreada; flechas/etiquetas "desliza"/"cubre carril" amontonadas. Reubicar el 4 al borde de la zona y separar etiquetas.
4. `teoria-03-desdoblamiento.svg` — las dos flechas blancas de carrera (7 arrastra / 2 desborda) se cruzan y entrelazan; separar trayectorias y etiquetarlas.

**Retoques OK opcionales (pulido fino, no obligatorios):**
- `teoria-04-corner-favor.svg` — completar el carrilero 2 como seguro atrás (matiz de completitud, no error táctico).
- `teoria-03-salida-3-pivote.svg` — flecha "ATAQUE" cortada en el borde superior.
- `teoria-01-doble-funcion.svg` — separar el carrilero 3 (panel der.) de la divisoria central.

---

## Notas de conformidad con la convención

- Nomenclatura correcta en los 16: carrileros = 2/3 (CAR), nunca "extremo/lateral/EI/ED"; línea de 5 = 3-6-5-4-2; líbero = 5; pivote = 8; interiores = 7/10; puntas = 9/11; POR = 1 (+1 líbero).
- La doble función (con balón 1-3-5-2 / sin balón 1-5-3-2) está bien representada en `doble-funcion`, `paso-3-a-5`, `mutacion-1352` y las dos transiciones.
- Marca y pie ("MISTER ÉLITE · Moisés Díaz", "Sistema 1-5-3-2") presentes y consistentes en todos.
