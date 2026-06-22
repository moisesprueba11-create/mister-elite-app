#!/usr/bin/env python3
"""Genera un PDF unico del curso 1-4-4-2 (textos + pizarras) -> curso-1442.pdf"""
import os, re, html
import markdown
from weasyprint import HTML

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAF = os.path.join(ROOT, "graficos")

DOCS = [
    ("README.md", None),
    ("modulos/01-fundamentos.md", "MÓDULO 01 · Fundamentos"),
    ("modulos/02-fase-defensiva.md", "MÓDULO 02 · Fase defensiva"),
    ("modulos/03-fase-ofensiva.md", "MÓDULO 03 · Fase ofensiva"),
    ("modulos/04-transiciones-y-balon-parado.md", "MÓDULO 04 · Transiciones y balón parado"),
    ("ejercicios/00-plan-sesiones.md", "PLAN DE SESIONES"),
    ("ejercicios/01-salida.md", "BLOQUE 1 · Salida de balón"),
    ("ejercicios/02-defensa.md", "BLOQUE 2 · Organización defensiva"),
    ("ejercicios/03-pressing.md", "BLOQUE 3 · Pressing"),
    ("ejercicios/04-delanteros-centros.md", "BLOQUE 4 · Delanteros y centros"),
    ("ejercicios/05-transiciones.md", "BLOQUE 5 · Transiciones"),
    ("ejercicios/06-partido-condicionado.md", "BLOQUE 6 · Partido condicionado"),
    ("ejercicios/07-balon-parado.md", "BLOQUE 7 · Balón parado"),
]

def fix_imgs(body):
    # rutas relativas a graficos -> ruta absoluta (file)
    body = body.replace('src="../graficos/', f'src="file://{GRAF}/')
    body = body.replace('src="graficos/', f'src="file://{GRAF}/')
    def repl(m):
        full = m.group(0)
        alt = re.search(r'alt="([^"]*)"', full)
        src = re.search(r'src="([^"]*)"', full)
        if not src: return full
        cap = re.sub(r'^\s*DIAGRAMA:\s*', '', alt.group(1) if alt else "")
        return (f'<figure class="diag"><img src="{src.group(1)}">'
                f'<figcaption>{html.escape(cap)}</figcaption></figure>')
    return re.sub(r'<img[^>]*>', repl, body)

def strip_md_links(body):
    # quita enlaces internos .md (no navegables en PDF) dejando el texto
    return re.sub(r'<a href="[^"]*\.md[^"]*">(.*?)</a>', r'\1', body, flags=re.S)

CSS = """
@page{size:A4;margin:1.8cm 1.6cm;
 @bottom-center{content:"Sistema 1-4-4-2 · del concepto al campo";font-size:8pt;color:#999;}
 @bottom-right{content:counter(page);font-size:8pt;color:#999;}}
@page:first{margin:0;}
*{box-sizing:border-box;}
body{font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif;color:#1a1a18;font-size:10.5pt;line-height:1.5;}
.cover{height:297mm;background:#1a1a18;color:#fff;padding:6cm 3cm;page-break-after:always;}
.cover .kicker{color:#1d6fb8;font-weight:700;letter-spacing:.2em;font-size:11pt;text-transform:uppercase;}
.cover h1{font-size:34pt;line-height:1.1;margin:.4cm 0;border:none;color:#fff;}
.cover .sub{font-size:13pt;color:#cfcfca;max-width:14cm;}
.cover .meta{margin-top:3cm;font-size:10pt;color:#9a9a95;border-top:1px solid #333;padding-top:.6cm;}
.doc{page-break-before:always;}
h1{font-size:20pt;color:#1a1a18;border-bottom:3px solid #1d6fb8;padding-bottom:.15cm;margin:0 0 .4cm;}
h2{font-size:14pt;margin:.7cm 0 .25cm;border-bottom:1px solid #ddd;padding-bottom:.1cm;}
h3{font-size:11.5pt;margin:.5cm 0 .15cm;color:#1d6fb8;}
h4{font-size:9.5pt;text-transform:uppercase;color:#666;letter-spacing:.04em;margin:.4cm 0 .1cm;}
p{margin:.2cm 0;}
ul,ol{margin:.2cm 0 .3cm .7cm;}
li{margin:.06cm 0;}
strong{color:#111;}
code{background:#eee;padding:0 .2em;border-radius:3px;font-size:.9em;}
blockquote{border-left:3px solid #1d6fb8;background:#eef4fa;padding:.3cm .5cm;margin:.3cm 0;color:#33485c;}
table{border-collapse:collapse;width:100%;margin:.3cm 0;font-size:8.8pt;}
th,td{border:1px solid #ccc;padding:.12cm .25cm;text-align:left;vertical-align:top;}
th{background:#efeee9;}
hr{border:none;border-top:1px solid #ddd;margin:.5cm 0;}
figure.diag{margin:.4cm 0;text-align:center;page-break-inside:avoid;}
figure.diag img{max-width:78%;max-height:11cm;}
figure.diag figcaption{font-size:8pt;color:#777;font-style:italic;margin-top:.1cm;}
"""

def main():
    md = markdown.Markdown(extensions=["tables","fenced_code","sane_lists","attr_list"])
    chunks = ['<div class="cover"><div class="kicker">Curso para entrenadores</div>'
              '<h1>Sistema 1-4-4-2<br>del concepto al campo</h1>'
              '<div class="sub">Poca teoría, mucha aplicación práctica. 4 módulos, 27 tareas de campo, '
              'plan de microciclos y 23 pizarras tácticas.</div>'
              '<div class="meta">Fundamentos · Fase defensiva · Fase ofensiva · Transiciones · '
              'Balón parado · Banco de tareas · Plan de sesiones</div></div>']
    for src, _ in DOCS:
        p = os.path.join(ROOT, src)
        if not os.path.exists(p):
            print("falta", src); continue
        md.reset()
        body = md.convert(open(p, encoding="utf-8").read())
        body = strip_md_links(fix_imgs(body))
        chunks.append(f'<div class="doc">{body}</div>')
    doc = (f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
           f'<style>{CSS}</style></head><body>{"".join(chunks)}</body></html>')
    out = os.path.join(ROOT, "curso-1442.pdf")
    HTML(string=doc, base_url=ROOT).write_pdf(out)
    print("PDF generado:", out, os.path.getsize(out), "bytes")

if __name__ == "__main__":
    main()
