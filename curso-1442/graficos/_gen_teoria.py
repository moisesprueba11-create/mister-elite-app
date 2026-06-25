#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera todos los diagramas de teoría del curso 1-4-4-2."""
import sys, os
sys.path.insert(0, '/home/user/mister-elite-app/curso-1442/graficos/lib')
from pitch import Pitch

OUT = '/home/user/mister-elite-app/curso-1442/graficos'

def mnote(p, x, y, s, c="#fff5cc", size=10, w=600):
    """Nota multilínea (cada línea de s separada por \\n)."""
    lines = s.split("\n")
    cx = p.X(x); cy = p.Y(y)
    n = len(lines)
    for i, ln in enumerate(lines):
        yy = cy + (i - (n - 1) / 2.0) * (size + 2)
        p.body.append(
            f'<text x="{cx:.1f}" y="{yy+size*0.35:.1f}" font-family="Segoe UI,Arial,sans-serif" '
            f'font-size="{size}" font-weight="{w}" fill="{c}" text-anchor="middle">{ln}</text>')

def save(p, name):
    path = os.path.join(OUT, name)
    p.save(path)
    print("OK", name)

# =====================================================================
# MÓDULO 01 — FUNDAMENTOS
# =====================================================================

# --- teoria-01: formación base plana ---
def t01():
    p = Pitch(title="Formación base 1-4-4-2 (plano)",
              subtitle="Tres líneas + portero · doble línea de cuatro · dos puntas")
    # portero
    p.player(50, 7, "POR", team="own", role="1 · portero")
    # defensa (4): 2 LD, 3 LI, 4 central der, 5 central izq
    p.player(15, 22, "LI", team="own", role="3 · lateral izq")
    p.player(38, 20, "DFC", team="own", role="5 · central izq")
    p.player(62, 20, "DFC", team="own", role="4 · central der")
    p.player(85, 22, "LD", team="own", role="2 · lateral der")
    # medios (4): 7 extremo izq, 6 MCD, 8 MCO, 11 extremo der
    p.player(13, 50, "EI", team="own", role="7 · extremo izq")
    p.player(40, 44, "MC", team="own", role="6 · pivote")
    p.player(60, 44, "MC", team="own", role="8 · llegador")
    p.player(87, 50, "ED", team="own", role="11 · extremo der")
    # delanteros (2) — rótulo DEBAJO (van muy arriba; encima tocaría el borde)
    p.player(40, 75, "DC", team="own", role="9 · referencia", role_below=True)
    p.player(60, 75, "DC", team="own", role="10 · 2º punta", role_below=True)
    save(p, "teoria-01-formacion-base.svg")

# --- teoria-02: carriles y franjas / lectura del campo ---
def t02():
    p = Pitch(title="Lectura del campo: 5 carriles · 3 franjas",
              subtitle="Medios espacios y zona 14 = puntos críticos del 4-4-2")
    # franjas horizontales (líneas divisorias finas)
    for yv in (33, 67):
        p._line(p.X(0), p.Y(yv), p.X(100), p.Y(yv), w=1.6, c="#ffffff", dash="3 6", opacity=0.55)
    # carriles: líneas verticales divisorias finas
    for xv in (20, 40, 60, 80):
        p._line(p.X(xv), p.Y(2), p.X(xv), p.Y(98), w=1.4, c="#ffffff", dash="3 6", opacity=0.5)
    # medios espacios resaltados (los puntos críticos)
    p.zone(20, 34, 40, 66, label="", c="#ffd54a", fill_op=0.20)
    p.zone(60, 34, 80, 66, label="", c="#ffd54a", fill_op=0.20)
    mnote(p, 30, 58, "medio\nespacio", c="#fff", size=9)
    mnote(p, 70, 58, "medio\nespacio", c="#fff", size=9)
    # zona 14
    p.zone(38, 71, 62, 85, label="ZONA 14", c="#ff9800", fill_op=0.24, ellipse=True)
    # etiquetas de carril (arriba)
    p.note(10, 96, "lateral izq", c="#cfe", size=8.5)
    p.note(30, 96, "interior izq", c="#cfe", size=8.5)
    p.note(50, 96, "central", c="#cfe", size=8.5)
    p.note(70, 96, "interior der", c="#cfe", size=8.5)
    p.note(90, 96, "lateral der", c="#cfe", size=8.5)
    # etiquetas de franja (a la izquierda, sin chocar con medios espacios)
    mnote(p, 9, 18, "FRANJA\nDEFENSIVA", c="#bfe8ff", size=9)
    mnote(p, 9, 50, "FRANJA\nMEDIA", c="#fff5cc", size=9)
    mnote(p, 9, 84, "FRANJA\nOFENSIVA", c="#ffd0d0", size=9)
    save(p, "teoria-02-carriles-franjas.svg")

# --- teoria-03: perfiles por línea ---
def t03():
    p = Pitch(title="Perfiles complementarios por línea",
              subtitle="Cada línea combina dos roles distintos")
    p.player(50, 7, "POR", team="own", role="juego pies + líbero")
    p.player(15, 22, "LI", team="own", role="recorrido 1v1")
    p.player(38, 20, "DFC", team="own", role="dominante aéreo")
    p.player(62, 20, "DFC", team="own", role="rápido + salida")
    p.player(85, 22, "LD", team="own", role="recorrido 1v1")
    p.player(13, 50, "EI", team="own", role="amplitud+repliegue")
    p.player(40, 44, "MC", team="own", role="6 organizador")
    p.player(60, 44, "MC", team="own", role="8 box-to-box")
    p.player(87, 50, "ED", team="own", role="amplitud+repliegue")
    p.player(40, 75, "DC", team="own", role="referencia/fija")
    p.player(60, 75, "DC", team="own", role="móvil/ruptura")
    save(p, "teoria-03-perfiles-por-linea.svg")

# --- teoria-04: comparación plano vs rombo (dos medios campos) ---
def t04():
    # campo completo: mitad inferior = plano, mitad superior = rombo
    p = Pitch(title="Plano vs Rombo: el centro del campo",
              subtitle="Abajo línea de 4 (amplitud) · Arriba rombo (eje)")
    # PLANO en mitad inferior (medios) — jugadores propios en azul
    p.note(50, 44, "— PLANO (2 extremos + 2 MC) —", c="#bfe8ff", size=11)
    p.player(13, 30, "EI", team="own")
    p.player(38, 27, "MC", team="own")
    p.player(62, 27, "MC", team="own")
    p.player(87, 30, "ED", team="own")
    p.note(50, 14, "amplitud por bandas, 2 en el eje", c="#cfe", size=9)
    # ROMBO en mitad superior — misma estructura propia, comodín (neutral)
    p.note(50, 56, "— ROMBO (MCD · 2 INT · enganche) —", c="#ffd0a0", size=11)
    p.player(50, 62, "MCD", team="neutral")
    p.player(33, 73, "INT", team="neutral")
    p.player(67, 73, "INT", team="neutral")
    p.player(50, 84, "ENG", team="neutral", role="enganche (zona 14)")
    p.note(50, 95, "4 en el eje, sin extremos", c="#ffe1c0", size=9)
    p.legend(["own", "neutral"])
    save(p, "teoria-04-plano-vs-rombo.svg")

# --- teoria-05: variante en rombo (formación completa rombo) ---
def t05():
    p = Pitch(title="Variante 4-4-2 en rombo (diamante)",
              subtitle="Superioridad central · ocupa la zona 14 · sin extremos")
    p.player(50, 7, "POR", team="own", role="1")
    p.player(13, 24, "LI", team="own", role="da la amplitud")
    p.player(38, 20, "DFC", team="own")
    p.player(62, 20, "DFC", team="own")
    p.player(87, 24, "LD", team="own", role="da la amplitud")
    # rombo
    p.player(50, 38, "MCD", team="own", role="ancla / pivote")
    p.player(30, 52, "INT", team="own", role="interior")
    p.player(70, 52, "INT", team="own", role="interior")
    p.player(50, 64, "ENG", team="own", role="enganche")
    # puntas
    p.player(40, 80, "DC", team="own")
    p.player(60, 80, "DC", team="own")
    # marca rombo con líneas guía suaves
    p.zone(28, 36, 72, 66, label="", c="#7ee0ff", fill_op=0.05, dash="4 6")
    save(p, "teoria-05-variante-rombo.svg")

# =====================================================================
# MÓDULO 02 — FASE DEFENSIVA
# =====================================================================

# --- teoria-06: roles defensivos por posición ---
def t06():
    p = Pitch(title="Roles defensivos por posición",
              subtitle="Bloque medio 4-4-2 · responsabilidades zonales")
    p.player(50, 9, "POR", team="own", role="líbero del espacio")
    p.player(14, 22, "LI", team="own", role="1v1 + intervalo")
    p.player(38, 19, "DFC", team="own", role="stopper")
    p.player(62, 19, "DFC", team="own", role="coberturas")
    p.player(86, 22, "LD", team="own", role="1v1 + intervalo")
    p.player(13, 44, "EI", team="own", role="ayuda lateral")
    p.player(40, 41, "MC", team="own", role="tapa entre líneas")
    p.player(60, 41, "MC", team="own", role="cae al pivote")
    p.player(87, 44, "ED", team="own", role="ayuda lateral")
    p.player(42, 62, "DC", team="own", role="referencia presión")
    p.player(58, 62, "DC", team="own", role="2º vértice presión")
    save(p, "teoria-06-roles-defensivos.svg")

# --- teoria-07: tres bloques + distancias ---
def t07():
    p = Pitch(title="Las tres alturas del bloque",
              subtitle="Última línea y primer presionador en alto / medio / bajo")
    # Bloque BAJO (tercio defensivo)
    p.zone(2, 16, 98, 30, label="", c="#ff5252", fill_op=0.10)
    p.note(50, 23, "BLOQUE BAJO · última línea ~18-25 m", c="#ffd0d0", size=10)
    # Bloque MEDIO
    p.zone(2, 32, 98, 46, label="", c="#ffd54a", fill_op=0.10)
    p.note(50, 39, "BLOQUE MEDIO · última línea ~30-40 m", c="#fff5cc", size=10)
    # Bloque ALTO
    p.zone(2, 48, 98, 62, label="", c="#7ee0ff", fill_op=0.10)
    p.note(50, 55, "BLOQUE ALTO · última línea ~45-55 m", c="#bfe8ff", size=10)
    # última línea propia (izq) y primer presionador propio (der): ambos son
    # jugadores PROPIOS (azul). El primer presionador es delantero propio (DC).
    p.player(20, 24, "DEF", team="own"); p.player(80, 24, "DC", team="own")
    p.player(20, 40, "DEF", team="own"); p.player(80, 40, "DC", team="own")
    p.player(20, 56, "DEF", team="own"); p.player(80, 56, "DC", team="own")
    p.note(20, 11, "última línea propia", c="#cfe", size=9)
    p.note(80, 11, "primer presionador (DC)", c="#bfe8ff", size=9)
    p.legend(["own"])
    save(p, "teoria-07-bloques-altura.svg")

# --- teoria-08: pressing 2 DC con sombra ---
def t08():
    p = Pitch(title="Presión de los dos delanteros + sombra",
              subtitle="Carrera curvada que tapa el pivote y orienta a banda")
    # rival saliendo
    p.player(38, 80, "DFC", team="rival", role="con balón")  # arriba = campo rival
    p.player(62, 80, "DFC", team="rival")
    p.player(50, 90, "POR", team="rival")
    p.player(50, 66, "MCD", team="rival", role="pivote (tapado)")
    p.ball(38, 76)
    # nuestros DC presionan (van hacia arriba)
    p.player(44, 60, "DC", team="own", role="1º presiona")
    p.player(60, 58, "DC", team="own", role="2º cubre")
    # sombra: zona que tapa la línea al pivote
    p.zone(40, 64, 56, 78, label="SOMBRA", c="#15202b", fill_op=0.30, dash="4 4")
    # carrera curvada (run) del primer DC hacia el central con balón
    p.arrow(44, 62, 40, 76, kind="run", label="curva")
    # orientar a banda: flecha indicando salida forzada hacia banda izquierda rival
    p.arrow(38, 80, 18, 72, kind="pass", label="salida forzada")
    p.legend(["run", "pass", "own", "rival", "zone"])
    save(p, "teoria-08-pressing-sombra.svg")

# --- teoria-09: basculación de las dos líneas ---
def t09():
    p = Pitch(title="Basculación de las dos líneas",
              subtitle="Balón en banda derecha · lado débil cerrado al centro")
    p.ball(86, 60)
    # línea defensiva basculada a la derecha
    p.player(48, 22, "LI", team="own", role="cierra a 3")   # lado débil metido
    p.player(58, 20, "DFC", team="own")
    p.player(72, 20, "DFC", team="own")
    p.player(88, 24, "LD", team="own", role="sale al balón")
    # línea de medios basculada
    p.player(45, 48, "EI", team="own")  # lado débil al carril central
    p.note(45, 38, "pisa centro", c="#fff5cc", size=9)
    p.player(60, 46, "MC", team="own")
    p.player(74, 46, "MC", team="own")
    p.player(88, 50, "ED", team="own", role="aprieta banda")
    # flechas de basculación (todo el bloque hacia la derecha)
    p.arrow(28, 42, 42, 42, kind="run", c="#7ee0ff", label="bascula")
    # banda lejana concedida (rótulo dentro del rectángulo, sin tocar la línea media)
    p.zone(2, 28, 22, 68, label="", c="#ff5252", fill_op=0.10)
    mnote(p, 12, 50, "banda lejana\nconcedida", c="#ffd0d0", size=9)
    p.legend(["run", "own", "zone"])
    save(p, "teoria-09-basculacion.svg")

# --- teoria-10: trampa de banda (gatillo lateral) ---
def t10():
    p = Pitch(title="Trampa de banda (gatillo: balón al lateral)",
              subtitle="Se concede el pase al lateral y se cierran las salidas")
    # rival
    p.player(70, 72, "LAT", team="rival")
    p.note(70, 64, "recibe (gatillo)", c="#ffd0d0", size=9)  # debajo del LAT
    p.player(50, 80, "DFC", team="rival")
    p.ball(70, 68)
    p.arrow(50, 80, 68, 73, kind="pass")
    p.note(50, 71, "pase concedido", c="#ffd54a", size=9)  # césped libre
    # nuestros cierres
    p.player(78, 56, "ED", team="own", role="salta al lateral")
    p.player(58, 52, "MC", team="own", role="tapa interior")
    p.player(82, 38, "LD", team="own", role="cierra línea")
    p.player(60, 30, "DFC", team="own", role="cierra vuelta")
    # flechas de presión escalonada
    p.arrow(78, 58, 72, 67, kind="run")
    p.arrow(58, 54, 64, 64, kind="block")
    p.arrow(82, 40, 76, 56, kind="run")
    # zona de robo
    p.zone(62, 58, 92, 78, label="ahogo en banda", c="#ffd54a", fill_op=0.14)
    p.legend(["pass", "run", "block", "own", "rival", "zone"])
    save(p, "teoria-10-trampa-banda.svg")

# --- teoria-11: línea de fuera de juego ---
def t11():
    p = Pitch(title="Línea de fuera de juego (la persiana)",
              subtitle="La defensa sube en bloque y deja a 2 atacantes pasados")
    # línea de cuatro subiendo (defensa propia, ataque hacia ARRIBA)
    yL = 52
    # línea horizontal trazo de fuera de juego (se dibuja primero, debajo de fichas)
    p.arrow(6, yL, 94, yL, kind="run", c="#ffd54a")
    p.note(72, 57, "línea de fuera de juego", c="#fff5cc", size=9.5)
    p.player(18, yL, "LI", team="own")
    p.player(40, yL, "DFC", team="own")
    p.player(60, yL, "DFC", team="own")
    p.player(82, yL, "LD", team="own")
    # flecha persiana: toda la línea sube (hacia y↑ = hacia el rival)
    for xx in (18, 40, 60, 82):
        p.arrow(xx, yL+3, xx, yL+12, kind="run", c="#7ee0ff")
    p.note(50, 67, "↑ SUBEN JUNTOS (achique vertical)", c="#bfe8ff", size=10)
    # atacantes rivales quedan A LA ESPALDA de la línea = pasados (y < línea,
    # lado del fondo propio, porque el rival ataca hacia ABAJO)
    p.player(31, 41, "DC", team="rival")
    p.note(31, 33, "FUERA DE JUEGO", c="#ffd0d0", size=9)
    p.player(69, 41, "DC", team="rival")
    p.note(69, 33, "FUERA DE JUEGO", c="#ffd0d0", size=9)
    # poseedor rival por delante de la línea (arriba) intentando filtrar
    p.player(50, 75, "MC", team="rival", role="no puede dar el pase")
    p.ball(50, 71)
    # pase filtrado anulado: cruzaría la línea hacia un atacante pasado
    p.arrow(50, 68, 36, 45, kind="pass", c="#ff5252")
    p.note(54, 62, "pase anulado", c="#ff8a8a", size=9)
    p.legend(["pass", "run", "own", "rival"])
    save(p, "teoria-11-fuera-de-juego.svg")

# --- teoria-12: problema 2v3 en el centro ---
def t12():
    p = Pitch(title="El problema: inferioridad 2 vs 3 en el centro",
              subtitle="Tres mediocentros rivales superan a los dos MC")
    # zona del problema (se dibuja primero, debajo de fichas/textos)
    p.zone(26, 36, 74, 76, label="", c="#ff5252", fill_op=0.12)
    # etiqueta "2 vs 3" en césped libre, esquina superior izq de la zona (sin tapar fichas)
    p.note(36, 74, "2 vs 3", c="#ffd0d0", size=12, w=800)
    # nuestros 2 MC
    p.player(40, 45, "MC", team="own")
    p.player(60, 45, "MC", team="own")
    # 3 rivales en el centro
    p.player(50, 61, "MCD", team="rival")
    p.note(50, 67.5, "pivote libre", c="#ffd0d0", size=9.5)   # debajo del MCD
    p.player(33, 70, "INT", team="rival")
    p.player(67, 70, "INT", team="rival")
    p.ball(43, 58)
    # el hombre libre supera líneas (pase ligeramente desplazado del eje)
    p.arrow(50, 58, 50, 38, kind="pass")
    # rótulo del pase en césped libre, a la derecha del eje (no toca círculos)
    p.note(67, 54, "el libre filtra", c="#ffd54a", size=9.5)
    p.legend(["pass", "own", "rival", "zone"])
    save(p, "teoria-12-problema-2v3.svg")

# --- teoria-13: solución 2v3 (pellizco extremo) ---
def t13():
    p = Pitch(title="Solución 2 vs 3: pellizco del extremo",
              subtitle="El extremo del lado débil entra al carril central = 3 funcional")
    p.ball(70, 60)  # balón en lado derecho rival
    # rivales del centro
    p.player(50, 62, "MCD", team="rival")
    p.player(34, 70, "INT", team="rival")
    p.player(66, 70, "INT", team="rival")
    # nuestros 2 MC
    p.player(42, 46, "MC", team="own")
    p.player(60, 46, "MC", team="own")
    # zona "3 funcional": etiqueta en la CABECERA (y=41) para no chocar con los MC
    p.zone(24, 40, 70, 53, label="", c="#7ee0ff", fill_op=0.14)
    p.note(47, 41, "3 funcional en el medio", c="#bfe8ff", size=9.5)
    # extremo del lado débil (izquierda) pellizca al centro
    p.player(34, 47, "EI", team="own")
    # carrera alargada y clara hacia el centro (rótulo bajo la ficha)
    p.arrow(15, 47, 31, 47, kind="run")
    p.note(24, 56, "MI entra al centro (pellizca)", c="#fff", size=9)
    # banda lejana concedida
    p.zone(2, 58, 18, 78, label="banda concedida", c="#ffd54a", fill_op=0.08)
    p.legend(["run", "own", "rival", "zone"])
    save(p, "teoria-13-solucion-2v3.svg")

# =====================================================================
# MÓDULO 03 — FASE OFENSIVA
# =====================================================================

# --- teoria-14: salida 4+2 / 3+2 ---
def t14():
    p = Pitch(title="Salida de balón 3+2 (descenso del 6)",
              subtitle="El MC posicional baja entre centrales = 3 vs 2",
              half="def")
    p.player(50, 6, "POR", team="own", role="hombre libre")
    # centrales abiertos a la anchura del área
    p.player(28, 14, "DFC", team="own")
    p.player(72, 14, "DFC", team="own")
    # 6 baja entre ellos
    p.player(50, 16, "MC6", team="own", role="baja a salir")
    p.arrow(50, 30, 50, 19, kind="run", label="drop")
    # laterales altos y abiertos
    p.player(10, 30, "LI", team="own", role="alto y abierto")
    p.player(90, 30, "LD", team="own", role="alto y abierto")
    # 8 liberado entre líneas
    p.player(55, 38, "MC8", team="own", role="libre entre líneas")
    # 2 DC rivales presionando
    p.player(40, 30, "DC", team="rival")
    p.player(60, 30, "DC", team="rival")
    p.ball(46, 14)
    p.zone(24, 9, 76, 23, label="", c="#7ee0ff", fill_op=0.12)
    p.note(50, 24, "superioridad 3 vs 2", c="#bfe8ff", size=10)
    p.legend(["run", "own", "rival", "zone"])
    save(p, "teoria-14-salida-3mas2.svg")

# --- teoria-15: tercer hombre / construcción ---
def t15():
    p = Pitch(title="Tercer hombre y triángulos de pase",
              subtitle="Central → pivote de espaldas → liberado de cara")
    p.player(40, 35, "DFC", team="own", role="inicia")
    p.player(50, 52, "MC6", team="own")
    p.note(50, 41, "recibe de espaldas", c="#fff5cc", size=9)
    p.player(66, 64, "MC8", team="own")
    p.note(74, 68, "3er hombre (de cara)", c="#fff5cc", size=9)
    p.ball(40, 39)
    # triángulo de banda (se dibuja antes para quedar bajo flechas/fichas)
    p.zone(62, 48, 94, 86, label="", c="#ffd54a", fill_op=0.10)
    p.note(78, 50, "triángulo de banda", c="#fff", size=9)
    p.player(86, 56, "ED", team="own")
    p.player(86, 80, "DC", team="own")
    # secuencia numerada del tercer hombre: 1 → 2 (descarga) → 3 (al liberado)
    p.arrow(40, 39, 49, 50, kind="pass", label="1")
    p.arrow(51, 54, 65, 63, kind="pass", label="2")
    p.arrow(68, 65, 84, 56, kind="pass", label="3")
    p.legend(["pass", "own", "zone"])
    save(p, "teoria-15-tercer-hombre.svg")

# --- teoria-16: apoyo + ruptura de los delanteros ---
def t16():
    p = Pitch(title="Automatismo de la dupla: el apoyo arrastra, la ruptura ataca",
              subtitle="El MC con balón encuentra al que rompe a la espalda del central que siguió al apoyo",
              half="att")
    # ESPACIO que se abre a la espalda del central que sigue al apoyo
    p.zone(24, 83, 56, 96, label="espacio a la espalda", c="#7ee0ff", fill_op=0.20)
    # central rival 1: marca al APOYO y SALE a seguirlo -> vacía su espalda
    p.player(44, 74, "DFC", team="rival", role="sigue al apoyo")
    p.arrow(45, 85, 44, 76, kind="run")          # sube siguiendo al apoyo
    p.note(57, 78, "el central muerde y deja su espalda", c="#ff9e9e", size=9.5)
    # central rival 2: marca al de RUPTURA, pero llega tarde al espacio
    p.player(68, 87, "DFC", team="rival", role="su central (tarde)")
    # MC con balón (el que asiste)
    p.player(52, 55, "MC", team="own", role="MC con balón")
    p.ball(52, 58)
    # DC de APOYO: baja de cara y arrastra a su central
    p.player(33, 68, "DC", team="own", role="APOYO: fija y arrastra", role_below=True)
    p.arrow(33, 80, 33, 70, kind="run")
    p.note(22, 74, "baja de cara", c="#ffffff", size=10)
    # DC de RUPTURA: ataca el espacio a la espalda del central que subió
    p.player(70, 76, "DC", team="own", role="RUPTURA", role_below=True)
    p.arrow(68, 75, 47, 91, kind="run")
    p.note(62, 86, "ataca la espalda", c="#ffffff", size=10)
    # pase del MC al espacio (al que rompe), NO al pie del apoyo
    p.arrow(52, 59, 46, 89, kind="pass")
    p.note(63, 66, "pase al espacio", c="#ffd54a", size=10)
    p.note(50, 50.5, "El apoyo no recibe: su función es FIJAR al central y VACIAR la zona", c="#fff5cc", size=10)
    p.legend(["run", "pass", "own", "rival", "zone"])
    save(p, "teoria-16-apoyo-ruptura.svg")

# --- teoria-17: ataque del área con dos puntas (centro) ---
def t17():
    p = Pitch(title="Ataque del área en el centro (2 puntas)",
              subtitle="Centro desde banda derecha · poblar 3-4 zonas de remate",
              half="att")
    # extremo que centra desde banda derecha
    p.player(90, 78, "ED", team="own", role="centra / cut-back")
    p.ball(90, 74)
    # zonas de remate
    p.player(62, 90, "DC", team="own", role="1er palo")
    p.player(50, 86, "DC", team="own", role="penalti")
    p.player(35, 88, "EI", team="own", role="2º palo")
    p.player(50, 70, "MC8", team="own", role="frontal/rechace")
    # trayectorias de centro (sin rótulo: las fichas ya están rotuladas)
    p.arrow(90, 76, 62, 88, kind="pass")
    p.arrow(90, 76, 50, 84, kind="pass")
    p.arrow(90, 74, 50, 72, kind="pass", label="cut-back")
    p.legend(["pass", "own"])
    save(p, "teoria-17-ataque-area.svg")

# --- teoria-18: desdoblamiento lateral-extremo (overlap/underlap) ---
def t18():
    p = Pitch(title="Desdoblamiento lateral-extremo",
              subtitle="OVERLAP (izq) y UNDERLAP (der)")
    # OVERLAP lado izquierdo: extremo dentro, lateral por fuera
    p.player(28, 55, "EI", team="own", role="pisa dentro")
    p.player(12, 45, "LI", team="own", role="overlap")
    p.arrow(12, 47, 14, 72, kind="run", label="por fuera")
    p.arrow(28, 57, 30, 70, kind="drive")
    p.note(20, 88, "OVERLAP", c="#bfe8ff", size=11)
    p.ball(28, 51)
    # UNDERLAP lado derecho: extremo por fuera retiene, lateral por dentro
    p.player(88, 55, "ED", team="own", role="retiene fuera")
    p.player(72, 45, "LD", team="own", role="underlap")
    p.arrow(72, 47, 70, 72, kind="run", label="por dentro")
    p.arrow(88, 57, 88, 72, kind="drive")
    p.note(80, 88, "UNDERLAP", c="#bfe8ff", size=11)
    p.legend(["run", "drive", "own"])
    save(p, "teoria-18-desdoblamiento.svg")

# =====================================================================
# MÓDULO 04 — TRANSICIONES Y BALÓN PARADO
# =====================================================================

# --- teoria-19: transición ofensiva (contraataque) ---
def t19():
    p = Pitch(title="Transición ofensiva: contraataque vertical",
              subtitle="Robo en zona media · pase vertical a los dos puntas")
    # robo
    p.player(50, 44, "MC", team="own")
    p.note(38, 41, "ROBO", c="#fff5cc", size=9.5)  # césped libre a la izq
    p.ball(50, 48)
    # DC apoyo y DC ruptura
    p.player(42, 70, "DC", team="own", role="apoyo")
    p.player(62, 72, "DC", team="own")
    p.note(62, 64, "ruptura", c="#fff5cc", size=9)  # debajo de la ficha
    p.arrow(62, 74, 72, 92, kind="run", label="a la espalda")
    # pase vertical
    p.arrow(50, 51, 61, 71, kind="pass", label="pase vertical")
    # extremo corre el carril
    p.player(88, 58, "ED", team="own", role="corre carril")
    p.arrow(88, 60, 88, 84, kind="run")
    # MC 8 llega de tercer hombre
    p.player(70, 56, "MC8", team="own")
    p.note(70, 48, "3er hombre", c="#fff5cc", size=9)
    p.arrow(70, 58, 72, 76, kind="run")
    p.legend(["pass", "run", "own"])
    save(p, "teoria-19-contraataque.svg")

# --- teoria-20: transición defensiva (repliegue) ---
def t20():
    p = Pitch(title="Transición defensiva: repliegue 4-4-2",
              subtitle="Recomponer las dos líneas · primero el eje central")
    # primer jugador ocupa el eje para frenar el balón
    p.player(50, 55, "MC", team="own", role="frena el eje")
    p.player(50, 70, "DC", team="rival", role="con balón")
    p.ball(50, 66)
    p.arrow(50, 62, 50, 58, kind="block", label="frena central")
    # flechas de repliegue de cada jugador a su carril/línea
    # línea de medios reformándose
    p.player(20, 50, "EI", team="own"); p.arrow(28, 60, 21, 52, kind="run")
    p.player(80, 50, "ED", team="own"); p.arrow(72, 60, 79, 52, kind="run")
    p.player(38, 48, "MC", team="own"); p.arrow(44, 58, 39, 50, kind="run")
    # línea defensiva
    p.player(18, 30, "LI", team="own")
    p.player(40, 28, "DFC", team="own")
    p.player(60, 28, "DFC", team="own")
    p.player(82, 30, "LD", team="own")
    p.note(50, 20, "dos líneas de cuatro recompuestas", c="#cfe", size=10)
    p.legend(["run", "block", "own", "rival"])
    save(p, "teoria-20-repliegue.svg")

# --- teoria-21: contrapresión 3-5 s ---
def t21():
    p = Pitch(title="Contrapresión (3-5 segundos)",
              subtitle="Salto inmediato al balón + cierre de líneas cortas")
    # cuenta atrás (zona; etiqueta en la cabecera para no pisar fichas)
    p.zone(34, 44, 78, 74, label="", c="#ff5252", fill_op=0.12)
    p.note(56, 72, "3-5 s para robar", c="#ffd0d0", size=10)
    # punto de pérdida
    p.player(55, 60, "RIVAL", team="rival")
    p.note(55, 52, "recupera", c="#ffd0d0", size=9)  # debajo del rival, legible
    p.ball(55, 56)
    # los más cercanos saltan al balón
    p.player(48, 68, "DC", team="own", role="ataca balón")
    p.player(66, 66, "MC8", team="own", role="2º salto")
    p.arrow(48, 66, 53, 60, kind="run")
    p.arrow(66, 64, 59, 60, kind="run")
    # apoyos laterales del rival (líneas de pase que hay que cerrar)
    p.player(38, 58, "AP", team="rival")
    p.player(74, 58, "AP", team="rival")
    # cierre de líneas cortas: block sobre los APOYOS, no sobre el balón
    p.player(40, 48, "MC6", team="own", role="tapa apoyo")
    p.player(72, 50, "ED", team="own", role="tapa apoyo")
    p.arrow(40, 50, 38, 56, kind="block")
    p.arrow(72, 52, 74, 56, kind="block")
    p.legend(["run", "block", "own", "rival", "zone"])
    save(p, "teoria-21-contrapresion.svg")

# --- teoria-22: córner ofensivo (masa de rematadores + bloqueos) ---
def t22():
    p = Pitch(title="Balón parado a favor: córner ofensivo",
              subtitle="Masa de rematadores + bloqueos · 1-2 arriba para la contra",
              half="att")
    # lanzador en el córner (banda derecha, fondo)
    p.player(95, 95, "LANZ", team="own", role="saca")
    p.ball(95, 92)
    # rematadores en zonas
    p.player(60, 95, "DC", team="own", role="1er palo")
    p.player(50, 90, "DC", team="own", role="zona central")
    p.player(40, 93, "DFC", team="own", role="2º palo")
    p.player(50, 78, "MC8", team="own", role="frontal/rechace")
    # bloqueo (cortina) ejemplo
    p.player(55, 86, "EI", team="own", role="bloqueo")
    p.arrow(95, 90, 52, 89, kind="pass", label="centro")
    # 1 arriba para contra
    p.player(50, 60, "DC", team="own", role="arriba (contra)")
    p.legend(["pass", "own"])
    save(p, "teoria-22-corner-ofensivo.svg")

# --- teoria-23: distancias y compacidad del bloque ---
def t23():
    p = Pitch(title="Compacidad: distancias del bloque",
              subtitle="Regla de Sacchi · 25-30 m de la 1ª a la última línea")
    # delanteros (primera línea)
    p.player(42, 70, "DC", team="own")
    p.player(58, 70, "DC", team="own")
    # medios
    p.player(15, 56, "EI", team="own")
    p.player(40, 53, "MC", team="own")
    p.player(60, 53, "MC", team="own")
    p.player(85, 56, "ED", team="own")
    # defensa (última línea)
    p.player(18, 38, "LI", team="own")
    p.player(40, 36, "DFC", team="own")
    p.player(60, 36, "DFC", team="own")
    p.player(85, 38, "LD", team="own")
    # cota de distancia entre líneas (lado izquierdo)
    p._line(p.X(4), p.Y(70), p.X(4), p.Y(36), w=2, c="#ffd54a")
    p.note(7, 53, "25-30 m", c="#fff5cc", size=9)
    # distancia corta entre líneas resaltada
    p.zone(10, 45, 90, 60, label="", c="#7ee0ff", fill_op=0.10)
    p.note(50, 49, "líneas cortas (8-12 m entre sí)", c="#bfe8ff", size=9)
    # bloque compacto
    p.zone(8, 34, 92, 72, label="", c="#ffd54a", fill_op=0.06, dash="6 5")
    p.note(50, 30, "bloque compacto = pocos espacios interiores", c="#cfe", size=9)
    save(p, "teoria-23-compacidad-distancias.svg")

ALL = [t01,t02,t03,t04,t05,t06,t07,t08,t09,t10,t11,t12,t13,
       t14,t15,t16,t17,t18,t19,t20,t21,t22,t23]
for f in ALL:
    f()
print("TOTAL", len(ALL))
