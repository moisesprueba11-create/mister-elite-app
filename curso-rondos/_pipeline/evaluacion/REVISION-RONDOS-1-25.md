# Revisión de calidad — Pizarras RONDOS 1–25

**Revisor:** Control de calidad de pizarras · Curso "Rondos" (MISTER ÉLITE — Moisés Díaz)
**Fecha:** 2026-06-23
**Lote:** `graficos/rondo-01.svg` … `graficos/rondo-25.svg`
**Método:** render a PNG (cairosvg, 680px) + cotejo con `ejercicios/01..04` (Organización / Desarrollo / Provocaciones) y `_pipeline/NOTACION.md`.
**Notación de referencia:** poseedores AZUL · defensores ROJO · comodines ÁMBAR · espacio con conos.

---

## Resumen ejecutivo

- **OK:** 14 · **MENOR:** 9 · **BLOQUEANTE:** 2
- **Media:** **7,4 / 10**
- **Conclusión:** ningún rondo es inmontable, pero hay **2 defectos sistémicos** que afectan a casi todo el lote (fondo de campo completo y leyenda "zona") y **3 solapes de fichas** que tapan jugadores en el centro (rondos 20, 21, 25 → BLOQUEANTE en 20 y 25, MENOR en 21).

---

## Defectos SISTÉMICOS (afectan a casi todas las pizarras)

1. **[MENOR, transversal] Fondo de campo 11-vs-11 completo.** Todas las pizarras dibujan un campo entero (dos áreas, círculo central, flecha "ATAQUE", líneas de banda). Un rondo es una tarea de espacio reducido; el campo completo es ruido visual, descontextualiza la medida real (un "6×6 m" pintado sobre un campo de 100 m engaña la escala) y la flecha "ATAQUE" no tiene sentido en rondos no direccionales (1–14). **Corrección:** usar un fondo de césped neutro (sin áreas/círculo/ATAQUE) en los rondos NO direccionales; reservar la flecha "ATAQUE"/líneas de meta solo para los direccionales (21–25).

2. **[MENOR, transversal] Leyenda ámbar etiquetada "zona".** En las pizarras CON comodines (2, 6, 15, 17) la leyenda muestra la misma muestra ámbar como **"zona"** además de "comodín", y en las que solo tienen conos/zona ámbar la única entrada ámbar es "zona". La notación oficial reserva el ÁMBAR para **comodines**; usar el mismo color para "zona" sombreada + conos + comodines es ambiguo. **Corrección:** separar muestras de leyenda — ámbar lleno = comodín; cuadro ámbar punteado = zona/área; triángulo = cono. Quitar "zona" cuando no haya área sombreada.

3. **[MENOR, transversal] Flechas de pase con punta tapada por la ficha receptora.** En casi todos los rondos la punta del pase (marker_end) queda parcialmente bajo la ficha de destino (P2/P3, etc.), restando claridad al sentido. **Corrección:** acortar el segmento del pase ~16px antes del centro de la ficha receptora.

4. **[MENOR, transversal] Geometría no coincide con el subtítulo en varios casos.** Rondos descritos como "pentágono" (3), "hexágono" (7) o "cuadrado/círculo" se dibujan como **elipse** genérica (5, 7, 11, 13). **Corrección:** dibujar el perímetro real (pentágono, hexágono, cuadrado) que indica el ejercicio, con los conos sobre los vértices.

---

## Tabla de evaluación

| # | Archivo | Pts | Sev. | Defecto principal | Corrección precisa |
|---|---------|-----|------|-------------------|--------------------|
| 1 | rondo-01.svg | 8 | OK | Conos (triángulos ámbar) quedan justo bajo las fichas P1–P4 y casi no se ven; leyenda "zona" para el área 6×6. | Desplazar los conos ~10px hacia fuera de cada ficha; renombrar "zona" → "área del rondo". |
| 2 | rondo-02.svg | 8 | OK | Comodín "interior" correcto; punta del pase tapada por el comodín; leyenda duplica ámbar (comodín + zona). | Acortar pases; dejar una sola muestra ámbar = comodín. |
| 3 | rondo-03.svg | 6 | MENOR | Subtítulo "pentágono" pero los 5 azules NO forman pentágono (dispersos en línea) y no hay conos visibles. | Colocar los 5 azules en pentágono regular con 5 conos en los vértices; centrar a D1/D2. |
| 4 | rondo-04.svg | 8 | OK | 3v1 + E1/E2 en espera correcto; punta de pase bajo P2; flecha desmarque clara. | Acortar el pase a P2 (relevo legible). |
| 5 | rondo-05.svg | 7 | MENOR | Círculo bien, pero los 7 azules y el "por dentro" se ven; geometría es elipse irregular y D1/D2 muy juntos al centro. | Reglar el círculo (8 conos equidistantes); separar D1/D2 para distinguir el 7v2. |
| 6 | rondo-06.svg | 7 | MENOR | Una ficha azul aparece etiquetada **"B1"** en vez de "P1"; "·10 m" se solapa con D1. | Corregir "B1"→"P1"; mover la cota de medida fuera de D1. |
| 7 | rondo-07.svg | 6 | MENOR | Subtítulo "hexágono 12×12" pero se dibuja una **elipse**, no hexágono; conos ausentes. | Dibujar hexágono real con 6 conos en los vértices sobre los que están los 6 azules. |
| 8 | rondo-08.svg | 6 | MENOR | La **provocación clave (recuperar en 6 s / cronómetro)** NO aparece en la imagen pese a anunciarla el alt-text; la leyenda no incluye "pase" aunque hay flechas de pase. | Añadir icono/etiqueta "⏱ 6 s" junto a la presión roja; incluir "pase" en la leyenda. |
| 9 | rondo-09.svg | 8 | OK | Roles "presiona/orienta/intercepta" + bloqueo bien representados; punta de pase bajo P2. | Acortar el pase a P2. |
| 10 | rondo-10.svg | 9 | OK | Zona-trampa sombreada + "robar aquí = +3" muy claros; provocación perfectamente visible. | Sin cambios relevantes (pizarra modelo). |
| 11 | rondo-11.svg | 8 | OK | Bloque rojo compacto "<5 m" bien marcado con zona punteada; geometría elipse vs "cuadrado 12×12". | Dibujar cuadrado con conos en vez de elipse. |
| 12 | rondo-12.svg | 8 | OK | Puertas de conos a ambos lados y "conduce ≤8 s" hacia la puerta; transición clara. | Acortar la cota "12×12" que pisa a D1. |
| 13 | rondo-13.svg | 7 | MENOR | "1 toque" + "anticipa control" visibles; perímetro elipse en vez de cuadrado 9×9. | Dibujar cuadrado 9×9 con conos. |
| 14 | rondo-14.svg | 8 | OK | 3v3 con cobertura y "sin doblar marca"; texto largo se solapa con la cota "14×14". | Subir el texto descriptivo para que no pise la cota. |
| 15 | rondo-15.svg | 6 | MENOR | Subtítulo "**6 v 2**" pero solo hay **4 azules** dibujados (coherente con el texto "4 dentro", pero el subtítulo confunde); etiqueta "P3" pisa el origen del pase de cambio. | Cambiar subtítulo a "4 (+2 comodines) v 2"; separar P3 del arranque del pase. |
| 16 | rondo-16.svg | 8 | OK | 3 carriles con líneas punteadas y label carril 1/2/3; 6 azules + 3 rojos repartidos. | Mover la cota "18×12" que pisa a D2. |
| 17 | rondo-17.svg | 8 | OK | Comodines móviles C1/C2 en "lado opuesto" + pase "al opuesto (+2)" claro. | Acortar el pase a C1. |
| 18 | rondo-18.svg | 8 | OK | Interior "Pi" + "línea a romper" (roja) + "rompe línea +3" bien resueltos; D2 pisa ligeramente un pase. | Separar D2 del trazado del pase vertical. |
| 19 | rondo-19.svg | 8 | OK | Tercer hombre A→B→C con comodines C1/C2/C3 y 3 rojos; secuencia clara; R1 pisa una punta de pase. | Acortar el pase que llega bajo R1. |
| 20 | rondo-20.svg | 4 | **BLOQUEANTE** | **A3 (azul) queda completamente tapado por R3 (rojo)** en el centro (cx 302 vs 308): en el render solo se ven 5 azules de 6 → parece un 5v4. Además la **línea divisoria de zonas usa el color rojo "bloqueo/corte"**, confundiéndola con una acción defensiva. | Reubicar A3 fuera del solape (p. ej. a la izquierda de R3, separación ≥34px); pintar la divisoria de zona en blanco/neutro, no en rojo de bloqueo. |
| 21 | rondo-21.svg | 6 | MENOR | **P5 queda entre D1 y D2 y se ocluye** parcialmente (su "5" apenas se lee); por lo demás conexión fondo-a-fondo y objetivos O1/O2 correctos. | Desplazar P5 a una posición libre (no entre los dos rojos) con separación ≥34px. |
| 22 | rondo-22.svg | 8 | OK | Direccional salida(Cs)→meta(Cm) con pases numerados y línea de PARTIDA/META; A1 pisa una punta de pase. | Acortar el pase que termina bajo A1. |
| 23 | rondo-23.svg | 9 | OK | 3v2 + 2 bandas + objetivo; secuencia banda(1)→(2)→objetivo(3) impecable y fiel al texto. | Sin cambios relevantes (pizarra modelo). |
| 24 | rondo-24.svg | 7 | MENOR | 3 franjas + puertas de conducción + flecha de conducción cian correctos, pero las **divisorias de franja se pintan con el color "bloqueo/corte" (rojo)**, ambiguo frente a una acción defensiva. | Pintar las líneas de franja en blanco/punteado neutro; reservar el rojo para acciones de defensa. |
| 25 | rondo-25.svg | 5 | **BLOQUEANTE** | **A3 (azul) tapado por R1/R2** en el centro (A3 entre dos rojos, su ficha apenas asoma): se leen 5 azules de 6 → distorsiona la relación 6v4. | Reubicar A3 fuera del cúmulo central (separación ≥34px de R1 y R2) para que se cuenten los 6 azules. |

---

## Lista priorizada de correcciones

### BLOQUEANTE (corregir antes de publicar)
1. **Rondo 20** — A3 azul totalmente oculto bajo R3 → la imagen aparenta 5v4 en vez de 6v4. Reubicar A3 y cambiar la divisoria de zona a color neutro (no rojo de bloqueo).
2. **Rondo 25** — A3 azul oculto entre R1/R2 → aparenta 5v4 en vez de 6v4. Reubicar A3 con separación suficiente.

### MENOR (recomendado)
3. **Rondo 21** — P5 ocluido entre D1/D2 (no llega a falsear el conteo, pero cuesta leerlo). Reubicar.
4. **Rondo 08** — añadir la provocación visible "⏱ 6 s" (hoy la regla estrella no se ve) e incluir "pase" en la leyenda.
5. **Rondo 06** — corregir etiqueta "B1" → "P1".
6. **Rondo 15** — subtítulo "6 v 2" engañoso → "4 (+2 comodines) v 2".
7. **Rondos 3, 5, 7, 11, 13** — dibujar la geometría real (pentágono/hexágono/cuadrado) con conos en los vértices en lugar de una elipse genérica.
8. **Rondos 24 y 20** — no usar el color rojo "bloqueo/corte" para divisorias de zona/franja.

### SISTÉMICO (mejora global de calidad, aplica a todo el lote)
9. Sustituir el fondo de campo completo por césped neutro en los rondos NO direccionales (1–14, 16–17); reservar áreas/ATAQUE/líneas de meta para los direccionales (21–25).
10. Limpiar la leyenda ámbar: una sola semántica por muestra (comodín vs zona vs cono).
11. Acortar todas las flechas de pase ~16px para que la punta no quede bajo la ficha receptora.
12. Reubicar cotas de medida ("10 m", "12×12") que hoy se solapan con fichas D (rondos 6, 12, 14, 16).

---

*Revisión de pizarras · Rondos 1–25 · MISTER ÉLITE — Moisés Díaz*
