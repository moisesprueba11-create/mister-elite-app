#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cover.py — Portada profesional MISTER ÉLITE parametrizada por SISTEMA.
Edita el bloque CONFIG y ejecuta:  python3 build_cover.py
Genera graficos/portada.svg

LINES va de la DEFENSA (primera lista) a la DELANTERA (última lista).
Cada jugador es (dorsal,) -> número que se pinta en la ficha.
El portero (GK) se coloca solo, centrado abajo.
"""
import os

CONFIG = dict(
    system="1-4-2-3-1",
    brand_top="MISTER ÉLITE",
    brand_sub="ACADEMIA DE ENTRENADORES · MOISÉS DÍAZ",
    title_big="1-4-2-3-1",
    title_small="del concepto al campo",
    tagline="Poca teoría. Mucha aplicación práctica.",
    footer_left="Doble pivote · Mediapunta · Extremos · Presión · Transiciones",
    stats=[("4", "módulos de teoría"), ("26", "tareas de campo"),
           ("+40", "pizarras tácticas"), ("2", "microciclos modelo")],
    gk=1,
    lines=[[3, 5, 4, 2],     # defensa de 4: LI, DFCizq, DFCder, LD
           [6, 8],           # doble pivote
           [11, 10, 7],      # linea de 3: EI, mediapunta, ED
           [9]],             # delantero
)

W, H = 794, 1123

def _dots(cfg):
    out = []
    xL, xR = 165, 629
    yGK, yDefRow, yFwdRow = 1012, 928, 612
    lines = cfg["lines"]; n = len(lines)
    # posición Y de cada línea (defensa abajo -> delantera arriba)
    ys = [yDefRow - (yDefRow - yFwdRow) * (i / (n - 1)) for i in range(n)] if n > 1 else [yDefRow]
    pos = []  # (x,y,dorsal,is_fwd)
    for i, line in enumerate(lines):
        m = len(line); y = ys[i]
        for j, d in enumerate(line):
            x = (xL + xR) / 2 if m == 1 else xL + (xR - xL) * (j / (m - 1))
            pos.append((x, y, d, i == n - 1))
    gk = ((xL + xR) / 2, yGK, cfg["gk"], False)
    # conexiones (spine): cada jugador con el más cercano de la línea de abajo
    links = []
    rows = [[gk]] + [[p for p in pos if abs(p[1] - ys[i]) < 1] for i in range(n)]
    for i in range(1, len(rows)):
        for p in rows[i]:
            below = rows[i - 1]
            q = min(below, key=lambda b: abs(b[0] - p[0]))
            links.append((p[0], p[1], q[0], q[1]))
    for x1, y1, x2, y2 in links:
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                   f'stroke="#f7c948" stroke-width="1.6" opacity="0.45" stroke-dasharray="5 5"/>')
    # flechas de ataque desde los delanteros
    for x, y, d, isf in pos:
        if isf:
            out.append(f'<line x1="{x:.0f}" y1="{y-22:.0f}" x2="{x:.0f}" y2="{y-92:.0f}" '
                       f'stroke="#f7c948" stroke-width="2.4" marker-end="url(#ar)" opacity="0.85"/>')
    # fichas
    allp = pos + [gk]
    for x, y, d, isf in allp:
        fill, stroke = ("#c62828", "#f7c948") if isf else ("#0d3c75", "#1d6fb8")
        r = 18 if isf else 17
        out.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{fill}" stroke="{stroke}" '
                   f'stroke-width="2.5"/><text x="{x:.0f}" y="{y+5:.0f}" font-size="13" '
                   f'font-weight="800" fill="#fff" text-anchor="middle">{d}</text></g>')
    return "\n".join(out)

def build(cfg=CONFIG, out_path=None):
    s = cfg["stats"]
    cards = ""
    coords = [(470, 318), (632, 318), (470, 414), (632, 414)]
    for (num, lab), (cx, cy) in zip(s, coords):
        cards += (f'<g transform="translate({cx},{cy})"><rect width="150" height="84" rx="12" '
                  f'fill="#13283d" stroke="#24435f"/><text x="18" y="46" font-size="36" '
                  f'font-weight="900" fill="#f7c948">{num}</text><text x="18" y="68" font-size="12" '
                  f'fill="#cdd9e5">{lab}</text></g>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Segoe UI,Arial,sans-serif">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="#0c1b2a"/><stop offset="0.55" stop-color="#0f2438"/><stop offset="1" stop-color="#08131f"/></linearGradient>
 <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f7c948"/><stop offset="1" stop-color="#e0a526"/></linearGradient>
 <radialGradient id="glow" cx="0.5" cy="0.42" r="0.6"><stop offset="0" stop-color="#1d6fb8" stop-opacity="0.35"/><stop offset="1" stop-color="#1d6fb8" stop-opacity="0"/></radialGradient>
 <marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#f7c948"/></marker>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/><rect width="{W}" height="{H}" fill="url(#glow)"/>
<g opacity="0.16" stroke="#ffffff" stroke-width="2" fill="none">
 <rect x="120" y="470" width="554" height="600"/><line x1="120" y1="770" x2="674" y2="770"/>
 <circle cx="397" cy="770" r="74"/><circle cx="397" cy="770" r="3" fill="#fff"/>
 <rect x="277" y="470" width="240" height="92"/><rect x="337" y="470" width="120" height="36"/>
 <rect x="277" y="978" width="240" height="92"/><rect x="337" y="1034" width="120" height="36"/>
</g>
<g opacity="0.92">{_dots(cfg)}</g>
<rect x="0" y="0" width="{W}" height="8" fill="url(#gold)"/>
<g transform="translate(64,92)"><rect width="46" height="46" rx="10" fill="url(#gold)"/>
 <text x="23" y="32" font-size="28" font-weight="900" fill="#0c1b2a" text-anchor="middle">ME</text>
 <text x="62" y="22" font-size="20" font-weight="900" fill="#ffffff" letter-spacing="3">{cfg["brand_top"]}</text>
 <text x="62" y="41" font-size="12.5" font-weight="600" fill="#f7c948" letter-spacing="2">{cfg["brand_sub"]}</text></g>
<g transform="translate(64,300)">
 <text x="0" y="0" font-size="17" font-weight="700" fill="#7fd0ff" letter-spacing="6">CURSO TÁCTICO PROFESIONAL</text>
 <text x="0" y="78" font-size="92" font-weight="900" fill="#ffffff" letter-spacing="-2">{cfg["title_big"]}</text>
 <text x="0" y="136" font-size="33" font-weight="800" fill="#f7c948">{cfg["title_small"]}</text>
 <line x1="4" y1="166" x2="120" y2="166" stroke="#f7c948" stroke-width="4"/>
 <text x="0" y="206" font-size="18" font-weight="500" fill="#cdd9e5">{cfg["tagline"]}</text></g>
<g>{cards}</g>
<rect x="0" y="1080" width="{W}" height="43" fill="#08131f"/>
<text x="64" y="1107" font-size="13" font-weight="600" fill="#8aa0b6">{cfg["footer_left"]}</text>
<text x="730" y="1107" font-size="13" font-weight="800" fill="#f7c948" text-anchor="end">{cfg["brand_top"]}</text>
<rect x="0" y="1115" width="{W}" height="8" fill="url(#gold)"/>
</svg>'''
    out_path = out_path or os.path.join(os.path.dirname(os.path.abspath(__file__)), "graficos", "portada.svg")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(svg)
    print("portada.svg generada:", out_path)

if __name__ == "__main__":
    build()
