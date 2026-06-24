#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prueba 2 de pizarra animada por código: RONDO 5 v 2.
El balón circula entre 5 poseedores (azul); 2 defensores (rojo) persiguen.
La flecha del pase aparece en cada acción. Salida GIF + MP4.
"""
import os, sys, io, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from pitch import Pitch
import cairosvg
from PIL import Image
import imageio.v2 as imageio
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__)); W = 560; FPS = 12

def clamp01(t): return max(0.0, min(1.0, t))
def ss(t): t = clamp01(t); return t * t * (3 - 2 * t)
def lerp(a, b, t): return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

# 5 poseedores alrededor de un cuadro (centro ~50,50)
P = [(30, 38), (50, 31), (70, 38), (63, 66), (37, 66)]
CONES = [(27, 33), (73, 33), (73, 71), (27, 71)]
# orden de pases (índices de P) — circula y cambia de orientación
ORDER = [0, 1, 2, 3, 4, 2, 0, 3, 1, 4, 0]
SEG = 7          # frames por pase
HOLD = 2         # frames de pausa al recibir
PER = SEG + HOLD
T = PER * (len(ORDER) - 1)

def ball_and_pass(f):
    i = min(f // PER, len(ORDER) - 2)
    local = f - i * PER
    a, b = P[ORDER[i]], P[ORDER[i + 1]]
    if local < SEG:
        t = ss(local / SEG); moving = True
    else:
        t = 1.0; moving = False
    return lerp(a, b, t), (a, b, moving), ORDER[i + 1]

def frame(f, d1, d2):
    ball, (pa, pb, moving), holder_idx = ball_and_pass(f)
    p = Pitch(title="Rondo 5 v 2", subtitle="MISTER ÉLITE · conservar y cambiar de orientación",
              half=None, attack_arrow=False)
    p.zone(27, 33, 73, 71, label="", c="#ffd54a", fill_op=0.08)
    for c in CONES: p.cone(*c)
    # flecha del pase en curso
    if moving:
        p.arrow(pa[0], pa[1], pb[0], pb[1], kind="pass")
    # poseedores (resalta al que tiene/va a recibir el balón)
    for idx, pos in enumerate(P):
        role = "" if idx != holder_idx else "recibe"
        p.player(pos[0], pos[1], f"P{idx+1}", team="own", role=role)
    # defensores
    p.player(d1[0], d1[1], "D", team="rival")
    p.player(d2[0], d2[1], "D", team="rival")
    p.ball(ball[0], ball[1])
    svg = p.svg()
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=W)
    return Image.open(io.BytesIO(png)).convert("RGB")

def main():
    # defensores con persecución suavizada (estado entre frames)
    d1 = [42.0, 45.0]; d2 = [58.0, 55.0]
    frames = []
    for f in range(T):
        ball, (pa, pb, moving), holder_idx = ball_and_pass(f)
        # D1 presiona el balón; D2 cubre hacia el centro del rondo (separado de D1)
        cover = ((ball[0] + 50) / 2, (ball[1] + 50) / 2)
        for d, tgt, k in ((d1, ball, 0.18), (d2, cover, 0.10)):
            d[0] += (tgt[0] - d[0]) * k; d[1] += (tgt[1] - d[1]) * k
        frames.append(frame(f, tuple(d1), tuple(d2)))
    durs = [int(1000 / FPS)] * T; durs[-1] = 900
    gif = os.path.join(OUT, "rondo-5v2.gif")
    frames[0].save(gif, save_all=True, append_images=frames[1:], duration=durs, loop=0, optimize=True)
    mp4 = os.path.join(OUT, "rondo-5v2.mp4")
    w = imageio.get_writer(mp4, fps=FPS, codec="libx264", quality=8, macro_block_size=None)
    for im in frames: w.append_data(np.asarray(im))
    w.close()
    frames[len(frames)//2].save(os.path.join(OUT, "still-rondo.png"))
    print("OK:", gif, os.path.getsize(gif)//1024, "KB |", mp4, os.path.getsize(mp4)//1024, "KB")

if __name__ == "__main__":
    main()
