#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las infografías de planificación (charts) del curso de pretemporada."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))
from chart import Calendar, Curve, Bars, Timeline, PAL

OUT = HERE
def p(name): return os.path.join(OUT, name)

# ============================ CONCEPTO / TEORÍA ============================

# 1) Mapa de fases de la pretemporada (6 semanas tipo)
Timeline(
    "Las 3 fases de la pretemporada", weeks=6,
    subtitle="modelo en embudo: de lo general a lo específico, afilando hacia el debut",
    phases=[
        ("ACUMULACIÓN", 1, 2, PAL["baja"], "volumen · base aeróbica"),
        ("TRANSFORMACIÓN", 3, 4, PAL["media"], "sube intensidad · específico · táctico"),
        ("REALIZACIÓN", 5, 6, PAL["blue"], "tapering · ritmo de competición"),
    ],
    rows=[
        ("Amistosos", [(2, 2, "1º suave", PAL["panelb"]), (3, 3, "2º", PAL["partido"]),
                       (4, 4, "3º-4º", PAL["partido"]), (5, 5, "5º fuerte", PAL["partido"]),
                       (6, 6, "DEBUT", PAL["gold"])]),
        ("Tests", [(1, 1, "30-15 / Yo-Yo", PAL["media"]), (6, 6, "re-test", PAL["media"])]),
    ],
).save(p("fases-pretemporada.svg"))

# 2) Supercompensación
Curve(
    "Supercompensación: por qué descansar entrena", area=True,
    subtitle="el estímulo baja el rendimiento; con la recuperación rebota por encima",
    points=[("", .5), ("estímulo", .5), ("fatiga", .2), ("recuperación", .5),
            ("supercomp.", .82), ("nueva base", .66)],
    bands=[(.47, .53, PAL["gold"], .14, "nivel inicial")],
    markers=[(2, "cae el rendimiento", PAL["alta"]), (4, "aquí toca el siguiente estímulo", PAL["baja"])],
    ylab="rendimiento",
).save(p("curva-supercompensacion.svg"))

# 3) ACWR semáforo (eje 0..2)
Curve(
    "ACWR: el semáforo de la carga", color=PAL["gold"],
    subtitle="carga aguda (7 d) ÷ crónica (28 d) · mantenla en la zona verde, evita los picos",
    points=[("Sem1", .50), ("Sem2", .58), ("Sem3", .62), ("Sem4", .55), ("Sem5", .47), ("Sem6", .50)],
    bands=[(.0, .40, PAL["reposo"], .22, "< 0,8 desentreno"),
           (.40, .65, PAL["baja"], .20, "0,8 – 1,3 zona segura"),
           (.75, 1.0, PAL["alta"], .20, "> 1,5 riesgo de lesión")],
    ylab="ACWR (×2)", area=False,
).save(p("acwr-semaforo.svg"))

# 4) Rampa de carga semanal (~10%) + taper
Bars(
    "Rampa de carga semanal (regla del ~10 %)", unit=" UA", maxv=3100,
    subtitle="sube progresivo, sin saltos bruscos; la última semana descarga (tapering)",
    items=[("Semana 1 · base", 1800, PAL["baja"]),
           ("Semana 2 · +11 %", 2300, PAL["media"]),
           ("Semana 3 · +17 %", 2700, PAL["media"]),
           ("Semana 4 · pico", 2900, PAL["alta"]),
           ("Semana 5 · estabiliza", 2500, PAL["media"]),
           ("Semana 6 · taper −40 %", 1700, PAL["baja"])],
).save(p("rampa-carga.svg"))

# 5) sRPE por tipo de sesión
Bars(
    "Cuánto pesa cada sesión (sRPE = RPE × minutos)", unit=" UA", maxv=820,
    subtitle="carga interna estimada sin tecnología, solo con la percepción de esfuerzo",
    items=[("Regenerativo  40' × RPE 3", 120, PAL["baja"]),
           ("Técnico-táctico  75' × 5", 375, PAL["media"]),
           ("Juegos reducidos  80' × 6", 480, PAL["media"]),
           ("HIIT / gran formato  70' × 8", 560, PAL["alta"]),
           ("Amistoso  90' × 8", 720, PAL["partido"]),
           ("Día doble  60'×7 + 60'×6", 780, PAL["alta"])],
).save(p("srpe-tipos.svg"))

# 6) Ondulación de la carga (duro-suave) — evita la monotonía
Curve(
    "Ondula la carga: alterna duro y suave", color=PAL["gold"],
    subtitle="semanas planas (monotonía > 2) = más fatiga y riesgo; busca picos y valles",
    points=[("LUN", .55), ("MAR", .9), ("MIÉ", .3), ("JUE", .9), ("VIE", .5), ("SÁB", .85), ("DOM", .1)],
    ylab="carga del día",
).save(p("ondulacion-monotonia.svg"))

# 7) Orden de capacidades
Timeline(
    "Orden de las capacidades físicas", weeks=6,
    subtitle="el motor primero (aeróbico), lo explosivo al final, prevención siempre",
    phases=[("BASE → HIIT → RSA → VELOCIDAD", 1, 6, PAL["blue"], "de lo general y seguro a lo específico y exigente")],
    rows=[
        ("Base aeróbica", [(1, 2, "énfasis", PAL["baja"]), (3, 6, "mantener", PAL["reposo"])]),
        ("HIIT (pot. aeróbica)", [(2, 4, "énfasis", PAL["media"])]),
        ("RSA (sprints repetidos)", [(3, 5, "énfasis", PAL["media"])]),
        ("Velocidad / fuerza máx.", [(4, 6, "énfasis", PAL["alta"])]),
        ("Prevención (Nordic, core)", [(1, 6, "continuo, casi diario", PAL["blue"])]),
    ],
).save(p("orden-capacidades.svg"))

# 8) Tapering: volumen baja, intensidad se mantiene
Curve(
    "Puesta a punto (tapering) hacia el debut", color=PAL["gold"],
    subtitle="baja el VOLUMEN ~40-60 % y MANTÉN la intensidad: así llegas fresco sin perder forma",
    points=[("MD-9", .9), ("MD-7", .82), ("MD-5", .7), ("MD-4", .55),
            ("MD-3", .45), ("MD-2", .36), ("MD-1", .3), ("DEBUT", .28)],
    points2=[("MD-9", .72), ("MD-7", .73), ("MD-5", .72), ("MD-4", .74),
             ("MD-3", .72), ("MD-2", .73), ("MD-1", .7), ("DEBUT", .9)],
    legend2=("volumen", "intensidad"),
    ylab="% de la carga", area=True,
).save(p("curva-tapering.svg"))

# ============================ CALENDARIOS (microciclos) ============================
A, M, B, R, P_ = "alta", "media", "baja", "reposo", "partido"

def day(d, load, sessions=None):
    return {"d": d, "load": load, "sessions": sessions or []}

def s(slot, focus, load): return {"slot": slot, "focus": focus, "load": load}

# DOBLES SESIONES — profesional / semipro
Calendar(
    "Microciclo tipo · DOBLES SESIONES (pro / semipro)",
    subtitle="9–12 sesiones · mañana = calidad/fuerza (fresco) · tarde = balón/condicional",
    note="2 picos · 1 descanso total",
    days=[
        day("LUN", M, [s("AM", "Fuerza + prevención", M), s("PM", "Técnica + posesión", M)]),
        day("MAR", A, [s("AM", "Velocidad / potencia", M), s("PM", "HIIT con balón (SSG)", A)]),
        day("MIÉ", B, [s("AM", "Regenerativo + movilidad", B)]),
        day("JUE", A, [s("AM", "Fuerza-pot.", M), s("PM", "Táctico intenso + fase de juego", A)]),
        day("VIE", M, [s("AM", "Activación + ABP", B), s("PM", "Táctico fino", M)]),
        day("SÁB", P_, [s("", "AMISTOSO", P_)]),
        day("DOM", R),
    ],
).save(p("micro-dobles.svg"))

# 6 SESIONES (L-S)
Calendar(
    "Microciclo tipo · 6 SESIONES (lunes a sábado)",
    subtitle="sesión única diaria · 1 capacidad dominante por día + dosis de mantenimiento",
    note="2 picos (MAR y JUE)",
    days=[
        day("LUN", B, [s("", "Reactivación + fuerza/prevención", B)]),
        day("MAR", A, [s("", "Resistencia con balón · HIIT/SSG", A)]),
        day("MIÉ", M, [s("", "Velocidad (inicio) + táctico", M)]),
        day("JUE", A, [s("", "Fuerza-pot. + táctico intenso", A)]),
        day("VIE", B, [s("", "Táctico fino / activación", B)]),
        day("SÁB", P_, [s("", "AMISTOSO", P_)]),
        day("DOM", R),
    ],
).save(p("micro-6.svg"))

# 5 SESIONES
Calendar(
    "Microciclo tipo · 5 SESIONES",
    subtitle="el descanso del miércoles separa los 2 picos y garantiza las 48 h",
    note="resistencia ~100 % con balón",
    days=[
        day("LUN", B, [s("", "Reactivación + fuerza", B)]),
        day("MAR", A, [s("", "Condicional con balón · HIIT/SSG", A)]),
        day("MIÉ", R),
        day("JUE", A, [s("", "Velocidad + táctico-potencia + fuerza 15'", A)]),
        day("VIE", M, [s("", "Táctico", M)]),
        day("SÁB", P_, [s("", "AMISTOSO", P_)]),
        day("DOM", R),
    ],
).save(p("micro-5.svg"))

# 4 SESIONES
Calendar(
    "Microciclo tipo · 4 SESIONES",
    subtitle="umbral: la integración físico-táctica deja de ser opción · cada sesión es híbrida",
    note="VIE = trabajo autónomo",
    days=[
        day("LUN", M, [s("", "Fuerza-prev 15' + técnica/posesión", M)]),
        day("MAR", A, [s("", "Resistencia con balón (SSG) + finalización", A)]),
        day("MIÉ", R),
        day("JUE", A, [s("", "Velocidad/potencia (inicio) + táctico/fases", A)]),
        day("VIE", B, [s("", "AUTÓNOMO: rodaje + Nordic", B)]),
        day("SÁB", P_, [s("", "AMISTOSO", P_)]),
        day("DOM", R),
    ],
).save(p("micro-4.svg"))

# 3 SESIONES — amateur típico
Calendar(
    "Microciclo tipo · 3 SESIONES (amateur)",
    subtitle="prioridad a lo específico e integrado · la resistencia de base se externaliza",
    note="1 solo pico claro",
    days=[
        day("LUN", B, [s("", "AUTÓNOMO: rodaje aeróbico 30'", B)]),
        day("MAR", M, [s("", "Prevención corta + técnica + táctica", M)]),
        day("MIÉ", B, [s("", "AUTÓNOMO: prevención + movilidad", B)]),
        day("JUE", A, [s("", "PICO: condicional con balón + fase de juego", A)]),
        day("VIE", R),
        day("SÁB", P_, [s("", "AMISTOSO / partido", P_)]),
        day("DOM", R),
    ],
).save(p("micro-3.svg"))

# 2 SESIONES — fútbol base / recursos muy limitados
Calendar(
    "Microciclo tipo · 2 SESIONES (base / recursos limitados)",
    subtitle="mínimos imprescindibles · todo integrado en el juego · cero tiempo muerto",
    note="el partido del finde es la carga fuerte",
    days=[
        day("LUN", R),
        day("MAR", M, [s("", "Activación + técnica densa + juego reducido", M)]),
        day("MIÉ", B, [s("", "RETO de balón en casa (voluntario)", B)]),
        day("JUE", M, [s("", "Técnica + juego / competición interna", M)]),
        day("VIE", R),
        day("SÁB", P_, [s("", "PARTIDO", P_)]),
        day("DOM", R),
    ],
).save(p("micro-2.svg"))

print("charts OK")
