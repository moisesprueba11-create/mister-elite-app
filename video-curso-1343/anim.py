#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
anim.py — Motor de animación de la tarea "SALIDA 1-3-4-3 + STOP BALL".
Genera el MP4 (1080x1080), un GIF ligero y los stills para el curso.

    python3 anim.py            # MP4 + GIF + stills
    python3 anim.py --stills   # solo stills (rápido, para revisar)
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))

from PIL import Image, ImageDraw
import imageio.v2 as imageio
import numpy as np

from board import Board, C, _f, F_BOLD, F_REG
from jugadas_1343 import (ZONE_X, LANE_Y, STOP_ZONE, MINI_GOALS, PITCH_RATIO,
                          BLUE_START, RED_START, LINEAS_SISTEMA, JUGADAS, REGLAS)

FPS = 25
OUT = os.path.dirname(os.path.abspath(__file__))
TITULO = "SALIDA DE BALÓN EN 1-3-4-3"
SUBTITULO = "JUEGO DE POSICIÓN POR ZONAS · 10 vs 8 · OBJETIVO: STOP BALL"
BALL_OFF = -3.2                      # el balón se dibuja al lado del jugador

RED_GAIN = {                         # deslizamiento del bloque rojo (kx, ky)
    "r11": (0.10, 0.34), "r9": (0.10, 0.34), "r7": (0.10, 0.34),
    "r10": (0.07, 0.26), "r6": (0.07, 0.26), "r8": (0.07, 0.26),
    "r4": (0.04, 0.18), "r5": (0.04, 0.18),
}


# ------------------------------------------------------------- interpolación --
def ss(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def kf_pos(kfs, t):
    if t <= kfs[0][0]:
        return kfs[0][1], kfs[0][2]
    if t >= kfs[-1][0]:
        return kfs[-1][1], kfs[-1][2]
    for i in range(len(kfs) - 1):
        t0, x0, y0 = kfs[i]
        t1, x1, y1 = kfs[i + 1]
        if t0 <= t <= t1:
            k = ss((t - t0) / (t1 - t0)) if t1 > t0 else 1.0
            return x0 + (x1 - x0) * k, y0 + (y1 - y0) * k
    return kfs[-1][1], kfs[-1][2]


class Jugada:
    """Resuelve posiciones de los 18 jugadores y del balón en cada instante."""

    def __init__(self, data):
        self.d = data
        self.moves = data.get("moves", {})
        self.rmoves = data.get("rmoves", {})
        self.ball_ev = data["ball"]
        self._ema = None

    # -- jugadores --------------------------------------------------------
    def blue(self, label, t):
        kfs = self.moves.get(label)
        return kf_pos(kfs, t) if kfs else BLUE_START[label]

    def red(self, label, t, bxy):
        kfs = self.rmoves.get(label)
        if kfs:
            return kf_pos(kfs, t)
        bx, by = bxy
        kx, ky = RED_GAIN[label]
        x0, y0 = RED_START[label]
        dx = max(-7.0, min(7.0, kx * (bx - 50.0)))
        dy = max(-14.0, min(14.0, ky * (by - 50.0)))
        return x0 + dx, y0 + dy

    def pos(self, label, t):
        return self.blue(label, t) if not label.startswith("r") else \
            (kf_pos(self.rmoves[label], t) if label in self.rmoves else RED_START[label])

    # -- balón ------------------------------------------------------------
    def ball(self, t):
        """Devuelve (x, y, portador|None, evento_activo)."""
        ev = self.ball_ev[0]
        for e in self.ball_ev:
            if e["t0"] <= t <= e["t1"]:
                ev = e
                break
            if t > e["t1"]:
                ev = e
        k = ev["k"]
        if k in ("hold", "conduce"):
            x, y = self.pos(ev["who"], min(t, ev["t1"]))
            return x + BALL_OFF, y, ev["who"], ev
        if k == "pase":
            ax, ay = self.pos(ev["a"], ev["t0"])
            bx, by = self.pos(ev["b"], ev["t1"])
            ax, bx = ax + BALL_OFF, bx + BALL_OFF
            u = ss((min(t, ev["t1"]) - ev["t0"]) / max(0.001, ev["t1"] - ev["t0"]))
            return ax + (bx - ax) * u, ay + (by - ay) * u, (ev["b"] if u >= 1 else None), ev
        if k == "tiro":
            ax, ay = self.pos(ev["a"], ev["t0"])
            bx, by = ev["xy"]
            u = ss((min(t, ev["t1"]) - ev["t0"]) / max(0.001, ev["t1"] - ev["t0"]))
            return ax + BALL_OFF + (bx - ax - BALL_OFF) * u, ay + (by - ay) * u, None, ev
        return 50, 50, None, ev

    def caption(self, t):
        cur = self.ball_ev[0]
        for e in self.ball_ev:
            if t >= e["t0"]:
                cur = e
        return cur

    def cadena(self, t):
        """Cadena de pases ya jugados, para el pie de la pizarra."""
        seq = []
        for e in self.ball_ev:
            if t < e["t0"]:
                break
            if e["k"] == "hold" and not seq:
                seq.append(e["who"])
            elif e["k"] == "pase":
                if not seq:
                    seq.append(e["a"])
                seq.append("ROJO " + e["b"][1:] if e["b"].startswith("r") else e["b"])
            elif e["k"] == "tiro":
                seq.append("TIRO")
            elif e["k"] == "conduce":
                seq.append("STOP BALL")
        seq = [s for s in seq]
        txt = "  →  ".join(seq[-9:])
        return ("…  →  " if len(seq) > 9 else "") + txt

    def trails(self, t, n=4):
        """Últimos pases completados (para dejar rastro) + pase activo."""
        out = []
        for e in self.ball_ev:
            if e["k"] not in ("pase", "tiro", "conduce"):
                continue
            if t < e["t0"]:
                continue
            if e["k"] == "conduce":
                p0 = self.pos(e["who"], e["t0"])
                p1 = self.pos(e["who"], min(t, e["t1"]))
                out.append((p0, p1, "conduce", e, t <= e["t1"]))
                continue
            p0 = self.pos(e["a"], e["t0"])
            p1 = e["xy"] if e["k"] == "tiro" else self.pos(e["b"], e["t1"])
            act = e["t0"] <= t <= e["t1"]
            if act:
                u = ss((t - e["t0"]) / max(0.001, e["t1"] - e["t0"]))
                p1 = (p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u)
            out.append((p0, p1, "rojo" if e.get("rojo") or e.get("perdida") else "pase",
                        e, act))
        return out[-n:]


# ------------------------------------------------------------------- render --
class Renderer:
    def __init__(self):
        self.bd = Board(1080, 1080, scale=2, ratio=PITCH_RATIO, zone_x=ZONE_X,
                        lane_y=LANE_Y, stop=STOP_ZONE, mini_goals=MINI_GOALS)
        self.bd.build_bg(TITULO, SUBTITULO)

    def frame(self, blues, reds, ball=None, carrier=None, trails=(), lines=(),
              chip="", titulo="", texto="", extra=None, glow=0.0, dimplayers=()):
        S = self.bd.S
        im = self.bd.bg.copy()
        ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
        do = ImageDraw.Draw(ov)
        d = ImageDraw.Draw(im)

        # brillo de la zona STOP BALL al conseguir el punto
        if glow > 0:
            sx0, sx1 = self.bd.X(STOP_ZONE["x0"]), self.bd.X(STOP_ZONE["x1"])
            sy0, sy1 = self.bd.Y(STOP_ZONE["y0"]), self.bd.Y(STOP_ZONE["y1"])
            do.rectangle([sx0, sy0, sx1, sy1], fill=(255, 255, 255, int(110 * glow)))

        # líneas del sistema (intro)
        for pts, alpha in lines:
            for i in range(len(pts) - 1):
                x0, y0 = pts[i]
                x1, y1 = pts[i + 1]
                do.line([(self.bd.X(x0), self.bd.Y(y0)), (self.bd.X(x1), self.bd.Y(y1))],
                        fill=(126, 224, 255, int(235 * alpha)), width=int(7 * S))

        # rastros de pases
        for i, (p0, p1, kind, ev, act) in enumerate(trails):
            age = len(trails) - i
            a = 255 if act else max(60, 235 - age * 52)
            col = C["carry"] if kind == "conduce" else (
                C["red_pass"] if kind == "rojo" else C["pass_c"])
            w = int((7.5 if act else 4.5) * S)
            if kind == "conduce":
                self.bd._dashed(do, (self.bd.X(p0[0]), self.bd.Y(p0[1])),
                                (self.bd.X(p1[0]), self.bd.Y(p1[1])),
                                col + (a,), w, 15 * S, 10 * S)
            else:
                do.line([(self.bd.X(p0[0]), self.bd.Y(p0[1])),
                         (self.bd.X(p1[0]), self.bd.Y(p1[1]))], fill=col + (a,), width=w)
                if act:
                    ang = math.atan2(self.bd.Y(p1[1]) - self.bd.Y(p0[1]),
                                     self.bd.X(p1[0]) - self.bd.X(p0[0]))
                    hx, hy = self.bd.X(p1[0]), self.bd.Y(p1[1])
                    hl, hw = 18 * S, 9.5 * S
                    do.polygon([(hx, hy),
                                (hx - hl * math.cos(ang) + hw * math.sin(ang),
                                 hy - hl * math.sin(ang) - hw * math.cos(ang)),
                                (hx - hl * math.cos(ang) - hw * math.sin(ang),
                                 hy - hl * math.sin(ang) + hw * math.cos(ang))],
                               fill=col + (a,))

        im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
        d = ImageDraw.Draw(im)

        for lb, (x, y) in reds.items():
            self.bd.player(d, x, y, lb[1:], team="rival",
                           ball=(carrier == lb), dim=0.62 if lb in dimplayers else 1.0)
        for lb, (x, y) in blues.items():
            self.bd.player(d, x, y, lb, team="own",
                           ball=(carrier == lb), dim=0.62 if lb in dimplayers else 1.0)
        if ball:
            self.bd.ball(d, ball[0], ball[1])

        self.bd.caption(d, chip, titulo, texto, extra)
        return self.bd.finish(im)


# ----------------------------------------------------------------- timeline --
def build_frames(stills_only=False, sink=None):
    """Genera la película fotograma a fotograma. `sink(img)` recibe cada frame
    (se escribe al vuelo para no acumular ~1 GB en memoria)."""
    R = Renderer()
    stills = {}
    last = {"img": None}

    def add(img, n=1):
        last["img"] = img
        if sink:
            for _ in range(n):
                sink(img)

    # ---------- 1. presentación de la tarea ----------
    intro_txt = ("10 azules en 1-3-4-3 (sin portero) contra 8 rojos. "
                 "Hay que llevar el balón desde el fondo propio hasta pararlo en la zona verde.")
    base = dict(blues=dict(BLUE_START), reds=dict(RED_START), chip="LA TAREA",
                titulo="ESPACIO, EQUIPOS Y OBJETIVO",
                texto=intro_txt, extra="   ·   ".join(REGLAS[:2]))
    img = R.frame(**base)
    stills["still-tarea.png"] = img
    if not stills_only:
        add(img, int(2.6 * FPS))

        # ---------- 2. las tres líneas del sistema ----------
        for idx, (labels, texto) in enumerate(LINEAS_SISTEMA):
            pts = [BLUE_START[l] for l in labels]
            for f in range(int(1.9 * FPS)):
                u = min(1.0, f / (0.55 * FPS))
                partial = _partial_line(pts, u)
                prev = [( [BLUE_START[l] for l in LINEAS_SISTEMA[j][0]], 0.45)
                        for j in range(idx)]
                add(R.frame(blues=dict(BLUE_START), reds=dict(RED_START),
                            lines=prev + [(partial, 1.0)], chip=f"1-3-4-3",
                            titulo="ESTRUCTURA DEL EQUIPO AZUL", texto=texto,
                            extra=REGLAS[2] + "   ·   " + REGLAS[3]))
        img = R.frame(blues=dict(BLUE_START), reds=dict(RED_START),
                      lines=[([BLUE_START[l] for l in lb], 0.75) for lb, _ in LINEAS_SISTEMA],
                      chip="1-3-4-3", titulo="ESTRUCTURA DEL EQUIPO AZUL",
                      texto="3 centrales + 2 carrileros + 2 interiores + 3 arriba. "
                            "Cada línea, en su zona.",
                      extra=REGLAS[2] + "   ·   " + REGLAS[3])
        stills["still-sistema.png"] = img
        add(img, int(1.4 * FPS))

    # ---------- 3. las dos jugadas ----------
    for jd in JUGADAS:
        J = Jugada(jd)
        chip = f"JUGADA {jd['num']}"
        n = int(jd["dur"] * FPS)
        key_still = int(n * 0.72)
        for f in range(n):
            t = f / FPS
            bx, by, carrier, ev = J.ball(t)
            blues = {lb: J.blue(lb, t) for lb in BLUE_START}
            reds = {lb: J.red(lb, t, (bx, by)) for lb in RED_START}
            cap = J.caption(t)
            glow = 0.0
            if cap.get("gol"):
                glow = 0.35 + 0.30 * math.sin(t * 7.0)
            img = R.frame(blues=blues, reds=reds, ball=(bx, by), carrier=carrier,
                          trails=J.trails(t), chip=chip, titulo=jd["titulo"],
                          texto=cap["txt"], extra=J.cadena(t), glow=max(0.0, glow))
            if f == key_still:
                stills[f"still-jugada{jd['num']}.png"] = img
            if not stills_only:
                add(img)
        if stills_only:
            continue
        # pausa entre jugadas
        add(last["img"], int(0.7 * FPS))

    if stills_only:
        return stills

    # ---------- 4. cierre ----------
    cierre = R.frame(blues=dict(BLUE_START), reds=dict(RED_START),
                     lines=[([BLUE_START[l] for l in lb], 0.55) for lb, _ in LINEAS_SISTEMA],
                     chip="CLAVES", titulo="QUÉ ENTRENAMOS CON ESTA TAREA",
                     texto="Salida en 1-3-4-3: centrales abiertos, carrileros altos, "
                           "interiores entre líneas y extremos atacando la última zona.",
                     extra="MISTER ÉLITE — Moisés Díaz   ·   Progresión por zonas + transición tras pérdida")
    stills["still-claves.png"] = cierre
    add(cierre, int(3.0 * FPS))
    return stills


def _partial_line(pts, u):
    """Dibuja progresivamente la polilínea que une una línea del sistema."""
    if u >= 1.0:
        return pts
    total = len(pts) - 1
    done = u * total
    out = [pts[0]]
    for i in range(total):
        if done >= i + 1:
            out.append(pts[i + 1])
        elif done > i:
            k = done - i
            out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * k,
                        pts[i][1] + (pts[i + 1][1] - pts[i][1]) * k))
            break
        else:
            break
    return out


def _gif_desde_mp4(mp4, gif, fps=12, ancho=540):
    """GIF en bucle a partir del MP4, con paleta propia (ffmpeg de imageio)."""
    import subprocess
    from imageio_ffmpeg import get_ffmpeg_exe
    vf = (f"fps={fps},scale={ancho}:-1:flags=lanczos,split[a][b];"
          f"[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=3")
    subprocess.run([get_ffmpeg_exe(), "-y", "-loglevel", "error", "-i", mp4,
                    "-vf", vf, "-loop", "0", gif], check=True)


def main():
    stills_only = "--stills" in sys.argv
    os.makedirs(os.path.join(OUT, "stills"), exist_ok=True)
    if stills_only:
        for name, img in build_frames(True).items():
            img.save(os.path.join(OUT, "stills", name))
            print("still ->", name)
        return

    mp4 = os.path.join(OUT, "animacion-1343-stopball.mp4")
    gif = os.path.join(OUT, "animacion-1343-stopball.gif")
    w = imageio.get_writer(mp4, fps=FPS, codec="libx264", quality=8,
                           macro_block_size=8, ffmpeg_params=["-pix_fmt", "yuv420p"])
    n = [0]

    def sink(img):
        w.append_data(np.asarray(img))
        n[0] += 1
        if n[0] % 100 == 0:
            print("  ...", n[0], "frames", flush=True)

    stills = build_frames(False, sink)
    w.close()
    print("mp4 ->", mp4, n[0], "frames")
    for name, img in stills.items():
        img.save(os.path.join(OUT, "stills", name))
        print("still ->", name)
    _gif_desde_mp4(mp4, gif)
    print("gif ->", gif, f"({os.path.getsize(gif)/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
