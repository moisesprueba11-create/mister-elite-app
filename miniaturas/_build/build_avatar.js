// Variantes del concepto 1 (El duelo táctico) con el avatar de Moisés Díaz (inputs/cara/avatar.png).
// El avatar se usa tal cual (solo recorte y fundido de bordes); no se altera el rostro.
// Uso: NODE_PATH=$(npm root -g) node miniaturas/_build/build_avatar.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { C, css, pitchV, grass, F433, F442 } = require('./build.js');

const OUT = path.resolve(__dirname, '..');
const AVATAR = 'data:image/png;base64,' + fs.readFileSync(path.resolve(__dirname, '../../inputs/cara/avatar.png')).toString('base64');

const base = `${css}
  .num{position:absolute;font-size:104px}
  .vs{position:absolute;border-radius:50%;background:${C.green};border:7px solid #fff;display:flex;align-items:center;
      justify-content:center;box-shadow:0 10px 40px rgba(0,0,0,.7)}
  .q{position:absolute;text-align:center;-webkit-text-stroke:9px #050a07}`;

const bg = (id, extra = '') => `<svg width="1280" height="720" xmlns="http://www.w3.org/2000/svg" style="position:absolute;inset:0">
  ${grass(id)}<rect width="1280" height="720" fill="url(#${id})"/>${extra}<rect width="1280" height="720" fill="url(#${id}v)"/></svg>`;

// ---------- A · Avatar en el centro, en medallón ----------
function optA() {
  return `<style>${base}
    .av{position:absolute;left:470px;top:190px;width:340px;height:340px;border-radius:50%;padding:8px;
        background:linear-gradient(160deg,#fff,${C.green});box-shadow:0 14px 50px rgba(0,0,0,.8)}
    .av img{width:100%;height:100%;border-radius:50%;object-fit:cover;transform:scale(1.07)}
    .av div{width:100%;height:100%;border-radius:50%;overflow:hidden;background:#0b0f14}
  </style>
  ${bg('ga', '<rect x="0" width="640" height="720" fill="rgba(255,255,255,.04)"/><rect x="640" width="640" height="720" fill="rgba(0,0,0,.25)"/>')}
  <svg width="1280" height="720" style="position:absolute;inset:0">
    ${pitchV(70, 150, 280, 420, F433, C.white, '#0a0a0a')}
    ${pitchV(930, 150, 280, 420, F442, C.green, '#062b14')}
  </svg>
  <div class="t num" style="left:40px;top:30px">1-4-3-3</div>
  <div class="t num" style="right:40px;top:30px;color:${C.green}">1-4-4-2</div>
  <div class="av"><div><img src="${AVATAR}"></div></div>
  <div class="t vs" style="left:580px;top:118px;width:120px;height:120px;font-size:54px">VS</div>
  <div class="t q" style="left:0;right:0;bottom:30px;font-size:98px">¿CUÁL ELIGES?</div>`;
}

// ---------- B · Avatar a la izquierda, formaciones en pizarra a la derecha ----------
function optB() {
  return `<style>${base}
    .av{position:absolute;left:-150px;top:70px;width:760px;height:760px;
        -webkit-mask-image:radial-gradient(circle at 380px 390px,#000 230px,transparent 340px);mask-image:radial-gradient(circle at 380px 390px,#000 230px,transparent 340px)}
    .av img{width:100%;height:100%;object-fit:cover}
    .num{font-size:66px}
  </style>
  <svg width="1280" height="720" style="position:absolute;inset:0"><defs>
    <radialGradient id="bgB" cx="30%" cy="45%" r="85%"><stop offset="0" stop-color="#1c6e3c"/><stop offset=".55" stop-color="#0a2a16"/><stop offset="1" stop-color="#020503"/></radialGradient></defs>
    <rect width="1280" height="720" fill="url(#bgB)"/>
    <rect x="560" y="120" width="690" height="440" rx="18" fill="#0c3b1f" stroke="#141414" stroke-width="14"/>
    ${pitchV(610, 185, 230, 345, F433, C.white, '#0a0a0a')}
    ${pitchV(970, 185, 230, 345, F442, C.green, '#062b14')}
  </svg>
  <div class="av"><img src="${AVATAR}"></div>
  <div class="t num" style="left:600px;top:30px">1-4-3-3</div>
  <div class="t num" style="left:960px;top:30px;color:${C.green}">1-4-4-2</div>
  <div class="t vs" style="left:855px;top:300px;width:100px;height:100px;font-size:44px">VS</div>
  <div class="t q" style="left:520px;right:10px;bottom:24px;font-size:96px">¿CUÁL ELIGES?</div>`;
}

// ---------- C · Avatar emergiendo en el centro entre los dos sistemas ----------
function optC() {
  return `<style>${base}
    .av{position:absolute;left:370px;top:150px;width:540px;height:540px;
        -webkit-mask-image:radial-gradient(circle at 270px 280px,#000 165px,transparent 240px);mask-image:radial-gradient(circle at 270px 280px,#000 165px,transparent 240px)}
    .av img{width:100%;height:100%;object-fit:cover}
    .strip{position:absolute;left:250px;right:250px;bottom:14px;height:126px;background:rgba(5,10,7,.86);border-radius:24px}
  </style>
  ${bg('gc', '<rect x="0" width="640" height="720" fill="rgba(255,255,255,.04)"/><rect x="640" width="640" height="720" fill="rgba(0,0,0,.25)"/>')}
  <svg width="1280" height="720" style="position:absolute;inset:0">
    ${pitchV(60, 150, 280, 420, F433, C.white, '#0a0a0a')}
    ${pitchV(940, 150, 280, 420, F442, C.green, '#062b14')}
  </svg>
  <div class="av"><img src="${AVATAR}"></div>
  <div class="t num" style="left:40px;top:30px">1-4-3-3</div>
  <div class="t num" style="right:40px;top:30px;color:${C.green}">1-4-4-2</div>
  <div class="t vs" style="left:582px;top:40px;width:116px;height:116px;font-size:52px">VS</div>
  <div class="strip"></div>
  <div class="t q" style="left:0;right:0;bottom:30px;font-size:98px">¿CUÁL ELIGES?</div>`;
}

(async () => {
  const b = await chromium.launch();
  const shot = async (html, file, w, h) => {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.setContent('<!doctype html><meta charset="utf-8"><body style="position:relative">' + html);
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
