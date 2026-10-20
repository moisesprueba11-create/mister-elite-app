# BRIEF — Landing de la membresía "MISTER ÉLITE · Cuerpo Técnico Digital"

## Producto
Membresía digital para **entrenadores de fútbol** (base, amateur, semiprofesional) que no tienen
cuerpo técnico: les da el "staff" que no pueden pagar. Creador: **Moisés Díaz** (marca MISTER ÉLITE).
Filosofía: **poca teoría, mucha aplicación práctica**. Todo listo para llevar al campo.

Roles del "cuerpo técnico digital" (mapeados a contenido REAL que existe hoy en este repo):
- **Analista táctico** → cursos por sistema: 1-4-3-3, 1-4-4-2, 1-5-3-2, 1-3-4-3, 1-4-2-3-1 (fase ofensiva, defensiva, transiciones, ABP).
- **Preparador físico** → curso de Pretemporada (física+táctica; 6 planes según sesiones/semana, banco de 12 sesiones, control de carga con RPE/ACWR, plantillas).
- **Segundo entrenador** → banco de tareas con pizarra: cada tarea con objetivo, organización, desarrollo, provocaciones medibles, variantes (fácil/media/difícil), coaching y duración + planes de sesiones.
- **Especialista ABP / posesión** → cursos de Posesión, Rondos, Ruedas de presión, Balón parado defensivo.

## Hechos que SÍ puedes usar (verificables en el repo)
- 10 cursos publicados (pretemporada, posesión, rondos, ruedas, bp-defensivo, 1-3-4-3, 1-4-2-3-1, 1-4-3-3, 1-4-4-2, 1-5-3-2).
- Más de 170 tareas/sesiones de campo, cada una con su pizarra (más de 400 gráficos SVG en total).
- Cada curso se entrega en 3 formatos: PDF, HTML único (offline) y sitio navegable.
- Marca "MISTER ÉLITE — Moisés Díaz" en portada y al pie de cada pizarra.
- Sin tecnología cara: control de carga con papel y RPE.
- Ejemplo real de tarea (puedes citarla/mostrarla): `curso-1433/ejercicios/01-salida.md` T1 "Rombo de salida: el pivote pivota"
  (1-4-3-3, 4v2 en 40×30 m, 4 series × 4 min, 90 s descanso; el 6 solo recibe dentro de su zona de conos;
  punto si el balón cruza la línea de medios tras pasar por 3 jugadores distintos; variantes fácil/media/difícil).
  Su pizarra: `curso-1433/graficos/tarea-01.svg` (puedes incrustarla inline en la landing).

## PROHIBIDO inventar (esto es un producto real, la landing se publicará)
- NO inventes testimonios, nombres de clientes, número de miembros, valoraciones, logos de clubes, titulaciones o trayectoria de Moisés, estadísticas ("el 87 % de..."), ni "plazas limitadas" falsas.
- Donde la persuasión necesitaría un dato que no tenemos (testimonios, credenciales, nº de miembros), NO lo inventes: coloca un bloque limpio y visible con un comentario HTML `<!-- TODO-USER: ... -->` explicando qué debe aportar Moisés, y diseña la página para que funcione bien aunque ese bloque aún no esté. Mejor sustituir prueba social por **prueba de producto** (muestra real, índice, garantía, vista previa).
- Precio, garantía y condiciones: usa los valores de la sección CONFIG de abajo, centralizados en un único objeto `const CONFIG` al inicio del `<script>` (o variables CSS/atributos data-*) para que Moisés los cambie en un único sitio.

## CONFIG (propuesta de partida, editable por el dueño)
- Precio mensual: 19 €/mes · Precio anual: 149 €/año (≈ 12,4 €/mes) · Garantía: 14 días de devolución sin preguntas.
- Enlace de compra/alta: `https://TU-WORDPRESS/membresia` (placeholder único `CONFIG.checkoutUrl`).
- Contacto: `CONFIG.contactoEmail` = `hola@TU-DOMINIO` (placeholder).

## Reglas técnicas
- **Un único archivo HTML autocontenido** (CSS y JS inline, SVG inline, sin librerías externas, sin imágenes externas; fuentes del sistema o Google Fonts permitidas solo vía <link> con fallback a system-ui). Debe funcionar abriéndolo con doble clic, sin internet.
- Responsive de verdad (móvil primero: la mayoría de entrenadores ve esto desde el móvil, sin scroll horizontal). Accesible (contraste AA, `lang="es"`, jerarquía h1/h2, foco visible, `prefers-reduced-motion`).
- Español de España, tuteo, tono de entrenador: directo, sin humo, sin jerga de marketing.
- CTA claro y repetido; cada CTA apunta a `CONFIG.checkoutUrl`. Muestra gratuita/lead magnet puede ser un `mailto:` o ancla (no hay backend).
- Peso < 400 KB. Sin dependencias.
- Pie con marca "MISTER ÉLITE — Moisés Díaz".

## Salida
Escribe tu landing en el archivo que se te indique, bajo `/home/user/mister-elite-app/landing-membresia/`.
No toques nada fuera de ese archivo. Al terminar, responde SOLO con 5 líneas: ángulo, titular, estructura de secciones, qué pusiste en TODO-USER, y peso del archivo.
