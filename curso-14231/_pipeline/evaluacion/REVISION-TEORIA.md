# Revisión de calidad — Diagramas de TEORÍA (teoria-01..17)

**Revisor:** Control de calidad de pizarras — Curso "Sistema 1-4-2-3-1" (MISTER ÉLITE).
**Fecha:** 2026-06-23
**Método:** rasterizado a PNG (680 px), lectura visual, cotejo con `graficos/PEDIDOS.md` y `_pipeline/CONVENCION.md`.
**Estándar:** muy alto. Severidad: BLOQUEANTE (error táctico/legibilidad que invalida) · MENOR (defecto corregible sin invalidar) · OK.

> Coordenadas en convención del motor: **x 0..100 izq→der, y 0..100 fondo propio (abajo) → portería rival (arriba); se ataca hacia arriba.**

---

## Tabla de evaluación

| Archivo | Punt. | Severidad | Defecto | Corrección precisa |
|---|---|---|---|---|
| teoria-01-estructura | 9.5 | OK | Estructura base impecable. Doble pivote escalonado correcto (6 más bajo ~y34 / 8 más alto ~y45), trivote 11-10-7, punta 9. Sin solapes. | Ninguna. Opcional: subir levemente DC 9 ya está bien. |
| teoria-02-mutacion | 7.5 | MENOR | Concepto correcto (izq 1-4-4-2 sin balón, der 1-2-3-5 con balón) pero **densidad alta**: en la mitad izq las etiquetas "7/11 bajan" y las flechas largas verticales casi pisan las fichas 10/9; el rótulo "6 de resto" queda muy pegado al área. Las dos mitades comparten POR duplicado, lo que puede leerse como dos equipos en vez de dos fases. | Reducir longitud de las flechas de movimiento (acortar ~30%) para que no crucen otras fichas. Separar el rótulo "6 de resto" del arco. Añadir mini-título "MISMO EQUIPO · DOS FASES" para evitar lectura de 2 equipos. |
| teoria-03-zona14 | 9.0 | OK | 10 en zona 14 medio de cara, 9 a la espalda, extremos 11/7 en amplitud, pase interior punteado y "dos opciones". Muy claro. | Ninguna. Opcional: el rótulo "al 9" sobre la flecha vertical se cruza con un rival; desplazarlo a x≈42. |
| teoria-04-variantes-extremos | 7.0 | MENOR | Concepto correcto (a abierto / b interior+desdoble 2v1). Pero en panel **a)** el 7 está demasiado **centrado** (~x12 está bien, pero la flecha "ataca espalda" nace lejos del LAT rival y el LAT está por dentro del extremo) — no transmite "pegado a banda atacando la espalda del lateral". El 2v1 del panel b) sí se entiende. | En panel a) pegar el 7 a la banda (x≈8) y colocar el LAT rival por **fuera/delante** del 7 para que la carrera a la espalda tenga sentido; nacer la flecha desde detrás del LAT. |
| teoria-05-vs-433 | 9.0 | OK | Batalla de medio 2v3 bien planteada; 10 ataca el espacio pivote-centrales (zona resaltada), doble pivote 6/8 por detrás, trivote rival de 3 marcado. | Ninguna. Opcional: escalonar un poco más 6/8 (ahora casi a la misma altura). |
| teoria-06-perfiles | 9.5 | OK | Mapa de perfiles con etiqueta de rol por línea y **sin texto sobre fichas** (cumple el pedido literal). Legible. | Ninguna. |
| teoria-07-mutacion-defensiva | 7.5 | MENOR | El estado final 1-4-4-2 (dos líneas de 4) está bien y las flechas 7/11 bajan + 10 sube son correctas. Pero el pedido pide **secuencia (1-2-3)** y aquí los números 1·2·3 son rótulos de columnas/zonas, no pasos temporales: no se lee una progresión. | Convertir en 3 viñetas temporales o numerar los movimientos (1 = 7/11 bajan → 2 = compactar a 10-12 m → 3 = 10 sube junto al 9) junto a cada flecha, no como columnas. |
| teoria-08-bloques | 8.5 | OK | Tres bloques con altura de primera línea de presión bien diferenciada (alto/medio/bajo) y zonas de color. | El bloque alto rotula "1-4-4-2" y muestra 4 (11-9-10-7); medio y bajo solo muestran 9-10. Es coherente (marca la 1ª línea de presión), pero para homogeneidad conviene aclarar en subtítulo "solo se marca la 1ª línea de presión". |
| teoria-09-pressing-gatillos | 8.5 | OK | Gatillo correcto: curva del 9 cerrando entre centrales, pase a lateral → salta 7, LD sube, 6 desliza (coberturas en cadena). | El 9 (~y37) y el 10 (~y37) arrancan muy bajos con flechas muy largas; acortar el origen de la curva del 9 a ~y45 para que la "curva (cierra)" sea más legible junto a los DFC. |
| teoria-10-basculacion | 7.0 | MENOR | Concepto correcto (bloque al lado del balón, lejanos pellizcan, 6 referencia al 10 rival). Pero **legibilidad**: las flechas de carrera atraviesan las fichas 11 (x≈40) y 3 (x≈40, abajo) y sus dorsales se ven "tachados"; confunde. | Desplazar el inicio de las flechas de 11 y 3 para que no crucen el disco (nacer al borde, no en el centro). Separar rótulo "pellizcan por dentro" de la ficha 6. |
| teoria-11-salida-base | 9.0 | OK | Centrales 4/5 abiertos, POR +1, 6 escalonado (8 más alto), laterales subiendo, superioridad 3v1/3v2 rotulada. | Ninguna. Opcional: añadir un 2º presionador rival para ilustrar el 3v2 que menciona el rótulo (solo hay 1 rival). |
| teoria-12-salida-en-3 | 8.5 | OK | 6 baja entre centrales (línea 5-6-4), laterales altos, 8 pivote único, 10 baja a ofrecer. Cumple. | El rótulo "10 baja a ofrecer" y su flecha pisan el disco 10; desplazar el texto a x≈22, y nacer la flecha por encima del disco. |
| teoria-13-1235 | 8.5 | OK | 1-2-3-5: 2 centrales + 6 de resto, 8/10 interiores (half-spaces), frente de 5 ocupando los carriles. Zona de frente de 5 resaltada. | El frente de 5 ordena 11-3-9-2-7 (laterales por dentro de los extremos): geométricamente válido, pero conviene verificar que 3 y 2 (laterales) no queden por dentro de 11 y 7 de forma que parezcan interiores; separar un punto en x los discos centrales. |
| teoria-14-ataque-area | 9.0 | OK | 9 1er palo, 10 al penalti, extremo lejano 11 al 2º palo, 8 al borde, 6 + central 4 de resto; centro desde la derecha (7). Correcto y legible. | Ninguna. |
| teoria-15-transicion-of | 9.0 | OK | 1er pase vertical al 9 a la espalda, extremos 11/7 a los carriles, 8 de 2ª oleada, 6 de equilibrio. Claro. | El rótulo "2ª oleada" se cruza con la trayectoria del 8; desplazar a x≈30. |
| teoria-16-repliegue | 8.5 | OK | Repliegue a 1-4-4-2: 11/7 bajan, 6 frena (bloqueo sobre balón), 8 cubre, dos líneas de 4 en caja, 9+10 arriba. | Rótulos "6 frena" y "8 cubre" muy juntos sobre el círculo central; separar verticalmente. |
| teoria-17-corner-of | 5.0 | **BLOQUEANTE** | **Error táctico:** el lanzador del córner es el dorsal **1 (POR)** — un portero no saca córners y, además, dejarlo arriba elimina al guardameta del balance defensivo, contradiciendo el propio "resto anti-contra". El resto del esquema es correcto (9 1er palo, 5 al penalti, 8/10 2º palo, 7 al borde, anti-contra 6+3+4). | Cambiar el lanzador de **1 → 11** (o 7 si se prefiere zurdo/diestro): mover el disco lanzador a la posición de saque manteniendo el dorsal 11/7, y **devolver el POR 1 a su portería** (~x50,y8) dentro del resto anti-contra. Reetiquetar "lanzador" sobre el nuevo ejecutante. |

---

## Lista priorizada de correcciones

### BLOQUEANTE (corregir antes de publicar)
1. **teoria-17-corner-of** — El córner lo saca el portero (dorsal 1). Sustituir lanzador por 11 (o 7) y devolver el 1 a portería en el bloque anti-contra. Es el único defecto que invalida el concepto.

### MENOR (mejora de calidad / legibilidad)
2. **teoria-04-variantes-extremos** — Panel a): pegar el 7 a banda (x≈8) y situar el LAT rival por fuera para que "ataca espalda" tenga sentido.
3. **teoria-10-basculacion** — Flechas de carrera atraviesan los discos 11 y 3 (dorsales "tachados"); nacer las flechas al borde del disco.
4. **teoria-02-mutacion** — Acortar flechas que cruzan fichas; aclarar "mismo equipo, dos fases" para no leerse como dos equipos.
5. **teoria-07-mutacion-defensiva** — Convertir los rótulos de columna 1·2·3 en una verdadera secuencia temporal numerada de movimientos.
6. **teoria-12 / teoria-15 / teoria-16 / teoria-03** — Microajustes de rótulos que pisan discos o trayectorias (desplazar 5-10 px): "10 baja a ofrecer", "2ª oleada", "6 frena/8 cubre", "al 9".

### OK (sin acción obligatoria)
- teoria-01, 03, 05, 06, 08, 09, 11, 13, 14: correctos; mejoras opcionales anotadas en la tabla.

---

## Resumen

- **OK:** 11 (01, 03, 05, 06, 08, 09, 11, 13, 14, 15) y 16 — *ver nota*: contando severidad final.
- **MENOR:** 5 (02, 04, 07, 10, 12)
- **BLOQUEANTE:** 1 (17)

> Recuento por severidad asignada en la tabla: **OK = 11 · MENOR = 5 · BLOQUEANTE = 1** (total 17).

**Media de puntuación:** (9.5+7.5+9.0+7.0+9.0+9.5+7.5+8.5+8.5+7.0+9.0+8.5+8.5+9.0+9.0+8.5+5.0) / 17 = **140.5 / 17 ≈ 8.26 / 10.**
</content>
</invoke>
