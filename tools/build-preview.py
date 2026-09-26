#!/usr/bin/env python3
"""
Genera una copia autocontenida de index.html con las imágenes incrustadas en
base64, para poder revisarla dentro de un chat (donde no se sirven los
archivos de assets/).

    python3 tools/build-preview.py            -> preview.html
    python3 tools/build-preview.py salida.html

El repositorio siempre usa rutas relativas a assets/img/. Esta copia es
desechable: no se versiona y no se publica.
"""
import base64
import mimetypes
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "index.html"
DESTINO = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "preview.html"

html = ORIGEN.read_text(encoding="utf-8")
cache: dict[str, str] = {}
faltantes: list[str] = []


def incrustar(ruta: str) -> str:
    if ruta not in cache:
        archivo = RAIZ / ruta
        if not archivo.is_file():
            faltantes.append(ruta)
            return ruta
        tipo = mimetypes.guess_type(archivo.name)[0] or "application/octet-stream"
        datos = base64.b64encode(archivo.read_bytes()).decode("ascii")
        cache[ruta] = f"data:{tipo};base64,{datos}"
    return cache.get(ruta, ruta)


# src="assets/…" y cada entrada de srcset="assets/… 420w, assets/… 720w"
html = re.sub(
    r'(?<=["\s,])(assets/[^\s"\'>,]+)',
    lambda m: incrustar(m.group(1)),
    html,
)

DESTINO.write_text(html, encoding="utf-8")
print(f"{DESTINO}  ·  {len(cache)} imágenes incrustadas  ·  {DESTINO.stat().st_size // 1024} KB")
if faltantes:
    print("FALTAN:", ", ".join(sorted(set(faltantes))))
    sys.exit(1)
