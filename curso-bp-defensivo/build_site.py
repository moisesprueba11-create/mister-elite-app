#!/usr/bin/env python3
"""Construye una versión HTML navegable del curso de Balón parado defensivo a partir de los .md.
Salida: curso-bp-defensivo/site/  (abrir site/index.html)."""
import os, re, shutil, html
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

# (ruta_md, ruta_salida_html, titulo, seccion)
PAGES = [
    ("README.md", "index.html", "Inicio", None),
    ("modulos/01-fundamentos.md", "modulos/01-fundamentos.html", "M01 · Fundamentos", "Teoría"),
    ("modulos/02-sistemas-marcaje.md", "modulos/02-sistemas-marcaje.html", "M02 · Sistemas de marcaje", "Teoría"),
    ("ejercicios/00-como-defender.md", "ejercicios/00-como-defender.html", "Cómo defender", "Práctica"),
    ("ejercicios/01-corner.md", "ejercicios/01-corner.html", "Córners", "Práctica"),
    ("ejercicios/02-faltas.md", "ejercicios/02-faltas.html", "Faltas", "Práctica"),
    ("ejercicios/03-saques-banda.md", "ejercicios/03-saques-banda.html", "Saques de banda", "Práctica"),
]

def prefix_for(out_path):
    depth = out_path.count("/")
    return "../" * depth

def build_nav(current_out, prefix):
    sections = {}
    order = []
    for md, out, title, sec in PAGES:
        key = sec or "Curso"
        if key not in sections:
            sections[key] = []
            order.append(key)
        sections[key].append((out, title))
    parts = ['<nav class="side">']
    parts.append(f'<a class="brand" href="{prefix}index.html">🛡️ Balón parado defensivo</a>')
    for sec in order:
        parts.append(f'<div class="sec-title">{html.escape(sec)}</div>')
        parts.append('<ul>')
        for out, title in sections[sec]:
            cls = ' class="active"' if out == current_out else ''
            parts.append(f'<li><a{cls} href="{prefix}{out}">{html.escape(title)}</a></li>')
        parts.append('</ul>')
    parts.append('</nav>')
    return "\n".join(parts)

def rewrite_links(body):
    # .md -> .html en los href; deja .svg y externos intactos
    def repl(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        if url.endswith(".md"):
            url = url[:-3] + ".html"
        elif ".md#" in url:
            url = url.replace(".md#", ".html#")
        return f'{attr}="{url}"'
    return re.sub(r'(href|src)="([^"]+)"', repl, body)

def figurify(body):
    # convierte <img alt="DIAGRAMA: x" src="..."> en figure con figcaption
    def repl(m):
        full = m.group(0)
        alt = re.search(r'alt="([^"]*)"', full)
        src = re.search(r'src="([^"]*)"', full)
        if not src:
            return full
        cap = alt.group(1) if alt else ""
        cap = re.sub(r'^\s*DIAGRAMA:\s*', '', cap)
        cap_html = html.escape(cap)
        return (f'<figure class="diagrama"><img loading="lazy" src="{src.group(1)}" '
                f'alt="{html.escape(cap)}"><figcaption>📋 {cap_html}</figcaption></figure>')
    return re.sub(r'<img[^>]*>', repl, body)

PAGE_TMPL = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Balón parado defensivo</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<button id="menu-btn" aria-label="Menú">☰</button>
<div class="layout">
{nav}
<main class="content">
<div class="content-inner">
{body}
<footer class="foot">Curso "Balón parado defensivo" · MISTER ÉLITE — Moisés Díaz</footer>
</div>
</main>
</div>
<script>
const b=document.getElementById('menu-btn');const s=document.querySelector('.side');
b.addEventListener('click',()=>s.classList.toggle('open'));
document.querySelectorAll('.side a').forEach(a=>a.addEventListener('click',()=>s.classList.remove('open')));
</script>
</body>
</html>
"""

CSS = """
:root{--bg:#f5f4f0;--ink:#1a1a18;--dark:#1a1a18;--muted:#6b6b66;--line:#e3e1da;--accent:#1d6fb8;--rival:#c0392b;--card:#fff;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--ink);line-height:1.6;}
.layout{display:flex;min-height:100vh;}
.side{width:280px;flex-shrink:0;background:var(--dark);color:#fff;padding:1.5rem 0;position:sticky;top:0;height:100vh;overflow-y:auto;}
.side .brand{display:block;font-size:17px;font-weight:700;color:#fff;text-decoration:none;padding:0 1.5rem 1rem;border-bottom:1px solid rgba(255,255,255,.12);margin-bottom:.5rem;}
.side .sec-title{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:rgba(255,255,255,.45);padding:1rem 1.5rem .35rem;}
.side ul{list-style:none;}
.side li a{display:block;padding:.5rem 1.5rem;color:rgba(255,255,255,.72);text-decoration:none;font-size:13.5px;border-left:3px solid transparent;}
.side li a:hover{color:#fff;background:rgba(255,255,255,.06);}
.side li a.active{color:#fff;border-left-color:var(--accent);background:rgba(29,111,184,.18);font-weight:600;}
.content{flex:1;min-width:0;display:flex;justify-content:center;}
.content-inner{max-width:820px;width:100%;padding:2.5rem 2rem 4rem;}
#menu-btn{display:none;position:fixed;top:12px;left:12px;z-index:50;background:var(--dark);color:#fff;border:none;font-size:20px;width:42px;height:42px;border-radius:8px;cursor:pointer;}
h1{font-size:30px;line-height:1.2;margin:.2rem 0 1rem;letter-spacing:-.02em;}
h2{font-size:22px;margin:2rem 0 .8rem;padding-bottom:.3rem;border-bottom:2px solid var(--line);}
h3{font-size:17px;margin:1.4rem 0 .5rem;color:#222;}
h4{font-size:14px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin:1.1rem 0 .4rem;}
p{margin:.6rem 0;}
ul,ol{margin:.5rem 0 .9rem 1.4rem;}
li{margin:.25rem 0;}
a{color:var(--accent);}
strong{color:#111;}
hr{border:none;border-top:1px solid var(--line);margin:2rem 0;}
code{background:#ecebe6;padding:.1em .35em;border-radius:4px;font-size:.9em;}
blockquote{border-left:4px solid var(--accent);background:#eef4fa;padding:.7rem 1rem;margin:1rem 0;border-radius:0 6px 6px 0;color:#33485c;}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:14px;display:block;overflow-x:auto;}
th,td{border:1px solid var(--line);padding:.5rem .7rem;text-align:left;vertical-align:top;}
th{background:#efeee9;font-weight:700;}
tr:nth-child(even) td{background:#faf9f6;}
figure.diagrama{margin:1.5rem 0;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.8rem;box-shadow:0 1px 3px rgba(0,0,0,.05);}
figure.diagrama img{display:block;width:100%;height:auto;border-radius:6px;background:#2e7d32;}
figure.diagrama figcaption{font-size:12.5px;color:var(--muted);margin-top:.6rem;font-style:italic;}
img.hero{display:block;width:100%;height:auto;border-radius:12px;margin:0 0 2rem;box-shadow:0 4px 20px rgba(0,0,0,.15);}
.foot{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--line);font-size:12px;color:var(--muted);}
@media(max-width:880px){
 .side{position:fixed;left:0;top:0;transform:translateX(-100%);transition:transform .2s;z-index:40;box-shadow:2px 0 12px rgba(0,0,0,.3);}
 .side.open{transform:translateX(0);}
 #menu-btn{display:block;}
 .content-inner{padding:4rem 1.1rem 3rem;}
 h1{font-size:25px;}
}
"""

def main():
    if os.path.exists(SITE):
        shutil.rmtree(SITE)
    os.makedirs(os.path.join(SITE, "assets"))
    # copiar graficos
    shutil.copytree(os.path.join(ROOT, "graficos"), os.path.join(SITE, "graficos"),
                    ignore=shutil.ignore_patterns("*.md"))
    with open(os.path.join(SITE, "assets", "style.css"), "w") as f:
        f.write(CSS)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    built = 0
    for src, out, title, sec in PAGES:
        src_path = os.path.join(ROOT, src)
        if not os.path.exists(src_path):
            print("AVISO: falta", src); continue
        with open(src_path, encoding="utf-8") as f:
            text = f.read()
        md.reset()
        body = md.convert(text)
        body = rewrite_links(body)
        body = figurify(body)
        prefix = prefix_for(out)
        if out == "index.html":
            body = (f'<img class="hero" src="{prefix}graficos/portada.svg" '
                    f'alt="Balón parado defensivo · MISTER ÉLITE">' + body)
        page = PAGE_TMPL.format(title=html.escape(title), prefix=prefix,
                                nav=build_nav(out, prefix), body=body)
        out_path = os.path.join(SITE, out)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        built += 1
    print(f"OK: {built} páginas generadas en {SITE}")

if __name__ == "__main__":
    main()
