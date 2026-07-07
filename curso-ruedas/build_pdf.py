#!/usr/bin/env python3
"""Genera un PDF unico del curso de Ruedas de pases (textos + pizarras) -> curso-ruedas.pdf"""
import os, re, html
from pathlib import Path
import markdown
from weasyprint import HTML

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAF = os.path.join(ROOT, "graficos")

GRAF_URI = Path(GRAF).as_uri()
DOCS = [
    ("README.md", None),
    ("modulos/01-fundamentos.md", "MÓDULO 01 · Fundamentos de la rueda de pases"),
    ("modulos/02-principios-tecnicos.md", "MÓDULO 02 · Principios técnicos (coaching points)"),
    ("modulos/03-organizar-progresar.md", "MÓDULO 03 · Organizar y progresar las ruedas"),
    ("modulos/04-del-patron-al-juego.md", "MÓDULO 04 · Del patrón al juego"),
    ("ejercicios/00-como-usar.md", "CÓMO USAR EL BANCO DE 30 RUEDAS"),
    ("ejercicios/01-basicas.md", "FAMILIA 1 · Básicas (01–05)"),
    ("ejercicios/02-movilidad.md", "FAMILIA 2 · Movilidad y rotación (06–10)"),
    ("ejercicios/03-tercer-hombre.md", "FAMILIA 3 · Pared y tercer hombre (11–15)"),
    ("ejercicios/04-progresion.md", "FAMILIA 4 · Progresión por zonas (16–20)"),
    ("ejercicios/05-finalizacion.md", "FAMILIA 5 · Finalización (21–25)"),
    ("ejercicios/06-oposicion.md", "FAMILIA 6 · Oposición y transferencia (26–30)"),
]

def fix_imgs(body):
    # rutas relativas a graficos -> ruta absoluta (file)
    body = body.replace('src="../graficos/', f'src="{GRAF_URI}/')
    body = body.replace('src="graficos/', f'src="{GRAF_URI}/')
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
 @bottom-center{content:"Ruedas de pases · MISTER ÉLITE — Moisés Díaz";font-size:8pt;color:#999;}
 @bottom-right{content:counter(page);font-size:8pt;color:#999;}}
@page cover{margin:0;}
.cover{page:cover;page-break-after:always;width:100%;height:100%;}
.cover img{display:block;width:100%;height:100vh;object-fit:cover;}
*{box-sizing:border-box;}
body{font-family:'Segoe UI','Helvetica Neue',Arial,sans-serif;color:#1a1a18;font-size:10.5pt;line-height:1.5;}
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
    chunks = [f'<div class="cover"><img src="{GRAF_URI}/portada.svg"></div>']
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
    out = os.path.join(ROOT, "curso-ruedas.pdf")
    HTML(string=doc, base_url=ROOT).write_pdf(out)
    print("PDF generado:", out, os.path.getsize(out), "bytes")

if __name__ == "__main__":
    main()
