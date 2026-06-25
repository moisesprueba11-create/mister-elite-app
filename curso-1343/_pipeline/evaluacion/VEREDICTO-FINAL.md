# VEREDICTO FINAL — "Sistema 1-3-4-3: del concepto al campo"
**MISTER ÉLITE — Moisés Díaz** · Evaluación editorial final · 2026-06-22

> Evaluación del producto REAL (README, 4 módulos, fichas de ejercicios, 41 SVG renderizados, PDF de 61 páginas). No de informes previos.

---

## Puntuación por dimensión

| # | Dimensión | Nota |
|---|---|---|
| 1 | Contenido (rigor táctico, teoría/práctica, utilidad, convención) | **9.3** |
| 2 | Cobertura (26 tareas ilustradas, módulos, 0 rutas rotas) | **9.5** |
| 3 | Calidad y coherencia gráfica | **9.0** |
| 4 | Portada y marca | **9.0** |
| 5 | PDF (existe, pág.1 = portada) | **9.5** |

### GLOBAL: **9.2 / 10**

---

## VEREDICTO: **TOP** — publicable, nivel de venta

≥ 8.5 y **sin bloqueantes**. Producto coherente, riguroso y comercializable tal cual.

---

## Evidencia por dimensión

### 1. Contenido — 9.3
- **Rigor del 1-3-4-3 impecable.** La mutación 3-4-3 ↔ 3-2-5 con balón y la línea de 3 ↔ 5 sin balón están bien explicadas y son el hilo conductor real de todo el curso (no un adorno). La ocupación de los 5 carriles (CAR 3 · EI 11 · DC 9 · ED 7 · CAR 2) con bloque 3+1 (DFC 4-5-6 + MC 8) detrás y el 10 de enlace es exacta y moderna.
- **Línea de 5 y pressing orientado** bien tratados: "uno salta, dos cubren", gatillos (pase a banda, pase atrás, control orientado), banda-trampa, basculación, riesgo a la espalda de los carrileros con 6 soluciones concretas. Tridente con doble desmarque del 9 y desdoblamiento CAR-extremo (2v1 al lateral).
- **Equilibrio teoría/práctica correcto:** 4 módulos breves con "Ideas clave" + "Errores comunes" y checklist de campo, frente a **26 tareas** de campo. Cumple la filosofía "poca teoría, mucha aplicación".
- **Fichas uniformes y utilizables:** Objetivo · Organización · Desarrollo · Provocaciones · Variantes (progresión F→A→S) · Coaching · Duración/Categoría. Provocaciones medibles (goles dobles/triples por condición), realistas y entrenables.
- **Plan de sesiones** sólido: 2 microciclos modelo con lógica MD-4…MD bien periodizada, tareas asignadas por día, tareas de síntesis y tabla de uso del banco. `MD` correctamente aclarado como matchday, no posición.
- **Convención coherente** en todo el producto (README, módulos, fichas, pizarras): POR 1 · DFC 4-5-6 (5 líbero) · CAR 2/3 · MC 8/10 · ED 7 · DC 9 · EI 11. Historia (Cruyff, Conte 13 victorias, Tuchel, Gasperini, De Zerbi, 3-2-5 de Guardiola/Xabi Alonso) precisa y bien dosificada.

### 2. Cobertura — 9.5
- `grep -cE '!\['`: 26 tareas con su pizarra (las 6 fichas suman 26 imágenes únicas a `tarea-01..26.svg`) y los 4 módulos ilustrados (5/3/3/3).
- **0 rutas rotas:** las 41 referencias a SVG resuelven a archivos existentes (verificado para ejercicios y módulos).
- 41 SVG en total; los 15 de teoría cubren estructura, ambas mutaciones, distancias, vs-433, pressing, basculación, salida, último tercio, transiciones y córner.

### 3. Calidad y coherencia gráfica — 9.0
- **Las 41 SVG renderizan limpias** (cairosvg, sin errores).
- Muestra amplia revisada (portada, teoría-01-estructura/mutacion-325/linea5, teoria-02-paso-3-a-5, y tareas 1, 8, 10, 13, 14, 16, 20, 21): legibles, profesionales, con campo, leyenda, flechas tipadas (pase / conducción / desmarque), zonas pintadas y etiquetas de rol.
- **Las dos antes bloqueantes están resueltas:** tarea-10 (gatillos del tridente: banda-trampa, 9 curva, 7 salta, 8 cubre) y tarea-13 (trampa de banda 11v11) renderizan correctas y coherentes con su texto.
- **Coherencia texto-pizarra alta:** tarea-14 = mutación a 3-2-5 con 5 carriles y 3+2 detrás; tarea-16 = 4v3 banda fuerte + desplome diagonal del CAR opuesto al 2º palo; tarea-21 = 4 referencias (9 1er palo, 11 2º, 10 frontal, CAR 4ª ola) idéntico a la regla del Módulo 3.
- Marca presente en pie de cada pizarra ("MISTER ÉLITE · Moisés Díaz") y banner "Sistema 1-3-4-3".

### 4. Portada y marca — 9.0
- Portada profesional: logo ME, "MISTER ÉLITE · ACADEMIA DE ENTRENADORES · MOISÉS DÍAZ", título 1-3-4-3, subtítulo "del concepto al campo", tagline "Poca teoría. Mucha aplicación práctica.", panel de stats (4 módulos / 26 tareas / +40 pizarras / 2 microciclos) y los **11 dorsales dispuestos en 1-3-4-3** (1 · 6-5-4 · 3-10-8-2 · 11-9-7) con tridente y carrileros destacados.
- Marca en portada y en pie de todas las pizarras.

### 5. PDF — 9.5
- `curso-1343.pdf` existe (61 páginas) y **la pág. 1 es la portada** (verificado con PyMuPDF). Subtítulo y panel correctos en la proporción real del PDF.
- Entregables completos: PDF + sitio HTML (`site/index.html` + assets) + HTML autocontenido (`curso-1343-completo.html`).

---

## Observaciones menores (no bloqueantes, pulido opcional)

1. **`graficos/portada.svg`** — al rasterizar a 700 px el subtítulo "del concepto al campo" roza el borde del panel de stats. **No afecta al PDF** (renderiza limpio a la proporción real). Corrección opcional: reducir 1-2 px el `font-size` del subtítulo o ampliar el margen derecho del bloque de texto para garantizar holgura en cualquier rasterización.
2. **Numeración de títulos en las SVG de tareas** — algunos diagramas usan el número de tarea del bloque (p. ej. `tarea-08.svg` titula "Tarea 2.3", `tarea-10.svg` titula "Tarea 3.1"). Es **internamente consistente** (la ficha referencia el archivo correcto y el contenido coincide), pero un lector que cruce "tarea-08" con "Tarea 2.3" podría dudar. Opcional: unificar a un único esquema de numeración visible.
3. Artefacto conocido de rasterización: "POR" se ve "PQR"/"PÔR" en algunas pizarras. Es artefacto del rasterizador, no defecto del SVG.

Ninguna de estas observaciones impide la publicación.

---

*Evaluador final · MISTER ÉLITE — Moisés Díaz · 2026-06-22*
