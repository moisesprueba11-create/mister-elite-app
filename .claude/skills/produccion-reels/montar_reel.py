#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta un Reel vertical 1080x1920 (clips de anim.py + locución) con la marca MISTER ÉLITE.
Salida compatible con la API de publicación de Instagram: H.264 4:2:0, GOP cerrado, AAC 48 kHz 128 kbps,
23-60 fps, <=5 Mbps VBR, moov al principio (faststart).
Multiplataforma (Windows/Mac/Linux). Requiere ffmpeg en el PATH.

Uso:
  python montar_reel.py salida.mp4 locucion.mp3 clip1.mp4 [clip2.mp4 ...]
  python montar_reel.py --texto locucion.txt salida.mp4 locucion.mp3 clip1.mp4   # con subtítulos
  python montar_reel.py --pendientes        # monta todo reels/pendientes/* con locucion.mp3 (+subtítulos si hay locucion.txt)
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

def duracion(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    try: return float(r.stdout.strip())
    except ValueError: return 0.0

def trocear(texto, max_car=30):
    """Parte la locución en frases cortas (subtítulos de 1-2 líneas)."""
    import re, textwrap
    frases = [f.strip() for f in re.split(r"(?<=[.!?¿?:;])\s+", " ".join(texto.split())) if f.strip()]
    trozos = []
    for f in frases:
        palabras, actual = f.split(), []
        for w in palabras:
            if len(" ".join(actual + [w])) > max_car * 2 and actual:
                trozos.append(" ".join(actual)); actual = []
            actual.append(w)
        if actual: trozos.append(" ".join(actual))
    return ["\n".join(textwrap.wrap(t, max_car)) for t in trozos]

def filtros_subtitulos(texto, dur, tmp, fnt):
    """Subtítulos quemados (retención +38 % según datos 2026). Tiempo repartido por nº de caracteres."""
    trozos = trocear(texto)
    if not trozos or dur <= 0 or not fnt: return ""
    total = sum(len(t.replace("\n", " ")) for t in trozos) or 1
    t0, partes = 0.0, []
    for i, t in enumerate(trozos):
        d = dur * len(t.replace("\n", " ")) / total
        ruta = os.path.join(tmp, "sub%d.txt" % i)
        open(ruta, "w", encoding="utf-8").write(t)
        partes.append(("drawtext=fontfile='%s':textfile='%s':fontcolor=white:fontsize=50:"
                       "borderw=4:bordercolor=black:line_spacing=10:x=(w-text_w)/2:y=1665:"
                       "enable='between(t,%.2f,%.2f)'") % (ff_escape(fnt), ff_escape(ruta), t0, t0 + d))
        t0 += d
    return "," + ",".join(partes)

def montar(salida, voz, clips, texto=None, gancho=None):
    if not shutil.which("ffmpeg"):
        sys.exit("ERROR: falta ffmpeg en el PATH (Windows: winget install Gyan.FFmpeg).")
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        lista = os.path.join(tmp, "lista.txt")
        with open(lista, "w", encoding="utf-8") as f:
            for c in clips:
                f.write("file '%s'\n" % os.path.abspath(c).replace("\\", "/").replace("'", r"'\''"))
        vf = "scale=960:-2:flags=lanczos,pad=1080:1920:(ow-iw)/2:100:color=0x0b0f14,fps=30"
        fnt = fuente()
        if texto:
            vf += filtros_subtitulos(texto, duracion(voz), tmp, fnt)
        if gancho and fnt:
            g_txt, g_dur = gancho
            gp = os.path.join(tmp, "gancho.txt")
            open(gp, "w", encoding="utf-8").write("\n".join(trocear(g_txt, 18)))
            vf += (",drawtext=fontfile='%s':textfile='%s':fontcolor=white:fontsize=84:borderw=6:"
                   "bordercolor=black:box=1:boxcolor=black@0.60:boxborderw=34:line_spacing=14:"
                   "x=(w-text_w)/2:y=(h-text_h)/2:enable='between(t,0,%.2f)'") % (
                       ff_escape(fnt), ff_escape(gp), max(g_dur, 1.5))
        if fnt:
            vf += (",drawtext=fontfile='%s':text='%s':fontcolor=0xD4AF37:fontsize=40:"
                   "x=(w-text_w)/2:y=1840" % (ff_escape(fnt), MARCA))
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista,
               "-i", voz, "-filter_complex", "[0:v]%s[v]" % vf, "-map", "[v]", "-map", "1:a",
               "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
               "-maxrate", "5M", "-bufsize", "10M", "-x264-params", "open-gop=0",
               "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2",
               "-movflags", "+faststart", "-shortest", salida]
        subprocess.run(cmd, check=True)
    print("OK ->", salida)

def montar_variantes(d, slug, clips):
    """3 versiones del mismo Reel: solo cambia el gancho (texto en pantalla + frase inicial).
    Requiere: ganchos.json, cuerpo.mp3, gancho_<ID>.mp3 y opcionalmente cuerpo.txt."""
    import json
    ganchos = json.load(open(os.path.join(d, "ganchos.json"), encoding="utf-8"))
    cuerpo_mp3 = os.path.join(d, "cuerpo.mp3")
    cuerpo_txt_p = os.path.join(d, "cuerpo.txt")
    cuerpo_txt = open(cuerpo_txt_p, encoding="utf-8").read() if os.path.exists(cuerpo_txt_p) else ""
    hechas = 0
    for g in ganchos:
        gid = g["id"]; g_mp3 = os.path.join(d, "gancho_%s.mp3" % gid)
        if not (os.path.exists(g_mp3) and os.path.exists(cuerpo_mp3)):
            print("· %s-%s: faltan gancho_%s.mp3 / cuerpo.mp3 (pendiente de voz)" % (slug, gid, gid)); continue
        with tempfile.TemporaryDirectory() as tmp:
            voz = os.path.join(tmp, "voz.mp3")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", g_mp3, "-i", cuerpo_mp3,
                            "-filter_complex", "[0:a][1:a]concat=n=2:v=0:a=1[a]", "-map", "[a]", voz], check=True)
            montar("reels/listos/reel-%s-%s.mp4" % (slug, gid), voz, clips,
                   (g.get("locucion", "") + " " + cuerpo_txt).strip(), (g["pantalla"], duracion(g_mp3)))
        hechas += 1
    return hechas == len(ganchos)

def pendientes():
    raiz = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or "."
    os.chdir(raiz)
    os.makedirs("reels/listos", exist_ok=True); os.makedirs("reels/hechos", exist_ok=True)
    hechos = 0
    for d in sorted(glob.glob("reels/pendientes/*/")):
        d = d.rstrip("/\\"); slug = os.path.basename(d)
        voz = os.path.join(d, "locucion.mp3"); lst = os.path.join(d, "clips.txt")
        if os.path.exists(os.path.join(d, "ganchos.json")) and os.path.exists(lst):
            clips = [l.strip() for l in open(lst, encoding="utf-8") if l.strip()]
            if montar_variantes(d, slug, clips):
                cap = os.path.join(d, "caption.txt")
                if os.path.exists(cap): shutil.copy(cap, "reels/listos/reel-%s.caption.txt" % slug)
                dest = os.path.join("reels/hechos", slug)
                if os.path.exists(dest): shutil.rmtree(dest)
                shutil.move(d, dest); hechos += 1
            continue
        if not os.path.exists(voz): print("· %s: falta locucion.mp3 (pendiente de voz)" % slug); continue
        if not os.path.exists(lst): print("· %s: falta clips.txt" % slug); continue
        clips = [l.strip() for l in open(lst, encoding="utf-8") if l.strip()]
        txt = os.path.join(d, "locucion.txt")
        texto = open(txt, encoding="utf-8").read() if os.path.exists(txt) else None
        montar("reels/listos/reel-%s.mp4" % slug, voz, clips, texto)
        cap = os.path.join(d, "caption.txt")
        if os.path.exists(cap): shutil.copy(cap, "reels/listos/reel-%s.caption.txt" % slug)
        dest = os.path.join("reels/hechos", slug)
        if os.path.exists(dest): shutil.rmtree(dest)
        shutil.move(d, dest); hechos += 1
    print("Reels montados:", hechos)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--pendientes"]: pendientes()
    elif len(a) >= 3 and a[0] != "--texto": montar(a[0], a[1], a[2:])
    elif a[:1] == ["--texto"] and len(a) >= 5: montar(a[2], a[3], a[4:], open(a[1], encoding="utf-8").read())
    else: sys.exit(__doc__)
