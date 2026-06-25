#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
drill.py — Lienzo de pizarra para TAREAS de espacio reducido (rondos / juegos de
posición / superioridades) del curso "Juego de posición" (MISTER ÉLITE).

Reutiliza todo el motor de `pitch.Pitch` (jugadores, flechas, zonas, conos,
leyenda, marca, render SVG) pero sustituye el campo reglamentario (áreas, círculo
central, punto de penalti) por un LIENZO LIMPIO de césped, sobre el que cada tarea
dibuja su propio cuadrado/rectángulo de juego con conos y zonas. Así las pizarras
de rondo no quedan sucias con marcas de un campo 11v11.

Uso:
    from drill import DrillPitch
    p = DrillPitch(title="Tarea 1 — ...", subtitle="5v2 · 9×9 m")
    p.field(18, 12, 82, 88)          # cuadrado/rect. de juego (en coords 0..100)
    p.player(...); p.arrow(...); p.save("graficos/tarea-01.svg")
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pitch import Pitch, PALETTE


class DrillPitch(Pitch):
    def __init__(self, title="", subtitle="", width=680, ratio=1.0):
        # ratio = alto/ancho del área jugable (1.0 = cuadrado).
        self._ratio = ratio
        super().__init__(title=title, subtitle=subtitle, width=width,
                         half=None, brand=True, attack_arrow=False)

    # --- redibuja el lienzo sin marcas de campo reglamentario ---
    def _draw_pitch(self):
        play_w = self.W - 2 * self.M
        play_h = play_w * self._ratio
        self.play_w, self.play_h = play_w, play_h
        self.H = play_h + 2 * self.M + self.title_h + self.foot_h
        self.x0 = self.M
        self.y0 = self.M + self.title_h
        gx0, gy0, gw, gh = self.x0, self.y0, self.play_w, self.play_h
        # fondo
        self._rect(0, 0, self.W, self.H, fill=PALETTE["dark"])
        # césped con franjas suaves
        stripes = 10
        for i in range(stripes):
            sh = gh / stripes
            col = "#2f8a3e" if i % 2 == 0 else "#2a7d36"
            self._rect(gx0, gy0 + i * sh, gw, sh + 0.5, fill=col)
        # borde exterior del lienzo
        self._rect(gx0, gy0, gw, gh, fill="none", stroke="#1f5f2a", stroke_width=2)
        # título / marca
        if self.title:
            self._rect(0, 0, self.W, self.title_h, fill=PALETTE["dark"])
            self._text(self.W/2, 24, self.title, size=17, c="#ffffff", w=800)
            if self.subtitle:
                self._text(self.W/2, 40, self.subtitle, size=11, c="#9fb3c8", w=500)
        if self.brand:
            self._rect(0, self.H - self.foot_h, self.W, self.foot_h, fill=PALETTE["dark"])
            self._text(self.W - 12, self.H - 8, "MISTER ÉLITE · Moisés Díaz",
                       size=10, c="#8aa0b6", w=700, anchor="end")
            self._text(12, self.H - 8, "Balón parado defensivo · MISTER ÉLITE",
                       size=10, c="#7f93a8", w=600, anchor="start")

    # --- rectángulo de juego de la tarea (con conos en las 4 esquinas) ---
    def field(self, x1, y1, x2, y2, corners=True, stroke="#ffffff", w=2.6, dash=None):
        X1, Y1, X2, Y2 = self.X(x1), self.Y(y2), self.X(x2), self.Y(y1)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(f'<rect x="{X1:.1f}" y="{Y1:.1f}" width="{abs(X2-X1):.1f}" '
                         f'height="{abs(Y2-Y1):.1f}" rx="3" fill="none" stroke="{stroke}" '
                         f'stroke-width="{w}"{d}/>')
        if corners:
            for cx, cy in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                self.cone(cx, cy)

    # --- línea interior (separa zonas/carriles) ---
    def divline(self, x1, y1, x2, y2, c="#dfe7ef", w=2.0, dash="5 6"):
        self._line(self.X(x1), self.Y(y1), self.X(x2), self.Y(y2), w=w, c=c, dash=dash)

    # --- puerta de conos (mini-puerta) horizontal u vertical ---
    def gate(self, x1, y1, x2, y2):
        self.cone(x1, y1)
        self.cone(x2, y2)
