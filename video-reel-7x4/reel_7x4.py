#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reel_7x4.py — Reel vertical (1080x1920, 30 fps, 20 s) del JUEGO DE POSICIÓN 7x4
para MISTER ÉLITE — Moisés Díaz.

Estructura:
  · 0–15 s  explicación animada (montaje, posiciones, salida de balón +
            mantenimiento, pérdida y presión tras pérdida)
  · 15–20 s cierre de marca (CTA)

Los tiempos de la animación están clavados a las marcas de palabra de la
locución (`audio/guion.json`), de modo que texto en pantalla y voz van juntos.

Uso:  python3 reel_7x4.py            -> reel-7x4.mp4 (sin audio) + portada
"""
import os, sys, math

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))

from board import (Board, W, H, FPS, YELLOW, WHITE, RED, BLUE, PANEL, MUTED,
                   ALERT, GRASS_DARK, seg, ss_ease, ease_out, lerp, lerp_p, clamp01)
from PIL import Image
import imageio.v2 as imageio
import numpy as np

DUR_EXP = 15.0          # explicación
DUR_CTA = 5.0           # cierre de marca
TOTAL = DUR_EXP + DUR_CTA
NFRAMES = int(round(TOTAL * FPS))

# ------------------------------------------------------------------ geometría
DY = 140                      # la pizarra baja 140 px: el rótulo va arriba (zona segura)
GX0, GX1 = 140, 940           # cuadrado de juego
GY0, GY1 = 500 + DY, 1420 + DY
GMX, GMY = (GX0 + GX1) / 2, (GY0 + GY1) / 2        # líneas interiores (540, 960)
R_PL = 44                     # radio de jugador

# 7 atacantes: 2 centrales (salida), 2 laterales, 1 medio centro, 2 medias puntas
ATT = {
    "DFCI": (340, GY1), "DFCD": (740, GY1),
    "LATI": (GX0, GMY), "LATD": (GX1, GMY),
    "MC":   (GMX, GMY),
    "MPI":  (340, GY0), "MPD": (740, GY0),
}
ATT_ORDER = ["DFCI", "DFCD", "LATI", "LATD", "MC", "MPI", "MPD"]
# 4 defensores, uno por zona
DEF = {"Z1": (352, 748 + DY), "Z2": (726, 726 + DY),
       "Z3": (352, 1168 + DY), "Z4": (752, 1186 + DY)}
DEF_ORDER = ["Z2", "Z1", "Z4", "Z3"]

BRAND_TITLE = "JUEGO DE POSICIÓN  7 vs 4"
BRAND_SUB = "MISTER ÉLITE · Moisés Díaz"


def breathe(name, t, amp=5.0):
    """micro-movimiento para que la pizarra no parezca congelada"""
    h = sum(ord(c) for c in name)
    return (math.sin(t * 1.6 + h) * amp, math.cos(t * 1.9 + h * 0.7) * amp * 0.8)


def path(t, kfs):
    """kfs = [(t, x, y), ...] con easing suave"""
    if t <= kfs[0][0]:
        return (kfs[0][1], kfs[0][2])
    if t >= kfs[-1][0]:
        return (kfs[-1][1], kfs[-1][2])
    for i in range(len(kfs) - 1):
        t0, x0, y0 = kfs[i]
        t1, x1, y1 = kfs[i + 1]
        if t0 <= t <= t1:
            k = ss_ease((t - t0) / (t1 - t0))
            return (lerp(x0, x1, k), lerp(y0, y1, k))
    return (kfs[-1][1], kfs[-1][2])


# ------------------------------------------------------------------ guion (s)
# marcas de la locución (HeyGen, es-ES) — ver guion-locucion.md
T_RED_IN, T_BLU_IN = 1.15, 2.05
T_ZONES = 2.95
T_GOALS = 4.05
T_POS = [("LAT", 5.15), ("MC", 5.80), ("MP", 6.72)]
T_BUILD = 7.90
T_LOSS = 10.45
T_PRESS = 11.30
T_COUNT = 12.85
T_WIN = 14.25

# recorrido del balón (salida de balón -> mantenimiento)
BALL_KF = [
    (T_BUILD, *ATT["DFCI"]),
    (8.15, *ATT["DFCI"]), (8.50, *ATT["LATI"]),          # 1 central -> lateral
    (8.70, *ATT["LATI"]), (9.02, *ATT["MC"]),            # 2 lateral -> medio centro
    (9.24, *ATT["MC"]), (9.66, *ATT["MPD"]),             # 3 interior a media punta
    (9.92, *ATT["MPD"]), (10.34, *ATT["MPI"]),           # 4 cambio de orientación
    (10.46, *ATT["MPI"]),
    (10.56, 352, 548 + DY), (11.30, 452, 742 + DY), (11.75, 498, 826 + DY),  # roba el azul
    (14.25, 512, 842 + DY), (14.55, *ATT["MC"]),         # recuperación
]
PASSES = [(8.15, 8.50, ATT["DFCI"], ATT["LATI"]),
          (8.70, 9.02, ATT["LATI"], ATT["MC"]),
          (9.24, 9.66, ATT["MC"], ATT["MPD"]),
          (9.92, 10.34, ATT["MPD"], ATT["MPI"])]

# defensores que saltan a presionar durante la circulación
DEF_KF = {
    "Z1": [(0, *DEF["Z1"]), (8.5, *DEF["Z1"]), (9.0, 300, 880 + DY), (10.0, 336, 700 + DY),
           (10.5, 348, 556 + DY), (11.3, 452, 748 + DY), (11.75, 498, 832 + DY),
           (14.5, 520, 850 + DY)],
    "Z2": [(0, *DEF["Z2"]), (8.9, *DEF["Z2"]), (9.4, 640, 700 + DY), (9.9, 700, 592 + DY),
           (10.6, 726, 700 + DY), (12.2, 700, 760 + DY)],
    "Z3": [(0, *DEF["Z3"]), (8.2, *DEF["Z3"]), (8.7, 258, 1060 + DY), (9.6, 352, 1100 + DY),
           (11.6, 400, 1010 + DY)],
    "Z4": [(0, *DEF["Z4"]), (9.3, *DEF["Z4"]), (10.0, 690, 1060 + DY), (11.8, 660, 1000 + DY)],
}


def zone_rect(i):
    """i: 0=sup-izq 1=sup-der 2=inf-izq 3=inf-der"""
    x0 = GX0 if i in (0, 2) else GMX
    x1 = GMX if i in (0, 2) else GX1
    y0 = GY0 if i in (0, 1) else GMY
    y1 = GMY if i in (0, 1) else GY1
    return x0, y0, x1, y1


# ------------------------------------------------------------------ frames
def draw_explain(b, t, chrome=True):
    # ---- cuadrícula de zonas (se dibuja sola al principio)
    k = ease_out(seg(t, 0.25, 0.95))
    if k > 0:
        cx, cy = GMX, GMY
        x0 = lerp(cx, GX0, k); x1 = lerp(cx, GX1, k)
        y0 = lerp(cy, GY0, k); y1 = lerp(cy, GY1, k)
        b.rect(x0, y0, x1, y1, outline=YELLOW, w=7)
        b.line(x0, GMY, x1, GMY, c=YELLOW, w=7)
        b.line(GMX, y0, GMX, y1, c=YELLOW, w=7)

    # ---- flash de zonas 1..4
    for i in range(4):
        t0 = T_ZONES + i * 0.28
        a = seg(t, t0, t0 + 0.22) * (1 - seg(t, t0 + 0.55, t0 + 1.0))
        if a > 0.01:
            x0, y0, x1, y1 = zone_rect(i)
            b.rect(x0 + 6, y0 + 6, x1 - 6, y1 - 6,
                   fill=(YELLOW[0], YELLOW[1], YELLOW[2], int(52 * a)))
            cx = x0 + 122 if i in (0, 2) else x1 - 122
            cy = y0 + (70 if i in (0, 1) else 58)
            b.chip(cx, cy, f"ZONA {i + 1}", size=28, alpha=int(255 * a))

    # ---- porterías destacadas
    ag = seg(t, T_GOALS, T_GOALS + 0.25) * (1 - seg(t, T_GOALS + 0.7, T_GOALS + 1.15))
    if ag > 0.01:
        pulse = 1 + 0.06 * math.sin((t - T_GOALS) * 9)
        for gy, up in ((440, True), (1760, False)):
            b.rect(540 - 205 * pulse, gy - 62 if up else gy - 8,
                   540 + 205 * pulse, gy + 8 if up else gy + 62,
                   outline=(YELLOW[0], YELLOW[1], YELLOW[2], int(255 * ag)), w=6, radius=12)
        b.chip(838, 470, "PORTERÍA", size=26, alpha=int(255 * ag))
        b.chip(242, 1790, "PORTERÍA", size=26, alpha=int(255 * ag))

    # ---- pases (flecha viva mientras el balón vuela)
    for (t0, t1, p, q) in PASSES:
        if t0 <= t <= t1 + 0.35:
            k = clamp01((t - t0) / (t1 - t0))
            a = 1 - seg(t, t1 + 0.1, t1 + 0.35)
            tip = lerp_p(p, q, max(0.12, k))
            b.arrow(p[0], p[1], tip[0], tip[1], c=YELLOW, w=8, head=30,
                    dash=True, alpha=int(230 * a))

    # ---- destello en el receptor
    for (t0, t1, p, q) in PASSES:
        ar = seg(t, t1 - 0.06, t1 + 0.06) * (1 - seg(t, t1 + 0.18, t1 + 0.5))
        if ar > 0.01:
            b.ring(q[0], q[1], R_PL + 12 + 20 * (1 - ar), c=YELLOW, w=7,
                   alpha=int(230 * ar))

    # ---- presión tras pérdida: flechas rojas convergentes
    if T_PRESS <= t <= T_WIN + 0.2:
        bx, by = path(t, BALL_KF)
        a = seg(t, T_PRESS, T_PRESS + 0.3) * (1 - seg(t, T_WIN, T_WIN + 0.2))
        pulse = 0.5 + 0.5 * math.sin((t - T_PRESS) * 7)
        for key in ("MPI", "MC", "MPD"):
            px, py = ATT[key]
            dx, dy = bx - px, by - py
            L = math.hypot(dx, dy) or 1
            ux, uy = dx / L, dy / L
            b.arrow(px + ux * (R_PL + 14), py + uy * (R_PL + 14),
                    px + ux * (L - 62 - 10 * pulse), py + uy * (L - 62 - 10 * pulse),
                    c=(232, 70, 70), w=9, head=32, alpha=int(235 * a))

    # ---- jugadores
    for i, key in enumerate(ATT_ORDER):
        t0 = T_RED_IN + i * 0.095
        a = ease_out(seg(t, t0, t0 + 0.3))
        if a <= 0:
            continue
        x, y = ATT[key]
        ox, oy = breathe(key, t)
        r = R_PL * (0.55 + 0.45 * a) * (1 + 0.10 * math.sin(math.pi * min(1, seg(t, t0, t0 + 0.45))))
        b.disc(x + ox, y + oy, r, RED, alpha=int(255 * a))

    for i, key in enumerate(DEF_ORDER):
        t0 = T_BLU_IN + i * 0.105
        a = ease_out(seg(t, t0, t0 + 0.3))
        if a <= 0:
            continue
        x, y = path(t, DEF_KF[key])
        ox, oy = breathe(key, t)
        r = R_PL * (0.55 + 0.45 * a)
        b.disc(x + ox, y + oy, r, BLUE, alpha=int(255 * a))

    # ---- etiquetas de posición
    labels = [("LATI", "LATERAL", 150, 0, "LAT"), ("LATD", "LATERAL", -150, 0, "LAT"),
              ("MC", "MEDIO CENTRO", 0, 86, "MC"),
              ("MPI", "MEDIA PUNTA", 0, -80, "MP"), ("MPD", "MEDIA PUNTA", 0, -80, "MP"),
              ("DFCI", "CENTRAL", 0, 84, "DFC"), ("DFCD", "CENTRAL", 0, 84, "DFC")]
    for key, txt, dx, dy, grp in labels:
        t0 = {"LAT": T_POS[0][1], "MC": T_POS[1][1], "MP": T_POS[2][1],
              "DFC": T_BUILD - 0.25}[grp]
        a = ease_out(seg(t, t0, t0 + 0.28)) * (1 - seg(t, T_LOSS - 0.2, T_LOSS + 0.1))
        if a <= 0.01:
            continue
        x, y = ATT[key]
        b.chip(x + dx, y + dy, txt, size=27, alpha=int(245 * a))

    # ---- balón
    if t >= T_BUILD - 0.15:
        bx, by = path(t, BALL_KF)
        # cuenta atrás de los 5 segundos de presión
        if T_COUNT <= t <= T_WIN + 0.15:
            frac = 1 - seg(t, T_COUNT, T_WIN)
            b.arc_ring(bx, by, 62, frac, c=(255, 90, 90), w=11)
            b.chip(bx + 120, by - 78, f"{max(1, math.ceil(frac * 5))} s", size=34,
                   bg=(232, 70, 70), fg=WHITE)
        b.ball(bx, by, r=22)

    # ---- "RECUPERADA"
    aw = seg(t, T_WIN, T_WIN + 0.18) * (1 - seg(t, DUR_EXP - 0.3, DUR_EXP))
    if aw > 0.01:
        b.chip(GMX, 1660, "RECUPERADA  ·  seguimos jugando", size=36,
               bg=(46, 170, 80), fg=WHITE, alpha=int(255 * aw))

    # ---- cabecera, pies y rótulos
    if not chrome:
        return
    b.header(BRAND_TITLE, BRAND_SUB, alpha=int(255 * ease_out(seg(t, 0.0, 0.3))))

    caps = [(0.40, 4.95, "7 vs 4 · 4 zonas · 2 porterías",
             "un defensor en cada zona", YELLOW),
            (5.00, 7.85, "Laterales · Medio centro · Medias puntas",
             "cada uno, en su posición y su zona", YELLOW),
            (7.90, 10.40, "Salida de balón + mantenimiento",
             "fija, juega interior y cambia de orientación", YELLOW),
            (10.45, 11.28, "¡Pérdida!", "", ALERT),
            (11.30, 12.82, "Presión tras pérdida", "saltan los tres más cercanos", ALERT),
            (12.85, 14.95, "Recuperar en 5 segundos",
             "si no, repliego y me reorganizo", ALERT)]
    for (t0, t1, txt, sub, acc) in caps:
        a = ease_out(seg(t, t0, t0 + 0.18)) * (1 - seg(t, t1 - 0.14, t1))
        if a > 0.01:
            b.caption(txt, sub, accent=acc, alpha=int(255 * a))
    b.footer(alpha=int(255 * ease_out(seg(t, 0.2, 0.5))))


def draw_cta(b, t):
    """t medido desde el inicio del reel (15..20 s)."""
    u = t - DUR_EXP
    # oscurecido progresivo del campo
    a = ease_out(seg(u, 0.0, 0.45))
    b.rect(0, 0, W, H, fill=(6, 18, 30, int(242 * a)))
    b.rect(0, 0, W, 14, fill=(YELLOW[0], YELLOW[1], YELLOW[2], int(255 * a)))
    b.rect(0, H - 14, W, H, fill=(YELLOW[0], YELLOW[1], YELLOW[2], int(255 * a)))

    k = ease_out(seg(u, 0.15, 0.6))
    b.text(W / 2, 640, "MISTER ÉLITE", size=int(96 * (0.86 + 0.14 * k)),
           c=WHITE, alpha=int(255 * k))
    kw = ease_out(seg(u, 0.45, 0.95))
    if kw > 0:
        b.rect(W / 2 - 250 * kw, 716, W / 2 + 250 * kw, 726, fill=YELLOW, radius=5)
    b.text(W / 2, 790, "Moisés Díaz", size=50, c=YELLOW,
           alpha=int(255 * ease_out(seg(u, 0.55, 0.95))))

    chips = ["Juego de posición", "Rondos", "Sistemas de juego"]
    for i, c in enumerate(chips):
        ka = ease_out(seg(u, 0.95 + i * 0.16, 1.35 + i * 0.16))
        if ka <= 0.01:
            continue
        y = 930 + i * 96
        b.chip(W / 2, y - 18 * (1 - ka), c, size=40, bg=(20, 44, 68), fg=WHITE,
               pad=30, radius=20, alpha=int(255 * ka))

    kb = ease_out(seg(u, 1.75, 2.15))
    if kb > 0.01:
        pulse = 1 + 0.02 * math.sin(u * 6)
        bw, bh = 760 * pulse, 132
        b.rect(W / 2 - bw / 2, 1270, W / 2 + bw / 2, 1270 + bh,
               fill=(YELLOW[0], YELLOW[1], YELLOW[2], int(255 * kb)), radius=24)
        b.text(W / 2, 1270 + bh / 2, "CURSO COMPLETO", size=54, c=(12, 26, 40),
               alpha=int(255 * kb))
        b.text(W / 2, 1452, "PDF + web · del concepto al campo", size=38, c=MUTED,
               alpha=int(255 * ease_out(seg(u, 2.05, 2.45))))
    b.text(W / 2, 1650, "Guarda el reel y llévatelo al entrenamiento", size=36,
           c=(226, 236, 245), alpha=int(255 * ease_out(seg(u, 2.6, 3.0))))
    b.footer(alpha=int(255 * ease_out(seg(u, 0.3, 0.7))))


def frame(t, bg):
    b = Board(bg)
    if t < DUR_EXP:
        draw_explain(b, t)
    else:
        draw_explain(b, min(t, DUR_EXP - 0.001), chrome=False)
        draw_cta(b, t)
    return b.out()


def main():
    bg = Board.grass()
    out = os.path.join(HERE, "reel-7x4.mp4")
    wri = imageio.get_writer(out, fps=FPS, codec="libx264", quality=9,
                             macro_block_size=None, ffmpeg_params=["-pix_fmt", "yuv420p"])
    for i in range(NFRAMES):
        t = i / FPS
        im = frame(t, bg)
        wri.append_data(np.asarray(im))
        if i % 60 == 0:
            print(f"  frame {i}/{NFRAMES}  t={t:5.2f}s", flush=True)
    wri.close()
    # portada / miniatura
    frame(4.6, bg).save(os.path.join(HERE, "portada-7x4.png"))
    frame(17.6, bg).save(os.path.join(HERE, "cierre-7x4.png"))
    print("OK ->", out)


if __name__ == "__main__":
    main()
