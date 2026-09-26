// Estilo «presentador + dos tarjetas» (referencia aportada por Moisés): figura central recortada,
// una tarjeta por sistema a cada lado, fondo partido en dos brillos y titular de dos partes arriba.
// Uso: NODE_PATH=$(npm root -g) node miniaturas/_build/build_estilo.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { C, css, pitchV, F433, F442 } = require('./build.js');

const OUT = path.resolve(__dirname, '..');
const CUT = 'data:image/png;base64,' + fs.readFileSync(path.resolve(__dirname, '../../inputs/cara/avatar_recorte.png')).toString('base64');
const GOLD = '#ffc53d';

// Fondo partido: izquierda (color a) y derecha (color b), con rayos y chispas.
function background(a, b) {
  const sparks = Array.from({ length: 40 }, (_, i) => {
    const x = 700 + ((i * 137) % 560), y = (i * 89) % 720, r = 1 + (i % 3);
    return `<circle cx="${x}" cy="${y}" r="${r}" fill="#fff" opacity="${0.25 + (i % 4) * 0.12}"/>`;
  }).join('');
  return `<div style="position:absolute;inset:0;background:
      radial-gradient(circle at 12% 30%, ${a.core} 0, ${a.mid} 16%, ${a.dark} 42%, transparent 60%),
      radial-gradient(circle at 88% 30%, ${b.core} 0, ${b.mid} 16%, ${b.dark} 42%, transparent 60%),
      linear-gradient(90deg, ${a.dark} 0 50%, ${b.dark} 50% 100%)"></div>
    <div style="position:absolute;inset:0;opacity:.35;background:repeating-conic-gradient(from 0deg at 12% 30%, rgba(255,255,255,.35) 0 2deg, transparent 2deg 12deg);
      -webkit-mask-image:linear-gradient(90deg,#000 0 38%,transparent 55%)"></div>
    <svg width="1280" height="720" style="position:absolute;inset:0">${sparks}</svg>
    <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 65%, transparent 40%, rgba(0,0,0,.55) 100%)"></div>`;
}

// Tarjeta tipo icono con la formación completa (11 con portero) y su número.
function card(x, y, rot, label, formation, grad, dot, dotStroke, labelColor) {
  return `<div style="position:absolute;left:${x}px;top:${y}px;width:300px;height:330px;border-radius:46px;transform:rotate(${rot}deg);
      background:${grad};border:5px solid rgba(255,255,255,.85);box-shadow:0 24px 50px rgba(0,0,0,.7), inset 0 2px 0 rgba(255,255,255,.4)">
    <svg width="300" height="330" style="position:absolute;inset:0">${pitchV(70, 22, 160, 222, formation, dot, dotStroke)}</svg>
    <div class="t" style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:54px;color:${labelColor};-webkit-text-stroke:6px #050a07">${label}</div>
  </div>`;
}

function page({ a, b, t1, t2, t2color, size = 92 }) {
  return `<style>${css}</style>
  ${background(a, b)}
  <img src="${CUT}" style="position:absolute;left:325px;top:150px;width:630px;
       filter:drop-shadow(0 0 3px rgba(255,255,255,.8)) drop-shadow(0 20px 40px rgba(0,0,0,.75))">
  ${card(60, 330, -9, '1-4-3-3', F433, 'linear-gradient(160deg,#2b2b2b,#0b0b0b)', '#fff', '#0a0a0a', '#fff')}
  ${card(920, 330, 9, '1-4-4-2', F442, `linear-gradient(160deg,#1fd466,#0a6b31)`, '#0b2a17', '#fff', '#fff')}
  <div class="t" style="position:absolute;left:0;right:0;top:22px;text-align:center;font-size:${size}px;white-space:nowrap;-webkit-text-stroke:10px #050a07">
    ${t1} <span style="color:${t2color}">${t2}</span></div>`;
}

const VARIANTS = [
  // 01 · Dorado (luz de estadio) vs verde de marca
  { file: 'miniatura_estilo_01.png', a: { core: '#fff3c4', mid: '#ffb347', dark: '#3a1d05' }, b: { core: '#c9ffe0', mid: '#18c25a', dark: '#03210f' },
    t1: '2 SISTEMAS.', t2: '1 ELECCIÓN.', t2color: GOLD },
  // 02 · Naranja fuego vs verde (lo más parecido a la referencia)
  { file: 'miniatura_estilo_02.png', a: { core: '#ffe08a', mid: '#ff6a1a', dark: '#3b0d02' }, b: { core: '#b8ffd6', mid: '#12a84d', dark: '#021a0c' },
    t1: '2 SISTEMAS.', t2: '¿CUÁL ELIGES?', t2color: GOLD, size: 80 },
  // 03 · Blanco frío vs verde (paleta de marca pura)
  { file: 'miniatura_estilo_03.png', a: { core: '#ffffff', mid: '#8fa3b8', dark: '#0b1118' }, b: { core: '#d6ffe8', mid: '#18c25a', dark: '#021a0c' },
    t1: '¿1-4-3-3', t2: 'O 1-4-4-2?', t2color: C.green },
];

(async () => {
  const b = await chromium.launch();
  const shot = async (html, file, w, h) => {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.setContent('<!doctype html><meta charset="utf-8"><body style="position:relative;overflow:hidden">' + html);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(OUT, file) });
    await p.close();
  };
  for (const v of VARIANTS) await shot(page(v), v.file, 1280, 720);
  const img = f => 'data:image/png;base64,' + fs.readFileSync(path.join(OUT, f)).toString('base64');
  await shot(`<style>*{margin:0}body{background:#0f0f0f;padding:20px;display:flex;gap:20px;font-family:Arial;color:#ccc;font-size:13px}
    img{width:320px;height:180px;display:block;border-radius:8px}</style>
    ${VARIANTS.map((v, i) => `<div><img src="${img(v.file)}"><p style="margin-top:6px">Estilo ${i + 1} · 320×180</p></div>`).join('')}`,
    'prueba_estilo_320x180.png', 1060, 240);
  await b.close();
  console.log('ok');
})();
