# SIO0010 · Técnicas Criptográficas

Material del módulo **Técnicas Criptográficas** de la **Especialización en Seguridad de la Información de las Organizaciones**, Facultad de Ingeniería de la **Institución Universitaria de Envigado**.

El módulo se dicta sobre un caso de estudio continuo —**Coopaburrá**, una cooperativa financiera ficticia— y se organiza en seis encuentros de cinco horas. Cada encuentro tiene un laboratorio que ataca un hallazgo concreto del caso, y todo el trabajo alimenta un único producto final: un informe de aseguramiento criptográfico.

> **Sitio del curso:** los laboratorios se abren con un clic en
> **https://andresdapena81.github.io/sio0010-tecnicas-criptograficas/**

---

## Cómo se usan los laboratorios

Los laboratorios son **archivos HTML autocontenidos**. Se descargan y se abren con doble clic en cualquier navegador moderno.

- **No requieren conexión a internet.** Todos los cálculos ocurren en el navegador.
- **No instalan nada** y **no envían información a ningún servidor.**
- Las partes que sí necesitan la máquina —OpenSSL, Python— traen los comandos listos, con botón de copiar.

Para descargar un laboratorio: entren al archivo en la carpeta [`laboratorios/`](laboratorios/), pulsen el botón **Download raw file**, y ábranlo. También se pueden imprimir a PDF desde el navegador (Ctrl+P): la hoja de impresión está preparada para eso.

| # | Laboratorio | Sesión | Ataca |
|---|-------------|--------|-------|
| 1 | Demostraciones y ejercicios · cifrados clásicos, modos y entropía | 1 | H8 |
| 2 | Modos de operación y la línea de Coopaburrá | 2 | H3, H4 |
| 3 | Auditar la evidencia B · resúmenes y contraseñas | 3 | H1, H2 |
| 4 | Firmar, verificar y medir · firma digital | 4 | H2, H7 |
| 5 | Inspeccionar, construir y romper una cadena · certificados | 5 | H5 |
| 6 | Repartir, rotar y tokenizar · gestión de llaves | 6 | H6, H7 |

---

## Qué hay en cada carpeta

- **[`laboratorios/`](laboratorios/)** — los seis laboratorios, en HTML. Es lo que usa el estudiante.
- **[`caso/`](caso/)** — el caso de estudio Coopaburrá y su anexo técnico, en PDF. El caso se lee antes de la sesión 1; el anexo trae la evidencia técnica por sistema que alimenta el inventario.
- **[`guias/`](guias/)** — la guía de la primera entrega del informe: cómo construir el inventario criptográfico.
- **[`presentaciones/`](presentaciones/)** — los seis decks de las sesiones, en PowerPoint y en PDF.
- **[`fuentes/`](fuentes/)** — los generadores del material, para quien quiera reconstruirlo o adaptarlo. Ver [`fuentes/README.md`](fuentes/README.md).

---

## Requisitos para las partes en máquina

Los laboratorios corren solos en el navegador. Para los ejercicios de línea de comandos hace falta:

- **OpenSSL 3** (viene con Git para Windows, con macOS y con cualquier Linux).
- **Python 3.10 o superior.** Desde la sesión 2 se usa la librería `cryptography`; en la sesión 6, además, `pycryptodome`:

```bash
pip install cryptography pycryptodome
```

---

## Sobre el caso

**Coopaburrá no existe.** Es un caso construido para este módulo. Las cifras, personas, proveedores y documentos son verosímiles y están inspirados en situaciones frecuentes del sector, pero no corresponden a ninguna entidad, empresa ni persona real. Las cédulas que aparecen en los ejercicios son inventadas.

---

## Créditos y licencia

Material docente de la Institución Universitaria de Envigado, Facultad de Ingeniería.
Autor: Jorge Andrés Dapena Ossa.

Publicado bajo licencia **Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)**. Se puede usar, adaptar y redistribuir citando la fuente y manteniendo la misma licencia. Ver [`LICENSE`](LICENSE).

El escudo y el nombre de la Institución Universitaria de Envigado son marcas de la Institución y no quedan cubiertos por la licencia del material.
