# Índice de diagramas pedidos (PEDIDOS) — Curso 1-4-3-3

> Lista completa de pizarras a generar con el motor `graficos/lib/pitch.py`. Convención de dorsales del curso (POR 1 · LD 2 · LI 3 · DFC 4/5 · pivote 6 · interiores 8/10 · ED 7 · DC 9 · EI 11). Coordenadas: x 0..100 (izq→der), y 0..100 (fondo propio abajo → fondo rival arriba); ataque hacia arriba. Pie de marca **MISTER ÉLITE — Moisés Díaz**.
>
> **Total: 43 diagramas** — 17 de teoría (`teoria-NN-slug.svg`) + 26 de tareas (`tarea-01..26.svg`, número = número de tarea). Cada una de las 26 tareas tiene **exactamente un** placeholder, situado tras su bloque *Organización*.

---

## Diagramas de teoría (17)

| Archivo | Dónde se usa | Qué debe mostrar |
|---|---|---|
| `teoria-01-estructura-base.svg` | M01 §1 | Formación base 1-4-3-3 con todos los dorsales: línea de 4 (2-4-5-3), medio de 3 (8-6-10), tridente (7-9-11). Tres alturas escalonadas. |
| `teoria-02-cinco-carriles.svg` | M01 §2 | Campo dividido en 5 carriles verticales; ocupación tipo del 1-4-3-3 y la regla 2 por columna / 3 por línea. |
| `teoria-03-triangulo-vertices.svg` | M01 §3 | El triángulo del medio en dos paneles: ▽ vértice abajo (6 solo, 8/10 arriba) y △ vértice arriba (6+8 doble pivote, 10 enganche). |
| `teoria-04-transformacion-1325.svg` | M01 §4 | Transformación a 1-3-2-5: el 6 baja entre DFC (línea de 3), doble pivote por delante, 5 ocupando carriles arriba. Flechas de movimiento. |
| `teoria-05-repliegue-1451.svg` | M01 §5 | Repliegue a 1-4-5-1: extremos 7 y 11 bajando (flechas) a la línea de medios; 5 medios juntos + 9 de referencia. |
| `teoria-06-variantes-extremos.svg` | M01 §6 | Dos paneles: extremo a pie natural (desborde por fuera + centro) vs a pie cambiado (corta dentro + lateral da la amplitud). |
| `teoria-07-bloques.svg` | M02 §2 | Tres alturas de bloque (alto / medio / bajo) marcadas sobre el campo con la línea de 4 y la primera línea de presión. |
| `teoria-08-pressing-gatillos.svg` | M02 §3 | Presión alta: 9 orienta cerrando al pivote, extremo salta al lateral, interior salta al pivote, 6 cubre; lado débil basculado. Flechas de salto y cobertura. |
| `teoria-09-basculacion.svg` | M02 §4 | Basculación del medio de 3 + línea de 4 al lado del balón; 6 deslizado al carril del balón, interior débil estrechando, lateral débil cerrando a tercer central. |
| `teoria-10-espalda-laterales.svg` | M02 §5 | LD 2 subido; DFC 4 ensancha, interior del lado débil vigila la espalda, LI 3 cierra a tercer central (estructura 3+1). |
| `teoria-11-salida-rombo.svg` | M03 §1A | Salida en rombo: POR 1 vértice bajo, DFC 4/5 abiertos, pivote 6 de eje, laterales altos; el central libre conduce (flecha). |
| `teoria-12-salida-en-3.svg` | M03 §1B | Salida lavolpiana: el 6 baja entre DFC formando línea de 3; laterales subiendo; 3v2 ante dos puntas rivales. |
| `teoria-13-entre-lineas.svg` | M03 §2 | Recepción entre líneas: un interior baja a recibir de medio giro, el otro ataca la espalda (profundidad alterna). |
| `teoria-14-ataque-area.svg` | M03 §3 | Centro lateral y ataque de los 4 puntos: 9 al primer palo, interior al penalti, extremo lejano al segundo palo, 6 al borde. |
| `teoria-15-transicion-ofensiva.svg` | M04 §1 | Tras robar: primer pase vertical; tridente atacando profundidad (9 al eje, extremos a los pasillos), interior acompañando; 6 + 2 DFC + lateral de resto. |
| `teoria-16-contra-vs-repliegue.svg` | M04 §2 | Dos paneles de decisión: campo rival con cobertura → contrapressing (6 tapa centro); campo propio / desventaja → repliegue a 1-4-5-1. |
| `teoria-17-corner-ofensivo.svg` | M04 §3 | Córner ofensivo: bloque de rematadores con movimientos cruzados (primer palo, penalti, segundo palo), frontal para el rechace, 6 + lateral de seguro. |

---

## Diagramas de tareas (26)

| Archivo | Tarea | Qué debe mostrar |
|---|---|---|
| `tarea-01.svg` | T1 · Rombo de salida | 4v2: POR 1 vértice bajo, DFC 4/5 abiertos, pivote 6 en zona de conos entre 2 presionadores; mini-porterías de progresión en el medio. |
| `tarea-02.svg` | T2 · Salida en 3 | El pivote 6 baja entre 4 y 5 (línea de 3), laterales 2/3 subiendo, 3v2 ante dos puntas; tres puertas de progresión. |
| `tarea-03.svg` | T3 · 4v4+3 al hombre | Poseedores 4-5-6-8, POR 1 fijo detrás, laterales 2/3 comodines en banda; rival marca al hombre; flecha del pase del POR al desmarque. |
| `tarea-04.svg` | T4 · Extremos fijando | 7 y 11 pegados a la cal (zona de conos), salida por dentro y cambio de orientación al extremo aislado en 1v1. |
| `tarea-05.svg` | T5 · Salida bajo presión | Partido 8v8: equipo A iniciando desde POR contra presión alta del tridente B; mini-porterías de salida superada + 2 grandes. |
| `tarea-06.svg` | T6 · Rondo de carriles | 6v3 sobre 5 carriles: 6 central, 8/10 semiespacios, 2/3 exteriores; punto al recibir en carril interior y girar. |
| `tarea-07.svg` | T7 · Rotación del triángulo | Vértice abajo (6 solo) y vértice arriba (6+8 doble pivote, 10 enganche); 3 franjas y puertas en la franja alta. |
| `tarea-08.svg` | T8 · Recibir y girar | El DFC sirve al interior entre líneas con defensor a la espalda; control orientado y pase a 9 (apoyo) o filtración al 7. |
| `tarea-09.svg` | T9 · Transformación a 1-3-2-5 | Línea de 3 (4/5 + 6 o lateral invertido), doble pivote, 5 ocupando carriles arriba; puertas en el último tercio. |
| `tarea-10.svg` | T10 · Extremo salta al lateral | 9 orienta al pivote, ED 7 salta al lateral de fuera hacia dentro, interior cubre, EI 11 bascula; mini-porterías de robo. |
| `tarea-11.svg` | T11 · Interior salta al pivote | El interior salta al pivote rival y el 6 cubre por detrás (≤8 m); el resto bascula al lado del balón. |
| `tarea-12.svg` | T12 · Contrapressing 5 s | Al perder, 3 más cercanos cierran portador y líneas; el 6 dentro del carril central marcado tapando la progresión. |
| `tarea-13.svg` | T13 · Partido de presión | 10v10 en 1-4-3-3; equipo en foco presiona orientado a banda creando la trampa (extremo dentro, lateral sube, interior aprieta). |
| `tarea-14.svg` | T14 · 1v1 del extremo | ED 7 ataca al lateral; salida por fuera (centro) o por dentro a pie cambiado (disparo); 9 entra a rematar. |
| `tarea-15.svg` | T15 · Sociedad de banda | Trío 7-2-8: extremo fija, lateral overlap por fuera, interior de tercer hombre; llegada a fondo y centro/pase atrás. |
| `tarea-16.svg` | T16 · Cambio de orientación | Atraer a un lado y cambiar al extremo del lado débil aislado (defensor a ≥3 m) que ataca el 1v1 con el lateral. |
| `tarea-17.svg` | T17 · Fábrica de centros | Centro desde banda y ataque de los 4 puntos: 9 primer palo, interior penalti, extremo lejano segundo palo, 6 al borde. |
| `tarea-18.svg` | T18 · Extremo dentro / lateral fuera | ED 7 recibe entre líneas en carril interior y LD 2 ataca el espacio exterior; prohibido ambos en el mismo carril. |
| `tarea-19.svg` | T19 · El 9 fija y descuelga | El 6 conduce; el 9 elige apoyo (descarga al interior) o ruptura (ataca la espalda); 8 y 10 llegan de segunda línea. |
| `tarea-20.svg` | T20 · Llegada de interiores | Ataque por banda; un interior a la frontal y otro al corazón del área, entrando desde fuera en los últimos 2 s. |
| `tarea-21.svg` | T21 · Tercer hombre | Portador → 9 (apoyo de espaldas) → interior (descarga) → extremo / ruptura; finalización dentro del área. |
| `tarea-22.svg` | T22 · Finalización en 8 s | Oleada desde el 6: progresión por interior, amplitud al extremo, centro/pase y llegada al área en ≤8 s. |
| `tarea-23.svg` | T23 · Repliegue a 1-4-5-1 | Tras la pérdida, extremos 7 y 11 bajando a la línea de medios (bloque de 5); 9 de referencia, línea de 4 compacta. |
| `tarea-24.svg` | T24 · Transición en 3 pases | Al robar, primer pase vertical al 9 (apoyo) o extremo (profundidad), llegada de un interior; finalizar rápido. |
| `tarea-25.svg` | T25 · Decisión de transición | Línea central divide el campo: pérdida arriba → contrapressing; pérdida abajo → repliegue a bloque. |
| `tarea-26.svg` | T26 · Partido global | 11v11 en 1-4-3-3 con dorsales reales y zonas de bonificación (salida superada, último tercio). |
