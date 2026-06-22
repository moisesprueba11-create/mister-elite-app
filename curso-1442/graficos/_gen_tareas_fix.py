#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenera pizarras de TAREAS corregidas tras la revisión de calidad.
Solo toca las tareas con BLOQUEANTES / MENORES de alto impacto del informe
_pipeline/evaluacion/REVISION-GRAFICOS-TAREAS.md
Mantiene EXACTOS los nombres tarea-NN.svg.
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from pitch import Pitch

OUT = HERE  # graficos/

def step(p, x, y, n, c="#ffd54a"):
    """Dibuja un círculo numerado (orden de secuencia) en coords de campo."""
    cx, cy = p.X(x), p.Y(y)
    p.body.append(
        f'<g><circle cx="{cx:.1f}" cy="{cy:.1f}" r="9" fill="{c}" '
        f'stroke="#15202b" stroke-width="1.6"/>'
        f'<text x="{cx:.1f}" y="{cy+3.5:.1f}" font-family="Segoe UI,Arial" '
        f'font-size="11" font-weight="800" fill="#15202b" text-anchor="middle">{n}</text></g>')


# =====================================================================
# TAREA 5 — Basculación de las dos líneas de 4  (BLOQUEANTE)
#   Fix: eliminar línea roja espuria MI-MC; LD a la altura de los DFC
#   (línea de 4 alineada); solapes MI/MC; flecha de basculación coherente
#   con balón a la izquierda circulando hacia la derecha.
# =====================================================================
def tarea_05():
    p = Pitch(title="Tarea 5 — Las dos líneas de 4: basculación al balón",
              subtitle="8 piezas (4+4) + atacantes circulan en U · medio campo 68×45")
    # Atacantes que circulan el balón en U por delante del bloque (arriba)
    p.player(18, 84, "AT", team="rival")
    p.player(50, 90, "AT", team="rival")
    p.player(82, 84, "AT", team="rival")
    p.ball(18, 84)
    # circulación en U: balón a la izq -> centro -> der (lado fuerte = izquierda)
    p.arrow(24, 84, 45, 90, kind="pass")
    p.arrow(55, 90, 76, 84, kind="pass")
    p.note(50, 95, "circula en U", c="#ffd54a")
    # Línea de medios (4) — alineada; lado fuerte (izq) denso, lado débil (der) pinza
    p.player(20, 64, "MI", team="own")
    p.player(33, 64, "MC", team="own")
    p.player(46, 64, "MC", team="own")
    p.player(60, 64, "MD", team="own")
    p.note(60, 72, "lado débil pinza", c="#fff5cc")
    # Línea de defensas (4) — alineada (LI, DFC, DFC, LD a la misma altura)
    p.player(22, 36, "LI", team="own")
    p.player(35, 36, "DFC", team="own")
    p.player(48, 36, "DFC", team="own")
    p.player(62, 36, "LD", team="own")
    p.note(62, 44, "cierra al centro", c="#fff5cc")
    # Flecha de basculación: el bloque se desplaza al lado del balón (izquierda)
    p.arrow(58, 50, 30, 50, kind="run", label="bascula al lado del balón")
    p.note(50, 14, "Mover el bloque como un solo hilo · lado débil pinza al centro · reajuste <3 s")
    p.legend(["pass", "run", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-05.svg"))


# =====================================================================
# TAREA 6 — Distancia entre líneas  (BLOQUEANTE prompt)
#   Fix: rótulos a los 2 EN; zona "franja prohibida" etiquetada SIN cruzar
#   las fichas EN (texto subido a césped libre); mini-leyenda local.
# =====================================================================
def tarea_06():
    p = Pitch(title="Tarea 6 — Distancia entre líneas: espacio intermedio",
              subtitle="4 def + 4 medios + 2 enganches + 4 exteriores · 60 × 45 m")
    # Franja prohibida (zona entre líneas). Etiqueta colocada en el borde
    # superior de la zona, en césped libre (no cruza los EN, que van más abajo).
    p.zone(12, 48, 88, 62, c="#ff5252", fill_op=0.14)
    p.note(50, 64, "FRANJA ENTRE LÍNEAS — zona prohibida", c="#ffd54a", size=11)
    # Exteriores rivales (dan el balón) — arriba
    p.player(8, 88, "EX", team="rival")
    p.player(38, 92, "EX", team="rival")
    p.player(62, 92, "EX", team="rival")
    p.player(92, 88, "EX", team="rival")
    p.ball(38, 92)
    # 2 enganches rivales entre líneas (rotulados con su rol)
    p.player(40, 55, "EN", team="rival")
    p.note(40, 47, "enganche 1", c="#fff5cc")
    p.player(57, 55, "EN", team="rival")
    p.note(57, 47, "enganche 2", c="#fff5cc")
    # Línea de medios (4)
    p.player(22, 70, "MI", team="own")
    p.player(38, 73, "MC", team="own")
    p.player(58, 73, "MC", team="own")
    p.player(78, 70, "MD", team="own")
    p.note(48, 81, "pivote no sale del centro", c="#fff5cc")
    # Línea de defensas (4)
    p.player(24, 30, "LI", team="own")
    p.player(40, 30, "DFC", team="own")
    p.player(58, 30, "DFC", team="own")
    p.player(76, 30, "LD", team="own")
    # acciones: exterior filtra al EN; MC tapa; defensa sube
    p.arrow(36, 86, 40, 62, kind="pass")
    p.note(28, 78, "filtran", c="#ffd54a")
    p.arrow(40, 67, 40, 60, kind="run")
    p.note(26, 66, "MC tapa", c="#ffffff")
    p.arrow(58, 36, 57, 50, kind="run", label="defensa sube (<12 m)")
    p.note(50, 18, "Decisión binaria: achicar o tapar · medios y defensas <12 m")
    p.legend(["pass", "run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-06.svg"))


# =====================================================================
# TAREA 9 — Línea de 4: subir/bajar y fuera de juego  (BLOQUEANTE prompt)
#   Fix: línea de FdJ MUY visible (línea clara horizontal + rótulo);
#   numerar la secuencia 1 (pasador busca el espacio) 2 (línea sube) 3 (FdJ);
#   repartir textos densos en la banda.
# =====================================================================
def tarea_09():
    p = Pitch(title="Tarea 9 — Línea de 4: subir, bajar y fuera de juego",
              subtitle="4 def + POR vs 4 atacantes + pasador · línea de FdJ móvil",
              half="att")  # solo media de ataque para dar aire
    # En half='att' los y van de 50..100; usamos ese rango.
    # Línea de fuera de juego — línea clara visible + rótulo
    yfdj = 72
    x1, x2 = p.X(6), p.X(94)
    yl = p.Y(yfdj)
    p.body.append(f'<line x1="{x1:.1f}" y1="{yl:.1f}" x2="{x2:.1f}" y2="{yl:.1f}" '
                  f'stroke="#ffd54a" stroke-width="4" stroke-dasharray="10 6"/>')
    p.note(50, yfdj + 2.5, "LÍNEA DE FUERA DE JUEGO", c="#ffd54a", size=11)
    # POR
    p.player(50, 96, "POR", team="own")
    # Línea de 4 que sube (debajo de la línea de FdJ, subiendo hacia ella)
    p.player(20, 64, "LI", team="own")
    p.player(40, 64, "DFC", team="own")
    p.note(40, 58, "referencia: ¡arriba!", c="#fff5cc")
    p.player(60, 64, "DFC", team="own")
    p.player(80, 64, "LD", team="own")
    for xx in (20, 40, 60, 80):
        p.arrow(xx, 67, xx, yfdj - 1, kind="run")
    # Atacantes: 2 DC quedan por delante de la línea (en FdJ)
    p.player(33, 80, "DC", team="rival")
    p.note(33, 86, "en FdJ", c="#fff5cc")
    p.player(67, 80, "DC", team="rival")
    p.note(67, 86, "en FdJ", c="#fff5cc")
    # Pasador (comodín) abajo, con balón
    p.player(50, 54, "PAS", team="neutral")
    p.ball(50, 54)
    # secuencia numerada
    p.arrow(50, 57, 38, 78, kind="pass")
    step(p, 50, 56.5, "1")
    step(p, 30, 66, "2")
    step(p, 33, 76, "3")
    p.note(62, 60, "1 pase al espacio  ·  2 sube la línea  ·  3 deja en FdJ", c="#fff5cc")
    p.legend(["pass", "run", "own", "rival", "neutral"])
    p.save(os.path.join(OUT, "tarea-09.svg"))


# =====================================================================
# TAREA 10 — Press de los 2 DC: curvar carrera y tapar pivote
#   Fix: carreras CURVAS (no rectas); cono/sombra del 1er DC al pivote;
#   unificar rótulo de los 2 centrales rivales (DFC); numerar el salto.
# =====================================================================
def tarea_10():
    p = Pitch(title="Tarea 10 — Press de los 2 DC: curvar carrera y tapar pivote",
              subtitle="2 DC presionan vs 2 centrales + pivote + POR · ancho × 35 m")
    # Rival: POR, 2 DFC (mismo rótulo), pivote
    p.player(50, 92, "POR", team="rival")
    p.player(30, 70, "DFC", team="rival")
    p.player(70, 70, "DFC", team="rival")
    p.player(50, 56, "PIV", team="rival")
    p.note(50, 49, "pivote (a tapar)", c="#fff5cc")
    p.ball(24, 67)  # balón al lado del DFC izq, sin tapar su rótulo
    # zonas-meta de banda (salida orientada a banda)
    p.zone(2, 60, 18, 80, c="#7ee0ff", fill_op=0.12, label="")
    p.note(10, 70, "ZONA-META banda", c="#fff", size=9)
    p.zone(82, 60, 98, 80, c="#7ee0ff", fill_op=0.12, label="")
    p.note(90, 70, "ZONA-META banda", c="#fff", size=9)
    # 2 DC propios
    p.player(38, 44, "DC1", team="own")
    p.note(38, 37, "inicia", c="#fff5cc")
    p.player(62, 44, "DC2", team="own")
    # carrera CURVA del DC1: tapa la sombra al pivote (curva hacia el centro)
    def curve(p, x1, y1, cx, cy, x2, y2, col="#ffffff", label=""):
        X1, Y1 = p.X(x1), p.Y(y1)
        CX, CY = p.X(cx), p.Y(cy)
        X2, Y2 = p.X(x2), p.Y(y2)
        p.body.append(f'<path d="M{X1:.1f},{Y1:.1f} Q{CX:.1f},{CY:.1f} {X2:.1f},{Y2:.1f}" '
                      f'fill="none" stroke="{col}" stroke-width="2.8" marker-end="url(#ah_run)"/>')
        if label:
            p._text((X1+X2)/2, (Y1+Y2)/2, label, size=9.5, c=col, w=700)
    # DC1 corre curvando por detrás del pivote para presionar al DFC izq tapando la línea al pivote
    curve(p, 40, 46, 56, 52, 33, 66, label="")
    p.note(42, 58, "curva: tapa al pivote", c="#ffffff")
    # cono de sombra desde DC1 hacia el pivote
    sx, sy = p.X(36), p.Y(48)
    px1, py1 = p.X(43), p.Y(54); px2, py2 = p.X(57), p.Y(54)
    p.body.append(f'<path d="M{sx:.1f},{sy:.1f} L{px1:.1f},{py1:.1f} L{px2:.1f},{py2:.1f} z" '
                  f'fill="#15202b" fill-opacity="0.34" stroke="#15202b" stroke-opacity="0.5" '
                  f'stroke-dasharray="4 4"/>')
    p.note(50, 53.5, "sombra", c="#cfe0ee", size=9)
    # DC2 salta curvando al central libre
    curve(p, 62, 46, 70, 56, 66, 66, label="")
    p.note(74, 58, "salta al central libre", c="#ffffff")
    # numeración del press en pareja
    step(p, 40, 46, "1")
    step(p, 64, 46, "2")
    p.note(50, 18, "Tapar con la carrera, no con la pierna · presionar en pareja · saltos alternos")
    p.legend(["run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-10.svg"))


# =====================================================================
# TAREA 16 — Pared y descarga del DC que baja  (BLOQUEANTE prompt)
#   Fix: numerar 1 (MC->DC), 2 (pared a un toque), 3 (suelta a banda / 2º DC);
#   rotular el MC inicial.
# =====================================================================
def tarea_16():
    p = Pitch(title="Tarea 16 — Pared y descarga del DC que baja",
              subtitle="MC + DC que baja + banda + DC que ataca · 30×30 m",
              half="att")
    p.player(50, 92, "POR", team="rival")
    p.player(50, 74, "def", team="rival")
    p.note(50, 80, "pasivo", c="#fff5cc")
    # MC inicial con balón (rotulado; balón desplazado para no tapar la ficha)
    p.player(30, 44, "MC", team="own")
    p.note(22, 44, "inicio (MC)", c="#fff5cc")
    p.ball(36, 44)
    # DC que baja a recibir
    p.player(45, 58, "DC", team="own")
    p.note(45, 64, "DC baja", c="#fff5cc")
    # segundo DC que ataca en profundidad
    p.player(62, 64, "DC", team="own")
    p.note(62, 70, "DC ataca", c="#fff5cc")
    # banda
    p.player(82, 56, "BANDA", team="own")
    # secuencia: 1 pase MC->DC ; 2 pared DC->MC ; 3 MC suelta a 2º DC / banda
    p.arrow(33, 47, 43, 56, kind="pass")          # 1 MC -> DC que baja
    p.arrow(45, 61, 35, 50, kind="pass")          # 2 pared (vuelta al MC)
    p.arrow(34, 46, 60, 62, kind="pass")          # 3 suelta al 2º DC en profundidad
    p.arrow(33, 43, 79, 55, kind="pass")          # 3b a banda
    step(p, 39, 52, "1")
    step(p, 41, 48, "2")
    step(p, 50, 50, "3")
    p.note(50, 22, "Pared a un toque · suelta al 2º DC en profundidad o a banda → centro y remate")
    p.legend(["pass", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-16.svg"))


# =====================================================================
# TAREA 18 — Segunda jugada del balón largo  (BLOQUEANTE prompt)
#   Fix: SEPARAR el balón largo y la 2ª jugada (no se solapan); dar aire
#   al clúster de delanteros/centrales; numerar 1 (largo) 2 (peina) 3 (2ª jugada).
# =====================================================================
def tarea_18():
    p = Pitch(title="Tarea 18 — Segunda jugada del balón largo",
              subtitle="POR/def + 2 DC + 2 MC vs 2 DFC + 2 MC · 50×50 m")
    # POR/def que envía (abajo)
    p.player(50, 8, "POR", team="own")
    p.ball(50, 8)
    # Pareja de DC (arriba, separados). El que pelea, a la izquierda y alto.
    p.player(34, 74, "DC", team="own")
    p.note(20, 74, "DC pelea/peina", c="#fff5cc")
    p.player(60, 66, "DC", team="own")
    p.note(74, 66, "DC recoge", c="#fff5cc")
    # DFC rivales (claramente separados de los DC)
    p.player(46, 82, "DFC", team="rival")
    p.player(72, 78, "DFC", team="rival")
    # MC rivales
    p.player(42, 54, "MC", team="rival")
    p.player(64, 52, "MC", team="rival")
    # MC propios que llegan a la 2ª jugada (abajo, separados)
    p.player(26, 42, "MC", team="own")
    p.note(26, 36, "MC llega", c="#fff5cc")
    p.player(54, 38, "MC", team="own")
    p.note(54, 32, "MC llega", c="#fff5cc")
    # 1) balón largo a la pareja (línea larga, a la izquierda, separada)
    p.arrow(48, 12, 35, 69, kind="pass")
    step(p, 44, 24, "1")
    p.note(30, 45, "balón largo", c="#ffd54a")
    # 2) peina/prolonga hacia el 2º DC (corto, arriba a la derecha)
    p.arrow(37, 75, 56, 68, kind="pass")
    step(p, 47, 72, "2")
    # 3) 2ª jugada: elipse de caída del rechace, separada; rótulo en borde derecho
    p.zone(42, 56, 66, 66, ellipse=True, c="#7ee0ff", fill_op=0.14)
    p.note(80, 60, "2ª jugada", c="#7ee0ff")
    p.arrow(28, 46, 48, 60, kind="run")   # MC llega a la 2ª jugada
    p.arrow(54, 42, 58, 58, kind="run")
    step(p, 40, 54, "3")
    p.note(50, 90, "MC llegan antes que rivales · recuperar y finalizar <6 s")
    p.legend(["pass", "run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-18.svg"))


# =====================================================================
# TAREA 20 — Repliegue a las dos líneas
#   Fix: cuadrar a 8 propios (el "frena eje" es una de las 8 piezas).
# =====================================================================
def tarea_20():
    p = Pitch(title="Tarea 20 — Repliegue a las dos líneas",
              subtitle="8 repliegan (4+4) vs 6 que contraatacan · 3/4 campo")
    # Rivales que contraatacan (arriba->hacia abajo, atacan portería propia abajo)
    for (x, y) in [(50, 70), (28, 66), (72, 64), (40, 78), (62, 80), (50, 86)]:
        p.player(x, y, "riv", team="rival")
    p.ball(50, 70)
    # Bloque propio de 8 (4 medios + 4 defensas). El "frena eje" es el MC central
    # que ocupa el eje (una de las 8 piezas, NO un noveno).
    # Línea de medios (4)
    p.player(20, 40, "MI", team="own")
    p.player(42, 40, "MC", team="own")   # este es el que frena el eje
    p.note(42, 47, "frena eje (1 de 8)", c="#fff5cc")
    p.player(58, 40, "MC", team="own")
    p.player(80, 40, "MD", team="own")
    # arranque del MC al eje para frenar el balón central
    p.arrow(42, 44, 48, 60, kind="run", label="roba y frena")
    # Línea de defensas (4)
    p.player(22, 18, "LI", team="own")
    p.player(40, 18, "DFC", team="own")
    p.player(58, 18, "DFC", team="own")
    p.player(78, 18, "LD", team="own")
    # repliegue: flechas de cada pieza hacia su posición (carril)
    for (x, yf) in [(20, 36), (58, 36), (80, 36), (22, 14), (40, 14), (58, 14), (78, 14)]:
        p.arrow(x, yf + 8, x, yf, kind="run")
    p.zone(14, 12, 86, 46, c="#ffd54a", fill_op=0.07, label="")
    p.note(50, 30, "dos líneas de 4 (bloque)", c="#fff")
    p.note(50, 92, "Frenar balón central 1º · replegar al carril, no perseguir")
    p.legend(["run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-20.svg"))


# =====================================================================
# TAREA 22 — Juego de las cuatro transiciones  (BLOQUEANTE prompt)
#   Fix: distinguir CLARAMENTE las cuatro transiciones con zonas+numeración
#   +colores; rotular referencias clave del 1-4-4-2 (no "own").
# =====================================================================
def tarea_22():
    p = Pitch(title="Tarea 22 — Juego de las cuatro transiciones",
              subtitle="8v8 + POR · 60×50 m · las 4 transiciones del juego")
    # Cuatro cuadrantes = las 4 fases del juego, cada uno con color y número.
    # 1 Ataque (tengo balón) / 2 Transición A-D (pierdo) /
    # 3 Defensa (no tengo) / 4 Transición D-A (robo).
    p.zone(2, 50, 50, 98, c="#1565c0", fill_op=0.12)   # ataque propio (arriba izq)
    p.note(26, 90, "1 ATAQUE", c="#9ec7ff", size=11)
    p.zone(50, 50, 98, 98, c="#ff5252", fill_op=0.12)  # A-D pierdo
    p.note(74, 90, "2 PIERDO → A-D", c="#ffb0b0", size=11)
    p.zone(50, 2, 98, 50, c="#c62828", fill_op=0.12)   # defensa
    p.note(74, 10, "3 DEFENSA", c="#ffb0b0", size=11)
    p.zone(2, 2, 50, 50, c="#7ee0ff", fill_op=0.12)    # D-A robo
    p.note(26, 10, "4 ROBO → D-A", c="#bdeeff", size=11)
    # POR de cada equipo
    p.player(50, 4, "POR", team="own")
    p.player(50, 96, "POR", team="rival")
    # referencias clave propias rotuladas
    p.player(30, 60, "DC", team="own")
    p.player(58, 55, "MC", team="own")
    p.player(18, 44, "MI", team="own")
    p.player(72, 46, "MD", team="own")
    p.player(46, 72, "DFC", team="own")
    # rivales (referencias)
    p.player(40, 52, "MC", team="rival")
    p.player(62, 40, "DC", team="rival")
    p.player(30, 36, "DFC", team="rival")
    p.player(70, 70, "MD", team="rival")
    p.ball(63, 58)  # junto al MC propio sin taparlo
    # flechas cíclicas entre fases (transiciones), numeradas
    p.arrow(40, 78, 64, 78, kind="run")   # 1->2 pierdo
    p.arrow(78, 60, 78, 40, kind="run")   # 2->3 me organizo
    p.arrow(64, 22, 40, 22, kind="run")   # 3->4 robo
    p.arrow(22, 40, 22, 60, kind="run")   # 4->1 ataco
    step(p, 52, 78, "2")
    step(p, 78, 50, "3")
    step(p, 52, 22, "4")
    step(p, 22, 50, "1")
    p.note(50, 49, "A-D: recuperar <5 s = punto  ·  D-A: gol <8 s = doble", c="#fff5cc", size=9.5)
    p.legend(["run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-22.svg"))


# =====================================================================
# TAREA 24 — Partido con zonas de puntos
#   Fix: TINTAR los dos carriles de banda (provocación "bandas resaltadas");
#   añadir alguna ficha de referencia.
# =====================================================================
def tarea_24():
    p = Pitch(title="Tarea 24 — Partido con zonas de puntos",
              subtitle="3 carriles (2 bandas + central) y 3 franjas · zonas de puntos")
    # Carriles de banda TINTADOS (zonas premiadas)
    p.zone(0, 0, 22, 100, c="#ffd54a", fill_op=0.18)
    p.zone(78, 0, 100, 100, c="#ffd54a", fill_op=0.18)
    p.note(11, 88, "BANDA +1", c="#fff", size=11)
    p.note(89, 88, "BANDA +1", c="#fff", size=11)
    # Carril central penalizado (tinte rojo tenue)
    p.zone(22, 0, 78, 100, c="#ff5252", fill_op=0.06)
    p.note(50, 50, "central (difícil)", c="#ffd9d9", size=10)
    # 3 franjas horizontales (líneas guía)
    for yy in (33.3, 66.6):
        x1, x2 = p.X(0), p.X(100); yl = p.Y(yy)
        p.body.append(f'<line x1="{x1:.1f}" y1="{yl:.1f}" x2="{x2:.1f}" y2="{yl:.1f}" '
                      f'stroke="#ffffff" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6"/>')
    # POR
    p.player(50, 5, "POR", team="own")
    p.player(50, 95, "POR", team="rival")
    # referencias propias (atacan por banda)
    p.player(90, 58, "MD", team="own")
    p.player(11, 50, "MI", team="own")
    p.player(50, 40, "MC", team="own")
    p.player(35, 30, "DFC", team="own")
    p.player(65, 32, "LD", team="own")
    p.ball(16, 52)
    # rivales de referencia
    p.player(78, 60, "riv", team="rival")
    p.player(40, 62, "riv", team="rival")
    # progresión por banda
    p.arrow(12, 54, 22, 78, kind="run", label="progresa")
    p.note(20, 30, "robo en banda = +1", c="#ffd54a")
    p.note(50, 12, "Atacar por bandas hacia el área · robar en banda (+1) · bloque <35 m (+1)")
    p.legend(["run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-24.svg"))


# =====================================================================
# TAREA 25 — Partido aplicado al rival  (BLOQUEANTE prompt)
#   Fix: SEPARAR el sparring rival y las flechas de salto (evitar
#   amontonamiento); cambiar línea roja "bloqueo" por grafismo de marca;
#   separar rótulos de los DC.
# =====================================================================
def tarea_25():
    p = Pitch(title="Tarea 25 — Partido aplicado al rival",
              subtitle="1-4-4-2 vs sparring (salida de 3 + 10 entre líneas)")
    # Sparring rival con SALIDA DE 3 (arriba) — bien separados
    p.player(50, 92, "POR", team="rival")
    p.player(28, 82, "DFC", team="rival")
    p.player(50, 84, "6", team="rival")     # pivote que baja = salida de 3
    p.player(72, 82, "DFC", team="rival")
    p.note(50, 90, "salida de 3", c="#fff5cc")
    p.player(14, 70, "LI", team="rival")
    p.player(86, 70, "LD", team="rival")
    # el 10 entre líneas (claramente separado)
    p.player(50, 58, "10", team="rival")
    p.note(50, 64, "10 entre líneas", c="#fff5cc")
    p.ball(50, 84)
    # 1-4-4-2 propio
    p.player(50, 8, "POR", team="own")
    p.player(20, 18, "LI", team="own")
    p.player(40, 16, "DFC", team="own")
    p.player(60, 16, "DFC", team="own")
    p.player(80, 18, "LD", team="own")
    # 2 DC propios saltan a la salida — separados, flechas claras y no amontonadas
    p.player(38, 70, "DC", team="own")
    p.note(30, 76, "salta a la salida", c="#fff5cc")
    p.player(62, 64, "DC", team="own")
    p.note(70, 70, "tapa pivote", c="#fff5cc")
    # 2 MC y bandas
    p.player(35, 46, "MC", team="own")
    p.player(65, 44, "MC", team="own")
    p.player(20, 40, "MI", team="own")
    p.player(80, 40, "MD", team="own")
    # saltos de los DC (flechas separadas, una a cada DFC)
    p.arrow(38, 73, 30, 79, kind="run")
    p.arrow(62, 67, 52, 80, kind="run")
    # bajada del MC al 10 — grafismo de MARCA/SEGUIMIENTO (línea punteada fina, no roja de bloqueo)
    X1, Y1 = p.X(35), p.Y(49); X2, Y2 = p.X(48), p.Y(56)
    p.body.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" '
                  f'stroke="#ff9800" stroke-width="2.4" stroke-dasharray="3 3" '
                  f'marker-end="url(#ah_run)"/>')
    p.note(34, 54, "MC baja a marcar al 10", c="#ffcc80", size=9.5)
    p.note(50, 27, "Quién salta a la salida de 3 · quién vigila al 10 · gatillos vs ESE rival")
    # leyenda local de la marca
    p.legend(["pass", "run", "own", "rival"])
    p.save(os.path.join(OUT, "tarea-25.svg"))


# =====================================================================
# TAREA 27 — Defensa mixta de córner + contragolpe  (BLOQUEANTE informe)
#   Fix: rehacer etiquetado del área (una etiqueta por función zona/hombre/
#   poste, bien separadas); renombrar "zMC"; clarificar destino del despeje;
#   reducir solapes texto-ficha.
# =====================================================================
def tarea_27():
    p = Pitch(title="Tarea 27 — Defensa mixta de córner + contragolpe",
              subtitle="zona + 2 al hombre + 2 postes + POR · 2 DC arriba",
              half="att")  # foco en el área de ataque rival (que defendemos abajo)
    # Trabajamos la portería propia abajo: usamos half='att' (y 50..100) e
    # invertimos visualmente colocando la portería defendida arriba para ver el área.
    # POR manda el área
    p.player(50, 95, "POR", team="own")
    p.note(68, 95, "POR manda el área", c="#fff5cc", size=9.5)
    # Postes (1 en cada palo) — bien separados y etiquetados una vez
    p.player(40, 92, "POSTE", team="own")
    p.player(60, 92, "POSTE", team="own")
    # ZONA: 3 en la zona de remate (primer palo + trayectoria central)
    p.player(38, 82, "DEF", team="own")
    p.player(50, 80, "DEF", team="own")
    p.player(62, 82, "DEF", team="own")
    p.zone(30, 76, 70, 88, c="#7ee0ff", fill_op=0.12)
    p.note(50, 74, "ZONA (1er palo + trayectoria)", c="#7ee0ff", size=10)
    # 2 AL HOMBRE sobre rematadores peligrosos (etiqueta única, separada)
    p.player(43, 70, "H1", team="own")
    p.player(57, 70, "H2", team="own")
    p.note(50, 65.5, "2 al hombre (peligrosos)", c="#fff5cc", size=10)
    # Rematadores rivales (peligrosos) — separados de las marcas
    p.player(43, 76, "REM", team="rival")
    p.player(57, 76, "REM", team="rival")
    p.player(50, 86, "REM", team="rival")
    # Lanzador en el córner
    p.player(94, 96, "LANZ", team="rival")
    p.ball(94, 96)
    p.arrow(92, 95, 60, 84, kind="pass")  # saque
    # 2 DC arriba para la salida de contragolpe (bien separados, abajo)
    p.player(38, 56, "DC", team="own")
    p.note(38, 50, "salida arriba", c="#fff5cc")
    p.player(62, 54, "DC", team="own")
    p.note(62, 48, "salida arriba", c="#fff5cc")
    # DESPEJE: una sola flecha clara, lejos y a banda por el lateral izq,
    # esquivando el clúster central, con destino claro al DC izq.
    p.arrow(46, 81, 22, 62, kind="run")   # despeje orientado al DC izq por fuera
    p.arrow(22, 60, 36, 57, kind="pass")  # segunda fase: balón al DC
    p.note(20, 70, "despeje lejos y a banda", c="#ffffff", size=9.5)
    p.note(28, 56, "→ DC", c="#ffd54a", size=9.5)
    p.note(50, 42, "Al despejar, ya estamos atacando · despejar lejos y a banda")
    p.legend(["pass", "run", "own", "rival", "zone"])
    p.save(os.path.join(OUT, "tarea-27.svg"))


if __name__ == "__main__":
    funcs = dict(
        t5=tarea_05, t6=tarea_06, t9=tarea_09, t10=tarea_10, t16=tarea_16,
        t18=tarea_18, t20=tarea_20, t22=tarea_22, t24=tarea_24, t25=tarea_25,
        t27=tarea_27,
    )
    sel = sys.argv[1:] if len(sys.argv) > 1 else list(funcs.keys())
    for k in sel:
        funcs[k]()
        print("OK", k)
