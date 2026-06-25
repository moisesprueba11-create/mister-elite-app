#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Animaciones de conceptos del Juego de posición. Render clips GIF+MP4 + reel."""
import os
from anim import Scene, save_clip, title_card, build_reel
OUT = os.path.dirname(os.path.abspath(__file__))
def sc_(t, s, n): return Scene(t, s, n, half=None, attack_arrow=False)

# 1) Superioridad numérica (3v2: siempre hay un hombre libre)
def a1():
    sc = sc_("Superioridad numérica", "3 v 2: siempre sobra un hombre", 52)
    sc.actor("P","own",[(0,30,52)]); sc.actor("P","own",[(0,50,40)]); sc.actor("P","own",[(0,70,52)], role="LIBRE", role_below=True)
    sc.actor("D","rival",[(0,42,50),(20,38,50)]); sc.actor("D","rival",[(0,58,50),(20,55,46)])
    sc.ball([(0,30,52),(14,50,42),(30,70,52)])
    sc.arrow(2,14,(30,52),(50,42)); sc.arrow(16,30,(50,42),(70,52))
    sc.caption(0,25,"1 · los 2 defensores no llegan a los 3")
    sc.caption(26,51,"2 · el balón encuentra al hombre LIBRE")
    return sc

# 2) Superioridad posicional (recibir entre líneas)
def a2():
    sc = sc_("Superioridad posicional", "recibir orientado entre líneas", 50)
    sc.actor("P","own",[(0,50,32)], role="con balón")
    sc.actor("P","own",[(0,50,52)], role="entre líneas", role_below=True)
    sc.actor("D","rival",[(0,38,46)]); sc.actor("D","rival",[(0,62,46)])
    sc.actor("D","rival",[(0,40,62)]); sc.actor("D","rival",[(0,60,62)])
    sc.zone(0,49,30,44,70,60,"ventana entre líneas")
    sc.ball([(0,50,34),(22,50,50)])
    sc.arrow(4,22,(50,34),(50,50))
    sc.caption(0,49,"el pase rompe la 1.ª línea y el receptor gira de cara")
    return sc

# 3) Hombre libre (presión a un lado → cambio)
def a3():
    sc = sc_("Encontrar al hombre libre", "presión a un lado, cambio al opuesto", 52)
    sc.actor("P","own",[(0,72,50)], role="con balón")
    sc.actor("P","own",[(0,55,40)]); sc.actor("P","own",[(0,20,58)], role="LIBRE", role_below=True)
    sc.actor("D","rival",[(0,66,52)]); sc.actor("D","rival",[(0,58,48)]); sc.actor("D","rival",[(0,44,56)])
    sc.ball([(0,72,50),(14,55,40),(40,20,58)])
    sc.arrow(2,14,(72,50),(55,40)); sc.arrow(20,40,(55,40),(20,58))
    sc.caption(0,25,"1 · el rival se desplaza al balón…")
    sc.caption(26,51,"2 · cambio al hombre libre del lado contrario")
    return sc

# 4) Atraer para liberar
def a4():
    sc = sc_("Atraer para liberar", "fijar a un lado y cambiar", 54)
    sc.actor("P","own",[(0,70,42)]); sc.actor("P","own",[(0,78,56)]); sc.actor("P","own",[(0,55,50)])
    sc.actor("P","own",[(0,22,56)], role="LIBRE", role_below=True)
    sc.actor("D","rival",[(0,64,46),(24,72,48)]); sc.actor("D","rival",[(0,56,56),(24,66,56)]); sc.actor("D","rival",[(0,42,52),(24,52,52)])
    sc.ball([(0,70,42),(10,78,56),(24,55,50),(44,22,56)])
    sc.arrow(2,10,(70,42),(78,56)); sc.arrow(12,24,(78,56),(55,50)); sc.arrow(26,44,(55,50),(22,56))
    sc.caption(0,25,"1 · fijamos al rival con pases a un lado")
    sc.caption(26,53,"2 · y cambiamos al espacio liberado")
    return sc

# 5) Tercer hombre
def a5():
    sc = sc_("Tercer hombre", "A → B (de espaldas) → C que aparece", 54)
    sc.actor("P","own",[(0,38,42)], role="A")
    sc.actor("P","own",[(0,55,58)], role="B de espaldas")
    sc.actor("P","own",[(0,40,52),(28,46,78)], role="C aparece", role_below=True)
    sc.actor("D","rival",[(0,55,64)]); sc.actor("D","rival",[(0,46,58)])
    sc.ball([(0,38,42),(12,55,57),(30,46,76)])
    sc.arrow(2,12,(38,42),(55,57)); sc.arrow(14,30,(55,57),(46,76))
    sc.caption(0,25,"1 · pase al pivote de espaldas (B)")
    sc.caption(26,53,"2 · B deja al TERCER HOMBRE (C) en carrera")
    return sc

# 6) Pase entre líneas (ventana)
def a6():
    sc = sc_("Pase entre líneas", "abrir la ventana y filtrar de perfil", 48)
    sc.actor("P","own",[(0,40,34)], role="con balón")
    sc.actor("P","own",[(0,60,52)], role="de perfil")
    sc.actor("D","rival",[(0,46,46)]); sc.actor("D","rival",[(0,72,46)])
    sc.ball([(0,40,34),(22,60,52)])
    sc.arrow(4,22,(40,34),(60,52))
    sc.caption(0,47,"el balón pasa por la ventana entre dos rivales")
    return sc

# 7) Ritmo: pausa-aceleración
def a7():
    sc = sc_("Ritmo: pausa-aceleración", "circular en pausa y romper rápido", 56)
    sc.actor("P","own",[(0,35,40)]); sc.actor("P","own",[(0,55,38)]); sc.actor("P","own",[(0,50,55)])
    sc.actor("P","own",[(0,55,82)], role="rompe", role_below=True)
    sc.actor("D","rival",[(0,45,50)]); sc.actor("D","rival",[(0,58,52)])
    sc.ball([(0,35,40),(10,55,38),(22,50,55),(34,55,80)])
    sc.arrow(2,10,(35,40),(55,38)); sc.arrow(12,22,(55,38),(50,55)); sc.arrow(24,34,(50,55),(55,80))
    sc.caption(0,21,"1 · PAUSA: circular y esperar la señal…")
    sc.caption(22,55,"2 · ACELERACIÓN: pase vertical y ruptura")
    return sc

# 8) Contrapresión tras pérdida
def a8():
    sc = sc_("Contrapresión", "recuperar en 5 s tras la pérdida", 50)
    sc.actor("P","own",[(0,46,56),(20,52,60)]); sc.actor("P","own",[(0,62,54),(20,58,58)]); sc.actor("P","own",[(0,50,42),(20,52,50)])
    sc.actor("D","rival",[(0,54,56)], role="acaba de robar")
    sc.actor("D","rival",[(0,70,66)]); sc.actor("D","rival",[(0,36,66)])
    sc.zone(8,49,40,46,68,70,"reacción ≤5 s","#ff5252")
    sc.ball([(0,54,56),(50,54,56)])
    sc.arrow(6,20,(52,50),(54,55)); sc.arrow(6,20,(52,60),(54,56)); sc.arrow(6,20,(58,58),(55,56))
    sc.caption(0,49,"al perder, los más cercanos saltan y tapan líneas")
    return sc

# 9) Juego de posición 4v4+3 (circulación)
def a9():
    sc = sc_("Juego de posición 4v4+3", "comodines + circulación para mantener", 56)
    P=[(28,40),(50,30),(72,40),(50,70)]
    for x,y in P: sc.actor("P","own",[(0,x,y)])
    sc.actor("C","neutral",[(0,20,55)]); sc.actor("C","neutral",[(0,80,55)]); sc.actor("C","neutral",[(0,50,50)], role="interior")
    sc.actor("D","rival",[(0,44,46),(28,60,44)]); sc.actor("D","rival",[(0,56,46),(28,44,56)])
    sc.actor("D","rival",[(0,40,60)]); sc.actor("D","rival",[(0,60,60)])
    sc.ball([(0,28,40),(12,50,30),(24,72,40),(36,80,55),(48,50,50)])
    sc.arrow(2,12,(28,40),(50,30)); sc.arrow(14,24,(50,30),(72,40)); sc.arrow(26,36,(72,40),(80,55)); sc.arrow(38,48,(80,55),(50,50))
    sc.caption(0,27,"circular por fuera con los comodines…")
    sc.caption(28,55,"…para encontrar al interior libre")
    return sc

# 10) Ocupar los 5 carriles
def a10():
    sc = sc_("Ocupar los 5 carriles", "uno por carril, no 3 en la misma línea", 46)
    for i in range(1,5): sc.zone(0,45, i*20, 10, i*20, 90, "")
    sc.actor("P","own",[(0,40,40),(24,10,46)]); sc.actor("P","own",[(0,60,40),(24,90,46)])
    sc.actor("P","own",[(0,42,62),(24,30,70)]); sc.actor("P","own",[(0,58,62),(24,70,70)])
    sc.actor("P","own",[(0,50,82)]); sc.actor("P","own",[(0,50,30)])
    sc.ball([(0,50,32),(46,50,32)])
    sc.caption(0,45,"cada jugador ocupa un carril distinto")
    return sc

PLAYS = [("01-superioridad-numerica", a1, "Superioridad numérica"),
         ("02-superioridad-posicional", a2, "Superioridad posicional"),
         ("03-hombre-libre", a3, "Encontrar al hombre libre"),
         ("04-atraer-cambiar", a4, "Atraer para liberar"),
         ("05-tercer-hombre", a5, "Tercer hombre"),
         ("06-pase-entre-lineas", a6, "Pase entre líneas"),
         ("07-ritmo", a7, "Ritmo: pausa-aceleración"),
         ("08-contrapresion", a8, "Contrapresión"),
         ("09-jdp-4v4mas3", a9, "Juego de posición 4v4+3"),
         ("10-cinco-carriles", a10, "Ocupar los 5 carriles")]

def main():
    clips = os.path.join(OUT, "clips"); os.makedirs(clips, exist_ok=True)
    segments = []
    for slug, fn, name in PLAYS:
        sc = fn(); frames = sc.render()
        save_clip(frames, os.path.join(clips, slug))
        frames[len(frames)*2//3].save(os.path.join(clips, slug + "-still.png"))
        segments.append(title_card(name, sc.subtitle)); segments.append(frames)
        print("clip:", slug, len(frames))
    n, size = build_reel(segments, os.path.join(OUT, "reel-posesion"))
    print("REEL:", n, "frames", size)

if __name__ == "__main__":
    main()
