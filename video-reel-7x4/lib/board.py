#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
board.py — Motor de pizarra animada estilo "tactical board" para reels verticales
(1080x1920) de MISTER ÉLITE — Moisés Díaz.

Estética: césped rayado, porterías blancas, zonas en amarillo, jugadores como
discos rojos (equipo con balón) y azules (defensores), balón blanco.
Dibuja con PIL en supersampling x2 para que los bordes salgan limpios.

Coordenadas: píxeles del lienzo final (1080x1920). El motor multiplica por SS.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1080, 1920
SS = 2                       # supersampling
FPS = 30

# ---------------------------------------------------------------- paleta
GRASS_A = (58, 142, 63)
GRASS_B = (46, 122, 51)
GRASS_DARK = (20, 58, 28)
WHITE = (255, 255, 255)
YELLOW = (255, 200, 40)
YELLOW_D = (214, 160, 16)
RED = (166, 30, 40)
RED_E = (255, 255, 255)
BLUE = (28, 101, 176)
BLUE_E = (255, 255, 255)
PANEL = (10, 24, 38)
TEXT = (255, 255, 255)
MUTED = (170, 190, 206)
ALERT = (214, 45, 45)

FONT_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
_fonts = {}


def font(size, bold=True):
    key = (size, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONT_B if bold else FONT_R, int(size * SS))
    return _fonts[key]


# ---------------------------------------------------------------- utilidades
def clamp01(t):
    return max(0.0, min(1.0, t))


def ss_ease(t):
    """smoothstep"""
    t = clamp01(t)
    return t * t * (3 - 2 * t)


def ease_out(t):
    t = clamp01(t)
    return 1 - (1 - t) ** 3


def lerp(a, b, t):
    return a + (b - a) * t


def lerp_p(p, q, t):
    return (lerp(p[0], q[0], t), lerp(p[1], q[1], t))


def seg(t, t0, t1):
    """progreso 0..1 dentro de la ventana [t0,t1]"""
    if t1 <= t0:
        return 1.0 if t >= t1 else 0.0
    return clamp01((t - t0) / (t1 - t0))


def S(v):
    return int(round(v * SS))


class Board:
    """Un frame de pizarra. Todas las medidas en coordenadas 1080x1920."""

    def __init__(self, bg=None):
        self.im = bg.copy() if bg is not None else Image.new("RGB", (W * SS, H * SS), GRASS_B)
        self.d = ImageDraw.Draw(self.im, "RGBA")

    # ---- geometría base -------------------------------------------------
    @staticmethod
    def grass():
        """Fondo de césped rayado + porterías + viñeteado. Se calcula una vez."""
        im = Image.new("RGB", (W * SS, H * SS), GRASS_B)
        d = ImageDraw.Draw(im)
        stripe = 135
        for i in range(0, W // stripe + 1):
            if i % 2 == 0:
                d.rectangle([S(i * stripe), 0, S((i + 1) * stripe), H * SS], fill=GRASS_A)
        b = Board.__new__(Board)
        b.im, b.d = im, ImageDraw.Draw(im, "RGBA")
        # líneas de campo tenues (fondo + banda)
        b.d.rectangle([S(60), S(440), S(W - 60), S(1760)], outline=(255, 255, 255, 55), width=S(4))
        b.d.line([S(60), S(1100), S(W - 60), S(1100)], fill=(255, 255, 255, 40), width=S(3))
        b.goal(540, 440, top=True)
        b.goal(540, 1760, top=False)
        return im

    def goal(self, cx, y, top=True):
        """Portería vista cenital, estilo del tablero de referencia."""
        gw, gh = 360, 54
        x0, x1 = cx - gw / 2, cx + gw / 2
        y0, y1 = (y - gh, y) if top else (y, y + gh)
        self.d.rectangle([S(x0 - 10), S(y0 - 6), S(x1 + 10), S(y1 + 6)],
                         fill=(255, 255, 255, 60))
        self.d.rectangle([S(x0), S(y0), S(x1), S(y1)], fill=(235, 248, 236, 225),
                         outline=WHITE, width=S(7))
        for i in range(1, 9):                       # malla de la red
            x = lerp(x0, x1, i / 9.0)
            self.d.line([S(x), S(y0 + 6), S(x), S(y1 - 6)], fill=(255, 255, 255, 200), width=S(2))
        self.d.line([S(x0 + 6), S((y0 + y1) / 2), S(x1 - 6), S((y0 + y1) / 2)],
                    fill=(255, 255, 255, 200), width=S(2))

    # ---- primitivas -----------------------------------------------------
    def rect(self, x0, y0, x1, y1, fill=None, outline=None, w=4, radius=0):
        box = [S(x0), S(y0), S(x1), S(y1)]
        if radius:
            self.d.rounded_rectangle(box, radius=S(radius), fill=fill, outline=outline,
                                     width=S(w) if outline else 0)
        else:
            self.d.rectangle(box, fill=fill, outline=outline, width=S(w) if outline else 0)

    def line(self, x0, y0, x1, y1, c=WHITE, w=4):
        self.d.line([S(x0), S(y0), S(x1), S(y1)], fill=c, width=S(w))

    def dashed(self, x0, y0, x1, y1, c=YELLOW, w=5, dash=26, gap=18):
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy)
        if L < 1:
            return
        ux, uy = dx / L, dy / L
        s = 0.0
        while s < L:
            e = min(s + dash, L)
            self.line(x0 + ux * s, y0 + uy * s, x0 + ux * e, y0 + uy * e, c=c, w=w)
            s = e + gap

    def disc(self, x, y, r, fill, edge=WHITE, ew=6, alpha=255, shadow=True):
        if alpha <= 0:
            return
        if shadow:
            self.d.ellipse([S(x - r + 3), S(y - r + 7), S(x + r + 3), S(y + r + 7)],
                           fill=(0, 0, 0, int(70 * alpha / 255)))
        f = (fill[0], fill[1], fill[2], alpha)
        e = (edge[0], edge[1], edge[2], alpha)
        self.d.ellipse([S(x - r), S(y - r), S(x + r), S(y + r)], fill=f, outline=e, width=S(ew))

    def ring(self, x, y, r, c=YELLOW, w=6, alpha=255):
        cc = (c[0], c[1], c[2], alpha)
        self.d.ellipse([S(x - r), S(y - r), S(x + r), S(y + r)], outline=cc, width=S(w))

    def arc_ring(self, x, y, r, frac, c=YELLOW, w=10, alpha=255):
        """Anillo que se vacía (cuenta atrás)."""
        cc = (c[0], c[1], c[2], alpha)
        end = -90 + 360 * clamp01(frac)
        self.d.arc([S(x - r), S(y - r), S(x + r), S(y + r)], start=-90, end=end,
                   fill=cc, width=S(w))

    def ball(self, x, y, r=20, alpha=255):
        self.d.ellipse([S(x - r - 2), S(y - r + 4), S(x + r + 2), S(y + r + 8)],
                       fill=(0, 0, 0, int(80 * alpha / 255)))
        self.d.ellipse([S(x - r), S(y - r), S(x + r), S(y + r)],
                       fill=(252, 252, 252, alpha), outline=(25, 25, 25, alpha), width=S(3))
        for a in (90, 210, 330):
            px = x + math.cos(math.radians(a)) * r * 0.5
            py = y + math.sin(math.radians(a)) * r * 0.5
            self.d.ellipse([S(px - r * 0.26), S(py - r * 0.26), S(px + r * 0.26), S(py + r * 0.26)],
                           fill=(30, 30, 30, alpha))
        self.d.ellipse([S(x - r * 0.26), S(y - r * 0.26), S(x + r * 0.26), S(y + r * 0.26)],
                       fill=(30, 30, 30, alpha))

    def arrow(self, x0, y0, x1, y1, c=YELLOW, w=7, head=28, dash=False, alpha=255):
        cc = (c[0], c[1], c[2], alpha)
        ang = math.atan2(y1 - y0, x1 - x0)
        bx, by = x1 - math.cos(ang) * head * 0.75, y1 - math.sin(ang) * head * 0.75
        if dash:
            self.dashed(x0, y0, bx, by, c=cc, w=w)
        else:
            self.line(x0, y0, bx, by, c=cc, w=w)
        p1 = (x1, y1)
        p2 = (x1 - math.cos(ang - 0.45) * head, y1 - math.sin(ang - 0.45) * head)
        p3 = (x1 - math.cos(ang + 0.45) * head, y1 - math.sin(ang + 0.45) * head)
        self.d.polygon([(S(p[0]), S(p[1])) for p in (p1, p2, p3)], fill=cc)

    # ---- texto ----------------------------------------------------------
    def text(self, x, y, s, size=44, c=TEXT, anchor="mm", bold=True, alpha=255, shadow=False):
        f = font(size, bold)
        cc = (c[0], c[1], c[2], alpha)
        if shadow:
            self.d.text((S(x) + S(2), S(y) + S(3)), s, font=f, fill=(0, 0, 0, int(alpha * 0.55)),
                        anchor=anchor)
        self.d.text((S(x), S(y)), s, font=f, fill=cc, anchor=anchor)

    def text_w(self, s, size=44, bold=True):
        f = font(size, bold)
        return self.d.textlength(s, font=f) / SS

    def chip(self, x, y, s, size=30, fg=(12, 26, 40), bg=YELLOW, pad=16, alpha=255, radius=14):
        w = self.text_w(s, size) + pad * 2
        h = size + pad * 0.9
        self.rect(x - w / 2, y - h / 2, x + w / 2, y + h / 2,
                  fill=(bg[0], bg[1], bg[2], alpha), radius=radius)
        self.text(x, y + 1, s, size=size, c=fg, alpha=alpha)

    # ---- bloques de marca ----------------------------------------------
    def header(self, title, subtitle, alpha=255):
        self.rect(0, 0, W, 196, fill=(PANEL[0], PANEL[1], PANEL[2], int(0.88 * alpha)))
        self.rect(0, 190, W, 196, fill=(YELLOW[0], YELLOW[1], YELLOW[2], alpha))
        self.text(W / 2, 76, title, size=62, c=WHITE, alpha=alpha)
        self.text(W / 2, 146, subtitle, size=31, c=YELLOW, alpha=alpha)

    def caption(self, text, sub="", accent=YELLOW, alpha=255, y0=214):
        h = 150 if not sub else 186
        self.rect(46, y0, W - 46, y0 + h, fill=(PANEL[0], PANEL[1], PANEL[2], int(0.92 * alpha)),
                  radius=22)
        self.rect(46, y0, 62, y0 + h, fill=(accent[0], accent[1], accent[2], alpha), radius=8)
        if sub:
            self.text(W / 2 + 8, y0 + 62, text, size=54, c=WHITE, alpha=alpha)
            self.text(W / 2 + 8, y0 + 130, sub, size=36, c=MUTED, alpha=alpha)
        else:
            self.text(W / 2 + 8, y0 + h / 2, text, size=54, c=WHITE, alpha=alpha)

    def footer(self, alpha=255):
        self.text(W / 2, 1876, "MISTER ÉLITE — Moisés Díaz  ·  del concepto al campo",
                  size=30, c=(226, 236, 245), alpha=alpha, shadow=True)

    def out(self):
        return self.im.resize((W, H), Image.LANCZOS)
