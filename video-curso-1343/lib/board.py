#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
board.py — Pizarra animada (render PIL) del espacio reducido por zonas
del sistema 1-3-4-3. Estética MISTER ÉLITE — Moisés Díaz.

Coordenadas de juego: x 0..100 (0 = fondo de ataque, pegado a STOP BALL),
y 0..100 (0 = carril superior). x<0 = dentro de la zona STOP BALL.
"""
import os
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/liberation"
F_BOLD = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")
F_REG = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
if not os.path.exists(F_BOLD):                      # respaldo
    F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    F_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

C = dict(
    bg="#0e1622", panel="#15202b", panel2="#1b2a3a",
    grass1=(58, 132, 62), grass2=(53, 122, 57),
    line=(255, 255, 255), border=(19, 44, 72),
    own=(26, 76, 158), own_edge=(9, 33, 74), own_ring=(226, 238, 255),
    rival=(206, 40, 40), rival_edge=(112, 12, 12), rival_ring=(255, 226, 226),
    cone=(236, 92, 36), stop=(34, 197, 94), stop2=(22, 150, 72),
    pass_c=(255, 213, 74), red_pass=(255, 120, 120), carry=(126, 224, 255),
    goalw=(238, 242, 246), text=(255, 255, 255), dim=(150, 172, 194),
    gold=(255, 200, 60),
)


def _f(path, size):
    return ImageFont.truetype(path, size)


class Board:
    """Lienzo cuadrado con cabecera de marca, pizarra y pie de texto."""

    def __init__(self, W=1080, H=1080, scale=2, ratio=817.0 / 608.0,
                 zone_x=(), lane_y=(), stop=None, mini_goals=()):
        self.W, self.H, self.S = W, H, scale
        self.ratio = ratio
        self.zone_x, self.lane_y = list(zone_x), list(lane_y)
        self.stop = stop or {}
        self.mini_goals = list(mini_goals)

        S = self.S
        self.head_h = 104 * S
        self.foot_h = 56 * S
        self.cap_h = 168 * S
        self.strip_h = 34 * S
        margin = 26 * S
        avail_w = W * S - 2 * margin
        # ancho total dibujado = zona stop (12%) + campo + fondo minipoterías
        board_top = self.head_h + self.strip_h
        board_zone_h = H * S - self.cap_h - self.foot_h - board_top - 10 * S
        self.PW = min(avail_w / (1.0 + abs(self.stop.get("x0", -12)) / 100.0 + 0.030),
                      board_zone_h * self.ratio)
        self.PH = self.PW / self.ratio
        self.PX = margin + abs(self.stop.get("x0", -12)) / 100.0 * self.PW
        self.PY = board_top + max(0, (board_zone_h - self.PH) / 2)
        self.bg = None

    # ---------------------------------------------------------- transformes --
    def X(self, x):
        return self.PX + x / 100.0 * self.PW

    def Y(self, y):
        return self.PY + y / 100.0 * self.PH

    def L(self, v):          # longitud relativa al largo del campo
        return v / 100.0 * self.PW

    # ------------------------------------------------------------- utilidad --
    @staticmethod
    def _dashed(d, p0, p1, fill, width, dash, gap):
        x0, y0 = p0
        x1, y1 = p1
        dx, dy = x1 - x0, y1 - y0
        ln = (dx * dx + dy * dy) ** 0.5
        if ln <= 0:
            return
        ux, uy = dx / ln, dy / ln
        t = 0.0
        while t < ln:
            t2 = min(t + dash, ln)
            d.line([(x0 + ux * t, y0 + uy * t), (x0 + ux * t2, y0 + uy * t2)],
                   fill=fill, width=width)
            t = t2 + gap

    def _dot(self, d, x, y, r, fill, outline=None, w=0):
        d.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=outline, width=w)

    # ------------------------------------------------------------ fondo fijo --
    def build_bg(self, titulo, subtitulo):
        S = self.S
        im = Image.new("RGB", (self.W * S, self.H * S), C["bg"])
        d = ImageDraw.Draw(im)

        # ---- cabecera de marca
        d.rectangle([0, 0, self.W * S, self.head_h], fill=C["panel"])
        d.rectangle([0, self.head_h - 4 * S, self.W * S, self.head_h], fill=C["gold"])
        f1, f2 = _f(F_BOLD, int(37 * S)), _f(F_BOLD, int(19 * S))
        d.text((32 * S, 22 * S), titulo, font=f1, fill=C["text"])
        d.text((32 * S, 66 * S), subtitulo, font=f2, fill=C["gold"])
        fb = _f(F_BOLD, int(17 * S))
        d.text((self.W * S - 32 * S, 30 * S), "MISTER ÉLITE", font=fb,
               fill=C["text"], anchor="ra")
        d.text((self.W * S - 32 * S, 56 * S), "Moisés Díaz", font=_f(F_REG, int(16 * S)),
               fill=C["dim"], anchor="ra")

        # ---- césped con franjas verticales
        px, py, pw, ph = self.PX, self.PY, self.PW, self.PH
        stripes = 10
        for i in range(stripes):
            x0 = px + i * pw / stripes
            d.rectangle([x0, py, x0 + pw / stripes + 1, py + ph],
                        fill=C["grass1"] if i % 2 == 0 else C["grass2"])

        # ---- zona STOP BALL (banda exterior rayada)
        if self.stop:
            sx0, sx1 = self.X(self.stop["x0"]), self.X(self.stop["x1"])
            sy0, sy1 = self.Y(self.stop["y0"]), self.Y(self.stop["y1"])
            bw, bh = int(sx1 - sx0), int(sy1 - sy0)
            band = Image.new("RGB", (bw, bh), (36, 150, 74))
            bd = ImageDraw.Draw(band)
            step = 20 * S
            x = -bh
            while x < bw + bh:
                bd.line([(x, bh), (x + bh, 0)], fill=C["stop"], width=int(7 * S))
                x += step
            im.paste(band, (int(sx0), int(sy0)))
            d.rectangle([sx0, sy0, sx1, sy1], outline=(210, 255, 220), width=int(2.4 * S))
            # rótulo vertical STOP BALL
            ft = _f(F_BOLD, int(30 * S))
            tw = int(d.textlength("STOP BALL", font=ft))
            tag = Image.new("RGBA", (tw + 8 * S, int(40 * S)), (0, 0, 0, 0))
            ImageDraw.Draw(tag).text((4 * S, 2 * S), "STOP BALL", font=ft, fill=(255, 255, 255, 255))
            tag = tag.rotate(90, expand=True)
            im.paste(tag, (int((sx0 + sx1) / 2 - tag.width / 2),
                           int((sy0 + sy1) / 2 - tag.height / 2)), tag)

        # ---- minipoterías en el fondo propio
        gd = self.L(3.0)
        for cy, hh in self.mini_goals:
            y0, y1 = self.Y(cy - hh / 2), self.Y(cy + hh / 2)
            x0 = self.X(100)
            d.rectangle([x0, y0, x0 + gd, y1], fill=(150, 168, 150),
                        outline=C["goalw"], width=int(2.4 * S))
            for k in range(1, 7):                       # red
                yy = y0 + (y1 - y0) * k / 7.0
                d.line([(x0, yy), (x0 + gd, yy)], fill=(232, 240, 232), width=int(1.2 * S))
            for k in range(1, 3):
                xx = x0 + gd * k / 3.0
                d.line([(xx, y0), (xx, y1)], fill=(232, 240, 232), width=int(1.2 * S))

        # ---- líneas discontinuas de zonas y carriles
        lw = int(2.6 * S)
        for zx in self.zone_x:
            self._dashed(d, (self.X(zx), self.Y(0)), (self.X(zx), self.Y(100)),
                         C["line"], lw, 14 * S, 11 * S)
        for ly in self.lane_y:
            self._dashed(d, (self.X(0), self.Y(ly)), (self.X(100), self.Y(ly)),
                         (16, 34, 58), int(3.0 * S), 16 * S, 12 * S)

        # ---- contorno del rectángulo
        d.rectangle([px, py, px + pw, py + ph], outline=C["border"], width=int(4.5 * S))

        # ---- conos: cruces de líneas y esquinas
        for zx in [0] + self.zone_x + [100]:
            for ly in self.lane_y:
                self._dot(d, self.X(zx), self.Y(ly), 5.4 * S, (214, 40, 40))
        for cx in (0, 100):
            for cy in (0, 100):
                self._dot(d, self.X(cx), self.Y(cy), 8.0 * S, C["cone"])

        # ---- franja superior con el nombre de cada zona
        fz = _f(F_BOLD, int(15 * S))
        edges = [0] + self.zone_x + [100]
        zy = self.PY - self.strip_h + 6 * S
        for i in range(len(edges) - 1):
            cxz = self.X((edges[i] + edges[i + 1]) / 2.0)
            d.text((cxz, zy + 9 * S), f"ZONA {5 - i}", font=fz, fill=C["dim"], anchor="ma")
        d.text((self.X(self.stop["x0"] / 2.0), zy + 9 * S), "◄", font=fz,
               fill=C["stop"], anchor="ma")

        # ---- pie de marca
        d.rectangle([0, self.H * S - self.foot_h, self.W * S, self.H * S], fill=C["panel"])
        d.text((32 * S, self.H * S - self.foot_h / 2), "MISTER ÉLITE — Moisés Díaz",
               font=_f(F_BOLD, int(19 * S)), fill=C["text"], anchor="lm")
        d.text((self.W * S - 32 * S, self.H * S - self.foot_h / 2),
               "◄ ATAQUE AZUL (STOP BALL)   ·   CONTRA ROJA A LAS MINIPOTERÍAS ►",
               font=_f(F_REG, int(16 * S)), fill=C["dim"], anchor="rm")
        self.bg = im
        return im

    # -------------------------------------------------------------- jugador --
    def player(self, d, x, y, label, team="own", r=None, ball=False, dim=1.0):
        S = self.S
        r = r or 19 * S
        cx, cy = self.X(x), self.Y(y)
        fill = C["own"] if team == "own" else C["rival"]
        edge = C["own_edge"] if team == "own" else C["rival_edge"]
        ring = C["own_ring"] if team == "own" else C["rival_ring"]
        if dim < 1.0:
            fill = tuple(int(c * dim + 30 * (1 - dim)) for c in fill)
        if ball:
            self._dot(d, cx, cy, r + 7 * S, None, C["gold"], int(3.4 * S))
        self._dot(d, cx, cy, r, fill, edge, int(2.6 * S))
        self._dot(d, cx, cy, r, None, ring, int(1.6 * S))
        f = _f(F_BOLD, int((16 if len(label) < 2 else 14.5) * S))
        d.text((cx, cy + 0.5 * S), label, font=f, fill=C["text"], anchor="mm")

    def ball(self, d, x, y, r=None):
        S = self.S
        r = r or 10.5 * S
        cx, cy = self.X(x), self.Y(y)
        self._dot(d, cx, cy, r + 2.2 * S, (20, 20, 20), None)
        self._dot(d, cx, cy, r, (252, 252, 252), (24, 24, 24), int(1.6 * S))
        self._dot(d, cx, cy, r * 0.40, (22, 22, 22))
        for a in (0, 72, 144, 216, 288):
            import math
            ang = math.radians(a - 90)
            self._dot(d, cx + math.cos(ang) * r * 0.72, cy + math.sin(ang) * r * 0.72,
                      r * 0.20, (22, 22, 22))

    # --------------------------------------------------------------- flechas --
    def arrow(self, d, p0, p1, color, w, dash=None, head=True):
        import math
        x0, y0 = self.X(p0[0]), self.Y(p0[1])
        x1, y1 = self.X(p1[0]), self.Y(p1[1])
        if dash:
            self._dashed(d, (x0, y0), (x1, y1), color, w, dash[0], dash[1])
        else:
            d.line([(x0, y0), (x1, y1)], fill=color, width=w)
        if head:
            ang = math.atan2(y1 - y0, x1 - x0)
            hl, hw = 17 * self.S, 9 * self.S
            d.polygon([(x1, y1),
                       (x1 - hl * math.cos(ang) + hw * math.sin(ang),
                        y1 - hl * math.sin(ang) - hw * math.cos(ang)),
                       (x1 - hl * math.cos(ang) - hw * math.sin(ang),
                        y1 - hl * math.sin(ang) + hw * math.cos(ang))], fill=color)

    # ----------------------------------------------------------------- texto --
    def caption(self, d, chip, titulo, texto, extra=None):
        S = self.S
        y0 = self.H * S - self.foot_h - self.cap_h + 10 * S
        d.rounded_rectangle([26 * S, y0, self.W * S - 26 * S,
                             self.H * S - self.foot_h - 12 * S],
                            radius=14 * S, fill=C["panel2"])
        if chip:
            fc = _f(F_BOLD, int(17 * S))
            wch = int(d.textlength(chip, font=fc)) + 28 * S
            d.rounded_rectangle([46 * S, y0 + 18 * S, 46 * S + wch, y0 + 52 * S],
                                radius=17 * S, fill=C["gold"])
            d.text((46 * S + wch / 2, y0 + 35 * S), chip, font=fc,
                   fill=(20, 26, 36), anchor="mm")
            tx = 46 * S + wch + 18 * S
        else:
            tx = 46 * S
        d.text((tx, y0 + 35 * S), titulo, font=_f(F_BOLD, int(19 * S)),
               fill=C["text"], anchor="lm")
        f = _f(F_BOLD, int(23 * S))
        lines = _wrap(d, texto, f, self.W * S - 100 * S)
        for i, ln in enumerate(lines[:2]):
            d.text((46 * S, y0 + 60 * S + i * 30 * S), ln, font=f, fill=C["text"])
        if extra:
            d.text((46 * S, y0 + 122 * S), extra, font=_f(F_REG, int(16 * S)),
                   fill=C["dim"])

    def finish(self, im):
        return im.resize((self.W, self.H), Image.LANCZOS)


def _wrap(d, txt, font, maxw):
    out, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out
