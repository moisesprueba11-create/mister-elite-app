# Inteligencia de contenido (Instagram)

Flujo de dos agentes (definidos en `.claude/agents/`):

1. **investigador-instagram** → encuentra cuentas extranjeras que venden cursos/herramientas para entrenadores de fútbol, las perfila y analiza cada pieza y su objetivo.
   Salidas: `cuentas/<handle>.md` y `analisis/informe-general.md`.
2. **guionista-contenido** → con ese análisis genera guiones/piezas para MISTER ÉLITE en `guiones/`.

Uso: "usa el agente investigador-instagram para buscar 12 cuentas…" y luego "usa el agente guionista-contenido con el curso 1-4-3-3".
Nota: Instagram limita el acceso automático; si no se ven las piezas, pega enlaces/capturas y el agente las analiza.
