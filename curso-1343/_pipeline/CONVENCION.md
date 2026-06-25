# Convención de posiciones y dorsales — Sistema 1-3-4-3

Estructura: **portero + 3 centrales + 4 medios (2 carrileros + 2 mediocentros) + 3 delanteros (2 extremos + 1 punta).**
Esta nomenclatura es ÚNICA para todo el curso (módulos, ejercicios y pizarras).

| Dorsal | Posición | Abrev. | Matiz de rol |
|---|---|---|---|
| 1 | Portero | POR | Hombre libre / portero-líbero, manda la línea de 3 |
| 2 | Carrilero derecho | CAR | Recorre toda la banda derecha: defiende y da amplitud en ataque |
| 3 | Carrilero izquierdo | CAR | Recorre toda la banda izquierda: defiende y da amplitud en ataque |
| 4 | Central derecho | DFC | Marca/cobertura; sale a presionar por su lado, puede conducir |
| 5 | Central / líbero | DFC | El central del medio: organiza la línea de 3, líbero/coberturas |
| 6 | Central izquierdo | DFC | Marca/cobertura; sale a presionar por su lado, puede conducir |
| 8 | Mediocentro (pivote) | MC | Ancla posicional por delante de la línea de 3; equilibrio |
| 10 | Mediocentro ofensivo | MC | Box-to-box / creación; recibe entre líneas y llega al área |
| 7 | Extremo derecho | ED | Amplitud o pisar por dentro; ayuda defensiva al carrilero |
| 9 | Delantero centro | DC | Referencia / pivote ofensivo, ataca el área |
| 11 | Extremo izquierdo | EI | Amplitud o pisar por dentro; ayuda defensiva al carrilero |

## Notas de nomenclatura (fijas)
- **Tres centrales (DFC ×3)**: uno por el centro (5, líbero/organizador) y dos por los lados (4 y 6). Son la base; defienden el centro y salen a presionar con coberturas.
- **Carrileros (CAR 2/3)** = los 2 medios de banda (wing-backs). Clave del sistema: con balón suben a dar la amplitud (el equipo se estira a un 1-3-4-3 muy ancho / casi 1-3-2-5); sin balón bajan y forman una línea de 5 (1-5-2-3 / 1-5-4-1 defensivo).
- **Dos mediocentros (MC 8/10)**: 8 más posicional (pivote), 10 más ofensivo (llegador/creador). Doble pivote que protege a los 3 centrales.
- **Tridente ofensivo (ED 7 · DC 9 · EI 11)**: los 2 extremos dan amplitud arriba o atacan los espacios interiores; el 9 es la referencia. SÍ hay extremos en este sistema.
- **Mutación con balón**: 1-3-4-3 ↔ 1-3-2-5 (carrileros y extremos forman una línea de 5 atacante).
- En el plan de sesiones, `MD` = "matchday" (MD-4 … MD), nunca posición.

## Para la portada (build_cover.py) — dorsales por línea (defensa→ataque, izq→der en pantalla)
- gk = 1
- línea defensa (3): [6, 5, 4]
- línea medio (4): [3, 10, 8, 2]   (CAR izq, MC, MC, CAR der)
- línea delantera (3): [11, 9, 7]  (EI, DC, ED)
