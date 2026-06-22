# Convención de posiciones y dorsales — Sistema 1-5-3-2

Estructura: **portero + 5 defensas (3 centrales + 2 carrileros) + 3 medios (1 pivote + 2 interiores) + 2 puntas.**
Esta nomenclatura es ÚNICA para todo el curso (módulos, ejercicios y pizarras).

| Dorsal | Posición | Abrev. | Matiz de rol |
|---|---|---|---|
| 1 | Portero | POR | Hombre libre / portero-líbero, manda la línea de 3 |
| 2 | Carrilero derecho | CAR | Recorre toda la banda derecha: defiende y da amplitud en ataque |
| 3 | Carrilero izquierdo | CAR | Recorre toda la banda izquierda: defiende y da amplitud en ataque |
| 4 | Central derecho | DFC | Marca/cobertura; sale a presionar por su lado |
| 5 | Central / líbero | DFC | El central del medio: organiza la línea de 3, líbero/coberturas |
| 6 | Central izquierdo | DFC | Marca/cobertura; sale a presionar por su lado |
| 7 | Interior derecho | MC | Box-to-box: ayuda a defender el carril y llega al área |
| 8 | Mediocentro / pivote | MC | Ancla posicional por delante de los 3 centrales |
| 10 | Interior izquierdo / media punta | MC | El más creativo: recibe entre líneas y asocia con los 2 DC |
| 9 | Delantero centro | DC | Referencia / pivote ofensivo |
| 11 | Segundo delantero | DC | Móvil / de ruptura |

## Notas de nomenclatura (fijas)
- **Carrileros (CAR)** = los 2 jugadores de banda del 1-5-3-2 (wing-backs). Son la CLAVE del sistema: dan la anchura en ataque y forman la línea de 5 en defensa. No son extremos ni laterales puros.
- **Línea de 3 centrales (DFC ×3)**: uno por el centro (5, líbero/organizador) y dos por los lados (4 y 6).
- **Doble función de los carrileros**: con balón el equipo es un 1-3-5-2; sin balón, un 1-5-3-2 (los carrileros bajan a la línea).
- **Medio de 3**: 1 pivote (8) + 2 interiores (7 y 10).
- **EI/ED** no se usan en este sistema (no hay extremos): los de banda son **carrileros (CAR)**.
- En el plan de sesiones, `MD` = "matchday" (MD-4 … MD), nunca posición.

## Para la portada (build_cover.py) — dorsales por línea (defensa→ataque, izq→der en pantalla)
- gk = 1
- línea defensa (5): [3, 6, 5, 4, 2]
- línea medio (3): [10, 8, 7]
- línea delantera (2): [9, 11]
