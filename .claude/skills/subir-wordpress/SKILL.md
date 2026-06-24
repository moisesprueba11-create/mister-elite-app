---
name: subir-wordpress
description: >
  Sube los entregables de un curso MISTER ÉLITE (PDF y HTML único) al WordPress de Moisés Díaz
  por la REST API, reemplazando la versión anterior (sin duplicar). Se ejecuta automáticamente
  al terminar de crear o actualizar CUALQUIER curso del proyecto. Úsala cuando un curso ya está
  construido y validado (TOP) y hay que publicarlo/actualizarlo en la web.
---

# Subir curso a WordPress (MISTER ÉLITE)

## Cuándo se activa
**Automáticamente al final de crear o actualizar un curso** (todos los cursos del proyecto son
de MISTER ÉLITE). Tras el build y la validación TOP, se ejecuta este paso para publicar/actualizar.

## Qué hace
1. Localiza `curso-<slug>/curso-<slug>.pdf` y `curso-<slug>/curso-<slug>-completo.html`.
2. Los sube a la Biblioteca de Medios de WordPress por la REST API.
3. Si el curso tiene un post/página/producto destino configurado (`post_id`), actualiza su
   enlace a la nueva versión y **publica** (publicación automática).
4. Borra la versión anterior de Medios para no acumular copias dobladas.
5. Guarda los IDs en `cursos.json` (commiteable; sin secretos).

## Cómo ejecutarla
```
python3 .claude/skills/subir-wordpress/upload.py <slug>
python3 .claude/skills/subir-wordpress/upload.py <slug> --dry-run   # solo comprueba
```

## Configuración necesaria (una sola vez)
**Credenciales — NUNCA en el repo.** Configúralas como secretos/variables de entorno del entorno:
- `WP_URL` — p. ej. `https://misterelite.com` (sin barra final)
- `WP_USER` — usuario de WordPress
- `WP_APP_PASSWORD` — *Contraseña de aplicación* (WordPress › Usuarios › Perfil › Contraseñas de
  aplicación › crear una nueva). No es la contraseña normal de la cuenta.
- `WP_PUBLISH` (opcional) — `auto` (por defecto, publica) o `draft` (deja en borrador).

**Destino por curso (en `cursos.json`).** Para que cada curso reemplace SIEMPRE el mismo sitio
de la web, se guarda por slug: `post_id` (la página/entrada/producto del curso) y los IDs de
medios. El primer `post_id` se rellena una vez (cuando sepamos en qué página vive cada curso).

Si faltan credenciales, el script avisa y NO sube nada (no rompe el flujo del curso).

## Notas
- El entorno remoto debe poder alcanzar el sitio (política de red). Si está bloqueado, ejecutar
  donde haya acceso o enrutar vía Make.com.
- Mantiene la convención del proyecto: nombres de archivo estables → la versión nueva reemplaza
  a la anterior, sin copias dobladas.
