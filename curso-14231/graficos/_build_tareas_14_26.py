#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las pizarras de las tareas 14..26 del curso 1-4-2-3-1 (MISTER ÉLITE)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from pitch import Pitch

OUT = HERE  # graficos/


def t14():
    # T4.1 Recepción orientada del 10 en zona 14, frente a portería con POR.
    p = Pitch(title="Tarea 14 — Recepción orientada del 10",
              subtitle="zona 14 · medio de cara entre marcador y línea", half="att")
    # zona 14 primero (debajo de las fichas)
    p.zone(28, 62, 60, 78, label="", ellipse=True)
    p.note(72, 70, "zona 14")
    # portería rival arriba
    p.player(50, 96, "POR", team="rival")
    # 9 fija arriba
    p.player(58, 86, "9", team="own", role="fija", role_below=True)
    # marcador (pivote rival) a la espalda del 10
    p.player(40, 78, "x", team="rival", role="marca a la espalda", role_below=True)
    # 10 perfilado medio de cara en zona 14
    p.player(44, 70, "10", team="own", role="medio de cara")
    # servidores 6 y 8 detrás (rotulados para que se distingan)
    p.player(32, 54, "6", team="own", role="servidor", role_below=True)
    p.player(62, 54, "8", team="own", role="servidor", role_below=True)
    p.ball(36, 52)
    # pase del pivote al 10
    p.arrow(33, 55, 43, 68, kind="pass", label="1 pase")
    # giro/conducción del 10 hacia portería
    p.arrow(46, 71, 54, 80, kind="drive", label="2 gira")
    # opción asistir al 9 a la espalda de la defensa
    p.arrow(47, 72, 57, 84, kind="pass", label="3 asiste")
    # desmarque previo en V del 10
    p.arrow(52, 66, 45, 69, kind="run", label="V")
    p.legend(["pass", "run", "drive", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-14.svg"))


def t15():
    # T4.2 "Encontrar al 10" 6v6+1, franja central entre líneas de 8 m, comodín 10 dentro.
    p = Pitch(title="Tarea 15 — Encontrar al 10 (6v6+1)",
              subtitle="franja entre líneas · pase interior vale doble", half=None)
    # franja central entre líneas (8 m) -> y 50..60 aprox
    p.zone(8, 50, 92, 60, label="")
    p.note(50, 62, "franja entre líneas · pase interior vale doble")
    # 10 comodín dentro de la franja
    p.player(40, 55, "10", team="neutral", role="comodín", role_below=True)
    # azules atacan desde abajo
    p.player(30, 24, "6", team="own")
    p.player(55, 20, "8", team="own")
    p.player(76, 28, "2", team="own")
    p.player(18, 40, "11", team="own")
    p.player(82, 42, "7", team="own")
    p.player(50, 36, "5", team="own")
    p.ball(30, 24)
    # rojos: línea de medios y de defensa por encima de la franja
    p.player(35, 66, "x", team="rival")
    p.player(65, 66, "x", team="rival")
    p.player(50, 72, "x", team="rival")
    p.player(30, 82, "x", team="rival")
    p.player(50, 86, "x", team="rival")
    p.player(70, 82, "x", team="rival")
    # circulación exterior para abrir la ventana
    p.arrow(31, 25, 53, 21, kind="pass", label="1 fija fuera")
    # pase interior filtrado al 10 en la franja
    p.arrow(54, 22, 41, 52, kind="pass", label="2 interior")
    # el 10 juega a un toque para progresar
    p.arrow(43, 56, 79, 44, kind="pass")
    p.note(70, 49, "3 al extremo", c="#ffd54a", w=700, size=9.5)
    p.legend(["pass", "neutral", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-15.svg"))


def t16():
    # T4.3 Triángulos 10-9-extremos, último tercio 4v3+POR.
    p = Pitch(title="Tarea 16 — Triángulos 10·9·extremos",
              subtitle="último tercio 4v3+POR · pared, descarga o filtrado", half="att")
    p.player(50, 96, "POR", team="rival")
    # zona 14 primero (debajo)
    p.zone(30, 58, 58, 72, label="", ellipse=True)
    p.note(70, 64, "zona 14")
    # 3 defensas rojos
    p.player(34, 84, "x", team="rival")
    p.player(66, 84, "x", team="rival")
    p.player(50, 79, "x", team="rival")
    # 9 a la espalda (hueco entre centrales)
    p.player(50, 88, "9", team="own", role="ruptura", role_below=True)
    # extremos en amplitud
    p.player(16, 70, "11", team="own")
    p.player(84, 70, "7", team="own")
    # 10 conduce a zona 14
    p.player(42, 64, "10", team="own", role="conduce")
    p.ball(42, 64)
    # pared con el 9
    p.arrow(44, 66, 49, 85, kind="pass", label="1 pared")
    # descarga al extremo
    p.arrow(44, 64, 81, 70, kind="pass", label="2 descarga")
    # filtrado a la ruptura del 9
    p.arrow(40, 66, 30, 80, kind="pass", label="3 filtra")
    p.legend(["pass", "run", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-16.svg"))


def t17():
    # T4.4 Llegada del 10 al área desde 2ª línea; centro con desdoblamiento; 3 alturas.
    p = Pitch(title="Tarea 17 — Llegada del 10 al área",
              subtitle="9 primer palo · 10 al penalti con tiempo · 8 al rechace", half="att")
    p.player(50, 97, "POR", team="rival")
    # defensa
    p.player(38, 90, "x", team="rival")
    p.player(62, 90, "x", team="rival")
    # carril de centro: extremo + lateral desdoblando por banda derecha
    p.player(78, 72, "7", team="own", role="fija dentro", role_below=True)
    p.player(90, 60, "2", team="own", role="desborda")
    p.ball(90, 60)
    p.arrow(90, 62, 86, 86, kind="drive", label="1 a fondo")
    # centro
    p.arrow(85, 88, 56, 89, kind="pass", label="2 centro")
    # 9 al primer palo
    p.player(50, 88, "9", team="own", role="1er palo", role_below=True)
    # 10 llegando desde fuera del área al penalti
    p.player(40, 62, "10", team="own", role="llega con tiempo", role_below=True)
    p.arrow(41, 64, 47, 84, kind="run", label="3 al penalti")
    # 8 al rechace del borde
    p.player(33, 58, "8", team="own", role="rechace", role_below=True)
    p.arrow(35, 60, 40, 76, kind="run")
    p.zone(34, 78, 64, 94, label="", ellipse=False)
    p.note(50, 76, "3 alturas de llegada")
    p.legend(["pass", "run", "drive", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-17.svg"))


def t18():
    # T4.5 Posesión 8v6 con el 10 hombre libre; progresión obligada por el 10; rotación.
    p = Pitch(title="Tarea 18 — Posesión con el 10 hombre libre",
              subtitle="8v6 · progresar SIEMPRE por el 10 entre líneas", half=None)
    # campo defensivo abajo, ofensivo arriba; línea divisoria conceptual en y=50
    p.zone(6, 49, 94, 61, label="")
    p.note(20, 58, "entre líneas")
    # azules estructura 1-4-2-3-1 reducida
    p.player(50, 10, "POR", team="own")
    p.player(30, 22, "5", team="own")
    p.player(70, 22, "4", team="own")
    p.player(15, 34, "3", team="own")
    p.player(85, 34, "2", team="own")
    p.player(36, 38, "6", team="own")
    p.player(60, 38, "8", team="own")
    p.ball(36, 38)
    # 10 hombre libre en la zona de enganche
    p.player(45, 55, "10", team="own", role="hombre libre")
    # extremo que entra al espacio si marcan al 10 (rotación)
    p.player(82, 52, "7", team="own", role="rotación", role_below=True)
    # rojos bloque medio (6)
    p.player(32, 46, "x", team="rival")
    p.player(62, 44, "x", team="rival")
    p.player(50, 40, "x", team="rival")
    p.player(26, 64, "x", team="rival")
    p.player(50, 68, "x", team="rival")
    p.player(72, 66, "x", team="rival")
    # progresión que pasa por el 10
    p.arrow(37, 39, 44, 52, kind="pass", label="1 al 10")
    p.arrow(48, 56, 79, 53, kind="pass", label="2 progresa")
    # rotación del extremo al espacio del 10
    p.arrow(82, 54, 56, 57, kind="run", label="entra si marcan")
    p.legend(["pass", "run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-18.svg"))


def t19():
    # T5.1 Desdoblamiento lateral-extremo por carril (banda derecha), 2v1.
    p = Pitch(title="Tarea 19 — Desdoblamiento lateral-extremo",
              subtitle="carril 2-7 · uno fija dentro, otro desborda por fuera (2v1)", half="att")
    # carril lateral derecho resaltado
    p.zone(70, 52, 98, 98, label="carril")
    # extremo fija por dentro
    p.player(74, 72, "7", team="own", role="ED 7 fija por dentro")
    # lateral aparece por fuera
    p.player(92, 66, "2", team="own", role="LD 2 desborda")
    p.ball(70, 69)
    # apoyo interior 8
    p.player(56, 64, "8", team="own")
    # lateral rival (2v1)
    p.player(82, 80, "x", team="rival", role="1 def", role_below=True)
    p.player(78, 92, "x", team="rival")
    # 2v1 sobre el lateral rival (extremo dentro + lateral fuera)
    p.zone(70, 64, 96, 84, label="", ellipse=True)
    p.note(64, 80, "2v1")
    # combinación: el extremo deja al lateral por fuera
    p.arrow(76, 73, 90, 68, kind="pass", label="1")
    # lateral a fondo
    p.arrow(92, 68, 90, 90, kind="drive", label="2 a fondo")
    # centro raso/tenso
    p.arrow(89, 91, 55, 90, kind="pass", label="3 centro raso")
    p.legend(["pass", "drive", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-19.svg"))


def t20():
    # T5.2 Amplitud máxima, 3 palos; defensa de 4 + POR.
    p = Pitch(title="Tarea 20 — Amplitud máxima · 3 palos",
              subtitle="9 1er palo · 10 penalti · extremo lejano 2º palo", half="att")
    p.player(50, 97, "POR", team="rival")
    # defensa de 4
    p.player(32, 92, "x", team="rival")
    p.player(45, 93, "x", team="rival")
    p.player(58, 93, "x", team="rival")
    p.player(72, 92, "x", team="rival")
    # 3 palos primero (debajo)
    p.zone(32, 82, 70, 95, label="")
    p.note(50, 80, "3 palos")
    # extremo del lado del centro + lateral que desdobla (derecha)
    p.player(84, 74, "7", team="own", role="fija", role_below=True)
    p.player(92, 62, "2", team="own", role="LD 2 centra", role_below=True)
    p.ball(88, 59)
    p.arrow(92, 64, 88, 84, kind="drive", label="1")
    p.arrow(86, 86, 64, 89, kind="pass", label="2 centro")
    # ocupación 3 palos
    p.player(38, 88, "9", team="own", role="1er palo", role_below=True)
    p.player(52, 84, "10", team="own", role="penalti", role_below=True)
    p.arrow(52, 76, 52, 82, kind="run")
    # extremo lejano entra al 2º palo
    p.player(16, 68, "11", team="own", role="2º palo", role_below=True)
    p.arrow(18, 70, 60, 89, kind="run", label="3 al 2º palo")
    p.legend(["pass", "run", "drive", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-20.svg"))


def t21():
    # T5.3 Amplitud abre el interior; 2 pasillos exteriores de 6 m.
    p = Pitch(title="Tarea 21 — Amplitud abre el interior",
              subtitle="extremo pisa el pasillo y fija al lateral · interior al 10/8", half=None)
    # dos pasillos exteriores de 6 m
    p.zone(0, 28, 11, 90, label="")
    p.zone(89, 28, 100, 90, label="")
    p.note(6, 84, "pasillo")
    p.note(94, 84, "pasillo")
    # azules 1-4-2-3-1
    p.player(50, 8, "POR", team="own")
    p.player(34, 20, "5", team="own")
    p.player(66, 20, "4", team="own")
    p.player(50, 32, "6", team="own")
    p.ball(50, 32)
    # 8 que llega por dentro
    p.player(38, 48, "8", team="own", role="llega por dentro", role_below=True)
    # 10 recibe por dentro
    p.player(60, 54, "10", team="own", role="interior")
    # extremo pisando pasillo (fija al lateral rival)
    p.player(6, 58, "11", team="own", role="amplitud", role_below=True)
    p.player(94, 58, "7", team="own", role="amplitud", role_below=True)
    # 9
    p.player(48, 74, "9", team="own")
    # rojos bloque + laterales fijados en los pasillos
    p.player(18, 62, "x", team="rival", role="fijado", role_below=True)
    p.player(82, 62, "x", team="rival", role="fijado", role_below=True)
    p.player(42, 64, "x", team="rival")
    p.player(58, 66, "x", team="rival")
    p.player(48, 84, "x", team="rival")
    # progresión por dentro al 10
    p.arrow(50, 34, 58, 52, kind="pass", label="2 interior")
    # extremo abre para fijar
    p.arrow(22, 56, 10, 58, kind="run", label="1 abro")
    # interior abierto: gol por dentro vale doble
    p.arrow(60, 56, 50, 72, kind="pass", label="3 al 9 (doble)")
    p.legend(["pass", "run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-21.svg"))


def t22():
    # T5.4 Ataque del área con tercer hombre; último tercio 6v5+POR.
    p = Pitch(title="Tarea 22 — Ataque del área · tercer hombre",
              subtitle="pase-pared-pase a un tercero en movimiento", half="att")
    p.player(50, 97, "POR", team="rival")
    # 5 defensas
    p.player(30, 86, "x", team="rival")
    p.player(44, 89, "x", team="rival")
    p.player(56, 89, "x", team="rival")
    p.player(70, 86, "x", team="rival")
    p.player(50, 78, "x", team="rival")
    # azules: 7, 2, 9, 10, 8
    p.player(84, 68, "7", team="own")
    p.player(92, 58, "2", team="own")
    p.player(58, 68, "9", team="own", role="apoyo", role_below=True)
    p.player(40, 60, "10", team="own", role="3er hombre", role_below=True)
    p.player(30, 54, "8", team="own")
    p.ball(30, 54)
    # tercer hombre: 8 -> 9 (pared) -> 10 que aparece
    p.arrow(31, 55, 56, 67, kind="pass")
    p.note(48, 58, "1", c="#ffd54a", w=700, size=9.5)
    p.arrow(57, 66, 43, 62, kind="pass", label="2 pared")
    p.arrow(43, 62, 60, 82, kind="run", label="3 al tercero")
    # llegada escalonada del 8
    p.arrow(30, 56, 46, 76, kind="run")
    p.zone(36, 76, 66, 93, label="")
    p.note(50, 74, "ataque escalonado")
    p.legend(["pass", "run", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-22.svg"))


def t23():
    # T6.1 Transición A-D (repliegue a 1-4-4-2). 7 y 11 bajan, doble pivote frena.
    p = Pitch(title="Tarea 23 — Transición A-D · repliegue",
              subtitle="7 y 11 bajan · doble pivote frena · dos líneas de 4", half=None)
    # balón perdido arriba (zona rival)
    p.player(50, 70, "x", team="rival", role="recupera")
    p.ball(50, 70)
    # extremos bajando a formar línea de medios
    p.player(20, 70, "11", team="own")
    p.player(80, 70, "7", team="own")
    p.arrow(20, 68, 22, 50, kind="run", label="baja")
    p.arrow(80, 68, 78, 50, kind="run", label="baja")
    # doble pivote frena el balón en el centro
    p.player(42, 52, "6", team="own", role="frena", role_below=True)
    p.player(58, 52, "8", team="own")
    p.arrow(50, 56, 50, 66, kind="block")
    # línea de 4 medios (resultado): 11 6 8 7
    p.note(50, 46, "línea de 4 — medios")
    # línea de 4 defensa
    p.player(18, 32, "3", team="own")
    p.player(40, 30, "5", team="own")
    p.player(60, 30, "4", team="own")
    p.player(82, 32, "2", team="own")
    p.player(50, 12, "POR", team="own")
    p.note(50, 24, "línea de 4 — defensa")
    # 9 y 10 arriba
    p.player(44, 64, "10", team="own")
    p.player(56, 78, "9", team="own")
    # regla: no progresar entre líneas hasta formarse
    p.zone(10, 34, 90, 50, label="cerrado hasta formar 1-4-4-2", ellipse=False)
    p.legend(["run", "block", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-23.svg"))


def t24():
    # T6.2 Transición D-A; primer pase al 9 (apoyo) o al 10; extremos suben.
    p = Pitch(title="Tarea 24 — Transición D-A · salida rápida",
              subtitle="primer pase al frente (9 apoyo / 10 entre líneas)", half=None)
    # recuperación en bloque 1-4-4-2 (medio campo)
    p.player(50, 12, "POR", team="own")
    p.player(18, 30, "3", team="own")
    p.player(40, 28, "5", team="own")
    p.player(60, 28, "4", team="own")
    p.player(82, 30, "2", team="own")
    # doble pivote / medios que recuperan
    p.player(42, 46, "6", team="own", role="recupera", role_below=True)
    p.player(58, 46, "8", team="own")
    p.ball(42, 46)
    # extremos volviendo a la altura de ataque
    p.player(18, 50, "11", team="own")
    p.player(82, 50, "7", team="own")
    p.arrow(18, 52, 24, 76, kind="run", label="sube")
    p.arrow(82, 52, 76, 76, kind="run", label="sube")
    # 9 que se apoya
    p.player(58, 64, "9", team="own", role="apoyo", role_below=True)
    # 10 entre líneas
    p.player(36, 62, "10", team="own", role="entre líneas", role_below=True)
    # primer pase hacia delante (al 9 o al 10)
    p.arrow(40, 48, 36, 59, kind="pass", label="1 al 10")
    p.arrow(46, 47, 56, 61, kind="pass")
    p.note(62, 53, "o al 9", c="#ffd54a", w=700, size=9.5)
    # 10 conecta con ruptura
    p.arrow(38, 64, 68, 80, kind="pass", label="2 ruptura")
    # rivales replegando
    p.player(44, 80, "x", team="rival")
    p.player(64, 82, "x", team="rival")
    p.player(54, 92, "x", team="rival")
    p.legend(["pass", "run", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-24.svg"))


def t25():
    # T6.3 Doble transición A-D-A; ciclo en flechas con mini-porterías de contra.
    p = Pitch(title="Tarea 25 — Doble transición A-D-A",
              subtitle="ataque (1-4-2-3-1) → pérdida → repliegue (1-4-4-2) → ataque", half=None)
    # mini-porterías de contra
    p.goalmini(15, 50)
    p.goalmini(85, 50)
    # FASE 1 ataque 1-4-2-3-1 (abajo->arriba): mostramos el frente ofensivo
    p.player(35, 74, "10", team="own", role="ataca (1-4-2-3-1)", role_below=True)
    p.player(50, 84, "9", team="own")
    p.ball(35, 74)
    p.arrow(36, 75, 49, 83, kind="pass", label="1 ataque")
    # FASE 2 pérdida
    p.player(50, 88, "x", team="rival", role="roba")
    p.note(64, 88, "2 pérdida")
    # FASE 3 repliegue a 1-4-4-2 (extremos bajan)
    p.player(22, 58, "11", team="own")
    p.player(78, 58, "7", team="own")
    p.arrow(22, 70, 22, 61, kind="run", label="3 baja")
    p.arrow(78, 70, 78, 61, kind="run", label="3 baja")
    p.player(42, 52, "6", team="own")
    p.player(58, 52, "8", team="own")
    p.note(50, 46, "repliegue 1-4-4-2")
    # línea defensa
    p.player(25, 32, "3", team="own")
    p.player(45, 30, "5", team="own")
    p.player(55, 30, "4", team="own")
    p.player(75, 32, "2", team="own")
    p.player(50, 12, "POR", team="own")
    # FASE 4 recuperación + ataque rápido a mini-portería
    p.arrow(50, 50, 84, 50, kind="drive", label="4 ataque rápido")
    p.zone(8, 26, 92, 44, label="forma 1-4-4-2", ellipse=False)
    p.legend(["pass", "run", "drive", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-25.svg"))


def t26():
    # T6.4 Partido condicionado 11v11; ambos en 1-4-2-3-1; resaltar zonas que premian.
    p = Pitch(title="Tarea 26 — Partido condicionado 11v11",
              subtitle="ambos en 1-4-2-3-1 · condiciones del sistema", half=None)
    # AZUL (own) ataca hacia arriba — 1-4-2-3-1
    p.player(50, 6, "POR", team="own")
    p.player(20, 16, "3", team="own"); p.player(40, 14, "5", team="own")
    p.player(60, 14, "4", team="own"); p.player(80, 16, "2", team="own")
    p.player(40, 26, "6", team="own"); p.player(60, 26, "8", team="own")
    p.player(18, 38, "11", team="own"); p.player(82, 38, "7", team="own")
    p.player(50, 40, "10", team="own"); p.player(58, 52, "9", team="own")
    # ROJO (rival) — 1-4-2-3-1 espejo
    p.player(50, 94, "POR", team="rival")
    p.player(80, 84, "x", team="rival"); p.player(60, 86, "x", team="rival")
    p.player(40, 86, "x", team="rival"); p.player(20, 84, "x", team="rival")
    p.player(60, 74, "x", team="rival"); p.player(40, 74, "x", team="rival")
    p.player(82, 62, "x", team="rival"); p.player(18, 62, "x", team="rival")
    p.player(50, 60, "x", team="rival"); p.player(50, 70, "x", team="rival")
    # zonas que premian las condiciones
    p.zone(32, 44, 68, 56, label="", ellipse=True)
    p.note(50, 47, "pase por el 10 = gol doble")
    p.zone(10, 10, 90, 22, label="salida limpia = +1")
    p.zone(37, 60, 63, 77, label="", ellipse=True)
    p.note(50, 73, "robo 9+10 = +1")
    p.legend(["own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-26.svg"))


if __name__ == "__main__":
    for fn in [t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26]:
        path = None
        fn()
    print("OK: tareas 14..26 generadas")
