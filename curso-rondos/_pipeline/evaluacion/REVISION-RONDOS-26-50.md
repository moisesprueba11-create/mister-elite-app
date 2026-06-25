# Revisión de calidad — Pizarras RONDOS 26–50

**Revisor:** Control de calidad MISTER ÉLITE — curso "Rondos"
**Fecha:** 2026-06-23
**Lote:** `graficos/rondo-26.svg` … `rondo-50.svg` (25 pizarras)
**Método:** render a PNG (680 px) + cotejo con `ejercicios/03..07`. Verificación de relación numérica/color contra el SVG. Notación: poseedores AZUL, defensores ROJO, comodines ÁMBAR; cuadro con conos; porterías en finalización.

**Criterio:** estándar MUY ALTO. Se penaliza con dureza el solape de textos sobre fichas/elementos clave (legibilidad), porque rompe el "montable solo con la imagen".

---

## Tabla de evaluación

| Rondo | Archivo | Pts | Severidad | Defecto principal | Corrección PRECISA |
|------|---------|-----|-----------|-------------------|--------------------|
| 26 | rondo-26.svg | 8.0 | MENOR | Etiqueta "1 sube" / "2 sube" de las líneas de pasillo solapa con la línea roja y queda casi ilegible; "pasillo 1 (salida)" cortada por la ficha A1. Conos del rectángulo (triángulos ámbar) confusos con los comodines (también ámbar). | Mover textos de pasillo al margen izquierdo del rectángulo, fuera de las líneas; separar la etiqueta de A1. Diferenciar conos (usar marca distinta o gris) de los comodines ámbar. |
| 27 | rondo-27.svg | 5.0 | BLOQUEANTE | Zona de "profundidad" ilegible: se amontonan el comodín de profundidad (Cp), la flecha blanca, "profundidad", "3 ataca espacio" y "zona de profundidad" en 3 cm². No se distingue Cp ni se entiende la mecánica pivote→descarga→3.º hombre. | Reposicionar Cp claramente dentro de la banda de profundidad; separar las 3 etiquetas (una arriba, retirar texto redundante); recolocar la flecha blanca del 3.er hombre para que no cruce el texto. |
| 28 | rondo-28.svg | 4.5 | BLOQUEANTE | Texto "pasillo seguro" / "puente" / "5 a B" / "1 al puente" se superpone unos a otros y al comodín Cp en el pasillo central; "cuadro A"/"cuadro B" cortados por fichas (Ra/Rd). Cae el orden de los dos cuadros. | Subir el rótulo "puente" y bajar "pasillo seguro" separados; mover "cuadro A"/"cuadro B" a una esquina libre de cada cuadro; reubicar Ra y "Ra"/"cuadro A" para que no se solapen. |
| 29 | rondo-29.svg | 7.5 | MENOR | El texto inferior "Tras 8 pases, un azul conduce…" queda dentro de la caja de leyenda y medio tapado; A2 pisa el balón y el rótulo. Cuadro 15×15 no cerrado con conos visibles (solo líneas de campo). | Subir la consigna por encima de la leyenda; marcar las 4 esquinas del cuadro con conos; separar balón/A2. |
| 30 | rondo-30.svg | 7.5 | MENOR | "≤6 s" de la conducción de robo queda encima de la flecha y poco legible; las dos mini-porterías "meta" están bien pero pegadas al borde. Sin portero (correcto, son mini-porterías). | Desplazar "≤6 s" al lado de la flecha, no encima. OK en lo demás. |
| 31 | rondo-31.svg | 8.0 | MENOR | Las 4 mini-porterías se ven (lados), pero las etiquetas "1 cambia"/"2 gol lado libre" se cruzan con fichas A1/A2. Comodín C bien. | Separar las etiquetas de secuencia de las fichas; engrosar levemente las mini-porterías para lectura. |
| 32 | rondo-32.svg | 5.5 | BLOQUEANTE | Solape grave: "2 descarga", "3 llega y remata", "2ª línea", "pivote" y la flecha blanca se amontonan sobre A3/Pv. La consigna inferior "El pivote descarga…" queda dentro de la leyenda. "cuadro 16…" cortado por D2. | Espaciar las etiquetas de secuencia (1-2-3) a lo largo de la trayectoria; subir la consigna sobre la leyenda; recolocar "cuadro 16×16" libre. |
| 33 | rondo-33.svg | 6.5 | BLOQUEANTE | "remata" se imprime encima de P1 (portero) y es ilegible; "2 ataca" y "1" sobre la línea de pase poco claros. Porteros P1/P2 en rojo: coinciden en color con los defensores rojos → ambigüedad (¿portero o defensor?). | Mover "remata" fuera del portero; dar a los porteros un color/anillo distinto del rojo defensor (p. ej. borde amarillo o etiqueta "GK") para no confundir. |
| 34 | rondo-34.svg | 7.0 | MENOR | Dos zonas de disparo bien marcadas (arcos de conos) y portería con portero OK. Pero "3 chut ≤1 s" flota suelto y la consigna inferior "1" queda pisada por A1/A2 al borde. | Anclar "3 chut ≤1 s" a la zona de disparo; subir fichas A1/A2 o el rótulo para que no se corten. |
| 35 | rondo-35.svg | 5.0 | BLOQUEANTE | Muy cargada: en zona 3 se solapan "ZONA 3 · finalizar (2v1 + portero)", el "5", la ficha azul y la conducción "gol"; fichas de zona 1 usan icono de cono encima de la "P" (poco claro). Consigna inferior dentro de la leyenda. | Separar rótulo de zona de la mecánica; aclarar las fichas (no superponer cono+letra); subir consigna sobre leyenda. Las 3 zonas y portería se entienden, pero el detalle de cada zona no. |
| 36 | rondo-36.svg | 8.0 | MENOR | 3 equipos (A azul, B ámbar, D rojo) correctos (4+4+4). Riesgo: el equipo B en ÁMBAR se confunde con "comodín" de la leyenda (aquí B no es comodín, es equipo poseedor). Las flechas 1-2-3 se cortan con fichas. | Aclarar en leyenda/título que ámbar = "equipo B" en esta tarea (no comodín); separar números de secuencia de las fichas. |
| 37 | rondo-37.svg | 7.0 | MENOR | 4 cuartos marcados (C1–C4) y valores de pase rotulados, pero "0 mismo cuarto"/"1 cambia cuarto"/"3 diagonal" se solapan con fichas P y con la línea media; fichas genéricas "P"/"D" sin numerar. | Recolocar las 3 etiquetas de valor en zonas vacías de cada cuarto; aceptable la genericidad, pero numerar P1–P6 mejoraría seguimiento. |
| 38 | rondo-38.svg | 8.5 | OK | 4 cuadros 5v2 en paralelo claros, conos por cuadro, "Cuadro 1–4" legibles. "90 s/ronda" sobre el círculo central algo apretado pero legible. Sin defecto bloqueante. | Opcional: subir "90 s/ronda" para que no toque el círculo. |
| 39 | rondo-39.svg | 8.0 | MENOR | 6v2+comodín correcto; escalera de toques explicada en pie. "+1 toque" del comodín se imprime sobre el círculo central y roza la ficha C. | Separar "+1 toque" de la ficha del comodín y del círculo. |
| 40 | rondo-40.svg | 7.5 | MENOR | 5v3 + comodín de premio en banda OK; "rompe línea → activa premio" en ámbar sobre fondo verde con bajo contraste; "premio 15 s" pegado al borde derecho. | Aumentar contraste del texto ámbar (caja oscura) o cambiar a blanco; separar "premio 15 s" del borde. |
| 41 | rondo-41.svg | 8.0 | MENOR | 3 equipos de 3 (A/B azul-ámbar/D) correcto; mecánica de permanencia clara en los pies. La numeración de pase "1" suelta. Igual que R36: B ámbar puede leerse como comodín. | Aclarar que ámbar = equipo, no comodín; anclar el "1" a la flecha. |
| 42 | rondo-42.svg | 7.5 | MENOR | 6v4, 2 mini-porterías y mecánica "banca o arriesga" OK; "¿arriesga?" y "2 (cambio orient.)" bien, pero la conducción azul cruza el texto de mini-portería. Fichas "P"/"D" genéricas. | Desviar la conducción para no cruzar el rótulo "mini-portería"; numerar opcional. |
| 43 | rondo-43.svg | 8.5 | OK | 7v3, cuadro grande 22×22, flechas rojas de presión/bloqueo coordinada bien representadas; consigna clara. Solo "1" del pase algo suelto. | Anclar el "1" a la flecha de pase. Buena pizarra. |
| 44 | rondo-44.svg | 8.5 | OK | 8v1 en círculo, "el manín" central, secuencia 1-2-3 (cruza) clara; consigna y castigo en pie. La consigna inferior roza la caja de leyenda. | Subir levemente la consigna sobre la leyenda. Muy buena. |
| 45 | rondo-45.svg | 8.5 | OK | 8v2 con DOS balones; "bal.1" (ámbar) y "bal.2" (azul/conducción) diferencian bien los dos balones. Mecánica clara. Leyenda no incluye "conducción" pese a usarse para bal.2. | Añadir "conducción" a la leyenda (se usa para el 2.º balón). Notable. |
| 46 | rondo-46.svg | 8.5 | OK | 7v2+comodín, conos de 4 colores rotulados (ROJO/VERDE/AZUL/AMARILLO) en esquinas y código en pie: excelente para montar. "→ comodín (señal AMARILLO)" cruza una línea de pase pero legible. | Sin corrección crítica. Ejemplar para tarea cognitiva. |
| 47 | rondo-47.svg | 8.0 | OK | 9v3 carrusel; flecha blanca "se reubica" comunica bien el movimiento perpetuo; "1 pase" claro. Leyenda OK. La flecha de reubicación apunta a zona vacía (correcto). | Sin corrección crítica. |
| 48 | rondo-48.svg | 8.5 | OK | 8 azules en 4 parejas (elipses agrupando cada pareja) muy buena solución visual; 2 rojos; consigna "<3 m" clara. "1 (pareja a pareja)" legible. | Sin corrección crítica. Excelente lectura del concepto de parejas. |
| 49 | rondo-49.svg | 8.5 | OK | 8 azules numerados 1–8, 2 rojos; "reloj"/"salto" rotulados sobre flechas amarilla/blanca: el concepto de número+sentido se entiende. "reloj" en ámbar bajo contraste. | Subir contraste de "reloj"; por lo demás, muy clara. |
| 50 | rondo-50.svg | 8.0 | OK | Gran rondo 12v3 (la olla), círculo amplio, secuencia 1-2 y "cruza" representada; consigna premio/castigo en pie. "cruza" en ámbar pisa la ficha roja D y baja contraste. | Separar "cruza" de la ficha D y subir contraste. Buen cierre. |

---

## Resumen por severidad

| Severidad | Rondos | Nº |
|-----------|--------|----|
| **BLOQUEANTE** | 27, 28, 32, 33, 35 | **5** |
| **MENOR** | 26, 29, 30, 31, 34, 36, 37, 39, 40, 41, 42 | **11** |
| **OK** | 38, 43, 44, 45, 46, 47, 48, 49, 50 | **9** |

**Media del lote: 7.5 / 10**

---

## Lista priorizada de correcciones

### P0 — BLOQUEANTES (impiden montar la tarea solo con la imagen)
1. **R28** (4.5) — Desamontonar el pasillo-puente central: rótulos "puente"/"pasillo seguro"/"5 a B"/"1 al puente" y comodín Cp se pisan; mover "cuadro A/B" a esquinas libres. *Es la pizarra peor del lote.*
2. **R27** (5.0) — Reconstruir la zona de profundidad: el comodín Cp, la flecha blanca y 3 etiquetas ocupan el mismo punto; hacer visible Cp y la mecánica pivote→3.er hombre.
3. **R35** (5.0) — Aligerar zona 3: separar rótulo de zona, "5", ficha azul y conducción "gol"; aclarar fichas de zona 1 (cono+letra superpuestos); subir consigna sobre leyenda.
4. **R32** (5.5) — Espaciar la secuencia 1-2-3 (descarga/llegada/remate) que se amontona sobre A3/Pv; subir consigna inferior fuera de la leyenda.
5. **R33** (6.5) — Quitar "remata" de encima del portero; **dar a los porteros (P1/P2) un color distinto del rojo defensor** para eliminar la ambigüedad portero↔defensor.

### P1 — MENORES recurrentes (patrón del lote)
6. **Textos de secuencia/consigna que pisan fichas o líneas**: R26, R29, R31, R34, R37, R39, R42 — reanclar etiquetas a su flecha y dejarlas en zonas vacías.
7. **Consigna inferior dentro de la caja de leyenda**: R29, R32, R34, R35 — subir el texto unos px por encima de la leyenda.
8. **Bajo contraste de texto ámbar sobre verde**: R40, R49, R50 — pasar a blanco o ponerle caja oscura.
9. **Conos (triángulos ámbar) confundibles con comodines (círculos ámbar)**: R26 (y en general) — diferenciar marca o color de los conos.
10. **Ámbar = "equipo poseedor B", no comodín** en R36 y R41 — aclararlo en título/leyenda para que no se lea como neutral.
11. **Leyenda incompleta**: R45 usa conducción (2.º balón) sin listarla → añadir entrada.

### Aciertos a mantener (referencia de calidad del lote)
- **R46** (conos de 4 colores rotulados + código en pie), **R48** (elipses agrupando parejas), **R49** (azules numerados 1–8), **R45** (dos balones diferenciados por color de flecha), **R38** (4 cuadros en paralelo), **R43**, **R44**. Son el estándar al que deben subir las bloqueantes.

---

## Coherencia numérica (verificada contra SVG)
Todas las relaciones X v Y (+comodines) **coinciden en número y color** con el texto de `ejercicios/`:
R26 6A/3R/2C · R27 5A/3R/2C(Ca+Cp) · R28 4+4A/4R/1C · R29 5A/2R/1C+POR · R30 6A/4R · R31 5A/3R/1C · R32 4A/2R/1Pv+POR · R33 6A/3R/2GK · R34 6A/4R/1C+POR · R35 6A/3R/1C+POR · R36 4+4+4 · R37 6/3 · R38 4×(5v2) · R39 6A/2R/1C · R40 5A/3R/1C · R41 3+3+3 · R42 6/4 · R43 7/3 · R44 8/1 · R45 8/2 · R46 7/2/1C · R47 9/3 · R48 8/2 · R49 8/2 · R50 12/3.

**No hay ningún error de recuento ni de color de notación.** Todos los defectos del lote son de **legibilidad/composición** (solapes de texto) y de un caso de **ambigüedad de color** (porteros rojos en R33).

*MISTER ÉLITE — Moisés Díaz*
