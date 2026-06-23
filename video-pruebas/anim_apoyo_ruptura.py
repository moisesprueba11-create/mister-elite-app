#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prueba de animación por código (NO IA de vídeo): automatismo apoyo + ruptura.
Interpola posiciones de fichas y balón fotograma a fotograma, renderiza cada
frame con el motor pitch.py (cairosvg -> PNG) y monta GIF + MP4.
"""
import os, sys, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from pitch import Pitch
import cairosvg
from PIL import Image
import imageio.v2 as imageio
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
W = 560

def clamp01(t): return max(0.0, min(1.0, t))
def ss(t):  # smoothstep easing
    t = clamp01(t); return t * t * (3 - 2 * t)
def seg(f, f0, f1):  # progreso suavizado en [f0,f1]
    return ss((f - f0) / (f1 - f0)) if f1 > f0 else 1.0
def lerp(a, b, t): return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

# --- guion temporal (fps=12) ---
FPS = 12
A = 24   # fin fase 1 (apoyo baja / arrastra)
B = 42   # fin fase 2 (pase + ruptura)
T = 58   # total frames

# posiciones clave (coords campo, half='att': y 50..100 visible; ataque ARRIBA)
MC      = (52, 55)                       # poseedor, fijo
APOYO0, APOYO1 = (40, 79), (37, 67)      # baja a recibir
DF1_0,  DF1_1  = (42, 86), (44, 73)      # central que sigue al apoyo
RUP0,   RUP1   = (66, 79), (47, 91)      # ataca el espacio
DF2     = (67, 86)                       # central del que rompe
BALL0,  BALL1  = (52, 58), (47, 89)      # balón: con MC -> al espacio

def frame(f):
    cap = ("1 · el apoyo BAJA y arrastra a su central" if f < A else
           "2 · PASE al espacio + RUPTURA a la espalda" if f < B else
           "3 · recibe a la espalda del central")
    p = Pitch(title="Automatismo: apoyo + ruptura",
              subtitle="MISTER ÉLITE · prueba de pizarra animada",
              half="att", attack_arrow=False)
    # zona "espacio a la espalda" aparece al final de la fase 1
    op = 0.10 + 0.12 * seg(f, A - 6, B)
    p.zone(24, 82, 56, 96, label="espacio a la espalda", c="#7ee0ff", fill_op=op)
    # posiciones interpoladas
    apoyo = lerp(APOYO0, APOYO1, seg(f, 0, A))
    df1   = lerp(DF1_0,  DF1_1,  seg(f, 0, A))
    rup   = lerp(RUP0,   RUP1,   seg(f, A, B))
    ball  = lerp(BALL0,  BALL1,  seg(f, A, B))
    # fichas
    p.player(*MC,  "MC",  team="own", role="con balón")
    p.player(*apoyo, "DC", team="own", role="apoyo", role_below=True)
    p.player(*rup,   "DC", team="own", role="ruptura", role_below=True)
    p.player(*df1, "DFC", team="rival")
    p.player(*df2_pos(), "DFC", team="rival")
    p.ball(*ball)
    # caption inferior
    p.note(50, 52, cap, c="#fff5cc", size=11)
    svg = p.svg()
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=W)
    return Image.open(io.BytesIO(png)).convert("RGB")

def df2_pos(): return DF2

def main():
    frames = [frame(f) for f in range(T)]
    # GIF (pausa final más larga)
    durs = [1.0 / FPS] * T
    durs[-1] = 1.2
    gif = os.path.join(OUT, "apoyo-ruptura.gif")
    frames[0].save(gif, save_all=True, append_images=frames[1:],
                   duration=[int(d * 1000) for d in durs], loop=0, optimize=True)
    # MP4
    mp4 = os.path.join(OUT, "apoyo-ruptura.mp4")
    w = imageio.get_writer(mp4, fps=FPS, codec="libx264", quality=8,
                           macro_block_size=None)
    for im in frames: w.append_data(np.asarray(im))
    for _ in range(int(FPS * 1.2)): w.append_data(np.asarray(frames[-1]))
    w.close()
    # stills de muestra
    for fr, name in [(8, "fase1"), (34, "fase2"), (T - 1, "fase3")]:
        frame(fr).save(os.path.join(OUT, f"still-{name}.png"))
    print("OK:", gif, os.path.getsize(gif)//1024, "KB |", mp4, os.path.getsize(mp4)//1024, "KB")

if __name__ == "__main__":
    main()
