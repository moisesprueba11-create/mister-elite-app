// Composición gráfica de las miniaturas (sin IA generativa: Higgsfield no disponible en el entorno).
// Uso: NODE_PATH=$(npm root -g) node miniaturas/_build/build.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT = path.resolve(__dirname, '..');
const FONT = 'data:font/woff2;base64,' + fs.readFileSync(path.join(__dirname, 'nunito900.woff2')).toString('base64');

const C = { black: '#07110b', green: '#18c25a', greenDark: '#0b5d2c', white: '#ffffff' };

const css = `
@font-face{font-family:'Nunito';font-weight:900;src:url(${FONT}) format('woff2');}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1280px;height:720px;overflow:hidden;background:${C.black}}
.t{font-family:'Nunito',sans-serif;font-weight:900;color:#fff;
   paint-order:stroke fill;-webkit-text-stroke:7px #050a07;letter-spacing:-1px;line-height:.95}
.brand{position:absolute;font-family:'Nunito',sans-serif;font-weight:900;font-size:22px;letter-spacing:2px;color:#fff;opacity:.9}
.brand b{color:${C.green}}
`;

// Formaciones en coordenadas de campo vertical 100 x 150 (ataca hacia arriba). 11 jugadores con portero.
const F433 = [[50, 142], [14, 118], [37, 122], [63, 122], [86, 118], [50, 97], [27, 84], [73, 84], [18, 52], [50, 44], [82, 52]];
const F442 = [[50, 142], [14, 118], [37, 122], [63, 122], [86, 118], [13, 86], [38, 90], [62, 90], [87, 86], [37, 52], [63, 52]];

function pitchV(x, y, w, h, formation, fill, stroke) {
  const sx = w / 100, sy = h / 150;
  const P = (px, py) => [x + px * sx, y + py * sy];
  const lines = `
    <rect x="${x}" y="${y}" width="${w}" height="${h}" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="3"/>
    <line x1="${x}" y1="${y + h / 2}" x2="${x + w}" y2="${y + h / 2}" stroke="rgba(255,255,255,.55)" stroke-width="3"/>
    <circle cx="${x + w / 2}" cy="${y + h / 2}" r="${13 * sx}" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="3"/>
    <rect x="${x + 22 * sx}" y="${y + h - 24 * sy}" width="${56 * sx}" height="${24 * sy}" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="3"/>
    <rect x="${x + 22 * sx}" y="${y}" width="${56 * sx}" height="${24 * sy}" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="3"/>`;
  const dots = formation.map(([px, py]) => {
    const [cx, cy] = P(px, py);
    return `<circle cx="${cx}" cy="${cy + 3}" r="${6.2 * sx}" fill="rgba(0,0,0,.45)"/>
            <circle cx="${cx}" cy="${cy}" r="${6.2 * sx}" fill="${fill}" stroke="${stroke}" stroke-width="4"/>`;
  }).join('');
  return lines + dots;
}

function grass(id) {
  return `<defs>
    <pattern id="${id}" width="80" height="720" patternUnits="userSpaceOnUse">
      <rect width="40" height="720" fill="#0f5a2b"/><rect x="40" width="40" height="720" fill="#0d5226"/>
    </pattern>
    <radialGradient id="${id}v" cx="50%" cy="45%" r="75%">
      <stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".78"/>
    </radialGradient></defs>`;
}

// ---------- Concepto 1 · El duelo táctico ----------
function concept1() {
  const svg = `<svg width="1280" height="720" xmlns="http://www.w3.org/2000/svg">
    ${grass('g1')}
    <rect width="1280" height="720" fill="url(#g1)"/>
    <rect width="640" height="720" fill="rgba(255,255,255,.05)"/>
    <rect x="640" width="640" height="720" fill="rgba(0,0,0,.28)"/>
    <rect width="1280" height="720" fill="url(#g1v)"/>
    ${pitchV(125, 150, 300, 420, F433, C.white, '#0a0a0a')}
    ${pitchV(855, 150, 300, 420, F442, C.green, '#062b14')}
    <polygon points="610,0 670,0 670,720 610,720" fill="${C.black}" opacity=".9"/>
  </svg>`;
  return `<style>${css}
    .num{position:absolute;top:36px;font-size:112px}
    .vs{position:absolute;left:560px;top:300px;width:160px;height:160px;border-radius:50%;background:${C.green};
        border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:72px;box-shadow:0 10px 40px rgba(0,0,0,.7)}
    .q{position:absolute;left:0;right:0;bottom:30px;text-align:center;font-size:98px;-webkit-text-stroke:9px #050a07}
    .strip{position:absolute;left:250px;right:250px;bottom:14px;height:126px;background:rgba(5,10,7,.82);border-radius:24px}
  </style>${svg}
  <div class="t num" style="left:70px">1-4-3-3</div>
  <div class="t num" style="right:70px;color:${C.green}">1-4-4-2</div>
  <div class="t vs">VS</div>
  <div class="strip"></div>
  <div class="t q">¿CUÁL ELIGES?</div>
  <div class="brand" style="left:24px;bottom:16px">MISTER <b>ÉLITE</b></div>`;
}

// ---------- Concepto 2 · La elección del entrenador ----------
function concept2() {
  // Pizarra con dos mitades de campo (formaciones completas) y un entrenador de espaldas en silueta, sin rostro.
  const board = `
    <rect x="360" y="30" width="880" height="440" rx="18" fill="#0c3b1f" stroke="#1b1b1b" stroke-width="18"/>
    <rect x="378" y="48" width="844" height="404" rx="6" fill="url(#chalk)"/>
    ${pitchV(470, 130, 200, 300, F433, C.white, '#0a0a0a')}
    ${pitchV(930, 130, 200, 300, F442, C.green, '#062b14')}`;
  const coach = `
    <g fill="#030604">
      <circle cx="235" cy="350" r="78"/>
      <rect x="200" y="410" width="70" height="60" rx="22"/>
      <path d="M20 720 C25 540 95 468 235 458 C375 468 445 540 450 720 Z"/>
    </g>`;
  const svg = `<svg width="1280" height="720" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <radialGradient id="bg2" cx="65%" cy="35%" r="80%"><stop offset="0" stop-color="#1f7a43"/><stop offset=".55" stop-color="#0a2a16"/><stop offset="1" stop-color="#020503"/></radialGradient>
      <linearGradient id="chalk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#14532b"/><stop offset="1" stop-color="#0b3a1d"/></linearGradient>
      <radialGradient id="rim" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#6dffa8" stop-opacity=".35"/><stop offset="1" stop-color="#6dffa8" stop-opacity="0"/></radialGradient>
    </defs>
    <rect width="1280" height="720" fill="url(#bg2)"/>
    ${board}
    <ellipse cx="235" cy="480" rx="280" ry="280" fill="url(#rim)"/>
    ${coach}
  </svg>`;
  return `<style>${css}
    .lab{position:absolute;top:58px;font-size:62px}
    .o{position:absolute;left:745px;top:200px;font-size:110px;color:${C.green}}
    .q{position:absolute;left:440px;right:20px;bottom:22px;text-align:center;font-size:84px;-webkit-text-stroke:9px #050a07}
  </style>${svg}
  <div class="t lab" style="left:465px">1-4-3-3</div>
  <div class="t lab" style="left:925px;color:${C.green}">1-4-4-2</div>
  <div class="t o">¿?</div>
  <div class="t q">¿CUÁL TE CONVIENE?</div>
  <div class="brand" style="right:24px;top:18px">MISTER <b>ÉLITE</b></div>`;
}

// ---------- Concepto 3 · La batalla del centro ----------
function concept3() {
  // Detalle parcial: franja central de un campo horizontal. Mediocampo del 1-4-3-3 (3) frente al doble pivote del 1-4-4-2 (2).
  const white3 = [[560, 250], [470, 370], [560, 490]];      // interior, pivote, interior (1-4-3-3)
  const green2 = [[720, 300], [720, 440]];                   // doble pivote (1-4-4-2)
  const dot = (x, y, f, s) => `<circle cx="${x}" cy="${y + 5}" r="34" fill="rgba(0,0,0,.5)"/><circle cx="${x}" cy="${y}" r="34" fill="${f}" stroke="${s}" stroke-width="7"/>`;
  const faded = [[250, 150], [250, 590], [300, 370], [1010, 150], [1010, 590], [960, 300], [960, 440]]
    .map(([x, y], i) => `<circle cx="${x}" cy="${y}" r="24" fill="${i < 3 ? '#fff' : C.green}" opacity=".22"/>`).join('');
  const svg = `<svg width="1280" height="720" xmlns="http://www.w3.org/2000/svg">
    ${grass('g3')}
    <rect width="1280" height="720" fill="url(#g3)"/>
    <line x1="640" y1="0" x2="640" y2="720" stroke="rgba(255,255,255,.6)" stroke-width="5"/>
    <circle cx="640" cy="370" r="120" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="5"/>
    <rect width="1280" height="720" fill="url(#g3v)"/>
    <rect x="0" y="0" width="1280" height="720" fill="rgba(0,0,0,.45)"/>
    ${faded}
    <rect x="410" y="185" width="380" height="370" rx="30" fill="rgba(24,194,90,.20)" stroke="${C.green}" stroke-width="8"/>
    ${white3.map(([x, y]) => dot(x, y, '#fff', '#0a0a0a')).join('')}
    ${green2.map(([x, y]) => dot(x, y, C.green, '#062b14')).join('')}
    <path d="M1170 200 C1150 330 1000 380 850 380" fill="none" stroke="#050a07" stroke-width="30" stroke-linecap="round"/>
    <path d="M1170 200 C1150 330 1000 380 850 380" fill="none" stroke="#fff" stroke-width="18" stroke-linecap="round"/>
    <polygon points="806,380 862,342 862,418" fill="#fff" stroke="#050a07" stroke-width="6" stroke-linejoin="round"/>
  </svg>`;
  return `<style>${css}
    .top{position:absolute;left:0;right:0;top:26px;text-align:center;font-size:70px}
    .k{position:absolute;left:0;right:0;bottom:34px;text-align:center;font-size:96px;-webkit-text-stroke:9px #050a07}
    .n{position:absolute;font-size:60px}
  </style>${svg}
  <div class="t top">1-4-3-3 <span style="color:${C.green}">vs 1-4-4-2</span></div>
  <div class="t n" style="left:430px;top:196px">3</div>
  <div class="t n" style="left:745px;top:196px;color:${C.green}">2</div>
  <div class="t k">LA CLAVE ESTÁ AQUÍ</div>
  <div class="brand" style="left:24px;top:24px;font-size:18px">MISTER <b>ÉLITE</b></div>`;
}

function gridPage(files) {
  const img = f => 'data:image/png;base64,' + fs.readFileSync(path.join(OUT, f)).toString('base64');
  // Orden mezclado: las propuestas no ocupan posiciones destacadas; la clave va en archivo aparte.
  const order = ['P', 'miniatura_02.png', 'P', 'P', 'miniatura_03.png', 'P', 'miniatura_01.png', 'P', 'P'];
  const cells = order.map((f, i) => {
    const th = f === 'P'
      ? `<div class="ph"><span>Referencia investigada<br>no disponible</span></div>`
      : `<img src="${img(f)}">`;
    const title = f === 'P' ? 'Hueco reservado para miniatura de la competencia' : '1-4-3-3 vs 1-4-4-2: ¿qué sistema le conviene a tu equipo?';
    const ch = f === 'P' ? '—' : 'Mister Élite';
    return `<div class="card"><div class="th">${th}</div><div class="meta"><div class="av"></div><div><div class="ti">${title}</div><div class="ch">${ch}</div></div></div><div class="pos">${i + 1}</div></div>`;
  }).join('');
  return `<style>*{margin:0;box-sizing:border-box}body{background:#0f0f0f;width:1280px;padding:28px;font-family:'Liberation Sans',Arial,sans-serif}
    .g{display:grid;grid-template-columns:repeat(3,1fr);gap:26px 18px}
    .card{position:relative}.th{aspect-ratio:16/9;border-radius:12px;overflow:hidden;background:#222}
    .th img{width:100%;height:100%;display:block}
    .ph{width:100%;height:100%;display:flex;align-items:center;justify-content:center;text-align:center;color:#777;font-size:17px;
        background:repeating-linear-gradient(45deg,#1d1d1d 0 14px,#232323 14px 28px)}
    .meta{display:flex;gap:10px;margin-top:10px}.av{width:34px;height:34px;border-radius:50%;background:#333;flex:none}
    .ti{color:#f1f1f1;font-size:15px;font-weight:bold;line-height:1.3}.ch{color:#aaa;font-size:13px;margin-top:4px}
    .pos{position:absolute;top:6px;left:6px;background:rgba(0,0,0,.75);color:#ddd;font-size:12px;padding:2px 7px;border-radius:4px}
  </style><div class="g">${cells}</div>`;
}

function smallPage() {
  const img = f => 'data:image/png;base64,' + fs.readFileSync(path.join(OUT, f)).toString('base64');
  const fs3 = ['miniatura_01.png', 'miniatura_02.png', 'miniatura_03.png'];
  return `<style>*{margin:0}body{background:#0f0f0f;padding:20px;display:flex;gap:20px;font-family:Arial;color:#ccc;font-size:13px}
  img{width:320px;height:180px;display:block;border-radius:8px}</style>
  ${fs3.map((f, i) => `<div><img src="${img(f)}"><p style="margin-top:6px">Propuesta ${i + 1} · 320×180</p></div>`).join('')}`;
}

(async () => {
  const b = await chromium.launch();
  const shot = async (html, file, w, h, full) => {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.setContent('<!doctype html><meta charset="utf-8">' + html);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(OUT, file), fullPage: !!full });
    await p.close();
  };
  await shot(concept1(), 'miniatura_01.png', 1280, 720);
  await shot(concept2(), 'miniatura_02.png', 1280, 720);
  await shot(concept3(), 'miniatura_03.png', 1280, 720);
  await shot(gridPage(), 'grilla.png', 1280, 900, true);
  await shot(smallPage(), 'prueba_320x180.png', 1060, 240, true);
  await b.close();
  console.log('ok');
})();
