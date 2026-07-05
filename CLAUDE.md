# MISTER ÉLITE — Notas del proyecto

Colección de cursos de fútbol generados con la metodología multi-agente y la marca
**MISTER ÉLITE**. Cada curso vive en su carpeta `curso-<nombre>/` y se
entrega en tres formatos: HTML único autocontenido, sitio navegable (`site/`) y PDF.

## Marca (IMPORTANTE)

**El nombre personal del usuario NUNCA debe aparecer** en ningún entregable (portadas,
pies de pizarra/infografía, reels, HTML, PDF, sitio, etc.). La única marca visible es
**MISTER ÉLITE** (sin nombre propio detrás). Si algún archivo o plantilla existente todavía
incluye el nombre personal, quítalo al tocar ese archivo.

## Convención de nombres de archivo (IMPORTANTE)

**Al corregir o actualizar un curso, los archivos entregables conservan SIEMPRE el mismo
nombre que la versión anterior.** El build sobrescribe el archivo; nunca se añaden sufijos
de versión (`-v2`, `-final`, `-mejorado`, fechas, etc.).

Motivo: el usuario sube el archivo a su plataforma y la nueva versión **reemplaza** a la
anterior (se "subscribe"). Si el nombre cambia, le quedan **copias dobladas** y no sabe
cuál es la buena.

Nombres fijos por curso (no cambiar):
- `curso-<nombre>/curso-<nombre>-completo.html` — HTML único autocontenido.
- `curso-<nombre>/curso-<nombre>.pdf` — PDF.
- `curso-<nombre>/site/` — sitio navegable.

Esto aplica a TODOS los cursos (actuales y futuros): pretemporada, posesión, rondos,
1-4-4-2, 1-5-3-2, 1-3-4-3, 1-4-2-3-1, 1-4-3-3, etc.

## Publicación en WordPress (flujo actual)

**Este entorno de código NO tiene WordPress conectado** (sus MCP son Canva, Gmail, Google Drive,
Make, Notion, GitHub). El MCP de WordPress vive en el Claude del chat del usuario.

Flujo elegido: al terminar de crear o actualizar un curso →
1. **Build + validación TOP** aquí.
2. **Entregar** los archivos: `SendUserFile` del PDF y el HTML único + `git commit`/`push` a la rama.
3. **El usuario publica desde su Claude del chat** (que sí tiene el MCP de WordPress), que sube el
   PDF y el HTML único y reemplaza la versión anterior (nombres estables → sin copias dobladas).

Opcional / futuro: si algún día se conecta WordPress a ESTE entorno (su MCP o credenciales REST
`WP_URL`/`WP_USER`/`WP_APP_PASSWORD`), la skill `subir-wordpress` ya está lista para automatizar la
subida desde aquí (`python3 .claude/skills/subir-wordpress/upload.py <slug>`).

## Estándar de calidad

- Bucle de mejora hasta que el evaluador considere el curso "TOP" (≥ 8,5/10).
- Techo realista de contenido: ~9,0–9,5. No perseguir el 10 (depende de validación en campo,
  no del archivo).
- Filosofía: poca teoría, mucha aplicación práctica. Marca **MISTER ÉLITE** (sin nombre
  personal) en portada y al pie de cada pizarra/infografía.
