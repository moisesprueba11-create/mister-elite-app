#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pitch.py — Motor de pizarra táctica para el curso 1-4-4-2 (MISTER ÉLITE).
Genera SVG limpios y consistentes. Sistema de coordenadas de CAMPO:
  x: 0 (banda izq) .. 100 (banda der)
  y: 0 (línea de fondo propia, abajo) .. 100 (fondo rival, arriba)
El ataque propio va hacia ARRIBA (y creciente).

Uso típico:
    p = Pitch(title="...", half=None)          # campo completo vertical
    p.player(50, 8, "POR", team="own", role="portero")
    p.arrow(50, 20, 50, 45, kind="pass")
    p.zone(30, 40, 70, 60, label="zona")
    p.legend(["pass","run"])
    p.save("graficos/xx.svg")
"""

PALETTE = dict(
    grass1="#2f8a3e", grass2="#2b8139", line="#ffffff",
    own="#1565c0", own_edge="#0d3c75", rival="#c62828", rival_edge="#7f1414",
    neutral="#f5a623", neutral_edge="#9c6510",
    ball="#fafafa", ball_edge="#222",
    pass_c="#ffd54a", run_c="#ffffff", dribble_c="#ffffff", drive_c="#7ee0ff",
    block_c="#ff5252", zone_c="#ffd54a", text="#ffffff", dark="#15202b",
)

class Pitch:
    def __init__(self, title="", half=None, width=680, brand=True, subtitle="", attack_arrow=True):
        """half: None=campo completo; 'att'=mitad de ataque; 'def'=mitad defensiva.
        attack_arrow=False para infografías conceptuales (oculta la flecha ATAQUE)."""
        self.half = half
        self.title = title
        self.subtitle = subtitle
        self.brand = brand
        self.attack_arrow = attack_arrow
        self.W = width
        self.M = 26                       # margen lateral
        self.title_h = 50 if title else 0
        self.foot_h = 24 if brand else 0
        # proporción del campo (105x68 ~ 1.545). Vertical => alto/ancho
        play_w = self.W - 2 * self.M
        ratio = 1.40 if half else 1.52
        play_h = play_w * ratio
        self.play_w, self.play_h = play_w, play_h
        self.H = play_h + 2 * self.M + self.title_h + self.foot_h
        self.x0 = self.M
        self.y0 = self.M + self.title_h   # top del área jugable (en SVG y crece hacia abajo)
        self.defs = []
        self.body = []
        self._legend = None
        self._draw_pitch()

    # ---- transformación coord campo (x:0..100, y:0..100 abajo->arriba) a SVG ----
    def X(self, x):
        return self.x0 + (x / 100.0) * self.play_w
    def Y(self, y):
        if self.half == "att":      # solo mostramos mitad superior 50..100
            yy = (y - 50) / 50.0
        elif self.half == "def":    # mitad inferior 0..50
            yy = y / 50.0
        else:
            yy = y / 100.0
        # y campo crece hacia arriba => SVG y crece hacia abajo
        return self.y0 + (1 - yy) * self.play_h
    def S(self, v):  # escala de longitud relativa al ancho jugable
        return v / 100.0 * self.play_w

    # ----------------------------- CAMPO -----------------------------
    def _rect(self, x, y, w, h, **kw):
        a = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in kw.items())
        self.body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" {a}/>')
    def _line(self, x1, y1, x2, y2, w=2.2, c=None, dash=None, opacity=1):
        c = c or PALETTE["line"]
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                         f'stroke="{c}" stroke-width="{w}"{d} opacity="{opacity}"/>')
    def _circle(self, cx, cy, r, **kw):
        a = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in kw.items())
        self.body.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" {a}/>')
    def _text(self, x, y, s, size=12, c=None, w=700, anchor="middle", style=""):
        c = c or PALETTE["text"]
        self.body.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Segoe UI,Arial,sans-serif" '
                         f'font-size="{size}" font-weight="{w}" fill="{c}" text-anchor="{anchor}" {style}>'
                         f'{_esc(s)}</text>')

    def _draw_pitch(self):
        gx0, gy0 = self.x0, self.y0
        gw, gh = self.play_w, self.play_h
        # césped con franjas
        self.defs.append(
            '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{PALETTE["grass1"]}"/>'
            f'<stop offset="1" stop-color="{PALETTE["grass2"]}"/></linearGradient>')
        # fondo general
        self._rect(0, 0, self.W, self.H, fill=PALETTE["dark"])
        # franjas de césped
        stripes = 10
        for i in range(stripes):
            sh = gh / stripes
            col = "#2f8a3e" if i % 2 == 0 else "#2a7d36"
            self._rect(gx0, gy0 + i * sh, gw, sh + 0.5, fill=col)
        lw = 2.4
        # contorno
        self._rect(gx0, gy0, gw, gh, fill="none", stroke=PALETTE["line"], stroke_width=lw)
        full = self.half is None
        # línea de medio campo y círculo central (solo campo completo)
        if full:
            ymid = self.Y(50)
            self._line(gx0, ymid, gx0 + gw, ymid, w=lw)
            self._circle(self.X(50), self.Y(50), self.S(9.15), fill="none",
                         stroke=PALETTE["line"], stroke_width=lw)
            self._circle(self.X(50), self.Y(50), 2.4, fill=PALETTE["line"])
        # áreas: dibuja según half
        if self.half in (None, "att"):
            self._penalty_area(top=True, lw=lw)
        if self.half in (None, "def"):
            self._penalty_area(top=False, lw=lw)
        # título y marca
        if self.title:
            self._rect(0, 0, self.W, self.title_h, fill=PALETTE["dark"])
            self._text(self.W/2, 24, self.title, size=17, c="#ffffff", w=800)
            if self.subtitle:
                self._text(self.W/2, 40, self.subtitle, size=11, c="#9fb3c8", w=500)
        if self.brand:
            self._rect(0, self.H - self.foot_h, self.W, self.foot_h, fill=PALETTE["dark"])
            self._text(self.W - 12, self.H - 8, "MISTER ÉLITE · Moisés Díaz",
                       size=10, c="#8aa0b6", w=700, anchor="end")
            self._text(12, self.H - 8, "Rondos · MISTER ÉLITE", size=10, c="#7f93a8", w=600, anchor="start")
        # flecha de sentido de ataque
        if self.attack_arrow:
            self._attack_arrow()

    def _penalty_area(self, top, lw):
        gx0, gw = self.x0, self.play_w
        # dimensiones relativas (campo 100 ancho)
        pa_w, pa_d = 58.0, 16.5     # gran área ancho/prof
        ga_w, ga_d = 26.0, 5.5      # área pequeña
        xL = self.X(50 - pa_w/2); xR = self.X(50 + pa_w/2)
        gxL = self.X(50 - ga_w/2); gxR = self.X(50 + ga_w/2)
        if top:
            yb = self.Y(100); yfront = self.Y(100 - pa_d); ygf = self.Y(100 - ga_d)
            spoty = self.Y(100 - 11)
        else:
            yb = self.Y(0); yfront = self.Y(pa_d); ygf = self.Y(ga_d)
            spoty = self.Y(11)
        # gran área
        self.body.append(f'<path d="M{xL:.1f},{yb:.1f} L{xL:.1f},{yfront:.1f} L{xR:.1f},{yfront:.1f} '
                         f'L{xR:.1f},{yb:.1f}" fill="none" stroke="{PALETTE["line"]}" stroke-width="{lw}"/>')
        # área pequeña
        self.body.append(f'<path d="M{gxL:.1f},{yb:.1f} L{gxL:.1f},{ygf:.1f} L{gxR:.1f},{ygf:.1f} '
                         f'L{gxR:.1f},{yb:.1f}" fill="none" stroke="{PALETTE["line"]}" stroke-width="{lw}"/>')
        # punto de penalti
        self._circle(self.X(50), spoty, 2.0, fill=PALETTE["line"])
        # portería
        gw2 = 9.0
        gxgL = self.X(50 - gw2/2); gxgR = self.X(50 + gw2/2)
        gy = yb + (-4 if top else 4)
        self.body.append(f'<rect x="{gxgL:.1f}" y="{min(gy,yb):.1f}" width="{(gxgR-gxgL):.1f}" '
                         f'height="4" fill="none" stroke="{PALETTE["line"]}" stroke-width="2"/>')
        # arco frontal del área
        r = self.S(9.15)
        cx = self.X(50)
        import math
        if top:
            self.body.append(f'<path d="M{cx-self.S(7):.1f},{yfront:.1f} A{r:.1f},{r:.1f} 0 0 1 '
                             f'{cx+self.S(7):.1f},{yfront:.1f}" fill="none" stroke="{PALETTE["line"]}" stroke-width="{lw}"/>')
        else:
            self.body.append(f'<path d="M{cx-self.S(7):.1f},{yfront:.1f} A{r:.1f},{r:.1f} 0 0 0 '
                             f'{cx+self.S(7):.1f},{yfront:.1f}" fill="none" stroke="{PALETTE["line"]}" stroke-width="{lw}"/>')

    def _attack_arrow(self):
        x = self.X(96)
        # La flecha debe quedar SIEMPRE dentro del área jugable, sin importar `half`.
        # En mitad de ataque (50..100) o defensa (0..50) los valores fijos 44/56
        # se extrapolan fuera del campo, así que centramos la flecha en el rango
        # visible y la mantenemos con un pequeño margen interior.
        if self.half == "att":
            lo, hi = 56.0, 62.0      # dentro de 50..100
        elif self.half == "def":
            lo, hi = 38.0, 44.0      # dentro de 0..50
        else:
            lo, hi = 44.0, 56.0
        # asegurar que las coordenadas SVG caen dentro del área jugable
        ytop, ybot = self.y0, self.y0 + self.play_h
        y1 = min(max(self.Y(lo), ytop + 4), ybot - 4)
        y2 = min(max(self.Y(hi), ytop + 4), ybot - 4)
        self.body.append(f'<g opacity="0.9"><line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" '
                         f'stroke="#ffffff" stroke-width="2.5" marker-end="url(#ah_white)"/>'
                         f'<text x="{x-6:.1f}" y="{(y1+y2)/2:.1f}" font-family="Segoe UI,Arial" font-size="9" '
                         f'fill="#ffffff" text-anchor="end" transform="rotate(-90 {x-6:.1f} {(y1+y2)/2:.1f})">ATAQUE</text></g>')

    # ----------------------------- ELEMENTOS -----------------------------
    def player(self, x, y, label, team="own", role="", r=15, number=None, role_below=False):
        cx, cy = self.X(x), self.Y(y)
        fill = {"own": PALETTE["own"], "rival": PALETTE["rival"], "neutral": PALETTE["neutral"]}[team]
        edge = {"own": PALETTE["own_edge"], "rival": PALETTE["rival_edge"], "neutral": PALETTE["neutral_edge"]}[team]
        self.body.append(f'<g><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" '
                         f'stroke="{edge}" stroke-width="2.5"/>'
                         f'<text x="{cx:.1f}" y="{cy+4:.1f}" font-family="Segoe UI,Arial" font-size="11.5" '
                         f'font-weight="800" fill="#fff" text-anchor="middle">{_esc(label)}</text></g>')
        if role:
            # role_below: coloca el rótulo DEBAJO de la ficha (para jugadores muy
            # arriba, donde el texto encima se saldría del campo o tocaría el borde).
            ry = cy + r + 12 if role_below else cy - r - 4
            self._text(cx, ry, role, size=9.5, c="#fff5cc", w=600)

    def ball(self, x, y, r=6):
        cx, cy = self.X(x), self.Y(y)
        self._circle(cx, cy, r, fill=PALETTE["ball"], stroke=PALETTE["ball_edge"], stroke_width=1.4)
        self.body.append(f'<path d="M{cx:.1f},{cy-r:.1f} l{r*0.5:.1f},{r*0.7:.1f} l-{r*0.8:.1f},0 z" '
                         f'fill="{PALETTE["ball_edge"]}"/>')

    def arrow(self, x1, y1, x2, y2, kind="pass", c=None, label=""):
        """kind: pass(amarillo discont.), run(blanco), drive(azul, conducción),
                 dribble(ondulado), block(T)."""
        X1, Y1, X2, Y2 = self.X(x1), self.Y(y1), self.X(x2), self.Y(y2)
        if kind == "block":
            import math
            ang = math.atan2(Y2 - Y1, X2 - X1)
            bx, by = math.cos(ang + math.pi/2) * 9, math.sin(ang + math.pi/2) * 9
            self._line(X1, Y1, X2, Y2, w=3, c=PALETTE["block_c"])
            self._line(X2 - bx, Y2 - by, X2 + bx, Y2 + by, w=3.4, c=PALETTE["block_c"])
            return
        col = c or {"pass": PALETTE["pass_c"], "run": PALETTE["run_c"],
                    "drive": PALETTE["drive_c"], "dribble": PALETTE["dribble_c"]}[kind]
        dash = ' stroke-dasharray="7 5"' if kind == "pass" else ""
        mk = {"pass": "ah_pass", "run": "ah_run", "drive": "ah_drive", "dribble": "ah_run"}[kind]
        if kind == "dribble":
            path = _wavy(X1, Y1, X2, Y2)
            self.body.append(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="2.6" '
                             f'marker-end="url(#{mk})"/>')
        else:
            self.body.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" '
                             f'stroke="{col}" stroke-width="2.8"{dash} marker-end="url(#{mk})"/>')
        if label:
            mx, my = (X1+X2)/2, (Y1+Y2)/2
            self._text(mx, my - 5, label, size=9.5, c=col, w=700)

    def zone(self, x1, y1, x2, y2, label="", c=None, fill_op=0.16, dash="6 5", ellipse=False):
        c = c or PALETTE["zone_c"]
        X1, Y1, X2, Y2 = self.X(min(x1,x2)), self.Y(max(y1,y2)), self.X(max(x1,x2)), self.Y(min(y1,y2))
        if ellipse:
            cx, cy = (X1+X2)/2, (Y1+Y2)/2
            self.body.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{abs(X2-X1)/2:.1f}" '
                             f'ry="{abs(Y2-Y1)/2:.1f}" fill="{c}" fill-opacity="{fill_op}" '
                             f'stroke="{c}" stroke-width="2" stroke-dasharray="{dash}"/>')
        else:
            self.body.append(f'<rect x="{X1:.1f}" y="{Y1:.1f}" width="{abs(X2-X1):.1f}" '
                             f'height="{abs(Y2-Y1):.1f}" rx="6" fill="{c}" fill-opacity="{fill_op}" '
                             f'stroke="{c}" stroke-width="2" stroke-dasharray="{dash}"/>')
        if label:
            self._text((X1+X2)/2, (Y1+Y2)/2 + 3, label, size=10.5, c="#fff", w=700)

    def cone(self, x, y):
        cx, cy = self.X(x), self.Y(y)
        self.body.append(f'<path d="M{cx:.1f},{cy-7:.1f} l5,11 l-10,0 z" fill="#ff9800" stroke="#7a4f00" stroke-width="1"/>')

    def goalmini(self, x, y):  # mini portería para tareas
        cx, cy = self.X(x), self.Y(y)
        self.body.append(f'<rect x="{cx-12:.1f}" y="{cy-3:.1f}" width="24" height="6" fill="none" '
                         f'stroke="#fff" stroke-width="3"/>')

    def note(self, x, y, s, size=10, c="#fff5cc", anchor="middle", w=600):
        self._text(self.X(x), self.Y(y), s, size=size, c=c, anchor=anchor, w=w)

    def legend(self, items):
        self._legend = items

    def _render_legend(self):
        if not self._legend: return ""
        labels = {"pass": ("pase", PALETTE["pass_c"], True),
                  "run": ("desmarque/carrera", PALETTE["run_c"], False),
                  "drive": ("conducción", PALETTE["drive_c"], False),
                  "dribble": ("regate", PALETTE["dribble_c"], False),
                  "block": ("bloqueo/corte", PALETTE["block_c"], False),
                  "own": ("propio", PALETTE["own"], None),
                  "rival": ("rival", PALETTE["rival"], None),
                  "neutral": ("comodín", PALETTE["neutral"], None),
                  "zone": ("zona", PALETTE["zone_c"], None)}
        items = [i for i in self._legend if i in labels]
        bw, rowh = 168, 17
        bh = 16 + rowh * len(items)
        bx = self.x0 + 6
        by = self.H - self.foot_h - self.M - bh + 6
        out = [f'<g><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="7" fill="#15202b" '
               f'fill-opacity="0.82" stroke="#3a4a5a" stroke-width="1"/>'
               f'<text x="{bx+10}" y="{by+14}" font-family="Segoe UI,Arial" font-size="10" '
               f'font-weight="800" fill="#9fb3c8">LEYENDA</text>']
        yy = by + 14 + 15
        for it in items:
            txt, col, dashed = labels[it]
            lx = bx + 12
            if it in ("own", "rival", "neutral", "zone"):
                out.append(f'<circle cx="{lx+5}" cy="{yy-3}" r="6" fill="{col}"/>')
            else:
                d = ' stroke-dasharray="6 4"' if dashed else ""
                out.append(f'<line x1="{lx}" y1="{yy-3}" x2="{lx+26}" y2="{yy-3}" stroke="{col}" '
                           f'stroke-width="3"{d}/>')
            out.append(f'<text x="{lx+34}" y="{yy}" font-family="Segoe UI,Arial" font-size="10.5" '
                       f'fill="#e6edf3">{_esc(txt)}</text>')
            yy += rowh
        out.append('</g>')
        return "".join(out)

    def _markers(self):
        def m(id_, col):
            return (f'<marker id="{id_}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" '
                    f'markerHeight="6.5" orient="auto-start-reverse">'
                    f'<path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')
        return ("<defs>" + "".join(self.defs)
                + m("ah_pass", PALETTE["pass_c"]) + m("ah_run", PALETTE["run_c"])
                + m("ah_drive", PALETTE["drive_c"]) + m("ah_white", "#ffffff") + "</defs>")

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W:.0f} {self.H:.0f}" '
                f'width="{self.W:.0f}" height="{self.H:.0f}" font-family="Segoe UI,Arial,sans-serif">'
                + self._markers() + "".join(self.body) + self._render_legend() + "</svg>")

    def save(self, path):
        import os
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.svg())
        return path


def _wavy(x1, y1, x2, y2, amp=4, n=6):
    import math
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    pts = [f"M{x1:.1f},{y1:.1f}"]
    for i in range(1, n + 1):
        t = i / n
        bx, by = x1 + dx * t, y1 + dy * t
        off = amp * (1 if i % 2 else -1) * (0 if i == n else 1)
        pts.append(f"L{bx + nx*off:.1f},{by + ny*off:.1f}")
    return " ".join(pts)


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
