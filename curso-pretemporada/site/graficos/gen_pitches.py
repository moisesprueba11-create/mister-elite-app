#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las pizarras (sesiones tipo del banco) del curso de pretemporada."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from pitch import Pitch

def P(name, **kw): return Pitch(**kw), os.path.join(HERE, name)

# --- Sesión 0 · Tests de campo (sin GPS) ---
p = Pitch("Sesión 0 — Tests de campo (sin GPS)", subtitle="mide el día 1 y repite al final · misma hora y condiciones",
          attack_arrow=False)
for y in (24, 58):
    p.cone(22, y); p.cone(50, y); p.cone(78, y)
p.note(22, 66, "20 m ida-vuelta", size=11); p.note(22, 18, "Yo-Yo IR1", c="#7ee0ff", size=11)
p.note(50, 66, "40 m progresivo", size=11); p.note(50, 18, "30-15 IFT", c="#7ee0ff", size=11)
p.note(78, 66, "30 m crono", size=11); p.note(78, 18, "Sprint 10/30 m", c="#7ee0ff", size=11)
p.note(50, 86, "+ CMJ (salto) y wellness de partida", c="#fff5cc", size=12)
p.save(os.path.join(HERE, "ses-test.svg"))

# --- Sesión A · Base aeróbica: juego de posición a gran formato ---
p = Pitch("Sesión A — Base aeróbica: posición a gran formato",
          subtitle="9v9 en campo grande · 4×6 min, pausa 2 min · FC 80-88 % · volumen", attack_arrow=False)
p.zone(10, 18, 90, 82, "mantener y progresar de área a área", fill_op=0.10)
own = [(25, 30), (50, 26), (75, 30), (20, 50), (50, 48), (80, 50), (35, 66), (65, 66)]
riv = [(40, 38), (60, 38), (30, 55), (70, 55), (50, 60), (45, 72), (55, 72)]
for i, (x, y) in enumerate(own): p.player(x, y, "", team="own")
for x, y in riv: p.player(x, y, "", team="rival")
p.ball(50, 26)
p.arrow(50, 26, 80, 50, kind="pass"); p.arrow(80, 50, 65, 66, kind="pass")
p.save(os.path.join(HERE, "ses-aerobico.svg"))

# --- Sesión B · HIIT con balón: 4v4 intermitente ---
p = Pitch("Sesión B — HIIT con balón: 4v4 intermitente",
          subtitle="espacio reducido · 4×4 min (W:R 1:1) · RPE 8 · FC ≥ 90 %", half="att", attack_arrow=False)
p.zone(22, 56, 78, 96, "30×30 m · 2 mini-porterías por lado", fill_op=0.12)
p.goalmini(35, 96); p.goalmini(65, 96); p.goalmini(35, 56); p.goalmini(65, 56)
for x, y in [(34, 66), (52, 62), (44, 78), (60, 84)]: p.player(x, y, "", team="own")
for x, y in [(46, 68), (60, 70), (38, 84), (56, 90)]: p.player(x, y, "", team="rival")
p.ball(52, 62)
p.arrow(52, 62, 44, 78, kind="pass"); p.arrow(44, 78, 35, 96, kind="run")
p.save(os.path.join(HERE, "ses-hiit-balon.svg"))

# --- Sesión C · RSA: juego de transiciones ---
p = Pitch("Sesión C — RSA: juego de transiciones",
          subtitle="6-8 sprints de 4-6 s · pausa 20-30 s · 2-3 series · alta velocidad repetida")
p.goalmini(50, 96); p.goalmini(50, 6)
for x, y in [(40, 40), (60, 42), (50, 55)]: p.player(x, y, "", team="own")
for x, y in [(42, 60), (58, 62)]: p.player(x, y, "", team="rival")
p.ball(50, 55)
p.arrow(50, 55, 50, 86, kind="run", label="sprint"); p.arrow(60, 42, 60, 14, kind="run", label="repliegue")
p.note(50, 26, "ataque-defensa ida y vuelta sin pausa", c="#fff5cc", size=11)
p.save(os.path.join(HERE, "ses-rsa.svg"))

# --- Sesión D · Velocidad y aceleraciones ---
p = Pitch("Sesión D — Velocidad y aceleraciones (fresco)",
          subtitle="sprints máximos 20-30 m · pausa completa 2-4 min · SIEMPRE al inicio de la sesión", attack_arrow=False)
p.cone(35, 35); p.cone(35, 70); p.cone(65, 35); p.cone(65, 70)
p.player(35, 30, "", team="own"); p.ball(50, 52)
p.arrow(35, 33, 35, 68, kind="run", label="sprint máx."); p.arrow(60, 50, 38, 64, kind="pass", label="recibe en carrera")
p.player(62, 48, "", team="own2")
p.note(50, 84, "calidad sobre cantidad · si baja la velocidad, se para", c="#fff5cc", size=11)
p.save(os.path.join(HERE, "ses-velocidad.svg"))

# --- Sesión E · Fuerza y prevención (circuito) ---
p = Pitch("Sesión E — Fuerza y prevención (circuito)",
          subtitle="10-15 min · 2-3×/sem · en el calentamiento o al inicio · −51 % lesiones isquios", attack_arrow=False)
p.zone(14, 56, 46, 86, "1 · Nordic hamstring", c="#7ee0ff", fill_op=0.12)
p.zone(54, 56, 86, 86, "2 · Copenhagen (aductor)", c="#7ee0ff", fill_op=0.12)
p.zone(14, 18, 46, 48, "3 · Isométricos / sentadilla", c="#7ee0ff", fill_op=0.12)
p.zone(54, 18, 86, 48, "4 · Core + tobillo (equilibrio)", c="#7ee0ff", fill_op=0.12)
p.note(50, 92, "progresar volumen poco a poco · bajo coste de fatiga", c="#fff5cc", size=11)
p.save(os.path.join(HERE, "ses-prevencion.svg"))

# --- Sesión F · Rondo de alta densidad ---
p = Pitch("Sesión F — Rondo de alta densidad",
          subtitle="5v2 · espacio mínimo · pausa corta · capacidad con muchísimos contactos", half="att", attack_arrow=False)
import math
cx, cy, r = 50, 76, 17
for i in range(5):
    a = math.radians(90 + i * 72)
    p.player(cx + r * math.cos(a), cy + r * math.sin(a) * 0.8, "", team="own")
p.player(46, 74, "", team="rival"); p.player(54, 78, "", team="rival")
p.ball(cx + r, cy)
p.arrow(67, 76, 50, 93, kind="pass"); p.arrow(50, 93, 33, 76, kind="pass")
p.note(50, 56, "rotación rápida · 2 toques · series de 1-2 min", c="#fff5cc", size=11)
p.save(os.path.join(HERE, "ses-rondo-densidad.svg"))

# --- Sesión G · Juego de posición condicional ---
p = Pitch("Sesión G — Juego de posición condicional",
          subtitle="4v4+3 comodines · regla: progresar de zona · el físico va DENTRO del balón", attack_arrow=False)
p.zone(12, 20, 88, 80, "", fill_op=0.06)
p.note(50, 50, "—  línea de progresión  —", c="#cfe0ee", size=10)
for x, y in [(30, 34), (58, 30), (40, 64), (66, 60)]: p.player(x, y, "", team="own")
for x, y in [(44, 40), (60, 44), (38, 56), (56, 58)]: p.player(x, y, "", team="rival")
for x, y in [(18, 50), (82, 50), (50, 70)]: p.player(x, y, "", team="neutral", role="comodín")
p.ball(58, 30)
p.arrow(58, 30, 82, 50, kind="pass"); p.arrow(82, 50, 66, 60, kind="pass", label="progresa")
p.save(os.path.join(HERE, "ses-juego-posicion.svg"))

# --- Sesión H · Fase de juego: salida de balón ---
p = Pitch("Sesión H — Fase de juego: salida de balón",
          subtitle="11v8 dirigido · superar la 1.ª presión y progresar con criterio", half="def")
p.player(50, 8, "POR", team="own", role="portero")
for x, y in [(28, 18), (44, 16), (56, 16), (72, 18)]: p.player(x, y, "", team="own")
p.player(50, 30, "", team="own", role="pivote")
for x, y in [(36, 40), (64, 40)]: p.player(x, y, "", team="own")
for x, y in [(42, 34), (58, 34), (50, 44)]: p.player(x, y, "", team="rival")
p.ball(44, 16)
p.arrow(44, 16, 50, 30, kind="pass"); p.arrow(50, 30, 64, 40, kind="pass", label="3.er hombre")
p.save(os.path.join(HERE, "ses-fase-salida.svg"))

# --- Sesión I · Presión tras pérdida (contrapresión) ---
p = Pitch("Sesión I — Presión tras pérdida (contrapresión)",
          subtitle="recuperar en ≤ 5 s · salta el más cercano, los demás tapan líneas", attack_arrow=False)
p.zone(30, 44, 70, 74, "reacción ≤ 5 s", c="#ff5252", fill_op=0.12)
p.player(50, 58, "", team="rival", role="acaba de robar")
for x, y in [(44, 66), (58, 64), (50, 48)]: p.player(x, y, "", team="own")
for x, y in [(34, 74), (66, 74)]: p.player(x, y, "", team="rival")
p.ball(50, 58)
p.arrow(46, 50, 50, 56, kind="block"); p.arrow(46, 64, 50, 58, kind="block"); p.arrow(56, 62, 52, 58, kind="block")
p.save(os.path.join(HERE, "ses-presion.svg"))

# --- Sesión J · Posesión para finalizar ---
p = Pitch("Sesión J — Posesión para finalizar",
          subtitle="ataque sobre defensa + remate · llegar con criterio y rematar", half="att")
for x, y in [(30, 60), (50, 56), (70, 60), (40, 74), (60, 74)]: p.player(x, y, "", team="own")
for x, y in [(42, 66), (58, 66), (50, 80), (35, 86), (65, 86)]: p.player(x, y, "", team="rival")
p.player(50, 95, "POR", team="rival", role="portero")
p.ball(30, 60)
p.arrow(30, 60, 50, 56, kind="pass"); p.arrow(50, 56, 60, 74, kind="pass")
p.arrow(60, 74, 52, 90, kind="drive", label="remate")
p.save(os.path.join(HERE, "ses-finalizacion.svg"))

# --- Sesión K · Partido dirigido a gran formato ---
p = Pitch("Sesión K — Partido dirigido a gran formato",
          subtitle="8v8 en campo grande · pausas para corregir · ritmo de competición")
own = [(50, 12), (30, 26), (50, 28), (70, 26), (35, 44), (65, 44), (50, 50), (50, 64)]
riv = [(50, 88), (32, 74), (50, 72), (68, 74), (40, 58), (60, 58), (50, 54), (45, 40)]
for x, y in own: p.player(x, y, "", team="own")
for x, y in riv: p.player(x, y, "", team="rival")
p.ball(50, 50)
p.arrow(50, 50, 65, 44, kind="pass"); p.arrow(65, 44, 70, 26, kind="pass")
p.save(os.path.join(HERE, "ses-partido-grande.svg"))

print("pitches OK")
