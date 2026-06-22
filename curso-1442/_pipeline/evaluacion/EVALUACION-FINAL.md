# EVALUACIÓN FINAL DE CALIDAD — Curso "Sistema 1-4-4-2: del concepto al campo"

> Rol: evaluador final de producto formativo. Listón: "producto TOP" (curso que un entrenador profesional pagaría y un formador de entrenadores avalaría).
> Objeto evaluado: `/home/user/mister-elite-app/curso-1442/` (README + 4 módulos + 7 archivos de ejercicios con 25 tareas + plan de sesiones + 21 gráficos SVG + PEDIDOS.md).
> Fecha: 2026-06-22.
> Método: lectura íntegra de los 12 documentos de texto; verificación automática de los 21 enlaces a gráficos contra los archivos reales; verificación de los enlaces internos `.md`; inspección directa de 4 SVG (01, 09, 14 y muestreo de tamaños/validez de los 21); contraste con el informe de validación del pipeline.

---

## 1. Puntuación por criterio

| # | Criterio | Nota /10 | Peso | Aportación |
|---|----------|---------|------|-----------|
| 1 | Propósito ("poca teoría, mucha aplicación práctica") | 9.5 | 20% | 1.90 |
| 2 | Contenido táctico (rigor y profundidad sobre el 1-4-4-2) | 9.5 | 20% | 1.90 |
| 3 | Tareas (completas, ejecutables, con transferencia + plan de sesiones) | 9.5 | 25% | 2.375 |
| 4 | Integración de gráficos (enlaces vivos + refuerzo del texto) | 9.5 | 15% | 1.425 |
| 5 | Navegación y coherencia (enlaces, terminología, sin contradicciones) | 9.0 | 12% | 1.08 |
| 6 | Acabado editorial (redacción y formato) | 9.5 | 8% | 0.76 |

### Puntuación global ponderada: **9.4 / 10**

---

## 2. VEREDICTO

# ✅ PRODUCTO TOP

Cumple los dos requisitos del listón: **global ≥ 9.0 (9.4)** y **sin defectos graves (cero BLOQUEANTES)**. Es un curso publicable tal cual; los defectos detectados son MENORES y mejoran un producto que ya es de nivel profesional. Todos los enlaces a gráficos están vivos (0 rotos), todos los enlaces internos resuelven, la terminología está unificada y la práctica domina sobre la teoría como exige la filosofía declarada.

---

## 3. Análisis por criterio

### Criterio 1 — Propósito (9.5)
- La filosofía "poca teoría, mucha aplicación" se cumple de forma medible: la teoría son 4 módulos concisos (~480 líneas) que **siempre cierran con "Ideas clave" + "Errores comunes"**; la práctica son 25 fichas de tarea + un plan de 2 microciclos (~616 líneas), más 8 de los 21 diagramas dedicados a tareas concretas.
- Cada bloque de ejercicios abre remitiendo a su módulo teórico y recordando que "el módulo dice *qué* y *por qué*; las fichas dicen *cómo*". La jerarquía teoría→aplicación es explícita y respetada.
- Ningún ejercicio es una "posesión genérica": todos tienen porterías o zonas-meta y reproducen un mecanismo concreto del sistema.

### Criterio 2 — Contenido táctico (9.5)
- Cobertura completa y correcta de las cuatro fases: estructura/variantes (plano, rombo, asimétrico), fase defensiva (bloques, basculación, coberturas, pressing con gatillos, fuera de juego), fase ofensiva (salida +1, doble pivote, último tercio, automatismos) y transiciones + balón parado.
- Tratamiento sobresaliente del **problema estructural 2 vs 3 en el centro**, hilo conductor del curso, con un repertorio de 6 soluciones concretas (M02 §6).
- Enfrentamientos sistémicos (vs 4-3-3, 3-5-2, espejo 4-4-2, 4-2-3-1) precisos y accionables, no tópicos.
- Referencias históricas correctas y bien contextualizadas (Sacchi como origen de la compacidad, Simeone/Leicester en transición). Sin errores tácticos.

### Criterio 3 — Tareas y plan de sesiones (9.5)
- Las 25 fichas siguen una plantilla uniforme (Objetivo · Tipo · Organización [jugadores/espacio/material] · Desarrollo · Provocaciones · Variantes fácil→difícil · Coaching · Duración/Categoría F-A-S). Son inmediatamente ejecutables en campo.
- Las "provocaciones" (reglas que premian/castigan la conducta objetivo) son el motor metodológico y están muy bien calibradas: gol válido solo con el patrón "uno baja/uno rompe" (T14), cuerda que penaliza alargar el bloque (T5), gatillo del lateral antes del 2.º toque (T11), tres puntos del área obligatorios + cut-back (T15), bonificaciones por fase en el 11v11 (T23).
- El plan de sesiones (`00-plan-sesiones.md`) integra excelentemente: 2 microciclos MD-4→MD-1 con progresión analítico→global, enlaces a la ficha de cada tarea, y un "mapa rápido tarea→bloque". Las 25 tareas quedan distribuidas con criterio.

### Criterio 4 — Integración de gráficos (9.5)
- **Los 21 placeholders `![DIAGRAMA: ...]` apuntan a un archivo SVG que EXISTE. 0 enlaces rotos** (verificación 1:1 automatizada placeholders↔archivos).
- Los SVG son válidos y sustanciales (5-8.5 KB cada uno, `viewBox` correcto, un único `</svg>` de cierre). Inspección de 01, 09 y 14: campo con franjas, líneas reglamentarias, convención de color (azul=propio / rojo=rival), triángulo=portero, markers de flecha diferenciados (movimiento/pase/conducción), cabecera de título, leyenda interna, etiquetas de rol y dimensiones. Coinciden fielmente con su caption y con la leyenda del README.
- `PEDIDOS.md` es un spec canónico consistente con los placeholders reales.

### Criterio 5 — Navegación y coherencia (9.0)
- Todos los enlaces internos `.md` (README→módulos/ejercicios, ejercicios→módulos, plan→fichas) **resuelven correctamente**.
- Terminología unificada en español en todo el curso (POR/LD-LI/DFC/MC[6,8]/MD-MI/DC). No quedan abreviaturas inglesas (GK/CB/ST) ni la notación "9.5" que el pipeline corrigió. Distancias de referencia estandarizadas (8-12 m entre líneas; 25-35 m de bloque) y contrapressing homogeneizado a "3-5 s".
- Recuento coherente: se anuncian "25 tareas" en README y plan, y hay exactamente las tareas T1–T25.
- Pequeñas asperezas (ver defectos): la columna "Dorsal de referencia" del README usa una numeración poco convencional (MD/MI=7/9, DC=10/11) y la T19 conserva en su título "(5 segundos)" mientras el cuerpo del curso usa "3-5 s".

### Criterio 6 — Acabado editorial (9.5)
- Redacción profesional, densa y sin relleno; formato Markdown limpio y consistente (tablas, citas de encabezado, listas, fichas homogéneas). Tono de formador UEFA. Sin secciones vacías ni rotas.

---

## 4. DEFECTOS PRIORIZADOS

No hay defectos BLOQUEANTES. No hay defectos IMPORTANTES. Todos los hallazgos son MENORES.

### MENOR-1 — Numeración de dorsales poco convencional en el README
- **Severidad:** MENOR
- **Ubicación:** `README.md`, tabla "Convención de posiciones", línea 77-78.
- **Problema:** asigna a los extremos MD/MI los dorsales **7 / 9** y a los delanteros DC los **10 / 11**. La convención futbolística estándar reserva el 9 para un delantero y suele dar 7/11 a las bandas. Un formador exigente lo notará. Internamente es coherente (la columna se titula "Dorsal de referencia" y la de rol explica el matiz), pero choca con la expectativa del lector experto.
- **Acción correctiva:** cambiar a una asignación convencional, p. ej. MD/MI = **7 / 11** y DC = **9 / 10** (o 9 / 19). Verificar que ningún otro punto del curso cite esos dorsales concretos (no se ha encontrado ninguno: el resto del curso usa siempre las abreviaturas 6/8 para los MC y nombres de rol, no dorsales de banda/punta), por lo que el cambio se limita a esas dos celdas.

### MENOR-2 — Título de la Tarea 19 conserva "(5 segundos)" frente al estándar "3-5 s"
- **Severidad:** MENOR
- **Ubicación:** `ejercicios/05-transiciones.md`, encabezado "## TAREA 19 — Contrapresión inmediata tras pérdida (5 segundos)" (línea 11) y referencias a "T19 contrapresión 5 s" en `ejercicios/00-plan-sesiones.md` (líneas 41 y 47-48).
- **Problema:** el curso fijó el contrapressing en "3-5 segundos" (módulos 02 §3.3 y 04 §2), pero la tarea-cronómetro y el plan siguen diciendo "5 s". No es un error táctico (la regla de la tarea fija deliberadamente un umbral de 5 s como provocación), pero genera una microincoherencia de cifra con la teoría.
- **Acción correctiva:** o bien (a) renombrar a "Contrapresión inmediata tras pérdida (ventana 3-5 s)" y aclarar en el desarrollo que la tarea usa 5 s como umbral concreto dentro de esa ventana; o (b) añadir una nota de una línea en la ficha aclarando que "la teoría habla de una ventana de 3-5 s; aquí se fija el umbral en 5 s". Mantener la variante de 3 s que ya existe.

### MENOR-3 — No hay tarea específica de balón parado ensayado (córner/falta)
- **Severidad:** MENOR
- **Ubicación:** carpeta `ejercicios/` (banco completo) frente a `modulos/04-transiciones-y-balon-parado.md` §3.
- **Problema:** el balón parado está bien tratado en teoría (M04 §3) y de forma implícita en práctica (centros y defensa de centros en T8/T15), pero **no existe una tarea dedicada a ensayar un córner o una falta** (ataque con bloqueos / defensa mixta). El plan de sesiones programa "ensayo de ABP" (Microciclo A, MD-1) remitiendo solo a la teoría, sin una ficha que dirigir. Ya señalado como hueco menor por el informe de validación del pipeline.
- **Acción correctiva:** derivar 1-2 fichas de ABP del M04 §3 (p. ej. "T26 — córner ofensivo con bloqueos y zonas de remate" y "T27 — defensa mixta de córner + salida de contragolpe"), con la misma plantilla. Si se añaden, actualizar el recuento "25 tareas" en `README.md` (línea 26) y `00-plan-sesiones.md` (línea 3), el "Mapa rápido tarea→bloque" del plan, y enlazarlas desde MD-1 de ambos microciclos. Opcional para un módulo de estrategia propio; no imprescindible para la filosofía "mucha práctica de campo".

### MENOR-4 — Consecuencia física como castigo en la Tarea 12
- **Severidad:** MENOR
- **Ubicación:** `ejercicios/03-pressing.md`, T12, provocación "sprint corto" como consecuencia si el rival supera la presión (líneas 64-65).
- **Problema:** usar un castigo físico (sprint) como provocación es válido como driver de intensidad, pero rompe ligeramente el tono metodológico del resto del banco, donde las consecuencias son de juego (conceder posesión/campo). Coherencia de estilo, no error.
- **Acción correctiva:** sustituir o complementar el sprint por una consecuencia de juego (p. ej. "si el rival supera la presión y llega a la mini-portería, suma 2 puntos y reinicia con superioridad"), manteniendo el sprint solo como opción. Cambio cosmético.

---

## 5. Enlaces a gráficos ROTOS

**NINGUNO.** Verificación 1:1 de los 21 placeholders contra los 21 archivos en `graficos/`:

| Placeholder en el texto | Archivo destino | Estado |
|---|---|---|
| `../graficos/01-formacion-base.svg` … `../graficos/21-tarea-zonas-puntos.svg` (los 21) | existen los 21 archivos homónimos | ✅ TODOS VIVOS |

- Placeholders referenciados en los `.md`: 21 (01→21, consecutivos, sin duplicados ni huecos).
- Archivos SVG presentes en `graficos/`: 21 (01→21).
- Coincidencia: total. Además, todos los SVG son ficheros válidos y no triviales (4.9–8.6 KB, con `viewBox` y cierre `</svg>` único).

---

## 6. Conclusión

Producto **publicable y de nivel profesional**. La cadena teoría→tarea→gráfico está completa y sin roturas; las 25 fichas tienen transferencia real al 1-4-4-2 con provocaciones bien diseñadas; los 21 diagramas existen, son coherentes y refuerzan el texto. Los cuatro defectos son menores y de pulido (un cambio de dos celdas de dorsales, una microincoherencia de cifra, un hueco opcional de ABP y un retoque de tono en una provocación). Ninguno bloquea la entrega.

**Veredicto: PRODUCTO TOP — 9.4/10.**
