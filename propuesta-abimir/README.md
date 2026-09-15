# Propuesta comercial — Abimir by DHC (Design Home Canarias, S.L.)

Estudio de empresa y propuesta de soluciones de IA para la tienda de cocinas y mobiliario
a medida **Abimir** (C/ Don Pedro Infinito, 111 — Las Palmas de Gran Canaria).

| Archivo | Para qué sirve | Para quién |
|---|---|---|
| `propuesta-abimir-completo.html` | Propuesta comercial completa (HTML autocontenido, imprimible) | **El cliente** |
| `propuesta-abimir.pdf` | La misma propuesta en PDF, 14 páginas A4 — esto es lo que se imprime y se deja en la tienda | **El cliente** |
| `dossier-abimir.md` | Estudio interno: datos verificados, fugas detectadas, competencia, checklist previo a la visita | **Uso interno** |
| `guion-visita.md` | Guion de la visita: entrada, 3 preguntas, objeciones y cierre | **Uso interno** |

> Los dos archivos internos **no** se entregan al cliente.

## Regenerar el PDF tras editar el HTML

```bash
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox \
  --no-pdf-header-footer --print-to-pdf=propuesta-abimir.pdf --virtual-time-budget=6000 \
  file://$PWD/propuesta-abimir-completo.html
```

Los nombres de archivo son **fijos**: al actualizar, se sobrescriben (sin sufijos de versión).

## Antes de entregarlo

- [ ] Rellenar teléfono/WhatsApp y correo en la portada y en el apartado 09.
- [ ] Verificar los 5 puntos del checklist del §7 del dossier (reseñas reales, posición en Google, última publicación).
- [ ] Ajustar precios si procede tras la reunión de arranque.
