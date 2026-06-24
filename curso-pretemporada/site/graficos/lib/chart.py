#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chart.py — Motor de infografías de planificación para el curso de PRETEMPORADA (MISTER ÉLITE).
Genera SVG limpios y consistentes con la estética del curso (fondo oscuro, oro #f7c948).
Tipos:
  Calendar  -> microciclo: columnas-día con sesiones y curva de carga semanal
  Curve     -> curva suave (supercompensación, ramp-up, ondulación, ACWR) con bandas
  Bars      -> barras (sRPE por tipo de sesión, volumen/intensidad por fase)
  Timeline  -> mapa de fases de la pretemporada (Gantt por semanas)
Todos exponen .save(path) y .svg().
Paleta de carga: alta=rojo, media=ámbar, baja=verde, reposo=gris, partido=azul.
"""
import math

PAL = dict(
    bg0="#0f2438", bg1="#0c1b2a", panel="#13283d", panelb="#24435f",
    ink="#eaf1f8", mut="#9fb3c8", gold="#f7c948", blue="#1d6fb8",
    alta="#e8453c", media="#f5a623", baja="#3fa34d", reposo="#5a6b7b",
    partido="#1d6fb8", grid="#23415c",
)
LOADc = {"alta": PAL["alta"], "media": PAL["media"], "baja": PAL["baja"],
         "reposo": PAL["reposo"], "partido": PAL["partido"], "amistoso": PAL["partido"]}
LOADv = {"reposo": 0.45, "baja": 1.6, "media": 3.0, "alta": 4.5, "partido": 4.2, "amistoso": 4.2}


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _wrap(s, n):
    """parte un texto en líneas de <= n caracteres por palabras; corta palabras muy largas."""
    words = []
    for w in str(s).split():
        while len(w) > n:                 # corta palabras que no caben
            words.append(w[:n - 1] + "-")
            w = w[n - 1:]
        words.append(w)
    out, line = [], ""
    for w in words:
        if len(line) + len(w) + 1 <= n:
            line = (line + " " + w).strip()
        else:
            if line:
                out.append(line)
            line = w
    if line:
        out.append(line)
    return out


class _Base:
    FONT = "Segoe UI,Arial,sans-serif"

    def __init__(self, W, H, title="", subtitle=""):
        self.W, self.H = W, H
        self.title, self.subtitle = title, subtitle
        self.title_h = 54 if title else 0
        self.foot_h = 24
        self.defs, self.body = [], []
        self._bg()

    def _bg(self):
        self.defs.append(
            f'<linearGradient id="bg" x1="0" y1="0" x2="0.3" y2="1">'
            f'<stop offset="0" stop-color="{PAL["bg0"]}"/>'
            f'<stop offset="1" stop-color="{PAL["bg1"]}"/></linearGradient>')
        self.body.append(f'<rect width="{self.W}" height="{self.H}" fill="url(#bg)"/>')
        if self.title:
            self.body.append(f'<rect x="0" y="0" width="{self.W}" height="{self.title_h}" fill="{PAL["bg1"]}"/>')
            self.body.append(f'<rect x="0" y="0" width="6" height="{self.title_h}" fill="{PAL["gold"]}"/>')
            self._t(20, 26, self.title, 18, PAL["ink"], 800, "start")
            if self.subtitle:
                self._t(20, 44, self.subtitle, 11.5, PAL["mut"], 500, "start")
        # footer marca
        self._t(self.W - 12, self.H - 8, "MISTER ÉLITE · Moisés Díaz", 10, "#8aa0b6", 700, "end")
        self._t(12, self.H - 8, "Pretemporada · MISTER ÉLITE", 10, "#7f93a8", 600, "start")

    # primitivas
    def _rect(self, x, y, w, h, fill="none", rx=0, stroke=None, sw=1, op=1, dash=None):
        s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
                         f'rx="{rx}" fill="{fill}" opacity="{op}"{s}{d}/>')

    def _line(self, x1, y1, x2, y2, c, w=2, dash=None, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                         f'stroke="{c}" stroke-width="{w}" opacity="{op}"{d}/>')

    def _circle(self, cx, cy, r, fill, stroke=None, sw=2):
        s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.body.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"{s}/>')

    def _t(self, x, y, s, size=12, c=None, w=600, anchor="middle", style=""):
        c = c or PAL["ink"]
        self.body.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{self.FONT}" font-size="{size}" '
                         f'font-weight="{w}" fill="{c}" text-anchor="{anchor}" {style}>{_esc(s)}</text>')

    def _path(self, d, c, w=2.5, fill="none", dash=None, op=1):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" opacity="{op}"{ds}/>')

    def _smooth(self, pts):
        """devuelve un path 'd' suavizado (catmull-rom -> bezier) por una lista de (x,y)."""
        if len(pts) < 2:
            return ""
        d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
        for i in range(len(pts) - 1):
            p0 = pts[i - 1] if i > 0 else pts[i]
            p1, p2 = pts[i], pts[i + 1]
            p3 = pts[i + 2] if i + 2 < len(pts) else p2
            c1x = p1[0] + (p2[0] - p0[0]) / 6.0
            c1y = p1[1] + (p2[1] - p0[1]) / 6.0
            c2x = p2[0] - (p3[0] - p1[0]) / 6.0
            c2y = p2[1] - (p3[1] - p1[1]) / 6.0
            d += f" C{c1x:.1f},{c1y:.1f} {c2x:.1f},{c2y:.1f} {p2[0]:.1f},{p2[1]:.1f}"
        return d

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" '
                f'width="{self.W}" height="{self.H}" font-family="{self.FONT}">'
                f'<defs>{"".join(self.defs)}</defs>{"".join(self.body)}</svg>')

    def save(self, path):
        open(path, "w", encoding="utf-8").write(self.svg())
        return path


class Calendar(_Base):
    """Microciclo tipo. days = lista de dicts:
       {"d":"LUN", "load":"media", "tag":"opcional",
        "sessions":[{"slot":"AM"/"", "focus":"...", "load":"media"}, ...]}
    """
    def __init__(self, title, days, subtitle="", note=""):
        n = len(days)
        W = max(720, 96 * n + 40)
        H = 470
        super().__init__(W, H, title, subtitle)
        self.days, self.note = days, note
        self._draw()

    def _draw(self):
        M = 20
        top = self.title_h + 14
        colw = (self.W - 2 * M) / len(self.days)
        cards_top = top + 26
        cards_h = 200
        # zona de curva de carga
        cg_top = cards_top + cards_h + 16
        cg_h = 96
        cg_bot = cg_top + cg_h
        # encabezados de día + tarjetas
        for i, day in enumerate(self.days):
            cx = M + i * colw
            cxc = cx + colw / 2
            # cabecera día
            self._rect(cx + 4, top, colw - 8, 22, fill=PAL["panel"], rx=6, stroke=PAL["panelb"], sw=1)
            self._t(cxc, top + 15, day["d"], 12.5, PAL["gold"], 800)
            # sesiones apiladas
            sess = day.get("sessions", [])
            if not sess:
                # día de descanso
                self._rect(cx + 4, cards_top, colw - 8, cards_h, fill="#102234", rx=8,
                           stroke=PAL["panelb"], sw=1, dash="4 4")
                self._t(cxc, cards_top + cards_h / 2 - 4, "DESCANSO", 11, PAL["reposo"], 800)
                self._t(cxc, cards_top + cards_h / 2 + 13, "recuperar", 9.5, PAL["mut"], 500)
                continue
            sh = (cards_h - (len(sess) - 1) * 8) / len(sess)
            for j, s in enumerate(sess):
                sy = cards_top + j * (sh + 8)
                lc = LOADc.get(s.get("load", "media"), PAL["media"])
                self._rect(cx + 4, sy, colw - 8, sh, fill=PAL["panel"], rx=8, stroke=PAL["panelb"], sw=1)
                self._rect(cx + 4, sy, 5, sh, fill=lc, rx=0)
                yy = sy + 16
                if s.get("slot"):
                    self._t(cx + 14, yy, s["slot"], 9.5, lc, 800, "start")
                    yy += 15
                for ln in _wrap(s["focus"], max(9, int(colw / 6.6))):
                    self._t(cx + 14, yy, ln, 10.3, PAL["ink"], 600, "start")
                    yy += 13
                # etiqueta de carga abajo
                lw = s.get("load", "media")
                self._t(cx + colw - 12, sy + sh - 8, lw.upper(), 8.5, lc, 800, "end")
        # ----- curva de carga semanal -----
        self._rect(M, cg_top, self.W - 2 * M, cg_h, fill="#0c1d2e", rx=8, stroke=PAL["panelb"], sw=1)
        self._t(M + 10, cg_top + 15, "CARGA DEL DÍA (sRPE relativo)", 9.5, PAL["mut"], 700, "start")
        base = cg_bot - 12
        peak = cg_top + 24
        pts = []
        for i, day in enumerate(self.days):
            cxc = M + (i + 0.5) * colw
            lv = LOADv.get(day.get("load", "media"), 3.0)
            h = (lv / 5.0) * (base - peak)
            by = base - h
            lc = LOADc.get(day.get("load", "media"), PAL["media"])
            self._rect(cxc - colw * 0.26, by, colw * 0.52, base - by, fill=lc, rx=3, op=0.85)
            pts.append((cxc, by))
        self._path(self._smooth(pts), PAL["gold"], 2.6)
        for (px, py) in pts:
            self._circle(px, py, 3.2, PAL["bg1"], PAL["gold"], 2)
        # leyenda de carga
        ly = cg_bot + 18
        lx = M
        for name in ["alta", "media", "baja", "reposo", "partido"]:
            self._rect(lx, ly - 9, 12, 12, fill=LOADc[name], rx=3)
            self._t(lx + 17, ly + 1, name, 10, PAL["mut"], 600, "start")
            lx += 22 + len(name) * 7.2
        if self.note:
            self._t(self.W - M, ly + 1, self.note, 10, PAL["gold"], 600, "end")


class Curve(_Base):
    """Curva suave con bandas opcionales. points = [(label, value0..1), ...]
       bands = [(y0,y1,color,op,label)] en fracción 0..1 del eje y.
       markers = [(x_index, texto, color)] anotaciones."""
    def __init__(self, title, points, subtitle="", bands=None, markers=None,
                 ylab="", xlab="", area=True, color=None, points2=None, legend2=None):
        super().__init__(760, 380, title, subtitle)
        self.points, self.bands = points, bands or []
        self.markers, self.ylab, self.xlab = markers or [], ylab, xlab
        self.area, self.color = area, color or PAL["gold"]
        self.points2, self.legend2 = points2, legend2 or ("", "")
        self._draw()

    def _draw(self):
        M = 54
        top = self.title_h + 22
        bot = self.H - 46
        left = M
        right = self.W - 24
        # bandas horizontales
        for (y0, y1, c, op, lab) in self.bands:
            yA = bot - y1 * (bot - top)
            yB = bot - y0 * (bot - top)
            self._rect(left, yA, right - left, yB - yA, fill=c, op=op, rx=0)
            if lab:
                self._t(right - 6, yA + 13, lab, 10, c, 800, "end")
        # ejes
        self._line(left, top, left, bot, PAL["grid"], 1.4)
        self._line(left, bot, right, bot, PAL["grid"], 1.4)
        if self.ylab:
            self._t(16, (top + bot) / 2, self.ylab, 11, PAL["mut"], 700, "middle",
                    style=f'transform="rotate(-90,16,{(top+bot)/2:.0f})"')
        if self.xlab:
            self._t((left + right) / 2, self.H - 28, self.xlab, 11, PAL["mut"], 700)
        n = len(self.points)
        pts = []
        for i, (lab, v) in enumerate(self.points):
            x = left + (i / max(1, n - 1)) * (right - left)
            y = bot - max(0, min(1, v)) * (bot - top)
            pts.append((x, y))
            self._t(x, bot + 16, lab, 9.5, PAL["mut"], 600)
        d = self._smooth(pts)
        if self.area and d:
            self._path(d + f" L{pts[-1][0]:.1f},{bot:.1f} L{pts[0][0]:.1f},{bot:.1f} Z",
                       "none", 0, fill=self.color, op=0.12)
        self._path(d, self.color, 3)
        for (px, py) in pts:
            self._circle(px, py, 3.4, PAL["bg1"], self.color, 2.2)
        # segunda serie (línea discontinua, p.ej. intensidad en el tapering)
        if self.points2:
            pts2 = []
            for i, (lab, v) in enumerate(self.points2):
                x = left + (i / max(1, len(self.points2) - 1)) * (right - left)
                y = bot - max(0, min(1, v)) * (bot - top)
                pts2.append((x, y))
            self._path(self._smooth(pts2), PAL["blue"], 2.6, dash="6 5")
            for (px, py) in pts2:
                self._circle(px, py, 3.0, PAL["bg1"], PAL["blue"], 2)
            # mini-leyenda de las dos series
            lx, ly = left + 8, top + 8
            self._line(lx, ly, lx + 22, ly, self.color, 3)
            self._t(lx + 28, ly + 4, self.legend2[0], 10, self.color, 700, "start")
            self._line(lx + 140, ly, lx + 162, ly, PAL["blue"], 2.6, dash="6 5")
            self._t(lx + 168, ly + 4, self.legend2[1], 10, PAL["blue"], 700, "start")
        for (xi, txt, c) in self.markers:
            x = left + (xi / max(1, n - 1)) * (right - left)
            self._line(x, top, x, bot, c, 1.4, dash="4 4", op=0.8)
            for k, ln in enumerate(_wrap(txt, 18)):
                self._t(x + 5, top + 12 + k * 13, ln, 9.5, c, 700, "start")


class Bars(_Base):
    """Barras horizontales. items = [(label, value, color?, valuetxt?)]. maxv opcional."""
    def __init__(self, title, items, subtitle="", maxv=None, unit=""):
        super().__init__(720, 70 + 38 * len(items) + 40, title, subtitle)
        self.items, self.unit = items, unit
        self.maxv = maxv or max(it[1] for it in items)
        self._draw()

    def _draw(self):
        M = 20
        top = self.title_h + 22
        labw = 200
        x0 = M + labw
        x1 = self.W - 70
        for i, it in enumerate(self.items):
            lab, val = it[0], it[1]
            c = it[2] if len(it) > 2 and it[2] else PAL["blue"]
            vt = it[3] if len(it) > 3 and it[3] else f"{val}{self.unit}"
            y = top + i * 38
            self._t(M, y + 17, lab, 11.5, PAL["ink"], 600, "start")
            self._rect(x0, y, x1 - x0, 22, fill="#0c1d2e", rx=5, stroke=PAL["panelb"], sw=1)
            w = (val / self.maxv) * (x1 - x0)
            self._rect(x0, y, max(2, w), 22, fill=c, rx=5)
            self._t(x1 + 8, y + 17, vt, 11, PAL["gold"], 800, "start")


class Timeline(_Base):
    """Mapa de fases de la pretemporada. weeks=int (nº semanas).
       phases = [(nombre, semana_ini, semana_fin, color, descripcion)]. (1-indexed inclusive)
       rows = [(etiqueta_fila, [(sem_ini, sem_fin, texto, color)])] barras extra (amistosos, tests...)."""
    def __init__(self, title, weeks, phases, subtitle="", rows=None):
        self.weeks = weeks
        rows = rows or []
        super().__init__(max(760, 90 + 86 * weeks), 150 + 46 * (1 + len(rows)) + 30, title, subtitle)
        self.phases, self.rows = phases, rows
        self._draw()

    def _draw(self):
        M = 20
        labw = 110
        top = self.title_h + 30
        x0 = M + labw
        x1 = self.W - 20
        cw = (x1 - x0) / self.weeks
        # cabecera semanas
        for w in range(self.weeks):
            cx = x0 + w * cw
            self._rect(cx + 2, top - 24, cw - 4, 20, fill=PAL["panel"], rx=5, stroke=PAL["panelb"], sw=1)
            self._t(cx + cw / 2, top - 10, f"SEM {w + 1}", 10.5, PAL["gold"], 800)
        # fila de fases
        self._t(M, top + 22, "FASES", 11, PAL["mut"], 800, "start")
        for (name, a, b, c, desc) in self.phases:
            bx = x0 + (a - 1) * cw
            bw = (b - a + 1) * cw
            self._rect(bx + 2, top + 4, bw - 4, 36, fill=c, rx=7, op=0.9)
            self._t(bx + bw / 2, top + 22, name, 11.5, "#0c1b2a", 800)
            self._t(bx + bw / 2, top + 35, desc, 8.8, "#0c1b2a", 600)
        # filas extra
        ry = top + 56
        for (rlab, bars) in self.rows:
            self._t(M, ry + 22, rlab, 10.5, PAL["mut"], 700, "start")
            self._rect(x0, ry + 4, x1 - x0, 34, fill="#0c1d2e", rx=6, stroke=PAL["panelb"], sw=1)
            for w in range(1, self.weeks):
                gx = x0 + w * cw
                self._line(gx, ry + 4, gx, ry + 38, PAL["grid"], 1, op=0.6)
            for (a, b, txt, c) in bars:
                bx = x0 + (a - 1) * cw
                bw = (b - a + 1) * cw
                self._rect(bx + 3, ry + 9, bw - 6, 24, fill=c, rx=6)
                self._t(bx + bw / 2, ry + 25, txt, 10, "#0c1b2a", 800)
            ry += 46
