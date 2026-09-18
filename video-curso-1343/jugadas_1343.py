#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jugadas_1343.py — Coreografía (datos puros) de la tarea de SALIDA + STOP BALL
del sistema 1-3-4-3 para MISTER ÉLITE — Moisés Díaz.

Reconstruida fotograma a fotograma del vídeo de referencia:
espacio rectangular por zonas, 10 azules (1-3-4-3 sin portero) contra 8 rojos,
tres minipoterías en el fondo propio (derecha) y zona verde STOP BALL en el
fondo contrario (izquierda). El ataque azul va hacia la IZQUIERDA.

Sistema de coordenadas del rectángulo de juego:
    x: 0 (línea de fondo de ATAQUE, pegada a la zona STOP BALL) .. 100 (fondo propio)
    y: 0 (carril superior) .. 100 (carril inferior)
Valores fuera de 0..100 en x son válidos: x<0 = dentro de la zona STOP BALL.
"""

# ---------------------------------------------------------------- geometría --
# Líneas verticales discontinuas (divisiones de zona a lo largo del campo)
ZONE_X = [23.9, 42.8, 56.3, 75.3]
# Líneas horizontales discontinuas (límite de los carriles exteriores)
LANE_Y = [15.6, 85.5]
# Zona STOP BALL: banda exterior pegada al fondo de ataque
STOP_ZONE = dict(x0=-12.0, x1=0.0, y0=LANE_Y[0], y1=LANE_Y[1])
# Minipoterías en el fondo propio (x=100), (centro_y, alto)
MINI_GOALS = [(26.5, 10.5), (49.0, 10.5), (74.5, 10.5)]

# Proporción real del rectángulo (ancho/alto) medida en el vídeo de referencia
PITCH_RATIO = 817.0 / 608.0

# ------------------------------------------------------------- posiciones 0 --
# Azules: 1-3-4-3 sin portero (3 centrales + 2 carrileros + 2 interiores + 3 arriba)
BLUE_START = {
    "5":  (89.5, 24.8),   # central derecho (defiende minipoertía superior)
    "6":  (89.5, 51.0),   # central puro
    "4":  (89.2, 75.7),   # central izquierdo
    "2":  (50.6,  8.4),   # carrilero superior
    "8":  (50.4, 37.7),   # interior/pivote superior
    "10": (50.3, 62.7),   # interior/pivote inferior
    "3":  (50.2, 93.8),   # carrilero inferior
    "7":  (16.6, 24.3),   # extremo superior
    "9":  (13.3, 50.2),   # punta
    "11": (16.9, 76.3),   # extremo inferior
}
RED_START = {
    "r11": (67.7, 29.3), "r9": (67.9, 49.3), "r7": (66.7, 72.5),   # 1.ª línea de presión
    "r10": (34.5, 30.3), "r6": (34.4, 49.5), "r8": (34.3, 70.9),   # 2.ª línea
    "r4":  (6.5, 35.2),  "r5": (6.9, 63.7),                        # pareja de cierre
}

# Líneas del dibujo táctico que se trazan en la introducción
LINEAS_SISTEMA = [
    (["5", "6", "4"],            "3 CENTRALES · primera línea de salida"),
    (["2", "8", "10", "3"],      "4 EN EL MEDIO · 2 carrileros + 2 interiores"),
    (["7", "9", "11"],           "3 ARRIBA · fijan a la última línea rival"),
]

# ------------------------------------------------------------------ jugada 1 --
JUGADA_1 = dict(
    num=1,
    titulo="SALIDA POR DENTRO Y FINALIZACIÓN POR EL CARRIL IZQUIERDO",
    dur=9.4,
    # keyframes de los azules: label -> [(t, x, y), ...]
    moves={
        "3":  [(0.0, 50.2, 93.8), (1.4, 79.0, 94.0), (2.6, 79.0, 94.0),
               (6.2, 26.0, 94.0), (8.0, 12.0, 94.0)],
        "2":  [(0.0, 50.6, 8.4), (2.6, 50.6, 8.4), (5.4, 30.0, 8.4),
               (8.0, 19.0, 8.4)],
        "9":  [(0.0, 13.3, 50.2), (3.0, 13.3, 50.2), (5.4, 17.8, 41.9)],
        "11": [(0.0, 16.9, 76.3), (4.0, 16.9, 76.3), (6.3, 13.6, 71.0),
               (7.9, -5.5, 79.0), (9.4, -7.5, 79.0)],
        "7":  [(0.0, 16.6, 24.3), (3.4, 16.6, 24.3), (5.6, 12.0, 21.0)],
        "8":  [(0.0, 50.4, 37.7), (3.3, 50.8, 36.0), (4.4, 50.8, 30.8)],
        "10": [(0.0, 50.3, 62.7), (3.2, 51.6, 58.0), (4.6, 51.4, 56.5)],
        "5":  [(0.0, 89.5, 24.8), (2.6, 92.0, 24.0), (3.6, 92.0, 24.0)],
        "6":  [(0.0, 89.5, 51.0), (1.0, 92.0, 51.0), (2.6, 92.0, 50.5)],
        "4":  [(0.0, 89.2, 75.7), (1.0, 89.5, 75.7)],
    },
    # secuencia del balón
    ball=[
        dict(k="hold", who="6", t0=0.0, t1=0.9,
             txt="6 arranca la salida. Los 3 centrales abren el campo a lo ancho."),
        dict(k="pase", a="6", b="4", t0=0.9, t1=1.5,
             txt="1 · 6 → 4: primer pase para orientar la presión roja hacia abajo."),
        dict(k="pase", a="4", b="3", t0=1.5, t1=2.1,
             txt="2 · 4 → 3: el carrilero inferior se desmarca en el carril exterior."),
        dict(k="pase", a="3", b="6", t0=2.3, t1=3.1,
             txt="3 · 3 → 6: devolución en diagonal. Si no hay línea de pase, se vuelve."),
        dict(k="pase", a="6", b="5", t0=3.1, t1=3.6,
             txt="4 · 6 → 5: cambio de orientación al central del lado contrario."),
        dict(k="pase", a="5", b="10", t0=3.6, t1=4.5,
             txt="5 · 5 → 10: PASE ENTRE LÍNEAS. Rompe la primera presión roja."),
        dict(k="pase", a="10", b="8", t0=4.7, t1=5.2,
             txt="6 · 10 → 8: los dos interiores se asocian dentro de la zona central."),
        dict(k="pase", a="8", b="2", t0=5.4, t1=6.0,
             txt="7 · 8 → 2: el carrilero superior ya ha atacado el espacio libre."),
        dict(k="pase", a="2", b="9", t0=6.0, t1=6.8,
             txt="8 · 2 → 9: balón al punta, que se ofrece al pie entre los dos cierres."),
        dict(k="pase", a="9", b="11", t0=6.8, t1=7.3,
             txt="9 · 9 → 11: descarga a un toque al extremo que ataca la zona."),
        dict(k="conduce", who="11", t0=7.3, t1=8.3,
             txt="10 · 11 conduce y para el balón en la ZONA STOP BALL. ¡Punto!"),
        dict(k="hold", who="11", t0=8.3, t1=9.4, gol=True,
             txt="10 pases · 0 pérdidas. Progresión limpia por las 5 zonas."),
    ],
)

# ------------------------------------------------------------------ jugada 2 --
JUGADA_2 = dict(
    num=2,
    titulo="PÉRDIDA, CONTRA ROJA A LAS MINIPOTERÍAS Y SEGUNDA SALIDA",
    dur=15.2,
    moves={
        "3":  [(0.0, 50.2, 93.8), (2.2, 72.0, 94.0), (3.4, 60.0, 94.0),
               (4.1, 47.0, 94.0), (5.0, 44.0, 94.0), (9.6, 44.0, 94.0),
               (10.6, 46.0, 93.0), (11.4, 42.0, 93.0)],
        "2":  [(0.0, 50.6, 8.4), (3.0, 56.0, 8.4), (5.0, 50.0, 8.4),
               (9.0, 44.0, 8.4), (12.0, 33.0, 8.4)],
        "10": [(0.0, 50.3, 62.7), (2.6, 48.5, 70.0), (3.6, 48.5, 70.0),
               (6.0, 50.0, 64.0), (9.2, 49.5, 61.0), (10.4, 48.5, 63.5)],
        "8":  [(0.0, 50.4, 37.7), (3.0, 50.4, 42.0), (6.0, 51.0, 34.0),
               (9.4, 50.5, 33.0)],
        "9":  [(0.0, 13.3, 50.2), (4.5, 13.3, 50.2), (7.0, 15.0, 45.0),
               (11.0, 14.0, 52.0), (12.6, 13.0, 55.0)],
        "7":  [(0.0, 16.6, 24.3), (5.0, 15.5, 22.0), (10.0, 13.0, 19.0),
               (11.8, 10.8, 15.8), (13.2, -5.5, 17.5), (15.2, -7.5, 17.5)],
        "11": [(0.0, 16.9, 76.3), (4.0, 15.0, 74.0), (9.0, 14.0, 77.0),
               (10.9, 18.7, 78.6), (12.0, 17.5, 74.0)],
        "5":  [(0.0, 89.5, 24.8), (0.8, 90.5, 24.2), (6.6, 90.5, 24.2),
               (8.2, 88.5, 24.6)],
        "6":  [(0.0, 89.5, 51.0), (1.2, 90.0, 51.0), (6.4, 92.5, 50.0),
               (7.4, 94.0, 50.2), (8.0, 89.0, 50.4)],
        "4":  [(0.0, 89.2, 75.7), (1.6, 90.5, 75.7), (2.6, 90.5, 75.7),
               (6.8, 88.0, 72.0), (8.4, 89.2, 75.7)],
    },
    # keyframes explícitos de los rojos durante la contra (el resto se
    # desplaza en bloque siguiendo el balón)
    rmoves={
        "r8":  [(0.0, 34.3, 70.9), (3.4, 32.0, 74.0), (4.3, 29.5, 78.0),
                (5.6, 31.0, 74.0), (8.5, 34.3, 70.9)],
        "r6":  [(0.0, 34.4, 49.5), (4.3, 31.5, 57.0), (5.2, 29.5, 56.5),
                (6.5, 33.0, 52.0), (8.5, 34.4, 49.5)],
        "r10": [(0.0, 34.5, 30.3), (4.6, 33.5, 36.0), (5.9, 34.5, 34.0),
                (7.0, 35.0, 31.0), (8.5, 34.5, 30.3)],
        "r11": [(0.0, 67.7, 29.3), (5.4, 64.0, 26.5), (6.4, 65.5, 25.0),
                (7.6, 67.0, 28.0), (9.0, 67.7, 29.3)],
        "r9":  [(0.0, 67.9, 49.3), (6.0, 66.0, 44.0), (7.0, 68.5, 47.0),
                (8.2, 72.0, 49.0), (9.4, 67.9, 49.3)],
        "r7":  [(0.0, 66.7, 72.5), (5.0, 64.0, 70.0), (7.2, 66.0, 71.0),
                (9.0, 66.7, 72.5)],
    },
    ball=[
        dict(k="hold", who="6", t0=0.0, t1=0.6,
             txt="Segunda salida: mismo principio, otra decisión."),
        dict(k="pase", a="6", b="5", t0=0.6, t1=1.2,
             txt="1 · 6 → 5: se arranca por el central superior."),
        dict(k="pase", a="5", b="4", t0=1.2, t1=2.1,
             txt="2 · 5 → 4: cambio largo POR DETRÁS de 6, que la deja pasar."),
        dict(k="pase", a="4", b="3", t0=2.1, t1=2.9,
             txt="3 · 4 → 3: apoyo del carrilero en el carril exterior."),
        dict(k="pase", a="3", b="10", t0=2.9, t1=3.5,
             txt="4 · 3 → 10: interior al perfil, dentro de la zona central."),
        dict(k="pase", a="10", b="3", t0=3.5, t1=4.0,
             txt="5 · 10 → 3: pared. El carrilero sigue su carrera."),
        dict(k="pase", a="3", b="r8", t0=4.0, t1=4.5, perdida=True,
             txt="¡PÉRDIDA! El pase hacia dentro lo intercepta el 8 rojo."),
        dict(k="pase", a="r8", b="r6", t0=4.6, t1=5.1, rojo=True,
             txt="CONTRA ROJA: primer pase para salir de la zona de pérdida."),
        dict(k="pase", a="r6", b="r10", t0=5.1, t1=5.7, rojo=True,
             txt="CONTRA ROJA: circulación rápida hacia el lado libre."),
        dict(k="pase", a="r10", b="r11", t0=5.7, t1=6.3, rojo=True,
             txt="CONTRA ROJA: los azules tienen que replegar 40 metros."),
        dict(k="pase", a="r11", b="r9", t0=6.3, t1=6.9, rojo=True,
             txt="CONTRA ROJA: balón al que ataca la minipoertía central."),
        dict(k="tiro", a="r9", xy=(97.0, 50.5), t0=6.9, t1=7.6, rojo=True,
             txt="Tiro a la minipoertía… ¡pero 6 llega al corte!"),
        dict(k="hold", who="6", t0=7.6, t1=8.2,
             txt="6 achica, blinda su minipoertía y recupera. Empieza otra vez."),
        dict(k="pase", a="6", b="5", t0=8.2, t1=8.7,
             txt="6 · 6 → 5: fijar por arriba para abrir el pasillo de dentro."),
        dict(k="pase", a="5", b="6", t0=8.7, t1=9.2,
             txt="7 · 5 → 6: devolución. Un pase para mover el bloque rojo."),
        dict(k="pase", a="6", b="10", t0=9.2, t1=10.1,
             txt="8 · 6 → 10: diagonal interior entre las dos líneas rojas."),
        dict(k="pase", a="10", b="3", t0=10.1, t1=10.6,
             txt="9 · 10 → 3: se vuelve a usar el carril exterior ya liberado."),
        dict(k="pase", a="3", b="11", t0=10.6, t1=11.4,
             txt="10 · 3 → 11: el extremo recibe en la última zona."),
        dict(k="pase", a="11", b="7", t0=11.4, t1=12.5,
             txt="11 · 11 → 7: CAMBIO DE CARRIL al extremo del lado débil."),
        dict(k="conduce", who="7", t0=12.5, t1=13.6,
             txt="12 · 7 conduce y para el balón en la zona. STOP BALL."),
        dict(k="hold", who="7", t0=13.6, t1=15.2, gol=True,
             txt="Tras la pérdida: repliegue, recuperación y salida por el lado contrario."),
    ],
)

JUGADAS = [JUGADA_1, JUGADA_2]

# --------------------------------------------------------------- reglas/HUD --
REGLAS = [
    "10 azules en 1-3-4-3 (sin portero) · 8 rojos en 3-3-2",
    "Cada línea juega en su zona: el campo está dividido en 5 zonas + 2 carriles",
    "Azul suma si PARA EL BALÓN dentro de la zona verde (STOP BALL)",
    "Rojo suma si marca en una de las 3 minipoterías",
]
