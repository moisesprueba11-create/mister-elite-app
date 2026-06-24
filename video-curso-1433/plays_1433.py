#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jugadas animadas del piloto 1-4-3-3. Renderiza clips GIF+MP4, reel y guion."""
import os
from anim import Scene, Actor, save_clip, title_card, build_reel, FPS

OUT = os.path.dirname(os.path.abspath(__file__))
def S(label, team, x, y, role="", rb=False): return (label, team, [(0, x, y)], role, rb)

# ---------- 1) Salida en rombo ----------
def p1():
    sc = Scene("Salida en rombo", "POR + 2 centrales + pivote", 54)
    sc.actor("1", "own", [(0,50,8)]); sc.actor("4","own",[(0,62,17)]); sc.actor("5","own",[(0,38,17)])
    sc.actor("6","own",[(0,50,29)], role="pivote")
    sc.actor("2","own",[(0,85,28),(54,88,46)], role="LD"); sc.actor("3","own",[(0,15,28),(54,12,46)], role="LI")
    sc.actor("8","own",[(0,62,44)]); sc.actor("10","own",[(0,40,46)])
    sc.actor("7","own",[(0,88,62)]); sc.actor("11","own",[(0,12,62)]); sc.actor("9","own",[(0,50,72)])
    sc.actor("DC","rival",[(0,44,36),(26,40,26)]); sc.actor("DC","rival",[(0,56,36),(26,47,22)])
    sc.ball([(0,50,11),(12,38,20),(26,50,31),(42,14,46)])
    sc.arrow(2,12,(50,11),(38,20)); sc.arrow(14,26,(38,20),(50,31)); sc.arrow(28,42,(50,31),(14,46))
    sc.caption(0,17,"1 · rombo: POR + 2 DFC + pivote 6")
    sc.caption(18,35,"2 · el 6 recibe de cara y orienta")
    sc.caption(36,53,"3 · progresa por el lateral libre")
    return sc

# ---------- 2) Salida en 3 (lavolpiana) ----------
def p2():
    sc = Scene("Salida en 3 (lavolpiana)", "el 6 baja entre centrales · laterales altos", 54)
    sc.actor("1","own",[(0,50,9)])
    sc.actor("4","own",[(0,66,18),(24,70,20)]); sc.actor("5","own",[(0,34,18),(24,30,20)])
    sc.actor("6","own",[(0,50,26),(24,50,17)], role="baja a la línea de 3")
    sc.actor("2","own",[(0,84,30),(30,90,52)], role="LD"); sc.actor("3","own",[(0,16,30),(30,10,52)], role="LI")
    sc.actor("8","own",[(0,60,42)]); sc.actor("10","own",[(0,40,44)])
    sc.actor("7","own",[(0,90,66)]); sc.actor("11","own",[(0,10,66)]); sc.actor("9","own",[(0,50,74)])
    sc.actor("DC","rival",[(0,44,34)]); sc.actor("DC","rival",[(0,56,34)])
    sc.ball([(0,50,12),(16,30,21),(40,30,21)])
    sc.arrow(4,16,(50,12),(30,21))
    sc.caption(0,23,"1 · el pivote 6 cae entre los centrales")
    sc.caption(24,53,"2 · línea de 3 + laterales altos → 3 vs 2")
    return sc

# ---------- 3) Transformación a 1-3-2-5 ----------
def p3():
    sc = Scene("Transformación a 1-3-2-5", "ocupar los 5 carriles con balón", 54)
    sc.actor("5","own",[(0,38,20)]); sc.actor("4","own",[(0,62,20)])
    sc.actor("6","own",[(0,50,16),(28,50,30)], role="3.ª salida")
    sc.actor("8","own",[(0,58,40),(30,56,48)])
    sc.actor("2","own",[(0,82,32),(40,86,72)], role="LD sube"); sc.actor("3","own",[(0,18,32),(40,14,72)], role="LI sube")
    sc.actor("7","own",[(0,86,66),(40,70,84)], role="ED"); sc.actor("11","own",[(0,14,66),(40,30,84)], role="EI")
    sc.actor("10","own",[(0,46,52),(40,50,72)], role="entre líneas")
    sc.actor("9","own",[(0,50,80),(40,50,88)], role="DC")
    sc.zone(20,53,10,78,90,92,"frente de ataque de 5")
    sc.ball([(0,50,18),(20,50,30),(40,86,70)])
    sc.arrow(22,40,(50,30),(86,70))
    sc.caption(0,19,"1 · base de 3 (2 DFC + pivote) y doble pivote")
    sc.caption(20,53,"2 · laterales y extremos forman el frente de 5")
    return sc

# ---------- 4) Pressing del tridente (gatillo) ----------
def p4():
    sc = Scene("Pressing del tridente", "gatillo: balón al lateral → salta el extremo", 54, half=None)
    # rival construye abajo (atacan hacia abajo); nuestro bloque arriba mirando hacia abajo... usamos campo normal:
    sc.actor("9","own",[(0,50,62),(20,58,52)], role="orienta")
    sc.actor("7","own",[(0,78,58),(24,86,40)], role="salta al lateral")
    sc.actor("11","own",[(0,22,58)], role="cierra dentro")
    sc.actor("8","own",[(0,60,46),(24,72,40)], role="tapa al pivote")
    sc.actor("6","own",[(0,50,40)], role="cubre")
    sc.actor("2","own",[(0,86,46),(24,88,55)], role="sube al extremo")
    # rival
    sc.actor("DFC","rival",[(0,62,34)]); sc.actor("DFC","rival",[(0,40,34)])
    sc.actor("LAT","rival",[(0,84,42)]); sc.actor("PIV","rival",[(0,58,44)])
    sc.zone(24,53,70,40,98,56,"trampa de banda","#ff5252")
    sc.ball([(0,62,36),(14,84,42)])
    sc.arrow(2,14,(62,36),(84,42))
    sc.caption(0,17,"1 · el 9 orienta la salida a una banda")
    sc.caption(18,53,"2 · gatillo: el ED 7 salta y el bloque sube")
    return sc

# ---------- 5) Apoyo + ruptura ----------
def p5():
    sc = Scene("Apoyo + ruptura", "el 9 baja y arrastra · el interior rompe", 56, half="att")
    sc.actor("10","own",[(0,50,57)], role="con balón")
    sc.actor("9","own",[(0,42,80),(24,40,69)], role="apoyo", role_below=True)
    sc.actor("8","own",[(0,66,72),(24,66,72),(44,48,92)], role="ruptura", role_below=True)
    sc.actor("DFC","rival",[(0,42,86),(24,44,74)], role="sigue al 9")
    sc.actor("DFC","rival",[(0,66,86)])
    sc.zone(22,55,26,82,56,96,"espacio a la espalda")
    sc.ball([(0,50,60),(24,50,60),(40,48,90)])
    sc.arrow(26,42,(50,60),(48,90))
    sc.caption(0,23,"1 · el 9 baja de cara y fija a su central")
    sc.caption(24,55,"2 · el interior 8 ataca la espalda + pase")
    return sc

# ---------- 6) Sociedad de banda (desdoblamiento) ----------
def p6():
    sc = Scene("Sociedad de banda", "extremo + lateral + interior (tercer hombre)", 56, half="att")
    sc.actor("7","own",[(0,80,66),(20,80,66),(40,76,72)], role="ED")
    sc.actor("2","own",[(0,72,58),(40,92,84)], role="LD desdobla")
    sc.actor("8","own",[(0,56,62),(30,66,80)], role="interior")
    sc.actor("9","own",[(0,52,82),(40,46,90)], role="DC")
    sc.actor("LI","rival",[(0,86,70)]); sc.actor("DFC","rival",[(0,58,86)])
    sc.ball([(0,80,66),(14,56,62),(30,92,82),(46,52,90)])
    sc.arrow(2,14,(80,66),(56,62)); sc.arrow(16,30,(56,62),(92,82)); sc.arrow(32,46,(92,82),(52,90))
    sc.caption(0,15,"1 · el extremo fija y descarga al interior")
    sc.caption(16,31,"2 · el lateral desdobla por fuera (2v1)")
    sc.caption(32,55,"3 · centro raso atrás al rematador")
    return sc

# ---------- 7) Transición ofensiva ----------
def p7():
    sc = Scene("Transición ofensiva", "robo y verticalidad por el tridente", 56)
    sc.actor("6","own",[(0,50,46)], role="roba")
    sc.actor("9","own",[(0,50,66),(40,52,90)], role="ataca")
    sc.actor("7","own",[(0,80,58),(44,84,90)], role="ED carril")
    sc.actor("11","own",[(0,20,58),(44,18,88)], role="EI carril")
    sc.actor("8","own",[(0,56,52),(44,60,76)], role="2.ª oleada")
    sc.actor("DFC","rival",[(0,44,78)]); sc.actor("DFC","rival",[(0,58,78)])
    sc.ball([(0,50,46),(16,50,66),(40,82,88)])
    sc.arrow(2,16,(50,46),(50,66)); sc.arrow(18,40,(50,66),(82,88))
    sc.caption(0,15,"1 · recuperación del pivote 6")
    sc.caption(16,55,"2 · pase vertical y carriles para el tridente")
    return sc

PLAYS = [("01-salida-rombo", p1, "Salida en rombo"),
         ("02-salida-en-3", p2, "Salida en 3 (lavolpiana)"),
         ("03-transformacion-1325", p3, "Transformación a 1-3-2-5"),
         ("04-pressing-tridente", p4, "Pressing del tridente"),
         ("05-apoyo-ruptura", p5, "Apoyo + ruptura"),
         ("06-sociedad-banda", p6, "Sociedad de banda"),
         ("07-transicion-ofensiva", p7, "Transición ofensiva")]

def main():
    clips = os.path.join(OUT, "clips"); os.makedirs(clips, exist_ok=True)
    segments = []
    for slug, fn, name in PLAYS:
        sc = fn(); frames = sc.render()
        save_clip(frames, os.path.join(clips, slug))
        # still de muestra
        frames[len(frames)*2//3].save(os.path.join(clips, slug + "-still.png"))
        segments.append(title_card(name, sc.subtitle))
        segments.append(frames)
        print("clip:", slug, len(frames), "frames")
    n, size = build_reel(segments, os.path.join(OUT, "reel-1433"))
    print("REEL:", n, "frames", size, "->", os.path.join(OUT, "reel-1433.mp4"))

if __name__ == "__main__":
    main()
