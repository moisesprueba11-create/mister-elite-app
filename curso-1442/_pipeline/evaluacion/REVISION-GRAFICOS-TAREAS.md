# Revisión de gráficos — Pizarras de TAREAS (Curso 1-4-4-2)

Revisor: control de calidad de pizarras tácticas (estándar "top").
Fecha: 2026-06-22.
Alcance: 27 pizarras de tareas (`graficos/tarea-01.svg` … `graficos/tarea-27.svg`).
Método: render a PNG (680 px de ancho) + lectura visual + contraste con la ficha de cada tarea en `ejercicios/01-salida.md` … `07-balon-parado.md`.

## Criterios
1. **Coherencia con la ficha**: nº de jugadores, espacio/zonas/conos, porterías, movimientos y, sobre todo, la **provocación** específica. ¿Se podría montar la tarea solo con la imagen?
2. **Legibilidad**: solapes de fichas/etiquetas/flechas, texto cortado, leyenda tapada.
3. **Corrección táctica del 1-4-4-2.**
4. **Calidad visual profesional.**

## Nota de paleta (set de tareas)
Las 27 pizarras usan una paleta propia **consistente entre sí** pero **distinta del set de módulos** (que es la referencia canónica del proyecto):
- Azul propio `#1565c0` (canónico: `#1d6fb8`).
- Rojo rival `#c62828` (canónico: `#c0392b`).
- Acento `#ffd54a` / `#f5a623` (canónico: `#ffd24a`).

No hay amarillos basura (`#ffd166` ya no aparece). La desviación es uniforme y de bajo impacto visual, pero es una **inconsistencia de marca** respecto al resto del curso: se recomienda alinear los tres tokens al canon en una pasada global. Se marca como MENOR transversal, no se repite en cada fila.

---

## Tabla de evaluación

| Tarea | Archivo | Punt. | Severidad | Defecto concreto | Corrección precisa |
|---|---|---|---|---|---|
| 1 | tarea-01.svg | 8 | MENOR | Etiqueta vertical "ATAQUE" arriba-derecha cortada por el borde del marco; comodines MI/MD dibujados pegados a la zona-meta (la ficha los define como medios rivales que saltan). | Mover "ATAQUE" 12-16 px hacia dentro del campo; bajar los comodines MI/MD ~80 px hacia la línea de medios para que se lea su rol de "saltan", no de receptores fijos. |
| 2 | tarea-02.svg | 7 | MENOR | Etiqueta "DFC1" (abajo-izq) montada sobre su ficha y la punta de la flecha de conducción ("D●1"). Los 3 carriles se dibujan sobre medio campo con área completa, pero la ficha pide 25×20 m (esquema, aceptable). | Reubicar el texto "DFC1" a la izquierda del marcador (offset -28 px en X); separar el inicio de la flecha de conducción del borde de la ficha (~6 px). |
| 3 | tarea-03.svg | 9 | OK | Tres salidas (por dentro / banda / MC ataca espacio) claras y rotuladas 1·2·3; coincide con la ficha. Sin solapes graves. | Sin cambios obligatorios. Opcional: separar la flecha blanca "3·MC ataca espacio" del texto "ataca espacio" de MC2. |
| 4 | tarea-04.svg | 6 | MENOR | **Error de rótulo**: "pase progresivo Z4→Z2" (debe ser **Z1→Z2**). Etiqueta "pivote disponible" montada sobre la ficha MI ("vote disponible"). | Corregir "Z4" → "Z1" en el texto de la flecha amarilla. Desplazar "pivote disponible" ~30 px a la derecha para liberar el marcador MI. |
| 5 | tarea-05.svg | 5 | BLOQUEANTE | (1) **Línea roja "bloqueo/corte"** entre MI y MC sin sentido en una tarea de basculación (parece resto/error). (2) LD dibujado muy alto (a la altura de "cierra al centro"), rompe la línea de 4 defensiva. (3) Etiquetas "MI"/"MC" pisadas por la línea roja ("M!", "M●C"). | Eliminar la línea roja MI-MC. Bajar LD a la altura de los DFC (línea de 4 alineada). Corregir solape de "MI"/"MC". Revisar el sentido de la flecha "bascula al lado fuerte" respecto a dónde está el balón (rival con balón a la izq circulando a la der). |
| 6 | tarea-06.svg | 6 | MENOR | El texto "FRANJA ENTRE LÍNEAS (zona prohibida)" **atraviesa los dos marcadores EN** ("...ENT[EN]...NEAS (zona p[EN]ida)"); "filtran" y "MC tapa" tocan fichas/flecha. | Subir el rótulo de la franja ~22 px (a la zona vacía superior de la banda verde) para que no cruce los EN; recolocar "filtran" fuera del marcador MC. |
| 7 | tarea-07.svg | 7 | MENOR | "carril encerrado · robo = 2 pts" pisa el balón/AT ("...il encerrado"); etiqueta "MC" tapada por la flecha de basculación; la leyenda cubre una de las mini-porterías inferiores. | Mover el texto "carril encerrado…" ~25 px arriba; separar "MC" de la flecha; subir/reducir la caja de leyenda o desplazar la mini-portería inferior-izq para que no quede tapada. |
| 8 | tarea-08.svg | 7 | MENOR | La relación de marca DC-rival → MC ("marca 2º palo") se dibuja con la **línea roja "bloqueo/corte"**, que en la leyenda significa otra cosa (uso semántico incorrecto). Leve solape "centro"/"DEC". | Sustituir la línea roja de marcaje por una línea/grafismo de "marca" (p. ej. discontinua fina) o añadir "marcaje" a la leyenda; separar el texto "centro" del marcador DFC. |
| 9 | tarea-09.svg | 8 | MENOR | En la banda de la línea de fuera de juego se amontonan "pase al espacio (tarde = fdj)" + "referencia partida" + el rótulo de la línea; lectura densa. | Repartir los tres textos: subir "referencia partida", dejar "pase al espacio…" junto a su flecha y centrar el rótulo de la línea de FdJ sin solapes. |
| 10 | tarea-10.svg | 6 | MENOR | **Las flechas de "carrera curva" están dibujadas RECTAS** (verticales): contradice el concepto y la provocación clave (curvar para tapar al pivote). No se dibuja la "sombra/cono" que tapa al pivote (sí existía en el set de módulos). Los dos centrales rivales están rotulados distinto ("DC" y "DFC"). | Convertir las dos carreras blancas en **trayectorias curvas** (path con curvatura hacia dentro). Añadir un cono/sombra desde el primer DC hacia el PIV. Unificar el rótulo de los dos centrales rivales (ambos "DFC"). |
| 11 | tarea-11.svg | 7 | MENOR | Tablero correcto pero cargado. La "vuelta al central" se traza con la línea roja "bloqueo/corte" cruzando media pizarra (confuso); solapes "D●C" (balón) y "SALTA al lateral" sobre MD. | Acortar/curvar la línea roja de "cierra vuelta" para que se lea como cierre del DC; separar "SALTA al lateral" del marcador MD. |
| 12 | tarea-12.svg | 6 | MENOR | Tercio inferior muy congestionado: "salta al gatillo", "POR juega corto", "P●R" y la flecha de press se pisan entre sí y con las fichas. | Dar aire al cluster del press: subir "salta al gatillo" ~18 px, mover "POR juega corto" al lado de la flecha (no encima), liberar el marcador POR. |
| 13 | tarea-13.svg | 6 | MENOR | El rótulo de banda "BLOQUE MEDIO (por defecto)" **atraviesa los dos marcadores DC** ("B[DC]E MEDIO…[DC]"). "líder activa" pegada a un DC. | Subir el rótulo "BLOQUE MEDIO…" a la franja libre superior de la zona amarilla (sin cruzar los DC); recolocar "líder activa". |
| 14 | tarea-14.svg | 8 | MENOR | Patrón "uno baja / uno rompe" claro y bien resuelto. Solo solape menor "descarga" sobre "sincronía…". | Separar el texto "descarga" del rótulo "sincronía: uno baja cuando el otro rompe". |
| 15 | tarea-15.svg | 8 | MENOR | Ocupación de los tres puntos del área correcta. Cluster apretado arriba (DC "1er palo" + DEF + DEF). El jugador de banda con balón ("desborde") no lleva rótulo de rol (MD/MI). | Separar ligeramente DC-1er palo de los DEF (±12 px); rotular el atacante de banda como "MD/MI". |
| 16 | tarea-16.svg | 7 | MENOR | La numeración del circuito empieza en "2 pared/1 toque" y "3 a banda": **falta el "1"** del primer pase (orden confuso). El MC con balón (inicio) está sin rótulo de rol. | Numerar el primer pase como "1" (MC→DC) y renumerar; rotular el marcador inicial como "MC". |
| 17 | tarea-17.svg | 8 | MENOR | 6v6 + carriles correcto y vía de banda clara. El rótulo "carril" (izq) pisa un marcador rival; jugadores propios algo amontonados en el centro-izq. | Mover el rótulo "carril" izq fuera del marcador rival; repartir levemente los azules del centro. |
| 18 | tarea-18.svg | 6 | MENOR | Zona central muy congestionada: "pelea/peina", "peina", "2ª jugada" se solapan con los marcadores DC/DFC y las flechas; el clúster DFC-DC-DFC-DC arriba está muy apretado. | Aumentar la separación del clúster de delanteros/centrales (±15 px); sacar los textos del interior de la elipse "2ª jugada" hacia sus bordes. |
| 19 | tarea-19.svg | 9 | OK | Excelente pedagogía: pérdida en círculo (ventana 5 s), 1·2·3 saltan, 4·5 cierran; 4 mini-porterías. Solo se muestran 5 propios de un 7v7 (foco aceptable). Solapes mínimos "salta". | Sin cambios obligatorios. Opcional: separar los rótulos "salta" de las puntas de flecha. |
| 20 | tarea-20.svg | 8 | MENOR | Repliegue a las dos líneas muy claro. **Conteo**: el "frena eje" + 8 en el bloque ≈ 9 propios; la ficha dice 8 (el que frena debe ser uno de los 8). | Ajustar para que el jugador "frena eje" sea una de las 8 piezas del bloque (no un noveno), o aclarar en rótulo. |
| 21 | tarea-21.svg | 8 | MENOR | Transición por banda (robo → 1er pase a banda → corre carril → centro → ruptura) clara y correcta. Solape "3er hombre" sobre un rival. | Separar "3er hombre" del marcador rival contiguo. |
| 22 | tarea-22.svg | 6 | MENOR | Jugadores rotulados genéricamente "own" (sin roles del 1-4-4-2), poco informativo. "zona de cambios de posesión" pisa un marcador. Plantilla escasa (≈6+POR por lado para un 8v8). | Rotular al menos las referencias clave (DC, MC, banda) en vez de "own"; mover el rótulo de la zona fuera del marcador; completar a 8 si es viable. |
| 23 | tarea-23.svg | 6 | MENOR | 1-4-4-2 propio completo y bien colocado, pero los textos de bonificación **cruzan marcadores rivales**: "+2 recuperar press alto…" atraviesa dos MC rojos; "+1 superar presión por suelo" pisa un DC azul. | Reubicar los rótulos de bonificación a las franjas libres de cada zona (sin cruzar fichas); reducir longitud del texto si hace falta. |
| 24 | tarea-24.svg | 6 | MENOR | La provocación clave ("**bandas resaltadas**") no se ve: los carriles están delimitados con líneas discontinuas pero **no tintados/resaltados**; pocos jugadores. | Tintar los dos carriles de banda con un sombreado de acento (zona) para que se lean como "zonas de robo/progresión premiadas"; añadir alguna ficha más de referencia. |
| 25 | tarea-25.svg | 8 | MENOR | Ajuste 1-4-4-2 vs salida de 3 + 10 entre líneas muy bien planteado (quién salta, quién tapa pivote, MC vigila al 10). "bajada MC al 10" usa la línea roja "bloqueo/corte" (semántica de marca/seguimiento, no de bloqueo); solapes "salta salida"/"tapa pivote" sobre los DC. | Cambiar la línea roja por grafismo de "marca/seguimiento" o ampliar la leyenda; separar los rótulos de los marcadores DC. |
| 26 | tarea-26.svg | 6 | MENOR | Concepto completísimo, pero el área superior está **muy saturada de etiquetas** ("central/penalti", "bloquea", "→1er palo", "→central", "→2º palo") que se pisan entre sí y con las fichas; el bloqueo (línea roja) corto y poco claro. | Repartir verticalmente los rótulos de las cuatro zonas de remate; alargar/aclarar la línea de bloqueo indicando bloqueador→defensor; dar aire al clúster del primer palo. |
| 27 | tarea-27.svg | 5 | BLOQUEANTE | Es el tablero más saturado: dentro del área se solapan "zona de peligro", "al hombre", "zona", "zona 1er palo", "poste", "banda a…" y varios marcadores ("zMC", textos cruzando fichas). La asignación zona/hombre/postes existe pero **cuesta leerla**; el destino del despeje es ambiguo. | Rehacer el etiquetado del área: una sola etiqueta por función (zona / al hombre / poste) bien separada; renombrar "zMC"; clarificar a qué DC llega el despeje (punta de flecha sobre la ficha). Reducir solapes texto-ficha en el bloque defensivo. |

---

## Resumen de puntuaciones

- **OK (≥9, sin defectos relevantes):** 2 → Tareas **3, 19**.
- **MENOR:** 23 → Tareas **1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26**.
- **BLOQUEANTE:** 2 → Tareas **5, 27**.
- **Puntuación media:** **6,9 / 10**.

Patrones transversales (afectan a casi todo el lote):
- **A) Texto sobre fichas/flechas**: rótulos de zona/acción que cruzan marcadores (5, 6, 11, 12, 13, 18, 23, 26, 27). Es el defecto dominante.
- **B) Uso semántico de la línea roja "bloqueo/corte"** para representar marcas/seguimientos (8, 25) o como elemento espurio (5). La leyenda solo declara "bloqueo/corte".
- **C) Inconsistencia de paleta** respecto al canon del curso (azul/rojo/acento), uniforme en las 27.

---

## Lista priorizada de correcciones

### BLOQUEANTES (resolver primero)
1. **Tarea 5** — Eliminar la línea roja espuria MI-MC; bajar LD para reconstruir la línea de 4 defensiva; corregir solapes "MI"/"MC"; verificar el sentido de la flecha de basculación.
2. **Tarea 27** — Rehacer el etiquetado del área (una etiqueta por función zona/hombre/postes, bien separadas), renombrar "zMC", clarificar el destino del despeje y eliminar solapes texto-ficha.

### MENORES de alto impacto (errores de contenido / concepto)
3. **Tarea 4** — Corregir rótulo "Z4→Z2" por **"Z1→Z2"** (error factual).
4. **Tarea 10** — Dibujar las carreras como **curvas** (no rectas) y añadir la sombra/cono al pivote (es la provocación central de la tarea).
5. **Tarea 24** — **Resaltar/tintar** los carriles de banda (provocación "bandas resaltadas" hoy invisible).
6. **Tarea 16** — Numerar el primer pase como "1" y renumerar el circuito; rotular el MC inicial.
7. **Tarea 20** — Cuadrar el conteo a 8 propios (el "frena eje" como una de las 8 piezas).
8. **Tarea 22** — Sustituir los rótulos genéricos "own" por roles del 1-4-4-2.

### MENORES de legibilidad (solapes texto-ficha)
9. **Tareas 6, 13, 23, 26** — Subir/reubicar los rótulos de zona/banda y bonificación para que no atraviesen marcadores.
10. **Tareas 12, 18** — Dar aire a los clústeres congestionados (press / 2ª jugada).
11. **Tareas 1, 2, 7, 9, 11, 15, 17, 21** — Reubicar etiquetas y flechas puntuales (detalle en la tabla).

### MENORES transversales (pasada global)
12. **Semántica de la línea roja** (8, 25): cambiar por grafismo de "marca/seguimiento" o ampliar la leyenda.
13. **Paleta**: alinear `#1565c0→#1d6fb8`, `#c62828→#c0392b`, `#ffd54a/#f5a623→#ffd24a` en las 27 para consistencia de marca.
