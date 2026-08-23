'use strict';

const test = require('node:test');
const assert = require('node:assert');
const { evaluar } = require('../nombres-estables.js');

// Los cursos reales del repo, inyectados para que los tests no dependan del disco.
const CURSOS = new Set([
  '1343', '14231', '1433', '1442', '1532',
  'bp-defensivo', 'posesion', 'pretemporada', 'rondos', 'ruedas',
]);

const escritura = (file_path, extra = {}) =>
  evaluar({ tool_name: 'Write', tool_input: { file_path, ...extra } }, CURSOS);
const edicion = (file_path, new_string) =>
  evaluar({ tool_name: 'Edit', tool_input: { file_path, new_string } }, CURSOS);
const bash = (command) => evaluar({ tool_name: 'Bash', tool_input: { command } }, CURSOS);

// ─── 1. Rutas de entregables ────────────────────────────────────────────────

test('deja pasar los nombres canonicos', () => {
  assert.equal(escritura('/repo/curso-1433/curso-1433-completo.html'), null);
  assert.equal(escritura('/repo/curso-1433/curso-1433.pdf'), null);
  assert.equal(escritura('curso-bp-defensivo/curso-bp-defensivo-completo.html'), null);
});

test('bloquea sufijos de version en el HTML unico', () => {
  for (const malo of [
    'curso-1433-completo-v2.html',
    'curso-1433-completo-final.html',
    'curso-1433-completo-mejorado.html',
    'curso-1433-completo-2026-08-23.html',
    'curso-1433-completo (1).html'.replace(' (1)', '-copia'),
  ]) {
    const r = escritura(`/repo/curso-1433/${malo}`);
    assert.ok(r, `deberia bloquear ${malo}`);
    assert.equal(r.id, 'ruta-no-canonica');
    assert.ok(r.esperado.includes('curso-1433-completo.html'));
  }
});

test('bloquea sufijos de version en el PDF', () => {
  const r = escritura('/repo/curso-posesion/curso-posesion-v3.pdf');
  assert.ok(r);
  assert.equal(r.id, 'ruta-no-canonica');
});

test('bloquea un entregable con nombre inventado', () => {
  assert.ok(escritura('/repo/curso-1433/curso-completo.html'));
  assert.ok(escritura('/repo/curso-1433/curso-1433-completo.pdf')); // .pdf no lleva -completo
});

// ─── 2. Falsos positivos que el repo ya contiene ────────────────────────────

test('no toca ficheros legitimos con -FINAL o -def en el nombre', () => {
  assert.equal(escritura('/repo/curso-1442/_pipeline/evaluacion/VEREDICTO-FINAL.md'), null);
  assert.equal(escritura('/repo/curso-1343/graficos/teoria-04-transicion-def.svg'), null);
  assert.equal(escritura('/repo/curso-1532/graficos/_gen_tareas_01_13.py'), null);
});

test('no toca el sitio navegable ni ficheros que no son entregables', () => {
  assert.equal(escritura('/repo/curso-1433/site/index.html'), null);
  assert.equal(escritura('/repo/curso-1433/site/modulos/m1.html'), null);
  assert.equal(escritura('/repo/curso-1433/README.md'), null);
  assert.equal(escritura('/repo/index.html'), null);
});

test('no toca carpetas que no son cursos', () => {
  assert.equal(escritura('/repo/video-curso-1433/algo-v2.html'), null);
  assert.equal(escritura('/repo/video-pruebas/prueba-final.pdf'), null);
});

// ─── 3. Contenido de los build scripts ──────────────────────────────────────

test('bloquea un build script que cambia el nombre de salida', () => {
  const r = edicion(
    '/repo/curso-1433/build_onefile.py',
    'out = os.path.join(ROOT, "curso-1433-completo-v2.html")'
  );
  assert.ok(r);
  assert.equal(r.id, 'salida-no-canonica');
});

test('deja pasar el build script real', () => {
  assert.equal(
    edicion('/repo/curso-1433/build_pdf.py', 'out = os.path.join(ROOT, "curso-1433.pdf")'),
    null
  );
  assert.equal(
    edicion('/repo/curso-1433/build_onefile.py', 'out = os.path.join(ROOT, "curso-1433-completo.html")'),
    null
  );
});

test('revisa todas las ediciones de un MultiEdit', () => {
  const r = evaluar({
    tool_name: 'MultiEdit',
    tool_input: {
      file_path: '/repo/curso-rondos/build_pdf.py',
      edits: [
        { new_string: 'import os' },
        { new_string: 'out = "curso-rondos-final.pdf"' },
      ],
    },
  }, CURSOS);
  assert.ok(r);
  assert.equal(r.id, 'salida-no-canonica');
});

// ─── 4. Bash ────────────────────────────────────────────────────────────────

test('bloquea copias con nombre nuevo', () => {
  assert.ok(bash('cp curso-1433/curso-1433.pdf curso-1433/curso-1433-v2.pdf'));
  assert.ok(bash('mv curso-posesion/curso-posesion-completo.html curso-posesion/curso-posesion-completo-old.html'));
  assert.ok(bash('python3 build_onefile.py > curso-1532/curso-1532-completo-nuevo.html'));
});

test('deja pasar los comandos de build normales', () => {
  assert.equal(bash('cd curso-1433 && python3 build_pdf.py'), null);
  assert.equal(bash('ls -la curso-1433/curso-1433.pdf'), null);
  assert.equal(bash('git add curso-1433/curso-1433-completo.html curso-1433/curso-1433.pdf'), null);
  assert.equal(bash('open curso-ruedas/curso-ruedas.pdf'), null);
});

test('el nombre canonico suelto, sin carpeta, tambien pasa', () => {
  assert.equal(bash('cp curso-1433.pdf /tmp/'), null);
});

// ─── 5. Robustez ────────────────────────────────────────────────────────────

test('ignora herramientas y entradas irrelevantes', () => {
  assert.equal(evaluar({ tool_name: 'Read', tool_input: { file_path: 'curso-1433/curso-1433-v2.pdf' } }, CURSOS), null);
  assert.equal(evaluar({ tool_name: 'Write', tool_input: null }, CURSOS), null);
  assert.equal(evaluar({ tool_name: 'Bash', tool_input: {} }, CURSOS), null);
});

// ─── 6. La variante que se disfrazaba de curso propio (regresion) ───────────

test('un nombre-variante suelto no pasa por ser "canonico de otro curso"', () => {
  // curso-rondos-final.pdf parece el PDF canonico de un curso "rondos-final".
  // Como "rondos" SI existe, es una variante y debe bloquearse.
  assert.ok(bash('cp curso-rondos.pdf curso-rondos-final.pdf'));
  assert.ok(bash('mv curso-1433.pdf curso-1433-v2.pdf'));
  assert.ok(
    edicion('/repo/curso-rondos/build_pdf.py', 'out = "curso-rondos-final.pdf"')
  );
});

test('un curso nuevo, aun sin carpeta, no se bloquea', () => {
  assert.equal(bash('cp /tmp/x.pdf curso-1352.pdf'), null);
  assert.equal(escritura('/repo/curso-1352/curso-1352-completo.html'), null);
});

test('un build script puede mencionar el entregable de otro curso existente', () => {
  assert.equal(
    edicion('/repo/curso-1433/build_pdf.py', 'REFERENCIA = "curso-posesion.pdf"'),
    null
  );
});

// ─── 7. Documentacion que menciona el nombre prohibido (regresion) ──────────
// Este hook se bloqueo a si mismo al escribir su propio README con un heredoc
// que contenia un ejemplo de nombre malo. El texto de un heredoc es texto, no
// una operacion sobre ficheros.

test('un heredoc que documenta un nombre prohibido no se bloquea', () => {
  assert.equal(
    bash([
      "cat > .claude/hooks/README.md <<'EOF'",
      'Ejemplo de lo que NO hay que hacer:',
      '  cp curso-1433.pdf curso-1433-v2.pdf',
      'EOF',
    ].join('\n')),
    null
  );
});

test('pero el comando real, fuera del heredoc, sigue bloqueado', () => {
  assert.ok(bash([
    "cat > notas.md <<'EOF'",
    'texto inocuo',
    'EOF',
    'cp curso-1433/curso-1433.pdf curso-1433/curso-1433-v2.pdf',
  ].join('\n')));
});
