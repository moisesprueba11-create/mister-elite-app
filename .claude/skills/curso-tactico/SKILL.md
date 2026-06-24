---
name: curso-tactico
description: >-
  Genera un curso táctico de fútbol COMPLETO y profesional para un sistema dado
  (p. ej. 1-4-3-3, 1-3-5-2, 1-4-2-3-1), con la metodología multi-agente, la
  estética y la marca MISTER ÉLITE — Moisés Díaz. Produce módulos de teoría
  concisos, un banco grande de tareas de campo (cada una con su pizarra), portada
  profesional y los entregables en PDF + sitio HTML + HTML único autocontenido.
  Filosofía: poca teoría, mucha aplicación práctica. Úsalo cuando el usuario pida
  "crea el curso del <sistema>", "hazme el 1-4-3-3", "otro sistema con la skill", etc.
---

# Curso táctico (MISTER ÉLITE)

Reproduce, para CUALQUIER sistema, el producto que ya se validó con el 1-4-4-2:
contenido riguroso + pizarras coherentes + PDF/HTML con marca, pasando por un
**bucle de calidad con evaluador final** hasta que el producto sea "TOP" (≥ 8.5/10).

## 0) Entrada
- **Sistema** (obligatorio): p. ej. `1-4-3-3`. Slug = sistema sin guion inicial → carpeta `curso-1433/`.
- Opcionales: idioma (def. español), nº de tareas (def. 24-27), categorías (Formativo/Amateur/Senior).

## 1) Preparar el proyecto
1. Crea la carpeta `curso-<slug>/` con subcarpetas `modulos/ ejercicios/ graficos/ graficos/lib/ _pipeline/investigacion/ _pipeline/evaluacion/`.
2. Copia los activos de esta skill al curso:
   - `assets/pitch.py` → `curso-<slug>/graficos/lib/pitch.py`
   - `assets/build_pdf.py`, `assets/build_site.py`, `assets/build_onefile.py`, `assets/build_cover.py` → `curso-<slug>/`
3. **Define la convención de dorsales/posiciones del sistema** (es lo único que cambia de verdad). Escríbela en `curso-<slug>/_pipeline/CONVENCION.md` y úsala en TODO el curso. Reglas fijas de nomenclatura:
   - Abreviaturas: POR, LD, LI, DFC; **MC** mediocentros; **DC** delanteros; **EI** = extremo izquierdo, **ED** = extremo derecho (NUNCA "MI/MD" ni "medio de banda"). Interiores = **MC** con matiz (o "INT" si el sistema lo pide).
   - Dorsales por defecto (ajusta al sistema): 1 POR · 2 LD · 3 LI · 4 central der · 5 central izq · 6 MC defensivo · 7 EI · 8 MC ofensivo/interior · 9 DC · 10 segundo delantero/media punta o interior · 11 ED.
   - Ejemplo 1-4-3-3: 1 POR · 2 LD · 3 LI · 4/5 centrales · 6 pivote · 8/10 interiores · 7 ED · 11 EI · 9 DC.

## 2) Investigación (agentes en paralelo)
Lanza 3-4 agentes `general-purpose` en paralelo (run_in_background), uno por área, que ESCRIBEN su informe en `_pipeline/investigacion/`:
fundamentos/estructura · roles+fase defensiva · fase ofensiva+transiciones+ABP · **banco de 24-27 tareas** (lo más importante: fichas de campo con transferencia real al sistema).
Cada agente: rigor de licencia UEFA, sin relleno; puede usar WebSearch.

## 3) Curación (estándar MUY alto)
Un agente cura los informes, corrige imprecisiones, unifica terminología con la CONVENCION y eleva el banco de tareas. Escribe `_pipeline/investigacion/00-VALIDACION.md`. Rechaza tareas genéricas.

## 4) Escritura
Un agente escribe en español (poca teoría, mucha práctica):
- `README.md` (portada-índice + **tabla de convención de dorsales** + distancias + leyenda + glosario).
- `modulos/01-fundamentos.md … 04-transiciones-y-balon-parado.md` (cada uno con "Ideas clave" y "Errores comunes").
- `ejercicios/00-plan-sesiones.md` (2 microciclos) + `01..07` por bloques con fichas uniformes (Objetivo·Organización·Desarrollo·Provocaciones·Variantes·Coaching·Duración/Categoría).
- Inserta un placeholder de imagen `![Pizarra ...](../graficos/<archivo>.svg)` por CADA tarea y en cada concepto teórico clave; lista todos en `graficos/PEDIDOS.md`.
> Mantén EXACTAMENTE estos nombres de archivo (módulos 01-04, ejercicios 00-07): los build scripts dependen de ellos. Si cambias bloques, actualiza la lista `PAGES`/`DOCS` en `build_site.py`, `build_pdf.py`, `build_onefile.py`.

## 5) Gráficos (motor `pitch.py`)
Agentes en paralelo (propiedad de archivos separada para evitar conflictos):
- Diagramas de teoría → `graficos/teoria-NN-slug.svg` (formación base con dorsales, variantes, bloques, pressing, basculación, fuera de juego, salida, apoyo+ruptura, ataque del área, desdoblamiento, transiciones…). El **Módulo 1 ≥ 5-6 diagramas**.
- Una pizarra por tarea → `graficos/tarea-01.svg … tarea-NN.svg`, FIEL a su Organización/Desarrollo/Provocación.
- API en `assets/pitch.py` (cabecera del archivo). Coordenadas: x 0..100 izq→der, y 0..100 fondo propio abajo→rival arriba, ataque hacia arriba. Numerar secuencias 1-2-3.
- OBLIGATORIO autoverificar: renderizar a PNG con `cairosvg` y LEER el PNG; iterar hasta que sea legible y coherente (sin texto sobre fichas).

## 6) Revisión + corrección de gráficos (bucle)
- Revisores comparan cada pizarra (render PNG) con su texto y puntúan coherencia/legibilidad/calidad (informe en `_pipeline/evaluacion/`).
- Correctores arreglan BLOQUEANTES y menores editando los generadores/SVG (manteniendo nombres). Repite hasta limpio.

## 7) Portada
Edita el `CONFIG` de `build_cover.py` (system, title_big, dorsales por línea `lines` de defensa→delantera, `gk`, `stats`) y ejecútalo → `graficos/portada.svg`. Verifica el render.

## 8) Entregables
Desde `curso-<slug>/`: `python3 build_site.py`, `python3 build_pdf.py`, `python3 build_onefile.py`.
Comprueba **0 rutas de imagen rotas** y que cada tarea tiene exactamente 1 pizarra.
Salidas: `site/` (web navegable), `curso-<slug>.pdf` (portada como pág. 1), `curso-<slug>-completo.html` (1 archivo autocontenido).

> **Nombres ESTABLES (no negociable):** al corregir o actualizar un curso ya existente, los entregables conservan SIEMPRE el mismo nombre que la versión anterior (`curso-<slug>.pdf`, `curso-<slug>-completo.html`). El build sobrescribe; NUNCA se añaden sufijos de versión (`-v2`, `-final`, fechas…). Así la nueva versión reemplaza a la anterior al subirla y el usuario no acumula copias dobladas.

## 9) Evaluador final → bucle hasta TOP
Un agente evaluador revisa el producto REAL (contenido, cobertura de imágenes, calidad/coherencia gráfica, portada/marca, PDF) y puntúa por dimensión + global. Veredicto en `_pipeline/evaluacion/VEREDICTO-FINAL.md`:
- **TOP** si ≥ 8.5 y sin bloqueantes → entrega.
- Si no, devuelve must-fix concretos → vuelve al paso pertinente (normalmente 6) y RE-EVALÚA. Repite hasta TOP.

## Convenciones fijas (no cambian entre sistemas)
- Marca **MISTER ÉLITE — Moisés Díaz** en portada y al pie de cada pizarra (lo pone `pitch.py`).
- Estética: paleta y estilo de `pitch.py`; portada dorada/azul de `build_cover.py`.
- Nomenclatura EI/ED, no MI/MD. Reservar la línea roja `kind="block"` solo para bloqueo/corte real.
- En el plan de sesiones, `MD` = "matchday" (MD-4…MD): NO confundir con posición.
- Git: desarrollar en la rama indicada, commit/push frecuente; no abrir PR salvo que lo pidan.

## Entrega al usuario
Envía el **PDF** y el **HTML único** con SendUserFile y resume el veredicto del evaluador. Ofrece extras (logo real, índice clicable, animaciones por código).
