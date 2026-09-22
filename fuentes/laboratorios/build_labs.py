# -*- coding: utf-8 -*-
"""Arma cada laboratorio como un solo archivo HTML autocontenido.

Toma labN-body.html, le incrusta la hoja común, las utilidades, el logo y las
imágenes, y escribe Laboratorio-N-SIO0010.html en la carpeta del material.
Uso:  python build_labs.py [2 3 4 ...]     (sin argumentos: todos los que encuentre)
"""
import base64, glob, io, os, re, sys

AQUI  = os.path.dirname(os.path.abspath(__file__))
PROY  = os.path.abspath(os.path.join(AQUI, "..", ".."))          # …\Material SIO0010
RAIZ  = os.path.abspath(os.path.join(PROY, ".."))                # …\Promoción especialización
MEDIA = os.path.join(AQUI, "media")

CABEZA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titulo)s</title>
<style>
%(css)s
</style>
</head>
<body>
<script>
%(js)s
</script>
"""


def b64(ruta):
    with open(ruta, "rb") as f:
        return base64.b64encode(f.read()).decode()


def arma(numero):
    cuerpo_ruta = os.path.join(AQUI, "lab%s-body.html" % numero)
    cuerpo = io.open(cuerpo_ruta, encoding="utf-8").read()

    m = re.match(r"\s*<!--\s*titulo:\s*(.+?)\s*-->\s*", cuerpo)
    titulo = m.group(1) if m else "Laboratorio %s · SIO0010 Técnicas Criptográficas" % numero
    if m:
        cuerpo = cuerpo[m.end():]

    html = CABEZA % {
        "titulo": titulo,
        "css": io.open(os.path.join(AQUI, "lab-base.css"), encoding="utf-8").read(),
        "js": io.open(os.path.join(AQUI, "lab-base.js"), encoding="utf-8").read(),
    } + cuerpo + "\n</body>\n</html>\n"

    html = html.replace("LOCKUP_B64", b64(os.path.join(RAIZ, "iue.png")))

    imagenes = []
    for nombre in sorted(set(re.findall(r"MEDIA\(([^)]+)\)", html))):
        ruta = os.path.join(MEDIA, nombre)
        if not os.path.exists(ruta):
            raise SystemExit("  falta la imagen: %s" % ruta)
        html = html.replace("MEDIA(%s)" % nombre, b64(ruta))
        imagenes.append(nombre)

    sobrantes = re.findall(r"[A-Z_]{4,}_B64|MEDIA\([^)]*\)", html)
    if sobrantes:
        raise SystemExit("  quedaron marcadores sin reemplazar: %s" % sorted(set(sobrantes)))

    salida = os.path.join(PROY, "Laboratorio-%s-SIO0010.html" % numero)
    io.open(salida, "w", encoding="utf-8").write(html)
    print("  laboratorio %s: %s KB · %d imagen(es) · %s"
          % (numero, round(len(html.encode("utf-8")) / 1024), len(imagenes), os.path.basename(salida)))


if __name__ == "__main__":
    pedidos = sys.argv[1:]
    if not pedidos:
        pedidos = sorted(re.findall(r"lab(\d+)-body\.html", " ".join(glob.glob(os.path.join(AQUI, "lab*-body.html")))))
    for n in pedidos:
        arma(n)
