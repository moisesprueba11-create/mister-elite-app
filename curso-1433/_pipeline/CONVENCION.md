# Convención de posiciones y dorsales — Sistema 1-4-3-3

Estructura: **portero + 4 defensas (2 centrales + 2 laterales) + mediocampo de 3 (1 pivote + 2 interiores) + tridente ofensivo (2 extremos + 1 delantero).**
Esta nomenclatura es ÚNICA para todo el curso (módulos, ejercicios y pizarras).

| Dorsal | Posición | Abrev. | Matiz de rol |
|---|---|---|---|
| 1 | Portero | POR | Portero-líbero, inicia el juego, cobertura a la espalda de la defensa |
| 2 | Lateral derecho | LD | Defiende el carril derecho y se proyecta dando amplitud |
| 3 | Lateral izquierdo | LI | Defiende el carril izquierdo y se proyecta dando amplitud |
| 4 | Central derecho | DFC | Marca/cobertura; saca el balón por su lado |
| 5 | Central izquierdo | DFC | Marca/cobertura; saca el balón por su lado |
| 6 | Mediocentro (pivote) | MC | Ancla del mediocampo, protege a la defensa, primera salida y equilibrio |
| 8 | Interior derecho | MC | Box-to-box: recibe entre líneas, conduce y llega al área |
| 10 | Interior izquierdo | MC | El más creativo: juega entre líneas, asocia y asiste |
| 7 | Extremo derecho | ED | Amplitud y desborde o pisar por dentro; ayuda al lateral en defensa |
| 9 | Delantero centro | DC | Referencia ofensiva: fija a los centrales, apoya y ataca el área |
| 11 | Extremo izquierdo | EI | Amplitud y desborde o pisar por dentro; ayuda al lateral en defensa |

## Notas de nomenclatura (fijas)
- **Línea de 4 (LD/LI + DFC ×2)**: defensa clásica de cuatro; los laterales (LD/LI) dan la amplitud en ataque y permiten que los extremos pisen por dentro.
- **Mediocampo de 3**: 1 pivote (6) + 2 interiores (8/10). Puede orientarse con el **vértice abajo** (6 solo, "1-pivote": triángulo ▽) o con el **vértice arriba** (doble pivote 6+8 y un enganche 10: triángulo △). El 6 nunca abandona el eje sin cobertura.
- **Tridente (ED 7 · DC 9 · EI 11)**: dos extremos que dan la anchura ofensiva + un 9 referencia. SÍ hay extremos.
- **Relación con otros sistemas**: defensivamente repliega a un **1-4-5-1 / 1-4-1-4-1** (los extremos bajan a la línea de medios). Con balón se transforma en **1-3-2-5 / 1-2-3-5** (un lateral o el pivote bajan, los extremos abren y los interiores llegan).
- En el plan de sesiones, `MD` = "matchday" (MD-4 … MD), nunca posición.

## Para la portada (build_cover.py) — dorsales por línea (defensa→ataque, izq→der en pantalla)
- gk = 1
- línea defensa (4): [3, 5, 4, 2]
- mediocampo (3): [10, 6, 8]   (interior izq, pivote, interior der)
- tridente (3): [11, 9, 7]      (EI, DC, ED)
