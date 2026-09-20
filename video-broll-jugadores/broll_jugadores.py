#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
broll_jugadores.py — B-roll MISTER ELITE: los cuatro jugadores van apareciendo
de uno en uno sobre el campo y se quedan, lo mas grandes que caben sin solaparse
ni salirse de cuadro.

  - Vertical 1080x1920: rejilla 2x2.
  - Horizontal 1920x1080: los cuatro en linea.

Cada jugador entra con un pequeno impulso hacia arriba + fundido, y se queda en
su sitio. El ritmo deja un hueco por jugador para nombrarlo en la locucion.

Uso:
    python3 broll_jugadores.py                       # vertical
    python3 broll_jugadores.py --formato h           # horizontal
    python3 broll_jugadores.py --paso 1.6            # mas tiempo por jugador
    python3 broll_jugadores.py --nombres "A,B,C,D"   # con rotulo de nombre
    python3 broll_jugadores.py --escala 0.35 --fps 12  # prueba rapida
"""
import argparse, glob, math, os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import imageio.v2 as imageio

BASE = os.path.dirname(os.path.abspath(__file__))
CAMPO = os.path.join(BASE, "assets", "campo.jpg")

FUENTES = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
           "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]

# ---------------------------------------------------------------- easings ---
def clamp01(t):
    return max(0.0, min(1.0, t))

def ease_out_cubic(t):
    return 1 - (1 - clamp01(t)) ** 3

def smoothstep(t):
    t = clamp01(t)
    return t * t * (3 - 2 * t)

def lerp(a, b, t):
    return a + (b - a) * t

# ------------------------------------------------------------------ campo ---
def cargar_campo(W, H, sobremuestreo=1.45):
    im = Image.open(CAMPO).convert("RGB")
    esc = max(W / im.width, H / im.height) * sobremuestreo
    return im.resize((int(im.width * esc), int(im.height * esc)), Image.LANCZOS)

def frame_campo(campo, W, H, zoom, desenfoque, oscuridad):
    cw, ch = min(int(W * zoom), campo.width), min(int(H * zoom), campo.height)
    x0, y0 = (campo.width - cw) // 2, (campo.height - ch) // 2
    rec = campo.crop((x0, y0, x0 + cw, y0 + ch))
    if desenfoque > 0.35:
        chico = rec.resize((max(1, cw // 2), max(1, ch // 2)), Image.BILINEAR)
        chico = chico.filter(ImageFilter.GaussianBlur(desenfoque * cw / W / 2))
        rec = chico.resize((W, H), Image.BILINEAR)
    else:
        rec = rec.resize((W, H), Image.LANCZOS)
    if oscuridad > 0.001:
        rec = Image.fromarray((np.asarray(rec, np.float32) * (1 - oscuridad)).astype(np.uint8), "RGB")
    return rec

def vineta(W, H, fuerza=0.34):
    ys, xs = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xs - W / 2) / (W / 2)) ** 2 + ((ys - H / 2) / (H / 2)) ** 2) / math.sqrt(2)
    return (np.clip((r - 0.35) / 0.65, 0, 1) ** 1.8 * fuerza)[:, :, None].astype(np.float32)

# -------------------------------------------------------------- jugadores ---
def cargar_jugadores():
    rutas = sorted(glob.glob(os.path.join(BASE, "assets", "jugador-*.png")))
    if not rutas:
        raise SystemExit("No hay recortes en assets/. Ejecuta antes preparar_recortes.py")
    return [Image.open(r).convert("RGBA") for r in rutas]

def difuminar_base(im, frac=0.11):
    """Las fotos estan cortadas por la cintura: se difumina el corte inferior
    para que no quede una linea recta flotando sobre el cesped."""
    a = np.asarray(im.split()[-1], np.float32)
    h = im.height
    n = max(1, int(h * frac))
    rampa = np.ones(h, np.float32)
    rampa[h - n:] = np.linspace(1.0, 0.0, n) ** 1.3
    a *= rampa[:, None]
    rgba = np.asarray(im).copy()
    rgba[..., 3] = a.astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")

def sombra_de(im, desenfoque, opacidad):
    alfa = im.split()[-1].filter(ImageFilter.GaussianBlur(desenfoque))
    alfa = alfa.point(lambda v: int(v * opacidad / 255))
    s = Image.new("RGBA", im.size, (0, 0, 0, 0))
    s.putalpha(alfa)
    return s

# ----------------------------------------------------------------- rotulo ---
def fuente(px):
    for f in FUENTES:
        if os.path.exists(f):
            return ImageFont.truetype(f, px)
    return ImageFont.load_default()

def rotulo(texto, ancho, alto_txt):
    """Placa con el nombre, en la linea grafica de la marca."""
    f = fuente(alto_txt)
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    caja = tmp.textbbox((0, 0), texto.upper(), font=f)
    tw, th = caja[2] - caja[0], caja[3] - caja[1]
    pad_x, pad_y = int(alto_txt * 0.7), int(alto_txt * 0.42)
    w, h = min(ancho, tw + pad_x * 2), th + pad_y * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=(14, 26, 38, 225))
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, outline=(255, 213, 74, 235), width=max(2, h // 22))
    d.text(((w - tw) / 2 - caja[0], (h - th) / 2 - caja[1]), texto.upper(),
           font=f, fill=(255, 255, 255, 255))
    return im

# ----------------------------------------------------------------- monta ----
def plantilla(formato, W, H, jugadores):
    """Devuelve (ancho, alto, x, y) de cada jugador: lo mas grande posible sin
    solaparse entre ellos ni salirse del cuadro."""
    cols, filas = (2, 2) if formato == "v" else (4, 1)
    ranura_w, ranura_h = W / cols, H / filas
    aspectos = [im.width / im.height for im in jugadores]

    # Misma altura para todos (lectura de alineacion), limitada por el ancho de
    # ranura del mas ancho y por el alto disponible.
    alto = min(0.97 * ranura_w / max(aspectos), 0.90 * ranura_h)
    hueco = alto * 0.05 if filas > 1 else 0
    bloque = filas * alto + hueco * (filas - 1)
    y0 = (H - bloque) / 2 + (H * 0.02)                 # ligeramente hacia abajo

    sitios = []
    for i, asp in enumerate(aspectos):
        c, fl = i % cols, i // cols
        w = alto * asp
        x = ranura_w * (c + 0.5) - w / 2
        y = y0 + fl * (alto + hueco)
        sitios.append((int(w), int(alto), int(x), int(y)))
    return sitios

def render(formato="v", dur=None, fps=30, paso=1.35, entrada=0.45, nombres=None,
           escala=1.0, salida=None):
    W, H = (1080, 1920) if formato == "v" else (1920, 1080)
    W, H = int(W * escala) // 2 * 2, int(H * escala) // 2 * 2   # yuv420p exige pares

    jugadores = cargar_jugadores()
    sitios = plantilla(formato, W, H, jugadores)

    T0 = 0.35                                           # campo solo, al arrancar
    COLA = 2.1                                          # ultimo plano con los cuatro
    if dur is None:
        dur = T0 + paso * len(jugadores) + COLA
    total = int(round(dur * fps))

    # Cache: figura, sombra y rotulo ya a tamano final.
    fijos = []
    for im, (w, h, x, y) in zip(jugadores, sitios):
        fig = difuminar_base(im).resize((w, h), Image.LANCZOS)
        fijos.append(dict(fig=fig, sombra=sombra_de(fig, max(6, int(h * 0.018)), 135)))
    if nombres:
        for d, n, (w, h, x, y) in zip(fijos, nombres, sitios):
            d["rotulo"] = rotulo(n, int(w * 1.25), max(16, int(h * 0.075)))

    campo = cargar_campo(W, H)
    mask_vineta = vineta(W, H)
    frames = []

    for f in range(total):
        t = f / max(1, total - 1)
        seg = t * dur                                    # tiempo en segundos

        # Fondo: push-in continuo; se desenfoca y oscurece segun entran jugadores
        entrados = clamp01((seg - T0) / (paso * len(jugadores)))
        fondo = frame_campo(campo, W, H, lerp(1.42, 1.26, smoothstep(t)),
                            lerp(0.0, 3.2, entrados), lerp(0.0, 0.13, entrados))
        arr = np.asarray(fondo, np.float32) * (1 - mask_vineta * lerp(0.45, 0.80, smoothstep(t)))
        lienzo = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB").convert("RGBA")

        for i, (d, (w, h, x, y)) in enumerate(zip(fijos, sitios)):
            p = clamp01((seg - (T0 + i * paso)) / entrada)
            if p <= 0:
                continue
            e = ease_out_cubic(p)
            dy = int((1 - e) * h * 0.10)                 # pequeno impulso hacia arriba
            op = smoothstep(p)

            capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            capa.alpha_composite(d["sombra"], (x, y + dy + int(h * 0.01)))
            capa.alpha_composite(d["fig"], (x, y + dy))
            if "rotulo" in d:
                r = d["rotulo"]
                ry = min(H - r.height - 6, y + h - r.height // 2 + dy)
                capa.alpha_composite(r, (x + (w - r.width) // 2, ry))

            if op < 0.999:                               # fundido de entrada
                a = np.asarray(capa, np.float32)
                a[..., 3] *= op
                capa = Image.fromarray(a.astype(np.uint8), "RGBA")
            lienzo = Image.alpha_composite(lienzo, capa)

        img = lienzo.convert("RGB")
        fade = min(smoothstep(clamp01(t / 0.04)), smoothstep(clamp01((1 - t) / 0.05)))
        if fade < 0.999:
            img = Image.fromarray((np.asarray(img, np.float32) * fade).astype(np.uint8), "RGB")
        frames.append(np.asarray(img))
        if (f + 1) % 30 == 0 or f == total - 1:
            print("  frame %d/%d" % (f + 1, total), flush=True)

    if salida is None:
        salida = os.path.join(BASE, "broll-jugadores%s.mp4" % ("" if formato == "v" else "-horizontal"))
    imageio.mimwrite(salida, frames, fps=fps, codec="libx264", macro_block_size=1,
                     output_params=["-crf", "19", "-preset", "slow", "-pix_fmt", "yuv420p",
                                    "-profile:v", "high", "-movflags", "+faststart"])
    print("OK ->", salida, "| %.2f s" % dur)

    still = os.path.splitext(salida)[0] + "-still.png"
    Image.fromarray(frames[int(total * 0.93)]).save(still)
    print("OK ->", still)
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--formato", default="v", choices=["v", "h"])
    ap.add_argument("--paso", type=float, default=1.35, help="segundos entre jugador y jugador")
    ap.add_argument("--entrada", type=float, default=0.45, help="duracion de la aparicion")
    ap.add_argument("--dur", type=float, default=None, help="forzar duracion total")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--nombres", default=None, help='rotulos, p. ej. "Nombre1,Nombre2,Nombre3,Nombre4"')
    ap.add_argument("--escala", type=float, default=1.0)
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    render(a.formato, a.dur, a.fps, a.paso, a.entrada,
           a.nombres.split(",") if a.nombres else None, a.escala, a.salida)
