# Hooks del proyecto

Hooks propios de MISTER ÉLITE. Se registran en `.claude/settings.json`, están
versionados en el repo y por tanto funcionan en cualquier sesión y en cualquier
máquina, sin instalar nada.

## `nombres-estables.js`

Convierte la regla más importante de `CLAUDE.md` —los entregables conservan
SIEMPRE el mismo nombre— en algo que el harness **ejecuta**, no que el modelo
recuerda. Si el nombre cambia, al subir el archivo a la plataforma quedan copias
dobladas y no se sabe cuál es la buena.

Nombres canónicos por curso:

| Entregable | Nombre |
|---|---|
| HTML único | `curso-<slug>/curso-<slug>-completo.html` |
| PDF | `curso-<slug>/curso-<slug>.pdf` |

### Qué vigila

Tres comprobaciones, en `PreToolUse` (deniegan **antes** de que la herramienta
se ejecute):

1. **Ruta** — `Write`/`Edit` sobre un `.html` o `.pdf` en la raíz de
   `curso-<slug>/` con nombre no canónico.
2. **Contenido** — `Write`/`Edit` de un `build_*.py` que escribiría una salida
   con nombre no canónico. Es el vector real: los entregables los genera Python
   (`out = os.path.join(ROOT, "curso-1433.pdf")`), no la herramienta `Write`.
3. **Bash** — comandos que copian, mueven o redirigen hacia un nombre no
   canónico.

### Qué NO toca

El alcance es deliberadamente estrecho: sólo ficheros `.html`/`.pdf` cuyo nombre
empieza por `curso-`. Por construcción quedan fuera `VEREDICTO-FINAL.md`,
`teoria-04-transicion-def.svg`, `_gen_tareas_01_13.py`, todo `site/`,
`graficos/` y `_pipeline/`, y las carpetas `video-*`.

Un curso **nuevo**, cuya carpeta aún no existe, tampoco se bloquea. Sí se
bloquea una *variante* de un curso existente (un `-final.pdf` cuando ya hay un
curso con ese slug).

El cuerpo de un heredoc se ignora: documentar un nombre prohibido dentro de un
`cat > fichero.md <<EOF` no es crearlo. (El hook se bloqueó a sí mismo al
escribir este README; de ahí la regla y sus dos tests.)

### Escape de emergencia

Si alguna vez hay que renombrar un curso de verdad:

```
MISTER_ELITE_PERMITIR_RENOMBRAR=true
```

### Tests

```
node --test .claude/hooks/tests/
```

19 tests, sin dependencias. Además se validó con un barrido sobre los 1.362
ficheros versionados del repo y el contenido real de los 99 scripts `.py`:
**0 falsos positivos**. Coste por llamada: ~55 ms de mediana, dominado por el
arranque de Node, no por la lógica.

### Origen

El patrón (hook = un script Node sin dependencias que lee el evento por stdin y
responde `permissionDecision` por stdout, con la lógica exportada como módulo
para poder testearla) está tomado de
[karanb192/claude-code-hooks](https://github.com/karanb192/claude-code-hooks).
Se estudió ese marketplace y se descartó instalarlo entero: sus 20 hooks apuntan
a bases de código con tests y CI, no a un repo de contenido como éste.
