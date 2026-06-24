# REVISIÓN DE CALIDAD — Diagramas de TEORÍA (16)

Curso **"Juego de posición: dominar con el balón"** · MISTER ÉLITE — Moisés Díaz
Revisor de calidad · estándar alto · lote `graficos/teoria-*.svg`
Método: render a PNG (680 px), lectura visual, contraste con `PEDIDOS.md` + módulo correspondiente y `NOTACION.md`.
Fecha: 2026-06-24

> Notación verificada: poseedores **azul**, defensores **rojo**, comodines **ámbar**, sin colores espurios (no púrpura/turquesa raro; los azul-cian/celeste que aparecen son zonas/flechas de conducción de la leyenda, coherentes).

---

## Tabla de evaluación

| Archivo | Pts | Severidad | Defecto principal | Corrección PRECISA |
|---|:--:|:--:|---|---|
| `teoria-01-jdp-vs-esteril.svg` | 7.0 | MENOR | Los dos paneles comparten el MISMO campo con sólo una fina línea azul vertical de separación; el lado "estéril" queda confinado abajo-derecha y desequilibrado frente a la cadena vertical larga de la izquierda. Etiquetas "JUEGO DE POSICIÓN"/"POSESIÓN ESTÉRIL" pisan el borde superior del área. | Separar visualmente los dos paneles (banda divisoria gruesa o dos minicampos lado a lado). Equilibrar: que el lado estéril tenga cadena horizontal/atrás de tamaño comparable. Bajar las etiquetas de cabecera para que no toquen la línea de área. |
| `teoria-02-superioridad-numerica.svg` | 7.5 | MENOR | Texto "al que sobra" se sitúa encima de la flecha de pase; el círculo ámbar discontinuo ("zona del balón") se solapa con el círculo central blanco del campo creando ruido. El token P "LIBRE (+1)" casi pegado al texto. | Subir "al que sobra" fuera de la línea de pase. Reducir/desplazar la elipse ámbar para que no choque con el círculo central. Separar el rótulo "LIBRE (+1)" del token. |
| `teoria-03-superioridad-posicional.svg` | 7.0 | MENOR | "salta 1 línea" pisa un token D y la línea de pase; el receptor entre líneas queda tapado por la elipse ámbar + rótulo "orientado · sin marca". | Mover "salta 1 línea" a un hueco libre del carril. Aclarar el receptor: token por encima de la zona ámbar y rótulo desplazado abajo. |
| `teoria-04-superioridad-cualitativa.svg` | 7.5 | MENOR | "rivales fijados" y "cambio" se solapan con el círculo central y un token P; lectura apretada en la zona central. | Reubicar "rivales fijados" sobre la elipse de fijación (zona despejada) y "cambio" junto a la flecha pero sin pisar tokens. Buen uso del regate blanco y el 1v1 aislado. |
| `teoria-05-cinco-carriles.svg` | 9.0 | OK | Limpio, coherente, regla "máx 2/carril, no 3/línea" bien ilustrada con triángulos/diagonales y pasillos interiores destacados. | Sin cambios obligatorios. (Opcional: marcar más visiblemente las 3 alturas.) |
| `teoria-06-hombre-libre.svg` | 7.5 | MENOR | "presión" pisa el token D; el portador queda tapado por D + triángulo de presión; lectura densa en el lado izquierdo. | Separar el rótulo "presión" del token rojo. Despejar el portador (no superponer triángulo de presión sobre su ficha). Buen contraste zona presión (roja) vs hombre libre (celeste). |
| `teoria-07-atraer-cambiar.svg` | 6.5 | MENOR | "3 cambio" y "rival basculado" se solapan con el círculo central y un token D; el token P "HOMBRE LIBRE" aparece medio cortado por el borde derecho; numeración 1-2 poco visible. | Meter el token "HOMBRE LIBRE" dentro del lienzo (separarlo del borde). Reubicar "3 cambio"/"rival basculado" a huecos libres. Reforzar el tamaño de los números de secuencia 1-2-3. |
| `teoria-08-tercer-hombre.svg` | 6.0 | BLOQUEANTE | Baja legibilidad: la leyenda inferior "el rival salta a D y deja libre a C (el tercero)" es texto oscuro sobre césped y pisa el arco del área (apenas legible); "pivote de espaldas" se solapa con su token; los números 1/2 de la secuencia casi no se ven. Es el concepto MÁS importante del módulo y el peor servido. | Pasar la caption clave a texto claro sobre banda/caja (no sobre césped/arco). Separar "pivote de espaldas" del token. Agrandar y numerar nítidamente 1-2-3. Asegurar que el movimiento de C (flecha blanca) y el pase de primeras de B se distinguen sin esfuerzo. |
| `teoria-09-pase-entre-lineas.svg` | 8.5 | OK | Concepto claro: ventana entre dos D, receptor de perfil en el medio-espacio. "firme, al pie correcto" queda algo cerca de la línea de defensas. | (Opcional) separar levemente "firme, al pie correcto" de la línea roja. Sin bloqueos. |
| `teoria-10-perfil-orientacion.svg` | 8.0 | OK | Comparativa malo/bueno bien resuelta (de espaldas vs cuerpo abierto + 1.er toque). Etiquetas "DE ESPALDAS"/"PERFIL ABIERTO" tocan el borde superior de la caja. | (Opcional) bajar las etiquetas de cabecera. Buen uso de flechas de escaneo y conducción. |
| `teoria-11-ritmo-pausa-aceleracion.svg` | 9.0 | OK | Línea de tiempo pausa→señal→aceleración limpia y didáctica, sin ruido. Es infografía y no aparece flecha "ATAQUE". | Sin cambios. |
| `teoria-12-cadena-transferencia.svg` | 8.5 | OK | Tres escalones rondo→juego de posición→partido con representatividad creciente, bien escalonado. "estructura posicional" roza tokens. | (Opcional) separar "estructura posicional" de las fichas. Sin bloqueos. |
| `teoria-13-mantener-progresar-finalizar.svg` | 8.5 | OK | Tres estadios encadenados claros con flechas ascendentes. Rótulo "entre líneas" aparece duplicado/cercano a un token. | (Opcional) eliminar el rótulo "entre líneas" redundante o separarlo del token. |
| `teoria-14-coaching-intervenciones.svg` | 7.0 | MENOR | Infografía con RUIDO del campo: las marcas (área, círculo central, semicírculos) atraviesan las cajas apiladas de la escalera de intervenciones; el círculo central cruza las cajas 2 y 3 y resta limpieza. PEDIDOS pide pirámide/escalera; aquí son cajas apiladas (aceptable) pero sobre campo visible. | Atenuar/ocultar el dibujo del campo bajo la infografía (fondo plano o muy desaturado) para que las marcas no crucen las cajas. Mantener el degradado de invasividad (azul→rojo) y la flecha "+ invasiva". |
| `teoria-15-finalizacion.svg` | 8.0 | OK | Cadena construir→romper línea→ocupar área (3 alturas)→último pase→remate, coherente y numerada. "área ocupada · 3 alturas" roza el token rematador. | (Opcional) separar el rótulo del token. Comprobar que el rótulo "3 ocupar el área" no se confunde de orden con la flecha; orden 1-2-3-4-5 legible. |
| `teoria-16-contrapresion.svg` | 8.0 | OK | Instante de pérdida bien planteado: azules (equipo protagonista) contrapresionan al rojo "(acaba de robar)", orientación a banda, líneas tapadas, cobertura y reloj 5-6 s. Notación coherente con el módulo. "portador (acaba de robar)" se solapa con tokens. | (Opcional) separar el rótulo del portador de las fichas amontonadas en el centro. Sin bloqueos. |

---

## Resumen

- **OK:** 8 → t05, t09, t10, t11, t12, t13, t15, t16
- **MENOR:** 7 → t01, t02, t03, t04, t06, t07, t14
- **BLOQUEANTE:** 1 → t08 (tercer hombre)

**Media: 7.75 / 10**

---

## Lista priorizada de correcciones

### P0 — Bloqueante (corregir antes de publicar)
1. **`teoria-08-tercer-hombre.svg`** — Rehacer la legibilidad: caption clave a texto claro sobre banda (no sobre césped/arco), separar "pivote de espaldas" del token, agrandar la numeración 1-2-3 y distinguir nítidamente el pase de primeras de B y la carrera de C. Es el concepto central del módulo 02 y hoy es el de peor lectura.

### P1 — Menores de alto impacto (solapes que estorban la comprensión)
2. **`teoria-07-atraer-cambiar.svg`** — Token "HOMBRE LIBRE" cortado por el borde derecho: meterlo en el lienzo; reubicar "3 cambio"/"rival basculado"; reforzar numeración.
3. **`teoria-14-coaching-intervenciones.svg`** — Quitar/atenuar el campo bajo la infografía (las marcas atraviesan las cajas = ruido).
4. **`teoria-01-jdp-vs-esteril.svg`** — Separar y equilibrar los dos paneles (divisor claro; lado estéril de tamaño comparable).
5. **`teoria-03-superioridad-posicional.svg`** y **`teoria-06-hombre-libre.svg`** — Despejar el receptor/portador tapado por zona+rótulo+triángulo.

### P2 — Pulidos menores (no bloquean)
6. **`teoria-02`, `teoria-04`** — Separar rótulos centrales del círculo y de los tokens.
7. **`teoria-09`, `teoria-10`, `teoria-12`, `teoria-13`, `teoria-15`, `teoria-16`** — Separaciones leves rótulo↔token / rótulo↔línea; bajar etiquetas de cabecera que tocan el borde de las cajas.

---

## Notas de coherencia (positivas)
- Notación de color **correcta y consistente** en los 16: azul=poseedor, rojo=defensor, ámbar=zona/comodín. No se detectó púrpura ni turquesa fuera de las flechas de conducción/zonas declaradas en la leyenda.
- Conceptos **bien representados**: superioridades (num/posicional/cualitativa), carriles+regla de ocupación, hombre libre, atraer-cambiar, pase entre líneas, perfil, ritmo, cadena de transferencia, tres estadios, finalización y contrapresión.
- Infografías (t11, t14) **sin** flecha "ATAQUE"; t14 conserva ruido del campo (ver P1·3).
- Marca **MISTER ÉLITE — Moisés Díaz** presente al pie en todos.

*MISTER ÉLITE — Moisés Díaz · Revisión de teoría.*
