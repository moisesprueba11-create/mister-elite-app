#!/usr/bin/env node
/**
 * nombres-estables — PreToolUse hook para MISTER ELITE
 *
 * Hace cumplir la convencion de nombres de CLAUDE.md: los entregables de cada
 * curso conservan SIEMPRE el mismo nombre. Nunca se anaden sufijos de version
 * (-v2, -final, -mejorado, fechas...), porque el usuario sube el archivo a su
 * plataforma y la nueva version debe REEMPLAZAR a la anterior. Si el nombre
 * cambia, le quedan copias dobladas y no sabe cual es la buena.
 *
 * Nombres canonicos por curso:
 *   curso-<slug>/curso-<slug>-completo.html
 *   curso-<slug>/curso-<slug>.pdf
 *
 * Tres comprobaciones (deniegan antes de que la herramienta se ejecute):
 *   1. RUTA      Write/Edit sobre un .html o .pdf en la raiz de curso-<slug>/
 *                cuyo nombre no es el canonico.
 *   2. CONTENIDO Write/Edit de un build_*.py que escribe una salida con nombre
 *                no canonico (el vector real: los entregables los genera
 *                Python, no la herramienta Write).
 *   3. BASH      Comando que menciona un nombre de entregable no canonico
 *                (cp/mv/redirecciones/python build_*.py).
 *
 * Alcance deliberadamente estrecho: solo ficheros .html/.pdf cuyo nombre
 * empieza por "curso-". Asi VEREDICTO-FINAL.md, teoria-04-transicion-def.svg
 * y todo lo de site/, graficos/ y _pipeline/ quedan fuera por construccion.
 *
 * Escape de emergencia: MISTER_ELITE_PERMITIR_RENOMBRAR=true (por si alguna vez
 * hace falta renombrar un curso de verdad).
 */

'use strict';

const fs = require('fs');
const path = require('path');

const HERRAMIENTAS_ESCRITURA = new Set(['Write', 'Edit', 'NotebookEdit', 'MultiEdit']);

// Un "nombre con forma de entregable": empieza por curso- y acaba en .html/.pdf
const FORMA_ENTREGABLE = /^curso-[A-Za-z0-9._-]+\.(html|pdf)$/;

// El mismo patron, para pescar rutas o nombres sueltos dentro de un comando bash.
const ENTREGABLE_EN_TEXTO = /(?:[A-Za-z0-9._\/-]*\/)?(curso-[A-Za-z0-9._-]+\.(?:html|pdf))/g;

const permitirRenombrar = () => process.env.MISTER_ELITE_PERMITIR_RENOMBRAR === 'true';

/** Nombres canonicos que admite un curso dado. */
function canonicos(slug) {
  return [`curso-${slug}-completo.html`, `curso-${slug}.pdf`];
}

/**
 * Extrae el slug del curso de una ruta, si el fichero cuelga DIRECTAMENTE de
 * curso-<slug>/. Devuelve null para site/, graficos/, _pipeline/, etc.
 */
function slugDeRutaRaiz(rutaFichero) {
  const partes = rutaFichero.split(path.sep).filter(Boolean);
  if (partes.length < 2) return null;
  const dir = partes[partes.length - 2];
  const m = /^curso-(.+)$/.exec(dir);
  return m ? m[1] : null;
}

/** Slug que un nombre de entregable implica: curso-1433.pdf -> "1433". */
function slugImplicito(basename) {
  const conCompleto = /^curso-(.+)-completo\.html$/.exec(basename);
  if (conCompleto) return conCompleto[1];
  const conPdf = /^curso-(.+)\.pdf$/.exec(basename);
  return conPdf ? conPdf[1] : null;
}

/**
 * Cursos que existen de verdad en disco. Sin este anclaje, "curso-rondos-final.pdf"
 * se leeria como el PDF canonico de un curso llamado "rondos-final" y el hook
 * se saltaria a si mismo.
 */
let cacheSlugs = null;
function slugsConocidos(baseDir) {
  if (cacheSlugs) return cacheSlugs;
  cacheSlugs = new Set();
  try {
    for (const e of fs.readdirSync(baseDir || process.cwd(), { withFileTypes: true })) {
      const m = e.isDirectory() && /^curso-(.+)$/.exec(e.name);
      if (m) cacheSlugs.add(m[1]);
    }
  } catch (e) { /* sin acceso al disco, el set queda vacio y todo se valida por ruta */ }
  return cacheSlugs;
}

/**
 * Un nombre suelto es aceptable si es el entregable canonico de algun curso
 * existente. "curso-rondos-final.pdf" no lo es: su slug implicito ("rondos-final")
 * es una VARIANTE de un curso conocido ("rondos"), justo lo que perseguimos.
 * Un slug del todo desconocido se acepta: es un curso nuevo aun sin carpeta.
 */
function nombreAceptableSuelto(basename, slugs) {
  const slug = slugImplicito(basename);
  if (!slug) return false;
  if (slugs.has(slug)) return canonicos(slug).includes(basename);
  for (const conocido of slugs) {
    if (slug.startsWith(conocido)) return false; // variante de un curso existente
  }
  return true; // curso nuevo: aun no tiene carpeta
}

/** COMPROBACION 1: la ruta escrita. */
function revisarRuta(rutaFichero) {
  if (!rutaFichero) return null;
  const basename = path.basename(rutaFichero);
  if (!FORMA_ENTREGABLE.test(basename)) return null;

  const slug = slugDeRutaRaiz(rutaFichero);
  if (!slug) return null; // no cuelga de curso-<slug>/: fuera de alcance

  const validos = canonicos(slug);
  if (validos.includes(basename)) return null;

  return {
    id: 'ruta-no-canonica',
    motivo: `"${basename}" no es un nombre de entregable valido para curso-${slug}/.`,
    esperado: validos,
  };
}

/**
 * COMPROBACION 2: el contenido de un build script.
 * Busca literales con forma de entregable y los valida contra el curso al que
 * pertenece el propio script.
 */
function revisarContenido(rutaFichero, contenido, slugs) {
  if (!rutaFichero || !contenido) return null;
  if (path.extname(rutaFichero) !== '.py') return null;

  const slug = slugDeRutaRaiz(rutaFichero);
  if (!slug) return null;

  const validos = canonicos(slug);
  for (const m of contenido.matchAll(ENTREGABLE_EN_TEXTO)) {
    const basename = m[1];
    if (validos.includes(basename)) continue;
    // Un script puede mencionar legitimamente el entregable de OTRO curso.
    if (nombreAceptableSuelto(basename, slugs)) continue;

    return {
      id: 'salida-no-canonica',
      motivo: `${path.basename(rutaFichero)} escribiria "${basename}", que no es el entregable canonico de curso-${slug}/.`,
      esperado: validos,
    };
  }
  return null;
}

/**
 * El cuerpo de un heredoc es texto, no una operacion de ficheros: un
 * `cat > README.md <<EOF` que DOCUMENTA un nombre prohibido no lo esta creando.
 * Se recorta antes de analizar para no bloquear la propia documentacion.
 */
function sinHeredocs(comando) {
  return comando.replace(
    /<<-?\s*(['"]?)([A-Za-z_][A-Za-z0-9_]*)\1\r?\n[\s\S]*?\r?\n\s*\2\b/g,
    '<<HEREDOC'
  );
}

/** COMPROBACION 3: el comando bash. */
function revisarBash(comando, slugs) {
  if (!comando) return null;
  comando = sinHeredocs(comando);

  for (const m of comando.matchAll(ENTREGABLE_EN_TEXTO)) {
    const rutaCompleta = m[0];
    const basename = m[1];

    // Si la ruta lleva su curso-<slug>/ delante, validamos contra ese curso.
    const slugPorRuta = slugDeRutaRaiz(rutaCompleta);
    if (slugPorRuta) {
      if (canonicos(slugPorRuta).includes(basename)) continue;
      return {
        id: 'bash-nombre-no-canonico',
        motivo: `El comando escribe o mueve "${basename}" dentro de curso-${slugPorRuta}/.`,
        esperado: canonicos(slugPorRuta),
      };
    }

    // Nombre suelto, sin directorio delante.
    if (nombreAceptableSuelto(basename, slugs)) continue;

    return {
      id: 'bash-nombre-no-canonico',
      motivo: `El comando menciona "${basename}", que no sigue la convencion de nombres de los entregables.`,
      esperado: null,
    };
  }
  return null;
}

function evaluar(evento, slugsInyectados) {
  const { tool_name: herramienta, tool_input: entrada } = evento;
  if (!entrada) return null;

  const slugs = slugsInyectados || slugsConocidos(evento.cwd);

  if (herramienta === 'Bash') return revisarBash(entrada.command, slugs);

  if (HERRAMIENTAS_ESCRITURA.has(herramienta)) {
    const ruta = entrada.file_path || entrada.notebook_path;
    const porRuta = revisarRuta(ruta);
    if (porRuta) return porRuta;

    // El texto que quedaria escrito: Write manda content, Edit manda new_string,
    // MultiEdit manda una lista de ediciones.
    const trozos = [entrada.content, entrada.new_string, entrada.new_source];
    if (Array.isArray(entrada.edits)) {
      for (const e of entrada.edits) trozos.push(e && e.new_string);
    }
    return revisarContenido(ruta, trozos.filter(Boolean).join('\n'), slugs);
  }

  return null;
}

function mensaje(hallazgo) {
  const lineas = [
    `[${hallazgo.id}] ${hallazgo.motivo}`,
    '',
    'CLAUDE.md: los entregables conservan SIEMPRE el mismo nombre. El build',
    'sobrescribe el archivo; nunca se anaden sufijos de version. Si el nombre',
    'cambia, al subirlo a la plataforma quedan copias dobladas.',
  ];
  if (hallazgo.esperado) {
    lineas.push('', `Nombres validos: ${hallazgo.esperado.join('  |  ')}`);
  }
  return lineas.join('\n');
}

async function main() {
  let entrada = '';
  for await (const trozo of process.stdin) entrada += trozo;

  try {
    if (permitirRenombrar()) return console.log('{}');

    const hallazgo = evaluar(JSON.parse(entrada));
    if (!hallazgo) return console.log('{}');

    console.log(JSON.stringify({
      hookSpecificOutput: {
        hookEventName: 'PreToolUse',
        permissionDecision: 'deny',
        permissionDecisionReason: mensaje(hallazgo),
      },
    }));
  } catch (e) {
    // Ante la duda, no estorbar: un hook roto nunca debe bloquear el trabajo.
    console.log('{}');
  }
}

if (require.main === module) {
  main();
} else {
  module.exports = { evaluar, revisarRuta, revisarContenido, revisarBash, canonicos, nombreAceptableSuelto, sinHeredocs };
}
