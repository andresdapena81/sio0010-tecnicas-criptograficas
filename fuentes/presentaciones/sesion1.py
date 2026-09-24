# -*- coding: utf-8 -*-
"""SIO0010 · Sesión 1 (martes) — Bloques 1 y 2."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_lib import *

LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media", "image-1-1.png")
p = nueva(LOGO, LOGO)
n = 0
def sig():
    global n; n += 1; return n

# ───────────────────────── 01 PORTADA ─────────────────────────
sig()
portada(p,
    "SESIÓN 1 DE 6 · 5 HORAS · BLOQUE 1: 2H15 · DESCANSO 30 MIN · BLOQUE 2: 2H15",
    ["TÉCNICAS", "CRIPTOGRÁFICAS"],
    "COOPABURRÁ CIFRA EL DISCO, EL CANAL Y LOS RESPALDOS. ¿POR QUÉ NO PUEDE PROBAR NADA?",
    "SIO0010 · Técnicas Criptográficas · Especialización en Seguridad de la Información de las Organizaciones · "
    "Facultad de Ingeniería · Institución Universitaria de Envigado")

# ───────────────────── SECCIÓN 01 · ENCUADRE ──────────────────
seccion(p, "01", "ENCUADRE DEL MÓDULO", "Qué vamos a hacer en seis sesiones, qué no, y cómo se evalúa", sig())

s, y = base(p, "// 01  AGENDA", "AGENDA DE LA SESIÓN", sig())
y = intro(s, y, "Cinco horas en dos bloques. El primero fija el lenguaje y las reglas del oficio; el segundo ataca "
                "la pieza de la que todo depende y que casi nadie mira: la llave.")
tabla(s, y, ["BLOQUE", "MINUTOS", "CONTENIDO", "MODALIDAD"], [
    [("Bloque 1", {"bold": True}), "0 – 45", "Encuadre del módulo, del caso y de la evaluación", "Magistral"],
    ["", "45 – 90", "Vocabulario, los cuatro servicios y el ejercicio relámpago", "Magistral y taller"],
    ["", "90 – 135", "Las reglas del oficio, los modelos de ataque y la vida útil del secreto", "Magistral"],
    [("Descanso", {"bold": True, "color": NARANJA}), "30", "", ""],
    [("Bloque 2", {"bold": True}), "0 – 50", "La llave: entropía, generadores y dos catástrofes reales", "Magistral y demostración"],
    ["", "50 – 95", "De César a AES: sustitución, transposición, Enigma y el cuaderno de un solo uso", "Magistral"],
    ["", "95 – 125", "Laboratorio 1, con ejercicio en Python", "Laboratorio"],
    ["", "125 – 135", "Cierre, entrega y trabajo independiente", "Magistral"],
], [1.1, 1.0, 4.4, 1.4], alto_fila=0.40)

s, y = base(p, "// 02  META", "AL FINAL DE ESTA SESIÓN PODRÁS…", sig())
pasos(s, y + 0.10, [
    ("Distinguir los cuatro servicios y decir cuál falla en un caso concreto",
     "Confidencialidad, integridad, autenticidad y no repudio no son sinónimos, y confundirlos es el error que explica el caso de Coopaburrá."),
    ("Explicar por qué un algoritmo correcto puede dejar a una organización indefensa",
     "HMAC-SHA256 no está roto. La aplicación de Coopaburrá lo usa. Y aun así cualquiera puede firmar operaciones."),
    ("Evaluar si una llave es una llave de verdad",
     "De dónde salió, cuánta entropía tiene, quién la conoce y cuánto tiempo va a seguir sirviendo."),
    ("Reconocer por qué fracasan los cifrados clásicos y por qué eso todavía importa",
     "Los errores de 1863 se siguen cometiendo en 2026, solo que con nombres nuevos."),
    ("Levantar el inventario criptográfico de una organización",
     "Es el hallazgo H8 del caso, la primera entrega del producto y lo que Coopaburrá no tenía."),
])

s, y = base(p, "// 03  DESLINDE", "LO QUE NO VAMOS A VER AQUÍ, Y POR QUÉ", sig())
y = intro(s, y, "Un módulo de dos créditos obliga a escoger. Estas exclusiones son deliberadas y conviene decirlas "
                "en voz alta el primer día para que nadie espere algo que no va a llegar.")
tarjetas(s, y, [
    ("// NO VAMOS A ESCRIBIR ALGORITMOS DESDE CERO", [
        "Nadie en su vida profesional va a escribir AES. Sí lo van a elegir, implementar con librerías estándar, configurar y auditar, que es más difícil y menos enseñado.",
        "Por eso cada laboratorio incluye un ejercicio en Python: implementar, medir y analizar."]),
    ("// NO VAMOS A HACER CRIPTOANÁLISIS MATEMÁTICO", [
        "Romper RSA es un curso de maestría. Sí vamos a ver los fundamentos: aritmética modular, factorización y logaritmo discreto, con números pequeños.",
        "Y sobre todo, a reconocer cuándo un sistema es vulnerable por cómo está usado, que es de donde vienen casi todas las fallas."]),
    ("// NO VAMOS A VER CADENA DE BLOQUES NI MONEDAS DIGITALES", [
        "Usan criptografía, pero el problema que resuelven no es el de Coopaburrá.",
        "Si alguien quiere profundizar, se puede orientar como lectura independiente."]),
    ("// NO VAMOS A REPETIR GESTIÓN DE RIESGOS NI MARCO LEGAL", [
        "Ustedes ya vieron los dos módulos, y conmigo.",
        "Los vamos a usar todo el tiempo como herramienta: para priorizar hallazgos y para sustentar el valor probatorio. Pero no los vamos a explicar otra vez."]),
], alto=1.86)

s, y = base(p, "// 04  PUENTE", "DE DÓNDE VIENEN USTEDES", sig())
y = intro(s, y, "Este módulo no arranca en cero. Arranca sobre dos cosas que ya construyeron, y las va a usar "
                "desde la primera entrega.")
y = dos_columnas(s, y + 0.05,
    ("// LO QUE TRAEN DE GESTIÓN DE RIESGOS", [
        "Saben identificar un activo de información, valorarlo y estimar el riesgo sobre él.",
        "Saben que un control se justifica por el riesgo que reduce, no por lo moderno que suene.",
        "En este módulo, la criptografía es exactamente eso: un control. Y como todo control, se prioriza."]),
    ("// LO QUE TRAEN DE MARCO LEGAL", [
        "Conocen la Ley 1273, la Ley 1581 y el régimen de protección de datos.",
        "Saben qué es un deber de custodia y qué consecuencias tiene incumplirlo.",
        "Aquí agregamos la pieza que faltaba: la Ley 527 y el valor probatorio de lo que se firma electrónicamente."]),
    alto=2.10)
nota(s, y, "// LA CONSECUENCIA PRÁCTICA",
     "Cuando lleguen a la hoja de ruta de Coopaburrá, nadie les va a enseñar a priorizar: ya saben. Lo que este "
     "módulo agrega es el criterio técnico para saber qué tan grave es cada hallazgo y cuánto cuesta arreglarlo.")

s, y = base(p, "// 05  EVALUACIÓN", "CÓMO SE EVALÚA ESTE MÓDULO", sig())
y = intro(s, y, "Una sola nota de 0.0 a 5.0, con 3.5 como mínimo aprobatorio, compuesta por los tres tipos que "
                "exige la carta descriptiva del módulo.")
y = tabla(s, y, ["TIPO", "PESO", "INSTRUMENTOS", "CUÁNDO"], [
    [("De conocimiento", {"bold": True}), "30 %", "Dos evaluaciones cortas sobre contenido", "Sesiones 3 y 6"],
    [("De desempeño", {"bold": True}), "30 %", "Seis laboratorios, 5 % cada uno. Se evalúa la ejecución y el análisis, no el resultado", "Todas"],
    [("De producto", {"bold": True}), "40 %", "Informe de aseguramiento criptográfico de Coopaburrá, 30 %, y su sustentación, 10 %", "Por partes"],
], [1.5, 0.8, 5.4, 1.3])
nota(s, y, "// LA REGLA QUE MÁS IMPORTA",
     "El informe se construye por partes a lo largo de las seis sesiones y cada parte se realimenta antes de la "
     "siguiente. No existe la opción de escribirlo el último fin de semana: las entregas parciales tienen fecha.")

s, y = base(p, "// 06  RUTA", "LAS SEIS SESIONES DE UN VISTAZO", sig())
tabla(s, y, ["SESIÓN", "TEMA", "HALLAZGO DEL CASO", "ENTREGA"], [
    [("1 · hoy", {"bold": True}), "Servicios, reglas del oficio y la llave", "H8 · No hay inventario", "—"],
    ["2", "Cifrado simétrico y sus errores clásicos", "H3 y H4 · Disco y respaldos", "Parte 1 · Inventario"],
    ["3", "Resúmenes, autenticación de mensajes y contraseñas", "H1 y H2 · Contraseñas y firma", "Parte 2 · Datos en reposo"],
    ["4", "Llave pública, curvas elípticas y firma digital", "H2 y H7 · No repudio", "Parte 3 · Contraseñas y firma"],
    ["5", "Certificados, infraestructura de llave pública y canal seguro", "H5 · Autoridad interna", "Parte 4 · Certificados y llaves"],
    ["6", "Gestión de llaves, Ley 527, post-cuántica y sustentación", "H6 y H7 · Cajeros e hipotecas", "Partes 5 y 6 · Hoja de ruta"],
], [0.9, 4.0, 2.6, 2.3], alto_fila=0.44)

# ───────────────────── SECCIÓN 02 · EL CASO ───────────────────
seccion(p, "02", "EL CASO Y LA PREGUNTA",
        "Coopaburrá · Treinta y ocho transferencias que nadie puede probar", sig())

s, y = base(p, "// 07  EL CASO", "COOPABURRÁ", sig())
y = intro(s, y, [[("Cooperativa financiera de Itagüí", {"bold": True}),
                  (", nacida en 1978 como fondo de empleados de las textileras y vigilada por la Superintendencia "
                   "Financiera desde 1997. Es la organización sobre la que ustedes trabajan durante los seis "
                   "encuentros. Todos los artefactos que produzcan se refieren a ella.", {})]])
y = cifras(s, y, [
    ("142.000", "ASOCIADOS", "ACTIVOS", False),
    ("$1,4 B", "EN ACTIVOS", "ADMINISTRADOS", False),
    ("32", "CAJEROS", "PROPIOS", False),
    ("20", "AÑOS DEL CRÉDITO", "MÁS LARGO", True),
    ("0", "INVENTARIO DE", "LLAVES", True),
])
tarjetas(s, y, [
    ("// LO QUE LA ORGANIZACIÓN SÍ TIENE", [
        "Criptografía en todas partes: cifrado de disco en los servidores, canal cifrado en el portal, respaldos cifrados, llaves en los 32 cajeros y firma de operaciones en la aplicación móvil.",
        "Una política de seguridad aprobada en 2019 que ordena cifrar."]),
    ("// LO QUE LA ORGANIZACIÓN NO TIENE", [
        "Ningún inventario de llaves ni de certificados. Ningún custodio designado. Ninguna ceremonia documentada.",
        "Ninguna forma de demostrar que un registro no fue alterado.",
        "Ningún responsable de seguridad de la información: la función la ejerce de hecho el Jefe de Infraestructura."]),
], alto=2.00)

s, y = base(p, "// 08  EL INCIDENTE", "LA CRONOLOGÍA DE OCHO SEMANAS", sig())
tabla(s, y, ["FECHA", "QUÉ PASÓ"], [
    [("12 de enero", {"bold": True}), "Una asociada reclama una transferencia de $1.850.000 que no hizo. Se radica como reclamo ordinario."],
    [("19 de enero", {"bold": True}), "Van nueve reclamos. Todos de la aplicación móvil. Todas las transferencias salieron hacia tres cuentas de otra entidad."],
    [("23 de enero", {"bold": True}), "Los registros muestran las operaciones como correctamente autenticadas. Ninguna alerta se disparó."],
    [("27 de enero", {"bold": True}), "El proveedor informa que la aplicación firma con una clave incrustada en el código, igual para todos los usuarios."],
    [("30 de enero", {"bold": True}), "Se bloquean las transferencias externas por la aplicación. En plena quincena."],
    [("2 de febrero", {"bold": True}), "38 reclamos por $71.400.000. Se reintegra el dinero. Cuatro asociados demandan de todos modos."],
    [("5 de febrero", {"bold": True}), "El apoderado pregunta cómo se prueba que las operaciones no las hizo el titular. Nadie sabe responder."],
    [("9 de febrero", {"bold": True}), "El comité ordena un diagnóstico criptográfico completo. Ahí entran ustedes."],
], [1.3, 8.0], alto_fila=0.40)

s, y = base(p, "// 09  EVIDENCIA", "EL CORREO QUE EXPLICA TODO EL CASO", sig())
y = intro(s, y, "Documento 2 del expediente. Correo de la fábrica de software, 27 de enero de 2026.")
y = bloque_codigo(s, y, [
    "«…confirmamos que el esquema de firma de operaciones utiliza HMAC-SHA256 con una clave",
    "compartida provisionada en tiempo de compilación. Esta decisión se tomó en 2023 de común",
    "acuerdo para evitar el costo de una infraestructura de llave pública y agilizar la salida",
    "a producción. El alcance contratado no incluía gestión de llaves…»",
], titulo="CORREO DE BITLAB S.A.S. · 27 DE ENERO DE 2026")
y = dos_columnas(s, y,
    ("// LO QUE ESTÁ BIEN", [
        "HMAC-SHA256 es un mecanismo correcto, moderno y ampliamente recomendado.",
        "No está roto. No hay ningún ataque práctico contra él.",
        "Si ustedes auditaran solo el algoritmo, este sistema pasaría."]),
    ("// LO QUE ESTÁ ROTO", [
        "La llave es una sola para los 142.000 asociados.",
        "Viaja dentro del paquete que cualquiera descarga de la tienda de aplicaciones.",
        "Lleva ahí desde marzo de 2023 y nunca se ha cambiado.",
        "No hay forma de saber cuál usuario firmó qué."]),
    alto=1.95)

s, y = base(p, "// 10  EVIDENCIA", "LA POLÍTICA DE CIFRADO, COMPLETA", sig())
y = intro(s, y, "Documento 3 del expediente. No es un extracto: es el artículo 14 íntegro de la Política de "
                "Seguridad de la Información aprobada en 2019 y vigente el día del incidente.")
y = bloque_codigo(s, y, [
    "«Artículo 14. Cifrado. Toda información confidencial de la Cooperativa deberá ser cifrada",
    "en reposo y en tránsito utilizando algoritmos de reconocida robustez. La Jefatura de",
    "Infraestructura velará por el cumplimiento de esta disposición.»",
], titulo="POLÍTICA DE SEGURIDAD DE LA INFORMACIÓN · 2019 · ARTÍCULO 14")
nota(s, y, "// POR QUÉ ESTA POLÍTICA NO SIRVE",
     "No dice qué algoritmos. No dice qué longitudes de llave. No dice quién custodia las llaves. No dice cada "
     "cuánto se rotan. No dice qué pasa cuando el custodio se va de la organización. No dice cómo se verifica el "
     "cumplimiento. Es una política que no se puede auditar, y por lo tanto no se puede incumplir: no hay contra "
     "qué contrastarla.", alto=1.30)

s, y = base(p, "// 11  EVIDENCIA", "EL INVENTARIO DE LLAVES, ÍNTEGRO", sig())
y = intro(s, y, "Documento 5. Esto es todo lo que Infraestructura pudo entregar cuando el comité pidió el "
                "inventario criptográfico, el 11 de febrero.")
y = bloque_codigo(s, y, [
    "Certificado del portal (vence en junio).",
    "Llaves de cajeros (las cargó el proveedor).",
    "Llave de respaldos (está en el servidor).",
    "Certificado del correo (lo renueva el proveedor de correo).",
    "Pendiente confirmar si la aplicación móvil usa llaves.",
], titulo="CORREO DE LA JEFATURA DE INFRAESTRUCTURA · 11 DE FEBRERO DE 2026")
nota(s, y, "// LA MAGNITUD",
     "Cinco líneas escritas en un correo. Ese es el inventario criptográfico completo de una entidad vigilada por "
     "la Superintendencia Financiera que administra 142.000 asociados y 1,4 billones de pesos. La última línea —"
     "«pendiente confirmar si la aplicación móvil usa llaves»— se refiere al canal donde ocurrió el fraude.",
     alto=1.20)

s, y = base(p, "// 12  MÉTODO", "CÓMO SE CONSTRUYE UN INVENTARIO CRIPTOGRÁFICO", sig(), titulo_tam=22)
y = intro(s, y, "Nadie tiene la lista completa: el inventario se arma cruzando fuentes, y cada una revela algo distinto.")
y = tabla(s, y, ["FUENTE", "QUÉ REVELA", "SU LÍMITE"], [
    [("Barrido de certificados y del canal seguro", {"bold": True}), "Versiones, suites, emisores y vencimientos de todo lo que expone un puerto", "Solo ve lo que está en la red"],
    [("Revisión de configuraciones y guiones", {"bold": True}), "Algoritmos, modos y dónde se guarda cada llave", "Exige acceso y saber leerlas"],
    [("Búsqueda en el código y los repositorios", {"bold": True, "color": NARANJA}), "Llaves escritas en el código, constantes y bibliotecas usadas", "Solo lo que se tiene en fuentes"],
    [("Consolas de llaves y módulos de hardware", {"bold": True}), "Qué llaves existen formalmente y quién puede usarlas", "Solo lo que ya se gestiona bien"],
    [("Entrevistas y contratos con proveedores", {"bold": True}), "Lo que ninguna herramienta ve: quién custodia qué y desde cuándo", "Depende de la memoria de las personas"],
], [3.6, 4.2, 2.2], alto_fila=0.48)
nota(s, y, "// LA REGLA DEL INVENTARIO",
     "Ninguna fuente basta sola, y <b>las contradicciones entre fuentes son hallazgos</b>: la sal declarada que no "
     "aparece en los datos, por ejemplo. Es exactamente lo que van a encontrar en la sesión 3.", alto=0.78)

tesis(p, "// LA TESIS DE LA SESIÓN",
      ["EL ALGORITMO DE COOPABURRÁ", "ESTABA BIEN ESCOGIDO.", "LO QUE NADIE ADMINISTRÓ", "FUE LA LLAVE."],
      "Ese es el patrón de casi todas las fallas criptográficas reales, y es el hilo de las seis sesiones. "
      "La criptografía moderna casi nunca se rompe por matemáticas: se rompe por generación de llaves predecible, "
      "por llaves compartidas donde debía haber llaves individuales, por llaves que nunca se rotan y por llaves "
      "guardadas al lado de lo que protegen. Hoy vamos a aprender a mirar ese lado del problema.", sig())

# ───────────── SECCIÓN 03 · LOS CUATRO SERVICIOS ──────────────
seccion(p, "03", "QUÉ PROMETE LA CRIPTOGRAFÍA",
        "Cuatro servicios distintos que no se sustituyen entre sí", sig())

s, y = base(p, "// 13  VOCABULARIO", "EL VOCABULARIO MÍNIMO DEL MÓDULO", sig())
y = intro(s, y, "Seis sesiones hablando de lo mismo exigen usar las palabras con precisión. Estas son las que se usan "
                "en todo el módulo y el sentido exacto en que se usan: la mitad de los malentendidos de una "
                "auditoría empiezan aquí.")
y = tabla(s, y, ["TÉRMINO", "QUÉ SIGNIFICA AQUÍ", "EJEMPLO EN EL CASO"], [
    [("Texto claro y texto cifrado", {"bold": True}), "El dato legible, y el mismo dato después de cifrarlo. Al cifrado también se le llama criptograma", "El volcado de la base antes y después del guion de respaldo"],
    [("Algoritmo o cifra", {"bold": True}), "El procedimiento. Se publica y se estudia: por Kerckhoffs, no es secreto", "AES-256 en el respaldo, SHA-1 en las contraseñas"],
    [("Llave", {"bold": True, "color": NARANJA}), "El único dato secreto. Toda la seguridad descansa en ella", "La del respaldo, guardada en un archivo de texto al lado"],
    [("Espacio de llaves", {"bold": True}), "Cuántas llaves posibles admite el algoritmo. Se expresa en bits", "256 bits en el respaldo: tamaño correcto, custodia pésima"],
    [("Criptografía, criptoanálisis y criptología", {"bold": True}), "Diseñar sistemas; atacarlos; y la disciplina que abarca las dos", "Este módulo es criptografía aplicada con criterio de criptoanalista"],
    [("Ataque", {"bold": True}), "Cualquier forma de obtener lo protegido sin tener la llave, no solo probar llaves", "Descompilar la aplicación para sacar la llave de firma"],
], [2.8, 4.3, 3.9], alto_fila=0.42)

s, y = base(p, "// 14  VOCABULARIO", "CODIFICAR, CIFRAR, RESUMIR Y FIRMAR NO SON LO MISMO", sig(), titulo_tam=22)
y = intro(s, y, "Cuatro operaciones que transforman datos y que se confunden todo el tiempo, incluso en informes de "
                "auditoría. La diferencia está en tres preguntas: si usan llave, si se pueden revertir y qué "
                "garantizan.")
y = tabla(s, y, ["OPERACIÓN", "¿USA LLAVE?", "¿SE PUEDE REVERTIR?", "QUÉ GARANTIZA"], [
    [("Codificar · Base64, hexadecimal", {"bold": True}), "No", "Sí: cualquiera, sin ningún secreto", "Nada. Solo cambia la representación para que el dato viaje o se almacene"],
    [("Cifrar", {"bold": True}), "Sí", "Sí, pero solo quien tiene la llave", "Confidencialidad"],
    [("Resumir", {"bold": True}), "No", "No: es de un solo sentido", "Integridad, siempre que el resumen mismo esté protegido"],
    [("Firmar", {"bold": True, "color": NARANJA}), "Sí, la privada", "No se revierte: se verifica con la pública", "Autenticidad y no repudio"],
], [2.9, 1.5, 2.8, 3.8], alto_fila=0.50)
nota(s, y, "// EL HALLAZGO QUE APARECE EN CASI TODA AUDITORÍA",
     "Un campo en Base64 no está cifrado: cualquiera lo lee en un segundo, sin llave y sin herramientas "
     "especiales. Aparece en bases de datos, en cookies y en archivos de configuración, casi siempre junto a la "
     "frase «la contraseña está encriptada». <b>Esa frase es la primera que hay que verificar.</b>", alto=0.92)

s, y = base(p, "// 15  MARCO", "NO ES UNA PROMESA, SON CUATRO", sig())
y = intro(s, y, "«Cifrado» no significa «protegido»: la criptografía presta cuatro servicios distintos, y cada uno exige su propio mecanismo.")
tarjetas(s, y, [
    ("// CONFIDENCIALIDAD", [
        "Que solo pueda leerlo quien deba.",
        "Se consigue cifrando. Es el único de los cuatro que la mayoría de la gente asocia con la palabra criptografía.",
        "En el caso: el cifrado de disco de los servidores apunta aquí, y aun así falla (H3)."]),
    ("// INTEGRIDAD", [
        "Que se pueda detectar si fue alterado.",
        "Se consigue con funciones resumen y códigos de autenticación. Cifrar no da integridad por sí solo.",
        "En el caso: nadie puede demostrar que los registros del servidor no fueron modificados."]),
    ("// AUTENTICIDAD", [
        "Que se pueda establecer quién lo originó.",
        "Se consigue con códigos de autenticación de mensajes o con firma digital, según de qué se trate.",
        "En el caso: la aplicación autentica, pero autentica a la aplicación, no al usuario (H2)."]),
    ("// NO REPUDIO", [
        "Que el autor no pueda negar después haberlo hecho, y que un tercero pueda verificarlo.",
        "Solo se consigue con firma digital y llave privada individual. Nunca con llave compartida.",
        "En el caso: es el servicio ausente, y por eso el abogado se quedó sin respuesta."]),
], alto=2.00)

s, y = base(p, "// 16  DIFERENCIAS", "CÓMO SE CONSIGUE CADA UNO", sig())
y = tabla(s, y, ["SERVICIO", "MECANISMO", "PREGUNTA QUE RESPONDE", "SI FALTA…"], [
    [("Confidencialidad", {"bold": True}), "Cifrado simétrico o asimétrico", "¿Quién puede leerlo?", "Cualquiera que acceda al dato lo entiende"],
    [("Integridad", {"bold": True}), "Funciones resumen, códigos de autenticación", "¿Fue alterado?", "No se puede distinguir el original de la copia manipulada"],
    [("Autenticidad", {"bold": True}), "Códigos de autenticación o firma digital", "¿Quién lo originó?", "Cualquiera puede hacerse pasar por otro"],
    [("No repudio", {"bold": True}), "Firma digital con llave privada individual", "¿Puede negarlo después?", "No hay prueba oponible ante un tercero"],
], [1.7, 3.0, 2.6, 3.1], alto_fila=0.50)
nota(s, y, "// EL ERROR MÁS CARO DE LA TABLA",
     "El código de autenticación de mensajes da autenticidad, pero no da no repudio, porque las dos partes "
     "comparten la misma llave: cualquiera de las dos pudo haber generado el mensaje. La firma digital sí lo da, "
     "porque la llave privada la tiene una sola persona. Coopaburrá eligió lo primero y necesitaba lo segundo.")

s, y = base(p, "// 17  TALLER", "EJERCICIO RELÁMPAGO: ¿QUÉ SERVICIO FALLÓ?", sig())
y = intro(s, y, "Seis situaciones. Tres minutos en parejas. Para cada una, digan cuál de los cuatro servicios "
                "falló. Ojo: en algunas falló más de uno, y en una de ellas no falló ninguno.")
tabla(s, y, ["N.°", "SITUACIÓN"], [
    [("1", {"bold": True, "color": NARANJA}), "Un proveedor recibe un correo, aparentemente del gerente, pidiendo cambiar la cuenta bancaria para el próximo pago. Lo hace. El dinero se pierde."],
    [("2", {"bold": True, "color": NARANJA}), "Un disco duro con la base de datos de clientes se pierde en un taxi. Estaba cifrado con una llave que solo conoce el área de sistemas."],
    [("3", {"bold": True, "color": NARANJA}), "Una factura electrónica llega con el valor modificado. El emisor jura que envió otro valor y no hay forma de saber quién tiene razón."],
    [("4", {"bold": True, "color": NARANJA}), "Un empleado descarga la lista de salarios desde la base de datos de nómina, a la que tiene acceso legítimo de lectura."],
    [("5", {"bold": True, "color": NARANJA}), "Un cliente niega haber autorizado una transferencia. El banco muestra el registro del sistema. El cliente responde que ese registro lo hizo el banco."],
    [("6", {"bold": True, "color": NARANJA}), "Alguien intercepta el tráfico entre la aplicación y el servidor. Va cifrado con TLS 1.3 y no logra leer nada."],
], [0.7, 9.3], alto_fila=0.52)

s, y = base(p, "// 18  TALLER", "RESPUESTAS Y POR QUÉ", sig())
tabla(s, y, ["N.°", "SERVICIO QUE FALLÓ", "POR QUÉ"], [
    [("1", {"bold": True, "color": NARANJA}), ("Autenticidad", {"bold": True}), "El correo no estaba firmado. No hay forma de establecer quién lo originó. Es el fraude más común del país y no se resuelve cifrando."],
    [("2", {"bold": True, "color": NARANJA}), ("Ninguno", {"bold": True, "color": NARANJA}), "La confidencialidad se mantuvo. Es la respuesta incómoda: aquí la criptografía funcionó. Lo que hay es un problema de custodia, no criptográfico."],
    [("3", {"bold": True, "color": NARANJA}), ("Integridad y no repudio", {"bold": True}), "No se detecta la alteración ni se puede probar quién dice la verdad. Es exactamente el escenario de la Ley 527."],
    [("4", {"bold": True, "color": NARANJA}), ("Ninguno", {"bold": True, "color": NARANJA}), "El acceso era legítimo. Ningún mecanismo criptográfico detiene a quien tiene permiso. Es control de acceso, no criptografía."],
    [("5", {"bold": True, "color": NARANJA}), ("No repudio", {"bold": True}), "El registro lo produce una sola parte, así que no es oponible. Es, literalmente, el caso Coopaburrá."],
    [("6", {"bold": True, "color": NARANJA}), ("Ninguno", {"bold": True, "color": NARANJA}), "Funcionó la confidencialidad en tránsito. Sirve para recordar que la criptografía sí hace bien su trabajo cuando está bien puesta."],
], [0.7, 2.3, 7.0], alto_fila=0.54)

s, y = base(p, "// 19  APLICACIÓN", "LOS CUATRO SERVICIOS EN COOPABURRÁ", sig())
y = intro(s, y, "Este cuadro es el esqueleto de la primera parte del informe. Consérvenlo.")
tabla(s, y, ["SERVICIO", "¿LO TIENE?", "EVIDENCIA EN EL CASO", "HALLAZGO"], [
    [("Confidencialidad", {"bold": True}), ("Parcial", {"bold": True, "color": NARANJA}), "Cifrado de disco que solo protege con el servidor apagado; datos en claro en la base con el servidor encendido", "H3, H4"],
    [("Integridad", {"bold": True}), ("No", {"bold": True, "color": NARANJA}), "Los registros del servidor pueden modificarse sin dejar rastro. Esa fue la pregunta del abogado", "H8"],
    [("Autenticidad", {"bold": True}), ("Aparente", {"bold": True, "color": NARANJA}), "La aplicación firma, pero con llave compartida: autentica al programa, no a la persona", "H2"],
    [("No repudio", {"bold": True}), ("No", {"bold": True, "color": NARANJA}), "Ninguna llave privada individual. Ningún sello de tiempo. Ninguna entidad de certificación", "H2, H7"],
], [1.7, 1.3, 6.2, 1.2], alto_fila=0.58)

# ──────────── SECCIÓN 04 · LAS REGLAS DEL OFICIO ──────────────
s, y = base(p, "// 20  MAPA", "DÓNDE VIVE LA CRIPTOGRAFÍA EN UNA ORGANIZACIÓN", sig(), titulo_tam=22)
y = intro(s, y, "Casi toda organización usa criptografía en más lugares de los que cree. Este mapa es el punto de partida de la entrega 1.")
y = tabla(s, y, ["DÓNDE", "QUÉ SERVICIO PRESTA", "QUIÉN SUELE SABERLO EN COOPABURRÁ"], [
    [("Portal, aplicación y correo", {"bold": True}), "Confidencialidad e integridad en tránsito", "Infraestructura, a medias"],
    [("Discos, bases de datos y respaldos", {"bold": True}), "Confidencialidad en reposo", "Quien lo configuró, si sigue en la empresa"],
    [("Contraseñas y sesiones", {"bold": True}), "Autenticación", "La fábrica de software"],
    [("Operaciones de la aplicación", {"bold": True}), "Autenticidad e integridad de cada transferencia", "La fábrica de software"],
    [("Cajeros y medios de pago", {"bold": True}), "Confidencialidad del PIN y autenticación del equipo", "El fabricante y dos personas de 2019"],
    [("Documentos firmados", {"bold": True, "color": NARANJA}), "Integridad y no repudio", "Nadie: hoy es una imagen escaneada"],
    [("Redes privadas con sedes y proveedores", {"bold": True}), "Confidencialidad entre sitios", "Redes, sin inventario"],
], [3.4, 3.6, 3.0], alto_fila=0.40)
nota(s, y, "// LA COLUMNA QUE MÁS IMPORTA",
     "La tercera. <b>Donde la respuesta es «nadie» o «alguien que ya se fue», hay un hallazgo antes de mirar un solo "
     "algoritmo</b>, y la entrega 1 tiene que decirlo con nombre y cargo.", alto=0.72)

s, y = base(p, "// 21  LÍMITE", "LO QUE LA CRIPTOGRAFÍA NO PUEDE HACER", sig())
y = intro(s, y, "Antes de las reglas del oficio conviene marcar el límite. La criptografía es un control poderoso y "
                "estrecho, y sobrevenderla es la forma más común de dejar huecos en un diseño.")
y = tarjetas(s, y, [
    ("// NO GARANTIZA DISPONIBILIDAD", [
        "Cifrar no evita que un sistema se caiga ni que lo tumben.",
        "El secuestro de datos usa criptografía impecable contra su dueño: la mejor prueba de que el algoritmo no sabe de quién es el dato."]),
    ("// NO PROTEGE UN EXTREMO COMPROMETIDO", [
        "Si el teléfono del asociado o el servidor están infectados, el atacante ve el dato antes de cifrarlo o después de descifrarlo.",
        "El canal cifrado llega intacto a un equipo que ya no es de confianza."]),
    ("// NO DETIENE AL USUARIO ENGAÑADO", [
        "Quien entrega su contraseña o su código en un sitio falso está autorizando al atacante con sus propias credenciales.",
        "La criptografía verifica llaves, no intenciones."]),
    ("// NO SIRVE SI LA LLAVE SE FILTRA", [
        "Con la llave correcta el sistema funciona perfecto para quien la robó, y no deja ninguna señal.",
        "Es el hallazgo H2: la llave de firma está al alcance de cualquiera que descargue la aplicación."]),
], alto=1.60)

seccion(p, "04", "LAS REGLAS DEL OFICIO",
        "Cuatro principios que llevan siglo y medio sin cambiar", sig())

s, y = base(p, "// 22  PRINCIPIO", "KERCKHOFFS, 1883", sig())
y = intro(s, y, "Auguste Kerckhoffs, lingüista neerlandés, publicó en 1883 en el Journal des sciences militaires "
                "seis requisitos para un sistema de cifra militar. El segundo se volvió el principio fundacional "
                "de toda la criptografía moderna.")
y = bloque_codigo(s, y, [
    "«El sistema no debe requerir ser secreto, y debe poder caer en manos del enemigo",
    " sin causar inconveniente.»",
], titulo="AUGUSTE KERCKHOFFS · LA CRYPTOGRAPHIE MILITAIRE · 1883")
y = dos_columnas(s, y,
    ("// LO QUE SIGNIFICA", [
        "Toda la seguridad debe descansar en la llave, no en que nadie sepa cómo funciona el mecanismo.",
        "El algoritmo se puede publicar, auditar y discutir. La llave, no."]),
    ("// POR QUÉ ES CIERTO", [
        "Los algoritmos se filtran, se descompilan y se deducen. Las personas que los conocen renuncian.",
        "Un secreto que conocen muchos y que dura años no es un secreto: es una expectativa."]),
    alto=1.55)

s, y = base(p, "// 23  CONSECUENCIA", "NO INVENTE CRIPTOGRAFÍA PROPIA", sig())
y = intro(s, y, "Es la regla más repetida del oficio y la más desobedecida. Estos son tres casos donde una "
                "organización seria decidió hacer su propio mecanismo, y el resultado.")
y = tabla(s, y, ["CASO", "QUÉ HICIERON", "CÓMO TERMINÓ"], [
    [("Cifrado de redes inalámbricas WEP", {"bold": True}), "Diseño propio sobre un algoritmo de flujo, con un vector de inicialización de solo 24 bits que se repetía", "Roto públicamente en 2001. Hoy una red con WEP se descifra en minutos con herramientas libres"],
    [("Tarjetas sin contacto MIFARE Classic", {"bold": True}), "Algoritmo propietario mantenido en secreto, usado en transporte y control de acceso en todo el mundo", "El algoritmo se dedujo por ingeniería inversa en 2008. Millones de tarjetas quedaron clonables"],
    [("Coopaburrá, 2023", {"bold": True, "color": NARANJA}), "No inventaron el algoritmo: eligieron uno correcto. Inventaron el esquema de administración de la llave", "38 transferencias no autorizadas y ninguna capacidad de probar nada"],
], [2.4, 4.0, 3.6], alto_fila=0.72)
nota(s, y, "// EL MATIZ QUE IMPORTA",
     "El tercer caso es el más instructivo porque muestra que la regla es más amplia de lo que suele enunciarse. "
     "No basta con no inventar el algoritmo: tampoco hay que inventar el protocolo, ni el esquema de llaves, ni el "
     "procedimiento de rotación. Esas partes también están estudiadas y estandarizadas.", alto=1.05)

s, y = base(p, "// 24  DIAGNÓSTICO", "ROTO FRENTE A MAL USADO", sig())
y = intro(s, y, "Cuando un sistema criptográfico falla en el mundo real, conviene saber dónde falló de verdad. "
                "Las categorías no se parecen en frecuencia.")
y = tabla(s, y, ["ORIGEN DE LA FALLA", "EJEMPLO", "FRECUENCIA REAL"], [
    [("El algoritmo es débil", {"bold": True}), "MD5 o SHA-1 para firmar, o DES", "Poco frecuente: sistemas heredados"],
    [("El algoritmo está mal configurado", {"bold": True}), "Modo inadecuado o vector repetido", "Frecuente"],
    [("La llave está mal generada", {"bold": True}), "Generador predecible, poca entropía", "Frecuente y catastrófico"],
    [("La llave está mal administrada", {"bold": True, "color": NARANJA}), "Compartida, en el código, nunca rotada", "La más frecuente. Es el caso Coopaburrá"],
    [("Se escogió el servicio equivocado", {"bold": True}), "Autenticidad donde hacía falta no repudio", "Frecuente y difícil de detectar"],
], [3.2, 3.6, 3.2], alto_fila=0.52)
nota(s, y, "// CÓMO USAR ESTO EN EL INFORME",
     "Cada hallazgo de Coopaburrá debería caer en una de estas cinco filas. La clasificación determina el tipo "
     "de solución y quién la ejecuta.", alto=0.70)

s, y = base(p, "// 25  CRITERIO", "CONTRA QUIÉN SE PROTEGE", sig())
y = intro(s, y, "No existe «seguro». Existe «seguro frente a un adversario con ciertos recursos, durante cierto "
                "tiempo». Definir el adversario es parte del diseño, y es la conversación que Coopaburrá nunca tuvo.")
y = tabla(s, y, ["ADVERSARIO", "RECURSOS", "QUÉ LO DETIENE EN EL CASO"], [
    [("Un curioso interno", {"bold": True}), "Acceso legítimo de lectura a la base de datos", "Cifrado a nivel de campo y registro de consultas. Hoy no hay ninguno de los dos"],
    [("Un atacante remoto oportunista", {"bold": True}), "Herramientas públicas, poco tiempo, busca blancos fáciles", "Canal bien configurado y contraseñas bien almacenadas. Hoy fallan ambos"],
    [("Alguien que descargó la aplicación", {"bold": True, "color": NARANJA}), "Un teléfono y un descompilador gratuito", "Llaves individuales por usuario. Hoy hay una sola llave para todos"],
    [("Un mensajero con el disco de respaldo", {"bold": True}), "Acceso físico al medio durante el traslado", "Llave separada del respaldo. Hoy viajan juntas en el mismo disco"],
    [("Un adversario con capacidad de cómputo futura", {"bold": True}), "Guarda hoy lo que podrá descifrar en diez años", "Algoritmos resistentes. Es la sesión 6, y afecta a los créditos a veinte años"],
], [3.0, 3.4, 3.6], alto_fila=0.58)

s, y = base(p, "// 26  ATAQUE", "LOS CUATRO MODELOS DE ATAQUE", sig())
y = intro(s, y, "El criptoanálisis clasifica los ataques por lo que el atacante tiene en la mano. Es terminología "
                "estándar, aparece en toda la bibliografía, y un algoritmo moderno tiene que resistir los cuatro.")
y = tabla(s, y, ["MODELO", "QUÉ TIENE EL ATACANTE", "DÓNDE APARECE EN EL CASO"], [
    [("Solo texto cifrado", {"bold": True}), "Únicamente mensajes cifrados", "Quien se lleve el disco de respaldo que viaja cada semana a Sabaneta"],
    [("Texto claro conocido", {"bold": True}), "Pares de mensaje y cifrado que él no escogió", "Cada respaldo nocturno empieza con el mismo encabezado de volcado"],
    [("Texto claro elegido", {"bold": True}), "Puede hacer cifrar lo que quiera y ver el resultado", "Cualquier asociado hace una transferencia y observa el código que la acompaña"],
    [("Texto cifrado elegido", {"bold": True, "color": NARANJA}), "Puede hacer descifrar lo que quiera y observar cómo reacciona el sistema", "Un servidor que responde distinto cuando el relleno está mal: el ataque de la sesión 2"],
], [2.6, 3.6, 3.8], alto_fila=0.52)
nota(s, y, "// POR QUÉ IMPORTA EL ÚLTIMO",
     "Un esquema que resiste el ataque de texto cifrado elegido resiste los otros tres. <b>Es el mínimo que se le "
     "exige hoy a cualquier cifrado</b>, y es la razón por la que la sesión 2 termina recomendando cifrado "
     "autenticado por defecto.", alto=0.85)

s, y = base(p, "// 27  ESCALA", "QUÉ SIGNIFICA «COMPUTACIONALMENTE INVIABLE»", sig(), titulo_tam=22)
y = intro(s, y, "La seguridad moderna no promete imposibilidad: promete que el ataque cuesta más tiempo del que "
                "existe. Conviene ver los números una vez, porque cambian la intuición para siempre.")
y = tabla(s, y, ["LLAVE", "LLAVES POSIBLES", "GRUPO CRIMINAL · 10¹² POR SEGUNDO", "UN ESTADO · 10¹⁸ POR SEGUNDO"], [
    [("56 bits · DES", {"bold": True}), "7,2 × 10¹⁶", "20 horas", "0,07 segundos"],
    [("80 bits", {"bold": True}), "1,2 × 10²⁴", "38.000 años", "14 días"],
    [("112 bits", {"bold": True}), "5,2 × 10³³", "1,6 × 10¹⁴ años", "164 millones de años"],
    [("128 bits · AES-128", {"bold": True, "color": NARANJA}), "3,4 × 10³⁸", "1,1 × 10¹⁹ años", "1,1 × 10¹³ años: 780 veces la edad del universo"],
    [("256 bits · AES-256", {"bold": True}), "1,2 × 10⁷⁷", "3,7 × 10⁵⁷ años", "3,7 × 10⁵¹ años"],
], [2.4, 2.1, 2.7, 2.8], alto_fila=0.42)
nota(s, y, "// LA CONCLUSIÓN PRÁCTICA",
     "De 80 a 128 bits no hay un 60 % más de seguridad: hay 2⁴⁸ veces más, unos 280 billones de veces. <b>Por eso "
     "nadie ataca AES probando llaves.</b> Se ataca la contraseña de la que salió la llave, el generador que la "
     "produjo o el lugar donde se guarda. Exactamente los hallazgos H1, H4 y H2.", alto=0.92)

s, y = base(p, "// 28  CRITERIO", "CUÁNTO TIENE QUE DURAR EL SECRETO", sig())
y = intro(s, y, "La pregunta que casi nadie hace, y que determina qué algoritmo y qué longitud de llave hacen falta.")
y = tabla(s, y, ["DATO DE COOPABURRÁ", "VIDA ÚTIL DEL SECRETO", "IMPLICACIÓN"], [
    [("Token de sesión del portal", {"bold": True}), "Minutos", "Puede usar mecanismos ligeros. Rotación constante"],
    [("Contraseña de un asociado", {"bold": True}), "Meses o años, según la política", "Exige función de derivación con factor de trabajo, no un resumen simple"],
    [("Saldo y movimientos", {"bold": True}), "Años, mientras dure la relación", "Cifrado en reposo con rotación de llaves planificada"],
    [("Historial crediticio", {"bold": True}), "Definido por la Ley 1266", "El plazo lo fija la norma, no la tecnología"],
    [("Contrato de crédito hipotecario", {"bold": True, "color": NARANJA}), "Hasta veinte años, y debe seguir siendo probatorio", "Es el dato más exigente de la organización. Determina la migración criptográfica"],
], [3.3, 3.2, 3.5], alto_fila=0.56)
nota(s, y, "// GUARDEN ESTA FILA",
     "La última fila explica la sesión 6: un crédito firmado este año vence hacia 2046 y tiene que poder probarse "
     "hasta entonces.", alto=0.72)

s, y = base(p, "// 29  CIERRE", "LO QUE LLEVAMOS DEL PRIMER BLOQUE", sig())
pasos(s, y + 0.10, [
    ("La criptografía presta cuatro servicios distintos y no intercambiables",
     "Confundir autenticidad con no repudio es lo que dejó a Coopaburrá sin respuesta ante su propio abogado."),
    ("La seguridad vive en la llave, no en el algoritmo",
     "Kerckhoffs lo escribió en 1883 y sigue siendo el criterio con el que se juzga cualquier diseño."),
    ("Las fallas reales casi nunca son matemáticas",
     "Son de configuración, de generación de llaves y, sobre todo, de administración de llaves."),
    ("No hay «seguro»: hay seguro frente a alguien, durante un tiempo",
     "Definir el adversario y la vida útil del secreto es una decisión de diseño, no un detalle."),
])
nota(s, 5.55, "// DESPUÉS DEL DESCANSO",
     "Vamos a la pieza de la que todo depende: la llave. De dónde sale, cuánta entropía necesita y qué pasa "
     "cuando se genera mal. Dos catástrofes reales y una demostración en vivo.", alto=0.95)

# ═══════════════════ BLOQUE 2 ═══════════════════
seccion(p, "05", "LA LLAVE",
        "Bloque 2 · De dónde sale, cuánta entropía necesita y qué pasa cuando se genera mal", sig())

s, y = base(p, "// 30  FUNDAMENTO", "TODO DEPENDE DE LA LLAVE", sig())
y = intro(s, y, "Si la seguridad vive en la llave, entonces la pregunta operativa de todo el oficio es cómo se "
                "produce una llave que merezca ese nombre. Hay cuatro propiedades y las cuatro son obligatorias.")
tarjetas(s, y, [
    ("// 1 · IMPREDECIBLE", [
        "Nadie debe poder adivinarla ni reproducir el proceso que la generó.",
        "Esto descarta el reloj del sistema, el número de proceso, el nombre de la empresa y el año."]),
    ("// 2 · SUFICIENTEMENTE LARGA", [
        "El espacio de búsqueda debe ser tan grande que recorrerlo sea inviable con la tecnología del adversario.",
        "128 bits de entropía real son suficientes hoy contra cualquier adversario clásico."]),
    ("// 3 · CONOCIDA POR QUIEN DEBE", [
        "Una llave compartida entre 142.000 personas no es una llave: es un dato público con retraso.",
        "Cada servicio criptográfico define cuántas partes pueden conocerla."]),
    ("// 4 · CON UN CICLO DE VIDA DEFINIDO", [
        "Se genera, se distribuye, se usa, se rota, se archiva y se destruye.",
        "Cada etapa tiene responsable. Es la sesión 6, y es lo que no existe en Coopaburrá."]),
], alto=1.80)

s, y = base(p, "// 31  CONCEPTO", "ENTROPÍA, EN UNA FRASE", sig())
y = intro(s, y, "Entropía es la medida de lo que el adversario no sabe. Se cuenta en bits, y un bit de entropía "
                "equivale a duplicar el número de posibilidades que tendría que probar.")
y = tabla(s, y, ["ORIGEN DE LA LLAVE", "ENTROPÍA REAL", "INTENTOS NECESARIOS"], [
    [("Un PIN de 4 dígitos", {"bold": True}), "Unos 13 bits", "10.000"],
    [("Una palabra del diccionario", {"bold": True}), "Unos 15 bits", "Decenas de miles"],
    [("«Cb4rr4-2023-HMAC-k3y»", {"bold": True, "color": NARANJA}), "Cero, una vez publicada", "1. Está en el paquete de la aplicación"],
    [("Contraseña humana de 8 caracteres", {"bold": True}), "Entre 25 y 30 bits en la práctica", "Cientos de millones. Horas con una tarjeta gráfica"],
    [("32 bytes de un generador criptográfico", {"bold": True}), "256 bits", "Inalcanzable con tecnología clásica"],
], [4.2, 2.6, 3.2], alto_fila=0.46)
nota(s, y, "// LA TRAMPA DE LA LONGITUD",
     "La llave de Coopaburrá tiene veinte caracteres y parece robusta, pero la entropía no la da la longitud: la da "
     "lo que el adversario no sabe. Publicada dentro de la aplicación, vale cero: <b>una llave de veinte caracteres "
     "puede valer menos que un PIN.</b>", alto=0.78)

s, y = base(p, "// 32  MECANISMO", "DOS GENERADORES QUE NO SON LO MISMO", sig())
y = dos_columnas(s, y + 0.05,
    ("// GENERADOR PSEUDOALEATORIO COMÚN", [
        "Diseñado para simulaciones, juegos y estadística. Rápido y reproducible a propósito.",
        "Si se conoce el estado interno, toda la secuencia futura y pasada queda determinada.",
        "Ejemplos típicos: las funciones de aleatoriedad por defecto de los lenguajes de programación.",
        "Nunca debe usarse para generar llaves, vectores de inicialización, tokens ni contraseñas."]),
    ("// GENERADOR CRIPTOGRÁFICO", [
        "Diseñado para que, conociendo cualquier parte de la salida, sea inviable deducir el resto.",
        "Se alimenta de fuentes de entropía del sistema operativo: ruido de dispositivos, tiempos de interrupción, instrucciones del procesador.",
        "Es el que hay que usar siempre, y en los lenguajes modernos suele estar a una línea de distancia.",
        "Si duda cuál está usando, esa duda ya es un hallazgo."]),
    alto=2.55)

s, y = base(p, "// 33  CATÁSTROFE", "DEBIAN, 2008: DOS LÍNEAS BORRADAS", sig())
y = intro(s, y, "El caso más didáctico de la historia reciente, porque nadie hizo nada malintencionado y el "
                "resultado fue devastador.")
y = tabla(s, y, ["MOMENTO", "QUÉ PASÓ"], [
    [("2006", {"bold": True}), "Un mantenedor comenta dos líneas de código de la biblioteca criptográfica para silenciar una advertencia de una herramienta de análisis de memoria. La intención es limpiar el código."],
    [("2006 – 2008", {"bold": True}), "Esas líneas alimentaban el generador con entropía. Sin ellas, la única fuente de variación que queda es el identificador del proceso."],
    [("Consecuencia", {"bold": True, "color": NARANJA}), "El espacio de llaves posibles se reduce de un número astronómico a unas 32.768 opciones. Todas las llaves generadas en ese periodo son enumerables."],
    [("Mayo de 2008", {"bold": True}), "Se descubre. Hubo que regenerar y reemplazar llaves de servidores, certificados y llaves de acceso remoto en todo el mundo durante meses."],
], [1.8, 8.2], alto_fila=0.62)
nota(s, y, "// LA MORALEJA OPERATIVA",
     "El algoritmo era correcto, la implementación era la oficial y el mantenedor actuaba de buena fe. Lo que "
     "falló fue la entropía de entrada, que es invisible: una llave mal generada se ve exactamente igual que una "
     "buena. No hay forma de detectarlo mirando la llave.")

s, y = base(p, "// 34  CATÁSTROFE", "PLAYSTATION 3, 2010: EL NÚMERO QUE DEBÍA CAMBIAR", sig())
y = intro(s, y, "El segundo caso muestra algo distinto: no falló la llave, falló un número que acompaña a cada "
                "firma y que debía ser distinto cada vez.")
y = dos_columnas(s, y,
    ("// QUÉ DEBÍA PASAR", [
        "El esquema de firma digital que usaba la consola exige un número aleatorio nuevo e irrepetible por cada firma.",
        "Ese número no es la llave, pero si se repite, la matemática del esquema permite despejar la llave privada a partir de dos firmas."]),
    ("// QUÉ PASÓ", [
        "La implementación usaba siempre el mismo valor fijo.",
        "En diciembre de 2010, un grupo lo demostró públicamente y derivó la llave privada con la que el fabricante firmaba el software de la consola.",
        "No se rompió el algoritmo de firma: se rompió un requisito de uso que estaba escrito en el estándar."]),
    alto=2.15)
nota(s, y, "// LO QUE ESTOS DOS CASOS TIENEN EN COMÚN",
     "En ninguno de los dos se rompió la matemática. En ambos falló la aleatoriedad: en uno, la que genera la "
     "llave; en otro, la que acompaña cada firma. Cuando lleguemos a firma digital en la sesión 4, este requisito "
     "va a reaparecer, y ustedes ya van a saber por qué importa.")

s, y = base(p, "// 35  PRÁCTICA", "DE DÓNDE SACAR ALEATORIEDAD BUENA", sig())
y = intro(s, y, "Referencia para el laboratorio y para el informe. La regla general: pídasela al sistema "
                "operativo, nunca la construya usted.")
y = tabla(s, y, ["ENTORNO", "LO QUE SE DEBE USAR", "LO QUE NUNCA"], [
    [("Línea de comandos", {"bold": True}), "openssl rand", "Cadenas escritas a mano o derivadas de la fecha"],
    [("Sistemas tipo Unix", {"bold": True}), "El dispositivo de aleatoriedad del núcleo o la llamada al sistema correspondiente", "Semillas fijas para «poder reproducir»"],
    [("Java", {"bold": True}), "La clase de aleatoriedad segura de la biblioteca estándar", "La clase de aleatoriedad general"],
    [("Python", {"bold": True}), "El módulo de secretos o la función de bytes aleatorios del sistema", "El módulo random"],
    [("Navegador", {"bold": True}), "La interfaz criptográfica del navegador", "La función de aleatoriedad del lenguaje"],
], [2.4, 4.6, 3.0], alto_fila=0.52)

s, y = base(p, "// 36  DEMOSTRACIÓN", "GENERAR Y MIRAR UNA LLAVE", sig())
y = intro(s, y, "Demostración en vivo. Observen tres cosas: que cada ejecución da un resultado distinto, que la "
                "longitud es la que pedimos, y que no hay ningún patrón visible.")
y = bloque_codigo(s, y, [
    "# 32 bytes = 256 bits de un generador criptográfico",
    "openssl rand -hex 32",
    "",
    "# la misma orden dos veces seguidas: nunca coincide",
    "openssl rand -hex 32",
    "",
    "# un vector de inicialización de 16 bytes",
    "openssl rand -hex 16",
], titulo="DEMOSTRACIÓN 1 · GENERACIÓN DE LLAVES")
nota(s, y, "// LA PREGUNTA PARA LA CLASE",
     "Si ejecutamos esta orden un millón de veces, ¿cuál es la probabilidad de que dos resultados coincidan? "
     "Y una segunda, más incómoda: ¿cómo sabríamos si el generador de esta máquina está comprometido?")

s, y = base(p, "// 37  DISTINCIÓN", "UNA CONTRASEÑA NO ES UNA LLAVE", sig())
y = intro(s, y, "Distinción que vamos a necesitar en la sesión 3, cuando arreglemos el hallazgo H1 de Coopaburrá.")
y = dos_columnas(s, y,
    ("// UNA LLAVE", [
        "La produce una máquina a partir de una fuente de entropía.",
        "Tiene la longitud exacta que el algoritmo necesita.",
        "Nadie la memoriza ni la escribe: se almacena y se custodia.",
        "Su entropía es conocida y calculable."]),
    ("// UNA CONTRASEÑA", [
        "La elige una persona, y las personas eligen mal y repiten.",
        "Tiene longitud variable y entropía baja e impredecible.",
        "Se memoriza, y por eso se parece a otras que la misma persona ya usó.",
        "Para convertirla en llave hay que pasarla por una función de derivación con factor de trabajo deliberadamente lento."]),
    alto=2.25)
nota(s, y, "// CONEXIÓN CON EL CASO",
     "Coopaburrá guarda las contraseñas con un resumen simple y una sal compartida. Eso es tratar una contraseña "
     "como si fuera una llave, y es el hallazgo H1. En la sesión 3 vamos a ver por qué esa decisión hace que "
     "142.000 contraseñas se puedan atacar todas a la vez en lugar de una por una.")

# ───────── SECCIÓN 06 · POR QUÉ FALLA LO QUE PARECE SEGURO ────
s, y = base(p, "// 38  MEDIDA", "CUÁNTA ENTROPÍA TIENE UNA CONTRASEÑA", sig())
y = intro(s, y, "Una llave de 128 bits tiene 128 bits de entropía porque la produjo una máquina al azar. Una "
                "contraseña tiene la entropía del procedimiento con que se escogió, y casi siempre es mucho menor "
                "de lo que aparenta.")
y = tabla(s, y, ["SECRETO", "CÓMO SE CALCULA", "ENTROPÍA MÁXIMA"], [
    [("PIN de cuatro dígitos", {"bold": True}), "4 × log2(10)", "13 bits"],
    [("Seis minúsculas: la política de Coopaburrá", {"bold": True, "color": NARANJA}), "6 × log2(26)", "28 bits"],
    [("Ocho caracteres al azar entre 94 símbolos", {"bold": True}), "8 × log2(94)", "52 bits"],
    [("Cinco palabras al azar de una lista de 7.776", {"bold": True}), "5 × log2(7.776)", "65 bits"],
    [("Llave AES-128 del generador del sistema", {"bold": True}), "128 bits al azar", "128 bits"],
], [4.6, 3.0, 2.4], alto_fila=0.42)
nota(s, y, "// LA CUENTA QUE HAY QUE HACER CON EL HALLAZGO H1",
     "Veintiocho bits son unos 270 millones de combinaciones. Una sola tarjeta gráfica calcula SHA-1 a razón de "
     "decenas de miles de millones por segundo: <b>recorre todas las contraseñas de seis minúsculas en menos de un "
     "segundo</b>. Y ese es el máximo teórico: las contraseñas que escoge la gente caen mucho antes.", alto=0.92)

seccion(p, "06", "POR QUÉ FALLA LO QUE PARECE SEGURO",
        "De César a AES: sustitución, transposición y las lecciones que siguen vigentes", sig())

s, y = base(p, "// 39  ORIGEN", "EL CIFRADO DE CÉSAR", sig())
y = intro(s, y, "Suetonio cuenta que Julio César desplazaba cada letra tres posiciones para su correspondencia "
                "militar. Es el punto de partida obligado, y se agota rápido: sirve para instalar el vocabulario.")
y = bloque_codigo(s, y, [
    "Texto claro : COOPABURRA",
    "Desplazamiento de 3",
    "Texto cifrado: FRRSDEXUUD",
    "",
    "Espacio de llaves: 25 desplazamientos posibles",
], titulo="EJEMPLO")
y = dos_columnas(s, y,
    ("// LO QUE INTRODUCE", [
        "La idea de algoritmo —desplazar— separada de la idea de llave —cuánto—.",
        "Ese es el aporte conceptual y por eso vale la pena verlo."]),
    ("// POR QUÉ MUERE", [
        "Veinticinco llaves posibles se prueban todas a mano en un par de minutos.",
        "El espacio de llaves es tan pequeño que ni siquiera hace falta ser astuto."]),
    alto=1.35)

s, y = base(p, "// 40  EVOLUCIÓN", "SUSTITUCIÓN: UN ESPACIO ENORME QUE IGUAL CAE", sig())
y = intro(s, y, "El paso siguiente parece resolverlo todo: en vez de desplazar, se asigna a cada letra otra "
                "cualquiera. El espacio de llaves se vuelve gigantesco y el sistema sigue siendo indefendible.")
y = cifras(s, y, [
    ("26!", "PERMUTACIONES", "POSIBLES", False),
    ("4×10²⁶", "LLAVES", "DISTINTAS", False),
    ("~88", "BITS DE ESPACIO", "DE LLAVES", False),
    ("Minutos", "LO QUE TARDA", "ROMPERLO", True),
])
nota(s, y, "// LA LECCIÓN, Y ES LA MÁS IMPORTANTE DE ESTA SECCIÓN",
     "Ochenta y ocho bits de espacio de llaves es una cifra respetable incluso para los estándares de hoy. Y sin "
     "embargo el sistema cae en minutos, porque el ataque no consiste en probar llaves: consiste en explotar una "
     "propiedad del texto que el cifrado no oculta. <b>Un espacio de llaves grande es necesario pero nunca "
     "suficiente.</b>", alto=1.15)

s, y = base(p, "// 41  ATAQUE", "ANÁLISIS DE FRECUENCIAS", sig())
y = intro(s, y, "La sustitución conserva intacta la estructura estadística del idioma: cada letra cambia de "
                "nombre pero mantiene su frecuencia. Con un texto suficientemente largo, eso basta.")
y = tabla(s, y, ["LETRA", "FRECUENCIA APROXIMADA EN ESPAÑOL", "LETRA", "FRECUENCIA APROXIMADA EN ESPAÑOL"], [
    [("E", {"bold": True}), "13,7 %", ("R", {"bold": True}), "6,9 %"],
    [("A", {"bold": True}), "12,5 %", ("N", {"bold": True}), "6,7 %"],
    [("O", {"bold": True}), "8,7 %", ("I", {"bold": True}), "6,2 %"],
    [("S", {"bold": True}), "8,0 %", ("D", {"bold": True}), "5,9 %"],
], [1.2, 3.8, 1.2, 3.8], alto_fila=0.44)
nota(s, y, "// CÓMO SE USA EN EL LABORATORIO",
     "Se cuenta la frecuencia de cada símbolo del texto cifrado, se ordena, y se prueba la correspondencia con "
     "esta tabla. Las primeras dos o tres letras suelen acertar de una vez; el resto se completa por contexto, "
     "buscando palabras cortas y terminaciones frecuentes del español.")

s, y = base(p, "// 42  FAMILIA", "TRANSPOSICIÓN: MOVER SIN CAMBIAR", sig())
y = intro(s, y, "La otra gran familia de los cifrados clásicos. No se cambia ninguna letra: se cambian de lugar. La "
                "escítala espartana, una cinta enrollada en un bastón, ya lo hacía en el siglo V antes de Cristo.")
y = bloque_codigo(s, y, [
    "Llave: CIFRA          Mensaje: PAGAR TODO EL VIERNES",
    "",
    "   C  I  F  R  A        ← la llave encabeza las columnas",
    "   P  A  G  A  R",
    "   T  O  D  O  E        ← el mensaje se escribe por filas",
    "   L  V  I  E  R",
    "   N  E  S  X  X        ← la última fila se completa con relleno",
    "",
    "Se leen las columnas en el orden alfabético de la llave: A, C, F, I, R",
    "Cifrado:   RERX  PTLN  GDIS  AOVE  AOEX",
], titulo="TRANSPOSICIÓN POR COLUMNAS")
nota(s, y, "// LO QUE HAY QUE NOTAR",
     "Las veinte letras del cifrado son exactamente las del mensaje, más dos de relleno. <b>Ninguna cambió; todas "
     "se movieron.</b> Esa diferencia con la sustitución es la que permite reconocer en segundos qué clase de "
     "cifrado se tiene delante.", alto=0.85)

s, y = base(p, "// 43  ATAQUE", "CÓMO SE DELATA Y CÓMO SE ROMPE UNA TRANSPOSICIÓN", sig(), titulo_tam=22)
y = intro(s, y, "Cada familia deja una huella distinta, y aprender a leerla es el primer oficio del criptoanalista.")
y = dos_columnas(s, y,
    ("// CÓMO SE DELATA", [
        "El análisis de frecuencias devuelve exactamente la distribución del español: la E cerca del 14 %, la A cerca del 12,5 %, la O cerca del 9 %.",
        "Con una sustitución eso no pasa, porque las letras cambiaron. Con una transposición pasa siempre.",
        "Es la primera prueba que hace un analista: le dice qué familia tiene delante antes de intentar nada más."]),
    ("// CÓMO SE ROMPE", [
        "Se prueban anchos de columna y se buscan combinaciones frecuentes del idioma: QU, ES, EN, DE, LA.",
        "El espacio de llaves útil es pequeño, y cada acierto parcial ayuda a encontrar el siguiente, como en un crucigrama.",
        "La doble transposición resiste mucho más, y se usó en operaciones militares hasta mediados del siglo XX."]),
    alto=2.30)
nota(s, y, "// LA LECCIÓN QUE LLEGA HASTA AES",
     "La sustitución sola cae por frecuencias; la transposición sola cae por anagramas. <b>Combinadas y repetidas "
     "son mucho más fuertes que cada una por separado.</b> Es la idea que Claude Shannon formalizó en 1949, y está "
     "dentro de todo cifrado de bloque moderno.", alto=0.85)

s, y = base(p, "// 44  EVOLUCIÓN", "VIGENÈRE Y LA LLAVE QUE SE REPITE", sig())
y = intro(s, y, "Durante tres siglos se consideró indescifrable. La idea es buena y sobrevive hasta hoy: usar una "
                "llave que cambie el desplazamiento letra por letra, de modo que la misma letra del texto claro "
                "no produzca siempre el mismo símbolo.")
y = bloque_codigo(s, y, [
    "Texto claro : C O O P A B U R R A",
    "Llave       : L L A V E L L A V E   ← se repite cíclicamente",
    "Texto cifrado: N Z O K E M F R M E",
], titulo="EJEMPLO CON LA LLAVE «LLAVE»")
y = dos_columnas(s, y,
    ("// POR QUÉ RESISTE EL ANÁLISIS SIMPLE", [
        "La misma letra produce símbolos distintos según su posición.",
        "Las frecuencias del idioma quedan aplanadas y la tabla anterior deja de servir directamente."]),
    ("// POR QUÉ CAE DE TODOS MODOS", [
        "La llave se repite. Si mide cinco letras, el texto son en realidad cinco cifrados de César intercalados.",
        "Kasiski publicó en 1863 cómo deducir la longitud de la llave a partir de secuencias repetidas. Hallada la longitud, se aplica el análisis de frecuencias a cada posición."]),
    alto=1.95)

s, y = base(p, "// 45  HISTORIA", "ENIGMA: LA MÁQUINA NO FALLÓ, FALLÓ LA OPERACIÓN", sig(), titulo_tam=22)
y = intro(s, y, "Vigenère mecanizado: rotores que cambian la sustitución con cada letra y un tablero de conexiones. "
                "La versión del ejército alemán admitía unos 159 trillones de configuraciones. Cayó igual, y por "
                "las mismas razones que Coopaburrá.")
y = tabla(s, y, ["DEBILIDAD", "DE QUÉ TIPO ERA", "SU EQUIVALENTE EN EL CASO"], [
    [("Una letra nunca se cifraba como sí misma", {"bold": True}), "Defecto de diseño, pequeño pero explotable", "Poco frecuente hoy: es la categoría del algoritmo débil"],
    [("Mensajes con texto predecible: partes del clima, fórmulas fijas", {"bold": True}), "Texto claro conocido", "El encabezado idéntico de cada respaldo nocturno"],
    [("La llave de cada mensaje se transmitía dos veces al inicio", {"bold": True, "color": NARANJA}), "Repetición que expuso la estructura", "La misma llave de firma en todas las versiones desde 2023"],
    [("Operadores que escogían llaves obvias o repetidas", {"bold": True}), "Mala generación de llave", "La contraseña de seis caracteres"],
], [3.9, 2.9, 3.2], alto_fila=0.50)
nota(s, y, "// QUIÉNES LA ROMPIERON Y CÓMO",
     "Los matemáticos polacos Rejewski, Różycki y Zygalski desde 1932, y después el equipo de Bletchley Park con "
     "Turing. <b>Ninguno atacó el espacio de llaves: atacaron la operación.</b> Es la lección de historia más útil "
     "para un auditor.", alto=0.85)

s, y = base(p, "// 46  LÍMITE", "EL ÚNICO CIFRADO PERFECTO", sig())
y = intro(s, y, "Si el problema de Vigenère es que la llave se repite, la solución evidente es que no se repita "
                "nunca. Ese sistema existe, se llama cuaderno de un solo uso, y Claude Shannon demostró en 1949 "
                "que es matemáticamente irrompible.")
y = tabla(s, y, ["CONDICIÓN", "POR QUÉ ES INDISPENSABLE"], [
    [("La llave es tan larga como el mensaje", {"bold": True}), "Si fuera más corta habría que repetirla, y volvería el ataque de Kasiski"],
    [("La llave es perfectamente aleatoria", {"bold": True}), "Cualquier patrón en la llave se traslada al texto cifrado"],
    [("La llave se usa una sola vez", {"bold": True}), "Dos mensajes con la misma llave se pueden combinar y la llave se cancela, dejando los textos relacionados"],
    [("La llave se distribuye en secreto", {"bold": True}), "Hay que hacerle llegar al destinatario tantos bits secretos como bits vaya a enviar"],
], [4.6, 5.4], alto_fila=0.54)
nota(s, y, "// LA PARADOJA QUE ENSEÑA TODO EL OFICIO",
     "Es perfecto e inservible. Para enviar un gigabyte en secreto hay que haberle entregado antes al "
     "destinatario un gigabyte de llave en secreto, con lo cual el problema no se resolvió: se movió. "
     "<b>Toda la criptografía moderna es la búsqueda de un compromiso practicable entre seguridad y "
     "manejabilidad de la llave.</b>", alto=1.10)

s, y = base(p, "// 47  PUENTE", "LA REUTILIZACIÓN DE LLAVE, QUE NO ES HISTORIA", sig())
y = intro(s, y, "La tercera condición del cuadro anterior no es una curiosidad histórica: es un error que se "
                "sigue cometiendo con algoritmos modernos, y lo vamos a ver en funcionamiento en el laboratorio.")
y = bloque_codigo(s, y, [
    "Si  C1 = M1 ⊕ K    y    C2 = M2 ⊕ K        (la misma llave K dos veces)",
    "",
    "entonces  C1 ⊕ C2 = M1 ⊕ M2                 ← la llave desaparece",
    "",
    "y quien tenga los dos textos cifrados obtiene una relación directa",
    "entre los dos mensajes, sin conocer K jamás.",
], titulo="POR QUÉ NUNCA SE REPITE UNA LLAVE DE FLUJO")
nota(s, y, "// DÓNDE REAPARECE ESTO",
     "En la sesión 2, cuando veamos modos de operación, el vector de inicialización repetido produce exactamente "
     "este efecto sobre AES. Y en la sesión 4, el número que se repitió en el caso de la consola es la misma "
     "idea aplicada a firma digital. Es un solo error con tres disfraces.")

# ────────────── SECCIÓN 07 · LABORATORIO 1 ───────────────────
s, y = base(p, "// 48  PRINCIPIOS", "CONFUSIÓN Y DIFUSIÓN: LO QUE SHANNON DEJÓ ESCRITO", sig(), titulo_tam=22)
y = intro(s, y, "En 1949 Claude Shannon publicó el trabajo que convirtió la criptografía en ciencia. Demostró por qué "
                "el cuaderno de un solo uso es perfecto y dejó dos principios de diseño que siguen gobernando todo "
                "cifrado moderno.")
y = tarjetas(s, y, [
    ("// CONFUSIÓN", [
        "Que la relación entre la llave y el texto cifrado sea lo más compleja posible.",
        "Cada bit del cifrado debe depender de muchas partes de la llave, de modo que conocer pedazos del cifrado no revele pedazos de la llave.",
        "Se consigue con <b>sustitución</b> no lineal."]),
    ("// DIFUSIÓN", [
        "Que cada bit del texto claro influya en muchos bits del cifrado.",
        "Cambiar una sola letra del mensaje debe cambiar, en promedio, la mitad del resultado: el efecto avalancha que van a medir en la sesión 3.",
        "Se consigue con <b>transposición</b> y mezcla."]),
], alto=2.05)
nota(s, y, "// LA CONSECUENCIA",
     "Los patrones estadísticos del idioma, que son los que rompen a César, a la sustitución y a la "
     "transposición, quedan disueltos en el cifrado. <b>El análisis de frecuencias deja de funcionar</b>, y el "
     "atacante vuelve a quedar frente al espacio de llaves completo.", alto=0.85)

s, y = base(p, "// 49  PUENTE", "DE LOS CIFRADOS CLÁSICOS A AES", sig())
y = intro(s, y, "Lo que van a ver el jueves ya lo conocen. AES es sustitución y transposición, combinadas con la llave "
                "y repetidas diez veces o más. Lo nuevo no es la idea: es el rigor con que se diseñó y se analizó "
                "en público.")
y = tabla(s, y, ["OPERACIÓN DE CADA RONDA", "IDEA CLÁSICA DE LA QUE VIENE", "PRINCIPIO"], [
    [("Sustituir cada byte con una tabla fija", {"bold": True}), "Sustitución, con una tabla construida para no dejar patrones", "Confusión"],
    [("Desplazar las filas del bloque", {"bold": True}), "Transposición", "Difusión"],
    [("Mezclar cada columna", {"bold": True}), "Cada byte pasa a depender de los otros tres de su columna", "Difusión"],
    [("Combinar con la llave de la ronda", {"bold": True, "color": NARANJA}), "La misma operación del cuaderno de un solo uso", "La única parte secreta"],
    [("Repetir 10, 12 o 14 veces", {"bold": True}), "Según la llave sea de 128, 192 o 256 bits", "Hasta que la salida sea indistinguible del azar"],
], [3.5, 4.3, 2.2], alto_fila=0.44)
nota(s, y, "// POR QUÉ NADIE LO DISCUTE",
     "Quince candidatos, un concurso público abierto a cualquier criptoanalista del mundo y un ganador, Rijndael, "
     "escogido en 2000. <b>Veinticinco años después, el mejor ataque conocido contra AES completo es apenas mejor "
     "que probar todas las llaves.</b> Eso es lo que significa un algoritmo estándar.", alto=0.90)

seccion(p, "07", "LABORATORIO 1",
        "Romper tres cifrados clásicos y entender por qué cayeron", sig())

s, y = base(p, "// 50  LABORATORIO", "OBJETIVO Y ENTREGABLE", sig())
y = intro(s, y, "Treinta minutos, en los equipos de tres que se conformaron al inicio. No se trata de resolver los "
                "retos: se trata de documentar por qué se pudieron resolver. Lo que no se cierre en clase se "
                "termina como trabajo independiente.")
y = pasos(s, y, [
    ("Ejercicio 1 · Un desplazamiento", "Descifrar un mensaje cifrado con César sin conocer el desplazamiento. Registrar cuántos intentos hicieron falta y cuánto tiempo tomó."),
    ("Ejercicio 2 · Una sustitución", "Romper un texto cifrado por sustitución usando análisis de frecuencias. Entregar la correspondencia deducida y el método seguido."),
    ("Ejercicio 3 · Dos mensajes, una llave", "Se les entregan dos textos cifrados con la misma llave de flujo. Combinarlos y explicar qué información aparece y por qué."),
])
nota(s, y, "// LO QUE SE ENTREGA",
     "Una página por equipo, al final del bloque: para cada ejercicio, el resultado obtenido, el método empleado "
     "y —lo que realmente se evalúa— <b>qué propiedad del cifrado permitió el ataque</b>. Un ejercicio resuelto "
     "sin esa explicación vale la mitad.")

s, y = base(p, "// 51  LABORATORIO", "ENTORNO DE TRABAJO", sig())
y = intro(s, y, "Todo el laboratorio funciona sin conexión a internet y sin permisos de administrador: Python se "
                "instala para el usuario, y la librería también. Desde la sesión 2, los ejercicios con OpenSSL van "
                "en Git Bash en Windows —no en cmd ni PowerShell—; en macOS y Linux, en la Terminal.")
y = tarjetas(s, y, [
    ("// HERRAMIENTA PRINCIPAL", [
        "Una página de utilidades criptográficas que se ejecuta dentro del navegador, sin enviar nada a ningún servidor.",
        "Se les entrega el archivo; se abre con doble clic y funciona aunque la sala no tenga internet."]),
    ("// PYTHON, EN TODOS LOS LABORATORIOS", [
        "Python 3 con su biblioteca estándar alcanza para hoy. Desde la sesión 2 se suma la librería cryptography.",
        "El análisis de frecuencias son diez líneas de código, y escribirlas enseña más que usar la herramienta."]),
], alto=1.55)
nota(s, y, "// ADVERTENCIA PARA TODO EL MÓDULO",
     "No carguen material del caso ni textos de los ejercicios en servicios en línea de terceros. Además de la "
     "regla 5 del caso, es una costumbre profesional: lo que se pega en un sitio público deja de ser confidencial "
     "en ese instante.")

s, y = base(p, "// 52  PYTHON", "LABORATORIO 1 · EL EJERCICIO EN PYTHON", sig())
y = intro(s, y, "Como pide la carta descriptiva: implementar y analizar con librerías estándar. Hoy, el ejercicio 2 "
                "hecho con código, más una prueba sobre generadores.")
y = bloque_codigo(s, y, [
    "from collections import Counter",
    "import random, secrets",
    "",
    "# Ejercicio 2 con código: frecuencias del texto cifrado",
    "cifrado = open(\"ejercicio2.txt\", encoding=\"utf-8\").read().upper()",
    "letras = [c for c in cifrado if c.isalpha()]",
    "for letra, n in Counter(letras).most_common(8):",
    "    print(letra, round(100 * n / len(letras), 1), \"%\")",
    "",
    "# Dos generadores: uno que se puede repetir y uno que no",
    "random.seed(2019);  print(random.getrandbits(128))   # siempre el mismo",
    "print(secrets.token_hex(16))                          # 128 bits del sistema",
], titulo="LABORATORIO 1 · PYTHON 3, SOLO BIBLIOTECA ESTÁNDAR")
nota(s, y, "// LAS DOS PREGUNTAS QUE VAN EN EL INFORME",
     "¿Qué letra del cifrado corresponde a la E, y cómo lo saben? Y ejecuten la línea del generador tres veces: "
     "<b>¿por qué el primer número sale siempre igual, y qué tiene que ver con Debian en 2008?</b>", alto=0.78)

# ────────────────── SECCIÓN 08 · CIERRE ──────────────────────
s, y = base(p, "// 53  SÍNTESIS", "LO QUE LLEVAMOS DE LA SESIÓN", sig())
pasos(s, y + 0.05, [
    ("Cuatro servicios, no uno", "Y el que le faltaba a Coopaburrá —no repudio— no se consigue con el mecanismo que eligieron."),
    ("La seguridad vive en la llave", "Kerckhoffs, 1883. Sigue siendo el criterio con el que se juzga cualquier diseño."),
    ("Una llave sin entropía no es una llave", "Debian y la consola de videojuegos lo demuestran: el algoritmo puede ser perfecto y el sistema caer igual."),
    ("Un espacio de llaves grande no basta", "La sustitución tiene ochenta y ocho bits y cae en minutos, porque el ataque no prueba llaves."),
    ("Repetir una llave la destruye", "Es el mismo error en el cuaderno de un solo uso, en los modos de cifrado y en la firma digital."),
])

s, y = base(p, "// 54  ENTREGA", "PRIMERA PARTE DEL PRODUCTO", sig())
y = intro(s, y, "Se entrega al inicio de la sesión 2. Es el hallazgo H8 y la base de todo lo que sigue. La guía de "
                "la entrega explica cómo llenar cada columna.")
y = tabla(s, y, ["COLUMNA DEL INVENTARIO", "QUÉ SE REGISTRA", "DÓNDE SALE EL DATO"], [
    [("Dónde está la criptografía", {"bold": True}), "Sistema, canal o proceso donde se usa", "Parte 3 del caso"],
    [("Para qué sirve ahí", {"bold": True}), "Cuál de los cuatro servicios pretende dar", "Lo deducen ustedes"],
    [("Qué algoritmo y qué versión", {"bold": True}), "Nombre, modo y longitud; «desconocido» es respuesta válida y reveladora", "Partes 3 y 8 · anexo técnico"],
    [("Qué llave lo protege", {"bold": True}), "Cuántas hay, quién las conoce, dónde se guardan", "Partes 7 y 8 · anexo técnico"],
    [("Quién responde por ella", {"bold": True}), "Nombre y cargo de la Parte 2 del caso", "Parte 2"],
    [("Cuándo vence o se rota", {"bold": True}), "Fecha conocida o «nunca se ha rotado»", "Partes 7 y 10 · anexo"],
], [3.4, 4.6, 2.0], alto_fila=0.40)
nota(s, y, "// CRITERIO DE EVALUACIÓN",
     "No se evalúa que esté completo: es imposible completarlo. Se evalúa que <b>las casillas vacías estén "
     "marcadas como desconocidas</b> y que se diga a quién preguntarle. El <b>anexo técnico</b> del caso trae, por "
     "sistema, el algoritmo y la llave que la Parte 3 no detalla.", alto=0.92)

trabajo_independiente(p, "// 55  CIERRE", ["TRABAJO INDEPENDIENTE", "HASTA LA SESIÓN 2"], [
    ("8 h", "TOTAL ENTRE", "MARTES Y JUEVES", False),
    ("3,5 h", "LECTURA", "PREVIA", False),
    ("4,5 h", "INVENTARIO E INFORME", "DEL LABORATORIO 1", True),
], [
    ("El caso Coopaburrá y su anexo técnico", "Las catorce páginas del caso más el anexo, que trae la evidencia por sistema. 1,5 horas. El jueves se asume leído, en especial las partes 3, 7, 8 y 10 y el anexo, que alimentan el inventario."),
    ("Katz y Lindell (2020)", "Introduction to Modern Cryptography, capítulos 1 y 2: cifrados clásicos, principios de la criptografía moderna y secreto perfecto. Una hora."),
    ("NIST SP 800-38A", "Recommendation for Block Cipher Modes of Operation, sección 6: los modos ECB, CBC y CTR. Una hora. Es la base del bloque 3."),
], "// CONDICIÓN DE ENTRADA A LA SESIÓN 2",
   "El jueves no se explica qué es un modo de operación: se discute cuál escoger. Las 4,5 horas de elaboración son "
   "el inventario (3 h, en equipo, con la guía de la entrega) y el cierre del informe del laboratorio (1,5 h). El "
   "quiz 1 incluye preguntas sobre estas lecturas.", sig(), titulo_lecturas="Lectura previa · 3,5 horas")

s, y = base(p, "// 56  ADELANTO", "LO QUE VIENE EL JUEVES", sig())
y = intro(s, y, "Sesión 2: cifrado simétrico. El bloque más práctico del módulo y el que ataca directamente dos "
                "hallazgos del caso.")
y = tarjetas(s, y, [
    ("// BLOQUE 1 · AES Y LOS MODOS DE OPERACIÓN", [
        "Qué es realmente AES y qué no es.",
        "Por qué el modo de operación importa más que el algoritmo, y por qué elegirlo mal deja los datos a la vista aunque estén «cifrados».",
        "Cifrado autenticado: el modo que da confidencialidad e integridad al tiempo, y por qué hoy es el que se debe usar por defecto."]),
    ("// BLOQUE 2 · LABORATORIO Y HALLAZGOS", [
        "Una demostración que no se olvida: el escudo de la Institución cifrado con AES-256, todavía perfectamente reconocible.",
        "Análisis de la línea real del script de respaldo de Coopaburrá, que tiene tres errores distintos y solo uno es evidente.",
        "Entrega y realimentación de la primera parte del inventario."]),
], alto=2.05)

glosario(p, "// 57  GLOSARIO", 1, 2, [
    ("AES", "Advanced Encryption Standard — Estándar de cifrado avanzado. Cifrado simétrico de bloque adoptado por el NIST en 2001."),
    ("Base64", "Codificación que representa datos binarios con 64 caracteres imprimibles. No es cifrado: se revierte sin llave."),
    ("CSPRNG", "Cryptographically Secure Pseudorandom Number Generator — Generador de números aleatorios apto para criptografía."),
    ("DES", "Data Encryption Standard — Estándar de cifrado de datos de 1977, con llave de 56 bits. Retirado."),
    ("ECB / CBC / CTR", "Electronic Codebook, Cipher Block Chaining, Counter — Modos de operación de un cifrado de bloque. Sesión 2."),
    ("H1 … H8", "Los ocho hallazgos del diagnóstico criptográfico de Coopaburrá, numerados como en el documento del caso."),
    ("HMAC", "Hash-based Message Authentication Code — Código de autenticación de mensajes basado en una función resumen. Sesión 3."),
    ("IV", "Initialization Vector — Vector de inicialización. Valor que debe cambiar en cada cifrado. Sesión 2."),
    ("NIST", "National Institute of Standards and Technology — Instituto Nacional de Estándares y Tecnología de Estados Unidos."),
    ("OTP", "One-Time Pad — Cuaderno de un solo uso. El único cifrado con secreto perfecto demostrado."),
], sig())

glosario(p, "// 58  GLOSARIO", 2, 2, [
    ("PIN", "Personal Identification Number — Número de identificación personal."),
    ("PS3", "PlayStation 3 — Consola cuya llave de firma se recuperó en 2010 porque un número que debía cambiar era constante."),
    ("RSA", "Rivest, Shamir y Adleman — Algoritmo de llave pública de 1977, nombrado por sus autores. Sesión 4."),
    ("SHA-1", "Secure Hash Algorithm 1 — Función resumen de 160 bits, rota desde 2017. La que usa Coopaburrá para contraseñas."),
    ("SQL", "Structured Query Language — Lenguaje de consulta de bases de datos. El respaldo del caso es un volcado SQL."),
    ("SSL / TLS", "Secure Sockets Layer / Transport Layer Security — Protocolos de canal seguro. Sesión 5."),
    ("XOR", "Exclusive OR — O exclusivo. Operación bit a bit con la que se combina la llave en el cuaderno de un solo uso."),
    ("MD5", "Message Digest 5 — Función resumen de 128 bits de 1992. Rota desde 2004: no sirve para nada que exija seguridad."),
    ("SP", "Special Publication — Serie de publicaciones técnicas del NIST, como la SP 800-38A sobre modos de operación."),
    ("WEP", "Wired Equivalent Privacy — Primer cifrado de redes inalámbricas. Roto en 2001 y reemplazado por WPA."),
], sig())

fuentes(p, "// 59  FUENTES", "REFERENCIAS DE LA SESIÓN", [
    ("Katz, J. y Lindell, Y. (2020).", "Introduction to modern cryptography (3.ª ed.). CRC Press.", "Capítulos 1 y 2: cifrados clásicos, principios y secreto perfecto · lectura previa"),
    ("Stallings, W. (edición vigente).", "Cryptography and network security: Principles and practice. Pearson.", "Técnicas clásicas de cifrado: sustitución y transposición"),
    ("Kerckhoffs, A. (1883).", "La cryptographie militaire. Journal des sciences militaires, 9, 5–38.", "Los seis requisitos; el segundo es el principio de Kerckhoffs"),
    ("Shannon, C. E. (1949).", "Communication theory of secrecy systems. Bell System Technical Journal, 28(4), 656–715.", "Secreto perfecto, confusión y difusión"),
    ("Singh, S. (2000).", "Los códigos secretos. Debate.", "De César a Enigma: la parte histórica de la sesión"),
    ("NIST. (2015).", "SP 800-90A Rev. 1: Recommendation for random number generation using deterministic random bit generators.", "Qué es un generador determinista y cómo se siembra"),
    ("NIST. (2001).", "SP 800-38A: Recommendation for block cipher modes of operation.", "Sección 6 · lectura previa de la sesión 2"),
], sig(), "// ACCESO A LAS FUENTES",
   "Las publicaciones del NIST son de acceso libre. Los libros se consultan en las bases de datos de la Institución "
   "o en la biblioteca; no está autorizado el uso de copias obtenidas por otros medios.")

p.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "SIO0010-S1-Tecnicas-criptograficas.pptx"))
print(f"Diapositivas generadas: {n}")
