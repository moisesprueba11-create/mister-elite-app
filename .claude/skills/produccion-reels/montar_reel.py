#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta un Reel vertical 1080x1920 (clips de anim.py + locución) con la marca MISTER ÉLITE.
Multiplataforma (Windows/Mac/Linux). Requiere ffmpeg en el PATH.

Uso:
  python montar_reel.py salida.mp4 locucion.mp3 clip1.mp4 [clip2.mp4 ...]
  python montar_reel.py --pendientes        # monta todo reels/pendientes/* con locucion.mp3
"""
import os, sys, shutil, subprocess, tempfile, glob

MARCA = "MISTER ÉLITE"   # NUNCA el nombre personal en contenido público
FUENTES = [
    r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
]

def ff_escape(path):
    return path.replace("\\", "/").replace(":", r"\:")

def fuente():
    return next((f for f in FUENTES if os.path.exists(f)), None)

def montar(salida, voz, clips):
    if not shutil.which("ffmpeg"):
        sys.exit("ERROR: falta ffmpeg en el PATH (Windows: winget install Gyan.FFmpeg).")
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        lista = os.path.join(tmp, "lista.txt")
        with open(lista, "w", encoding="utf-8") as f:
            for c in clips:
                f.write("file '%s'\n" % os.path.abspath(c).replace("\\", "/").replace("'", r"'\''"))
        vf = "scale=1080:-2:flags=lanczos,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0b0f14,fps=30"
        fnt = fuente()
        if fnt:
            vf += (",drawtext=fontfile='%s':text='%s':fontcolor=0xD4AF37:fontsize=44:"
                   "x=(w-text_w)/2:y=h-120" % (ff_escape(fnt), MARCA))
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista,
               "-i", voz, "-filter_complex", "[0:v]%s[v]" % vf, "-map", "[v]", "-map", "1:a",
               "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
               "-c:a", "aac", "-b:a", "192k", "-shortest", salida]
        subprocess.run(cmd, check=True)
    print("OK ->", salida)

def pendientes():
    raiz = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or "."
    os.chdir(raiz)
    os.makedirs("reels/listos", exist_ok=True); os.makedirs("reels/hechos", exist_ok=True)
    hechos = 0
    for d in sorted(glob.glob("reels/pendientes/*/")):
        d = d.rstrip("/\\"); slug = os.path.basename(d)
        voz = os.path.join(d, "locucion.mp3"); lst = os.path.join(d, "clips.txt")
        if not os.path.exists(voz): print("· %s: falta locucion.mp3 (pendiente de voz)" % slug); continue
        if not os.path.exists(lst): print("· %s: falta clips.txt" % slug); continue
        clips = [l.strip() for l in open(lst, encoding="utf-8") if l.strip()]
        montar("reels/listos/reel-%s.mp4" % slug, voz, clips)
        cap = os.path.join(d, "caption.txt")
        if os.path.exists(cap): shutil.copy(cap, "reels/listos/reel-%s.caption.txt" % slug)
        dest = os.path.join("reels/hechos", slug)
        if os.path.exists(dest): shutil.rmtree(dest)
        shutil.move(d, dest); hechos += 1
    print("Reels montados:", hechos)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--pendientes"]: pendientes()
    elif len(a) >= 3: montar(a[0], a[1], a[2:])
    else: sys.exit(__doc__)
