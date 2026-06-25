# Convención de posiciones y dorsales — Sistema 1-4-2-3-1

Estructura: **portero + 4 defensas (2 centrales + 2 laterales) + doble pivote (2 MC) + línea de 3 (2 extremos + 1 mediapunta) + 1 delantero.**
Esta nomenclatura es ÚNICA para todo el curso (módulos, ejercicios y pizarras).

| Dorsal | Posición | Abrev. | Matiz de rol |
|---|---|---|---|
| 1 | Portero | POR | Portero-líbero, inicia el juego, cobertura a la espalda de la defensa |
| 2 | Lateral derecho | LD | Defiende el carril derecho y se proyecta dando amplitud |
| 3 | Lateral izquierdo | LI | Defiende el carril izquierdo y se proyecta dando amplitud |
| 4 | Central derecho | DFC | Marca/cobertura; saca el balón por su lado |
| 5 | Central izquierdo | DFC | Marca/cobertura; saca el balón por su lado |
| 6 | Mediocentro defensivo (pivote) | MC | Ancla del doble pivote, protege a la defensa, primera salida |
| 8 | Mediocentro (box-to-box) | MC | El otro pivote: equilibrio, conducción y llegada |
| 7 | Extremo derecho | ED | Amplitud o pisar por dentro; repliega a ayudar al lateral |
| 10 | Mediapunta | MCO | El enganche: recibe entre líneas, crea y llega; cabeza del trivote |
| 11 | Extremo izquierdo | EI | Amplitud o pisar por dentro; repliega a ayudar al lateral |
| 9 | Delantero centro | DC | Referencia ofensiva: fija a los centrales, apoya y ataca el área |

## Notas de nomenclatura (fijas)
- **Línea de 4 (LD/LI + DFC ×2)**: defensa clásica de cuatro; los laterales (LD/LI) dan la amplitud en ataque.
- **Doble pivote (MC 6/8)**: 6 más posicional (ancla), 8 más box-to-box; protegen a los centrales y son la base de la construcción. **Nunca salen los dos a la vez** en defensa.
- **Trivote ofensivo (ED 7 · MCO 10 · EI 11)**: la línea de 3 por detrás del 9. La **mediapunta (10)** es la pieza clave: juega entre líneas en la zona 14. Los extremos 7/11 dan amplitud o pisan por dentro. SÍ hay extremos.
- **Delantero (DC 9)**: referencia única arriba; asocia con el 10 y los extremos.
- **Relación con otros sistemas**: defensivamente suele replegar a un **1-4-4-2** o **1-4-4-1-1** (los extremos bajan a la línea de medios, el 10 junto al 9). Con balón se estira a un **1-2-3-5 / 1-4-3-3** según suban laterales y baje un pivote.
- En el plan de sesiones, `MD` = "matchday" (MD-4 … MD), nunca posición.

## Para la portada (build_cover.py) — dorsales por línea (defensa→ataque, izq→der en pantalla)
- gk = 1
- línea defensa (4): [3, 5, 4, 2]
- doble pivote (2): [6, 8]
- línea de 3 (mediapuntas): [11, 10, 7]   (EI, mediapunta, ED)
- delantero (1): [9]
