#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
preparar_recortes.py — Normaliza las fotos de origen a recortes PNG con alfa limpio.

Las fotos de plantilla vienen con fondo oscuro o con un halo azul marino
semitransparente incrustado. Aqui se segmenta la figura (rembg / u2net_human_seg),
se rellenan los huecos que la segmentacion abre en el escudo o el patrocinador,
se limpia el borde y se recorta al contenido -> assets/jugador-N.png.

Solo hay que ejecutarlo si se cambian las fotos de origen:
    python3 preparar_recortes.py foto1.jpg foto2.png foto3.png foto4.jpg
"""
import os, sys

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
from rembg import remove, new_session

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")


def rellenar_huecos(alfa, rgb):
    """La segmentacion se come los logos circulares del pecho. Una zona
    transparente que no toca el borde de la imagen es candidata a hueco, pero
    solo se rellena si es clara (el logo): los huecos oscuros entre el brazo y
    el torso son fondo de verdad y deben seguir siendo transparentes."""
    fondo = alfa < 128
    etiquetas, n = ndimage.label(fondo)
    if n == 0:
        return alfa
    del_borde = np.unique(np.concatenate([etiquetas[0, :], etiquetas[-1, :],
                                          etiquetas[:, 0], etiquetas[:, -1]]))
    del_borde = set(int(v) for v in del_borde if v != 0)

    lum = rgb.mean(axis=2)
    relleno = np.zeros_like(fondo)
    for et in range(1, n + 1):
        if et in del_borde:
            continue
        m = etiquetas == et
        if lum[m].mean() > 70:                 # claro -> logo tapado por la mascara
            relleno |= m
    return np.where(relleno, 255, alfa).astype(np.uint8)


def limpiar_borde(rgb, alfa):
    """Erosiona 1 px de alfa y descontamina el color del borde con el color
    interior, para que no quede reborde del fondo original sobre el cesped."""
    a_im = Image.fromarray(alfa, "L").filter(ImageFilter.MinFilter(3))
    a_im = a_im.filter(ImageFilter.GaussianBlur(0.7))
    a_new = np.asarray(a_im, dtype=np.float32) / 255.0

    def _blur(arr, r):
        return np.asarray(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "L")
                          .filter(ImageFilter.GaussianBlur(r)), dtype=np.float32)

    nucleo = np.asarray(Image.fromarray(alfa, "L").filter(ImageFilter.MinFilter(9)),
                        dtype=np.float32) / 255.0          # solo pixeles bien interiores
    peso = _blur(nucleo * 255, 4.0) / 255.0 + 1e-4
    interior = np.stack([_blur(rgb[..., c] * nucleo, 4.0) / peso for c in range(3)], -1)
    mezcla = np.clip((0.99 - a_new) / 0.55, 0, 1)[..., None]
    rgb = rgb * (1 - mezcla) + interior * mezcla
    return np.dstack([np.clip(rgb, 0, 255), a_new * 255]).astype(np.uint8)


def recortar(origen, destino, sesion):
    original = Image.open(origen).convert("RGBA")
    # Sobre negro: asi el halo oscuro del PNG original se lee como fondo.
    plano = Image.new("RGBA", original.size, (0, 0, 0, 255))
    plano.alpha_composite(original)

    seg = remove(plano, session=sesion, alpha_matting=True,
                 alpha_matting_foreground_threshold=250,
                 alpha_matting_background_threshold=15,
                 alpha_matting_erode_size=8)

    # El color sale de la foto original: el estimado de rembg emborrona los logos.
    rgb = np.asarray(plano.convert("RGB"), dtype=np.float32)
    alfa = rellenar_huecos(np.asarray(seg)[..., 3], rgb)

    out = Image.fromarray(limpiar_borde(rgb, alfa), "RGBA")
    out = out.crop(out.split()[-1].getbbox())
    out.save(destino)
    print("OK ->", destino, out.size)


if __name__ == "__main__":
    fuentes = sys.argv[1:]
    if not fuentes:
        sys.exit("uso: preparar_recortes.py <foto1> <foto2> ...")
    os.makedirs(ASSETS, exist_ok=True)
    sesion = new_session("u2net_human_seg")
    for i, f in enumerate(fuentes, 1):
        recortar(f, os.path.join(ASSETS, "jugador-%d.png" % i), sesion)
