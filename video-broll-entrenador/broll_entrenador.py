#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
broll_entrenador.py — B-roll MISTER ELITE: el entrenador sube desde abajo sobre el
campo y queda centrado y protagonista.

Animacion:
  1. Establecimiento: solo el campo (push-in lento).
  2. Entrada: el entrenador sube desde fuera de cuadro (abajo) con ease-out.
  3. Protagonismo: el campo se desenfoca y oscurece; el entrenador queda centrado
     con micro-movimiento (respiracion + acercamiento sutil).

Uso:
    python3 broll_entrenador.py                 # vertical 1080x1920 (reel)
    python3 broll_entrenador.py --formato h     # horizontal 1920x1080
    python3 broll_entrenador.py --dur 10 --fps 30
"""
import argparse, math, os, sys

import numpy as np
from PIL import Image, ImageFilter
import imageio.v2 as imageio

BASE = os.path.dirname(os.path.abspath(__file__))
CAMPO = os.path.join(BASE, "assets", "campo.jpg")
ENTRENADOR = os.path.join(BASE, "assets", "entrenador.png")

# ---------------------------------------------------------------- easings ---
def clamp01(t):
    return max(0.0, min(1.0, t))

def ease_out_cubic(t):
    t = clamp01(t)
    return 1 - (1 - t) ** 3

def ease_out_quint(t):
    t = clamp01(t)
    return 1 - (1 - t) ** 5

def smoothstep(t):
    t = clamp01(t)
    return t * t * (3 - 2 * t)

def lerp(a, b, t):
    return a + (b - a) * t

# ------------------------------------------------------------------ campo ---
def cargar_campo(W, H, sobremuestreo=1.45):
    """Campo escalado a 'cover' con margen extra para el push-in."""
    im = Image.open(CAMPO).convert("RGB")
    esc = max(W / im.width, H / im.height) * sobremuestreo
    return im.resize((int(im.width * esc), int(im.height * esc)), Image.LANCZOS)

def frame_campo(campo, W, H, zoom, desenfoque, oscuridad):
    """Recorte centrado del campo con zoom, desenfoque progresivo y oscurecido."""
    cw, ch = int(W * zoom), int(H * zoom)
    cw, ch = min(cw, campo.width), min(ch, campo.height)
    x0, y0 = (campo.width - cw) // 2, (campo.height - ch) // 2
    rec = campo.crop((x0, y0, x0 + cw, y0 + ch))

    if desenfoque > 0.35:
        # Desenfocar a media resolucion: mismo resultado visual, mitad de coste.
        chico = rec.resize((max(1, cw // 2), max(1, ch // 2)), Image.BILINEAR)
        chico = chico.filter(ImageFilter.GaussianBlur(desenfoque * cw / W / 2))
        rec = chico.resize((W, H), Image.BILINEAR)
    else:
        rec = rec.resize((W, H), Image.LANCZOS)

    if oscuridad > 0.001:
        arr = np.asarray(rec, dtype=np.float32) * (1.0 - oscuridad)
        rec = Image.fromarray(arr.astype(np.uint8), "RGB")
    return rec

def vineta(W, H, fuerza=0.34):
    """Mascara de vineta (mas oscuro en los bordes) para centrar la mirada."""
    ys, xs = np.mgrid[0:H, 0:W]
    nx = (xs - W / 2) / (W / 2)
    ny = (ys - H / 2) / (H / 2)
    r = np.sqrt(nx * nx + ny * ny) / math.sqrt(2)
    m = np.clip((r - 0.35) / 0.65, 0, 1) ** 1.8 * fuerza
    return m[:, :, None].astype(np.float32)

# ------------------------------------------------------------- entrenador ---
def cargar_entrenador():
    """Recorta el sobrante transparente y limpia el halo claro del recorte."""
    im = Image.open(ENTRENADOR).convert("RGBA")
    im = im.crop(im.split()[-1].getbbox())

    rgb = np.asarray(im.convert("RGB"), dtype=np.float32)
    alfa = np.asarray(im.split()[-1], dtype=np.float32) / 255.0

    # El PNG trae un reborde claro del recorte: se come 1 px de alfa y se suaviza.
    a_im = Image.fromarray((alfa * 255).astype(np.uint8), "L")
    a_im = a_im.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    a_new = np.asarray(a_im, dtype=np.float32) / 255.0

    # Descontaminacion de color: el borde toma el color del interior, no del fondo.
    def _blur(arr, r):
        return np.asarray(
            Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "L")
                 .filter(ImageFilter.GaussianBlur(r)), dtype=np.float32)

    nucleo = np.asarray(
        Image.fromarray((alfa * 255).astype(np.uint8), "L").filter(ImageFilter.MinFilter(9)),
        dtype=np.float32) / 255.0                                 # solo pixeles bien interiores
    peso = _blur(nucleo * 255, 4.0) / 255.0 + 1e-4
    interior = np.stack([_blur(rgb[..., c] * nucleo, 4.0) / peso for c in range(3)], axis=-1)
    mezcla = np.clip((0.99 - a_new) / 0.55, 0, 1)[..., None]      # solo cerca del borde
    rgb = rgb * (1 - mezcla) + interior * mezcla

    out = np.dstack([np.clip(rgb, 0, 255), a_new * 255]).astype(np.uint8)
    return Image.fromarray(out, "RGBA")

def sombra_de(im, desenfoque=28, opacidad=150):
    """Silueta negra difuminada a partir del alfa: despega al sujeto del fondo."""
    alfa = im.split()[-1].filter(ImageFilter.GaussianBlur(desenfoque))
    alfa = alfa.point(lambda v: int(v * opacidad / 255))
    sombra = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sombra.putalpha(alfa)
    return sombra

# ------------------------------------------------------------------ clip ----
def render(formato="v", dur=8.0, fps=30, salida=None, escala=1.0):
    W, H = (1080, 1920) if formato == "v" else (1920, 1080)
    W, H = int(W * escala), int(H * escala)
    total = int(round(dur * fps))

    campo = cargar_campo(W, H)
    coach = cargar_entrenador()
    aspecto = coach.width / coach.height

    # Tamano final: protagonista, sin que los hombros se salgan de cuadro.
    if formato == "v":
        h_obj = min(0.72 * H, 0.98 * W / aspecto)
        recorte_inf = 0.03                    # se corta un poco por abajo
    else:
        h_obj = min(1.04 * H, 0.60 * W / aspecto)
        recorte_inf = 0.04
    h_fin = int(h_obj)
    w_fin = int(h_fin * aspecto)

    # Escala del plano: entra un pelin mas pequeno y "se acerca" al llegar.
    ESC_ENT, ESC_FIN, ESC_DERIVA = 0.90, 1.0, 1.035

    y_fin = H * (1 + recorte_inf) - h_fin     # y del borde superior al llegar
    cx = W // 2

    # Tiempos (en fraccion del clip)
    T_ESPERA, T_SUBIDA = 0.06, 0.40           # establecimiento / subida

    mask_vineta = vineta(W, H)
    fondo_prev = None
    frames = []

    for f in range(total):
        t = f / max(1, total - 1)

        # --- progreso de la entrada --------------------------------------
        p = clamp01((t - T_ESPERA) / T_SUBIDA)
        subida = ease_out_cubic(p)
        llegado = clamp01((t - (T_ESPERA + T_SUBIDA)) / max(1e-6, 1 - T_ESPERA - T_SUBIDA))

        # --- fondo --------------------------------------------------------
        zoom = lerp(1.42, 1.24, smoothstep(t))           # push-in continuo
        desenfoque = lerp(0.0, 4.0, ease_out_cubic(p * 0.9 + llegado * 0.1))
        oscuridad = lerp(0.0, 0.14, smoothstep(clamp01(p * 1.1)))
        fondo = frame_campo(campo, W, H, zoom, desenfoque, oscuridad)

        arr = np.asarray(fondo, dtype=np.float32)
        arr *= (1 - mask_vineta * lerp(0.45, 0.80, smoothstep(t)))

        # --- entrenador ----------------------------------------------------
        if p > 0:
            esc = lerp(ESC_ENT, ESC_FIN, ease_out_cubic(p))
            esc = lerp(esc, ESC_DERIVA, smoothstep(llegado)) if llegado > 0 else esc
            w = max(2, int(w_fin * esc))
            h = max(2, int(h_fin * esc))

            # Sube desde fuera de cuadro hasta su sitio + respiracion al posarse.
            y_ini = H + h * 0.04
            respira = math.sin(llegado * math.pi * 1.6) * h * 0.006 * smoothstep(llegado)
            y = lerp(y_ini, y_fin - (h - h_fin) * 0.5, subida) - respira
            x = cx - w // 2

            fondo = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

            figura = coach.resize((w, h), Image.LANCZOS)
            sombra = sombra_de(figura, desenfoque=max(8, int(h * 0.022)),
                               opacidad=int(165 * smoothstep(p)))
            capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            capa.alpha_composite(sombra, (int(x), int(y + h * 0.012)))
            capa.alpha_composite(figura, (int(x), int(y)))
            fondo = Image.alpha_composite(fondo.convert("RGBA"), capa).convert("RGB")
        else:
            fondo = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

        # Fundido de entrada y de salida, para encadenar el b-roll con otros planos.
        fade = min(smoothstep(clamp01(t / 0.05)), smoothstep(clamp01((1 - t) / 0.06)))
        if fade < 0.999:
            fondo = Image.fromarray(
                (np.asarray(fondo, dtype=np.float32) * fade).astype(np.uint8), "RGB")

        frames.append(np.asarray(fondo))
        fondo_prev = fondo
        if (f + 1) % 30 == 0 or f == total - 1:
            print(f"  frame {f + 1}/{total}", flush=True)

    if salida is None:
        salida = os.path.join(BASE, "broll-entrenador%s.mp4" % ("" if formato == "v" else "-horizontal"))
    imageio.mimwrite(salida, frames, fps=fps, codec="libx264", macro_block_size=1,
                     output_params=["-crf", "19", "-preset", "slow",
                                    "-pix_fmt", "yuv420p", "-profile:v", "high",
                                    "-movflags", "+faststart"])
    print("OK ->", salida)

    # Fotograma final como still (portada / miniatura).
    still = os.path.splitext(salida)[0] + "-still.png"
    Image.fromarray(frames[int(total * 0.82)]).save(still)
    print("OK ->", still)
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--formato", default="v", choices=["v", "h"],
                    help="v = vertical 1080x1920 (reel), h = horizontal 1920x1080")
    ap.add_argument("--dur", type=float, default=8.0, help="duracion en segundos")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--escala", type=float, default=1.0, help="factor de resolucion (pruebas rapidas)")
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    render(a.formato, a.dur, a.fps, a.salida, a.escala)
