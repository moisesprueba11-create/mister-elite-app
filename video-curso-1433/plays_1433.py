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

# ---------- 8) Repliegue a 1-4-5-1 ----------
def p8():
    sc = Scene("Repliegue a 1-4-5-1", "sin balón los extremos bajan a la línea de medios", 50)
    sc.actor("2","own",[(0,82,26)]); sc.actor("4","own",[(0,60,18)]); sc.actor("5","own",[(0,40,18)]); sc.actor("3","own",[(0,18,26)])
    sc.actor("6","own",[(0,50,36)]); sc.actor("8","own",[(0,62,42)]); sc.actor("10","own",[(0,38,42)])
    sc.actor("7","own",[(0,84,60),(28,76,42)], role="baja"); sc.actor("11","own",[(0,16,60),(28,24,42)], role="baja")
    sc.actor("9","own",[(0,50,64)], role="referencia")
    sc.actor("DC","rival",[(0,50,80)]); sc.actor("DC","rival",[(0,66,76)]); sc.actor("DC","rival",[(0,34,76)])
    sc.ball([(0,50,82),(50,50,82)])
    sc.caption(0,25,"1 · perdemos el balón: los extremos repliegan")
    sc.caption(26,49,"2 · bloque 1-4-5-1 compacto, dos líneas")
    return sc

# ---------- 9) Basculación ----------
def p9():
    sc = Scene("Basculación", "el bloque se desplaza al lado del balón", 48)
    D = 16
    for lbl, x, y in [("2",82,30),("4",58,24),("5",38,24),("3",16,30),("6",50,42),("8",62,46),("10",40,46)]:
        sc.actor(lbl,"own",[(0,x,y),(30,x+D,y)])
    sc.actor("7","own",[(0,84,60),(30,90,60)]); sc.actor("11","own",[(0,16,60),(30,40,60)], role="pisa dentro")
    sc.actor("9","own",[(0,50,68),(30,62,68)])
    sc.actor("DC","rival",[(0,30,82),(30,80,80)], role="circula")
    sc.ball([(0,30,80),(30,80,78)])
    sc.zone(30,47,62,20,99,72,"lado fuerte (densidad)","#ffd54a")
    sc.caption(0,23,"1 · el balón cambia de lado…")
    sc.caption(24,47,"2 · …y las dos líneas bascula juntas")
    return sc

# ---------- 10) Ataque del área ----------
def p10():
    sc = Scene("Ataque del área", "centro y los cuatro puntos de remate", 54, half="att")
    sc.actor("7","own",[(0,82,72),(16,86,80)], role="centra")
    sc.actor("9","own",[(0,52,80),(40,40,90)], role="1er palo")
    sc.actor("10","own",[(0,46,72),(40,52,90)], role="penalti")
    sc.actor("11","own",[(0,18,74),(40,62,92)], role="2º palo")
    sc.actor("8","own",[(0,56,64),(40,54,78)], role="frontal")
    sc.actor("DFC","rival",[(0,44,86)]); sc.actor("DFC","rival",[(0,58,86)]); sc.actor("1",("rival"),[(0,50,97)])
    sc.ball([(0,82,72),(18,86,80),(40,56,90)])
    sc.arrow(18,40,(86,80),(56,90))
    sc.caption(0,17,"1 · desborde y centro del extremo")
    sc.caption(18,53,"2 · 1er palo · penalti · 2º palo · frontal")
    return sc

# ---------- 11) Los 5 carriles ----------
def p11():
    sc = Scene("Ocupar los 5 carriles", "uno por carril: nunca dos en el mismo", 44)
    for i in range(1,5):
        sc.zone(0,43, i*20, 6, i*20, 94, "")  # líneas divisorias suaves
    sc.actor("3","own",[(0,30,34),(26,10,40)], role="LI"); sc.actor("2","own",[(0,70,34),(26,90,40)], role="LD")
    sc.actor("11","own",[(0,30,66),(26,12,78)], role="EI"); sc.actor("7","own",[(0,70,66),(26,88,78)], role="ED")
    sc.actor("10","own",[(0,44,60),(26,30,70)], role="interior"); sc.actor("8","own",[(0,56,60),(26,70,70)], role="interior")
    sc.actor("9","own",[(0,50,80),(26,50,86)], role="DC")
    sc.actor("6","own",[(0,50,40)]); sc.actor("5","own",[(0,40,24)]); sc.actor("4","own",[(0,60,24)])
    sc.ball([(0,50,42),(44,50,42)])
    sc.caption(0,43,"un jugador por cada uno de los 5 carriles")
    return sc

# ---------- 12) 1v1 del extremo a pie cambiado ----------
def p12():
    sc = Scene("1v1 del extremo (pie cambiado)", "corta dentro y dispara", 48, half="att")
    sc.actor("7","own",[(0,80,66),(18,80,66),(40,64,82)], role="ED")
    sc.actor("2","own",[(0,72,60),(40,90,82)], role="LD da amplitud")
    sc.actor("LI","rival",[(0,84,72),(40,74,84)], role="lateral")
    sc.actor("1","rival",[(0,50,97)])
    sc.ball([(0,80,66),(40,64,82),(48,50,98)])
    sc.arrow(40,48,(64,82),(50,97), kind="pass")
    sc.caption(0,19,"1 · el extremo encara con el lateral abierto")
    sc.caption(20,47,"2 · corta hacia dentro y dispara a portería")
    return sc

# ---------- 13) Cambio de orientación ----------
def p13():
    sc = Scene("Cambio de orientación", "atraer a un lado y cambiar al extremo aislado", 52)
    sc.actor("8","own",[(0,64,48),(24,54,50)], role="atrae")
    sc.actor("2","own",[(0,84,52)]); sc.actor("7","own",[(0,88,64)])
    sc.actor("6","own",[(0,50,40)])
    sc.actor("11","own",[(0,14,66),(40,12,74)], role="EI aislado 1v1")
    sc.actor("3","own",[(0,20,52),(40,22,66)], role="LI acompaña")
    sc.actor("DFC","rival",[(0,70,58)]); sc.actor("DFC","rival",[(0,58,60)]); sc.actor("LD","rival",[(0,24,70)])
    sc.ball([(0,64,48),(24,52,50),(44,14,70)])
    sc.arrow(26,44,(52,50),(14,70))
    sc.caption(0,23,"1 · se atrae al rival al lado fuerte")
    sc.caption(24,51,"2 · cambio largo al extremo aislado")
    return sc

# ---------- 14) Llegada de interiores al área ----------
def p14():
    sc = Scene("Llegada de interiores", "el centro lo rematan los que llegan de atrás", 52, half="att")
    sc.actor("11","own",[(0,18,72),(16,14,80)], role="centra")
    sc.actor("9","own",[(0,50,82),(40,40,90)], role="fija 1er palo")
    sc.actor("10","own",[(0,46,66),(40,54,90)], role="llega al punto de penalti")
    sc.actor("8","own",[(0,60,60),(40,58,80)], role="al frontal")
    sc.actor("DFC","rival",[(0,44,86)]); sc.actor("DFC","rival",[(0,58,86)]); sc.actor("1","rival",[(0,50,97)])
    sc.ball([(0,18,72),(18,14,80),(40,52,90)])
    sc.arrow(18,40,(14,80),(52,90))
    sc.caption(0,17,"1 · centro desde la banda contraria")
    sc.caption(18,51,"2 · interiores rematan desde segunda línea")
    return sc

PLAYS = [("01-salida-rombo", p1, "Salida en rombo"),
         ("02-salida-en-3", p2, "Salida en 3 (lavolpiana)"),
         ("03-transformacion-1325", p3, "Transformación a 1-3-2-5"),
         ("04-pressing-tridente", p4, "Pressing del tridente"),
         ("05-apoyo-ruptura", p5, "Apoyo + ruptura"),
         ("06-sociedad-banda", p6, "Sociedad de banda"),
         ("07-transicion-ofensiva", p7, "Transición ofensiva"),
         ("08-repliegue-1451", p8, "Repliegue a 1-4-5-1"),
         ("09-basculacion", p9, "Basculación"),
         ("10-ataque-area", p10, "Ataque del área"),
         ("11-cinco-carriles", p11, "Ocupar los 5 carriles"),
         ("12-extremo-1v1", p12, "1v1 del extremo"),
         ("13-cambio-orientacion", p13, "Cambio de orientación"),
         ("14-llegada-interiores", p14, "Llegada de interiores")]

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
