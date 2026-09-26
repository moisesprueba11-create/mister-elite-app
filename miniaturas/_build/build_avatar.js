// Variantes del concepto 1 (El duelo táctico) con Moisés Díaz recortado (sin el fondo de la foto).
// Recorte: inputs/cara/avatar_recorte.png (rembg, modelo birefnet-portrait, a partir de inputs/cara/avatar.png).
// No se altera el rostro: solo se recorta el fondo y se añade luz de contorno.
// Uso: NODE_PATH=$(npm root -g) node miniaturas/_build/build_avatar.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { C, css, pitchV, grass, F433, F442 } = require('./build.js');

const OUT = path.resolve(__dirname, '..');
const CUT = 'data:image/png;base64,' + fs.readFileSync(path.resolve(__dirname, '../../inputs/cara/avatar_recorte.png')).toString('base64');

const base = `${css}
  .num{position:absolute;font-size:104px}
  .vs{position:absolute;border-radius:50%;background:${C.green};border:7px solid #fff;display:flex;align-items:center;
      justify-content:center;box-shadow:0 10px 40px rgba(0,0,0,.7)}
  .q{position:absolute;text-align:center;-webkit-text-stroke:9px #050a07}
  .me{position:absolute;filter:drop-shadow(0 0 2px rgba(255,255,255,.9)) drop-shadow(0 0 26px rgba(24,194,90,.75)) drop-shadow(0 24px 30px rgba(0,0,0,.7))}
  .strip{position:absolute;background:rgba(5,10,7,.88);border-radius:24px}`;

const bg = id => `<svg width="1280" height="720" style="position:absolute;inset:0">
  ${grass(id)}<rect width="1280" height="720" fill="url(#${id})"/>
  <rect x="0" width="640" height="720" fill="rgba(255,255,255,.04)"/><rect x="640" width="640" height="720" fill="rgba(0,0,0,.25)"/>
  <rect width="1280" height="720" fill="url(#${id}v)"/></svg>`;

const board = (id, x, y, w, h) => `<svg width="1280" height="720" style="position:absolute;inset:0"><defs>
  <radialGradient id="${id}" cx="50%" cy="45%" r="85%"><stop offset="0" stop-color="#1c6e3c"/><stop offset=".55" stop-color="#0a2a16"/><stop offset="1" stop-color="#020503"/></radialGradient></defs>
  <rect width="1280" height="720" fill="url(#${id})"/>
  <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="18" fill="#0c3b1f" stroke="#141414" stroke-width="14"/></svg>`;

// ---------- A · Moisés en el centro, entre los dos sistemas ----------
function optA() {
  return `<style>${base}</style>
  ${bg('ga')}
  <svg width="1280" height="720" style="position:absolute;inset:0">
    ${pitchV(50, 150, 280, 420, F433, C.white, '#0a0a0a')}
    ${pitchV(950, 150, 280, 420, F442, C.green, '#062b14')}
  </svg>
  <img class="me" src="${CUT}" style="left:385px;top:215px;width:510px">
  <div class="t num" style="left:30px;top:30px">1-4-3-3</div>
  <div class="t num" style="right:30px;top:30px;color:${C.green}">1-4-4-2</div>
  <div class="t vs" style="left:582px;top:66px;width:116px;height:116px;font-size:52px">VS</div>
  <div class="strip" style="left:250px;right:250px;bottom:14px;height:126px"></div>
  <div class="t q" style="left:0;right:0;bottom:30px;font-size:98px">¿CUÁL ELIGES?</div>`;
}

// ---------- B · Presentador a la izquierda, pizarra con los dos sistemas a la derecha ----------
function optB() {
  return `<style>${base}.num{font-size:66px}</style>
  ${board('bgB', 560, 120, 690, 440)}
  <svg width="1280" height="720" style="position:absolute;inset:0">
    ${pitchV(610, 185, 230, 345, F433, C.white, '#0a0a0a')}
    ${pitchV(970, 185, 230, 345, F442, C.green, '#062b14')}
  </svg>
  <img class="me" src="${CUT}" style="left:-40px;top:95px;width:620px">
  <div class="t num" style="left:600px;top:30px">1-4-3-3</div>
  <div class="t num" style="left:960px;top:30px;color:${C.green}">1-4-4-2</div>
  <div class="t vs" style="left:855px;top:300px;width:100px;height:100px;font-size:44px">VS</div>
  <div class="t q" style="left:520px;right:10px;bottom:24px;font-size:96px">¿CUÁL ELIGES?</div>`;
}

// ---------- C · Primer plano a la derecha, pizarra a la izquierda y pregunta arriba ----------
function optC() {
  return `<style>${base}.num{font-size:58px}</style>
  ${board('bgC', 30, 175, 640, 420)}
  <svg width="1280" height="720" style="position:absolute;inset:0">
    ${pitchV(75, 250, 220, 330, F433, C.white, '#0a0a0a')}
    ${pitchV(405, 250, 220, 330, F442, C.green, '#062b14')}
  </svg>
  <img class="me" src="${CUT}" style="left:655px;top:150px;width:680px">
  <div class="t num" style="left:80px;top:190px">1-4-3-3</div>
  <div class="t num" style="left:405px;top:190px;color:${C.green}">1-4-4-2</div>
  <div class="t vs" style="left:302px;top:370px;width:96px;height:96px;font-size:42px">VS</div>
  <div class="t q" style="left:20px;top:26px;font-size:112px;text-align:left">¿CUÁL ELIGES?</div>`;
}

(async () => {
  const b = await chromium.launch();
  const shot = async (html, file, w, h) => {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.setContent('<!doctype html><meta charset="utf-8"><body style="position:relative;overflow:hidden">' + html);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(OUT, file) });
    await p.close();
  };
  const files = [['miniatura_avatar_01.png', optA], ['miniatura_avatar_02.png', optB], ['miniatura_avatar_03.png', optC]];
  for (const [f, fn] of files) await shot(fn(), f, 1280, 720);
  const img = f => 'data:image/png;base64,' + fs.readFileSync(path.join(OUT, f)).toString('base64');
  await shot(`<style>*{margin:0}body{background:#0f0f0f;padding:20px;display:flex;gap:20px;font-family:Arial;color:#ccc;font-size:13px}
    img{width:320px;height:180px;display:block;border-radius:8px}</style>
    ${files.map(([f], i) => `<div><img src="${img(f)}"><p style="margin-top:6px">Avatar ${i + 1} · 320×180</p></div>`).join('')}`,
    'prueba_avatar_320x180.png', 1060, 240);
  await b.close();
  console.log('ok');
})();
