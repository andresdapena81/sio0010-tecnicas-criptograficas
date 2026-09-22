# -*- coding: utf-8 -*-
"""Genera las imágenes del laboratorio 2: el escudo cifrado con AES-256 en ECB y en CTR.

Se cifran los bytes crudos de los píxeles, no el archivo PNG: así el resultado sigue
siendo una imagen del mismo tamaño y se ve lo que hace cada modo. Es exactamente lo
que los estudiantes reproducen en el ejercicio 1 con OpenSSL sobre un BMP.
"""
import io, os
from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTE = os.path.join(AQUI, "..", "..", "..", "logo_iue_transparent.png")
DESTINO = os.path.join(AQUI, "media")
LADO, ESCALA = 128, 3          # 96×96 píxeles reales, ampliados ×3 sin suavizar

os.makedirs(DESTINO, exist_ok=True)

origen = Image.open(FUENTE).convert("RGBA")
lado = min(origen.size)
origen = origen.crop(((origen.width - lado) // 2, (origen.height - lado) // 2,
                      (origen.width + lado) // 2, (origen.height + lado) // 2))
fondo = Image.new("RGBA", origen.size, (255, 255, 255, 255))
base = Image.alpha_composite(fondo, origen).convert("RGB").resize((LADO, LADO), Image.LANCZOS)
# Aplanar a pocos colores: ECB solo delata lo que se repite, y un degradado no se repite.
base = base.quantize(colors=2, method=Image.MEDIANCUT, dither=Image.Dither.NONE).convert("RGB")

# la fila tiene que ser múltiplo de 16 bytes para que el patrón por bloques se vea alineado
assert (LADO * 3) % 16 == 0, "el ancho en bytes debe ser múltiplo del bloque de AES"

crudo = base.tobytes()
llave, vector = os.urandom(32), os.urandom(16)


def cifra(modo):
    c = Cipher(algorithms.AES(llave), modo).encryptor()
    return c.update(crudo) + c.finalize()


def guarda(datos, nombre):
    img = Image.frombytes("RGB", (LADO, LADO), datos[:len(crudo)])
    img = img.resize((LADO * ESCALA, LADO * ESCALA), Image.NEAREST)
    ruta = os.path.join(DESTINO, nombre)
    img.save(ruta, optimize=True)
    print("  %-22s %6d bytes" % (nombre, os.path.getsize(ruta)))


base.resize((LADO * ESCALA, LADO * ESCALA), Image.NEAREST).save(
    os.path.join(DESTINO, "escudo-original.png"), optimize=True)
print("  %-22s %6d bytes" % ("escudo-original.png", os.path.getsize(os.path.join(DESTINO, "escudo-original.png"))))

# ECB: cada bloque de 16 bytes se cifra igual siempre, así que el dibujo sobrevive
guarda(cifra(modes.ECB()), "escudo-ecb.png")
# CTR: cada bloque se combina con un contador distinto; no queda patrón
guarda(cifra(modes.CTR(vector)), "escudo-ctr.png")
