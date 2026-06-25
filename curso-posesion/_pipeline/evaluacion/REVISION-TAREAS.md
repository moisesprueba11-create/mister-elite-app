# Revisión de calidad — Pizarras de TAREAS (T1–T30)

Curso "Juego de posición: dominar con el balón" — MISTER ÉLITE · Moisés Díaz
Revisor: control de calidad de pizarras. Estándar alto. Lote: `graficos/tarea-01.svg` … `tarea-30.svg`.
Método: render PNG (cairosvg) + cotejo con `ejercicios/01..06` (Organización/Desarrollo/Provocaciones) contra `_pipeline/NOTACION.md`.
Fecha: 2026-06-24.

## Resumen
- **OK: 24** · **MENOR: 5** · **BLOQUEANTE: 1**
- **Media: 8.4 / 10**
- Único bloqueante: **T11** (notación azul-cian mal usada + relación numérica no constructible).
- Patrón menor recurrente (Familia 4): pizarras con marco de **campo completo y porterías dibujadas** aunque la tarea sea "sin portería", y **rojos sin numerar** (todos "D"/"R"). No bloquea el montaje pero rebaja precisión.

## Tabla de evaluación

| Tarea | Archivo | Pts | Sev. | Defecto | Corrección precisa |
|---|---|---|---|---|---|
| T1 Rondo orientación 2 colores | tarea-01.svg | 8 | MENOR | El material pide "cono **amarillo** izq + cono **rojo** der" por lado; en la pizarra los conos de orientación son todos triángulos **ámbar** iguales: no se distingue amarillo/rojo, que es justo la referencia del ejercicio. Etiquetas P5/P6 se solapan con la flecha de control. | Pintar el cono izquierdo en amarillo y el derecho en rojo (par por lado) para que la referencia de orientación sea legible; separar la etiqueta del jugador receptor de la punta de flecha. |
| T2 Rondo al comodín opuesto | tarea-02.svg | 9 | OK | 4 azules (P1,P2 y dos receptores) + 2 rojos (D1,D2) + 2 comodines ámbar (CA izq, CB der) en bandas cortas opuestas. Secuencia A→pared→cambio→B clara. | — |
| T3 Rondo 3 jaulas | tarea-03.svg | 8 | OK | 6 azules (2/zona) + 3 rojos (1/zona) = coincide con subtítulo 6v3. Progresión Z1→Z2→Z3 con pase que cruza la ventana, visible. (Nota: el .md describe "2 az + 1 puente/zona" = 9 az, incoherencia del texto, no de la pizarra). | Opcional: alinear el texto del ejercicio con la pizarra (la pizarra 6v3 es la correcta). |
| T4 Rondo 4+1 central | tarea-04.svg | 9 | OK | 4 azules + 2 rojos + 1 comodín ámbar central (G). "Entra al central y sale a azul distinto" representado con pase G→P2. | — |
| T5 Rondo 2 puertas contiguas | tarea-05.svg | 9 | OK | 5 azules + 3 rojos. Dos puertas en lados **contiguos** (A arriba, B derecha). Conducción (azul) por la puerta libre B. Coherente. | — |
| T6 JdP clásico 4v4+3 | tarea-06.svg | 8 | OK | 4 az + 4 rojos + 3 comodines ámbar (2 banda + 1 central) = 7v4. Etiquetas C2/C3 rozan los conos del lado derecho pero se leen. | Separar ligeramente las etiquetas de comodín de los conos de esquina derechos. |
| T7 JdP 3v3+3 rombo | tarea-07.svg | 8 | OK | 3 az + 3 rojos + 3 comodines (arriba, abajo, lateral móvil). El 4.º vértice del rombo lo cierra un azul; la secuencia recorre el diamante. | — |
| T8 Cuadrícula 5 carriles | tarea-08.svg | 9 | OK | 3 az + 3 rojos + 3 comodines (carriles 1,3,5). 5 carriles numerados × 3 alturas. Regla de ocupación legible. | — |
| T9 5v5+3 zonas finalización | tarea-09.svg | 8 | OK | 5 az + 5 rojos + 3 comodines (2 banda + central). Dos zonas de finalización enfrentadas. Pequeño racimo de etiquetas a la izquierda (banda/centro/C1/P1). | Aclarar el racimo de etiquetas del comodín de banda izquierdo. |
| T10 4 porterías 4v4+2 | tarea-10.svg | 9 | OK | 4 az + 4 rojos + 2 comodines. 4 mini-porterías (par de conos por lado). Gol por la portería sin rojo, con pase. Coherente. | — |
| T11 Generar 3v2 por zonas | tarea-11.svg | 4 | **BLOQUEANTE** | (1) El **flotante** se pinta **azul-cian** y la leyenda lo llama "equipo B": viola la notación (cian = 2.º equipo poseedor), pero aquí pertenece al **mismo** equipo azul (el .md pide "peto distinto para el flotante **azul**"). (2) Relación numérica no cuadra: el .md exige 2v2 por zona (4 az) **+ flotante** = 5 propios vs 4 rojos; la pizarra solo muestra **3 azules + 1 flotante = 4 propios**, y la Zona A no es un 2v2 (1 az + flotante vs D1,D2). El "3v2" anunciado no es constructible con la imagen. (3) Etiquetas "flotante +1 / llega / crea 3v2 / F" apiladas e ilegibles. | Pintar el flotante **azul** con marca/peto distinto (NO cian); reservar cian solo para tareas a 2 equipos. Añadir el azul que falta en Zona A para que sea 2v2 real (4 az base) y situar el flotante entrando a Zona A → muestra el 3v2. Desapilar las etiquetas (una por línea). |
| T12 Hombre libre entre líneas | tarea-12.svg | 8 | MENOR | 4 az + 4 rojos + 1 comodín ámbar entre líneas. 3 franjas correctas. La **punta de flecha del pase tapa la etiqueta P4** (arriba-dcha), que por un instante parece "D4" (hay otro D4 rojo). | Desplazar la punta de flecha/etiqueta para que P4 sea inequívoco y no se confunda con el D4 rojo. |
| T13 Atraer-liberar 6v4 | tarea-13.svg | 7 | MENOR | 6 az (2 de banda + 4 interiores) + 4 rojos. Cambio a banda libre representado. Racimo de etiquetas arriba (D1/fija/jugador con balón) se solapa. | Espaciar el grupo superior izquierdo; numerar los azules interiores para contarlos sin esfuerzo. |
| T14 Tercer hombre | tarea-14.svg | 9 | OK | 5 az + 3 rojos + 1 comodín pivote ámbar. Cadena 1.º→pivote→descarga→3.er hombre→zona finalización, secuenciada y clara. | — |
| T15 4v3 dinámico relevo | tarea-15.svg | 9 | OK | 4 az + 3 rojos. Pase al libre + rotación al nuevo libre (P3 resaltado con aro de zona). Limpio. | — |
| T16 Las tres zonas 6v6+2 | tarea-16.svg | 7 | MENOR | 6 az numerados + 6 rojos + 2 comodines banda. **El .md dice "sin porterías" pero el campo se dibuja completo con áreas y porterías**. Rojos sin numerar (todos "D"). El "3" azul central queda parcialmente tapado por un rojo y la punta de flecha. | Usar marco neutro (rectángulo + líneas de zona) sin porterías; numerar los rojos; separar el azul "3" del rojo solapado. |
| T17 Romper líneas por puertas | tarea-17.svg | 7 | MENOR | 7 az + 5 rojos + 3 puertas internas con pares de conos a distintas alturas. Secuencia 1→cruza puerta→2.ª rotura. Igual que T16: **campo con porterías** pese a "sin portería"; rojos sin numerar. | Marco sin porterías; numerar rojos. |
| T18 Jugador-puente | tarea-18.svg | 7 | MENOR | 5 az + 5 rojos + 1 comodín-puente ámbar en línea media. Apoyo→dejada→superación clara. Mismo patrón: **porterías dibujadas** pese a "sin portería"; rojos sin numerar. | Marco sin porterías; numerar rojos. |
| T19 Cambio de orientación 8v6 | tarea-19.svg | 7 | MENOR | 8 az numerados + 6 rojos + 3 carriles con divisorias de conos + 2 líneas de gol laterales. Cambio diagonal izq→der + conducción a gol. Rojos sin numerar; densidad alta de etiquetas. | Numerar rojos; reducir solape de etiquetas en franja central. |
| T20 Pausa-aceleración | tarea-20.svg | 7 | MENOR | 6 az + 6 rojos + 3 comodines de zona (1/zona). Cerrojos entre zonas. Secuencia pausa→acelera→rompe. Rojos sin numerar; pizarra muy cargada. | Numerar rojos; aligerar etiquetas; (campo con porterías pese a "sin portería"). |
| T21 Del control a la ocasión | tarea-21.svg | 9 | OK | 6 az + 4 rojos + 1 comodín + **portero (POR)** con aro distintivo. Mini-porterías rojas al fondo opuesto. Zona creación→remate y línea, claras. | — |
| T22 Remate por zonas de centro | tarea-22.svg | 9 | OK | 7 az + 6 rojos + 2 comodines de banda + portero distinguible. Pasillos de banda con conos; ataque de los 3 espacios del área. Coherente. | — |
| T23 4v4+3 que termina en portero | tarea-23.svg | 9 | OK | 4 az + 4 rojos + 3 comodines (2 ext + central libre) + portero. Pase al central libre abre 2v1+portero. Claro. | — |
| T24 Dos equipos, dos porterías | tarea-24.svg | 9 | OK | **Uso correcto de azul-cian**: 8 azules vs 8 azul-cian (equipo B) + 2 comodines ámbar + 2 porteros. 3 zonas; cadena def→medio→ataque. Notación impecable. | — |
| T25 Superioridad efímera 3v2 | tarea-25.svg | 8 | MENOR | 5 az + 5 rojos + 1 comodín + portero. Conducción cruza línea → 3v2 (defensores "−2 m"). Coherente. La **flecha de conducción es cian** y la leyenda redefine cian como "conducción": colisiona con el código de color de la notación (cian = 2.º equipo). | Pintar la conducción en **azul** (no cian) para no chocar con el color reservado al 2.º equipo. |
| T26 Contrapresión 5 s | tarea-26.svg | 8 | OK | 6 azules numerados + 6 recuperadores "R" + 2 comodines. Presión al portador (carrera blanca) + trampas de presión (líneas de corte rojas). Concepto legible. | Opcional: numerar los R. |
| T27 Robar y conservar 6 pases | tarea-27.svg | 8 | OK | 2 equipos de 6 (azul vs azul-cian) + 3 comodines ámbar que cambian de bando. Robo + descargas. **Uso correcto de cian** (2 equipos reales). Algo cargada. | Verificar que se cuenten 6 vs 6 sin esfuerzo (aligerar). |
| T28 Transición 3 equipos | tarea-28.svg | 8 | OK | 3 equipos de 4: azul "A", azul-cian "B", rojo "D". 8 en posesión vs 4 presionando. **3 colores correctamente diferenciados**. Secuencia de pases. | — |
| T29 Recuperar y atacar portería | tarea-29.svg | 7 | MENOR | 6 az + 6 R + portero + mini-porterías. Zona de presión alta (discontinua roja). Robo + remate ≤8 s con carrera a portería. Defecto: los azules llevan **numeración duplicada** (dos "1", dos "2", dos "3") → confunde en un 6v6. | Numerar los 6 azules de 1 a 6 (sin repetir). |
| T30 Bloque de reacción 8 s | tarea-30.svg | 8 | OK | 7 az numerados (1–7) + 7 R + 1 comodín + 2 porteros + 3 zonas. Presiona→contrapresión→roba + flechas de repliegue (5,6). Rico y coherente. | Opcional: numerar los R. |

## Lista priorizada de correcciones

### BLOQUEANTE (corregir antes de publicar)
1. **T11** — Reconvertir el flotante de **azul-cian a azul con peto distinto** (cian queda reservado al 2.º equipo); **añadir el azul que falta** para que la Zona A sea un 2v2 real y el flotante materialice un 3v2 constructible desde la imagen; **desapilar** el bloque de etiquetas "flotante/llega/crea 3v2/F".

### MENOR (recomendado; mejora notación/legibilidad)
2. **T25** — Conducción en **azul**, no cian (color reservado al 2.º equipo).
3. **T29** — Eliminar numeración duplicada de los azules (1–6 únicos).
4. **T1** — Conos de orientación en **amarillo (izq) y rojo (der)**, no ámbar uniforme (es la referencia del ejercicio).
5. **T12** — Que la etiqueta **P4** no quede tapada por la flecha ni se confunda con el D4 rojo.
6. **Familia 4 (T16, T17, T18, T19, T20) + T29** — Patrón común: usar **marco sin porterías** donde el .md dice "sin portería" y **numerar los rojos** (hoy todos "D"/"R") para contar y leer la relación numérica de un vistazo.
7. **T13** — Espaciar el racimo de etiquetas superior izquierdo; numerar interiores.

### OK (sin acción)
T2, T3, T4, T5, T6, T7, T8, T9, T10, T14, T15, T21, T22, T23, T24, T26, T27, T28, T30 — coherentes, legibles y con notación correcta (porteros distinguibles en T21–T24; uso correcto de azul-cian en T24, T27, T28).

---
*MISTER ÉLITE — Moisés Díaz · Revisión de calidad de pizarras (Tareas).*
