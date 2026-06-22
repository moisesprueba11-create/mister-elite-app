#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los 14 diagramas de teoría del curso 1-3-4-3 (MISTER ÉLITE)."""
import sys, os
sys.path.insert(0, '/home/user/mister-elite-app/curso-1343/graficos/lib')
from pitch import Pitch

OUT = "/home/user/mister-elite-app/curso-1343/graficos"

# ---- posiciones base (campo completo, ataque hacia arriba) ----
# x: 0 izq .. 100 der ; y: 0 fondo propio .. 100 fondo rival


def t01_estructura():
    p = Pitch(title="Estructura base 1-3-4-3",
              subtitle="Tres lineas, cuatro alturas · POR 1 · DFC 4-5-6 · CAR 2/3 · MC 8/10 · tridente 7-9-11")
    # POR
    p.player(50, 8, "1", role="POR")
    # Linea de 3 centrales (izq->der: 6, 5, 4)
    p.player(28, 24, "6", role="DFC")
    p.player(50, 21, "5", role="DFC libero", role_below=True)
    p.player(72, 24, "4", role="DFC")
    # Carrileros abiertos (3 izq, 2 der) a media altura
    p.player(11, 46, "3", role="CAR")
    p.player(89, 46, "2", role="CAR")
    # Doble pivote escalonado (8 mas bajo, 10 mas alto)
    p.player(40, 42, "8", role="MC")
    p.player(60, 54, "10", role="MC")
    # Tridente (EI 11 izq, DC 9 centro, ED 7 der)
    p.player(22, 74, "11", role="EI", role_below=True)
    p.player(50, 80, "9", role="DC", role_below=True)
    p.player(78, 74, "7", role="ED", role_below=True)
    p.legend(["own"])
    p.save(f"{OUT}/teoria-01-estructura.svg")


def t01_mutacion_325():
    p = Pitch(title="Mutacion con balon: 1-3-4-3 → 1-3-2-5",
              subtitle="Los carrileros 2 y 3 suben a la linea de 5 · cinco carriles ocupados")
    p.player(50, 9, "1", role="POR")
    # Bloque 3+1 detras
    p.player(30, 26, "6", role="DFC")
    p.player(50, 23, "5", role="DFC")
    p.player(70, 26, "4", role="DFC")
    p.player(50, 41, "8", role="MC pivote", role_below=True)
    # 10 enlace flotante
    p.player(58, 55, "10", role="MC enlace")
    # Linea de 5 atacante (5 carriles): CAR3 · EI11 · DC9 · ED7 · CAR2
    p.player(10, 78, "3", role="CAR", role_below=True)
    p.player(30, 80, "11", role="EI", role_below=True)
    p.player(50, 82, "9", role="DC", role_below=True)
    p.player(70, 80, "7", role="ED", role_below=True)
    p.player(90, 78, "2", role="CAR", role_below=True)
    # flechas de subida de carrileros
    p.arrow(11, 48, 10, 73, kind="run")
    p.arrow(89, 48, 90, 73, kind="run")
    # carriles guia
    for cx in (20, 40, 60, 80):
        p._line(p.X(cx), p.Y(58), p.X(cx), p.Y(96), w=1.2, c="#ffffff", dash="3 6", opacity=0.35)
    p.note(50, 67, "5 carriles ocupados")
    p.legend(["run", "own"])
    p.save(f"{OUT}/teoria-01-mutacion-325.svg")


def t01_linea5():
    p = Pitch(title="Mutacion sin balon: linea de 3 → linea de 5",
              subtitle="Los carrileros bajan · bloque 1-5-2-3 · orden visual 3-6-5-4-2")
    p.player(50, 8, "1", role="POR")
    # Linea de 5 (izq->der: 3, 6, 5, 4, 2)
    p.player(12, 26, "3", role="CAR")
    p.player(31, 24, "6", role="DFC")
    p.player(50, 23, "5", role="DFC libero", role_below=True)
    p.player(69, 24, "4", role="DFC")
    p.player(88, 26, "2", role="CAR")
    # Doble pivote
    p.player(38, 42, "8", role="MC")
    p.player(62, 42, "10", role="MC")
    # Tridente arriba
    p.player(26, 64, "11", role="EI", role_below=True)
    p.player(50, 68, "9", role="DC", role_below=True)
    p.player(74, 64, "7", role="ED", role_below=True)
    # flechas de bajada de carrileros
    p.arrow(12, 44, 12, 30, kind="run")
    p.arrow(88, 44, 88, 30, kind="run")
    p.zone(6, 18, 94, 31, label="linea de 5", fill_op=0.10)
    p.legend(["run", "own", "zone"])
    p.save(f"{OUT}/teoria-01-linea5.svg")


def t01_distancias():
    p = Pitch(title="Distancias de referencia (estandar unico)",
              subtitle="Centrales 8-12 m · doble pivote 6-10 m · entre lineas 10-15 m · bloque < 35-40 m")
    p.player(50, 10, "1", role="POR")
    # linea de 3
    p.player(30, 28, "6")
    p.player(50, 26, "5")
    p.player(70, 28, "4")
    # doble pivote
    p.player(42, 44, "8")
    p.player(58, 54, "10")
    # tridente
    p.player(26, 70, "11")
    p.player(50, 74, "9")
    p.player(74, 70, "7")
    # cota separacion centrales 8-12 m
    p._line(p.X(30), p.Y(33), p.X(70), p.Y(33), w=2, c="#7ee0ff", dash="5 4")
    p.note(50, 35, "8-12 m centrales")
    # cota doble pivote 6-10 m
    p._line(p.X(42), p.Y(46), p.X(58), p.Y(52), w=2, c="#7ee0ff", dash="5 4")
    p.note(40, 50, "6-10 m", anchor="end")
    p.note(40, 53, "doble pivote", anchor="end")
    # entre lineas 10-15 m (vertical, lado izq)
    p._line(p.X(14), p.Y(28), p.X(14), p.Y(70), w=2, c="#7ee0ff", dash="5 4")
    p.note(18, 49, "10-15 m", anchor="start")
    p.note(18, 52, "entre lineas", anchor="start")
    # bloque total < 35-40 m (vertical, lado der)
    p._line(p.X(90), p.Y(28), p.X(90), p.Y(74), w=2.4, c="#ffd54a")
    p.note(86, 51, "< 35-40 m", anchor="end")
    p.note(86, 54, "bloque total", anchor="end")
    # POR adelantado 14-18 m
    p._line(p.X(50), p.Y(2), p.X(50), p.Y(10), w=2, c="#ffffff", dash="4 4")
    p.note(57, 6, "POR 14-18 m", anchor="start")
    p.save(f"{OUT}/teoria-01-distancias.svg")


def t01_vs_433():
    p = Pitch(title="1-3-4-3 vs 1-4-3-3",
              subtitle="3 centrales vs 1 punta (3v1 · 4v3 con POR) · carrileros generan 2v1 a los laterales")
    # PROPIO (azul) abajo, atacando hacia arriba
    p.player(50, 10, "1", role="POR")
    p.player(30, 26, "6", role="DFC")
    p.player(50, 23, "5", role="DFC")
    p.player(70, 26, "4", role="DFC")
    p.player(12, 46, "3", role="CAR")
    p.player(88, 46, "2", role="CAR")
    p.player(40, 40, "8")
    p.player(62, 42, "10")
    # RIVAL 4-3-3 (rojo) arriba, su ataque baja
    # 1 punta presiona los 3 centrales
    p.player(50, 36, "9", team="rival", role="punta", role_below=True)
    # 3 medios rivales
    p.player(33, 54, "6", team="rival")
    p.player(50, 62, "8", team="rival")
    p.player(67, 54, "10", team="rival")
    # laterales rivales (los que sufren el 2v1) — LD rival a su izq (nuestra der)
    p.player(20, 60, "3", team="rival", role="LI rival", role_below=True)
    p.player(80, 60, "2", team="rival", role="LD rival", role_below=True)
    # superioridad 3v1
    p.zone(22, 18, 78, 30, label="3 v 1", fill_op=0.12)
    # 2v1 en banda derecha (CAR 2 + ED) sobre el lateral rival
    p.zone(70, 50, 94, 74, label="2 v 1", fill_op=0.12, c="#7ee0ff")
    p.arrow(84, 50, 82, 66, kind="run")
    p.legend(["own", "rival", "zone"])
    p.save(f"{OUT}/teoria-01-vs-433.svg")


# =================== MODULO 2 · FASE DEFENSIVA ===================

def t02_paso_3_a_5():
    p = Pitch(title="El paso de linea de 3 a linea de 5",
              subtitle="Los carrileros 2 y 3 retroceden y se alinean con DFC 4-5-6 · basculacion, no carrera frontal")
    p.player(50, 8, "1", role="POR")
    # destino: linea de 5 (3-6-5-4-2)
    p.player(12, 26, "3", role="CAR")
    p.player(31, 24, "6", role="DFC")
    p.player(50, 23, "5", role="DFC libero", role_below=True)
    p.player(69, 24, "4", role="DFC")
    p.player(88, 26, "2", role="CAR")
    # doble pivote
    p.player(38, 42, "8", role="MC")
    p.player(62, 42, "10", role="MC")
    # tridente arriba
    p.player(26, 64, "11", role="EI", role_below=True)
    p.player(50, 68, "9", role="DC", role_below=True)
    p.player(74, 64, "7", role="ED", role_below=True)
    # posicion previa (alta) de los carrileros, marcada en gris claro
    p.note(13, 50, "CAR alto")
    p.note(87, 50, "CAR alto")
    # flechas de retroceso/basculacion (diagonales hacia dentro y atras)
    p.arrow(14, 48, 12, 31, kind="run", label="retrocede")
    p.arrow(86, 48, 88, 31, kind="run", label="retrocede")
    p.zone(6, 18, 94, 31, label="linea de 5", fill_op=0.10)
    p.legend(["run", "own", "zone"])
    p.save(f"{OUT}/teoria-02-paso-3-a-5.svg")


def t02_pressing_gatillos():
    p = Pitch(title="Pressing orientado: gatillos del tridente",
              subtitle="El 9 curva su carrera tapando el pase entre centrales · el 7 salta al receptor · balon a la banda-trampa")
    # RIVAL (rojo) saliendo desde abajo en su campo (parte alta de la pizarra)
    # central rivales y portero abajo (su fondo arriba)
    p.player(40, 88, "C", team="rival", role="central")
    p.player(60, 88, "C", team="rival", role="central")
    # carrilero/lateral rival receptor en banda derecha (nuestra der)
    p.player(86, 74, "L", team="rival", role="lateral")
    # pivote rival
    p.player(50, 70, "P", team="rival", role="pivote", role_below=True)
    p.ball(60, 88)
    # PROPIO presionando (atacan hacia arriba)
    # 9 curva su carrera tapando el pasillo entre centrales
    p.player(50, 78, "9", role="DC")
    p.arrow(50, 78, 62, 86, kind="run", label="curva")
    # 7 (ED) salta al receptor de banda
    p.player(74, 64, "7", role="ED")
    p.arrow(76, 66, 84, 73, kind="run", label="salta")
    # 11 cierra el lado debil
    p.player(24, 64, "11", role="EI")
    # cobertura del 8 (interior) y del DFC de lado
    p.player(58, 56, "8", role="MC cobertura", role_below=True)
    p.player(70, 50, "4", role="DFC sube", role_below=True)
    p.player(46, 46, "10", role="MC")
    # banda-trampa
    p.zone(74, 58, 96, 92, fill_op=0.14, c="#ff5252")
    p.note(85, 90, "banda-trampa", c="#ffd6d6")
    # corte del pase interior (9 tapa el pase al pivote)
    p.arrow(46, 76, 50, 72, kind="block")
    p.legend(["run", "block", "own", "rival", "zone"])
    p.save(f"{OUT}/teoria-02-pressing-gatillos.svg")


def t02_basculacion():
    p = Pitch(title="Basculacion de la linea de 5",
              subtitle="Toda la linea se desplaza al lado del balon · el carrilero lejano se cierra como 5.o defensor · uno salta, dos cubren")
    p.player(46, 8, "1", role="POR")
    # balon en banda derecha rival
    p.ball(86, 56)
    p.player(86, 60, "R", team="rival", role="portador", role_below=True)
    # linea de 5 basculada al lado del balon (der): todos desplazados a la derecha
    p.player(34, 26, "3", role="CAR cierra", role_below=True)   # lado debil cerrado dentro
    p.player(50, 25, "6", role="DFC")
    p.player(64, 26, "5", role="DFC")
    p.player(76, 30, "4", role="DFC")
    p.player(90, 40, "2", role="CAR salta", role_below=True)    # salta al portador
    # flecha salto del carrilero del lado del balon
    p.arrow(90, 42, 88, 54, kind="run", label="salta")
    # flecha de cierre del carrilero lejano
    p.arrow(20, 28, 32, 26, kind="run", label="cierra dentro")
    # doble pivote tambien bascula
    p.player(55, 42, "8", role="MC")
    p.player(70, 46, "10", role="MC")
    # zona del lado del balon
    p.zone(60, 16, 98, 52, fill_op=0.10, c="#7ee0ff")
    p.note(80, 33, "lado del balon")
    p.note(27, 20, "lado debil vacio")
    p.legend(["run", "own", "rival", "zone"])
    p.save(f"{OUT}/teoria-02-basculacion.svg")


# =================== MODULO 3 · FASE OFENSIVA ===================

def t03_salida():
    p = Pitch(title="Salida desde atras: rombo 3+1",
              subtitle="POR 1 + DFC 4-5-6 forman el rombo · MC 8 vertice superior · carrileros 2/3 amplitud alta · superioridad 3v2")
    p.player(50, 9, "1", role="POR")
    # linea de 3 abierta
    p.player(26, 24, "6", role="DFC")
    p.player(50, 22, "5", role="DFC libero", role_below=True)
    p.player(74, 24, "4", role="DFC")
    # 8 vertice superior del rombo
    p.player(50, 40, "8", role="MC vertice", role_below=True)
    # carrileros amplitud ALTA
    p.player(10, 52, "3", role="CAR")
    p.player(90, 52, "2", role="CAR")
    # 10 entre lineas
    p.player(58, 56, "10", role="MC")
    # rival: 2 puntas presionando (3v2)
    p.player(40, 36, "9", team="rival")
    p.player(60, 36, "9", team="rival")
    # lineas del rombo (POR-6-8-4 con 5)
    p.arrow(50, 12, 50, 19, kind="pass")
    p.arrow(50, 25, 50, 37, kind="pass")
    # libero conduce
    p.arrow(50, 25, 44, 33, kind="drive", label="5 conduce")
    p.zone(20, 18, 80, 28, label="3 v 2", fill_op=0.12)
    p.legend(["pass", "drive", "own", "rival", "zone"])
    p.save(f"{OUT}/teoria-03-salida.svg")


def t03_mutacion():
    p = Pitch(title="Construccion y mutacion a 1-3-2-5",
              subtitle="Carrileros suben · bloque 3+1 (DFC 4-5-6 + MC 8) detras · el 10 enlace flotante · 5 carriles")
    p.player(50, 9, "1", role="POR")
    # bloque 3+1
    p.player(30, 25, "6", role="DFC")
    p.player(50, 22, "5", role="DFC")
    p.player(70, 25, "4", role="DFC")
    p.player(50, 40, "8", role="MC pivote", role_below=True)
    # 10 enlace flotante
    p.player(60, 54, "10", role="MC enlace")
    # linea de 5 atacante
    p.player(10, 76, "3", role="CAR", role_below=True)
    p.player(30, 78, "11", role="EI", role_below=True)
    p.player(50, 80, "9", role="DC", role_below=True)
    p.player(70, 78, "7", role="ED", role_below=True)
    p.player(90, 76, "2", role="CAR", role_below=True)
    p.arrow(11, 50, 10, 71, kind="run")
    p.arrow(89, 50, 90, 71, kind="run")
    # enlace flotante: 10 conecta atras-adelante
    p.arrow(50, 44, 58, 51, kind="pass")
    p.arrow(60, 58, 68, 73, kind="pass")
    for cx in (20, 40, 60, 80):
        p._line(p.X(cx), p.Y(60), p.X(cx), p.Y(94), w=1.2, c="#ffffff", dash="3 6", opacity=0.30)
    p.note(50, 65, "5 carriles ocupados")
    p.legend(["run", "pass", "own"])
    p.save(f"{OUT}/teoria-03-mutacion.svg")


def t03_ultimo_tercio():
    p = Pitch(title="Ultimo tercio: desdoblamiento y ataque del area",
              subtitle="2v1 CAR+extremo al lateral · 5 referencias al area (9 1.er palo · extremo 2.o palo · 10 frontal · carrilero contrario)",
              half="att")
    # banda derecha: desdoblamiento CAR 2 (fuera) + ED 7 (dentro) -> 2v1
    p.player(92, 66, "2", role="CAR sobra", role_below=True)
    p.player(76, 70, "7", role="ED dentro", role_below=True)
    p.player(82, 60, "L", team="rival", role="lateral", role_below=True)
    p.zone(72, 58, 98, 76, label="2 v 1", fill_op=0.12, c="#7ee0ff")
    # extremo pisa dentro, carrilero sobra por fuera y centra
    p.arrow(76, 72, 70, 82, kind="run")
    p.arrow(92, 68, 92, 80, kind="run")
    p.arrow(92, 82, 60, 90, kind="pass", label="centro")
    # ataque del area, 5 referencias
    p.player(56, 92, "9", role="1.er palo", role_below=True)        # 9 primer palo
    p.player(40, 90, "11", role="2.o palo", role_below=True)        # extremo lejano 2o palo
    p.player(54, 80, "10", role="frontal", role_below=True)         # 10 frontal/rechace
    p.player(30, 74, "3", role="carrilero contrario", role_below=True)  # carrilero del lado debil
    p.legend(["run", "pass", "own", "rival", "zone"])
    p.save(f"{OUT}/teoria-03-ultimo-tercio.svg")


# =================== MODULO 4 · TRANSICIONES Y ABP ===================

def t04_transicion_of():
    p = Pitch(title="Transicion ofensiva tras robo",
              subtitle="Extremos 7/11 y DC 9 atacan la profundidad · carrileros 2/3 lanzados por fuera · 3 centrales + MC 8 sostienen")
    p.ball(50, 50)
    # robo en zona media
    p.player(50, 47, "10", role="recupera", role_below=True)
    # tridente ataca profundidad
    p.player(28, 68, "11", role="EI", role_below=True)
    p.player(50, 70, "9", role="DC", role_below=True)
    p.player(72, 68, "7", role="ED", role_below=True)
    # carreras de ruptura (arrancan por delante de las fichas)
    p.arrow(24, 76, 24, 90, kind="run")
    p.arrow(54, 78, 54, 92, kind="run")
    p.arrow(76, 76, 76, 90, kind="run")
    # carrileros lanzados por fuera
    p.player(12, 56, "3", role="CAR lanzado", role_below=True)
    p.player(88, 56, "2", role="CAR lanzado", role_below=True)
    p.arrow(12, 62, 12, 84, kind="run")
    p.arrow(88, 62, 88, 84, kind="run")
    # primer pase vertical
    p.arrow(50, 47, 50, 64, kind="pass", label="profundidad")
    # equilibrio: 3 centrales + 8
    p.player(30, 26, "6", role="DFC")
    p.player(50, 22, "5", role="DFC")
    p.player(70, 26, "4", role="DFC")
    p.player(50, 36, "8", role="MC resto", role_below=True)
    p.zone(20, 15, 80, 30, fill_op=0.10, c="#7ee0ff")
    p.note(50, 17, "equilibrio 3+1")
    p.legend(["run", "pass", "own", "zone"])
    p.save(f"{OUT}/teoria-04-transicion-of.svg")


def t04_transicion_def():
    p = Pitch(title="Transicion defensiva desde 1-3-2-5",
              subtitle="Frenar → replegar → reorganizar · carrileros vuelan a la linea de 5 · el 8 frena, el 5 ordena")
    # perdida arriba; rival con balon ataca hacia abajo (su sentido es hacia nuestro marco)
    p.ball(50, 64)
    p.player(50, 68, "R", team="rival", role="contra", role_below=True)
    # 8 frena el contra
    p.player(50, 54, "8", role="MC frena", role_below=True)
    p.arrow(50, 52, 50, 62, kind="run")
    p.arrow(50, 60, 50, 56, kind="block")
    # carrileros vuelan a reformar la linea de 5 (desde arriba a su sitio bajo)
    p.player(20, 40, "3", role="CAR vuela", role_below=True)
    p.player(80, 40, "2", role="CAR vuela", role_below=True)
    p.arrow(14, 64, 14, 30, kind="run")
    p.arrow(86, 64, 86, 30, kind="run")
    # extremos repliegan
    p.player(34, 48, "11", role="repliega")
    p.player(66, 48, "7", role="repliega")
    p.arrow(34, 56, 34, 44, kind="run")
    p.arrow(66, 56, 66, 44, kind="run")
    # linea de 3 -> 5 (5 ordena)
    p.player(32, 24, "6", role="DFC")
    p.player(50, 22, "5", role="DFC ordena", role_below=True)
    p.player(68, 24, "4", role="DFC")
    p.zone(6, 16, 94, 30, label="reformar linea de 5", fill_op=0.10)
    p.note(50, 36, "frenar - replegar - reorganizar")
    p.legend(["run", "block", "own", "rival", "zone"])
    p.save(f"{OUT}/teoria-04-transicion-def.svg")


def t04_corner_of():
    p = Pitch(title="Corner ofensivo",
              subtitle="Rematan DFC 4, 6 + DC 9 (+10) · resto: DFC 5 + carrileros 2/3 mini-linea de 3 · MC 8 al borde del rechace",
              half="att")
    # corner desde la esquina derecha (rival fondo arriba)
    p.ball(99, 99)
    p.player(96, 96, "11", role="lanza", role_below=True)
    p.arrow(97, 97, 60, 92, kind="pass", label="centro")
    # rematadores en el area
    p.player(58, 93, "9", role="1.er palo", role_below=True)
    p.player(48, 90, "4", role="DFC remate", role_below=True)
    p.player(38, 92, "6", role="DFC remate", role_below=True)
    p.player(54, 84, "10", role="llega", role_below=True)
    # 8 al borde para el rechace
    p.player(50, 74, "8", role="borde / rechace", role_below=True)
    # resto de corner: mini-linea de 3 (5 + carrileros)
    p.player(30, 62, "3", role="CAR resto", role_below=True)
    p.player(50, 60, "5", role="DFC ancla", role_below=True)
    p.player(70, 62, "2", role="CAR resto", role_below=True)
    p.zone(22, 56, 78, 66, label="resto: mini-linea de 3", fill_op=0.10, c="#7ee0ff")
    p.legend(["pass", "own", "zone"])
    p.save(f"{OUT}/teoria-04-corner-of.svg")


if __name__ == "__main__":
    fns = [t01_estructura, t01_mutacion_325, t01_linea5, t01_distancias, t01_vs_433,
           t02_paso_3_a_5, t02_pressing_gatillos, t02_basculacion,
           t03_salida, t03_mutacion, t03_ultimo_tercio,
           t04_transicion_of, t04_transicion_def, t04_corner_of]
    for f in fns:
        f(); print("OK", f.__name__)
