# REVISIÓN DE CALIDAD — Diagramas de TEORÍA (14)

Curso **Sistema 1-3-4-3** (MISTER ÉLITE). Revisor: control de calidad de pizarras.
Método: render `cairosvg` a 680 px + lectura visual + cotejo con `graficos/PEDIDOS.md` y `_pipeline/CONVENCION.md`.
Estándar: coherencia con el 1-3-4-3, legibilidad (sin solapes), corrección táctica (línea de 3, mutación 3-2-5, línea de 5, tridente) y calidad.

> **Nota de método (importante):** a 680 px las etiquetas `POR` parecen leerse "PQR" en varios diagramas. **Verificado en el SVG fuente: el texto es "POR" en todos los casos** — es un artefacto de rasterizado de cairosvg (el círculo del dorsal 1 queda pegado bajo la "O" a font-size 9.5). NO es defecto. En PDF/HTML a resolución real se ve correcto.

## Tabla de evaluación

| Archivo | Punt. | Severidad | Defecto | Corrección precisa (coordenadas SVG) |
|---|---|---|---|---|
| `teoria-01-estructura.svg` | 9.5 | OK | Estructura base correcta: POR 1, DFC 6-5-4, CAR 3/2 abiertos, MC 8/10 escalonados (8 más bajo, 10 más alto), tridente EI 11 · DC 9 · ED 7. Coherente con convención y PEDIDOS. | Sin acción. (Opcional: el escalonamiento 8/10 podría exagerarse ~10 px más para enfatizar el doble pivote.) |
| `teoria-01-mutacion-325.svg` | 9.0 | OK | Mutación 1-3-4-3→1-3-2-5 bien resuelta: CAR 3 y 2 con flecha de subida a línea de 5; 5 carriles ocupados (3·11·9·7·2); bloque 3+1 (DFC 4-5-6 + MC 8) detrás; MC 10 enlace. Carriles punteados ayudan. | Sin acción. |
| `teoria-01-linea5.svg` | 9.0 | OK | Mutación sin balón correcta: zona punteada con línea de 5 en orden 3-6-5-4-2; carrileros bajan con flecha; MC 8/10 por delante; tridente arriba. Coincide con "bloque 1-5-2-3". | Sin acción. (Etiqueta "línea de 5" y "DFC líbero" muy juntas bajo el 5; legible.) |
| `teoria-01-distancias.svg` | 8.5 | MENOR | Todas las cotas del estándar presentes (centrales 8-12, doble pivote 6-10, entre líneas 10-15, bloque <35-40, POR 14-18). La cota "doble pivote 6-10 m" se traza como diagonal 8↔10 cruzando el círculo central; el texto "doble pivote / 6-10 m" (~x235,y520) queda algo pegado al borde del círculo y a la cota "entre líneas". | Separar el texto "doble pivote 6-10 m" ~12 px a la izquierda (x≈210) o subirlo fuera del círculo central para evitar el roce visual con la circunferencia (cx340,cy553,r57). |
| `teoria-01-vs-433.svg` | 8.0 | MENOR | Conceptos correctos (3 centrales vs 1 punta 3v1, zona 4v3, carrileros 2v1 al lateral). **El equipo rival (rojo) reutiliza dorsales 3/6/8/10/9 que coinciden con los del equipo propio (azul)**; solo el color los distingue. Además el equipo propio NO muestra el tridente (7/9/11), lo que es defendible por enfoque pero deja la mitad ofensiva vacía. | Etiquetar a los rivales por rol (LI/LD/MC/punta) en lugar de dorsal, o usar dorsales rivales distintos, para que un dorsal nunca tenga dos significados. Considerar añadir el tridente propio atenuado para contexto. |
| `teoria-02-paso-3-a-5.svg` | 9.0 | OK | Mecánica 3→5 clara: CAR 3/2 "CAR alto → retrocede" con flecha vertical de retroceso hasta alinearse con DFC 4-5-6 en zona punteada; basculación lateral implícita. Coherente con PEDIDOS. | Sin acción. (Subtítulo dice "basculación, no carrera frontal" pero las flechas son verticales/frontales; aceptable como esquema, el matiz lo da el texto.) |
| `teoria-02-pressing-gatillos.svg` | 9.0 | OK | Pressing orientado correcto: DC 9 curva (flecha roja de bloqueo/corte) tapando pase entre centrales; ED 7 salta al lateral L; balón a banda-trampa (zona punteada); MC 8 cobertura y DFC 4 "sube". Buen uso de leyenda bloqueo/corte. | Sin acción. (El EI 11 queda aislado abajo-izq sin función explícita; opcional añadir microetiqueta "cierra interior".) |
| `teoria-02-basculacion.svg` | 9.0 | OK | Basculación de la línea de 5 al lado del balón bien resuelta: zona desplazada al lado fuerte; CAR 2 "salta" al portador R; CAR 3 "cierra dentro" como 5.º defensor; "lado débil vacío"; MC 8/10 acompañan. Mecanismo "uno salta, dos cubren" legible. | Sin acción. |
| `teoria-03-salida.svg` | 8.5 | MENOR | Rombo de salida 3+1 correcto: POR 1 base, DFC 4-5-6 abiertos, MC 8 vértice, CAR 3/2 amplitud alta, superioridad "3v2"; flechas de pase y conducción del 5. **Los dos presores rivales se etiquetan ambos como dorsal "9" (rojo)** — dos jugadores rivales con el mismo número confunde. | Cambiar el dorsal de uno de los rojos (p. ej. uno "9" punta y otro "11"/"7" extremo) o etiquetarlos por rol genérico, para no repetir el "9". |
| `teoria-03-mutacion.svg` | 9.0 | OK | Construcción y mutación a 1-3-2-5 en zona media: CAR 3/2 suben (flechas), bloque 3+1 (DFC 4-5-6 + MC 8) detrás, MC 10 enlace flotante con pases punteados (8→10→7), 5 carriles. Coherente. | Sin acción. |
| `teoria-03-ultimo-tercio.svg` | 8.5 | MENOR | Último tercio bien planteado: desdoblamiento CAR 2 + ED 7 (2v1 al lateral L, zona punteada), centro punteado al área, 5 referencias (9 1.er palo, 11 2.º palo, 10 frontal, 3 carrilero contrario). Concepto completo. | El "ataque" (flecha vertical inferior-derecha) y el texto del pie "MISTER ÉLITE · Moisés Díaz" se cruzan visualmente (~x630,y960). Subir el ancla de la flecha ATAQUE ~20 px o acortarla para que no invada la franja de pie. |
| `teoria-04-transicion-of.svg` | 9.0 | OK | Transición ofensiva tras robo correcta: MC 10 recupera y pase de profundidad; tridente 11-9-7 ataca espacios (flechas verticales); CAR 3/2 "lanzados" por fuera; equilibrio 3+1 (DFC 4-5-6 + MC 8) en zona punteada atrás. Coherente con PEDIDOS. | Sin acción. |
| `teoria-04-transicion-def.svg` | 8.5 | MENOR | Transición defensiva 3-2-5 bien secuenciada (frenar-replegar-reorganizar): MC 8 frena (bloqueo rojo a R), EI 11 y ED 7 "repliegan", CAR 3/2 "vuelan" a reformar línea de 5 (zona punteada con 6-5-4). **Falta el MC 10** en el dibujo (presente en mutación); aceptable como instantánea, pero rompe ligeramente la simetría del doble pivote. | Opcional: añadir MC 10 replegando junto al 8 para reflejar el doble pivote completo del bloque que se reorganiza. |
| `teoria-04-corner-of.svg` | 8.5 | MENOR | Córner ofensivo correcto: rematan DFC 4, 6 + DC 9 (+MC 10 llega al borde), saque del EI 11 (pase punteado al 1.er palo), resto en mini-línea de 3 (CAR 3 + DFC 5 + CAR 2) en zona punteada, MC 8 borde/rechace. Buen reparto. | La flecha "ATAQUE" inferior-derecha y el texto del pie se solapan (~x630,y960), igual que en último-tercio. Subir/acortar la flecha ATAQUE para liberar la franja de pie. |

## Lista priorizada de correcciones

### BLOQUEANTES (0)
Ninguno. Los 14 diagramas son tácticamente correctos y publicables.

### MENORES (6) — recomendadas antes de publicar
1. **`teoria-01-vs-433.svg`** — Dorsales rivales (rojo) duplican números del equipo propio (3/6/8/9/10). Etiquetar rivales por rol (LI/LD/MC/punta) o con dorsales distintos. *(Impacto: legibilidad/coherencia.)*
2. **`teoria-03-salida.svg`** — Dos presores rivales ambos con dorsal "9". Diferenciar uno (p. ej. 9 y 11) o etiquetar por rol. *(Impacto: legibilidad.)*
3. **`teoria-03-ultimo-tercio.svg`** — Flecha "ATAQUE" invade el pie de página (cruce con "MISTER ÉLITE · Moisés Díaz", ~x630,y960). Subir/acortar la flecha. *(Impacto: estética.)*
4. **`teoria-04-corner-of.svg`** — Mismo cruce flecha ATAQUE ↔ pie (~x630,y960). Subir/acortar. *(Impacto: estética.)*
5. **`teoria-01-distancias.svg`** — Texto "doble pivote 6-10 m" pegado al círculo central y a "entre líneas". Reubicar ~12 px (x≈210) o fuera del círculo (cx340,cy553,r57). *(Impacto: legibilidad.)*
6. **`teoria-04-transicion-def.svg`** — Falta MC 10 del doble pivote en la reorganización. Añadirlo junto al 8 (opcional). *(Impacto: completitud táctica.)*

### OK directos (8)
`teoria-01-estructura` · `teoria-01-mutacion-325` · `teoria-01-linea5` · `teoria-02-paso-3-a-5` · `teoria-02-pressing-gatillos` · `teoria-02-basculacion` · `teoria-03-mutacion` · `teoria-04-transicion-of`.

## Resumen
- **OK: 8 · MENOR: 6 · BLOQUEANTE: 0**
- **Media: 8.79 / 10**
- Lote sólido y coherente con la convención del 1-3-4-3. Sin bloqueantes. Las 6 mejoras menores son de legibilidad/estética (duplicación de dorsales rivales, dos solapes flecha-pie, una cota apretada) y una de completitud opcional. El falso "PQR" es artefacto de render, no defecto.
