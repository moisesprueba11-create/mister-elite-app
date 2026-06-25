# Revisión de calidad — Diagramas de TEORÍA + SESIONES

**Revisor:** Control de calidad de pizarras tácticas · curso *Sistema 1-4-4-2* (MISTER ÉLITE)
**Fecha:** 2026-06-22
**Lote:** 23 diagramas `graficos/teoria-*.svg` + `graficos/sesion-1.svg` + `graficos/sesion-2.svg` (25 en total)
**Método:** render a PNG (cairosvg, 680px) → lectura visual → cotejo con el placeholder/texto del módulo correspondiente → evaluación de coherencia, legibilidad, corrección táctica y calidad visual.

> Nota de sistema de coordenadas (de `lib/pitch.py`): `x` 0 (banda izq) → 100 (banda der); `y` 0 (fondo propio, abajo) → 100 (fondo rival, arriba). **El ataque propio va hacia ARRIBA (y creciente).** Las etiquetas de rol se dibujan SOBRE la ficha (centro de ficha `cy - r - 4`, radio 15 px). El rival (rojo) ataca hacia ABAJO (y decreciente).

---

## Tabla de evaluación

| Archivo | Punt. | Severidad | Defecto concreto | Corrección sugerida (precisa) |
|---|:---:|:---:|---|---|
| teoria-01-formacion-base.svg | 9.0 | OK | Etiquetas "pivote 6/8" rozan la línea de medio campo; todo legible. | Sin acción obligatoria. Si se busca el 10: subir ambos MC de y=47 a y=44 para despejar el círculo central. |
| teoria-02-carriles-franjas.svg | 8.5 | OK | Las etiquetas "FRANJA …" se ubican en el carril lateral izq (x=9); leves, pero compiten con el contorno. | Mover las 3 etiquetas FRANJA de x=9 a x=11 y bajar font-size a 8.5 para separarlas del borde. |
| teoria-03-perfiles-por-linea.svg | 9.0 | OK | "6 organizador" / "8 box-to-box" rozan el círculo central. | Subir los dos MC de y=47 a y=44 (igual que t01). |
| teoria-04-plano-vs-rombo.svg | 6.5 | MENOR | El rombo se dibuja con fichas RIVAL (rojas) y el plano con propias (azules): induce a leerlo como confrontación, no como dos alternativas de TU centro del campo. Etiquetas PLANO/ROMBO apiladas en el centro (y=48/52) confunden a qué mitad se refieren. | Pintar el rombo con `team="neutral"` (naranja) o `own`, no `rival`. Separar etiquetas: "PLANO" a y=44 y "ROMBO" a y=56 (cada una dentro de su mitad), no pegadas en la línea media. |
| teoria-05-variante-rombo.svg | 8.0 | MENOR | El borde discontinuo del rombo (zone 28,36→72,66) cruza por encima de las etiquetas "interior" de ambos INT y de "enganche". | Reducir la zona-guía a 30,38→70,62, o subir la etiqueta "enganche" de su posición a y=66 y bajar el rótulo "interior" a `cy+r+12` (debajo de la ficha) en los INT. |
| teoria-06-roles-defensivos.svg | 9.0 | OK | Limpio; todos los roles legibles, bloque medio realista. | Sin acción. |
| teoria-07-bloques-altura.svg | 6.5 | MENOR | La columna derecha está rotulada "primer presionador" pero las fichas son RIVAL (rojas, "DC"). El primer presionador es jugador PROPIO; pintarlo de rival contradice la leyenda de colores y el concepto. | Cambiar las 3 fichas de la derecha a `team="own"` con label "DC" (delantero propio que presiona) y mantener la última línea propia (azul) a la izquierda; o renombrarlas como referencia rival "balón rival" en lugar de "primer presionador". |
| teoria-08-pressing-sombra.svg | 7.5 | MENOR | La carrera del 1.º DC se llama "curva" pero se dibuja recta y corta, casi tapada por la caja SOMBRA y el balón. Etiqueta "curva" pisa el borde izq de la caja. | Usar `kind="dribble"` (ondulada) para sugerir la curva, alargar la carrera (44,62→39,77) y mover la etiqueta "curva" a x=34,y=70 fuera de la caja. |
| teoria-09-basculacion.svg | 7.0 | MENOR | "pisa centro" pisa la ficha MI y el círculo central; "banda lejana concedida" se solapa con el borde de zona y la línea media; la flecha "bascula" queda baja (y=35), separada del bloque. | Mover "pisa centro" sobre la ficha (`cy-r-4`); bajar el rótulo de zona a y=50 alineado dentro del rectángulo; subir la flecha bascula a y=42. |
| teoria-10-trampa-banda.svg | 7.0 | MENOR | Cúmulo en esquina sup-der: "pase concedido" pisa al DFC rival y el borde de zona; "recibe (gatillo)" pisa al LAT; flecha "tapa interior" corta y rótulo encima del MC. | Separar rótulos: "pase concedido" a x=52,y=70 (sobre césped libre); "recibe (gatillo)" a `cy+r+12` (debajo del LAT). Alargar la flecha block del MC (58,54→64,64). |
| **teoria-11-fuera-de-juego.svg** | **5.0** | **BLOQUEANTE** | **Geometría de fuera de juego INVERTIDA.** El rival ataca hacia abajo (y↓); "a la espalda" de la línea (y=50) = y<50. Pero los 2 DC marcados "FUERA DE JUEGO" están en y=60/62 (ARRIBA de la línea), lado en el que estarían EN JUEGO. El diagrama contradice el concepto. Además rótulos "central ordena" / "línea de fuera de juego" / "SUBEN JUNTOS" pisan fichas y la línea naranja. | Recolocar los 2 DC rivales en y=44 y y=46 (BAJO la línea defensiva, lado del fondo propio), con la línea de fuera de juego en y=50 y la defensa subiendo (flechas hacia y↑) dejándolos pasados. Separar rótulos del trazo: "línea de fuera de juego" a y=55; "SUBEN JUNTOS" a y=40 sobre césped libre. |
| teoria-12-problema-2v3.svg | 8.0 | MENOR | "hombre libre filtra" pisa círculo central y línea media (poco contraste); "2 vs 3" se solapa con balón/flecha. | Mover "hombre libre filtra" a x=58,y=52; subir "2 vs 3" al título de la zona (y=72) y dejar la flecha sola. |
| teoria-13-solucion-2v3.svg | 6.5 | MENOR | Racimo central confuso: "3 funcional en el medio" choca con el texto "MC" del jugador derecho; "pellizca dentro"/"entra al centro" pisan la ficha MI y la flecha es muy corta. | Bajar el rótulo de zona "3 funcional…" a y=42 (cabecera de la zona) para no chocar con los MC en y=46; alargar la flecha run del MI (14,48→30,48) y poner "entra al centro" a y=53. |
| teoria-14-salida-3mas2.svg | 7.0 | MENOR | La flecha blanca larga (de ~y=44 a MC6) rotulada "drop" es ambigua: parece una carrera vertical en vez del descenso del 6; "baja a salir" pisa MC6; los 2 DC rivales (y=30) quedan algo desconectados del 3 atrás. | Acortar el drop a un arco corto del 6 (de y=24 a y=19) y rotular "drop del 6"; separar "superioridad 3 vs 2" del trazo (a x=50,y=26 dentro de la zona cian). |
| teoria-15-tercer-hombre.svg | 8.0 | OK | "recibe de espaldas" pisa MC6 y círculo central; "3er hombre (de cara)" toca el borde de zona y MC8. | Mover "recibe de espaldas" a `cy+r+12` bajo MC6; subir "3er hombre…" a y=68 dentro de la zona. |
| teoria-16-apoyo-ruptura.svg | 8.5 | OK | Concepto claro (apoyo baja / ruptura a la espalda / descarga al que rompe). La carrera blanca del APOYO es larga. | Acortar la run del APOYO (de y=78 a y=70). Sin más acción. |
| teoria-17-ataque-area.svg | 8.5 | OK | Rótulos duplicados (en ficha y en flecha) "1er palo"/"penalti"; las 3 flechas convergen y se cruzan, pero legible. | Quitar el `label` de las flechas pass (ya están rotuladas las fichas) para aligerar. |
| teoria-18-desdoblamiento.svg | 9.0 | OK | Overlap/underlap bien diferenciados; sin solapes. | Sin acción. Diagrama modelo. |
| teoria-19-contraataque.svg | 8.0 | OK | Racimo central: "3er hombre" pisa MC8 y círculo; "ROBO" pisa MC y balón; "ruptura" pisa DC. | Mover "ROBO" a `cy+r+12` bajo el MC; subir "3er hombre" a y=60; "ruptura" a `cy+r+12` bajo el DC. |
| teoria-20-repliegue.svg | 8.5 | OK | Repliegue y "frena el eje" claros; sin solapes graves. | Sin acción. |
| teoria-21-contrapresion.svg | 7.0 | MENOR | "recupera / 3-5 s para robar" pisan de lleno la ficha RIVAL (texto sobre rojo, ilegible); las 2 flechas block (MC6/MD "tapa apoyo") apuntan al balón, no a las líneas de pase, leyéndose como un 4.º y 5.º salto al balón en vez de cierre de apoyos. | Mover "3-5 s para robar" al título de la zona (y=72) y "recupera" a `cy+r+12` bajo el rival. Reorientar las flechas block para que cubran a un apoyo lateral (p.ej. MC6 → x=46,y=54) en vez de apuntar al balón. |
| teoria-22-corner-ofensivo.svg | 8.5 | OK | Setup correcto; solo un trazo de "centro" hacia la zona central (los demás rematadores sin trayectoria). | Opcional: añadir 1-2 flechas pase tenues hacia 1er y 2.º palo para reflejar "poblar varias zonas". |
| teoria-23-compacidad-distancias.svg | 8.0 | OK | "líneas cortas (8-12 m entre sí)" se apoya sobre el borde cian discontinuo y la línea media (bajo contraste). | Bajar ese rótulo a y=49 y/o aumentar contraste (fondo oscuro tras el texto). |
| sesion-1.svg | 8.5 | OK | Curva de carga del microciclo bien rotulada y profesional; coherente con "carga modulada, baja MD-1". | Sin acción. |
| sesion-2.svg | 9.0 | OK | Flujo de la sesión (activación → foco → global → vuelta a la calma) exacto al texto. | Sin acción. Diagrama modelo. |

---

## Lista priorizada de correcciones

### BLOQUEANTES (corregir antes de publicar)
1. **teoria-11-fuera-de-juego.svg** — Fuera de juego invertido: los 2 atacantes "FUERA DE JUEGO" están en el lado ONSIDE (y=60/62, por encima de la línea). Recolocarlos en y≈44/46 (bajo la línea, lado del fondo propio) para que queden realmente pasados al subir la defensa. Es un error conceptual visible en el módulo de fase defensiva, que es justo el contenido que la imagen debe enseñar.

### MENORES (mejorables; recomendadas para acabado "top")
2. **teoria-07-bloques-altura.svg** — "primer presionador" pintado como rival (rojo); pasarlo a propio o renombrar.
3. **teoria-04-plano-vs-rombo.svg** — el rombo en rojo (rival) confunde la comparación; usar neutral/propio y separar las etiquetas PLANO/ROMBO por mitades.
4. **teoria-13-solucion-2v3.svg** — racimo central con texto solapado ("3 funcional" sobre "MC"); reubicar rótulos y alargar la flecha del pellizco.
5. **teoria-21-contrapresion.svg** — texto sobre la ficha rival (ilegible) y flechas block que apuntan al balón en vez de a los apoyos.
6. **teoria-09-basculacion.svg** — "pisa centro" y "banda lejana concedida" solapados con fichas/líneas.
7. **teoria-10-trampa-banda.svg** — cúmulo de rótulos en la esquina sup-der.
8. **teoria-08-pressing-sombra.svg** — la "curva" se dibuja recta y tapada; usar trazo ondulado y alargarla.
9. **teoria-14-salida-3mas2.svg** — el "drop" como flecha larga vertical es ambiguo; convertir en arco corto del 6.
10. **teoria-05-variante-rombo.svg** — el borde-guía del rombo cruza las etiquetas "interior"/"enganche".

### OK (publicables tal cual; nits opcionales)
teoria-01, teoria-02, teoria-03, teoria-06, teoria-12, teoria-15, teoria-16, teoria-17, teoria-18, teoria-19, teoria-20, teoria-22, teoria-23, sesion-1, sesion-2.

---

## Resumen cuantitativo

- **OK:** 15
- **MENOR:** 9
- **BLOQUEANTE:** 1
- **Total evaluados:** 25
- **Puntuación media:** **7.92 / 10**

**Veredicto:** el lote tiene una base sólida y visualmente profesional (motor de pizarra consistente, paleta y leyenda claras). Un único defecto **bloqueante** (teoria-11, fuera de juego invertido) debe corregirse sí o sí por ser un error conceptual. El patrón de defecto recurrente y más fácil de subir nota es el **solapamiento de rótulos sobre fichas/líneas** en los diagramas con racimos centrales (t09, t10, t13, t19, t21): reubicar etiquetas a césped libre o debajo de la ficha (`cy+r+12`) elevaría varios de un 7 a un 9.
