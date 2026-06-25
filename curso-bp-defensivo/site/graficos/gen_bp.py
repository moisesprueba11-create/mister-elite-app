#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pizarras del curso de Balón parado DEFENSIVO (MISTER ÉLITE).
Defendemos la portería de ARRIBA (half='att'). Azul = nosotros · rojo = rival.
Códigos en la ficha: P portero · Z zonal · H al hombre · B barrera."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from pitch import Pitch

def out(name): return os.path.join(HERE, name)
def att(t, s): return Pitch(t, half="att", subtitle=s, attack_arrow=False)
def half_def(t, s): return Pitch(t, half="def", subtitle=s, attack_arrow=False)
RR = 12
def Z(p, x, y): p.player(x, y, "Z", team="own", r=RR)
def H(p, x, y): p.player(x, y, "H", team="own", r=RR)
def B(p, x, y): p.player(x, y, "B", team="own", r=RR)
def G(p, x, y): p.player(x, y, "P", team="own", r=RR+1, role="portero", role_below=True)
def Rv(p, x, y, lab=""): p.player(x, y, lab, team="rival", r=RR)
def leg(p): p.note(50, 54, "P portero · Z zonal · H al hombre · azul nosotros · rojo rival", c="#cfe0ee", size=10)

# corner desde la derecha del ataque (banderín arriba-derecha)

# ===== 1) CÓRNER ZONAL =====
p = att("Córner defensivo · ZONAL", "cada uno protege un ESPACIO y ataca el balón · línea sobre el área pequeña")
p.zone(38, 84, 58, 95, "", c="#7ee0ff", fill_op=0.10)
p.zone(58, 84, 73, 95, "", c="#7ee0ff", fill_op=0.10)
p.zone(27, 84, 42, 95, "", c="#7ee0ff", fill_op=0.10)
G(p, 51, 96)
Z(p, 63, 90); Z(p, 35, 90); Z(p, 46, 88); Z(p, 54, 88); Z(p, 50, 82); Z(p, 50, 75)
p.note(65, 84, "1.er palo", c="#cfe0ee", size=10); p.note(48, 84, "corazón", c="#cfe0ee", size=10)
p.note(33, 84, "2.º palo", c="#cfe0ee", size=10); p.note(50, 79, "penalti", c="#cfe0ee", size=10)
p.note(50, 72, "frontal · rechaces", c="#cfe0ee", size=10)
Rv(p, 94, 97); p.ball(94, 97)
for x, y in [(43, 86), (57, 86), (50, 79), (40, 81)]: Rv(p, x, y)
p.arrow(94, 97, 51, 87, kind="pass", label="centro")
leg(p)
p.note(28, 64, "1-2 jugadores arriba (contra)", c="#fff5cc", size=11)
p.save(out("corner-zonal.svg"))

# ===== 2) CÓRNER AL HOMBRE =====
p = att("Córner defensivo · AL HOMBRE", "cada defensor marca a UN rematador · goal-side y en contacto")
G(p, 51, 96)
for (x, y) in [(43, 85), (57, 86), (49, 80), (38, 82), (60, 78)]:
    Rv(p, x, y); H(p, x + (3 if x < 50 else -3), y + 4)
Z(p, 64, 92); Z(p, 37, 92)
Rv(p, 94, 97); p.ball(94, 97)
p.arrow(94, 97, 51, 86, kind="pass", label="centro")
leg(p)
p.note(50, 64, "riesgo: bloqueos/pantallas y zonas sin dueño", c="#ff8a8a", size=11)
p.save(out("corner-hombre.svg"))

# ===== 3) CÓRNER MIXTO (recomendado) =====
p = att("Córner defensivo · MIXTO (recomendado)", "zona en las áreas críticas + hombre sobre los rematadores peligrosos")
p.zone(38, 84, 60, 95, "zona", c="#7ee0ff", fill_op=0.10)
G(p, 51, 96)
Z(p, 64, 90); Z(p, 36, 90); Z(p, 46, 87); Z(p, 55, 87); Z(p, 50, 81); Z(p, 50, 74)
for (x, y) in [(42, 84), (60, 83), (50, 78)]:
    Rv(p, x, y); H(p, x + (3 if x < 50 else -3), y + 4)
Rv(p, 94, 97); p.ball(94, 97)
p.arrow(94, 97, 51, 86, kind="pass", label="centro")
leg(p)
p.note(26, 64, "1 arriba (contra)", c="#fff5cc", size=11)
p.save(out("corner-mixto.svg"))

# ===== 4) INSWINGER vs OUTSWINGER (altura de línea) =====
p = att("Córner · INSWINGER vs OUTSWINGER", "ajusta la ALTURA de la línea zonal según el envío")
p.zone(34, 90, 66, 96, "INSWINGER → la línea BAJA, pegada a la línea de gol", c="#ff8a8a", fill_op=0.12)
p.zone(34, 79, 66, 86, "OUTSWINGER → la línea SUBE, sale del área pequeña", c="#7ee0ff", fill_op=0.12)
G(p, 51, 96)
for x in (42, 50, 58): Z(p, x, 92)
Rv(p, 94, 97); p.ball(94, 97)
p.arrow(94, 97, 57, 93, kind="pass", c="#ff8a8a", label="inswinger")
p.arrow(94, 97, 50, 82, kind="pass", c="#7ee0ff", label="outswinger")
p.arrow(34, 91, 34, 82, kind="run", label="sube")
p.save(out("corner-swinger.svg"))

# ===== 5) CÓRNER EN CORTO (defensa) =====
p = att("Córner en corto · DEFENSA", "1 (mejor 2) defensores salen · no regales el centro fácil")
G(p, 51, 96)
Z(p, 63, 90); Z(p, 37, 90); Z(p, 47, 87); Z(p, 55, 87); Z(p, 50, 82)
Rv(p, 94, 97); p.ball(94, 97); Rv(p, 85, 90)
H(p, 89, 93); H(p, 80, 86)
p.arrow(94, 97, 85, 90, kind="pass", label="corto")
p.arrow(84, 88, 88, 92, kind="run"); p.arrow(74, 84, 80, 88, kind="run")
p.note(50, 70, "crear 2v2 en la banda · no quedar en inferioridad", c="#fff5cc", size=11)
p.save(out("corner-corto.svg"))

# ===== 6) TRANSICIÓN tras despejar =====
p = att("Tras el córner · TRANSICIÓN", "despejar ALTO, LEJOS y ANCHO → subir la línea y salir al contra")
G(p, 51, 96)
B(p, 50, 88)  # el que despeja
for x in (40, 60): Z(p, x, 86)
p.ball(50, 88)
p.arrow(50, 88, 18, 70, kind="pass", label="despeje a banda")
p.player(25, 62, "", team="own", r=RR, role="adelantado", role_below=True)
p.arrow(20, 67, 27, 60, kind="run", label="contra")
for x in (40, 50, 60): p.arrow(x, 84, x, 76, kind="run")
p.note(50, 80, "↑ subir la línea (fuera de juego)", c="#fff5cc", size=11)
for x, y in [(46, 83), (57, 83), (50, 80)]: Rv(p, x, y)
p.save(out("corner-transicion.svg"))

# ===== 7) FALTA FRONTAL · BARRERA =====
p = att("Falta frontal · LA BARRERA", "la barrera tapa el palo del portero · él cubre el resto · saltar de frente")
ball_x, ball_y = 50, 70
p.ball(ball_x, ball_y); Rv(p, 50, 67, "")  # lanzador
# barrera de 4 cubre el lado derecho (palo cercano del portero)
for x in (49, 53, 57, 61): B(p, x, 80)
G(p, 42, 94)  # portero cubre el lado libre (izquierda)
p.player(55, 83, "", team="own", r=RR-2, role="tumbado", role_below=True)  # tumbado tras la barrera
p.player(46, 78, "", team="own", r=RR-2, role="saltador", role_below=True)  # sale al golpeo
p.note(50, 75, "9,15 m", c="#cfe0ee", size=10)
p.arrow(50, 70, 38, 92, kind="pass", c="#ff8a8a", label="tiro")
# marcaje en el área
for x, y in [(35, 86), (63, 86)]: Rv(p, x, y); H(p, x + (3 if x < 50 else -3), y + 4)
leg(p)
p.save(out("falta-barrera.svg"))

# ===== 8) FALTA LATERAL (defender como un córner) =====
p = att("Falta lateral · COMO UN CÓRNER", "poca o ninguna barrera · línea zonal + hombre · el portero entra en juego")
p.zone(38, 84, 60, 95, "zona", c="#7ee0ff", fill_op=0.10)
G(p, 51, 96)
Z(p, 63, 90); Z(p, 37, 90); Z(p, 47, 87); Z(p, 55, 87); Z(p, 50, 81)
for (x, y) in [(43, 84), (58, 83), (50, 78)]:
    Rv(p, x, y); H(p, x + (3 if x < 50 else -3), y + 4)
B(p, 70, 80); B(p, 74, 80)  # mini-barrera de 1-2 por si tiran al palo
Rv(p, 86, 68); p.ball(86, 68)
p.arrow(86, 68, 51, 86, kind="pass", label="centro")
p.note(28, 64, "1 arriba (contra)", c="#fff5cc", size=11)
leg(p)
p.save(out("falta-lateral.svg"))

# ===== 9) Nº DE BARRERA SEGÚN LA ZONA =====
p = att("¿Cuántos en la barrera? · POR ZONA", "más frontal y cerca = más barrera · más lateral = menos barrera, más marcaje")
G(p, 50, 96)
# tres faltas tipo
p.ball(50, 70); p.note(50, 66, "FRONTAL ~18 m → 4-5", c="#fff5cc", size=11)
for x in (47, 51, 55, 59): B(p, x, 80)
p.ball(76, 66); p.note(76, 61, "LATERAL ~22 m → 2-3", c="#fff5cc", size=11)
for x in (66, 70): B(p, x, 76)
p.ball(50, 58); p.note(50, 55, "LEJANA >30 m → 0-1 (como un centro)", c="#fff5cc", size=11)
p.save(out("falta-numeros.svg"))

# ===== 10) SAQUE DE BANDA EN CAMPO PROPIO =====
p = half_def("Saque de banda propio · DEFENSA", "marca los apoyos · presiona al sacador · gana profundidad · evita el saque rápido")
Rv(p, 6, 60, "")  # sacador en la banda
p.ball(4, 60)
H(p, 14, 58)  # un jugador cerca/detrás del sacador (anula la pared)
for (rx, ry) in [(18, 70), (24, 52), (30, 64)]:
    Rv(p, rx, ry); H(p, rx - 4, ry - 3)  # marcar los apoyos goal-side
p.arrow(6, 60, 18, 70, kind="pass", c="#ff8a8a", label="apoyo")
p.note(55, 40, "orienta el saque hacia atrás/banda y presiona tras el control", c="#fff5cc", size=11)
p.save(out("saque-propio.svg"))

# ===== 11) SAQUE DE BANDA LARGO (como un córner) =====
p = att("Saque de banda LARGO · COMO UN CÓRNER", "sin fuera de juego · primer palo fijo · target marcado por delante · portero al mando")
p.zone(38, 84, 60, 95, "zona", c="#7ee0ff", fill_op=0.10)
G(p, 51, 96)
Z(p, 64, 90)  # primer palo fijo
Z(p, 36, 90); Z(p, 47, 87); Z(p, 55, 87); Z(p, 50, 81)
# target del flick-on marcado POR DELANTE en el primer palo
Rv(p, 60, 84, ""); H(p, 60, 88)
for (x, y) in [(44, 84), (50, 78)]: Rv(p, x, y); H(p, x + (3 if x < 50 else -3), y + 4)
Rv(p, 6, 80, ""); p.ball(4, 80)  # sacador
p.arrow(6, 80, 60, 86, kind="pass", label="plano al 1.er palo")
p.player(50, 72, "", team="own", r=RR, role="2.ª jugada", role_below=True)
leg(p)
p.save(out("saque-largo.svg"))

print("BP defensivo OK")
