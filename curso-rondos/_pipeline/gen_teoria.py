#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de los 10 diagramas de TEORÍA del curso Rondos (MISTER ÉLITE)."""
import sys, math
sys.path.insert(0, '/home/user/mister-elite-app/curso-rondos/graficos/lib')
from pitch import Pitch, PALETTE, _esc

G = "graficos"

# Helpers de bajo nivel para infografía (dibujan directamente en coords SVG) -----

def panel(p, x1, y1, x2, y2, fill="#15202b", op=0.86, stroke="#3a4a5a", sw=1.6, rx=10):
    """Caja en coords de CAMPO (0..100)."""
    X1, Y1 = p.X(min(x1, x2)), p.Y(max(y1, y2))
    X2, Y2 = p.X(max(x1, x2)), p.Y(min(y1, y2))
    p.body.append(f'<rect x="{X1:.1f}" y="{Y1:.1f}" width="{abs(X2-X1):.1f}" '
                  f'height="{abs(Y2-Y1):.1f}" rx="{rx}" fill="{fill}" fill-opacity="{op}" '
                  f'stroke="{stroke}" stroke-width="{sw}"/>')

def chip(p, x1, y1, x2, y2, fill, op=0.92, stroke=None, sw=2, rx=9):
    X1, Y1 = p.X(min(x1, x2)), p.Y(max(y1, y2))
    X2, Y2 = p.X(max(x1, x2)), p.Y(min(y1, y2))
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    p.body.append(f'<rect x="{X1:.1f}" y="{Y1:.1f}" width="{abs(X2-X1):.1f}" '
                  f'height="{abs(Y2-Y1):.1f}" rx="{rx}" fill="{fill}" fill-opacity="{op}"{st}/>')

def txt(p, x, y, s, size=11, c="#ffffff", w=700, anchor="middle"):
    p._text(p.X(x), p.Y(y), s, size=size, c=c, w=w, anchor=anchor)

def bigarrow(p, x1, y1, x2, y2, c="#f7c948", w=5, mk="ah_pass"):
    p.body.append(f'<line x1="{p.X(x1):.1f}" y1="{p.Y(y1):.1f}" x2="{p.X(x2):.1f}" '
                  f'y2="{p.Y(y2):.1f}" stroke="{c}" stroke-width="{w}" marker-end="url(#{mk})"/>')

def chevron(p, x, y, w=4, c="#f7c948"):
    """Flecha gruesa hacia la derecha en (x,y)."""
    X, Y = p.X(x), p.Y(y)
    s = 9
    p.body.append(f'<path d="M{X-s:.1f},{Y-s:.1f} L{X:.1f},{Y:.1f} L{X-s:.1f},{Y+s:.1f}" '
                  f'fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')

GOLD = "#f7c948"

# ======================================================================
# 01 — DEFINICIÓN (el "cerco")
# ======================================================================
def t01():
    p = Pitch(title="Qué es un rondo — el cerco",
              subtitle="4v1 · poseedores en el perímetro, recuperador acosado en el centro", half=None)
    # cuadro
    cx = [22, 78, 78, 22]; cy = [72, 72, 32, 32]
    for x, y in zip(cx, cy):
        p.cone(x, y)
    p.zone(22, 32, 78, 72, label="")
    # poseedores azules en las esquinas
    P = [(24, 70, "P1"), (76, 70, "P2"), (76, 34, "P3"), (24, 34, "P4")]
    for x, y, l in P:
        p.player(x, y, l, team="own")
    # defensor rojo en el centro
    p.player(50, 52, "D", team="rival", role="acosa")
    p.ball(28, 67)
    # pases rodeando al defensor (cerco)
    p.arrow(28, 70, 72, 70, kind="pass")
    p.arrow(76, 67, 76, 37, kind="pass")
    p.arrow(72, 34, 28, 34, kind="pass")
    p.arrow(24, 37, 24, 67, kind="pass")
    p.note(50, 26, "Superioridad estable + espacio reducido + posiciones fijas + oposición real")
    p.legend(["pass", "own", "rival", "zone"])
    p.save(f"{G}/teoria-01-definicion.svg")

# ======================================================================
# 02 — CONTINUO DE ESPECIFICIDAD (5 peldaños)
# ======================================================================
def t02():
    p = Pitch(title="Continuo de especificidad",
              subtitle="cada peldaño gana realismo y pierde control aislado del estímulo", half=None)
    steps = [
        ("RONDO", "sin dirección", PALETTE["own"]),
        ("RONDO\nDIRECCIONAL", "+ sentido", "#1f7ab8"),
        ("JUEGO DE\nPOSICIÓN", "+ zonas/dirección", PALETTE["neutral"]),
        ("PARTIDO\nREDUCIDO", "+ porterías", "#d77a1e"),
        ("PARTIDO", "+ rival/igualdad", PALETTE["rival"]),
    ]
    n = len(steps)
    x0, x1 = 8, 92
    bw = 14.5
    gap = (x1 - x0 - bw) / (n - 1)
    # banda guía
    panel(p, 5, 78, 95, 22, fill="#0c1b2a", op=0.35, stroke="#2a3a4a", sw=1)
    yc = 56
    for i, (name, sub, col) in enumerate(steps):
        xL = x0 + i * gap
        xR = xL + bw
        chip(p, xL, yc + 9, xR, yc - 9, col, op=0.9, stroke="#ffffff", sw=1.5)
        lines = name.split("\n")
        ly = yc + (4 if len(lines) == 1 else 7.5)
        for ln in lines:
            txt(p, (xL + xR) / 2, ly, ln, size=10.5, c="#fff", w=800)
            ly -= 7
        txt(p, (xL + xR) / 2, yc - 13, sub, size=8.5, c="#cfe0ee", w=600)
        if i < n - 1:
            chevron(p, xR + gap / 2 + 1.0, yc, w=4, c=GOLD)
    # flechas crecientes/decrecientes
    bigarrow(p, 10, 38, 90, 38, c=GOLD, w=5, mk="ah_pass")
    txt(p, 50, 33, "+ REALISMO / ESPECIFICIDAD  →", size=11, c=GOLD, w=800)
    bigarrow(p, 90, 70, 10, 70, c="#9fb3c8", w=4.5, mk="ah_run")
    txt(p, 50, 73.5, "←  + CONTROL AISLADO DEL ESTÍMULO", size=10.5, c="#cfe0ee", w=700)
    p.note(50, 27, "El rondo es la puerta de entrada; el partido, la validación", size=10)
    p.save(f"{G}/teoria-02-continuo-especificidad.svg")

# ======================================================================
# 03 — TIPOS DE BENEFICIO (5 bloques convergiendo en rondo central)
# ======================================================================
def t03():
    p = Pitch(title="Los cinco tipos de beneficio",
              subtitle="el rondo entrena todas estas dimensiones a la vez", half=None)
    # rondo central (mini)
    cxc, cyc = 50, 50
    panel(p, 38, 62, 62, 38, fill="#1f7a36", op=0.30, stroke="#ffffff", sw=1.5)
    for dx, dy in [(-8, 8), (8, 8), (8, -8), (-8, -8)]:
        p.player(cxc + dx, cyc + dy, "P", team="own", r=9)
    p.player(cxc, cyc, "D", team="rival", r=9)
    # 5 bloques alrededor
    blocks = [
        ("TÉCNICO", "control orientado · pase · 1-2 toques", 50, 86, PALETTE["own"]),
        ("TÁCTICO", "apoyos · triángulos · defensa en inferioridad", 17, 64, "#1f7ab8"),
        ("COGNITIVO-PERCEPTIVO", "escaneo · decisión bajo presión", 83, 64, PALETTE["neutral"]),
        ("FÍSICO-CONDICIONAL", "intermitente · RSA · agilidad", 17, 30, "#d77a1e"),
        ("SOCIOEMOCIONAL", "competir · comunicar · gestionar el error", 83, 30, PALETTE["rival"]),
    ]
    for name, sub, bx, by, col in blocks:
        chip(p, bx - 16, by + 6, bx + 16, by - 6, col, op=0.9, stroke="#ffffff", sw=1.4)
        txt(p, bx, by + 2.5, name, size=10, c="#fff", w=800)
        txt(p, bx, by - 3.5, sub, size=7.6, c="#eef3f8", w=600)
        # flecha hacia el centro
        ang = math.atan2((cyc - by), (cxc - bx))
        sx = bx + 17 * math.cos(ang)
        sy = by + 7 * math.sin(ang)
        ex = cxc - 14 * math.cos(ang)
        ey = cyc - 14 * math.sin(ang)
        bigarrow(p, sx, sy, ex, ey, c=GOLD, w=3, mk="ah_pass")
    p.save(f"{G}/teoria-03-tipos-beneficio.svg")

# ======================================================================
# 04 — VARIABLES DE DISEÑO (panel de mandos, 6 diales)
# ======================================================================
def t04():
    p = Pitch(title="El panel de mandos",
              subtitle="seis variables de diseño · toca una cada vez", half=None)
    panel(p, 5, 87, 95, 15, fill="#0c1b2a", op=0.45, stroke="#2a3a4a", sw=1)
    # color de marca unificado para todos los diales (azul de marca, sin rojo)
    DIAL = "#3f6f9e"
    vars_ = [
        ("RELACIÓN\nNUMÉRICA", "4v1 · 5v2 · 6v3 · 7v2"),
        ("ESPACIO\n/ FORMA", "tamaño · cuadro / círculo"),
        ("Nº DE\nTOQUES", "libre → 3 → 2 → 1"),
        ("COMODINES", "interior · banda · puerta"),
        ("REGLAS /\nPROVOCACIONES", "premios · prohibiciones"),
        ("OBJETIVO", "mantener · progresar · presionar"),
    ]
    # rejilla 3 columnas x 2 filas; cada celda: dial arriba, nombre debajo, sublabel debajo
    cols = 3
    xs = [22, 50, 78]
    dial_y = [74, 44]                 # centro del dial por fila
    R = 6.8
    rr = (R / 100.0) * p.play_w
    for i, (name, sub) in enumerate(vars_):
        cxx = xs[i % cols]
        dy = dial_y[i // cols]
        CX, CY = p.X(cxx), p.Y(dy)
        # dial
        p.body.append(f'<circle cx="{CX:.1f}" cy="{CY:.1f}" r="{rr:.1f}" fill="#10202e" '
                      f'stroke="{DIAL}" stroke-width="3"/>')
        p.body.append(f'<circle cx="{CX:.1f}" cy="{CY:.1f}" r="{rr*0.18:.1f}" fill="{DIAL}"/>')
        # aguja (ámbar de marca como acento)
        a = math.radians(140 - i * 35)
        nx = CX + rr * 0.72 * math.cos(a)
        ny = CY - rr * 0.72 * math.sin(a)
        p.body.append(f'<line x1="{CX:.1f}" y1="{CY:.1f}" x2="{nx:.1f}" y2="{ny:.1f}" '
                      f'stroke="{GOLD}" stroke-width="2.6" stroke-linecap="round"/>')
        # ticks
        for k in range(5):
            ta = math.radians(150 - k * 60)
            x1 = CX + rr * 0.92 * math.cos(ta); y1 = CY - rr * 0.92 * math.sin(ta)
            x2 = CX + rr * 1.05 * math.cos(ta); y2 = CY - rr * 1.05 * math.sin(ta)
            p.body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                          f'stroke="#7f93a8" stroke-width="1.4"/>')
        # nombre (1-2 líneas) anclado BAJO el dial
        lines = name.split("\n")
        ly = dy - R - 4.5
        for ln in lines:
            txt(p, cxx, ly, ln, size=9.4, c="#fff", w=800)
            ly -= 5.4
        # sublabel anclado bajo el nombre, dentro de la celda
        txt(p, cxx, ly - 0.5, sub, size=7.4, c="#cfe0ee", w=600)
    # banda inferior con la regla de oro, separada de los diales
    chip(p, 14, 23, 86, 16, "#1c2c3a", op=0.95, stroke=GOLD, sw=1.6, rx=8)
    txt(p, 50, 20.2, "OBJETIVO → VARIABLES, nunca al revés", size=11.5, c=GOLD, w=800)
    p.save(f"{G}/teoria-04-variables-diseno.svg")

# ======================================================================
# 05 — RELACIONES NUMÉRICAS (4 mini-jaulas: 4v1, 5v2, 4v2, 3v1)
# ======================================================================
def t05():
    p = Pitch(title="Relaciones numéricas",
              subtitle="la misma idea, distinta superioridad", half=None)
    # 4 cuadrantes
    def cage(cx, cy, hw, poss, defs, name, sup):
        # marco
        panel(p, cx - hw, cy + hw * 0.92, cx + hw, cy - hw * 0.92,
              fill="#1f7a36", op=0.26, stroke="#ffffff", sw=1.4, rx=8)
        # poseedores azules en perímetro (reparto en círculo)
        for i in range(poss):
            a = math.pi / 2 + 2 * math.pi * i / poss
            x = cx + (hw - 1.5) * math.cos(a)
            y = cy + (hw * 0.8) * math.sin(a)
            p.player(x, y, "P", team="own", r=7)
        # defensores rojos en el centro
        if defs == 1:
            p.player(cx, cy, "D", team="rival", r=7)
        else:
            for i in range(defs):
                x = cx + 3.2 * (i - (defs - 1) / 2)
                p.player(x, cy, "D", team="rival", r=7)
        txt(p, cx, cy + hw * 1.02 + 2.5, name, size=11.5, c="#fff", w=800)
        txt(p, cx, cy - hw * 1.02 - 1.5, sup, size=10, c=GOLD, w=800)
    cage(28, 71, 11.5, 4, 1, "4 v 1", "+3")
    cage(72, 71, 11.5, 5, 2, "5 v 2", "+3")
    cage(28, 31, 11.5, 6, 3, "6 v 3", "+3")
    cage(72, 31, 11.5, 7, 2, "7 v 2", "+5")
    # divisores sutiles
    p._line(p.X(50), p.Y(88), p.X(50), p.Y(15), w=1.2, c="#2a3a4a", dash="5 6", opacity=0.7)
    p._line(p.X(8), p.Y(51), p.X(92), p.Y(51), w=1.2, c="#2a3a4a", dash="5 6", opacity=0.7)
    p.note(50, 9, "misma idea, superioridad creciente: +3 · +3 · +3 · +5", size=10)
    p.save(f"{G}/teoria-05-relaciones-numericas.svg")

# ======================================================================
# 06 — PROGRESIÓN (escalera + zona de reto 60-75%)
# ======================================================================
def t06():
    p = Pitch(title="Cómo progresar un rondo",
              subtitle="subir exigencia de forma graduada y medible", half=None)
    # zona de reto sombreada (banda horizontal)
    p.zone(8, 47, 92, 67, label="", c="#6fe08a", fill_op=0.16)
    txt(p, 50, 70.5, "ZONA DE RETO · ≈ 60–75 % de éxito", size=11, c="#bff0c8", w=800)
    # escalera ascendente: 5 peldaños
    levers = [
        ("Reducir\nespacio", 16, 30),
        ("Limitar\ntoques", 31, 40),
        ("+ Defensor", 48, 50),
        ("Exigir\ndirección", 65, 60),
        ("Premiar\ncomportam.", 82, 70),
    ]
    # peldaños como cajas
    prev = None
    for name, x, y in levers:
        chip(p, x - 7, y + 4.5, x + 7, y - 4.5, PALETTE["own"], op=0.92, stroke="#ffffff", sw=1.4)
        lines = name.split("\n")
        ly = y + (2.5 if len(lines) == 1 else 4.5)
        for ln in lines:
            txt(p, x, ly, ln, size=8.8, c="#fff", w=800)
            ly -= 5.2
        if prev:
            bigarrow(p, prev[0] + 7, prev[1] + 1, x - 7, y - 1, c=GOLD, w=3.2, mk="ah_pass")
        prev = (x, y)
    # eje exigencia
    bigarrow(p, 8, 22, 8, 82, c="#9fb3c8", w=3, mk="ah_run")
    txt(p, 5.5, 50, "EXIGENCIA", size=9, c="#cfe0ee", w=700, anchor="middle")
    p.body[-1] = p.body[-1].replace('>EXIGENCIA<', f' transform="rotate(-90 {p.X(5.5):.1f} {p.Y(50):.1f})">EXIGENCIA<')
    bigarrow(p, 8, 14, 92, 14, c="#9fb3c8", w=3, mk="ah_run")
    txt(p, 50, 11, "PROGRESIÓN  →", size=9.5, c="#cfe0ee", w=700)
    p.note(50, 84, "Si el balón no circula: agranda el espacio o libera toques (regresar es legítimo)", size=9.2)
    p.save(f"{G}/teoria-06-progresion.svg")

# ======================================================================
# 07 — COACHING / FREEZE
# ======================================================================
def t07():
    p = Pitch(title="Coachear el rondo — el freeze",
              subtitle="congelar la imagen y preguntar por la línea no vista", half=None)
    # cuadro de rondo
    for x, y in [(24, 68), (76, 68), (76, 34), (24, 34)]:
        p.cone(x, y)
    p.zone(24, 34, 76, 68, label="")
    # poseedores
    p.player(28, 64, "P1", team="own"); p.ball(31, 61)
    p.player(72, 64, "P2", team="own")
    p.player(72, 38, "P3", team="own")
    p.player(28, 38, "P4", team="own")
    # defensor de espaldas (centro)
    p.player(50, 51, "D", team="rival", role="de espaldas")
    # línea de pase NO vista (blanca discontinua) entre P1 y P3 por detrás del defensor
    p.body.append(f'<line x1="{p.X(31):.1f}" y1="{p.Y(60):.1f}" x2="{p.X(70):.1f}" '
                  f'y2="{p.Y(40):.1f}" stroke="#ffffff" stroke-width="2.6" '
                  f'stroke-dasharray="7 6" marker-end="url(#ah_run)"/>')
    txt(p, 56, 47, "línea libre", size=9, c="#ffffff", w=700)
    # entrenador señalando (icono) fuera del cuadro
    CX, CY = p.X(12), p.Y(78)
    p.body.append(f'<circle cx="{CX:.1f}" cy="{CY:.1f}" r="9" fill="#2b3a4a" stroke="#f7c948" stroke-width="2"/>')
    p.body.append(f'<text x="{CX:.1f}" y="{CY+4:.1f}" font-family="Segoe UI,Arial" font-size="11" '
                  f'font-weight="800" fill="#f7c948" text-anchor="middle">T</text>')
    # bocadillo de pregunta
    bx0, by0 = 22, 86
    panel(p, bx0, by0, bx0 + 56, by0 - 8, fill="#15202b", op=0.92, stroke=GOLD, sw=1.6, rx=8)
    txt(p, bx0 + 28, by0 - 3.0, "¿Tenías al hombre libre detrás del defensor?",
        size=9.6, c="#fff5cc", w=700)
    # FREEZE label
    panel(p, 78, 86, 94, 80, fill="#c62828", op=0.9, stroke="#fff", sw=1.4, rx=6)
    txt(p, 86, 82.6, "FREEZE", size=11, c="#fff", w=800)
    p.note(50, 28, "Observa 2–3 vueltas · pregunta antes que decir · un foco por serie", size=9.4)
    p.legend(["pass", "run", "own", "rival"])
    p.save(f"{G}/teoria-07-coaching-freeze.svg")

# ======================================================================
# 08 — CADENA DE TRANSFERENCIA (4 escalones encadenados)
# ======================================================================
def t08():
    p = Pitch(title="La cadena de transferencia",
              subtitle="rondo → juego de posición → partido condicionado → competición", half=None)
    steps = [
        ("RONDO", "el principio puro", PALETTE["own"], 80),
        ("JUEGO DE\nPOSICIÓN", "+ porterías / dirección", PALETTE["neutral"], 67),
        ("PARTIDO\nCONDICIONADO", "+ reglas del modelo", "#d77a1e", 54),
        ("COMPETICIÓN", "+ rival real", PALETTE["rival"], 41),
    ]
    # escalones ascendentes (cada uno un peldaño más alto y a la derecha)
    bw, bh = 18, 9
    xs = [18, 39, 60, 81]
    prev = None
    for (name, sub, col, _), x in zip(steps, xs):
        # altura del peldaño crece
        y = 38 + xs.index(x) * 9
        chip(p, x - bw / 2, y + bh / 2, x + bw / 2, y - bh / 2, col, op=0.92, stroke="#ffffff", sw=1.5)
        lines = name.split("\n")
        ly = y + (2.5 if len(lines) == 1 else 5)
        for ln in lines:
            txt(p, x, ly, ln, size=9.6, c="#fff", w=800)
            ly -= 6
        txt(p, x, y - bh / 2 - 3, sub, size=8, c="#cfe0ee", w=600)
        if prev:
            bigarrow(p, prev[0] + bw / 2 - 1, prev[1] + 1, x - bw / 2 + 1, y - 1, c=GOLD, w=3.6, mk="ah_pass")
        prev = (x, y)
    # roles bajo cada uno
    txt(p, 50, 30, "aísla  →  orienta  →  integra  →  valida", size=10.5, c=GOLD, w=800)
    p.note(50, 24, "Saltar del rondo al partido deja un hueco de transferencia", size=9.5)
    p.save(f"{G}/teoria-08-cadena-transferencia.svg")

# ======================================================================
# 09 — FAMILIAS Y PRINCIPIOS (mapa de las 7 familias)
# ======================================================================
def t09():
    p = Pitch(title="Las 7 familias y sus principios",
              subtitle="elige la familia por el principio del modelo que toque", half=None)
    fams = [
        ("1 · Iniciación / mantenimiento", "conservación, apoyos, 1.er toque", "Posesión segura", PALETTE["own"]),
        ("2 · Presión y recuperación", "presión tras pérdida, coberturas", "Transición defensiva", PALETTE["rival"]),
        ("3 · Posicional / orientación", "cambio de orientación, escaneo", "Cambiar el punto de juego", "#1f7ab8"),
        ("4 · Líneas y comodines", "progresión, tercer hombre, entre líneas", "Romper líneas / progresar", PALETTE["neutral"]),
        ("5 · Finalización", "última pasada, llegada, definición", "Convertir en gol", "#d77a1e"),
        ("6 · Competitivos / condicionados", "dos fases con marcador, decisión", "Lo más cercano al partido", "#8e44ad"),
        ("7 · Lúdicos / calentamiento", "activación, ritmo, cohesión", "Preparar cuerpo y ojo", "#2e9e6b"),
    ]
    yt, yb = 84, 12
    n = len(fams)
    rowh = (yt - yb) / n
    for i, (name, princ, conx, col) in enumerate(fams):
        cyy = yt - rowh * (i + 0.5)
        # banda de fila
        panel(p, 6, cyy + rowh * 0.42, 94, cyy - rowh * 0.42, fill="#10202e", op=0.55, stroke="#2a3a4a", sw=1, rx=6)
        # marcador de familia (color)
        chip(p, 7, cyy + rowh * 0.34, 36, cyy - rowh * 0.34, col, op=0.9, rx=6)
        txt(p, 21.5, cyy + 1.0, name, size=8.8, c="#fff", w=800)
        # principio
        txt(p, 53, cyy + 1.0, princ, size=8.4, c="#dfe9f2", w=600)
        # flecha a conexión
        chevron(p, 71, cyy, w=3, c=GOLD)
        # conexión con el partido
        chip(p, 73, cyy + rowh * 0.34, 93.5, cyy - rowh * 0.34, "#1c2c3a", op=0.9, stroke=GOLD, sw=1, rx=6)
        txt(p, 83.2, cyy + 1.0, conx, size=8.0, c="#fff5cc", w=700)
    # cabeceras
    txt(p, 21.5, 87.5, "FAMILIA", size=9, c="#9fb3c8", w=800)
    txt(p, 53, 87.5, "PRINCIPIOS QUE ENTRENA", size=9, c="#9fb3c8", w=800)
    txt(p, 83.2, 87.5, "FASE DEL PARTIDO", size=9, c="#9fb3c8", w=800)
    p.save(f"{G}/teoria-09-familias-principios.svg")

# ======================================================================
# 10 — MICROCICLO (línea de semana + curva de carga)
# ======================================================================
def t10():
    p = Pitch(title="El rondo en el microciclo (MD)",
              subtitle="el principio es constante; el tipo de rondo cambia según el día", half=None)
    days = [
        ("MD+2", "Recuperación", 22, "Lúdico 7v2", "F7/1"),
        ("MD-4", "Fuerza", 68, "Reducido, presión", "F1/2"),
        ("MD-3", "Duración", 78, "Posicional/progresión", "F3/4"),
        ("MD-2", "Velocidad", 55, "Competitivo/finaliz.", "F5/6"),
        ("MD-1", "Activación", 30, "Mantenimiento", "F1/7"),
        ("MD", "Partido", 20, "Calentamiento", "F7"),
    ]
    xs = [12, 28, 44, 60, 76, 90]
    # curva de carga (área bajo línea)
    pts = []
    for (d, foco, carga, rec, fam), x in zip(days, xs):
        y = 40 + (carga / 100.0) * 36   # carga 0..100 -> y 40..76
        pts.append((x, y))
    # área
    area = f'M{p.X(xs[0]):.1f},{p.Y(40):.1f} '
    for x, y in pts:
        area += f'L{p.X(x):.1f},{p.Y(y):.1f} '
    area += f'L{p.X(xs[-1]):.1f},{p.Y(40):.1f} Z'
    p.body.append(f'<path d="{area}" fill="{GOLD}" fill-opacity="0.16" stroke="none"/>')
    # línea de carga
    line = "M" + " L".join(f'{p.X(x):.1f},{p.Y(y):.1f}' for x, y in pts)
    p.body.append(f'<path d="{line}" fill="none" stroke="{GOLD}" stroke-width="3.2"/>')
    for x, y in pts:
        p.body.append(f'<circle cx="{p.X(x):.1f}" cy="{p.Y(y):.1f}" r="3.4" fill="{GOLD}" stroke="#7a5a00" stroke-width="1"/>')
    # línea base de semana
    p._line(p.X(8), p.Y(40), p.X(94), p.Y(40), w=2, c="#9fb3c8", opacity=0.7)
    txt(p, 50, 79.5, "CURVA DE CARGA — sube al pico (MD-4/MD-3) y baja hacia el partido", size=9.6, c="#fff5cc", w=700)
    # etiquetas de día + recomendación
    for (d, foco, carga, rec, fam), x in zip(days, xs):
        col = PALETTE["rival"] if d == "MD" else PALETTE["own"]
        chip(p, x - 6, 38, x + 6, 33, col, op=0.92, stroke="#ffffff", sw=1.3, rx=5)
        txt(p, x, 34.8, d, size=9.2, c="#fff", w=800)
        txt(p, x, 30.5, foco, size=7.6, c="#cfe0ee", w=700)
        # caja de rondo recomendado
        panel(p, x - 7, 27, x + 7, 16, fill="#10202e", op=0.6, stroke="#2a3a4a", sw=1, rx=5)
        # texto envuelto simple
        words = rec.split()
        # partir en 2 líneas
        if len(words) > 1:
            l1 = words[0]; l2 = " ".join(words[1:])
        else:
            l1 = rec; l2 = ""
        txt(p, x, 24, l1, size=7.4, c="#dfe9f2", w=600)
        if l2:
            txt(p, x, 20.5, l2, size=7.4, c="#dfe9f2", w=600)
        txt(p, x, 17.5, fam, size=8, c=GOLD, w=800)
    txt(p, 50, 12, "El rondo de MD-1 es el termómetro de frescura del equipo", size=9.5, c="#cfe0ee", w=700)
    p.save(f"{G}/teoria-10-microciclo.svg")


if __name__ == "__main__":
    import os
    os.chdir('/home/user/mister-elite-app/curso-rondos')
    t01(); t02(); t03(); t04(); t05(); t06(); t07(); t08(); t09(); t10()
    print("OK - 10 diagramas generados")
