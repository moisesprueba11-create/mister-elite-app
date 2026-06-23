#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de pizarras Rondos 35-50 (MISTER ÉLITE)."""
import sys, math
sys.path.insert(0, '/home/user/mister-elite-app/curso-rondos/graficos/lib')
from pitch import Pitch

OUT = '/home/user/mister-elite-app/curso-rondos/graficos'


def box(p, x1, y1, x2, y2):
    """Conos en las 4 esquinas de un rectángulo."""
    p.cone(x1, y1); p.cone(x2, y1); p.cone(x1, y2); p.cone(x2, y2)


# ---------------------------------------------------------------------------
# R35 — Conservar-progresar-finalizar (3 zonas en línea hacia portería)
# ---------------------------------------------------------------------------
def r35():
    p = Pitch(title="Rondo 35 — Conservar · Progresar · Finalizar",
              subtitle="4v2 → pasillo +1 comodín → 2v1+portero · 3 zonas ~45 m · finalización",
              half="att")
    # Zona 1 (conservación, abajo) y2 ~ 55-68 ; Zona 2 (progresión) 70-80 ; Zona 3 (finalización) 82-96
    # Zona 1 conservación
    p.zone(22, 55, 78, 68, label="ZONA 1 · conservar (4v2)")
    box(p, 22, 55, 78, 68)
    # Zona 2 progresión (pasillo)
    p.zone(30, 70, 70, 79, label="ZONA 2 · progresar")
    box(p, 30, 70, 70, 79)
    # Zona 3 finalización
    p.zone(28, 82, 72, 95, label="ZONA 3 · finalizar (2v1 + portero)")
    box(p, 28, 82, 72, 95)

    # Zona 1: 4 azules + 2 rojos
    p.player(28, 58, "P", team="own"); p.player(72, 58, "P", team="own")
    p.player(28, 66, "P", team="own"); p.player(72, 66, "P", team="own")
    p.player(45, 62, "D", team="rival"); p.player(58, 63, "D", team="rival")
    p.ball(28, 58)
    # pases zona 1
    p.arrow(28, 58, 72, 58, kind="pass", label="1")
    p.arrow(72, 58, 72, 66, kind="pass", label="2")
    # Zona 2: comodín
    p.player(50, 75, "C", team="neutral", role="comodín")
    p.arrow(72, 66, 50, 75, kind="pass", label="3 progresa")
    # Zona 3: 2 azules vs 1 rojo + portero
    p.player(40, 87, "P", team="own"); p.player(60, 88, "P", team="own")
    p.player(50, 90, "D", team="rival")
    p.player(50, 97, "POR", team="rival", role="portero", role_below=True)
    p.goalmini(50, 99)
    p.arrow(50, 75, 40, 87, kind="pass", label="4")
    p.arrow(40, 87, 60, 88, kind="pass", label="5")
    p.arrow(60, 88, 50, 98, kind="drive", label="gol")
    p.note(50, 51, "5 pases mín. en Z1 · resolver 2v1 en ≤5 s · secuencia completa = 3 pts")
    p.legend(["own", "rival", "neutral", "pass", "drive", "zone"])
    p.save(f"{OUT}/rondo-35.svg")


# ---------------------------------------------------------------------------
# R36 — Liga 4v4v4 (dos equipos conservan 8 vs 4 que presionan)
# ---------------------------------------------------------------------------
def r36():
    p = Pitch(title="Rondo 36 — Liga de rondos 4v4v4",
              subtitle="3 equipos de 4 · 8 conservan vs 4 presionan · 18×18 m · marcador",
              half=None)
    box(p, 22, 28, 78, 72)
    p.zone(22, 28, 78, 72)
    # Equipo A (azul own) 4 jugadores perímetro
    p.player(28, 34, "A", team="own"); p.player(50, 31, "A", team="own")
    p.player(28, 66, "A", team="own"); p.player(40, 50, "A", team="own")
    # Equipo B (otro poseedor) -> usamos neutral ámbar como segundo equipo poseedor
    p.player(72, 34, "B", team="neutral"); p.player(72, 66, "B", team="neutral")
    p.player(50, 69, "B", team="neutral"); p.player(60, 50, "B", team="neutral")
    # Equipo rojo (4 presionan)
    p.player(44, 40, "D", team="rival"); p.player(56, 40, "D", team="rival")
    p.player(44, 60, "D", team="rival"); p.player(56, 60, "D", team="rival")
    p.ball(28, 34)
    p.arrow(28, 34, 40, 50, kind="pass", label="1")
    p.arrow(40, 50, 60, 50, kind="pass", label="2")
    p.arrow(60, 50, 72, 66, kind="pass", label="3")
    # marcador
    p.note(50, 22, "MARCADOR   A: 0   B: 0   ·   10 pases (A+B) = 1 pto para ambos")
    p.note(50, 78, "Quien provoca la pérdida pasa a presionar · máx. 3 toques")
    p.legend(["own", "neutral", "rival", "pass"])
    p.save(f"{OUT}/rondo-36.svg")


# ---------------------------------------------------------------------------
# R37 — Puntos por orientación (6v3, 4 cuartos)
# ---------------------------------------------------------------------------
def r37():
    p = Pitch(title="Rondo 37 — Puntos por orientación",
              subtitle="6v3 · 20×20 m en 4 cuartos · pase corto 0 · cambio 1 · diagonal 3",
              half=None)
    box(p, 22, 26, 78, 74)
    p.zone(22, 26, 78, 74)
    # divisorias de cuartos
    p.arrow(50, 26, 50, 74, kind="run"); p.arrow(22, 50, 78, 50, kind="run")
    p.note(35, 71, "C1"); p.note(65, 71, "C2"); p.note(35, 29, "C3"); p.note(65, 29, "C4")
    # 6 azules (perímetro, repartidos por cuartos)
    p.player(28, 66, "P", team="own"); p.player(42, 70, "P", team="own")
    p.player(72, 66, "P", team="own"); p.player(72, 34, "P", team="own")
    p.player(28, 34, "P", team="own"); p.player(58, 30, "P", team="own")
    # 3 rojos centro
    p.player(45, 55, "D", team="rival"); p.player(58, 50, "D", team="rival")
    p.player(50, 42, "D", team="rival")
    p.ball(28, 66)
    p.arrow(28, 66, 42, 70, kind="pass", label="0 mismo cuarto")
    p.arrow(42, 70, 72, 66, kind="pass", label="1 cambia cuarto")
    p.arrow(72, 66, 28, 34, kind="pass", label="3 diagonal")
    p.note(50, 21, "Pase recibido y controlado · diagonal a cuarto opuesto = 3 ptos · robo rojo = -2")
    p.legend(["own", "rival", "pass", "zone"])
    p.save(f"{OUT}/rondo-37.svg")


# ---------------------------------------------------------------------------
# R38 — Torneo eliminatorio (4 cuadros 5v2 en paralelo)
# ---------------------------------------------------------------------------
def r38():
    p = Pitch(title="Rondo 38 — Torneo de rondos eliminatorio",
              subtitle="4 cuadros 5v2 (12×12 m) en paralelo · menos pases/ronda = eliminado",
              half=None)
    centers = [(36, 64, "1"), (64, 64, "2"), (36, 36, "3"), (64, 36, "4")]
    for cx, cy, n in centers:
        x1, x2 = cx - 11, cx + 11
        y1, y2 = cy - 11, cy + 11
        box(p, x1, y1, x2, y2)
        p.zone(x1, y1, x2, y2)
        p.note(cx, y2 - 3, f"Cuadro {n}", size=9)
        # 5 azules perímetro
        p.player(cx, y2 - 1, "P", team="own"); p.player(x1 + 1, cy + 5, "P", team="own")
        p.player(x2 - 1, cy + 5, "P", team="own"); p.player(x1 + 2, y1 + 2, "P", team="own")
        p.player(x2 - 2, y1 + 2, "P", team="own")
        # 2 rojos
        p.player(cx - 4, cy, "D", team="rival"); p.player(cx + 4, cy, "D", team="rival")
        p.ball(cx, y2 - 1)
    p.note(50, 50, "90 s/ronda", size=11)
    p.note(50, 13, "El cuadro con menos pases se elimina cada ronda · final 5v4")
    p.legend(["own", "rival", "zone"])
    p.save(f"{OUT}/rondo-38.svg")


# ---------------------------------------------------------------------------
# R39 — Escalera de toques (6v2 +1 comodín)
# ---------------------------------------------------------------------------
def r39():
    p = Pitch(title="Rondo 39 — Escalera de toques",
              subtitle="6v2 (+1 comodín) · 16×16 m · libre→3→2→1 toque por minuto",
              half=None)
    box(p, 24, 28, 76, 72)
    p.zone(24, 28, 76, 72)
    # 6 azules perímetro
    p.player(50, 70, "P", team="own"); p.player(26, 60, "P", team="own")
    p.player(74, 60, "P", team="own"); p.player(26, 40, "P", team="own")
    p.player(74, 40, "P", team="own"); p.player(50, 30, "P", team="own")
    # comodín interior
    p.player(40, 50, "C", team="neutral", role="+1 toque")
    # 2 rojos
    p.player(54, 54, "D", team="rival"); p.player(60, 46, "D", team="rival")
    p.ball(50, 70)
    p.arrow(50, 70, 26, 60, kind="pass", label="1")
    p.arrow(26, 60, 40, 50, kind="pass", label="2")
    p.arrow(40, 50, 74, 40, kind="pass", label="3")
    # cartel escalera
    p.note(50, 22, "ESCALERA:  min1 libre  ·  min2 ≤3  ·  min3 ≤2  ·  min4 = 1 toque")
    p.note(50, 78, "8 pases = 1 pto · comodín juega un toque por encima de la condición")
    p.legend(["own", "rival", "neutral", "pass"])
    p.save(f"{OUT}/rondo-39.svg")


# ---------------------------------------------------------------------------
# R40 — Rondo del premio (5v3, romper línea activa comodín 15 s)
# ---------------------------------------------------------------------------
def r40():
    p = Pitch(title="Rondo 40 — Rondo del premio",
              subtitle="5v3 · 18×18 m · romper línea de los 3 rojos activa comodín 15 s (6v3)",
              half=None)
    box(p, 22, 28, 78, 72)
    p.zone(22, 28, 78, 72)
    # 5 azules perímetro
    p.player(50, 70, "P", team="own"); p.player(26, 58, "P", team="own")
    p.player(74, 58, "P", team="own"); p.player(30, 32, "P", team="own")
    p.player(70, 32, "P", team="own")
    # 3 rojos formando una línea (bloque)
    p.player(40, 52, "D", team="rival"); p.player(52, 50, "D", team="rival")
    p.player(64, 52, "D", team="rival")
    # comodín de premio en banda
    p.player(82, 50, "C", team="neutral", role="premio 15 s")
    p.ball(26, 58)
    # pase interior que rompe línea (entre 2 rojos)
    p.arrow(26, 58, 70, 32, kind="pass", label="rompe línea → activa premio")
    p.note(50, 22, "Pase interior entre 2 rojos (controlado) = comodín 15 s · renueva si repite")
    p.note(50, 78, "Cada robo rojo desactiva el comodín · medir % tiempo activo")
    p.legend(["own", "rival", "neutral", "pass"])
    p.save(f"{OUT}/rondo-40.svg")


# ---------------------------------------------------------------------------
# R41 — Tres equipos con permanencia (3 equipos de 3, 6v3)
# ---------------------------------------------------------------------------
def r41():
    p = Pitch(title="Rondo 41 — Tres equipos con permanencia",
              subtitle="3 equipos de 3 · 15×15 m · 6 conservan vs 3 presionan · cronómetro posesión",
              half=None)
    box(p, 26, 30, 74, 70)
    p.zone(26, 30, 74, 70)
    # Equipo A (own) 3
    p.player(50, 68, "A", team="own"); p.player(28, 56, "A", team="own")
    p.player(28, 40, "A", team="own")
    # Equipo B (neutral ámbar = segundo poseedor) 3
    p.player(72, 56, "B", team="neutral"); p.player(72, 40, "B", team="neutral")
    p.player(50, 32, "B", team="neutral")
    # Equipo rojo presiona 3
    p.player(46, 52, "D", team="rival"); p.player(58, 52, "D", team="rival")
    p.player(52, 44, "D", team="rival")
    p.ball(50, 68)
    p.arrow(50, 68, 72, 56, kind="pass", label="1")
    p.arrow(72, 56, 28, 40, kind="pass", label="2")
    p.note(50, 24, "Quien PIERDE el balón baja a presionar · el que presionaba sube")
    p.note(50, 76, "Cronómetro de tiempo en posesión · 12 pases = +30 s · gana quien más acumula")
    p.legend(["own", "neutral", "rival", "pass"])
    p.save(f"{OUT}/rondo-41.svg")


# ---------------------------------------------------------------------------
# R42 — Finalización condicionada (6v4 + 2 mini-porterías, banca o arriesga)
# ---------------------------------------------------------------------------
def r42():
    p = Pitch(title="Rondo 42 — Finalización condicionada",
              subtitle="6v4 · 24×18 m · 2 mini-porterías · 8 pases=1 pto · gol=3 / fallo=pierdes posesión",
              half="att")
    box(p, 20, 54, 80, 94)
    p.zone(20, 54, 80, 94)
    # 2 mini-porterías en el fondo (arriba)
    p.goalmini(38, 95); p.goalmini(62, 95)
    p.note(38, 97, "mini-portería", size=8); p.note(62, 97, "mini-portería", size=8)
    # 6 azules
    p.player(30, 60, "P", team="own"); p.player(70, 60, "P", team="own")
    p.player(28, 75, "P", team="own"); p.player(72, 75, "P", team="own")
    p.player(45, 84, "P", team="own"); p.player(58, 84, "P", team="own")
    # 4 rojos
    p.player(42, 66, "D", team="rival"); p.player(58, 66, "D", team="rival")
    p.player(45, 78, "D", team="rival"); p.player(60, 78, "D", team="rival")
    p.ball(30, 60)
    p.arrow(30, 60, 28, 75, kind="pass", label="1")
    p.arrow(28, 75, 45, 84, kind="pass", label="2 (cambio orient.)")
    p.arrow(45, 84, 38, 95, kind="drive", label="¿arriesga?")
    p.note(50, 57, "8 pases=1 pto · gol=+3 · fallo/robo=pierdes lo acumulado · tras 1 cambio orient.")
    p.legend(["own", "rival", "pass", "drive", "zone"])
    p.save(f"{OUT}/rondo-42.svg")


# ---------------------------------------------------------------------------
# R43 — Presión a contrarreloj (7v3, 22×22)
# ---------------------------------------------------------------------------
def r43():
    p = Pitch(title="Rondo 43 — Presión a contrarreloj",
              subtitle="7v3 · 22×22 m · los 3 rojos deben robar en <20 s · presión coordinada",
              half=None)
    box(p, 18, 22, 82, 78)
    p.zone(18, 22, 82, 78)
    # 7 azules amplio perímetro
    p.player(50, 75, "P", team="own"); p.player(24, 64, "P", team="own")
    p.player(76, 64, "P", team="own"); p.player(22, 38, "P", team="own")
    p.player(78, 38, "P", team="own"); p.player(38, 26, "P", team="own")
    p.player(62, 26, "P", team="own")
    # 3 rojos presionando (orientan robo)
    p.player(44, 56, "D", team="rival"); p.player(58, 54, "D", team="rival")
    p.player(50, 44, "D", team="rival")
    p.ball(50, 75)
    p.arrow(50, 75, 24, 64, kind="pass", label="1")
    p.arrow(24, 64, 22, 38, kind="pass", label="2")
    # presión coordinada (flechas rojas)
    p.arrow(44, 56, 30, 64, kind="block")
    p.arrow(58, 54, 50, 70, kind="block")
    p.note(50, 17, "Ventanas de 20 s · robo a tiempo = pto rojo · aguantar = pto azul · azules máx. 2 toques")
    p.legend(["own", "rival", "pass", "block"])
    p.save(f"{OUT}/rondo-43.svg")


# ---------------------------------------------------------------------------
# Helpers para rondos circulares
# ---------------------------------------------------------------------------
def circle_players(p, cx, cy, rx, ry, labels, team="own", start_deg=90, role=""):
    n = len(labels)
    pts = []
    for i, lab in enumerate(labels):
        ang = math.radians(start_deg - i * 360.0 / n)
        x = cx + rx * math.cos(ang)
        y = cy + ry * math.sin(ang)
        p.player(x, y, lab, team=team, role=role)
        pts.append((x, y))
    return pts


def circle_cones(p, cx, cy, rx, ry, n=12):
    for i in range(n):
        ang = math.radians(i * 360.0 / n)
        p.cone(cx + rx * math.cos(ang), cy + ry * math.sin(ang))


# ---------------------------------------------------------------------------
# R44 — El manín / burro (8v1, círculo)
# ---------------------------------------------------------------------------
def r44():
    p = Pitch(title="Rondo 44 — El manín / burro",
              subtitle="8v1 · círculo 8-9 m · quien pierde entra · caño = doble castigo",
              half=None)
    cx, cy, rx, ry = 50, 50, 27, 23
    circle_cones(p, cx, cy, rx, ry, n=12)
    p.zone(cx - rx, cy - ry, cx + rx, cy + ry, ellipse=True)
    pts = circle_players(p, cx, cy, rx - 2, ry - 2,
                         ["P", "P", "P", "P", "P", "P", "P", "P"], team="own")
    # burro al centro
    p.player(cx, cy, "D", team="rival", role="el manín")
    p.ball(*pts[0])
    # pases a ras de suelo rodeando
    p.arrow(pts[0][0], pts[0][1], pts[1][0], pts[1][1], kind="pass", label="1")
    p.arrow(pts[1][0], pts[1][1], pts[2][0], pts[2][1], kind="pass", label="2")
    p.arrow(pts[2][0], pts[2][1], pts[5][0], pts[5][1], kind="pass", label="3 (cruza)")
    p.note(50, 12, "Quien pierde el balón entra · caño = entra + vuelta al círculo · pase a ras de suelo")
    p.legend(["own", "rival", "pass"])
    p.save(f"{OUT}/rondo-44.svg")


# ---------------------------------------------------------------------------
# R45 — Multibalón (8v2, dos balones)
# ---------------------------------------------------------------------------
def r45():
    p = Pitch(title="Rondo 45 — Multibalón (dos balones)",
              subtitle="8v2 · 16×16 m · DOS balones a la vez · comunicación para no chocar",
              half=None)
    box(p, 24, 26, 76, 74)
    p.zone(24, 26, 76, 74)
    pts = []
    coords = [(50, 72), (28, 64), (72, 64), (26, 50), (74, 50),
              (28, 36), (72, 36), (50, 28)]
    for (x, y) in coords:
        p.player(x, y, "P", team="own"); pts.append((x, y))
    p.player(44, 54, "D", team="rival"); p.player(58, 46, "D", team="rival")
    # dos balones
    p.ball(50, 72); p.ball(26, 50)
    # cadena balón 1
    p.arrow(50, 72, 72, 64, kind="pass", label="bal.1")
    p.arrow(72, 64, 72, 36, kind="pass")
    # cadena balón 2
    p.arrow(26, 50, 28, 36, kind="pass", c="#7ee0ff", label="bal.2")
    p.arrow(28, 36, 50, 28, kind="drive")
    p.note(50, 20, "2 balones simultáneos · balones que chocan = prenda · rojo toca = sale ese balón")
    p.legend(["own", "rival", "pass"])
    p.save(f"{OUT}/rondo-45.svg")


# ---------------------------------------------------------------------------
# R46 — Rondo de colores (7v2 +1 comodín, conos 4 colores)
# ---------------------------------------------------------------------------
def r46():
    p = Pitch(title="Rondo 46 — Rondo de colores",
              subtitle="7v2 (+1 comodín) · 16×16 m · conos de 4 colores · reacción a la señal",
              half=None)
    x1, y1, x2, y2 = 24, 26, 76, 74
    p.zone(x1, y1, x2, y2)
    # conos de color en las 4 esquinas (con etiqueta de color)
    p.cone(x1, y2); p.note(x1 + 2, y2 + 3, "ROJO", size=8, c="#ff8a80")
    p.cone(x2, y2); p.note(x2 - 2, y2 + 3, "VERDE", size=8, c="#a5d6a7")
    p.cone(x1, y1); p.note(x1 + 2, y1 - 3, "AZUL", size=8, c="#90caf9")
    p.cone(x2, y1); p.note(x2 - 2, y1 - 3, "AMARILLO", size=8, c="#fff59d")
    # 7 azules
    coords = [(50, 71), (28, 62), (72, 62), (27, 50), (73, 50), (32, 30), (68, 30)]
    for (x, y) in coords:
        p.player(x, y, "P", team="own")
    # comodín
    p.player(50, 50, "C", team="neutral", role="comodín")
    # 2 rojos
    p.player(44, 56, "D", team="rival"); p.player(58, 44, "D", team="rival")
    p.ball(50, 71)
    p.arrow(50, 71, 50, 50, kind="pass", label="→ comodín (señal AMARILLO)")
    p.note(50, 20, "Rojo→pase a esa esquina · Verde→girar horario · Azul→1 toque · Amarillo→al comodín")
    p.legend(["own", "rival", "neutral", "pass"])
    p.save(f"{OUT}/rondo-46.svg")


# ---------------------------------------------------------------------------
# R47 — Carrusel (9v3, movimiento perpetuo)
# ---------------------------------------------------------------------------
def r47():
    p = Pitch(title="Rondo 47 — Carrusel",
              subtitle="9v3 · 22×22 m · tras pasar, reubicarse en un nuevo espacio (movimiento perpetuo)",
              half=None)
    box(p, 18, 22, 82, 78)
    p.zone(18, 22, 82, 78)
    # 9 azules
    coords = [(50, 75), (26, 66), (74, 66), (22, 50), (78, 50),
              (26, 34), (74, 34), (40, 26), (62, 26)]
    for (x, y) in coords:
        p.player(x, y, "P", team="own")
    # 3 rojos
    p.player(44, 56, "D", team="rival"); p.player(58, 54, "D", team="rival")
    p.player(50, 44, "D", team="rival")
    p.ball(50, 75)
    p.arrow(50, 75, 26, 66, kind="pass", label="1 pasa")
    # desmarque tras pasar (carrera blanca)
    p.arrow(50, 75, 62, 60, kind="run", label="se reubica")
    p.arrow(26, 66, 22, 50, kind="pass", label="2")
    p.note(50, 17, "Prohibido quedarse quieto tras pasar · pérdida = prenda 3 últimos + rota el medio")
    p.legend(["own", "rival", "pass", "run"])
    p.save(f"{OUT}/rondo-47.svg")


# ---------------------------------------------------------------------------
# R48 — Las parejas (8 en 4 parejas v2)
# ---------------------------------------------------------------------------
def r48():
    p = Pitch(title="Rondo 48 — Las parejas",
              subtitle="8 azules en 4 parejas vs 2 rojos · 18×18 m · cada pareja a <3 m",
              half=None)
    box(p, 22, 24, 78, 76)
    p.zone(22, 24, 78, 76)
    # 4 parejas (dos azules muy próximos), con elipse de pareja
    pairs = [(34, 68), (66, 68), (30, 36), (70, 36)]
    for (px, py) in pairs:
        p.zone(px - 6, py - 5, px + 6, py + 5, ellipse=True, fill_op=0.10)
        p.player(px - 4, py, "P", team="own"); p.player(px + 4, py, "P", team="own")
    # 2 rojos
    p.player(46, 52, "D", team="rival"); p.player(58, 48, "D", team="rival")
    p.ball(30, 68)
    p.arrow(38, 68, 66, 68, kind="pass", label="1 (pareja a pareja)")
    p.arrow(70, 64, 70, 40, kind="pass", label="2")
    p.note(50, 18, "Parejas a <3 m · si se separan o pierden, esa pareja entra al medio (2 a presionar)")
    p.legend(["own", "rival", "pass"])
    p.save(f"{OUT}/rondo-48.svg")


# ---------------------------------------------------------------------------
# R49 — Rondo reloj (8 numerados 1-8 v2)
# ---------------------------------------------------------------------------
def r49():
    p = Pitch(title="Rondo 49 — Rondo reloj",
              subtitle="8v2 · 16×16 m · azules numerados 1-8 · número / reloj / contrarreloj / salto",
              half=None)
    cx, cy, rx, ry = 50, 50, 27, 24
    circle_cones(p, cx, cy, rx, ry, n=8)
    p.zone(cx - rx, cy - ry, cx + rx, cy + ry, ellipse=True)
    pts = circle_players(p, cx, cy, rx - 2, ry - 2,
                         ["1", "2", "3", "4", "5", "6", "7", "8"], team="own", start_deg=90)
    # 2 rojos centro
    p.player(cx - 5, cy, "D", team="rival"); p.player(cx + 5, cy, "D", team="rival")
    p.ball(*pts[0])
    # "reloj": horario
    p.arrow(pts[0][0], pts[0][1], pts[1][0], pts[1][1], kind="pass", label="reloj")
    p.arrow(pts[1][0], pts[1][1], pts[2][0], pts[2][1], kind="pass")
    # "salto"
    p.arrow(pts[2][0], pts[2][1], pts[4][0], pts[4][1], kind="run", label="salto")
    p.note(50, 12, "Número → balón a ese jugador · reloj/contrarreloj → sentido · salto → no al de al lado")
    p.legend(["own", "rival", "pass", "run"])
    p.save(f"{OUT}/rondo-49.svg")


# ---------------------------------------------------------------------------
# R50 — Gran rondo final (12v3, la olla)
# ---------------------------------------------------------------------------
def r50():
    p = Pitch(title="Rondo 50 — Gran rondo final: la olla",
              subtitle="12v3 · círculo 12-14 m · 15 pases liberan a un jugador · caño manda al medio",
              half=None)
    cx, cy, rx, ry = 50, 50, 30, 27
    circle_cones(p, cx, cy, rx, ry, n=12)
    p.zone(cx - rx, cy - ry, cx + rx, cy + ry, ellipse=True)
    pts = circle_players(p, cx, cy, rx - 1, ry - 1,
                         ["P"] * 12, team="own", start_deg=90)
    # 3 rojos en el centro (la olla)
    p.player(cx, cy + 5, "D", team="rival"); p.player(cx - 5, cy - 3, "D", team="rival")
    p.player(cx + 5, cy - 3, "D", team="rival")
    p.ball(*pts[0])
    p.arrow(pts[0][0], pts[0][1], pts[1][0], pts[1][1], kind="pass", label="1")
    p.arrow(pts[1][0], pts[1][1], pts[2][0], pts[2][1], kind="pass", label="2")
    p.arrow(pts[2][0], pts[2][1], pts[7][0], pts[7][1], kind="pass", label="cruza")
    p.note(50, 9, "15 pases = libera un jugador / punto de grupo · caño = entrar al medio · récord de racha")
    p.legend(["own", "rival", "pass"])
    p.save(f"{OUT}/rondo-50.svg")


if __name__ == "__main__":
    for fn in [r35, r36, r37, r38, r39, r40, r41, r42, r43,
               r44, r45, r46, r47, r48, r49, r50]:
        fn()
        print("OK", fn.__name__)
