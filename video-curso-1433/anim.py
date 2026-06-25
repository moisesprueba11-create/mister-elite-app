#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
anim.py — Motor de animación táctica por código (declarativo) sobre pitch.py.
Cada jugada se define como datos: actores con keyframes + balón + flechas + zonas + captions.
Renderiza GIF + MP4 y devuelve los frames (PIL) para montar un reel.
"""
import os, sys, io
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from pitch import Pitch
import cairosvg
from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio
import numpy as np

W = 600
FPS = 12

def clamp01(t): return max(0.0, min(1.0, t))
def ss(t): t = clamp01(t); return t * t * (3 - 2 * t)

class Actor:
    """label, team in own/rival/neutral; kfs=[(frame,x,y),...]; role opcional."""
    def __init__(self, label, team, kfs, role="", role_below=False):
        self.label, self.team, self.role, self.role_below = label, team, role, role_below
        self.kfs = sorted(kfs, key=lambda k: k[0])
    def pos(self, f):
        ks = self.kfs
        if f <= ks[0][0]: return (ks[0][1], ks[0][2])
        if f >= ks[-1][0]: return (ks[-1][1], ks[-1][2])
        for i in range(len(ks) - 1):
            f0, x0, y0 = ks[i]; f1, x1, y1 = ks[i + 1]
            if f0 <= f <= f1:
                t = ss((f - f0) / (f1 - f0))
                return (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)
        return (ks[-1][1], ks[-1][2])

def _xy(o, f):
    return o.pos(f) if isinstance(o, Actor) else (o[0], o[1])

class Scene:
    def __init__(self, title, subtitle, total, half=None, attack_arrow=False):
        self.title, self.subtitle, self.total = title, subtitle, total
        self.half, self.attack_arrow = half, attack_arrow
        self.actors, self.ball_kfs, self.arrows, self.zones, self.caps = [], [], [], [], []
    def actor(self, *a, **k): self.actors.append(Actor(*a, **k)); return self.actors[-1]
    def ball(self, kfs): self.ball_kfs = sorted(kfs, key=lambda k: k[0])
    def arrow(self, t0, t1, src, dst, kind="pass"): self.arrows.append((t0, t1, src, dst, kind))
    def zone(self, t0, t1, x1, y1, x2, y2, label="", c="#7ee0ff"): self.zones.append((t0, t1, x1, y1, x2, y2, label, c))
    def caption(self, t0, t1, text): self.caps.append((t0, t1, text))

    def _ball_pos(self, f):
        ks = self.ball_kfs
        if not ks: return None
        if f <= ks[0][0]: return (ks[0][1], ks[0][2])
        if f >= ks[-1][0]: return (ks[-1][1], ks[-1][2])
        for i in range(len(ks) - 1):
            f0, x0, y0 = ks[i]; f1, x1, y1 = ks[i + 1]
            if f0 <= f <= f1:
                t = ss((f - f0) / (f1 - f0)); return (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)
        return (ks[-1][1], ks[-1][2])

    def frame(self, f):
        p = Pitch(title=self.title, subtitle=self.subtitle, half=self.half, attack_arrow=self.attack_arrow)
        for (t0, t1, x1, y1, x2, y2, label, c) in self.zones:
            if t0 <= f <= t1:
                op = 0.10 + 0.12 * ss((f - t0) / max(1, (t1 - t0) * 0.3))
                p.zone(x1, y1, x2, y2, label=label, c=c, fill_op=min(op, 0.22))
        for (t0, t1, src, dst, kind) in self.arrows:
            if t0 <= f <= t1:
                a = _xy(src, t0); b = _xy(dst, t1); p.arrow(a[0], a[1], b[0], b[1], kind=kind)
        for ac in self.actors:
            x, y = ac.pos(f); p.player(x, y, ac.label, team=ac.team, role=ac.role, role_below=ac.role_below)
        bp = self._ball_pos(f)
        if bp: p.ball(bp[0], bp[1])
        for (t0, t1, text) in self.caps:
            if t0 <= f <= t1:
                yy = 52 if (self.half == "att") else 6
                p.note(50, yy, text, c="#fff5cc", size=11)
        png = cairosvg.svg2png(bytestring=p.svg().encode(), output_width=W)
        return Image.open(io.BytesIO(png)).convert("RGB")

    def render(self):
        return [self.frame(f) for f in range(self.total)]

def _even(im):
    """ffmpeg/yuv420p exige ancho y alto pares; rellena 1px si hace falta."""
    cw = im.width + (im.width % 2); ch = im.height + (im.height % 2)
    if (cw, ch) == im.size: return im
    canvas = Image.new("RGB", (cw, ch), (12, 27, 42)); canvas.paste(im, (0, 0)); return canvas

def save_clip(frames, path_noext, hold=12):
    durs = [int(1000 / FPS)] * len(frames); durs[-1] = 800
    frames[0].save(path_noext + ".gif", save_all=True, append_images=frames[1:],
                   duration=durs, loop=0, optimize=True)
    ef = [_even(im) for im in frames]
    w = imageio.get_writer(path_noext + ".mp4", fps=FPS, codec="libx264", quality=8, macro_block_size=None)
    for im in ef: w.append_data(np.asarray(im))
    for _ in range(hold): w.append_data(np.asarray(ef[-1]))
    w.close()

def title_card(big, small, n_frames=18, size=(W, None)):
    """Tarjeta de título estilo marca para separar jugadas en el reel."""
    # render por SVG para mantener estética
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 760" width="600" height="760" font-family="Segoe UI,Arial">
    <rect width="600" height="760" fill="#0c1b2a"/>
    <rect x="0" y="0" width="600" height="6" fill="#f7c948"/><rect x="0" y="754" width="600" height="6" fill="#f7c948"/>
    <text x="300" y="300" font-size="20" font-weight="700" fill="#7fd0ff" text-anchor="middle" letter-spacing="4">MISTER ÉLITE · 1-4-3-3</text>
    <text x="300" y="370" font-size="40" font-weight="900" fill="#ffffff" text-anchor="middle">{_esc(big)}</text>
    <text x="300" y="420" font-size="20" font-weight="600" fill="#f7c948" text-anchor="middle">{_esc(small)}</text>
    <text x="300" y="720" font-size="13" fill="#8aa0b6" text-anchor="middle">del concepto al campo · Moisés Díaz</text>
    </svg>'''
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=W)
    im = Image.open(io.BytesIO(png)).convert("RGB")
    return [im] * n_frames

def _esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _norm(im, cw, ch):
    """centra im en un lienzo cw x ch con fondo oscuro (frames de distinta altura)."""
    if im.size == (cw, ch): return im
    canvas = Image.new("RGB", (cw, ch), (12, 27, 42))
    x = (cw - im.width) // 2; y = (ch - im.height) // 2
    canvas.paste(im, (x, y)); return canvas

def build_reel(segments, path_noext):
    """segments = lista de listas de frames (tarjetas + jugadas) ya en orden."""
    flat = []
    for seg in segments: flat.extend(seg)
    cw = max(im.width for im in flat); ch = max(im.height for im in flat)
    # ffmpeg exige dimensiones pares
    cw += cw % 2; ch += ch % 2
    flat = [_norm(im, cw, ch) for im in flat]
    w = imageio.get_writer(path_noext + ".mp4", fps=FPS, codec="libx264", quality=8, macro_block_size=None)
    for im in flat: w.append_data(np.asarray(im))
    w.close()
    return len(flat), (cw, ch)
