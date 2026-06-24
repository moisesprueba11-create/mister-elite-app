#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las 30 pizarras de ruedas de pases del curso (MISTER ÉLITE)."""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from drill import DrillPitch
from pitch import Pitch

def out(name): return os.path.join(HERE, name)

def frame(p):
    """marco sutil del área de trabajo (sin conos de esquina)."""
    p.field(8, 8, 92, 92, corners=False, stroke="#ffffff", w=1.6, dash="4 6")

def st(p, x, y, letter, team="own"):
    p.player(x, y, letter, team=team)

# ============================ FAMILIA 1 · BÁSICAS ============================

# 01 Cuadrado base
p = DrillPitch("Rueda 01 — Cuadrado base", "4 estaciones · 12×12 m · primer toque orientado")
frame(p)
st(p, 22, 22, "A"); st(p, 78, 22, "B"); st(p, 78, 78, "C"); st(p, 22, 78, "D")
p.ball(28, 22)
p.arrow(22, 22, 78, 22, kind="pass", label="1"); p.arrow(78, 22, 78, 78, kind="pass", label="2")
p.arrow(78, 78, 22, 78, kind="pass", label="3"); p.arrow(22, 78, 22, 22, kind="pass", label="4")
p.save(out("rueda-01.svg"))

# 02 Rombo
p = DrillPitch("Rueda 02 — Rombo (diamante)", "4 estaciones · 15×15 m · orientación en diagonal")
frame(p)
st(p, 50, 16, "A"); st(p, 84, 50, "B"); st(p, 50, 84, "C"); st(p, 16, 50, "D")
p.ball(56, 18)
p.arrow(50, 16, 84, 50, kind="pass", label="1"); p.arrow(84, 50, 50, 84, kind="pass", label="2")
p.arrow(50, 84, 16, 50, kind="pass", label="3"); p.arrow(16, 50, 50, 16, kind="pass", label="4")
p.save(out("rueda-02.svg"))

# 03 Triángulo de apoyos
p = DrillPitch("Rueda 03 — Triángulo de apoyos", "3 estaciones · ~15 m · triangulación y reapoyo")
frame(p)
st(p, 50, 20, "A"); st(p, 82, 74, "B"); st(p, 18, 74, "C")
p.ball(56, 22)
p.arrow(50, 20, 82, 74, kind="pass", label="1"); p.arrow(82, 74, 18, 74, kind="pass", label="2")
p.arrow(18, 74, 50, 20, kind="pass", label="3")
p.note(50, 90, "variante: “sigue tu pase” (A va detrás del balón)", c="#fff5cc", size=11)
p.save(out("rueda-03.svg"))

# 04 Forma en Y
p = DrillPitch("Rueda 04 — Forma en Y", "4 estaciones · tronco + dos brazos · introduce el tercer hombre")
frame(p)
st(p, 50, 16, "A"); st(p, 50, 50, "B"); st(p, 22, 84, "C"); st(p, 78, 84, "D")
p.ball(56, 18)
p.arrow(50, 16, 50, 50, kind="pass", label="1"); p.arrow(50, 50, 22, 84, kind="pass", label="2")
p.arrow(22, 84, 50, 50, kind="pass", label="3"); p.arrow(50, 50, 78, 84, kind="pass", label="4")
p.note(50, 92, "B juega de cara y alterna brazos", c="#fff5cc", size=11)
p.save(out("rueda-04.svg"))

# 05 Estrella / 5 puntas
p = DrillPitch("Rueda 05 — Estrella (5 puntas)", "5 estaciones · pentágono · visión periférica y timing")
frame(p)
cx, cy, r = 50, 52, 36
pts = {}
for i, L in enumerate(["A", "B", "C", "D", "E"]):
    a = math.radians(90 + i * 72)
    pts[L] = (cx + r * math.cos(a), cy + r * math.sin(a))
for L, (x, y) in pts.items(): st(p, x, y, L)
p.ball(pts["A"][0] + 6, pts["A"][1])
seq = ["A", "C", "E", "B", "D", "A"]
for i in range(5):
    (x1, y1), (x2, y2) = pts[seq[i]], pts[seq[i + 1]]
    p.arrow(x1, y1, x2, y2, kind="pass", label=str(i + 1))
p.save(out("rueda-05.svg"))

# ============================ FAMILIA 2 · MOVILIDAD ============================

# 06 Sigue tu pase
p = DrillPitch("Rueda 06 — Sigue tu pase", "cuadrado 15×15 m · correr a la estación a la que pasas")
frame(p)
st(p, 22, 24, "A"); st(p, 78, 24, "B"); st(p, 78, 78, "C"); st(p, 22, 78, "D")
p.ball(28, 24)
p.arrow(22, 24, 78, 24, kind="pass", label="1"); p.arrow(28, 28, 70, 28, kind="run", label="sigue")
p.arrow(78, 24, 78, 78, kind="pass", label="2"); p.arrow(74, 30, 74, 72, kind="run")
p.save(out("rueda-06.svg"))

# 07 Rondó de circulación con rotación
p = DrillPitch("Rueda 07 — Rotación interior con comodín", "4 + comodín central · sostener y rotar tras pasar")
frame(p)
st(p, 50, 85, "A"); st(p, 85, 52, "B"); st(p, 50, 19, "C"); st(p, 15, 52, "D")
st(p, 50, 52, "E", team="neutral")
p.ball(56, 85)
p.arrow(50, 85, 50, 52, kind="pass", label="1"); p.arrow(50, 52, 85, 52, kind="pass", label="2")
p.arrow(85, 52, 50, 19, kind="pass", label="3")
p.note(50, 94, "A entra al centro · E sale a la estación de A", c="#fff5cc", size=11)
p.save(out("rueda-07.svg"))

# 08 Cambio de estación (L)
p = DrillPitch("Rueda 08 — Cambio de estación (L)", "relevo posicional · desmarque de recepción")
frame(p)
st(p, 20, 80, "A"); st(p, 82, 80, "B"); st(p, 20, 20, "C")
p.ball(26, 80)
p.arrow(20, 80, 82, 80, kind="pass", label="1"); p.arrow(82, 80, 60, 80, kind="drive", label="2")
p.arrow(60, 80, 20, 20, kind="pass", label="3"); p.arrow(28, 26, 76, 74, kind="run", label="C ocupa B")
p.save(out("rueda-08.svg"))

# 09 Molino / rotación de 3
p = DrillPitch("Rueda 09 — Molino (rotación de 3)", "el triángulo “gira” · cada pasador rota a la siguiente")
frame(p)
st(p, 50, 82, "A"); st(p, 82, 25, "B"); st(p, 18, 25, "C")
p.ball(56, 82)
p.arrow(50, 82, 82, 25, kind="pass", label="1"); p.arrow(54, 78, 78, 30, kind="run")
p.arrow(82, 25, 18, 25, kind="pass", label="2"); p.arrow(78, 25, 22, 25, kind="run")
p.save(out("rueda-09.svg"))

# 10 Cruce y permuta (doble rombo)
p = DrillPitch("Rueda 10 — Cruce y permuta", "rombo 16 m · permutas y desmarques cruzados")
frame(p)
st(p, 50, 15, "A"); st(p, 85, 52, "B"); st(p, 50, 88, "C"); st(p, 15, 52, "D")
p.ball(56, 16)
p.arrow(50, 15, 50, 88, kind="pass", label="1"); p.arrow(50, 88, 85, 52, kind="pass", label="2")
p.arrow(85, 52, 15, 52, kind="pass", label="3")
p.arrow(80, 58, 22, 58, kind="run", label="permutan B↔D")
p.save(out("rueda-10.svg"))

# ============================ FAMILIA 3 · PARED / TERCER HOMBRE ============================

# 11 Pase y pared
p = DrillPitch("Rueda 11 — Pase y pared (give-and-go)", "pared y desmarque de ruptura · 1-2")
frame(p)
st(p, 30, 16, "A"); st(p, 54, 30, "B", team="neutral"); st(p, 50, 86, "C")
p.ball(36, 16)
p.arrow(30, 16, 54, 30, kind="pass", label="1"); p.arrow(34, 20, 40, 48, kind="run")
p.arrow(54, 30, 40, 50, kind="pass", label="2"); p.arrow(40, 50, 50, 82, kind="drive", label="3")
p.save(out("rueda-11.svg"))

# 12 Dejar de cara
p = DrillPitch("Rueda 12 — Dejar de cara", "apoyo de espaldas · descarga de primeras (juego de pivote)")
frame(p)
st(p, 50, 18, "A"); st(p, 50, 55, "B", team="neutral"); st(p, 76, 44, "C")
p.ball(56, 18)
p.arrow(50, 18, 50, 55, kind="pass", label="1"); p.arrow(50, 55, 76, 44, kind="pass", label="2")
p.arrow(76, 44, 56, 22, kind="pass", label="3")
p.note(50, 90, "B deja de cara a 1 toque", c="#fff5cc", size=11)
p.save(out("rueda-12.svg"))

# 13 Tercer hombre
p = DrillPitch("Rueda 13 — Tercer hombre", "A→B (de espaldas)→C que aparece desde atrás")
frame(p)
st(p, 40, 18, "A"); st(p, 52, 52, "B", team="neutral"); st(p, 80, 82, "C")
p.ball(46, 18)
p.arrow(40, 18, 52, 52, kind="pass", label="1"); p.arrow(52, 52, 80, 82, kind="pass", label="2")
p.arrow(62, 34, 78, 76, kind="run", label="C aparece"); p.arrow(80, 82, 84, 70, kind="drive", label="3")
p.save(out("rueda-13.svg"))

# 14 Pared doble
p = DrillPitch("Rueda 14 — Pared doble (uno-dos encadenado)", "enlazar dos paredes en conducción")
frame(p)
st(p, 20, 15, "A"); st(p, 40, 42, "B", team="neutral"); st(p, 72, 60, "C", team="neutral"); st(p, 55, 88, "D")
p.ball(26, 15)
p.arrow(20, 15, 40, 42, kind="pass", label="1"); p.arrow(40, 42, 32, 50, kind="pass", label="2")
p.arrow(32, 50, 72, 60, kind="pass", label="3"); p.arrow(72, 60, 55, 70, kind="pass", label="4")
p.arrow(55, 70, 55, 86, kind="drive", label="5")
p.save(out("rueda-14.svg"))

# 15 Tercer hombre con cambio de orientación
p = DrillPitch("Rueda 15 — Tercer hombre + cambio", "termina en cambio de banda", ratio=0.66)
frame(p)
st(p, 16, 35, "A"); st(p, 44, 52, "B", team="neutral"); st(p, 60, 58, "C"); st(p, 86, 60, "D")
p.ball(20, 35)
p.arrow(16, 35, 44, 52, kind="pass", label="1"); p.arrow(44, 52, 60, 58, kind="pass", label="2")
p.arrow(60, 58, 86, 60, kind="pass", label="3 cambio"); p.arrow(86, 60, 80, 40, kind="drive", label="4")
p.save(out("rueda-15.svg"))

# ============================ FAMILIA 4 · PROGRESIÓN ============================

# 16 Salida en rombo
p = DrillPitch("Rueda 16 — Salida en rombo (build-up)", "salida de balón desde zona baja")
frame(p)
st(p, 50, 14, "A"); st(p, 25, 34, "B"); st(p, 75, 34, "C"); st(p, 50, 52, "D", team="neutral")
p.ball(56, 14)
p.arrow(50, 14, 25, 34, kind="pass", label="1"); p.arrow(25, 34, 50, 52, kind="pass", label="2")
p.arrow(50, 52, 75, 34, kind="pass", label="3"); p.arrow(75, 34, 78, 80, kind="drive", label="4 progresa")
p.save(out("rueda-16.svg"))

# 17 De carril a carril
p = DrillPitch("Rueda 17 — De carril a carril", "circular de banda a banda rompiendo por dentro", ratio=0.66)
frame(p)
st(p, 15, 30, "A"); st(p, 40, 58, "B"); st(p, 60, 38, "C"); st(p, 85, 64, "D")
p.ball(19, 30)
p.arrow(15, 30, 40, 58, kind="pass", label="1"); p.arrow(40, 58, 60, 38, kind="pass", label="2")
p.arrow(60, 38, 85, 64, kind="pass", label="3"); p.arrow(85, 64, 80, 40, kind="drive", label="4")
p.save(out("rueda-17.svg"))

# 18 Romper líneas
p = DrillPitch("Rueda 18 — Romper líneas", "pase vertical filtrado entre líneas + control orientado")
frame(p)
st(p, 50, 14, "A"); st(p, 50, 58, "B", team="neutral"); st(p, 50, 86, "C")
p.cone(42, 44); p.cone(58, 44)
p.ball(56, 14)
p.arrow(50, 14, 50, 56, kind="pass", label="1 filtra"); p.arrow(50, 58, 50, 86, kind="pass", label="2")
p.arrow(50, 86, 60, 78, kind="drive", label="3")
p.note(50, 38, "puerta = línea rival", c="#cfe0ee", size=10)
p.save(out("rueda-18.svg"))

# 19 Subir el balón en tres zonas
p = DrillPitch("Rueda 19 — Subir en tres zonas", "progresión baja → media → alta con apoyos escalonados", ratio=1.25)
frame(p)
st(p, 50, 12, "A"); st(p, 30, 35, "B"); st(p, 70, 52, "C"); st(p, 50, 70, "D", team="neutral"); st(p, 50, 88, "E")
p.ball(56, 12)
p.arrow(50, 12, 30, 35, kind="pass", label="1"); p.arrow(30, 35, 70, 52, kind="pass", label="2")
p.arrow(70, 52, 50, 70, kind="pass", label="3"); p.arrow(50, 70, 50, 88, kind="pass", label="4")
p.save(out("rueda-19.svg"))

# 20 Salida con desdoblamiento
p = DrillPitch("Rueda 20 — Salida con desdoblamiento", "banda + desdoblamiento del lateral (sobremarca)", ratio=1.2)
frame(p)
st(p, 38, 18, "A"); st(p, 30, 40, "B"); st(p, 26, 66, "C", team="neutral"); st(p, 58, 82, "D")
p.ball(44, 18)
p.arrow(38, 18, 30, 40, kind="pass", label="1"); p.arrow(30, 40, 26, 66, kind="pass", label="2")
p.arrow(26, 66, 56, 80, kind="pass", label="3"); p.arrow(40, 50, 56, 78, kind="run", label="desdobla")
p.arrow(58, 82, 60, 64, kind="drive", label="4")
p.save(out("rueda-20.svg"))

# ============================ FAMILIA 5 · FINALIZACIÓN (media pista) ============================

def att(title, sub):
    return Pitch(title, half="att", subtitle=sub, attack_arrow=False)

# 21 Centro y remate
p = att("Rueda 21 — Centro y remate", "apertura a banda · centro y remate de primeras")
p.player(36, 58, "A"); p.player(20, 66, "B"); p.player(56, 82, "R")
p.ball(40, 58)
p.arrow(36, 58, 20, 66, kind="pass", label="1"); p.arrow(20, 66, 18, 88, kind="drive", label="2")
p.arrow(18, 88, 52, 90, kind="pass", label="3 centro"); p.arrow(56, 82, 50, 97, kind="drive", label="remate")
p.save(out("rueda-21.svg"))

# 22 Pase de la muerte
p = att("Rueda 22 — Pase de la muerte", "llegada desde segunda línea · corte atrás y definición")
p.player(40, 60, "A"); p.player(72, 72, "B"); p.player(52, 80, "C")
p.ball(45, 60)
p.arrow(40, 60, 72, 72, kind="pass", label="1"); p.arrow(72, 72, 80, 92, kind="drive", label="2")
p.arrow(80, 92, 52, 84, kind="pass", label="3 atrás"); p.arrow(52, 80, 50, 96, kind="drive", label="remate")
p.save(out("rueda-22.svg"))

# 23 Pared y definición
p = att("Rueda 23 — Pared y definición", "uno-dos frente al área y disparo")
p.player(50, 62, "A"); p.player(64, 70, "B", team="neutral")
p.ball(45, 62)
p.arrow(50, 62, 64, 70, kind="pass", label="1"); p.arrow(52, 66, 52, 84, kind="run")
p.arrow(64, 70, 52, 84, kind="pass", label="2"); p.arrow(52, 84, 50, 97, kind="drive", label="3 define")
p.save(out("rueda-23.svg"))

# 24 Combinación central + remate
p = att("Rueda 24 — Triángulo ofensivo + remate", "triangulación en zona de creación que acaba en disparo")
p.player(38, 60, "A"); p.player(56, 72, "B", team="neutral"); p.player(64, 62, "C")
p.ball(43, 60)
p.arrow(38, 60, 56, 72, kind="pass", label="1"); p.arrow(56, 72, 64, 62, kind="pass", label="2 de cara")
p.arrow(64, 62, 52, 96, kind="drive", label="3 dispara")
p.save(out("rueda-24.svg"))

# 25 Doble banda y centro
p = att("Rueda 25 — Doble banda y centro", "circulación amplia con cambio de banda y finalización")
p.player(20, 56, "A"); p.player(50, 62, "B"); p.player(82, 64, "C"); p.player(54, 84, "R")
p.ball(24, 56)
p.arrow(20, 56, 50, 62, kind="pass", label="1"); p.arrow(50, 62, 82, 64, kind="pass", label="2 cambio")
p.arrow(82, 64, 84, 90, kind="drive", label="3"); p.arrow(84, 90, 52, 90, kind="pass", label="centro")
p.arrow(54, 84, 50, 97, kind="drive", label="remate")
p.save(out("rueda-25.svg"))

# ============================ FAMILIA 6 · OPOSICIÓN / TRANSFERENCIA ============================

# 26 Semioposición (defensor pasivo)
p = DrillPitch("Rueda 26 — Semioposición", "defensor pasivo que orienta el pase (no roba)")
frame(p)
st(p, 50, 20, "A"); st(p, 82, 74, "B"); st(p, 18, 74, "C"); st(p, 50, 52, "X", team="rival")
p.ball(56, 20)
p.arrow(50, 20, 82, 74, kind="pass", label="1"); p.arrow(82, 74, 18, 74, kind="pass", label="2")
p.note(50, 90, "X cierra líneas · juega siempre al apoyo libre", c="#fff5cc", size=11)
p.save(out("rueda-26.svg"))

# 27 Decisión (dos salidas)
p = DrillPitch("Rueda 27 — Decisión (dos salidas)", "leer al defensor y pasar al receptor libre")
frame(p)
st(p, 50, 20, "A"); st(p, 24, 66, "B"); st(p, 76, 66, "C"); st(p, 38, 50, "X", team="rival")
p.ball(56, 20)
p.arrow(50, 20, 76, 66, kind="pass", label="al libre"); p.arrow(76, 66, 70, 50, kind="drive", label="conduce")
p.note(50, 90, "X tapa a uno (aquí B) · A pasa al otro", c="#fff5cc", size=11)
p.save(out("rueda-27.svg"))

# 28 Pase-pared contra defensor real
p = DrillPitch("Rueda 28 — Pared contra defensor", "give-and-go superando a un rival activo")
frame(p)
st(p, 30, 22, "A"); st(p, 58, 40, "B", team="neutral"); st(p, 46, 56, "X", team="rival")
p.ball(36, 22)
p.arrow(30, 22, 58, 40, kind="pass", label="1"); p.arrow(34, 26, 48, 64, kind="run", label="supera a X")
p.arrow(58, 40, 50, 64, kind="pass", label="2"); p.arrow(50, 64, 52, 86, kind="drive", label="3")
p.save(out("rueda-28.svg"))

# 29 Rueda condicionada
p = DrillPitch("Rueda 29 — Rueda condicionada", "rombo 18 m · máx. 2 toques · salir al lado contrario de X")
frame(p)
st(p, 50, 16, "A"); st(p, 84, 52, "B"); st(p, 50, 86, "C"); st(p, 16, 52, "D"); st(p, 62, 56, "X", team="rival")
p.ball(56, 16)
p.arrow(50, 16, 16, 52, kind="pass", label="1"); p.arrow(16, 52, 50, 86, kind="pass", label="2")
p.arrow(50, 86, 84, 52, kind="pass", label="3")
p.save(out("rueda-29.svg"))

# 30 Transición rueda → 3v2 a portería (media pista)
p = att("Rueda 30 — Transición a 3v2", "combinar la rueda y romper a portería en superioridad")
p.player(30, 56, "A"); p.player(50, 52, "B"); p.player(70, 56, "C")
p.player(42, 76, "X", team="rival"); p.player(60, 76, "Y", team="rival")
p.ball(34, 56)
p.arrow(30, 56, 50, 52, kind="pass", label="1"); p.arrow(50, 52, 70, 56, kind="pass", label="2")
p.arrow(70, 56, 56, 92, kind="drive", label="3 rompen")
p.note(50, 64, "3-4 pases de la rueda → a la señal, 3v2", c="#fff5cc", size=11)
p.save(out("rueda-30.svg"))

print("ruedas OK")
