#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera tarea-01..13.svg para el curso 1-5-3-2 (MISTER ÉLITE)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from pitch import Pitch

OUT = HERE  # graficos/

def save(p, n):
    p.save(os.path.join(OUT, f"tarea-{n:02d}.svg"))
    print(f"tarea-{n:02d}.svg")

# =====================================================================
# T1 — Salida 3+POR vs 2: superioridad de la primera línea
# =====================================================================
def t01():
    p = Pitch(title="Tarea 1 — Salida 3+POR vs 2",
              subtitle="aprovechar la superioridad de la primera línea (3v2)", half="def")
    # zonas de progresión al frente (40 m ~ y 44)
    p.zone(8, 40, 38, 48, label="zona progresión")
    p.zone(62, 40, 92, 48, label="zona progresión")
    # portero
    p.player(50, 5, "1", team="own", role="POR")
    # 3 centrales abiertos, escalonados: 4 y 6 a la altura del área, 5 un paso por delante centro
    p.player(24, 17, "6", team="own", role="DFC")
    p.player(50, 21, "5", team="own", role="líbero")
    p.player(76, 17, "4", team="own", role="DFC")
    # pivote ofreciéndose entre líneas
    p.player(50, 33, "8", team="own", role="pivote")
    # interior que aparece
    p.player(70, 34, "7", team="own", role="INT")
    # carrileros altísimos dando amplitud
    p.player(8, 30, "3", team="own", role="CAR")
    p.player(92, 30, "2", team="own", role="CAR")
    # 2 DC rivales presionando
    p.player(40, 28, "DC", team="rival")
    p.player(60, 28, "DC", team="rival")
    # balón en portero
    p.ball(50, 7)
    # conducción del líbero (fija) + vías de pase
    p.arrow(50, 24, 50, 30, kind="drive", label="conduce 5")
    p.arrow(50, 22, 70, 33, kind="pass")          # a interior espalda
    p.arrow(24, 19, 9, 30, kind="pass")           # a carrilero izq
    p.arrow(76, 19, 91, 30, kind="pass")          # a carrilero der
    p.note(50, 46, "")
    p.legend(["pass", "drive", "own", "rival", "zone"])
    save(p, 1)

# =====================================================================
# T2 — Rondo de salida 3v2 + carriles
# =====================================================================
def t02():
    p = Pitch(title="Tarea 2 — Rondo de salida 3+1 vs 2",
              subtitle="tres carriles: progresar por dentro o por fuera", half=None)
    # tres carriles verticales (conos / franjas)
    p.zone(0, 6, 30, 94)
    p.zone(35, 6, 65, 94)
    p.zone(70, 6, 100, 94)
    p.note(15, 90, "carril exterior", c="#fff5cc")
    p.note(50, 90, "carril central", c="#fff5cc")
    p.note(85, 90, "carril exterior", c="#fff5cc")
    # conos delimitando carriles
    for yy in (12, 30, 48, 66, 84):
        p.cone(30, yy); p.cone(35, yy); p.cone(65, yy); p.cone(70, yy)
    # 3 centrales + pivote: RONDO COMPACTO 3+1 en el carril central (cuadro)
    # los 3 DFC forman la base y el pivote remata el cuadro arriba
    p.player(42, 38, "6", team="own", role="DFC")          # esquina inf-izq
    p.player(58, 38, "4", team="own", role="DFC")          # esquina inf-der
    p.player(50, 32, "5", team="own", role="")             # base centro
    p.note(50, 27, "líbero (5)", c="#fff5cc")
    p.player(50, 56, "8", team="own", role="pivote")       # vértice superior
    # 2 DC rivales DENTRO del cuadro (los que persiguen el balón)
    p.player(46, 47, "DC", team="rival")
    p.player(55, 48, "DC", team="rival")
    # carrileros fijos exteriores
    p.player(15, 47, "3", team="own", role="CAR")
    p.player(85, 47, "2", team="own", role="CAR")
    # balón y circulación dentro del rondo y apertura a banda
    p.ball(46, 35)
    p.arrow(44, 36, 56, 36, kind="pass")                   # base izq->der
    p.arrow(58, 40, 84, 46, kind="pass", label="abre a banda")  # central->carrilero
    p.arrow(85, 51, 85, 70, kind="drive", label="salida liberada")
    p.arrow(50, 54, 50, 41, kind="pass")                   # pivote->base
    p.legend(["pass", "drive", "own", "rival"])
    save(p, 2)

# =====================================================================
# T3 — Construcción con cuatro salidas
# =====================================================================
def t03():
    p = Pitch(title="Tarea 3 — Construcción con 4 salidas",
              subtitle="elegir la vía libre: bandas, entrelíneas o profundidad", half=None)
    # 4 zonas-meta
    p.zone(2, 42, 22, 62, label="banda izq")
    p.zone(78, 42, 98, 62, label="banda der")
    p.zone(40, 52, 60, 64, label="entrelíneas")
    p.zone(40, 80, 60, 94, label="profundidad")
    # bloque de salida
    p.player(50, 6, "1", team="own", role="POR")
    p.player(28, 18, "6", team="own", role="DFC")
    p.player(50, 22, "5", team="own", role="líbero")
    p.player(72, 18, "4", team="own", role="DFC")
    p.player(42, 38, "8", team="own", role="pivote")
    p.player(64, 46, "7", team="own", role="INT")
    p.player(10, 40, "3", team="own", role="CAR")
    p.player(90, 40, "2", team="own", role="CAR")
    # delantero que cae a profundidad/apoyo
    p.player(46, 73, "9", team="own", role="DC")
    # rivales: 2 DC + 2 MC
    p.player(40, 30, "DC", team="rival")
    p.player(60, 30, "DC", team="rival")
    p.player(38, 46, "MC", team="rival")
    p.player(62, 56, "MC", team="rival")
    p.ball(50, 8)
    # cuatro vías de salida (numeradas)
    p.arrow(28, 20, 13, 41, kind="pass", label="1")          # banda izq
    p.arrow(72, 20, 87, 41, kind="pass", label="2")          # banda der
    p.arrow(54, 24, 56, 52, kind="pass", label="3")          # entrelíneas (al INT)
    p.arrow(44, 42, 47, 70, kind="pass", label="4")          # profundidad (al delantero)
    p.note(50, 14, "4 salidas: 1-2 bandas · 3 entrelíneas · 4 profundidad", c="#fff5cc")
    p.legend(["pass", "own", "rival", "zone"])
    save(p, 3)

# =====================================================================
# T4 — Salida 11v11 con zonas de presión (mutación 3->5)
# =====================================================================
def t04():
    p = Pitch(title="Tarea 4 — Salida 11v11 en 3 zonas",
              subtitle="superar la 1ª línea y mutar de 1-5-3-2 a 1-3-5-2", half=None)
    # 3 zonas horizontales
    p.zone(0, 0, 100, 33, label="zona 1 · salida")
    p.zone(0, 33, 100, 66, label="zona 2 · medio")
    p.zone(0, 66, 100, 100, label="zona 3 · ataque")
    # línea de superación z1->z2
    p.arrow(15, 33, 35, 33, kind="block", label="")
    p.note(50, 35, "línea de superación z1 → z2", c="#7ee0ff")
    # POR + 3 DFC (atrás)
    p.player(50, 6, "1", team="own", role="POR")
    p.player(30, 16, "6", team="own", role="DFC")
    p.player(50, 19, "5", team="own", role="líbero")
    p.player(70, 16, "4", team="own", role="DFC")
    # pivote + 2 interiores en zona media
    p.player(50, 40, "8", team="own", role="pivote")
    p.player(38, 50, "10", team="own", role="INT")
    p.player(62, 50, "7", team="own", role="INT")
    # carrileros SUBIENDO por encima de la linea de medios (mutación)
    p.player(10, 30, "3", team="own", role="CAR")
    p.player(90, 30, "2", team="own", role="CAR")
    p.arrow(10, 33, 10, 52, kind="run", label="sube")
    p.arrow(90, 33, 90, 52, kind="run", label="sube")
    # 2 DC arriba
    p.player(44, 72, "9", team="own", role="DC")
    p.player(56, 78, "11", team="own", role="DC")
    # rival: 2 DC + 2 MC presionan en zona 1
    p.player(42, 26, "DC", team="rival")
    p.player(58, 26, "DC", team="rival")
    p.player(35, 32, "MC", team="rival")
    p.player(65, 32, "MC", team="rival")
    p.ball(50, 8)
    p.arrow(50, 21, 50, 38, kind="pass", label="progresa")
    p.legend(["pass", "run", "block", "own", "rival"])
    save(p, 4)

# =====================================================================
# T5 — De 3 a 5: bajada de carrileros (★ línea de 5)
# =====================================================================
def t05():
    p = Pitch(title="Tarea 5 — De 3 a 5: bajada de carrileros",
              subtitle="los 2 carrileros sprintan a su carril y forman la línea de 5", half="def")
    # conos de referencia donde cierra cada carrilero (a la altura de los centrales)
    p.cone(15, 22); p.cone(85, 22)
    p.note(15, 16, "cono ref.", c="#ffd54a")
    p.note(85, 16, "cono ref.", c="#ffd54a")
    # estructura de 3 atrás (DFC) ya formando la línea
    p.player(30, 22, "6", team="own", role="DFC")
    p.player(50, 22, "5", team="own", role="líbero")
    p.player(70, 22, "4", team="own", role="DFC")
    # carrileros ALTOS (estructura de 3) bajando a sus conos
    p.player(12, 44, "3", team="own", role="CAR")
    p.player(88, 44, "2", team="own", role="CAR")
    p.arrow(13, 41, 15, 25, kind="run", label="sprint abajo")
    p.arrow(87, 41, 85, 25, kind="run", label="sprint abajo")
    # medio de 3 reajustando: 8 al eje, 7/10 escoltando
    p.player(50, 38, "8", team="own", role="pivote")
    p.player(33, 40, "10", team="own", role="INT")
    p.player(67, 40, "7", team="own", role="INT")
    p.arrow(35, 38, 50, 38, kind="run")           # escoltan al eje
    p.arrow(65, 38, 50, 38, kind="run")
    # atacantes que circulan (señal)
    p.player(40, 48, "A", team="rival")
    p.player(60, 48, "A", team="rival")
    p.ball(40, 48)
    p.note(50, 13, "línea de 5 formada en < 4 s", c="#fff5cc")
    p.legend(["run", "own", "rival"])
    save(p, 5)

# =====================================================================
# T6 — Basculación de la línea de 5 (★)
# =====================================================================
def t06():
    p = Pitch(title="Tarea 6 — Basculación de la línea de 5",
              subtitle="lado fuerte sale, escalera de coberturas, lado débil pinza", half="def")
    # balón en banda derecha (lado fuerte = der)
    # atacantes circulando
    p.player(80, 40, "A", team="rival")
    p.player(55, 44, "A", team="rival")
    p.player(40, 30, "A", team="rival")
    p.ball(80, 40)
    # línea de 5 basculada al lado del balón (derecha) -> todos desplazados a la der
    # carrilero del lado fuerte (der=2) sale al receptor
    p.player(78, 30, "2", team="own", role="CAR")
    p.arrow(78, 28, 80, 37, kind="run", label="sale al balón")
    # centrales en escalera diagonal cubriendo
    p.player(64, 24, "4", team="own", role="DFC")   # cubre contiguo
    p.player(52, 20, "5", team="own", role="") # reparte / hombre libre (rótulo aparte)
    p.player(40, 18, "6", team="own", role="DFC")
    # carrilero lado débil (izq=3) pinza HACIA DENTRO (no pegado a banda)
    p.player(30, 20, "3", team="own", role="CAR")
    p.arrow(15, 22, 28, 21, kind="run", label="pinza dentro")
    # pivote
    p.player(58, 34, "8", team="own", role="pivote")
    p.player(50, 6, "1", team="own", role="POR")
    # hombre libre señalado (rótulo encima de la elipse, sin pisar el dorsal 5)
    p.zone(44, 14, 60, 24, label="", ellipse=True)
    p.note(52, 28, "hombre libre (5)", c="#fff5cc")
    # coberturas en escalera (diagonales)
    p.arrow(64, 26, 70, 31, kind="run")
    p.arrow(52, 22, 60, 26, kind="run")
    p.legend(["run", "own", "rival", "zone"])
    save(p, 6)

# =====================================================================
# T7 — Distancia línea de 5 <-> medio de 3 (anular entrelíneas)
# =====================================================================
def t07():
    p = Pitch(title="Tarea 7 — Distancia línea de 5 ↔ medio de 3",
              subtitle="anular el entrelíneas: tapar la franja prohibida", half="def")
    # franja entrelíneas pintada (rótulo en el borde superior, libre de fichas)
    p.zone(8, 30, 92, 40, label="")
    p.note(50, 38.5, "franja prohibida (entrelíneas)", c="#fff5cc")
    # línea de 5
    p.player(15, 22, "3", team="own", role="CAR")
    p.player(33, 22, "6", team="own", role="DFC")
    p.player(50, 22, "5", team="own", role="líbero")
    p.player(67, 22, "4", team="own", role="DFC")
    p.player(85, 22, "2", team="own", role="CAR")
    # medio de 3
    p.player(50, 45, "8", team="own", role="pivote")
    p.player(35, 47, "10", team="own", role="INT")
    p.player(65, 47, "7", team="own", role="INT")
    p.player(50, 6, "1", team="own", role="POR")
    # 2 enganches rivales en la franja (algo más bajos, sin pisar el rótulo)
    p.player(38, 33, "10R", team="rival")
    p.player(64, 33, "10R", team="rival")
    # 2 DC y exteriores que sirven
    p.player(30, 60, "DC", team="rival")
    p.player(70, 60, "DC", team="rival")
    p.ball(70, 60)
    # decisiones: interior baja a tapar
    p.arrow(65, 44, 62, 38, kind="run", label="interior baja")
    p.arrow(50, 42, 50, 38, kind="run", label="pivote tapa")
    # un central sale, carrilero cierra por dentro
    p.arrow(33, 24, 40, 32, kind="run", label="central sale")
    p.arrow(15, 24, 30, 23, kind="run", label="CAR cierra dentro")
    p.legend(["run", "own", "rival", "zone"])
    save(p, 7)

# =====================================================================
# T8 — Defender el centro lateral con 5
# =====================================================================
def t08():
    p = Pitch(title="Tarea 8 — Defender el centro lateral con 5",
              subtitle="ocupar los puntos del área ante el centro", half="att")
    # half='att': portería propia ARRIBA (y=100). Gran área: y≈83.5..100; área
    # pequeña: y≈94.5..100; media luna (arco) en y≈83.5. Hay que OCUPAR el área.
    # balón en banda der que centra (alto, junto al área)
    p.player(92, 90, "B", team="rival")           # hombre de banda que centra
    p.ball(92, 90)
    p.arrow(91, 92, 55, 95, kind="pass", label="centro")
    # carrilero del lado salta al que centra (cerca de banda, dentro del campo)
    p.player(83, 86, "2", team="own", role="CAR", role_below=True)
    p.arrow(85, 87, 90, 89, kind="run", label="salta")
    # 3 centrales ocupando los palos DENTRO del área grande/pequeña
    p.player(40, 94, "6", team="own", role="1er palo", role_below=True)
    p.player(50, 95, "5", team="own", role="centro", role_below=True)
    p.player(60, 93, "4", team="own", role="2º palo", role_below=True)
    # carrilero contrario cierra el 2º palo lejano (dentro del área, lado izq)
    p.player(28, 92, "3", team="own", role="CAR", role_below=True)
    p.arrow(15, 86, 24, 90, kind="run", label="cierra 2º palo")
    # interior vigila el frontal del área (media luna) para el rechace
    p.player(50, 80, "8", team="own")
    p.note(50, 76, "frontal · 8 (rechace)", c="#fff5cc")
    p.zone(34, 76, 66, 84, label="", ellipse=True)
    # atacantes que atacan el centro dentro del área
    p.player(46, 92, "DC", team="rival")
    p.player(57, 90, "DC", team="rival")
    p.player(50, 85, "MC", team="rival")          # llega de 2ª línea a la frontal
    p.legend(["pass", "run", "own", "rival", "zone"])
    save(p, 8)

# =====================================================================
# T9 — Línea de 5: subir, bajar, offside (★)
# =====================================================================
def t09():
    p = Pitch(title="Tarea 9 — Línea de 5: subir y offside",
              subtitle="persiana de 5 tablillas sobre la línea de fuera de juego", half="def")
    # linea de fuera de juego de referencia (pintada)
    yfj = 40
    p.zone(0, yfj-0.6, 100, yfj+0.6, label="", c="#7ee0ff", fill_op=0.5)
    p.note(50, yfj+4, "línea de fuera de juego", c="#7ee0ff")
    # línea de 5 (incluye carrileros) subiendo al unísono
    line = [("3",15),("6",33),("5",50),("4",67),("2",85)]
    for lbl, x in line:
        role = "líbero" if lbl=="5" else ("CAR" if lbl in ("2","3") else "DFC")
        p.player(x, 30, lbl, team="own", role=role)
        p.arrow(x, 32, x, 38, kind="run")
    p.note(50, 26, "sube como una persiana de 5 tablillas", c="#fff5cc")
    # 5 ordena con la voz
    p.note(50, 22, "« ¡arriba! » (5 manda)", c="#fff5cc")
    p.player(50, 6, "1", team="own", role="POR")
    # 2 atacantes quedan en OFFSIDE (por delante de la línea)
    p.player(38, 45, "A", team="rival", role="OFFSIDE")
    p.player(62, 47, "A", team="rival", role="OFFSIDE")
    # pasador
    p.player(50, 62, "P", team="rival")
    p.ball(50, 62)
    p.arrow(50, 60, 40, 47, kind="pass", label="al espacio")
    p.legend(["pass", "run", "own", "rival"])
    save(p, 9)

# =====================================================================
# T10 — Press de los 2 DC
# =====================================================================
def t10():
    p = Pitch(title="Tarea 10 — Press de los 2 DC",
              subtitle="curvar la carrera, tapar al pivote y orientar a la banda", half="att")
    # rival sale 3+POR (abajo en su campo): los colocamos en y alto (su salida)
    # nuestros 2 DC presionan hacia arriba
    # salida rival: portero + 2 centrales + pivote
    p.player(50, 95, "POR", team="rival")
    p.player(30, 86, "DFC", team="rival")
    p.player(70, 86, "DFC", team="rival")
    p.player(50, 74, "8R", team="rival", role="pivote")
    p.ball(30, 86)
    # zonas-meta en bandas (a donde empujamos la salida)
    p.zone(2, 78, 20, 94, label="banda-meta")
    p.zone(80, 78, 98, 94, label="banda-meta")
    # 2 DC nuestros presionando en pareja
    p.player(44, 70, "9", team="own", role="DC")
    p.player(60, 68, "11", team="own", role="DC")
    # primer DC curva la carrera tapando sombra al pivote
    p.arrow(44, 72, 34, 83, kind="run", label="curva")
    # segundo DC vigila pivote/central libre
    p.arrow(60, 70, 62, 80, kind="run", label="vigila 8R")
    # sombra de pase tapada (al pivote)
    p.arrow(38, 80, 50, 76, kind="block")
    # salida orientada a banda-meta izq
    p.arrow(30, 84, 12, 86, kind="pass", label="forzado a banda")
    p.legend(["pass", "run", "block", "own", "rival", "zone"])
    save(p, 10)

# =====================================================================
# T11 — El gatillo del carrilero ★
# =====================================================================
def t11():
    p = Pitch(title="Tarea 11 — El gatillo del carrilero ★",
              subtitle="salto a la banda + cobertura en cadena, línea en 4 temporal", half=None)
    # salida rival arriba: 2 centrales + carrilero + pivote
    p.player(50, 78, "DFCr", team="rival")
    p.player(82, 64, "CARr", team="rival")        # carrilero rival recibe en banda der
    p.player(50, 60, "8R", team="rival", role="pivote")
    p.player(72, 78, "DCr", team="rival")         # delantero/central que se ofrece
    p.ball(82, 64)
    # nuestro carrilero (2, der) SALTA agresivo a la banda
    p.player(82, 44, "2", team="own", role="CAR")
    p.arrow(82, 47, 82, 61, kind="run", label="GATILLO: salta")
    # interior (7) baja a cubrir el carril abandonado
    p.player(64, 50, "7", team="own", role="INT")
    p.arrow(64, 52, 80, 50, kind="run", label="cubre carril")
    # conos del carril que abandona el carrilero
    p.cone(94, 52); p.cone(94, 38)
    p.note(94, 30, "carril abandonado", c="#ffd54a")
    # central del lado se desliza a vigilar al delantero
    p.player(64, 38, "4", team="own", role="DFC")
    p.arrow(64, 40, 70, 48, kind="run", label="desliza al DC")
    # resto de la línea queda en 4 temporal
    p.player(48, 36, "5", team="own", role="líbero")
    p.player(32, 36, "6", team="own", role="DFC")
    p.player(16, 40, "3", team="own", role="CAR")
    p.zone(8, 32, 72, 42, label="línea en 4 temporal")
    # DC borra la vuelta atrás al central rival
    p.player(56, 60, "9", team="own", role="DC")
    p.arrow(56, 62, 52, 74, kind="run", label="borra vuelta")
    # pivote reordena
    p.player(46, 50, "8", team="own", role="pivote")
    p.legend(["run", "own", "rival", "zone"])
    save(p, 11)

# =====================================================================
# T12 — Press alto 8v8+POR
# =====================================================================
def t12():
    p = Pitch(title="Tarea 12 — Press alto 8v8+POR",
              subtitle="2 DC orientan + carrileros saltan + interiores cubren", half=None)
    # 2 mini-porterías al centro (meta del rival: superar la presión)
    p.goalmini(35, 18)
    p.goalmini(65, 18)
    p.note(50, 13, "metas del rival (superar presión)", c="#fff5cc")
    # rival sale (abajo): POR + 2 centrales + carrileros + pivote
    p.player(50, 80, "PORr", team="rival")
    p.player(35, 70, "DFCr", team="rival")
    p.player(65, 70, "DFCr", team="rival")
    p.player(50, 60, "8R", team="rival")
    p.player(12, 58, "CARr", team="rival")
    p.player(88, 58, "CARr", team="rival")
    p.ball(35, 70)
    # nuestro press alto 8: 2 DC + 8/7/10 + 2 CAR + 1 DFC
    p.player(42, 76, "9", team="own", role="DC")
    p.player(58, 76, "11", team="own", role="DC")
    p.arrow(42, 74, 38, 70, kind="run", label="orienta")
    p.arrow(58, 74, 62, 70, kind="run", label="orienta")
    # carrileros saltan a las bandas rivales
    p.player(16, 50, "3", team="own", role="CAR")
    p.player(84, 50, "2", team="own", role="CAR")
    p.arrow(16, 52, 13, 57, kind="run", label="salta")
    p.arrow(84, 52, 87, 57, kind="run", label="salta")
    # interiores cubren detrás de los carrileros
    p.player(34, 50, "10", team="own", role="INT")
    p.player(66, 50, "7", team="own", role="INT")
    p.arrow(34, 50, 20, 48, kind="run", label="cubre")
    p.arrow(66, 50, 80, 48, kind="run", label="cubre")
    # pivote
    p.player(50, 50, "8", team="own", role="pivote")
    # 1 DFC de equilibrio
    p.player(50, 38, "5", team="own", role="DFC")
    p.legend(["run", "own", "rival"])
    save(p, 12)

# =====================================================================
# T13 — Press medio vs press alto por señal
# =====================================================================
def t13():
    p = Pitch(title="Tarea 13 — Press medio vs press alto",
              subtitle="izq. bloque medio (CAR bajos) · der. bloque alto (CAR suben)", half=None)
    # divisoria central conceptual
    p.arrow(50, 4, 50, 96, kind="block")
    p.note(25, 95, "BLOQUE MEDIO", c="#7ee0ff")
    p.note(75, 95, "BLOQUE ALTO", c="#ff8a8a")
    # señal del entrenador (centro)
    p.note(50, 8, "señal del entrenador", c="#fff5cc")
    p.cone(50, 12)

    # --- IZQUIERDA: bloque medio, carrileros BAJOS en línea de 5 ---
    # línea de 5 baja
    for lbl, x in [("3",6),("6",16),("5",25),("4",34),("2",44)]:
        role = ""
        p.player(x, 30, lbl, team="own", r=12)
    p.zone(3, 26, 47, 34, label="línea de 5")
    # medio de 3
    p.player(16, 44, "10", team="own", r=12)
    p.player(25, 44, "8", team="own", r=12)
    p.player(34, 44, "7", team="own", r=12)
    # 2 DC
    p.player(20, 58, "9", team="own", r=12)
    p.player(30, 58, "11", team="own", r=12)

    # --- DERECHA: bloque alto, carrileros SUBEN a presionar bandas ---
    # 3 DFC atrás
    for lbl, x in [("6",62),("5",71),("4",80)]:
        p.player(x, 32, lbl, team="own", r=12)
    # carrileros subidos a las bandas
    p.player(54, 58, "3", team="own", r=12, role="sube")
    p.player(90, 58, "2", team="own", r=12, role="sube")
    p.arrow(54, 50, 54, 57, kind="run")
    p.arrow(90, 50, 90, 57, kind="run")
    # interiores cubren
    p.player(66, 52, "10", team="own", r=12)
    p.player(78, 52, "7", team="own", r=12)
    p.arrow(66, 52, 58, 56, kind="run", label="cubre")
    p.arrow(78, 52, 86, 56, kind="run", label="cubre")
    # pivote + 2 DC arriba presionando
    p.player(71, 50, "8", team="own", r=12)
    p.player(66, 68, "9", team="own", r=12)
    p.player(76, 70, "11", team="own", r=12)
    p.legend(["run", "block", "own"])
    save(p, 13)

if __name__ == "__main__":
    for fn in (t01,t02,t03,t04,t05,t06,t07,t08,t09,t10,t11,t12,t13):
        fn()
    print("OK")
