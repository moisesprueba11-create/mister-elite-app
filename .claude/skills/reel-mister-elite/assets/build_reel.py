#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_reel.py — Convierte un vídeo/animación de un ejercicio (rondo, tarea, jugada...)
en un reel vertical 9:16 con la marca MISTER ÉLITE, sin deformar ni recortar el vídeo
original: se escala a ancho completo y se centra sobre un lienzo navy, con franjas de
marca arriba/abajo (tarjeta de intro + overlay persistente + tarjeta de cierre).

Requiere: cairosvg, pillow, imageio, numpy, imageio-ffmpeg (pip install si faltan).
No requiere ffmpeg del sistema: usa el binario estático de imageio_ffmpeg.

Uso:
    python3 build_reel.py

Edita el CONFIG de abajo para cada vídeo nuevo (título, subtítulo, textos de marca,
rutas). Pensado para ejecutarse una vez por reel, no como librería genérica.
"""
import subprocess
import cairosvg

# ---------------------------------------------------------------------------
# CONFIG — edita esto para cada reel
# ---------------------------------------------------------------------------
CONFIG = dict(
    src_video="/ruta/al/video_original.mp4",   # el vídeo/animación que te ha pasado el usuario
    out_video="reel-slug.mp4",                  # nombre estable del entregable

    eyebrow="MISTER ÉLITE",                     # marca, SIEMPRE esto, nunca un nombre propio
    kicker="RONDOS · METODOLOGÍA",               # categoría / familia del curso
    title="RONDO 6 v 3",                         # título grande de la tarjeta de intro
    subtitle="+ MINI-PORTERÍA CENTRAL",          # subtítulo dorado
    descriptor="superioridad posicional  →  finalización rápida",  # línea gris de contexto
    footer_tag="del concepto al campo · MISTER ÉLITE",  # pie de la tarjeta de intro

    overlay_kicker="RONDOS · 6v3 + MINI-PORTERÍA",       # texto de la franja superior (durante el vídeo)
    overlay_descriptor="superioridad posicional en espacio reducido",
    overlay_cta_title="CURSO COMPLETO: RONDOS",          # franja inferior / CTA
    overlay_cta_subtitle="el corazón del entrenamiento",
    overlay_footer="del concepto al campo · MISTER ÉLITE",

    outro_title="¿MÁS RONDOS?",                  # tarjeta de cierre
    outro_subtitle="CURSO COMPLETO: RONDOS",
    outro_line2="el corazón del entrenamiento",
    outro_line3="metodología · 50 rondos · plan de sesiones",
    outro_footer="MISTER ÉLITE",

    intro_dur=2.4,     # segundos
    outro_dur=2.8,
)
# Nota audio: este script conserva SIEMPRE el audio original del vídeo fuente tal cual
# (mux directo). Si el usuario pide silenciarlo o poner música, cambia a mano el mapeo
# de audio en `filter_complex`/`-map` más abajo (p. ej. sustituir [1:a] por una pista
# de música con -i musica.mp3 y aformat/atrim a la duración total).

# ---------------------------------------------------------------------------
# Paleta de marca (fija — no cambiar entre cursos)
# ---------------------------------------------------------------------------
NAVY, GOLD, CYAN, WHITE, GRAY = "#0c1b2a", "#f7c948", "#7fd0ff", "#ffffff", "#8aa0b6"
FONT = "DejaVu Sans"
W, H = 1080, 1920  # lienzo vertical 9:16


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size, color, weight=700, anchor="middle", spacing=None):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}"{ls}>{esc(s)}</text>')


def ffprobe_dims(path, ffmpeg_bin):
    out = subprocess.run([ffmpeg_bin, "-i", path], capture_output=True, text=True).stderr
    for line in out.splitlines():
        if "Video:" in line and "x" in line:
            for tok in line.replace(",", " ").split():
                if "x" in tok and tok[0].isdigit():
                    w, h = tok.split("x")[:2]
                    try:
                        return int(w), int(h.split(":")[0])
                    except ValueError:
                        continue
    raise RuntimeError(f"no pude leer dimensiones de {path}")


def main():
    c = CONFIG
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()

    sw, sh = ffprobe_dims(c["src_video"], ff)
    # escala a ancho completo (sin recortar ni deformar) y calcula el hueco vertical
    vh = int(round(W * sh / sw))
    vh += vh % 2  # ffmpeg exige alto par
    pad_y = (H - vh) // 2
    if pad_y < 0:
        raise SystemExit(f"el vídeo ({sw}x{sh}) es demasiado alto para caber en 1080 de ancho "
                          f"sin recortar en un lienzo de {H} — usa un vídeo menos vertical o "
                          f"reduce el ancho del lienzo.")

    intro_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<rect width="{W}" height="{H}" fill="{NAVY}"/>
<rect x="0" y="0" width="{W}" height="14" fill="{GOLD}"/>
<rect x="0" y="{H-14}" width="{W}" height="14" fill="{GOLD}"/>
{text(W/2, 760, c["eyebrow"], 48, CYAN, spacing="6")}
{text(W/2, 815, c["kicker"], 28, GOLD, weight=600, spacing="3")}
{text(W/2, 970, c["title"], 90, WHITE, weight=900)}
{text(W/2, 1055, c["subtitle"], 40, GOLD, weight=700, spacing="1")}
{text(W/2, 1140, c["descriptor"], 30, GRAY, weight=500)}
{text(W/2, 1840, c["footer_tag"], 26, GRAY, weight=500)}
</svg>'''

    outro_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<rect width="{W}" height="{H}" fill="{NAVY}"/>
<rect x="0" y="0" width="{W}" height="14" fill="{GOLD}"/>
<rect x="0" y="{H-14}" width="{W}" height="14" fill="{GOLD}"/>
{text(W/2, 780, c["eyebrow"], 48, CYAN, spacing="6")}
{text(W/2, 940, c["outro_title"], 80, WHITE, weight=900)}
{text(W/2, 1030, c["outro_subtitle"], 38, GOLD, weight=700, spacing="1")}
{text(W/2, 1085, c["outro_line2"], 32, CYAN, weight=600)}
{text(W/2, 1160, c["outro_line3"], 26, GRAY, weight=500)}
{text(W/2, 1840, c["outro_footer"], 26, GRAY, weight=500)}
</svg>'''

    # el hueco del vídeo va de pad_y a pad_y+vh — NO dibujar nada ahí
    overlay_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<rect x="0" y="0" width="{W}" height="8" fill="{GOLD}"/>
<rect x="140" y="60" width="{W-280}" height="4" fill="{GOLD}" opacity="0.85"/>
{text(W/2, 150, c["eyebrow"], 44, CYAN, spacing="5")}
{text(W/2, 205, c["overlay_kicker"], 27, GOLD, weight=600, spacing="1")}
{text(W/2, 260, c["overlay_descriptor"], 23, GRAY, weight=500)}
<rect x="140" y="{H-70}" width="{W-280}" height="4" fill="{GOLD}" opacity="0.85"/>
{text(W/2, H-390, c["overlay_cta_title"], 34, WHITE, weight=800, spacing="1")}
{text(W/2, H-340, c["overlay_cta_subtitle"], 26, CYAN, weight=600)}
{text(W/2, H-65, c["overlay_footer"], 21, GRAY, weight=500)}
<rect x="0" y="{H-8}" width="{W}" height="8" fill="{GOLD}"/>
</svg>'''

    cairosvg.svg2png(bytestring=intro_svg.encode(), write_to="intro.png", output_width=W, output_height=H)
    cairosvg.svg2png(bytestring=outro_svg.encode(), write_to="outro.png", output_width=W, output_height=H)
    cairosvg.svg2png(bytestring=overlay_svg.encode(), write_to="overlay.png", output_width=W, output_height=H)

    # duración del vídeo fuente, para acotar el input en bucle del overlay
    # (¡CRÍTICO! un `-loop 1` sin `-t` ni `-frames:v` es infinito y CUELGA ffmpeg)
    probe = subprocess.run([ff, "-i", c["src_video"]], capture_output=True, text=True).stderr
    src_dur = 0.0
    for line in probe.splitlines():
        if "Duration:" in line:
            hms = line.split("Duration:")[1].split(",")[0].strip()
            hh, mm, ss = hms.split(":")
            src_dur = int(hh) * 3600 + int(mm) * 60 + float(ss)
    overlay_t = max(1.0, src_dur + 1.0)

    filter_complex = f"""
    [0:v]scale={W}:{H},setsar=1,fps=30,format=yuv420p[intro_v];
    [2:v]scale={W}:{H},setsar=1,fps=30,format=yuv420p[outro_v];
    [3:v]scale={W}:{H},fps=30,format=rgba[ovl];
    [1:v]scale={W}:{vh},pad={W}:{H}:0:{pad_y}:color=0x{NAVY[1:]},setsar=1,fps=30[main_bg];
    [main_bg][ovl]overlay=0:0:shortest=1,format=yuv420p[main_v];
    [1:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[main_a];
    [4:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[intro_a];
    [5:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[outro_a];
    [intro_v][intro_a][main_v][main_a][outro_v][outro_a]concat=n=3:v=1:a=1[v][a]
    """

    cmd = [
        ff, "-y",
        "-loop", "1", "-framerate", "30", "-t", str(c["intro_dur"]), "-i", "intro.png",
        "-i", c["src_video"],
        "-loop", "1", "-framerate", "30", "-t", str(c["outro_dur"]), "-i", "outro.png",
        "-loop", "1", "-framerate", "30", "-t", str(overlay_t), "-i", "overlay.png",
        "-f", "lavfi", "-t", str(c["intro_dur"]), "-i", "anullsrc=r=44100:cl=stereo",
        "-f", "lavfi", "-t", str(c["outro_dur"]), "-i", "anullsrc=r=44100:cl=stereo",
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-preset", "medium",
        "-c:a", "aac", "-b:a", "160k",
        c["out_video"],
    ]
    subprocess.run(cmd, check=True, timeout=180)
    print("OK ->", c["out_video"])


if __name__ == "__main__":
    main()
