#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera UN SOLO archivo HTML autocontenido (SVG + CSS embebidos) -> curso-1442-completo.html"""
import os, re, html
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAF = os.path.join(ROOT, "graficos")

PAGES = [
    ("README.md", "inicio", "Inicio", "Curso"),
    ("modulos/01-fundamentos.md", "m01", "M01 · Fundamentos", "Teoría"),
    ("modulos/02-fase-defensiva.md", "m02", "M02 · Fase defensiva", "Teoría"),
    ("modulos/03-fase-ofensiva.md", "m03", "M03 · Fase ofensiva", "Teoría"),
    ("modulos/04-transiciones-y-balon-parado.md", "m04", "M04 · Transiciones y ABP", "Teoría"),
    ("ejercicios/00-plan-sesiones.md", "plan", "Plan de sesiones", "Práctica"),
    ("ejercicios/01-salida.md", "b1", "B1 · Salida (T1–4)", "Práctica"),
    ("ejercicios/02-defensa.md", "b2", "B2 · Defensa (T5–9)", "Práctica"),
    ("ejercicios/03-pressing.md", "b3", "B3 · Pressing (T10–13)", "Práctica"),
    ("ejercicios/04-delanteros-centros.md", "b4", "B4 · Delanteros y centros (T14–18)", "Práctica"),
    ("ejercicios/05-transiciones.md", "b5", "B5 · Transiciones (T19–22)", "Práctica"),
    ("ejercicios/06-partido-condicionado.md", "b6", "B6 · Partido condicionado (T23–25)", "Práctica"),
    ("ejercicios/07-balon-parado.md", "b7", "B7 · Balón parado (T26–27)", "Práctica"),
]

def read_svg(name):
    p = os.path.join(GRAF, name)
    if not os.path.exists(p):
        return None
    s = open(p, encoding="utf-8").read()
    s = re.sub(r'<\?xml[^>]*\?>', '', s).strip()
    # quitar width/height fijos para que escale al contenedor
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r'\1', s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r'\1', s, count=1)
    return s

def inline_images(body):
    def repl(m):
        full = m.group(0)
        alt = re.search(r'alt="([^"]*)"', full)
        src = re.search(r'src="([^"]*)"', full)
        if not src:
            return full
        fname = src.group(1).split("/")[-1]
        svg = read_svg(fname)
        cap = re.sub(r'^\s*(DIAGRAMA|Pizarra[^:]*):\s*', '', alt.group(1) if alt else "")
        cap_html = html.escape(cap)
        if svg is None:
            return f'<figure class="diag"><em>[falta {html.escape(fname)}]</em></figure>'
        return f'<figure class="diag">{svg}<figcaption>📋 {cap_html}</figcaption></figure>'
    return re.sub(r'<img[^>]*>', repl, body)

def strip_md_links(body):
    # los enlaces .md internos se convierten en anclas si apuntan a una página conocida
    name2anchor = {os.path.basename(src): anc for src, anc, _, _ in PAGES}
    def repl(m):
        url, text = m.group(1), m.group(2)
        base = url.split("/")[-1].split("#")[0]
        if base in name2anchor:
            return f'<a href="#{name2anchor[base]}">{text}</a>'
        if base == "PEDIDOS.md":
            return text
        return text if url.endswith(".md") else m.group(0)
    return re.sub(r'<a href="([^"]+)">(.*?)</a>', repl, body, flags=re.S)

CSS = """
:root{--bg:#f5f4f0;--ink:#1a1a18;--dark:#15202b;--muted:#6b6b66;--line:#e3e1da;--accent:#1d6fb8;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--ink);line-height:1.6;}
.layout{display:flex;}
.side{width:280px;flex-shrink:0;background:var(--dark);color:#fff;position:sticky;top:0;height:100vh;overflow-y:auto;padding:1.4rem 0;}
.side .brand{display:block;font-size:17px;font-weight:800;color:#fff;text-decoration:none;padding:0 1.4rem 1rem;border-bottom:1px solid rgba(255,255,255,.12);margin-bottom:.4rem;}
.side .brand small{display:block;font-size:11px;font-weight:600;color:#f7c948;letter-spacing:1px;margin-top:2px;}
.side .sec{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:rgba(255,255,255,.45);padding:.9rem 1.4rem .3rem;}
.side a.nav{display:block;padding:.45rem 1.4rem;color:rgba(255,255,255,.72);text-decoration:none;font-size:13.5px;border-left:3px solid transparent;}
.side a.nav:hover{color:#fff;background:rgba(255,255,255,.06);}
.content{flex:1;min-width:0;display:flex;justify-content:center;}
.inner{max-width:840px;width:100%;padding:2.4rem 2rem 5rem;}
section{scroll-margin-top:1rem;padding-top:1.5rem;border-top:1px solid var(--line);margin-top:2.5rem;}
section:first-of-type{border-top:none;margin-top:0;}
#menu-btn{display:none;position:fixed;top:12px;left:12px;z-index:50;background:var(--dark);color:#fff;border:none;font-size:20px;width:42px;height:42px;border-radius:8px;cursor:pointer;}
img.hero{display:block;width:100%;height:auto;border-radius:12px;margin:0 0 2rem;box-shadow:0 4px 20px rgba(0,0,0,.15);}
h1{font-size:30px;line-height:1.2;margin:.2rem 0 1rem;letter-spacing:-.02em;}
h2{font-size:22px;margin:1.8rem 0 .7rem;padding-bottom:.3rem;border-bottom:2px solid var(--line);}
h3{font-size:17px;margin:1.3rem 0 .4rem;}
h4{font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin:1rem 0 .3rem;}
p{margin:.55rem 0;} ul,ol{margin:.4rem 0 .8rem 1.4rem;} li{margin:.2rem 0;}
a{color:var(--accent);} strong{color:#111;}
code{background:#ecebe6;padding:.1em .35em;border-radius:4px;font-size:.9em;}
blockquote{border-left:4px solid var(--accent);background:#eef4fa;padding:.7rem 1rem;margin:1rem 0;border-radius:0 6px 6px 0;color:#33485c;}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:14px;display:block;overflow-x:auto;}
th,td{border:1px solid var(--line);padding:.5rem .7rem;text-align:left;vertical-align:top;}
th{background:#efeee9;font-weight:700;} tr:nth-child(even) td{background:#faf9f6;}
figure.diag{margin:1.4rem 0;background:#fff;border:1px solid var(--line);border-radius:10px;padding:.7rem;box-shadow:0 1px 3px rgba(0,0,0,.05);}
figure.diag svg{display:block;width:100%;height:auto;border-radius:6px;}
figure.diag figcaption{font-size:12.5px;color:var(--muted);margin-top:.5rem;font-style:italic;}
.foot{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--line);font-size:12px;color:var(--muted);}
@media(max-width:880px){.side{position:fixed;transform:translateX(-100%);transition:transform .2s;z-index:40;box-shadow:2px 0 12px rgba(0,0,0,.3);}
 .side.open{transform:translateX(0);} #menu-btn{display:block;} .inner{padding:4rem 1.1rem 3rem;} h1{font-size:24px;}}
"""

def main():
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    # nav
    secs = {}
    order = []
    for src, anc, title, sec in PAGES:
        secs.setdefault(sec, []);
        if sec not in order: order.append(sec)
        secs[sec].append((anc, title))
    nav = ['<a class="brand" href="#inicio">⚽ Curso 1-4-4-2<small>MISTER ÉLITE · MOISÉS DÍAZ</small></a>']
    for sec in order:
        nav.append(f'<div class="sec">{html.escape(sec)}</div>')
        for anc, title in secs[sec]:
            nav.append(f'<a class="nav" href="#{anc}">{html.escape(title)}</a>')
    nav_html = "\n".join(nav)
    # secciones
    parts = []
    portada = read_svg("portada.svg")
    for src, anc, title, sec in PAGES:
        p = os.path.join(ROOT, src)
        if not os.path.exists(p):
            continue
        md.reset()
        body = md.convert(open(p, encoding="utf-8").read())
        body = strip_md_links(body)
        body = inline_images(body)
        if anc == "inicio" and portada:
            body = f'<div class="hero">{portada}</div>' + body
        parts.append(f'<section id="{anc}">{body}</section>')
    doc = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Curso 1-4-4-2 · MISTER ÉLITE</title><style>{CSS}</style></head><body>
<button id="menu-btn">☰</button>
<div class="layout"><nav class="side">{nav_html}</nav>
<main class="content"><div class="inner">{''.join(parts)}
<footer class="foot">Curso "Sistema 1-4-4-2: del concepto al campo" · MISTER ÉLITE — Moisés Díaz</footer>
</div></main></div>
<script>const b=document.getElementById('menu-btn'),s=document.querySelector('.side');
b.onclick=()=>s.classList.toggle('open');
document.querySelectorAll('.side a').forEach(a=>a.onclick=()=>s.classList.remove('open'));</script>
</body></html>"""
    out = os.path.join(ROOT, "curso-1442-completo.html")
    open(out, "w", encoding="utf-8").write(doc)
    print("HTML único:", out, round(os.path.getsize(out)/1024), "KB")

if __name__ == "__main__":
    main()
