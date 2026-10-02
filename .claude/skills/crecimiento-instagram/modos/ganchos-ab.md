# Sistema de 3 ganchos (A/B/C) — SIEMPRE, en cada Reel

## Regla
Cada Reel se produce en **3 versiones que comparten cuerpo, clips y cierre**; solo cambian los primeros ~3 s
(texto grande en pantalla + frase de apertura). Se publican como **Trial Reels** (solo no seguidores, 72 h) y
gana el que mejor retenga y se envíe. Nada de 3 redacciones del mismo ángulo: **3 ángulos distintos**.

## Los 3 ángulos (uno de cada, salvo que tests-ganchos.md diga otra cosa)
| ID | Tipo | Plantilla | Ejemplo MISTER ÉLITE |
|---|---|---|---|
| A | **opinión** (giro/"es una trampa") | "El [sistema] de [equipo] es una trampa" | "El 4-3-3 de México es una trampa" |
| B | **resultado concreto** (cifra/plazo) | "[N] pases y [equipo] rompe la presión" | "3 pases y México rompe la presión" |
| C | **curiosidad** ("nadie te cuenta") | "Nadie ve este movimiento del [dorsal]" | "Nadie ve este movimiento del 6" |
Otros ángulos para rotar cuando haga falta: estadística, error típico ("el error nº1 del lateral"), robo ("roba esta rueda de pases"), POV de entrenador.

## Reglas de redacción (cada gancho)
- ≤ 9 palabras en pantalla (≤ 2 líneas); lo más fuerte en las 3 primeras palabras. Sin saludo.
- Concreción: número, dorsal, equipo, plazo. Verdadero y comprobable (no inventar datos del equipo).
- La frase de locución dice lo mismo que la pantalla (el audio empieza en el segundo 0).
- El cuerpo y el cierre (CTA "Comenta SISTEMA/RUEDAS/SALIDA") NO cambian entre versiones.
- Marca pública: solo MISTER ÉLITE.

## Entregable de cada pieza (carpeta `reels/pendientes/<fecha>-<slug>/`)
- `ganchos.json`: `[{"id":"A","tipo":"opinion","pantalla":"...","locucion":"..."}, {B}, {C}]`
- `cuerpo.txt`: locución del cuerpo (sin el gancho).
- `clips.txt`, `caption.txt`, `manychat.txt`.
- Voz (PC, ElevenLabs): `gancho_A.mp3`, `gancho_B.mp3`, `gancho_C.mp3` y `cuerpo.mp3`.
- Montaje: `python .claude/skills/produccion-reels/montar_reel.py --pendientes` → `reel-<slug>-A/B/C.mp4`.

## Protocolo de test (72 h)
1. Publicar A, B, C como Trial Reels el mismo día, a la hora recomendada (15:30-17:30 WEST), uno tras otro.
2. A las 72 h leer, por versión: abandono a 3 s, completado, envíos/espectador, comentarios.
3. Ganador = mayor combinación (retención 3 s y envíos/espectador); desempate por completado.
4. Registrar en `conocimiento/tests-ganchos.md`. El ganador pasa a público (automático si supera el umbral, o manualmente).
5. Perdedores: no se borran; se anota por qué (ángulo + métrica).

## Aprendizaje (cierra el bucle)
Cada ronda semanal recalcula en `tests-ganchos.md` la tasa de victoria por TIPO de ángulo y por SERIE.
Con ≥ 8 tests: el ángulo con más victorias va en 2 de las 3 versiones y el ángulo con menos, en 1 (nunca eliminar uno del todo: el público cambia).
