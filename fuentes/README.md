# Fuentes del material

Aquí están los generadores del material, por si alguien quiere reconstruirlo o adaptarlo a otro caso. No hacen falta para usar los laboratorios: esos ya vienen listos en [`../laboratorios/`](../laboratorios/).

## Laboratorios

Cada laboratorio es un archivo `labN-body.html` con el contenido, más dos archivos comunes:

- `lab-base.css` — la hoja de estilo, incluida la de impresión.
- `lab-base.js` — utilidades compartidas (bytes y hexadecimal, copiar comandos, el motor del repaso, el cronómetro).

Para armar los HTML autocontenidos, que incrustan la hoja, las utilidades, el logo y las imágenes:

```bash
cd fuentes/laboratorios
python build_labs.py           # todos
python build_labs.py 2         # solo el laboratorio 2
```

Las imágenes del laboratorio 2 —el escudo cifrado en ECB y en CTR— se regeneran con:

```bash
python gen_media.py
```

**Nota:** el archivo de datos del laboratorio 1 (la clave de sus ejercicios) no está en el repositorio; se distribuye por separado a los docentes. Los otros cinco laboratorios no tienen clave: las respuestas surgen del cálculo.

## Presentaciones

Los decks se generan con `python-pptx` a partir de `sesionN.py`, que usan la biblioteca de plantillas `deck_lib.py`:

```bash
cd fuentes/presentaciones
python sesion1.py              # produce SIO0010-S1-*.pptx
```

Herramientas de control de calidad:

- `qa_deck.py` — detecta solapes, desbordes de texto e invasión del pie de página.
- `siglas.py` — comprueba que toda sigla del cuerpo esté en el glosario del deck.
- `renumerar.py` — renumera las cejas de sección.

## Requisitos

```bash
pip install python-pptx pillow cryptography
```
