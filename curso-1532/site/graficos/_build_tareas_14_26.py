#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las pizarras tarea-14 .. tarea-26 del curso 1-5-3-2 (MISTER ÉLITE)."""
import sys, os
sys.path.insert(0, '/home/user/mister-elite-app/curso-1532/graficos/lib')
from pitch import Pitch

OUT = '/home/user/mister-elite-app/curso-1532/graficos'

# ============================================================
# T14 — Carrilero 1v1 defensivo: frenar y orientar a la línea
# ============================================================
def t14():
    p = Pitch(title="Tarea 14 — Carrilero 1v1 defensivo",
              subtitle="frenar, temporizar y orientar a la línea de fondo", half=None)
    # carril de banda derecha marcado con conos (ancho ~12-15m, fondo 25m)
    # banda derecha: x 70..88, y 8..62
    for cy in (12, 24, 36, 48, 60):
        p.cone(70, cy); p.cone(88, cy)
    p.zone(70, 8, 88, 62, label="", c="#ffd54a", fill_op=0.05)
    # zona de fondo (donde el atacante quiere centrar)
    p.zone(70, 56, 88, 64, label="zona de centro", c="#ff5252", fill_op=0.18)
    # zona interior protegida (a la que el carrilero orienta = cobertura central)
    p.zone(50, 30, 66, 50, label="cobertura central", c="#7ee0ff", fill_op=0.16)
    # servidor
    p.player(79, 8, "S", team="neutral", role="servidor")
    p.ball(79, 18)
    # atacante de banda con balón subiendo
    p.player(79, 20, "ATA", team="rival", role="hombre banda")
    # carrilero defendiendo, temporizando, cuerpo cerrando el interior
    p.player(75, 34, "2", team="own", role="CAR · temporiza")
    # DFC contiguo dando cobertura diagonal por dentro
    p.player(60, 42, "4", team="own", role="DFC cobertura")
    # flecha: atacante intenta progresar por el carril
    p.arrow(79, 22, 79, 40, kind="dribble", label="encara")
    # flecha: carrilero orienta al atacante a la línea de fondo (fuera, sin daño)
    p.arrow(76, 36, 85, 56, kind="run", label="orienta a fondo")
    # flecha de bloqueo: NO por dentro
    p.arrow(74, 34, 64, 34, kind="block")
    p.note(67, 30, "cierra el interior", size=9)
    # cobertura diagonal del central
    p.arrow(62, 44, 72, 38, kind="run", label="cobertura")
    p.legend(["own", "rival", "neutral", "run", "dribble", "block", "zone"])
    p.save(f"{OUT}/tarea-14.svg")

# ============================================================
# T15 — Carrilero ofensivo: amplitud, desborde y centro
# ============================================================
def t15():
    p = Pitch(title="Tarea 15 — Carrilero ofensivo: amplitud y centro",
              subtitle="recibe pegado a banda, desborda y centra al área", half="att")
    # central/pivote que sirve (abajo, dentro)
    p.player(45, 56, "8", team="own", role="sirve")
    p.ball(45, 58)
    # carrilero recibiendo pegado a la cal (banda derecha alta)
    p.player(90, 66, "2", team="own", role="CAR · amplitud")
    # defensor de banda
    p.player(84, 72, "DEF", team="rival", role="")
    # interior que se asocia
    p.player(70, 70, "7", team="own", role="INT")
    # zonas del área marcadas
    p.zone(58, 84, 72, 95, label="1er palo", c="#ffd54a", fill_op=0.14)
    p.zone(38, 86, 52, 96, label="2º palo", c="#ffd54a", fill_op=0.14)
    p.zone(40, 70, 56, 80, label="frontal", c="#ffd54a", fill_op=0.14)
    # 2 DC + interior llegando (sin rótulo: las zonas ya etiquetan el punto)
    p.player(65, 90, "9", team="own", role="")
    p.player(45, 91, "11", team="own", role="")
    p.player(48, 75, "10", team="own", role="")
    # pase del 8 al carrilero
    p.arrow(46, 58, 87, 65, kind="pass", label="1")
    # carrilero desborda por fuera
    p.arrow(90, 68, 90, 84, kind="dribble", label="2 desborda")
    # centro al área
    p.arrow(89, 84, 67, 89, kind="pass", label="3 centro")
    # carreras de los DC
    p.arrow(65, 83, 65, 88, kind="run")
    p.arrow(45, 85, 45, 90, kind="run")
    p.legend(["own", "rival", "pass", "run", "dribble", "zone"])
    p.save(f"{OUT}/tarea-15.svg")

# ============================================================
# T16 — Transición del carrilero: de defender a centrar
# ============================================================
def t16():
    p = Pitch(title="Tarea 16 — Transición del carrilero",
              subtitle="de defender el carril (línea de 5) a subir y centrar", half=None)
    # banda derecha completa, dos fases
    p.goalmini(79, 4)      # portería propia que defiende (abajo)
    # zona defensiva abajo
    p.zone(66, 6, 92, 32, label="FASE 1 · defiende 1v1", c="#7ee0ff", fill_op=0.10)
    # zona de centro arriba
    p.zone(66, 70, 92, 96, label="FASE 2 · sube y centra", c="#ffd54a", fill_op=0.10)
    # FASE 1: carrilero defiende su carril
    p.player(79, 22, "2", team="own", role="CAR defiende")
    p.player(83, 28, "ATA", team="rival", role="")
    p.ball(83, 30)
    p.arrow(82, 27, 75, 20, kind="block")
    # tras recuperar: sprint largo de subida (flecha larga)
    p.arrow(78, 26, 84, 74, kind="run", label="sprint 50-60 m")
    # FASE 2: carrilero arriba recibe y centra
    p.player(86, 80, "2", team="own", role="recibe")
    p.ball(86, 82)
    p.arrow(85, 82, 56, 88, kind="pass", label="centro")
    p.player(54, 90, "9", team="own", role="remate")
    # interior cubre su espalda
    p.player(60, 40, "7", team="own", role="INT cubre espalda")
    p.arrow(62, 44, 72, 30, kind="run", label="cobertura carril")
    # mini portería rival arriba
    p.goalmini(50, 96)
    p.note(30, 50, "ciclo continuo:", size=10)
    p.note(30, 45, "recupera→sube", size=9)
    p.note(30, 40, "pierde→baja", size=9)
    p.legend(["own", "rival", "pass", "run", "block", "zone"])
    p.save(f"{OUT}/tarea-16.svg")

# ============================================================
# T17 — Dos carrileros y equilibrio de bandas
# ============================================================
def t17():
    p = Pitch(title="Tarea 17 — Dos carrileros y equilibrio de bandas",
              subtitle="7v7 por dentro + cambio de orientación al carrilero libre", half=None)
    # dos carriles de banda marcados
    p.zone(0, 8, 14, 92, label="", c="#ffffff", fill_op=0.06)
    p.zone(86, 8, 100, 92, label="", c="#ffffff", fill_op=0.06)
    for cy in (15, 35, 55, 75):
        p.cone(14, cy); p.cone(86, cy)
    p.goalmini(50, 4); p.goalmini(50, 96)
    # carrileros fijos en sus carriles
    p.player(7, 60, "3", team="own", role="CAR izq (lado fuerte)")
    p.player(93, 64, "2", team="own", role="CAR der (lado débil · LIBRE)")
    # juego por dentro 7v7 (representado con algunos jugadores)
    p.player(35, 50, "8", team="own", role="")
    p.player(50, 58, "10", team="own", role="")
    p.player(60, 48, "9", team="own", role="")
    p.player(42, 40, "RIV", team="rival", role="")
    p.player(58, 62, "RIV", team="rival", role="")
    p.player(72, 55, "RIV", team="rival", role="")
    p.ball(36, 52)
    # balón en lado fuerte -> cambio de orientación al lado débil
    p.arrow(36, 52, 50, 58, kind="pass", label="1")
    p.arrow(51, 60, 89, 66, kind="pass", label="2 cambio orientación")
    # carrilero libre centra
    p.arrow(92, 70, 60, 86, kind="pass", label="3 centro")
    p.player(58, 88, "11", team="own", role="remate")
    p.arrow(60, 80, 58, 86, kind="run")
    p.note(50, 30, "gol solo si pasa por carrilero + centro", size=9)
    p.legend(["own", "rival", "pass", "run", "zone"])
    p.save(f"{OUT}/tarea-17.svg")

# ============================================================
# T18 — Circuito del carrilero (numerado 1..6)
# ============================================================
def t18():
    p = Pitch(title="Tarea 18 — Circuito del carrilero",
              subtitle="1 duelo · 2 sprint · 3 recepción · 4 desborde · 5 centro · 6 repliegue", half=None)
    p.goalmini(79, 4)     # mini-portería defensiva abajo
    p.goalmini(50, 96)    # portería de finalización arriba
    # zonas de duelo (abajo) y desborde/centro (arriba)
    p.zone(66, 6, 92, 30, label="zona duelo", c="#7ee0ff", fill_op=0.10)
    p.zone(66, 66, 92, 92, label="zona desborde/centro", c="#ffd54a", fill_op=0.10)
    # (1) 1v1 defensivo abajo
    p.player(79, 20, "2", team="own", role="")
    p.player(83, 26, "ATA", team="rival", role="def. activo")
    p.ball(83, 28)
    p.arrow(82, 25, 76, 18, kind="block", label="1 duelo")
    # (2) sprint de subida
    p.arrow(77, 24, 82, 60, kind="run", label="2 sprint <=8s")
    # (3) recepción en carrera
    p.player(83, 64, "2", team="own", role="3 recibe")
    p.ball(80, 64)
    # (4) desborde a defensor activo
    p.player(90, 73, "DEF", team="rival", role="")
    p.arrow(83, 66, 83, 80, kind="dribble", label="4 desborde")
    # (5) centro a zona marcada con interior llegando
    p.arrow(83, 82, 55, 88, kind="pass", label="5 centro")
    p.zone(44, 83, 62, 94, label="zona remate", c="#ffd54a", fill_op=0.14)
    p.player(52, 88, "7", team="own", role="INT llega", role_below=True)
    p.arrow(54, 80, 53, 86, kind="run")
    # (6) repliegue a zona defensiva
    p.arrow(80, 80, 76, 30, kind="run", label="6 repliegue <=7s")
    p.legend(["own", "rival", "pass", "run", "dribble", "block", "zone"])
    p.save(f"{OUT}/tarea-18.svg")

# ============================================================
# T19 — Pareja de delanteros: uno baja, otro rompe + interior 10
# ============================================================
def t19():
    p = Pitch(title="Tarea 19 — Pareja de delanteros: uno baja, otro rompe",
              subtitle="+ el interior 10 como tercer hombre entre líneas", half="att")
    # pivote 8 sirve (abajo)
    p.player(50, 56, "8", team="own", role="sirve")
    p.ball(50, 58)
    # linea de 3 centrales rival + POR
    p.player(35, 84, "DFC", team="rival", role="")
    p.player(50, 86, "DFC", team="rival", role="")
    p.player(65, 84, "DFC", team="rival", role="")
    # franja entre líneas (etiqueta a la izquierda, lejos de las fichas)
    p.zone(26, 62, 74, 72, label="", c="#ffd54a", fill_op=0.10)
    p.note(33, 67, "entre líneas", size=9)
    # un DC baja a recibir de espaldas
    p.player(40, 73, "9", team="own", role="baja · apoyo")
    # el otro DC ataca diagonal el espacio a la espalda
    p.player(66, 78, "11", team="own", role="rompe a la espalda", role_below=True)
    # interior 10 aparece entre líneas (tercer hombre)
    p.player(58, 67, "10", team="own", role="3er hombre")
    # pase del pivote al 9 que baja
    p.arrow(50, 58, 42, 70, kind="pass", label="1")
    # descarga del 9 al 10
    p.arrow(43, 72, 55, 68, kind="pass", label="2")
    # ruptura diagonal del 11 a la espalda
    p.arrow(64, 76, 73, 90, kind="run", label="rompe")
    # pase filtrado del 10 entre dos centrales al 11
    p.arrow(60, 69, 71, 88, kind="pass", label="3 filtrado")
    p.legend(["own", "rival", "pass", "run", "zone"])
    p.save(f"{OUT}/tarea-19.svg")

# ============================================================
# T20 — Llegada del interior box-to-box (7) al área
# ============================================================
def t20():
    p = Pitch(title="Tarea 20 — Llegada del interior box-to-box (7)",
              subtitle="los DC fijan y abren el pasillo, el 7 llega de segunda línea", half="att")
    # rival: 3 DFC + 1 MC + POR
    p.player(38, 88, "DFC", team="rival", role="")
    p.player(62, 88, "DFC", team="rival", role="")
    p.player(50, 90, "DFC", team="rival", role="")
    p.player(50, 76, "MC", team="rival", role="")
    # 2 DC fijando a los centrales y abriendo el pasillo
    p.player(40, 82, "9", team="own", role="fija")
    p.player(60, 82, "11", team="own", role="fija")
    # interior 10 da el último pase (cut-back)
    p.player(74, 78, "10", team="own", role="último pase")
    p.ball(74, 80)
    # carrilero que centra/juega por dentro
    p.player(90, 74, "2", team="own", role="CAR")
    # interior 7 llega lanzado desde fuera del área
    p.player(50, 60, "7", team="own", role="7 llega en carrera")
    # pasillo abierto (zona) por donde llega el 7
    p.zone(44, 70, 56, 86, label="pasillo abierto", c="#7ee0ff", fill_op=0.14)
    # cut-back / centro atrás del 10 a la frontal/media luna
    p.arrow(73, 80, 54, 78, kind="pass", label="cut-back")
    # llegada del 7 a rematar
    p.arrow(50, 62, 52, 78, kind="run", label="llega desde fuera")
    # zona de llegada (frontal / media luna)
    p.zone(40, 72, 60, 80, label="", c="#ffd54a", fill_op=0.08)
    p.note(50, 66, "remate de primeras", size=9)
    p.legend(["own", "rival", "pass", "run", "zone"])
    p.save(f"{OUT}/tarea-20.svg")

# ============================================================
# T21 — Conexión interior creativo (10) entre líneas
# ============================================================
def t21():
    p = Pitch(title="Tarea 21 — Conexión del interior creativo (10)",
              subtitle="recibe orientado entre líneas y conecta con los 2 DC", half="att")
    # pivote 8 abajo
    p.player(50, 58, "8", team="own", role="busca al 10")
    p.ball(50, 60)
    # franja entre líneas marcada (rótulo a la izquierda)
    p.zone(26, 66, 74, 77, label="", c="#ffd54a", fill_op=0.12)
    p.note(34, 71, "franja entrelíneas", size=9)
    # defensas que vigilan el entrelíneas
    p.player(40, 80, "DEF", team="rival", role="")
    p.player(62, 80, "DEF", team="rival", role="")
    # interior 10 recibe orientado (medio giro)
    p.player(54, 71, "10", team="own", role="recibe orientado")
    # un DC baja a la pared
    p.player(42, 86, "9", team="own", role="pared", role_below=True)
    # el otro DC rompe a la espalda
    p.player(68, 87, "11", team="own", role="rompe", role_below=True)
    # pase 8 -> 10
    p.arrow(50, 60, 53, 68, kind="pass", label="1")
    # pared con el 9
    p.arrow(52, 73, 45, 84, kind="pass", label="2 pared")
    p.arrow(44, 85, 54, 76, kind="pass")
    # ruptura del 11 + filtrado
    p.arrow(67, 84, 72, 93, kind="run", label="rompe")
    p.arrow(56, 73, 70, 90, kind="pass", label="3 filtrado")
    p.legend(["own", "rival", "pass", "run", "zone"])
    p.save(f"{OUT}/tarea-21.svg")

# ============================================================
# T22 — Ataque organizado: por dentro o por fuera
# ============================================================
def t22():
    p = Pitch(title="Tarea 22 — Ataque por dentro o por fuera",
              subtitle="vía interior (asociación) vs vía exterior (centro de carrilero)", half=None)
    # carriles de banda + central marcados
    p.zone(0, 8, 22, 92, label="", c="#ffffff", fill_op=0.05)
    p.zone(78, 8, 100, 92, label="", c="#ffffff", fill_op=0.05)
    p.zone(38, 8, 62, 92, label="", c="#ffffff", fill_op=0.04)
    p.note(50, 16, "carril central", size=9)
    p.goalmini(50, 96); p.goalmini(50, 4)
    # VÍA POR DENTRO (rival cierra el centro): asociación delanteros-interiores
    p.player(50, 50, "8", team="own", role="")
    p.player(46, 64, "10", team="own", role="")
    p.player(54, 70, "9", team="own", role="")
    p.player(48, 74, "11", team="own", role="")
    p.zone(34, 56, 66, 82, label="", c="#7ee0ff", fill_op=0.12)
    p.note(50, 80, "VÍA DENTRO (si abre)", size=9, c="#7ee0ff")
    p.arrow(50, 52, 47, 62, kind="pass", label="dentro")
    p.arrow(46, 66, 52, 76, kind="pass")
    # VÍA POR FUERA (rival cierra dentro): carrilero centra
    p.player(90, 60, "2", team="own", role="CAR")
    p.zone(78, 60, 100, 90, label="VÍA FUERA (si cierra)", c="#ffd54a", fill_op=0.12)
    p.arrow(50, 50, 88, 60, kind="pass", label="cambio")
    p.arrow(90, 64, 58, 82, kind="pass", label="centro")
    # rival defendiendo junto por dentro
    p.player(44, 58, "RIV", team="rival", role="")
    p.player(56, 60, "RIV", team="rival", role="")
    p.player(50, 66, "RIV", team="rival", role="")
    p.note(50, 36, "leer cómo defiende el rival → elegir vía", size=9)
    p.legend(["own", "rival", "pass", "zone"])
    p.save(f"{OUT}/tarea-22.svg")

# ============================================================
# T23 — Transición A-D: recomponer la línea de 5
# ============================================================
def t23():
    p = Pitch(title="Tarea 23 — Transición A-D: recomponer la línea de 5",
              subtitle="pérdida con carrileros arriba · banda descubierta", half=None)
    # estructura propia atacaba en 1-3-5-2 (carrileros arriba)
    # los 3 DFC atrás
    p.player(38, 24, "4", team="own", role="")
    p.player(50, 22, "5", team="own", role="líbero")
    p.player(62, 24, "6", team="own", role="")
    # medio de 3 frena el balón por el centro
    p.player(50, 42, "8", team="own", role="frena el centro")
    # carrileros arriba (descubiertos) sprintando a bajar
    p.player(88, 70, "2", team="own", role="CAR · sprinta a bajar")
    p.player(12, 68, "3", team="own", role="CAR · sprinta a bajar")
    p.arrow(88, 66, 84, 30, kind="run", label="recompone línea 5")
    p.arrow(12, 64, 16, 30, kind="run", label="recompone línea 5")
    # rival contraataca una banda descubierta
    p.player(80, 56, "RIV", team="rival", role="")
    p.ball(80, 58)
    p.player(66, 64, "RIV", team="rival", role="")
    p.arrow(80, 54, 82, 36, kind="drive", label="ataca banda vacía")
    # interior del lado cubre provisionalmente la banda
    p.player(70, 44, "7", team="own", role="INT cubre banda")
    p.arrow(68, 46, 80, 40, kind="run", label="seguro provisional")
    # balón frenado por el centro
    p.arrow(50, 44, 60, 52, kind="block")
    p.goalmini(50, 4)
    p.note(50, 12, "frenar centro 1º · recomponer bandas 2º", size=9)
    p.legend(["own", "rival", "run", "drive", "block"])
    p.save(f"{OUT}/tarea-23.svg")

# ============================================================
# T24 — Contrapresión inmediata (4 mini-porterías)
# ============================================================
def t24():
    p = Pitch(title="Tarea 24 — Contrapresión inmediata tras pérdida",
              subtitle="3-5 s · los más cercanos saltan, el resto cierra interiores", half=None)
    # 4 mini-porterías (2 por equipo) en espacio reducido
    p.goalmini(30, 4); p.goalmini(70, 4)
    p.goalmini(30, 96); p.goalmini(70, 96)
    # instante de la pérdida: balón con el rival
    p.ball(50, 52)
    p.player(50, 54, "RIV", team="rival", role="recupera")
    # 2-3 más cercanos saltan al balón (contrapresión)
    p.player(44, 62, "10", team="own", role="salta")
    p.player(56, 60, "9", team="own", role="salta")
    p.player(50, 40, "8", team="own", role="salta")
    p.arrow(45, 60, 49, 54, kind="run")
    p.arrow(55, 58, 51, 54, kind="run")
    p.arrow(50, 42, 50, 50, kind="run")
    # contrapresión sombreada sobre el balón
    p.zone(40, 44, 60, 64, label="", c="#ff5252", fill_op=0.14, ellipse=True)
    p.note(50, 46, "contrapresión <5s", size=9, c="#ffd0d0")
    # el resto cierra líneas de pase interiores (bloqueos)
    p.player(35, 70, "7", team="own", role="cierra interior")
    p.player(65, 70, "11", team="own", role="cierra interior")
    p.arrow(38, 68, 46, 58, kind="block")
    p.arrow(62, 68, 54, 58, kind="block")
    # rivales receptores tapados
    p.player(38, 44, "RIV", team="rival", role="")
    p.player(62, 46, "RIV", team="rival", role="")
    p.note(50, 30, "no todos al balón: cierra líneas interiores", size=9)
    p.legend(["own", "rival", "run", "block", "zone"])
    p.save(f"{OUT}/tarea-24.svg")

# ============================================================
# T25 — Transición D-A: ataque rápido
# ============================================================
def t25():
    p = Pitch(title="Tarea 25 — Transición D-A: ataque rápido",
              subtitle="robo en la línea de 5 · vertical al delantero · carrilero al espacio", half=None)
    # robo en la línea de 5
    p.player(50, 22, "5", team="own", role="roba")
    p.ball(50, 24)
    # primer pase vertical hacia adelante al delantero que rompe
    p.player(44, 56, "9", team="own", role="apoyo")
    p.player(60, 72, "11", team="own", role="rompe a la espalda", role_below=True)
    p.arrow(50, 26, 45, 52, kind="pass", label="1 vertical")
    p.arrow(46, 58, 60, 78, kind="pass", label="2 profundidad")
    p.arrow(58, 66, 66, 86, kind="run")
    # carrilero lanza su carrera al espacio por la banda
    p.player(86, 40, "2", team="own", role="CAR")
    p.arrow(86, 44, 88, 80, kind="run", label="desdoblamiento al espacio")
    # remate del contra con centro
    p.arrow(64, 82, 84, 84, kind="pass")  # opción descarga al carrilero
    p.arrow(88, 84, 60, 90, kind="pass", label="3 centro")
    p.player(52, 90, "10", team="own", role="remate")
    # zonas de banda y profundidad señaladas
    p.zone(76, 50, 98, 92, label="banda/profundidad", c="#ffd54a", fill_op=0.08)
    # rival en desorden
    p.player(44, 44, "RIV", team="rival", role="")
    p.player(60, 50, "RIV", team="rival", role="")
    p.goalmini(50, 96)
    p.note(50, 14, "máx 6 s / 5 pases · 1er pase adelante", size=9)
    p.legend(["own", "rival", "pass", "run", "zone"])
    p.save(f"{OUT}/tarea-25.svg")

# ============================================================
# T26 — 11v11 con bonificaciones por fase
# ============================================================
def t26():
    p = Pitch(title="Tarea 26 — 11v11 con bonificaciones por fase",
              subtitle="partido completo en 1-5-3-2 · puntuación por patrones", half=None)
    # equipo propio en 1-5-3-2 completo
    p.player(50, 8, "1", team="own", role="")
    # línea de 5 (izq->der pantalla: 3,6,5,4,2)
    p.player(12, 22, "3", team="own", role="")
    p.player(33, 20, "6", team="own", role="")
    p.player(50, 19, "5", team="own", role="")
    p.player(67, 20, "4", team="own", role="")
    p.player(88, 22, "2", team="own", role="")
    # medio de 3 (10,8,7)
    p.player(34, 40, "10", team="own", role="")
    p.player(50, 38, "8", team="own", role="")
    p.player(66, 40, "7", team="own", role="")
    # 2 puntas
    p.player(42, 56, "9", team="own", role="")
    p.player(58, 56, "11", team="own", role="")
    # rival en 1-5-3-2 (esquemático arriba)
    for x, y, l in [(12,78,"R"),(33,80,"R"),(50,81,"R"),(67,80,"R"),(88,78,"R"),
                    (34,62,"R"),(50,64,"R"),(66,62,"R"),(45,48,"R"),(57,48,"R")]:
        p.player(x, y, l, team="rival", role="")
    p.ball(50, 40)
    p.goalmini(50, 96); p.goalmini(50, 4)
    # pizarra de puntuación al lado (panel)
    bx, by = 2, 92
    p.note(bx+13, by, "PUNTUACIÓN", size=10, anchor="middle")
    lines = [
        "Superar presión por suelo  +1",
        "Centro de carrilero (2+INT) +2",
        "Patrón delanteros / INT 2ª  +2",
        "Robo tras gatillo carrilero +2",
        "Recomponer línea de 5      +1",
        "Banda descubierta          -2",
        "Gol normal                  3",
    ]
    yy = by - 4
    for ln in lines:
        p.note(bx+1, yy, ln, size=8, anchor="start")
        yy -= 4
    p.legend(["own", "rival"])
    p.save(f"{OUT}/tarea-26.svg")


if __name__ == "__main__":
    funcs = [t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26]
    for f in funcs:
        f()
        print("OK", f.__name__)
