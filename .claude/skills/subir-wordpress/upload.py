#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
upload.py — Sube los entregables de un curso MISTER ÉLITE a WordPress por la REST API.

Uso:
    python3 upload.py <slug>            # p.ej.  python3 upload.py pretemporada
    python3 upload.py <slug> --dry-run  # comprueba archivos y config, NO sube nada

Sube el PDF y el HTML único a la Biblioteca de Medios y, si hay un post/página/producto
configurado, actualiza su enlace para que apunte a la versión nueva (reemplaza la anterior,
"se subscribe": el alumno siempre ve la última en la misma página). Guarda los IDs en
cursos.json para no duplicar en futuras actualizaciones.

CREDENCIALES (nunca en el repo): se leen de variables de entorno / secretos del entorno:
    WP_URL            https://tu-sitio.com        (sin barra final)
    WP_USER           tu_usuario_wordpress
    WP_APP_PASSWORD   contraseña de aplicación    (Usuarios > Perfil > Contraseñas de aplicación)

Si faltan, el script avisa y no hace nada (no rompe el flujo del curso).
"""
import os, sys, json, base64, mimetypes
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CONFIG = os.path.join(HERE, "cursos.json")
PUBLISH = os.environ.get("WP_PUBLISH", "auto")  # "auto" = publicar; "draft" = borrador


def load_config():
    if os.path.exists(CONFIG):
        return json.load(open(CONFIG, encoding="utf-8"))
    return {}


def save_config(cfg):
    json.dump(cfg, open(CONFIG, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def creds():
    url = os.environ.get("WP_URL", "").rstrip("/")
    user = os.environ.get("WP_USER", "")
    pw = os.environ.get("WP_APP_PASSWORD", "")
    return url, user, pw


def auth_header(user, pw):
    token = base64.b64encode(f"{user}:{pw}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def upload_media(url, headers, path):
    """Sube un archivo a /wp/v2/media y devuelve (id, source_url)."""
    fname = os.path.basename(path)
    ctype = mimetypes.guess_type(fname)[0] or "application/octet-stream"
    h = dict(headers)
    h["Content-Disposition"] = f'attachment; filename="{fname}"'
    h["Content-Type"] = ctype
    with open(path, "rb") as f:
        r = requests.post(f"{url}/wp-json/wp/v2/media", headers=h, data=f.read(), timeout=120)
    r.raise_for_status()
    j = r.json()
    return j["id"], j["source_url"]


def delete_media(url, headers, media_id):
    try:
        requests.delete(f"{url}/wp-json/wp/v2/media/{media_id}?force=true", headers=headers, timeout=60)
    except Exception as e:
        print(f"  · aviso: no se pudo borrar el medio anterior {media_id}: {e}")


def update_post_link(url, headers, post_id, old_url, new_url):
    """Reemplaza la URL antigua por la nueva en el contenido del post/página/producto."""
    r = requests.get(f"{url}/wp-json/wp/v2/posts/{post_id}?context=edit", headers=headers, timeout=60)
    # si no es 'post', probar páginas
    if r.status_code == 404:
        base = f"{url}/wp-json/wp/v2/pages/{post_id}"
    else:
        base = f"{url}/wp-json/wp/v2/posts/{post_id}"
    cur = requests.get(f"{base}?context=edit", headers=headers, timeout=60)
    cur.raise_for_status()
    content = cur.json()["content"]["raw"]
    if old_url and old_url in content:
        content = content.replace(old_url, new_url)
    payload = {"content": content}
    if PUBLISH != "draft":
        payload["status"] = "publish"
    upd = requests.post(base, headers=headers, json=payload, timeout=60)
    upd.raise_for_status()


def main():
    if len(sys.argv) < 2:
        print("uso: python3 upload.py <slug> [--dry-run]"); sys.exit(1)
    slug = sys.argv[1]
    dry = "--dry-run" in sys.argv

    pdf = os.path.join(REPO, f"curso-{slug}", f"curso-{slug}.pdf")
    htmlf = os.path.join(REPO, f"curso-{slug}", f"curso-{slug}-completo.html")
    for p in (pdf, htmlf):
        if not os.path.exists(p):
            print(f"ERROR: no existe {p}"); sys.exit(1)
    print(f"Curso '{slug}': encontrados PDF y HTML.")

    cfg = load_config()
    entry = cfg.get(slug, {})

    url, user, pw = creds()
    if dry:
        print("DRY-RUN: archivos OK. Config actual:", json.dumps(entry, ensure_ascii=False))
        print("Credenciales presentes:" , bool(url and user and pw))
        return
    if not (url and user and pw):
        print("AVISO: faltan WP_URL / WP_USER / WP_APP_PASSWORD en el entorno. "
              "No se sube nada. (Configúralas como secretos del entorno para activar la subida.)")
        return

    headers = auth_header(user, pw)
    print(f"Subiendo a {url} …")

    # PDF
    old_pdf_id = entry.get("pdf_media_id")
    pdf_id, pdf_url = upload_media(url, headers, pdf)
    print(f"  · PDF subido → media #{pdf_id}  {pdf_url}")
    # HTML
    old_html_id = entry.get("html_media_id")
    html_id, html_url = upload_media(url, headers, htmlf)
    print(f"  · HTML subido → media #{html_id}  {html_url}")

    # actualizar enlaces en el post/página destino (si está configurado)
    post_id = entry.get("post_id")
    if post_id:
        update_post_link(url, headers, post_id, entry.get("pdf_url", ""), pdf_url)
        update_post_link(url, headers, post_id, entry.get("html_url", ""), html_url)
        print(f"  · enlaces actualizados en el contenido #{post_id}")
    else:
        print("  · (sin post_id configurado: los archivos están en Medios; falta enlazarlos una vez)")

    # borrar versiones anteriores para no acumular dobles
    if old_pdf_id and old_pdf_id != pdf_id:
        delete_media(url, headers, old_pdf_id)
    if old_html_id and old_html_id != html_id:
        delete_media(url, headers, old_html_id)

    cfg[slug] = {"pdf_media_id": pdf_id, "pdf_url": pdf_url,
                 "html_media_id": html_id, "html_url": html_url,
                 "post_id": post_id}
    save_config(cfg)
    print("OK · cursos.json actualizado.")


if __name__ == "__main__":
    main()
