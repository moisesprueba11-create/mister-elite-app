#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_html.py — Genera el HTML único autocontenido con la animación
(SVG + JS, sin dependencias externas) a partir de la MISMA coreografía
que usa el MP4. MISTER ÉLITE — Moisés Díaz.

    python3 build_html.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from jugadas_1343 import (ZONE_X, LANE_Y, STOP_ZONE, MINI_GOALS, PITCH_RATIO,
                          BLUE_START, RED_START, LINEAS_SISTEMA, JUGADAS, REGLAS)

DATA = dict(
    zoneX=ZONE_X, laneY=LANE_Y, stop=STOP_ZONE, goals=MINI_GOALS, ratio=PITCH_RATIO,
    blue=BLUE_START, red=RED_START,
    lineas=[dict(labels=l, txt=t) for l, t in LINEAS_SISTEMA],
    reglas=REGLAS,
    jugadas=[dict(num=j["num"], titulo=j["titulo"], dur=j["dur"],
                  moves=j.get("moves", {}), rmoves=j.get("rmoves", {}),
                  ball=j["ball"]) for j in JUGADAS],
    gain={"r11": [0.10, 0.34], "r9": [0.10, 0.34], "r7": [0.10, 0.34],
          "r10": [0.07, 0.26], "r6": [0.07, 0.26], "r8": [0.07, 0.26],
          "r4": [0.04, 0.18], "r5": [0.04, 0.18]},
    ballOff=-3.2,
)

HTML = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Salida de balón en 1-3-4-3 · STOP BALL — MISTER ÉLITE</title>
<style>
  :root{
    --bg:#0e1622; --panel:#15202b; --panel2:#1b2a3a; --gold:#ffc83c;
    --text:#ffffff; --dim:#96acc2; --own:#1a4c9e; --rival:#ce2828;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--text);
       font-family:"Segoe UI",system-ui,-apple-system,Arial,sans-serif}
  .wrap{max-width:1080px;margin:0 auto;padding:0 0 28px}
  header{background:var(--panel);border-bottom:4px solid var(--gold);
         padding:16px 22px;display:flex;justify-content:space-between;align-items:flex-end;gap:12px}
  header h1{margin:0;font-size:clamp(18px,3.4vw,32px);letter-spacing:.3px}
  header .sub{color:var(--gold);font-weight:700;font-size:clamp(11px,1.7vw,16px);margin-top:4px}
  header .brand{text-align:right;line-height:1.25;flex:0 0 auto}
  header .brand b{font-size:clamp(12px,1.7vw,16px)}
  header .brand span{color:var(--dim);font-size:clamp(10px,1.4vw,14px)}
  .board{padding:0 14px}
  svg{width:100%;height:auto;display:block}
  .cap{background:var(--panel2);border-radius:14px;margin:12px 14px 0;padding:14px 18px 16px}
  .cap .row{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
  .chip{background:var(--gold);color:#141a24;font-weight:800;font-size:13px;
        padding:5px 14px;border-radius:20px;white-space:nowrap}
  .cap h2{margin:0;font-size:clamp(12px,1.8vw,16px);letter-spacing:.3px;text-transform:uppercase}
  .cap p{margin:12px 0 0;font-size:clamp(15px,2.3vw,21px);font-weight:700;line-height:1.35;min-height:2.7em}
  .cap .chain{margin-top:10px;color:var(--dim);font-size:clamp(11px,1.6vw,14px);
              letter-spacing:.4px;min-height:1.2em}
  .ctrl{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:14px 14px 0}
  button{background:var(--panel2);color:var(--text);border:1px solid #2c3f55;
         border-radius:10px;padding:9px 14px;font-weight:700;font-size:14px;cursor:pointer}
  button:hover{background:#25384d}
  button.on{background:var(--gold);color:#141a24;border-color:var(--gold)}
  .bar{flex:1 1 180px;height:8px;background:#22303f;border-radius:6px;overflow:hidden;min-width:120px}
  .bar i{display:block;height:100%;background:var(--gold);width:0}
  footer{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;
         background:var(--panel);margin-top:16px;padding:12px 22px;font-size:13px}
  footer .d{color:var(--dim)}
  .legend{display:flex;gap:16px;flex-wrap:wrap;margin:12px 14px 0;color:var(--dim);font-size:13px}
  .legend b{color:var(--text)}
  .dot{display:inline-block;width:12px;height:12px;border-radius:50%;vertical-align:-1px;margin-right:5px}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div>
      <h1>SALIDA DE BALÓN EN 1-3-4-3</h1>
      <div class="sub">JUEGO DE POSICIÓN POR ZONAS · 10 vs 8 · OBJETIVO: STOP BALL</div>
    </div>
    <div class="brand"><b>MISTER ÉLITE</b><br><span>Moisés Díaz</span></div>
  </header>

  <div class="board"><svg id="svg" xmlns="http://www.w3.org/2000/svg"></svg></div>

  <div class="cap">
    <div class="row"><span class="chip" id="chip">LA TAREA</span><h2 id="titulo"></h2></div>
    <p id="texto"></p>
    <div class="chain" id="chain"></div>
  </div>

  <div class="ctrl">
    <button id="play">⏸ Pausa</button>
    <button id="reset">↺ Reiniciar</button>
    <button class="seg" data-seg="0">La tarea</button>
    <button class="seg" data-seg="1">Jugada 1</button>
    <button class="seg" data-seg="2">Jugada 2</button>
    <button id="spd">1x</button>
    <div class="bar"><i id="barfill"></i></div>
  </div>

  <div class="legend">
    <span><i class="dot" style="background:#1a4c9e"></i><b>AZUL</b> · 1-3-4-3 sin portero (10)</span>
    <span><i class="dot" style="background:#ce2828"></i><b>ROJO</b> · bloque 3-3-2 (8)</span>
    <span><i class="dot" style="background:#22c55e"></i><b>STOP BALL</b> · parar el balón en la zona verde</span>
    <span><i class="dot" style="background:#ffd54a"></i>pase &nbsp;·&nbsp; <i class="dot" style="background:#7ee0ff"></i>conducción</span>
  </div>

  <footer>
    <span><b>MISTER ÉLITE — Moisés Díaz</b></span>
    <span class="d">◄ ataque azul (STOP BALL) &nbsp;·&nbsp; contra roja a las minipoterías ►</span>
  </footer>
</div>

<script>
const D = __DATA__;
const R = D.ratio, SVG="http://www.w3.org/2000/svg";
const X = x => x, Y = y => y / R;
const svg = document.getElementById("svg");
svg.setAttribute("viewBox", `-15 -5 121 ${100/R + 7}`);

function el(n, a, parent){const e=document.createElementNS(SVG,n);
  for(const k in a) e.setAttribute(k,a[k]); (parent||svg).appendChild(e); return e;}

/* ---------------------------------------------------------------- fondo --- */
const defs = el("defs",{});
const pat = el("pattern",{id:"hatch",width:3.2,height:3.2,patternTransform:"rotate(45)",
  patternUnits:"userSpaceOnUse"},defs);
el("rect",{width:3.2,height:3.2,fill:"#24964a"},pat);
el("rect",{width:1.5,height:3.2,fill:"#22c55e"},pat);
const gnet = el("pattern",{id:"net",width:1.1,height:1.1,patternUnits:"userSpaceOnUse"},defs);
el("rect",{width:1.1,height:1.1,fill:"#93a893"},gnet);
el("path",{d:"M0 0H1.1M0 0V1.1",stroke:"#e8f0e8","stroke-width":.22},gnet);

const gBack = el("g",{}), gLines = el("g",{}), gPlay = el("g",{});
for(let i=0;i<10;i++)
  el("rect",{x:i*10,y:0,width:10.02,height:Y(100),fill:i%2?"#357a39":"#3a843e"},gBack);
/* zona STOP BALL */
el("rect",{x:D.stop.x0,y:Y(D.stop.y0),width:(D.stop.x1-D.stop.x0),
  height:Y(D.stop.y1)-Y(D.stop.y0),fill:"url(#hatch)",stroke:"#d2ffdc","stroke-width":.28},gBack);
el("text",{x:(D.stop.x0+D.stop.x1)/2,y:Y((D.stop.y0+D.stop.y1)/2),fill:"#fff",
  "font-size":3.4,"font-weight":800,"text-anchor":"middle","dominant-baseline":"central",
  transform:`rotate(-90 ${(D.stop.x0+D.stop.x1)/2} ${Y((D.stop.y0+D.stop.y1)/2)})`},gBack)
  .textContent="STOP BALL";
/* minipoterías */
D.goals.forEach(([cy,hh])=>{
  el("rect",{x:100,y:Y(cy-hh/2),width:3,height:Y(cy+hh/2)-Y(cy-hh/2),fill:"url(#net)",
    stroke:"#eef2f6","stroke-width":.28},gBack);
});
/* líneas de zona y carriles */
D.zoneX.forEach(zx=>el("line",{x1:zx,y1:0,x2:zx,y2:Y(100),stroke:"#fff","stroke-width":.3,
  "stroke-dasharray":"1.6 1.2"},gLines));
D.laneY.forEach(ly=>el("line",{x1:0,y1:Y(ly),x2:100,y2:Y(ly),stroke:"#12233a","stroke-width":.34,
  "stroke-dasharray":"1.8 1.3"},gLines));
el("rect",{x:0,y:0,width:100,height:Y(100),fill:"none",stroke:"#132c48","stroke-width":.5},gLines);
[0,...D.zoneX,100].forEach(zx=>D.laneY.forEach(ly=>
  el("circle",{cx:zx,cy:Y(ly),r:.6,fill:"#d62828"},gLines)));
[[0,0],[100,0],[0,100],[100,100]].forEach(([cx,cy])=>
  el("circle",{cx:cx,cy:Y(cy),r:.9,fill:"#ec5c24"},gLines));

/* rótulos de zona sobre el campo */
const zw=[0,...D.zoneX,100];
for(let i=0;i<zw.length-1;i++)
  el("text",{x:(zw[i]+zw[i+1])/2,y:-1.7,fill:"#96acc2","font-size":1.75,"font-weight":700,
    "text-anchor":"middle","font-family":"Segoe UI,Arial,sans-serif","letter-spacing":.12},
    gLines).textContent="ZONA "+(5-i);
el("text",{x:(D.stop.x0+D.stop.x1)/2,y:-1.7,fill:"#22c55e","font-size":2.1,"font-weight":800,
  "text-anchor":"middle"},gLines).textContent="◄";

/* --------------------------------------------------------------- motor --- */
const ss = t => {t=Math.max(0,Math.min(1,t)); return t*t*(3-2*t);};
function kf(k,t){
  if(t<=k[0][0]) return [k[0][1],k[0][2]];
  if(t>=k[k.length-1][0]) return [k[k.length-1][1],k[k.length-1][2]];
  for(let i=0;i<k.length-1;i++){
    const [t0,x0,y0]=k[i],[t1,x1,y1]=k[i+1];
    if(t0<=t&&t<=t1){const u=t1>t0?ss((t-t0)/(t1-t0)):1;
      return [x0+(x1-x0)*u, y0+(y1-y0)*u];}
  }
  return [k[k.length-1][1],k[k.length-1][2]];
}
function posOf(J,lb,t){
  if(lb[0]==="r") return J.rmoves[lb]? kf(J.rmoves[lb],t) : D.red[lb].slice();
  return J.moves[lb]? kf(J.moves[lb],t) : D.blue[lb].slice();
}
function redPos(J,lb,t,b){
  if(J.rmoves[lb]) return kf(J.rmoves[lb],t);
  const [kx,ky]=D.gain[lb], p=D.red[lb];
  return [p[0]+Math.max(-7,Math.min(7,kx*(b[0]-50))),
          p[1]+Math.max(-14,Math.min(14,ky*(b[1]-50)))];
}
function ballAt(J,t){
  let ev=J.ball[0];
  for(const e of J.ball){ if(t>=e.t0) ev=e; if(e.t0<=t&&t<=e.t1){ev=e;break;} }
  if(ev.k==="hold"||ev.k==="conduce"){
    const p=posOf(J,ev.who,Math.min(t,ev.t1));
    return [p[0]+D.ballOff,p[1],ev.who,ev];
  }
  if(ev.k==="pase"){
    const a=posOf(J,ev.a,ev.t0), b=posOf(J,ev.b,ev.t1);
    const u=ss((Math.min(t,ev.t1)-ev.t0)/Math.max(.001,ev.t1-ev.t0));
    return [a[0]+D.ballOff+(b[0]-a[0])*u, a[1]+(b[1]-a[1])*u, u>=1?ev.b:null, ev];
  }
  if(ev.k==="tiro"){
    const a=posOf(J,ev.a,ev.t0);
    const u=ss((Math.min(t,ev.t1)-ev.t0)/Math.max(.001,ev.t1-ev.t0));
    return [a[0]+D.ballOff+(ev.xy[0]-a[0]-D.ballOff)*u, a[1]+(ev.xy[1]-a[1])*u, null, ev];
  }
  return [50,50,null,ev];
}
function trailsAt(J,t,n=4){
  const out=[];
  for(const e of J.ball){
    if(t<e.t0) continue;
    if(e.k==="conduce"){out.push([posOf(J,e.who,e.t0),posOf(J,e.who,Math.min(t,e.t1)),
      "conduce",t<=e.t1]); continue;}
    if(e.k!=="pase"&&e.k!=="tiro") continue;
    let p0=posOf(J,e.a,e.t0);
    let p1=e.k==="tiro"? e.xy.slice() : posOf(J,e.b,e.t1);
    const act=(t>=e.t0&&t<=e.t1);
    if(act){const u=ss((t-e.t0)/Math.max(.001,e.t1-e.t0));
      p1=[p0[0]+(p1[0]-p0[0])*u, p0[1]+(p1[1]-p0[1])*u];}
    out.push([p0,p1,(e.rojo||e.perdida)?"rojo":"pase",act]);
  }
  return out.slice(-n);
}
function cadena(J,t){
  const s=[];
  for(const e of J.ball){
    if(t<e.t0) break;
    if(e.k==="hold"&&!s.length) s.push(e.who);
    else if(e.k==="pase"){ if(!s.length) s.push(e.a);
      s.push(e.b[0]==="r"? "ROJO "+e.b.slice(1) : e.b); }
    else if(e.k==="tiro") s.push("TIRO");
    else if(e.k==="conduce") s.push("STOP BALL");
  }
  const last=s.slice(-9);
  return (s.length>9?"…  →  ":"")+last.join("  →  ");
}

/* --------------------------------------------------------------- dibujo --- */
function draw(st){
  gPlay.innerHTML="";
  if(st.glow>0)
    el("rect",{x:D.stop.x0,y:Y(D.stop.y0),width:(D.stop.x1-D.stop.x0),
      height:Y(D.stop.y1)-Y(D.stop.y0),fill:"#fff",opacity:0.45*st.glow},gPlay);
  (st.lines||[]).forEach(([pts,a])=>{
    const dd=pts.map((p,i)=>(i?"L":"M")+X(p[0])+" "+Y(p[1])).join(" ");
    el("path",{d:dd,fill:"none",stroke:"#7ee0ff","stroke-width":.8,"stroke-linecap":"round",
      opacity:a},gPlay);
  });
  (st.trails||[]).forEach(([p0,p1,kind,act],i,arr)=>{
    const age=arr.length-i;
    const op=act?1:Math.max(.25,.92-age*.2);
    const col=kind==="conduce"?"#7ee0ff":(kind==="rojo"?"#ff7878":"#ffd54a");
    const a={x1:X(p0[0]),y1:Y(p0[1]),x2:X(p1[0]),y2:Y(p1[1]),stroke:col,
      "stroke-width":act?.85:.5,opacity:op,"stroke-linecap":"round"};
    if(kind==="conduce") a["stroke-dasharray"]="1.7 1.1";
    el("line",a,gPlay);
    if(act){
      const ang=Math.atan2(Y(p1[1])-Y(p0[1]),X(p1[0])-X(p0[0])), hl=2.0,hw=1.05;
      el("path",{d:`M${X(p1[0])} ${Y(p1[1])} L${X(p1[0])-hl*Math.cos(ang)+hw*Math.sin(ang)} `+
        `${Y(p1[1])-hl*Math.sin(ang)-hw*Math.cos(ang)} L${X(p1[0])-hl*Math.cos(ang)-hw*Math.sin(ang)} `+
        `${Y(p1[1])-hl*Math.sin(ang)+hw*Math.cos(ang)} Z`,fill:col},gPlay);
    }
  });
  const put=(lb,p,team)=>{
    const g=el("g",{},gPlay);
    if(st.carrier===lb) el("circle",{cx:X(p[0]),cy:Y(p[1]),r:2.95,fill:"none",
      stroke:"#ffc83c","stroke-width":.42},g);
    el("circle",{cx:X(p[0]),cy:Y(p[1]),r:2.15,fill:team==="own"?"#1a4c9e":"#ce2828",
      stroke:team==="own"?"#09214a":"#700c0c","stroke-width":.3},g);
    el("circle",{cx:X(p[0]),cy:Y(p[1]),r:2.0,fill:"none",
      stroke:team==="own"?"#e2eeff":"#ffe2e2","stroke-width":.18},g);
    el("text",{x:X(p[0]),y:Y(p[1]),fill:"#fff","font-size":lb.length>1?1.75:1.95,
      "font-weight":800,"text-anchor":"middle","dominant-baseline":"central",
      "font-family":"Segoe UI,Arial,sans-serif"},g).textContent=lb.replace(/^r/,"");
  };
  for(const lb in st.reds) put(lb,st.reds[lb],"rival");
  for(const lb in st.blues) put(lb,st.blues[lb],"own");
  if(st.ball){
    const g=el("g",{},gPlay);
    el("circle",{cx:X(st.ball[0]),cy:Y(st.ball[1]),r:1.32,fill:"#111"},g);
    el("circle",{cx:X(st.ball[0]),cy:Y(st.ball[1]),r:1.15,fill:"#fcfcfc",stroke:"#181818",
      "stroke-width":.16},g);
    el("circle",{cx:X(st.ball[0]),cy:Y(st.ball[1]),r:.42,fill:"#161616"},g);
  }
  document.getElementById("chip").textContent=st.chip;
  document.getElementById("titulo").textContent=st.titulo;
  document.getElementById("texto").textContent=st.texto;
  document.getElementById("chain").textContent=st.chain||"";
  document.getElementById("barfill").style.width=(st.prog*100).toFixed(1)+"%";
}

/* -------------------------------------------------------------- guion ---- */
const INTRO_D = 2.4 + D.lineas.length*1.9 + 1.4;
const SEGS = [{k:"intro",dur:INTRO_D}].concat(D.jugadas.map(j=>({k:"jugada",j:j,dur:j.dur+0.8})));
const TOTAL = SEGS.reduce((a,s)=>a+s.dur,0);
const OFFS = []; let acc=0; SEGS.forEach(s=>{OFFS.push(acc); acc+=s.dur;});

function stateAt(T){
  let i=SEGS.length-1;
  while(i>0 && T<OFFS[i]) i--;
  const s=SEGS[i], t=T-OFFS[i];
  if(s.k==="intro"){
    const blues={},reds={};
    for(const k in D.blue) blues[k]=D.blue[k];
    for(const k in D.red) reds[k]=D.red[k];
    let lines=[],chip="LA TAREA",titulo="ESPACIO, EQUIPOS Y OBJETIVO",
        texto="10 azules en 1-3-4-3 (sin portero) contra 8 rojos. Hay que llevar el balón "+
              "desde el fondo propio hasta pararlo en la zona verde.",
        chain=D.reglas[0]+"   ·   "+D.reglas[1];
    if(t>2.4){
      const k=Math.min(D.lineas.length-1,Math.floor((t-2.4)/1.9));
      const u=Math.min(1,((t-2.4)-k*1.9)/0.55);
      for(let q=0;q<k;q++) lines.push([D.lineas[q].labels.map(l=>D.blue[l]),0.45]);
      const pts=D.lineas[k].labels.map(l=>D.blue[l]);
      lines.push([partial(pts,u),1]);
      chip="1-3-4-3"; titulo="ESTRUCTURA DEL EQUIPO AZUL";
      texto=D.lineas[k].txt; chain=D.reglas[2]+"   ·   "+D.reglas[3];
      if(t>2.4+D.lineas.length*1.9){
        lines=D.lineas.map(L=>[L.labels.map(l=>D.blue[l]),0.7]);
        texto="3 centrales + 2 carrileros + 2 interiores + 3 arriba. Cada línea, en su zona.";
      }
    }
    return {blues,reds,lines,chip,titulo,texto,chain,glow:0,prog:T/TOTAL};
  }
  const J=s.j, tt=Math.min(t,J.dur);
  const b=ballAt(J,tt), blues={},reds={};
  for(const k in D.blue) blues[k]=posOf(J,k,tt);
  for(const k in D.red) reds[k]=redPos(J,k,tt,b);
  let cur=J.ball[0]; for(const e of J.ball) if(tt>=e.t0) cur=e;
  return {blues,reds,ball:[b[0],b[1]],carrier:b[2],trails:trailsAt(J,tt),
    chip:"JUGADA "+J.num, titulo:J.titulo, texto:cur.txt, chain:cadena(J,tt),
    glow:cur.gol?(0.35+0.3*Math.sin(tt*7)):0, prog:T/TOTAL};
}
function partial(pts,u){
  if(u>=1) return pts;
  const tot=pts.length-1, done=u*tot, out=[pts[0]];
  for(let i=0;i<tot;i++){
    if(done>=i+1) out.push(pts[i+1]);
    else if(done>i){const k=done-i;
      out.push([pts[i][0]+(pts[i+1][0]-pts[i][0])*k, pts[i][1]+(pts[i+1][1]-pts[i][1])*k]);
      break;}
    else break;
  }
  return out;
}

/* -------------------------------------------------------------- control -- */
let T=0, playing=true, speed=1, last=performance.now();
const mh=/[#&]t=([\d.]+)/.exec(location.hash); if(mh){T=parseFloat(mh[1]); playing=false;}
function loop(now){
  const dt=(now-last)/1000; last=now;
  if(playing){ T+=dt*speed; if(T>TOTAL) T=0; }
  draw(stateAt(T));
  requestAnimationFrame(loop);
}
if(!playing) document.getElementById("play").textContent="▶ Reproducir";
document.getElementById("play").onclick=e=>{
  playing=!playing; e.target.textContent=playing?"⏸ Pausa":"▶ Reproducir";};
document.getElementById("reset").onclick=()=>{T=0;};
document.querySelectorAll(".seg").forEach(b=>b.onclick=()=>{T=OFFS[+b.dataset.seg]+0.01;});
const SP=[1,1.5,0.5];let sp=0;
document.getElementById("spd").onclick=e=>{sp=(sp+1)%SP.length;speed=SP[sp];
  e.target.textContent=SP[sp]+"x";};
requestAnimationFrame(loop);
</script>
</body>
</html>
"""


def main():
    out = os.path.join(HERE, "animacion-1343-stopball.html")
    html = HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("html ->", out, f"({os.path.getsize(out)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
