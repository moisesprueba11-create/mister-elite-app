# Revisión de calidad — Diagramas de TEORÍA (17)

Curso **Sistema 1-4-3-3** · MISTER ÉLITE — Moisés Díaz
Revisor: control de calidad de pizarras · Estándar alto
Fecha: 2026-06-23
Método: render PNG (cairosvg, width 680) + lectura visual + cotejo con `graficos/PEDIDOS.md` y `_pipeline/CONVENCION.md`.
Convención verificada: línea de 4 (LD 2 / LI 3 + DFC 4·5), pivote 6 + interiores 8/10, tridente ED 7 · DC 9 · EI 11.

## Tabla de evaluación

| Archivo | Punt. | Severidad | Defecto detectado | Corrección precisa |
|---|---|---|---|---|
| `teoria-01-estructura-base.svg` | 9.5 | OK | Estructura base correcta: línea de 4 (3·5·4·2), medio de 3 (10·6·8), tridente (11·9·7), tres alturas escalonadas. Dorsales y abreviaturas conformes. Sin solapes. | Ninguna. |
| `teoria-02-cinco-carriles.svg` | 9.5 | OK | 5 carriles bien rotulados (banda/semiesp./centro); ocupación tipo correcta; regla "2 por columna / 3 por línea" legible. Sin solapes texto-ficha. | Ninguna. |
| `teoria-03-triangulo-vertices.svg` | 7.0 | MENOR | Dos orientaciones (▽ izq con 6 bajo + 8/10 arriba; △ der con 6+8 doble pivote + 10 enganche) correctas, PERO ambos paneles comparten un único campo sin separador claro de marco, y la caption "6 solo: 2 interiores llegadores" (y≈817) queda muy baja y aislada del cluster del panel ▽. Riesgo de lectura ambigua de a qué panel pertenece cada token. | Reforzar la división de paneles con una línea vertical sólida en x=340 (como en teoria-16) o un sombreado de medio campo; subir la caption del panel ▽ a y≈700 para acercarla a los tokens 8/10. |
| `teoria-04-transformacion-1325.svg` | 8.5 | MENOR | Transformación 1-3-2-5 correcta: línea de 3 (5·6·4), doble pivote (10·8), 5 arriba (3·11·9·7·2). Flecha "6 baja" y subidas de laterales OK. Caption "última línea = 5 carriles ocupados" (y≈473) cae en zona media, lejos de la última línea real (arriba), levemente desorientadora. | Mover la caption "última línea = 5 carriles ocupados" arriba, a y≈300-320, justo bajo la fila de los 5 atacantes. |
| `teoria-05-repliegue-1451.svg` | 9.5 | OK | Repliegue 1-4-5-1 impecable: 7 y 11 bajan (flechas) a la línea de medios (11·10·6·8·7), 9 de referencia, línea de 4 compacta. Conforme a la convención. | Ninguna. |
| `teoria-06-variantes-extremos.svg` | 8.0 | MENOR | Dos variantes correctas (pie natural: desborde+centro; pie cambiado: corta dentro, lateral da amplitud). En panel derecho ED 7 (y≈553) y LD 2 (y≈648) quedan muy juntos verticalmente en el mismo carril exterior; legible pero apretado. La flecha cian "corta dentro" apunta correctamente hacia dentro/arriba. | Separar LD 2 del panel derecho hacia abajo (y≈690) o hacia el carril, para airear el cluster ED+LD; opcional añadir línea divisoria de paneles en x=340. |
| `teoria-07-bloques.svg` | 9.5 | OK | Tres alturas de bloque (alto/medio/bajo) bien zonificadas con cotas (~65/55/20 m); línea de 4 (3·5·4·2) y 1ª presión (9) ubicadas. Claro y didáctico. | Ninguna. |
| `teoria-08-pressing-gatillos.svg` | 9.0 | OK | Presión alta correcta: 9 orienta cerrando al pivote, 7 salta al lateral, 8 salta al pivote, 6 cubre, 11 bascula dentro, zona trampa lado débil; rivales en rojo + leyenda. Coherente con los gatillos. | Ninguna. (Artefacto "DFC"→aspecto "DOC" al rasterizar; ignorable.) |
| `teoria-09-basculacion.svg` | 9.0 | OK | Basculación correcta: 8 presiona lado balón, 6 desliza, 10 estrecha, línea de 4 deslizada (2 sube · 4 marca · 5 cubre · 3 cierra a 3er central), "líneas a ≤10-12 m". Coherente. | Ninguna. |
| `teoria-10-espalda-laterales.svg` | 8.5 | MENOR | Estructura 3+1 correcta: LD 2 sube, DFC 4 ensancha, 8 vigila la espalda, LI 3 cierra a 3er central. La zona discontinua "espalda del lateral / proyección" (x≈480-635) se solapa con la etiqueta vertical "ATAQUE" y la flecha de subida en x≈620, generando aglomeración en el borde derecho. | Recortar el ancho derecho de la zona discontinua a x≈610, o desplazar la etiqueta "ATAQUE" + flecha fuera del recuadro (no es bloqueante, sólo apretado). |
| `teoria-11-salida-rombo.svg` | 7.0 | MENOR | Rombo de salida correcto (POR 1 vértice bajo · DFC 5/4 · pivote 6 eje · laterales altos · 4 conduce). DEFECTO COSMÉTICO REAL: la flecha "ATAQUE" se dibuja con `y2="-29.5"`, sobresale por encima del campo (y=0) e invade la banda de cabecera, superponiéndose al borde superior-derecho del header. | En el `<line>` de ATAQUE acortar `y2` de `-29.5` a `≈90` (que termine dentro del campo, bajo el header que ocupa y 0-50). Mismo patrón en teoria-12. |
| `teoria-12-salida-en-3.svg` | 7.0 | MENOR | Salida lavolpiana correcta: 6 baja entre 4/5 (línea de 3), laterales suben, 3v2 ante 2 DC rivales, "superioridad +1". MISMO defecto cosmético: flecha "ATAQUE" con `y2="-29.5"` invade la cabecera arriba-derecha. Caption "3 (5-6-4)" es notación algo confusa. | Acortar `y2` de la flecha ATAQUE a `≈90`. Opcional: reescribir la caption como "línea de 3 (5·6·4) vs 2 puntas = +1". |
| `teoria-13-entre-lineas.svg` | 9.0 | OK | Recepción entre líneas correcta: bisagra interior (token central) filtra a 10 que baja a recibir de medio giro, y 8 ataca la espalda (profundidad alterna). Líneas rival en rojo, leyenda OK. Pase a 10 roza el token pero legible. | Ninguna. |
| `teoria-14-ataque-area.svg` | 8.5 | MENOR | Ataque de los 4 puntos correcto: 9 al 1er palo (lado del centro, der), 11 al 2º palo (izq), 8 al penalti, 6 al borde, 7 centra. Coherente con cruce de palos. La flecha "ATAQUE" inferior (`y2` baja) sobresale ligeramente hacia el pie de marca; la etiqueta "centro" roza el borde del área. | Acortar la flecha ATAQUE inferior para que no invada el footer; separar la etiqueta "centro" del trazo del área (mover a x≈500, y≈360). Menor. |
| `teoria-15-transicion-ofensiva.svg` | 9.5 | OK | Transición ofensiva correcta: 6 da 1er pase vertical, 9 al eje, 7/11 a los pasillos, 8 de 2ª oleada, resto defensivo 5+4+2 (6 + 2 DFC + lateral). Limpio y coherente. | Ninguna. |
| `teoria-16-contra-vs-repliegue.svg` | 9.0 | OK | Dos paneles de decisión correctos: izq pérdida alta con cobertura → contrapressing (9/11 cierran al RIV, 6 tapa centro); der pérdida con desventaja → repliegue 1-4-5-1 (11·6·8·7 + 9 ref + línea de 4). Separador central presente. Coherente. | Ninguna. (Levemente denso pero legible.) |
| `teoria-17-corner-ofensivo.svg` | 8.5 | MENOR | Córner ofensivo correcto: 10 lanza, centro a zona de palos, rematadores con movimientos cruzados (1er palo/penalti/2º palo), 7 arrastre, 8 frontal/rechace, 6+2 seguro de transición. Los rematadores se rotulan por rol pero SIN dorsal, mientras 7/8/6/2 sí lo llevan (inconsistencia menor de etiquetado). Flecha ATAQUE inferior roza el footer. | Asignar dorsales a los 3 rematadores (p. ej. 9 al 1er palo, 11 al 2º palo, interior al penalti) para coherencia con el resto del lote; acortar la flecha ATAQUE inferior. Menor. |

## Lista priorizada de correcciones

### BLOQUEANTE
- (ninguno)

### MENOR — corregir antes de publicar
1. **teoria-11 / teoria-12** — Flecha "ATAQUE" con `y2="-29.5"` invade la cabecera. Acortar a `y2≈90`. (Defecto idéntico, mismo fix, dos archivos.)
2. **teoria-03** — Falta separador claro de paneles ▽/△ y la caption del ▽ queda descolgada. Añadir divisoria vertical en x=340 y subir caption a y≈700.
3. **teoria-14 / teoria-17** — Flecha "ATAQUE" inferior invade el footer; acortar su extremo. En teoria-17, además dar dorsal a los 3 rematadores.
4. **teoria-10** — Zona "espalda del lateral" se solapa con etiqueta "ATAQUE" en el borde derecho; recortar el recuadro a x≈610.
5. **teoria-04** — Reubicar la caption "última línea = 5 carriles" a y≈300-320 (junto a la fila atacante).
6. **teoria-06** — Airear el cluster ED 7 + LD 2 del panel derecho (separar el 2 a y≈690).

### OK — sin cambios
teoria-01, 02, 05, 07, 08, 09, 13, 15, 16.

## Resumen
- **OK:** 9 (teoria-01, 02, 05, 07, 08, 09, 13, 15, 16)
- **MENOR:** 8 (teoria-03, 04, 06, 10, 11, 12, 14, 17)
- **BLOQUEANTE:** 0
- **Media:** 8.74 / 10

Veredicto: lote tácticamente sólido y conforme a la convención del 1-4-3-3 (línea de 4, medio de 3 con triángulo ▽/△, transformación 1-3-2-5, repliegue 1-4-5-1, tridente). Sin bloqueantes. Los defectos son cosméticos/de legibilidad (flechas ATAQUE que invaden cabecera/footer, separación de paneles, reubicación de captions). Apto para publicar tras los retoques menores listados.
