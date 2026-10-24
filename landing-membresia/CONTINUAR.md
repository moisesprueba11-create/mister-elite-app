# Cómo seguir este proyecto (landing de la membresía MISTER ÉLITE)

## Estado
- `landing-membresia.html` — landing CORTA (la que recomendamos publicar como principal). Enlaza con anclas a la completa.
- `landing-b-sesion.html` — landing COMPLETA (muestras, sesión imprimible, índices, condiciones, perfiles).
- `landing-a-staff.html`, `landing-c-metodo.html` — las otras dos propuestas de la ronda 0 (no ganaron).
- Las dos landings comparten el mismo objeto `const CONFIG` (precios, condiciones, club, bio, testimonios…). Si cambias un dato, cámbialo en las dos.
- Ambas deben quedar en la MISMA carpeta (enlaces relativos).

## Pendiente (solo lo puede aportar Moisés) — ver `_pipeline/PENDIENTE-DEL-DUENO.md`
1. Testimonios reales con permiso → `CONFIG.testimonios` · 2. Foto/titulación/trayectoria → `CONFIG.bio` · 3. `numeroMiembros` solo si es cierto
4. `checkoutUrl` y `contactoEmail` reales · 5. `legalUrls` · 6. Confirmar condiciones propuestas y qué significa "hasta 10 equipos" del plan club (55 €/mes)
7. Probar el sitio de Moisés (misterelite.es) para leer testimonios: el entorno de la nube lo bloqueaba (red); en el PC se pueden leer directamente.

## Siguiente paso previsto
Con testimonios y bio puestos: nueva ronda con los 9 evaluadores (`_pipeline/PERFILES.md`, instrucciones en `_pipeline/EVAL_CORTA.md` y `_pipeline/EVAL_LOOP.md`), capturas con `node _pipeline/shots.js <html> <prefijo>` + `python3 _pipeline/slice.py <png>`.
Resultados anteriores: `_pipeline/RONDA0-RESULTADO.md`, `RONDA1-RESULTADO.md`, `RONDA2-RESULTADO.md`, `RESULTADO-CORTA.md`.

## Reglas del proyecto
Nada inventado (testimonios, titulaciones, cifras de miembros). Nombres de archivo estables, sin sufijos de versión (ver CLAUDE.md en la raíz).
