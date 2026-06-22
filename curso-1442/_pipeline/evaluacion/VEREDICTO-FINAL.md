# VEREDICTO FINAL — Curso "Sistema 1-4-4-2: del concepto al campo"

**Producto:** MISTER ÉLITE — Moisés Díaz
**Evaluador:** Evaluador final (criterio editorial exigente)
**Fecha:** 2026-06-22 — re-evaluación tras la "vuelta corta de legibilidad" (partía de 7.9/10)
**Listón TOP:** global ≥ 8.5 y sin defectos bloqueantes.
**Método:** render real a PNG con cairosvg (1100 px) e inspección visual de las 7 pizarras corregidas + 5 al azar (portada incluida); verificación automática 1:1 de enlaces a SVG y enlaces internos `.md`; comprobación de la portada como página 1 del PDF (PyMuPDF, 80 págs.).

---

## VEREDICTO: TOP (publicable, nivel profesional de venta)

### Puntuación global: 9.0 / 10  (antes 7.9)

No se detectan defectos bloqueantes. No requiere otra vuelta.

---

## 1. Verificación visual de las pizarras corregidas — TODAS RESUELTAS

| Pizarra | Defecto bloqueante previo | Estado tras render PNG | Veredicto |
|---|---|---|---|
| `tarea-22` | etiquetas amontonadas sobre fichas | 4 cuadrantes separados (1 ATAQUE / 2 PIERDO→A-D / 3 DEFENSA / 4 ROBO→D-A), rótulos sobre césped libre, leyenda lateral | RESUELTO |
| `tarea-27` | zona/hombre/poste solapados en el área | mini-leyenda lateral + labels (ZONA, POSTE, "2 al hombre") despejados; área legible | RESUELTO |
| `teoria-12-problema-2v3` | "2 vs 3" y pivote solapando círculos | "2 vs 3" arriba-izda del recuadro; "pivote libre"/"el libre filtra" sin solape | RESUELTO |
| `teoria-01-formacion-base` | etiquetas de rol cortadas/fuera | extremo·lateral·central·pivote 6/8·referencia·móvil, todas dentro del campo, nada cortado | RESUELTO |
| `teoria-07-bloques-altura` | etiquetas de bloque/metros desbordadas | BLOQUE ALTO/MEDIO/BAJO con metros (~45-55/~30-40/~18-25 m) dentro de cada banda; roles al pie, dentro | RESUELTO |
| `tarea-10` | sombra al pivote poco visible | cono de sombra gris sobre "pivote (a tapar)" claramente dibujado; carreras curvas rotuladas | RESUELTO |
| `tarea-18` | 2ª jugada poco resaltada | elipse sombreada + rótulo "2ª jugada"; "balón largo / DC pelea-peina / DC recoge" claros | RESUELTO |

Sin solapes de texto sobre fichas, legibles y coherentes con paleta y convención de flechas en las 7.

### Muestreo aleatorio (control de no-regresión)
`portada`, `teoria-14-salida-3mas2`, `teoria-19-contraataque`, `tarea-15`, `teoria-22-corner-ofensivo`: render correcto, etiquetas dentro de campo, leyenda presente, paleta consistente. **Sin regresiones.**

---

## 2. Integridad técnica

- **Enlaces a gráficos:** 52 referencias `.svg` en los `.md`, **0 rotas**; ningún SVG referenciado falta. Único SVG no referenciado: `portada.svg` (esperado: se usa en portada/PDF/sitio).
- **Enlaces internos `.md`:** **0 rotos** (README↔módulos↔ejercicios↔plan).
- **PDF:** `curso-1442.pdf`, 80 páginas; **página 1 = portada** (CURSO TÁCTICO PROFESIONAL · 1-4-4-2 · del concepto al campo · MISTER ÉLITE; callouts 4 módulos / 27 tareas / +40 pizarras / 2 microciclos).

---

## 3. Puntuación por dimensión

| # | Dimensión | 7.9 previo | Ahora | Comentario |
|---|-----------|-----------|-------|-----------|
| 1 | Legibilidad de pizarras (texto sin solapes, dentro de campo) | 6.5 | 9.0 | Los 7 puntos bloqueantes resueltos; nitidez recuperada |
| 2 | Corrección táctica de los diagramas | 9.0 | 9.0 | Sin cambios; sigue correcta |
| 3 | Consistencia visual (paleta, flechas, título, leyenda) | 8.5 | 9.0 | Leyendas laterales homogéneas en las corregidas |
| 4 | Integración texto↔gráfico (enlaces vivos) | 9.0 | 9.5 | 52/52 refs vivas, 0 rotas |
| 5 | Navegación y coherencia (.md, recuentos) | 8.5 | 9.0 | 0 enlaces internos rotos, 27 tareas coherente |
| 6 | Acabado / entregable (PDF, portada, marca) | 8.0 | 9.0 | Portada como pág. 1, 80 págs., pie de marca en todas las pizarras |

### Global ponderado: 9.0 / 10

---

## 4. Observaciones MENORES (cosméticas, NO bloquean)

- **MENOR-1 — glifo de balón sobre rótulo POR.** En varias pizarras el icono de balón en posesión se dibuja encima del texto "POR" (p. ej. `tarea-18`, `teoria-14`). Es la convención de "balón en juego" y es interpretable, pero superpone ligeramente el rótulo del portero. Pulido opcional: desplazar el balón ~6-8 px o bajar opacidad.
- **MENOR-2 — etiquetas casi tocando una ficha.** Toques mínimos label↔chip sin solape real: `tarea-15` "1er palo" junto al DC; `teoria-01` "pivote 6" rozando la línea del círculo central. Legibles; reubicar 5-10 px las dejaría impecables.
- **MENOR-3 — `tarea-27`, ficha rival "L/Z" arriba-dcha.** La etiqueta combinada "L/Z" queda algo apretada dentro de su ficha; separar lanzador y zona aclararía la lectura.

Ninguna afecta a la comprensión táctica ni a la entrega.

---

## Conclusión

Los 7 defectos de legibilidad marcados como bloqueantes en el 7.9/10 están **resueltos y verificados visualmente sobre PNG**; el muestreo no revela regresiones; los enlaces (gráficos e internos) están todos vivos; y el PDF abre con la portada como página 1. El curso sube de **7.9 a 9.0** y obtiene veredicto **PRODUCTO TOP — listo para publicar y vender.**
