# Revisión de calidad — Diagramas de TEORÍA (10)

Curso "Rondos: el corazón del entrenamiento" · MISTER ÉLITE — Moisés Díaz
Revisor de calidad · estándar alto · evaluación 0–10 · 2026-06-23

Notación de referencia: poseedores AZUL · defensores/recuperadores ROJO · comodines/apoyos ÁMBAR · pase amarillo discontinuo · conducción azul · desmarque/apoyo blanco. Fuente: `_pipeline/NOTACION.md` y `graficos/PEDIDOS.md`.

## Tabla de evaluación

| Archivo | Punt. | Severidad | Defecto principal | Corrección precisa |
|---|---|---|---|---|
| `teoria-01-definicion.svg` | 7.5 | MENOR | Concepto "cerco" correcto (4 azules perímetro + 1 rojo centro + pase amarillo rodeando). La LEYENDA incluye entrada "zona" (punto ámbar) que NO aparece en el diagrama → leyenda con ítem fantasma. Además flecha "ATAQUE" lateral irrelevante para un rondo no direccional. | Eliminar la entrada "zona" de la leyenda (o sombrear realmente el cuadro con `p.zone`). Quitar la flecha/etiqueta "ATAQUE" del lateral. |
| `teoria-02-continuo-especificidad.svg` | 8 | MENOR | 5 peldaños correctos (rondo→direccional→j. posición→p. reducido→partido) con doble flecha (control aislado ← / realismo →). Pitch de fondo y flecha "ATAQUE" añaden ruido visual ajeno al concepto; las líneas del campo se transparentan tras los paneles. | Quitar la flecha "ATAQUE". Reducir opacidad del campo o usar fondo neutro bajo la banda de peldaños para que las líneas no atraviesen los paneles. |
| `teoria-03-tipos-beneficio.svg` | 7.5 | MENOR | 5 bloques convergiendo en mini-rondo central: bien. PERO el rondo central muestra solo azul+rojo; el brief pide azul/rojo/ÁMBAR. Colores de los 5 bloques (azul/azul/ámbar/ámbar/rojo) son decorativos y pueden confundir con la notación de fichas. Flecha "ATAQUE" irrelevante. | Añadir 1 ficha ámbar (comodín) al mini-rondo central para cumplir azul/rojo/ámbar. Neutralizar el color de los bloques (todos un mismo tono de marca) para no chocar con la notación. Quitar "ATAQUE". |
| `teoria-04-variables-diseno.svg` | 5 | BLOQUEANTE | Solape de texto grave: las etiquetas de 2 líneas ("RELACIÓN/NUMÉRICA", "ESPACIO/FORMA", "Nº DE/TOQUES") caen sobre la fila inferior de diales; "/ FORMA" se monta sobre el dial rojo central. Sublabels "interior·banda·puerta" y "mantener·progresar·presionar" quedan sueltos sin dial asociado. Flecha "ATAQUE" pisa el borde del dial derecho. Un dial es rojo (choca con notación). | Reorganizar a rejilla 3×2 con más alto de fila para que cada etiqueta de 2 líneas quepa BAJO su dial sin invadir la fila siguiente. Anclar cada sublabel a su dial. Unificar color de diales (tono marca, no rojo). Quitar "ATAQUE". |
| `teoria-05-relaciones-numericas.svg` | 4 | BLOQUEANTE | NO cumple el pedido: el brief exige 4v1·5v2·6v3·7v2 con etiquetas +3·+3·+3·+5. El diagrama muestra 4v1·5v2·4v2·3v1 con +3·+3·+2·+2 → faltan 6v3 y 7v2/+5; se pierde el mensaje "misma idea, superioridad creciente hasta +5". Leyenda parcialmente tapada por el cuadro inferior. | Rehacer los 4 mini-cuadros como 4v1(+3), 5v2(+3), 6v3(+3) y 7v2(+5) según PEDIDOS. Reposicionar la leyenda fuera del solape. |
| `teoria-06-progresion.svg` | 7.5 | MENOR | Escalera de 5 palancas (espacio→toques→+defensor→dirección→premiar) con "ZONA DE RETO ≈60–75%" sombreada: concepto correcto. El rótulo superior "Si el balón no circula…" se cruza con el arco del área y una flecha tenue → legibilidad baja en esa línea. La línea de medio campo atraviesa la caja "+Defensor". | Subir/recolocar el rótulo "Si el balón no circula…" sobre fondo limpio. Atenuar las líneas del campo bajo la escalera para que no crucen las cajas. |
| `teoria-07-coaching-freeze.svg` | 8.5 | OK | Freeze muy logrado: rojo "de espaldas", línea blanca discontinua "línea libre" entre azules saltando al defensor, bocadillo de pregunta y tag FREEZE. Coach "T" en ámbar. Único pero: flecha "ATAQUE" lateral irrelevante en un freeze. | (Opcional) Quitar la flecha "ATAQUE". Verificar que la línea blanca se distinga de la del campo (engrosar/contraste). |
| `teoria-08-cadena-transferencia.svg` | 8.5 | OK | 4 escalones encadenados (Rondo azul → J. Posición ámbar → Partido condicionado naranja → Competición rojo) con flechas ascendentes y sublabels (+porterías, +reglas, +rival). Gradiente lógico y limpio. Líneas del campo cruzan tras las cajas (cosmético). | (Opcional) Atenuar el campo bajo las cajas. Sin cambios obligatorios. |
| `teoria-09-familias-principios.svg` | 8 | MENOR | Mapa de las 7 familias con principio + fase del partido: claro y bien tabulado. Los chips de familia usan PÚRPURA y TURQUESA (familias 6 y 7), colores fuera de la paleta azul/rojo/ámbar de la notación y sin entrada en leyenda. | Usar para los chips de familia tonos de la paleta de marca (o un único tono neutro numerado), evitando púrpura/turquesa que no pertenecen a la notación. |
| `teoria-10-microciclo.svg` | 8 | MENOR | Semana MD+2…MD con curva de carga (pico MD-4/MD-3 y descenso) y familia recomendada por día: concepto correcto y completo. Los chips inferiores de familia (p. ej. "Lúdico 7v2", "F7/1") tienen bajo contraste sobre verde oscuro. Flecha "ATAQUE" irrelevante. | Subir el contraste de los chips inferiores (fondo más claro o texto más brillante). Quitar la flecha "ATAQUE". |

## Lista priorizada de correcciones

### BLOQUEANTES (corregir antes de publicar)
1. **`teoria-05-relaciones-numericas.svg`** — Contenido erróneo: debe mostrar 4v1·5v2·6v3·7v2 con +3·+3·+3·+5 (ahora muestra 4v1·5v2·4v2·3v1 / +3·+3·+2·+2). Rehacer mini-cuadros + leyenda sin solape.
2. **`teoria-04-variables-diseno.svg`** — Solape de etiquetas sobre la fila inferior de diales; rejilla apretada. Reorganizar a 3×2 con altura suficiente, anclar sublabels, unificar color de diales (quitar el rojo) y quitar "ATAQUE".

### MENORES (mejoran calidad; recomendado)
3. **`teoria-09`** — Sustituir púrpura/turquesa de los chips por la paleta de marca.
4. **`teoria-03`** — Añadir ficha ámbar al mini-rondo central; neutralizar color de los 5 bloques.
5. **`teoria-01`** — Quitar entrada "zona" fantasma de la leyenda (o sombrear de verdad).
6. **`teoria-06`** — Recolocar el rótulo "Si el balón no circula…" sobre fondo limpio.
7. **`teoria-10`** — Subir contraste de los chips inferiores de familia.
8. **`teoria-02`** — Reducir transparencia del campo bajo los peldaños.

### TRANSVERSAL (afecta a 8 de 10)
- La flecha/etiqueta lateral **"ATAQUE"** aparece en 01, 02, 03, 04, 05, 06, 07, 09 y 10 sin aportar nada: estos diagramas son infografías conceptuales, no jugadas con dirección de ataque. Eliminarla en todos salvo donde el sentido de juego sea relevante (no lo es en ninguno de teoría).
- El **fondo de campo de fútbol** se usa en los 10. Para infografías conceptuales (paneles, escaleras, mapas) genera ruido y deja líneas del campo cruzando cajas. Recomendado: fondo neutro de marca o atenuar mucho el césped bajo los paneles.

## Resumen
- **OK:** 2 (`teoria-07`, `teoria-08`)
- **MENOR:** 6 (`teoria-01`, `02`, `03`, `06`, `09`, `10`)
- **BLOQUEANTE:** 2 (`teoria-04`, `teoria-05`)
- **Media:** 7.30 / 10

*MISTER ÉLITE — Moisés Díaz*
