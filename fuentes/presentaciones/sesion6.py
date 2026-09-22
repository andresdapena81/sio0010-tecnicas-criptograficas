# -*- coding: utf-8 -*-
"""SIO0010 · Sesión 6 (jueves) — Gestión de llaves, conservación, post-cuántica y sustentación."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck_lib
deck_lib.PIE_TXT = "SIO0010 · TÉCNICAS CRIPTOGRÁFICAS · SESIÓN 6"
from deck_lib import *

AQUI = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(AQUI, "media", "image-1-1.png")
p = nueva(LOGO, LOGO)
n = 0
def sig():
    global n; n += 1; return n

sig()
portada(p,
    "SESIÓN 6 DE 6 · 5 HORAS · BLOQUE 11: 2H15 · DESCANSO 30 MIN · BLOQUE 12: 2H15",
    ["GESTIÓN DE LLAVES", "Y LO QUE VIENE"],
    "LA LLAVE ES UN ACTIVO. TIENE DUEÑO, TIENE FECHA Y TIENE SUCESOR.",
    "SIO0010 · Técnicas Criptográficas · Especialización en Seguridad de la Información de las Organizaciones · "
    "Facultad de Ingeniería · Institución Universitaria de Envigado")

seccion(p, "01", "EL CIERRE DEL MÓDULO",
        "Lo que falta para que las cinco sesiones anteriores se sostengan en el tiempo", sig())

s, y = base(p, "// 01  AGENDA", "AGENDA DE LA SESIÓN", sig())
y = intro(s, y, "La última sesión tiene tres partes: la gestión de las llaves, que es lo que hace durable todo lo "
                "anterior; lo que viene después de la criptografía actual; y la sustentación ante el comité.")
y = tabla(s, y, ["BLOQUE", "MINUTOS", "CONTENIDO", "MODALIDAD"], [
    [("Bloque 11", {"bold": True}), "0 – 10", "Recepción de la entrega 5", "Taller"],
    ["", "10 – 75", "La llave como activo: NIST SP 800-57, ceremonias, módulos de hardware y tokenización", "Magistral"],
    ["", "75 – 105", "Laboratorio 6, en Python", "Laboratorio"],
    ["", "105 – 135", "Conservación a veinte años y cierre del hallazgo H7", "Magistral"],
    [("Descanso", {"bold": True, "color": NARANJA}), "30", "", ""],
    [("Bloque 12", {"bold": True}), "0 – 40", "Transición post-cuántica: CNSA 2.0, NIST IR 8547 y criptoagilidad", "Magistral"],
    ["", "40 – 55", "Quiz 2 · Sesiones 4, 5 y 6", "Evaluación"],
    ["", "55 – 125", "Sustentación de la hoja de ruta ante el comité", "Sustentación"],
    ["", "125 – 135", "Cierre del módulo", "Magistral"],
], [1.1, 1.0, 4.4, 1.4], alto_fila=0.38)

s, y = base(p, "// 02  HILO", "LAS SEIS SESIONES, EN UNA SOLA FRASE CADA UNA", sig(), titulo_tam=24)
y = intro(s, y, "Antes de la última pieza conviene ver el hilo completo. Cada sesión respondió una pregunta y "
                "dejó una abierta, y la siguiente la recogió.")
y = tabla(s, y, ["SESIÓN", "LO QUE RESOLVIÓ", "LO QUE DEJÓ ABIERTO"], [
    [("1 · Panorama", {"bold": True}), "Qué servicios presta la criptografía y por qué hay que inventariar", "No sabemos proteger el dato guardado"],
    [("2 · Simétrico", {"bold": True}), "Cifrar volúmenes, y por qué el modo importa más que el algoritmo", "Una llave compartida no prueba quién hizo qué"],
    [("3 · Resúmenes", {"bold": True}), "Integridad, contraseñas y autenticación de mensajes", "Un código con llave compartida no da no repudio"],
    [("4 · Llave pública", {"bold": True}), "Firma digital: el único mecanismo con no repudio", "¿De quién es esa llave pública?"],
    [("5 · Certificados", {"bold": True}), "Cadena de confianza, canal seguro y ciclo del certificado", "¿Quién custodia las llaves, y por cuánto tiempo?"],
    [("6 · Hoy", {"bold": True, "color": NARANJA}), "Gestión de llaves, conservación y transición", "Nada: es la sustentación"],
], [2.6, 4.6, 2.8], alto_fila=0.42)

s, y = base(p, "// 03  ENTREGA", "RECEPCIÓN DE LA ENTREGA 5", sig())
y = intro(s, y, "Diez minutos. Se recibe el análisis del valor probatorio de los créditos y se revisan dos "
                "puntos que conviene tener claros antes de la sustentación.")
y = tarjetas(s, y, [
    ("// LA DECISIÓN QUE NO SE PUEDE ESQUIVAR", [
        "Hay cartera vigente firmada con una imagen escaneada. Ninguna solución técnica la arregla hacia atrás.",
        "Las tres salidas posibles son: resellar lo que se pueda, aceptar el riesgo documentándolo, o provisionarlo contablemente.",
        "<b>Un informe que no elige una no está terminado</b>, y en la sustentación el comité va a preguntar por ella."]),
    ("// EL COSTO POR DOCUMENTO", [
        "Los equipos que cotizaron descubrieron que el costo no está en la firma: está en la conservación año tras año.",
        "Firmar es un gasto único; conservar con validez comprobable durante veinte años es un gasto recurrente.",
        "Ese cambio de mentalidad, de compra a servicio, es lo que hay que llevarle al comité."]),
], alto=2.10)

# ─────────────── SECCIÓN 02 ───────────────
seccion(p, "02", "LA LLAVE COMO ACTIVO",
        "Generación, custodia, rotación y retiro: el oficio que Coopaburrá no hizo", sig())

s, y = base(p, "// 04  CICLO", "LAS SIETE ETAPAS DE LA VIDA DE UNA LLAVE", sig(), titulo_tam=24)
y = intro(s, y, "Ninguna de estas etapas es criptográfica. Todas son de gestión, y es en ellas donde fallan los "
                "sistemas reales, incluido el de este caso.")
y = tabla(s, y, ["ETAPA", "QUÉ HAY QUE DEFINIR", "QUÉ PASA SI NO SE DEFINE"], [
    [("Generación", {"bold": True}), "Dónde se genera y con qué fuente de aleatoriedad", "Llaves predecibles, y no se sabe hasta que es tarde"],
    [("Registro", {"bold": True}), "Identificador, propósito, responsable y fecha de vencimiento", "El hallazgo H8: nadie sabe qué llaves existen"],
    [("Distribución", {"bold": True}), "Cómo llega a donde se usa sin exponerse", "La llave del respaldo en un archivo de texto al lado"],
    [("Uso", {"bold": True}), "Una llave, un propósito. Y quién puede invocarla", "Una sola llave para 142.000 asociados desde 2023"],
    [("Rotación", {"bold": True, "color": NARANJA}), "Cada cuánto y con qué procedimiento sin cortar el servicio", "Las llaves de los 32 cajeros: siete años sin rotar"],
    [("Retiro", {"bold": True}), "Cuándo deja de usarse para proteger, pero sigue guardada para descifrar lo viejo", "Datos antiguos que ya nadie puede leer"],
    [("Destrucción", {"bold": True}), "Cuándo se borra de verdad, y con qué constancia", "Se borra una llave que todavía protegía datos vivos"],
], [2.2, 4.4, 3.4], alto_fila=0.40)

s, y = base(p, "// 05  GENERACIÓN", "DE DÓNDE SALE LA ALEATORIEDAD", sig())
y = intro(s, y, "Es la tercera vez en el módulo que la aleatoriedad decide todo, y vale la pena cerrar el tema con "
                "los dos casos donde de verdad falla en producción.")
y = dos_columnas(s, y,
    ("// EL ARRANQUE EN FRÍO", [
        "Un servidor recién encendido, o una máquina virtual recién creada, todavía no ha acumulado suficiente entropía.",
        "Las llaves generadas en ese primer instante pueden ser predecibles.",
        "Se han encontrado en internet miles de llaves de servidores que compartían factores, justamente por esto."]),
    ("// LOS EQUIPOS EMBEBIDOS", [
        "Un cajero, un lector de tarjetas o un dispositivo industrial no tienen teclado, ni ratón, ni disco con actividad variada.",
        "Sin una fuente de hardware dedicada, su aleatoriedad es pobre y repetible entre equipos del mismo lote.",
        "<b>Para los 32 cajeros, esta pregunta es obligatoria</b>: ¿dónde se generaron esas llaves y con qué fuente?"]),
    alto=2.15)

s, y = base(p, "// 06  CUSTODIA", "LA CEREMONIA DE LLAVES", sig())
y = intro(s, y, "Una ceremonia es un procedimiento documentado para generar o cargar una llave crítica de forma "
                "que nadie, individualmente, la conozca ni pueda usarla. Suena solemne y es, sobre todo, "
                "un acta.")
y = pasos(s, y + 0.05, [
    ("Custodios nombrados, con suplentes y con acta",
     "Personas identificadas por rol, no por nombre propio, para que la salida de alguien no deje la llave huérfana. Es exactamente lo que le pasó a Coopaburrá."),
    ("Doble control y conocimiento dividido",
     "Doble control: hacen falta al menos dos personas para ejecutar la operación. Conocimiento dividido: ninguna de ellas conoce la llave completa."),
    ("Guion previo, testigos y registro de cada paso",
     "Se escribe antes lo que se va a hacer, se ejecuta con testigos y se firma el acta al terminar, con las huellas de verificación."),
    ("Resguardo de las partes en custodias separadas",
     "Sobres o dispositivos sellados, en cajas fuertes distintas, con control de apertura. Reunir las partes exige reunir a las personas."),
], alto=0.84)

s, y = base(p, "// 07  TÉCNICA", "REPARTIR UN SECRETO ENTRE VARIAS PERSONAS", sig(), titulo_tam=24)
y = intro(s, y, "El conocimiento dividido tiene una solución matemática elegante que conviene conocer, porque "
                "aparece en toda documentación de módulos de hardware.")
y = bloque_codigo(s, y, [
    "Un secreto se puede partir en n partes de modo que hagan falta k",
    "de ellas para reconstruirlo, y que con k-1 no se sepa absolutamente nada.",
    "",
    "  Ejemplo típico:  5 custodios, se necesitan 3 para reconstruir.",
    "",
    "  Tolera que dos custodios no estén disponibles.",
    "  Resiste que dos custodios se pongan de acuerdo para robarla.",
    "",
    "No es partir la llave en pedazos: con k-1 partes no hay ninguna ventaja,",
    "ni siquiera parcial. Esa es la diferencia con cortar un papel en cinco.",
], titulo="UMBRAL K DE N")

s, y = base(p, "// 08  JERARQUÍA", "POR QUÉ NO SE CIFRA TODO CON LA MISMA LLAVE", sig(), titulo_tam=24)
y = intro(s, y, "La forma estándar de organizar llaves en una entidad es en niveles, y entenderla resuelve la "
                "pregunta práctica de cómo se rota sin descifrar y volver a cifrar toda la base.")
y = bloque_codigo(s, y, [
    "  LLAVE MAESTRA          en módulo de hardware, ceremonia, nunca sale",
    "        │ protege",
    "  LLAVE DE LLAVES        cifra las llaves de datos; rota anualmente",
    "        │ protege",
    "  LLAVES DE DATOS        una por campo, por archivo o por cliente",
    "",
    "Rotar la llave de llaves = volver a cifrar unas pocas llaves pequeñas.",
    "Rotar la llave maestra   = ceremonia, pero no toca ni un solo dato.",
    "",
    "Sin jerarquía, rotar significa descifrar y recifrar 142.000 registros.",
], titulo="TRES NIVELES")
nota(s, y, "// LA RESPUESTA A LA OBJECIÓN MÁS FRECUENTE",
     "Cuando alguien diga que rotar llaves es inviable porque habría que recifrarlo todo, la respuesta es esta "
     "diapositiva: <b>con una jerarquía de llaves, rotar es barato</b>. Lo inviable es no haberla diseñado.", alto=0.78)

s, y = base(p, "// 09  ROTACIÓN", "CADA CUÁNTO SE ROTA Y CÓMO", sig())
y = tabla(s, y, ["TIPO DE LLAVE", "PERIODO SEGÚN SP 800-57", "CÓMO SE ROTA SIN CORTAR EL SERVICIO"], [
    [("Llave de sesión", {"bold": True}), "Cada conexión", "Automático: es lo que hace el canal seguro"],
    [("Llave de datos", {"bold": True}), "Hasta dos años para cifrar, o ante incidente", "Se cifra lo nuevo con la llave nueva y se conserva la vieja para leer lo anterior"],
    [("Llave de llaves", {"bold": True}), "Hasta dos años; anual es buena práctica", "Se recifran solo las llaves de datos: minutos, no días"],
    [("Llave raíz del módulo de hardware", {"bold": True}), "Hasta dos años, como toda llave que cifra llaves", "Ceremonia. No se toca ni un solo dato"],
    [("Llaves de dispositivos", {"bold": True, "color": NARANJA}), "Lo que diga el fabricante. Aquí, dos años", "Por lotes, con ventana de mantenimiento. Los 32 cajeros llevan siete años"],
    [("Pareja de firma de una persona", {"bold": True}), "La vigencia del certificado", "Se emite una nueva; las firmas antiguas siguen siendo válidas si hay sello de tiempo"],
], [2.8, 2.8, 4.4], alto_fila=0.44)

s, y = base(p, "// 10  NORMA", "LOS PERIODOS CRIPTOGRÁFICOS DE NIST SP 800-57", sig(), titulo_tam=24)
y = intro(s, y, "La norma de referencia para el ciclo de vida de las llaves. Su tabla de periodos criptográficos es "
                "lo que cualquier auditor espera ver citado en una política de llaves.")
y = tabla(s, y, ["TIPO DE LLAVE", "USO PARA PROTEGER", "USO PARA LEER O VERIFICAR"], [
    [("Simétrica de cifrado de datos", {"bold": True}), "Hasta 2 años", "Hasta 3 años más, solo para descifrar"],
    [("Simétrica que cifra otras llaves", {"bold": True}), "Hasta 2 años", "Hasta 3 años más"],
    [("Simétrica de autenticación · la de H2", {"bold": True, "color": NARANJA}), "Hasta 2 años", "Hasta 3 años más. La de Coopaburrá lleva tres sin rotar"],
    [("Privada de firma", {"bold": True}), "1 a 3 años", "La pública verifica por más tiempo, según su tamaño"],
    [("Maestra simétrica de derivación", {"bold": True}), "Alrededor de 1 año", "—"],
    [("Efímera de acuerdo de llave", {"bold": True}), "Una sola transacción", "—"],
], [3.8, 2.4, 3.8], alto_fila=0.42)
nota(s, y, "// LOS DOS PERIODOS DE UNA MISMA LLAVE",
     "Una llave de datos deja de cifrar a los dos años, pero se conserva para descifrar lo ya cifrado. <b>Rotar no "
     "es borrar.</b>", alto=0.62)

s, y = base(p, "// 11  NORMA", "LOS SEIS ESTADOS DE UNA LLAVE", sig())
y = intro(s, y, "SP 800-57 define seis estados y las transiciones permitidas entre ellos. Registrar el estado de cada "
                "llave es lo que convierte el inventario en un instrumento de gestión.")
y = tabla(s, y, ["ESTADO", "QUÉ SE PUEDE HACER CON LA LLAVE", "EJEMPLO EN EL CASO"], [
    [("Pre-activación", {"bold": True}), "Nada todavía: existe, pero su uso no está autorizado", "La llave nueva de los cajeros, generada y aún sin cargar"],
    [("Activa", {"bold": True}), "Cifrar y firmar, y también descifrar y verificar", "La llave del respaldo, hoy"],
    [("Suspendida", {"bold": True}), "Nada, temporalmente, mientras se investiga", "Un teléfono reportado como perdido, mientras se confirma"],
    [("Desactivada", {"bold": True}), "Solo descifrar o verificar lo que ya existía", "La llave de datos rotada, que se guarda para leer lo viejo"],
    [("Comprometida", {"bold": True, "color": NARANJA}), "Solo lo necesario para gestionar el incidente", "La raíz interna de 2019, según la conclusión de la sesión 5"],
    [("Destruida", {"bold": True}), "Nada: ya no existe, y queda constancia", "Lo que nunca debe pasarle a una llave que aún protege datos vivos"],
], [2.2, 4.0, 3.8], alto_fila=0.42)

s, y = base(p, "// 12  CASO", "EL HALLAZGO H6, LEÍDO CON TODO LO ANTERIOR", sig(), titulo_tam=24)
y = tabla(s, y, ["LO QUE DICE EL HALLAZGO", "QUÉ ETAPA DEL CICLO FALTÓ"], [
    [("Se cargaron manualmente en la puesta en marcha, en 2019", {"bold": True}), "Generación y distribución: no consta dónde se generaron ni con qué fuente"],
    [("Lo ejecutaron dos personas, una ya no trabaja allí", {"bold": True}), "Custodia: había dos personas, pero no custodios por rol ni suplentes"],
    [("No hay registro de ceremonia", {"bold": True, "color": NARANJA}), "Registro: sin acta no se puede probar quién conoció la llave, ni descartar una copia"],
    [("Ni custodios designados, ni doble control", {"bold": True}), "Uso: una sola persona pudo haber operado la llave completa"],
    [("Ni fecha de rotación. El fabricante recomienda dos años; van siete", {"bold": True}), "Rotación: el procedimiento no existe, así que la fecha nunca llegó"],
], [4.8, 5.2], alto_fila=0.50)
nota(s, y, "// LO QUE HAY QUE ESCRIBIR EN EL INFORME",
     "El hallazgo no es que las llaves sean débiles: <b>puede que sean perfectamente fuertes</b>. El hallazgo es "
     "que no existe forma de afirmar quién las conoce. Y con 32 cajeros propios, eso es una exposición que la "
     "Superintendencia va a preguntar.", alto=0.85)

tesis(p, "// LA PRIMERA TESIS DE LA SESIÓN",
      ["UNA LLAVE SIN DUEÑO,", "SIN FECHA Y SIN ACTA", "NO ES UN CONTROL:", "ES UNA DEUDA."],
      "Los cinco hallazgos de gestión de este caso — la llave del código, la del respaldo, la de la autoridad "
      "interna, las de los cajeros y la ausencia de inventario — tienen la misma forma. En todos, el algoritmo "
      "era correcto y lo que faltaba era alguien que respondiera por la llave, una fecha en la que dejara de "
      "valer y un documento que probara quién la conoció. Eso no se compra: se gobierna. Y es exactamente lo "
      "que el comité les está pidiendo.", sig())

s, y = base(p, "// 13  HARDWARE", "MÓDULOS DE HARDWARE: QUÉ SE COMPRA REALMENTE", sig(), titulo_tam=22)
y = intro(s, y, "Cuando alguien propone comprar un módulo de hardware, lo que hay que preguntar no es la marca: "
                "es el nivel certificado, porque de ahí depende si sirve para lo que se quiere.")
y = tabla(s, y, ["NIVEL", "QUÉ GARANTIZA", "PARA QUÉ ALCANZA"], [
    [("Nivel 1", {"bold": True}), "Requisitos criptográficos básicos. Puede ser puro software", "Cumplimiento formal. No protege la llave de quien administre el equipo"],
    [("Nivel 2", {"bold": True}), "Evidencia física de manipulación y autenticación por rol", "Entornos controlados con vigilancia física"],
    [("Nivel 3", {"bold": True, "color": NARANJA}), "Resistencia física activa: ante intrusión, borra las llaves. Autenticación por identidad", "Es el nivel habitual del sector financiero, y el que aplica a este caso"],
    [("Nivel 4", {"bold": True}), "Protección total, incluida la detección de ataques por temperatura o voltaje", "Entornos hostiles o de altísima exigencia. Rara vez necesario"],
], [1.7, 4.7, 3.6], alto_fila=0.54)
nota(s, y, "// LA PREGUNTA QUE DESARMA UNA PROPUESTA COMERCIAL",
     "¿La llave se genera dentro del módulo y no puede salir nunca, o se genera fuera y se importa? "
     "<b>Si puede salir, el módulo es un lugar cómodo donde guardarla, no una garantía de custodia exclusiva.</b>", alto=0.78)

s, y = base(p, "// 14  NUBE", "CUSTODIA DE LLAVES EN LA NUBE", sig())
y = intro(s, y, "Casi ninguna organización monta hoy su propio módulo: lo alquila. Eso está bien, y cambia las "
                "preguntas que hay que hacer, no la responsabilidad.")
y = tabla(s, y, ["MODELO", "QUIÉN CONTROLA LA LLAVE", "CUÁNDO CONVIENE"], [
    [("Llaves administradas por el proveedor", {"bold": True}), "El proveedor, por completo. El cliente solo elige activarlo", "Datos de sensibilidad baja o media, cuando lo que se busca es no tener que operar nada"],
    [("Llaves del cliente dentro del servicio", {"bold": True, "color": NARANJA}), "El cliente define políticas, permisos y rotación; el proveedor opera el módulo", "El punto de equilibrio habitual, y el razonable para Coopaburrá"],
    [("Llave propia importada", {"bold": True}), "El cliente la genera en su propia ceremonia y la importa", "Cuando hay que poder demostrar el origen de la llave ante un supervisor"],
    [("Módulo externo bajo control propio", {"bold": True}), "El cliente, incluso frente al proveedor de nube", "Datos que no pueden quedar accesibles al proveedor por requisito legal o contractual"],
], [3.0, 3.8, 3.2], alto_fila=0.50)
nota(s, y, "// LAS CUATRO PREGUNTAS PARA EL CONTRATO",
     "¿En qué país reside la llave? ¿Puede el proveedor acceder a ella, y bajo qué orden judicial? ¿Qué registro "
     "de uso queda y quién lo audita? ¿Y qué pasa con las llaves el día que se termine el contrato? "
     "<b>Delegar la operación no delega la responsabilidad ante la Superintendencia.</b>", alto=0.85)

s, y = base(p, "// 15  TÉCNICA", "TOKENIZACIÓN: SUSTITUIR EN VEZ DE CIFRAR", sig(), titulo_tam=24)
y = intro(s, y, "La técnica que más reduce el riesgo cuando el dato no se necesita en claro para operar. En lugar de "
                "cifrarlo, se reemplaza por un sustituto que no tiene ninguna relación matemática con él.")
y = bloque_codigo(s, y, [
    "Número de tarjeta:   4000 1234 5678 9010",
    "Token:               4000 1293 8841 9010     ← mismo formato, sin relación con el original",
    "",
    "La correspondencia entre token y dato real vive en una bóveda, separada y custodiada.",
    "Los demás sistemas solo ven el token: pueden operar, conciliar y reportar",
    "sin haber tenido nunca el dato real.",
], titulo="TOKENIZACIÓN CON BÓVEDA")
nota(s, y, "// DOS VARIANTES",
     "Con bóveda: una tabla protegida guarda la correspondencia. Sin bóveda: el token se calcula con un cifrado que "
     "conserva el formato, como el FF1 de la NIST SP 800-38G. <b>La primera es más simple de razonar; la segunda "
     "escala mejor</b>, y exige custodiar una llave.", alto=0.85)

s, y = base(p, "// 16  TÉCNICA", "TOKENIZACIÓN FRENTE A CIFRADO", sig())
y = intro(s, y, "No compiten: resuelven problemas distintos. La pregunta que decide es si el sistema necesita el "
                "dato real para hacer su trabajo.")
y = tabla(s, y, ["CRITERIO", "CIFRADO", "TOKENIZACIÓN"], [
    [("Relación con el dato", {"bold": True}), "Matemática: con la llave se recupera", "Ninguna: solo la bóveda conoce la correspondencia"],
    [("Formato", {"bold": True}), "El resultado es otro tipo de dato, más largo", "Puede conservar el formato: los sistemas no cambian"],
    [("Si se roba lo protegido", {"bold": True}), "A salvo mientras la llave lo esté", "El token no sirve de nada fuera del sistema"],
    [("Qué hay que custodiar", {"bold": True}), "La llave", "La bóveda, o la llave si es sin bóveda"],
    [("Alcance de auditoría", {"bold": True, "color": NARANJA}), "Todo sistema que tenga la llave", "Solo la bóveda y lo que la consulta: el resto sale del alcance"],
    [("Mejor para", {"bold": True}), "Datos que se usan en claro con frecuencia", "Identificadores que se guardan y se comparan, pero casi nunca se leen"],
], [2.6, 3.6, 3.8], alto_fila=0.42)

s, y = base(p, "// 17  CASO", "TOKENIZACIÓN EN COOPABURRÁ", sig())
y = intro(s, y, "Tres datos del caso donde la tokenización resuelve mejor que el cifrado, y uno donde no tiene "
                "sentido.")
y = tabla(s, y, ["DATO", "¿QUIÉN LO NECESITA EN CLARO?", "RECOMENDACIÓN"], [
    [("Número de tarjeta de los asociados", {"bold": True, "color": NARANJA}), "Solo el autorizador de transacciones", "Tokenizar: saca de la norma de tarjetas a todos los demás sistemas"],
    [("Cédula en analítica y en archivos para terceros", {"bold": True}), "Nadie: basta un identificador estable", "Tokenizar. Resumirla no sirve: se revierte, como en la sesión 3"],
    [("Cédula en el core", {"bold": True}), "Varios procesos, todos los días", "Cifrado de campo con índice ciego, como en la sesión 2"],
    [("Saldo", {"bold": True}), "La operación completa, todo el tiempo", "Cifrado de campo y control de acceso; tokenizarlo no tiene sentido"],
], [3.4, 3.1, 3.5], alto_fila=0.50)
nota(s, y, "// EL ARGUMENTO ANTE EL COMITÉ",
     "Tokenizar la tarjeta <b>reduce el número de sistemas que audita la norma de tarjetas</b>, y con eso su costo "
     "anual. Es de las pocas medidas de seguridad que se pueden presentar como ahorro.", alto=0.78)

s, y = base(p, "// 18  CASO", "LA LLAVE DEL RESPALDO, VISTA DESDE LA GESTIÓN", sig(), titulo_tam=24)
y = intro(s, y, "El hallazgo H4 lo diagnosticaron en la sesión 2. Ahora ya se puede decir dónde debería estar esa "
                "llave y por qué, que es lo que el informe necesita.")
y = dos_columnas(s, y,
    ("// POR QUÉ ESTÁ DONDE ESTÁ", [
        "Porque el guion de respaldo debe ejecutarse solo, de madrugada, sin intervención humana.",
        "Es una necesidad operativa real, y por eso la solución no puede ser simplemente quitar el archivo.",
        "Quien lo diseñó no fue negligente: resolvió el problema que tenía delante sin el marco que ustedes ya tienen."]),
    ("// DÓNDE DEBERÍA ESTAR", [
        "En un servicio de gestión de llaves, al que el proceso de respaldo se autentica <b>como proceso</b>, con permiso solo para cifrar.",
        "Y con una llave distinta para descifrar, cuyo uso exija aprobación de una persona y quede registrado.",
        "Así, quien tenga el archivo de respaldo no puede leerlo, y quien pueda leerlo no tiene el archivo. Eso es separación de funciones."]),
    alto=2.20)

s, y = base(p, "// 19  INCIDENTE", "QUÉ SE HACE CUANDO UNA LLAVE SE COMPROMETE", sig(), titulo_tam=22)
y = intro(s, y, "Rotar por calendario es rutina. Rotar por incidente es otra cosa, y conviene tener el "
                "procedimiento escrito antes de necesitarlo.")
y = pasos(s, y + 0.05, [
    ("Declarar, revocar y reemplazar",
     "En ese orden y sin improvisar. Revocar el certificado asociado, emitir la llave nueva y distribuirla por el procedimiento previsto."),
    ("Determinar el alcance: qué protegió esa llave y durante cuánto tiempo",
     "Sin inventario este paso es imposible, y es el que decide todo lo demás. Es la razón práctica por la que H8 va primero."),
    ("Reclasificar lo protegido",
     "Lo cifrado con esa llave se considera expuesto. Lo firmado en el periodo se considera dudoso, salvo que haya sello de tiempo que acote la ventana."),
    ("Preservar evidencia y notificar",
     "El equipo comprometido no se formatea: se preserva. Y hay obligaciones de notificación a titulares y al supervisor que no las decide el área técnica."),
], alto=0.84)

# ─────────────── SECCIÓN 03 ───────────────
seccion(p, "03", "LABORATORIO 6",
        "Treinta minutos · Repartir un secreto, rotar sin recifrar y tokenizar, en Python", sig())

s, y = base(p, "// 20  LABORATORIO", "LOS TRES EJERCICIOS", sig())
y = pasos(s, y + 0.05, [
    ("Ejercicio 1 · Repartir la llave de los cajeros entre cinco custodios",
     "Con un umbral de tres, repartan una llave de 128 bits, reconstrúyanla con tres partes y comprueben que con dos no se obtiene nada."),
    ("Ejercicio 2 · Rotar la llave maestra sin tocar los datos",
     "Cifren mil registros en sobre, roten la llave que cifra las llaves y verifiquen que todos siguen legibles. Midan cuánto tardó frente a recifrarlo todo."),
    ("Ejercicio 3 · Tokenizar las cédulas de un archivo de analítica",
     "Reemplacen cada cédula por un token aleatorio, guarden la correspondencia aparte y expliquen qué puede hacer un tercero con el archivo y qué no."),
], alto=0.92)
nota(s, y, "// LO QUE SE ENTREGA",
     "Una página por equipo con los tres resultados y, sobre todo, <b>la respuesta del ejercicio 3</b>: va directo a "
     "la recomendación de la entrega final.", alto=0.72)

s, y = base(p, "// 21  PYTHON", "LABORATORIO 6 · EL EJERCICIO EN PYTHON", sig())
y = intro(s, y, "Los tres ejercicios con la biblioteca estándar, cryptography y pycryptodome, que trae una "
                "implementación del reparto de Shamir.")
y = bloque_codigo(s, y, [
    "# pip install cryptography pycryptodome",
    "import os, secrets",
    "from Crypto.Protocol.SecretSharing import Shamir",
    "from cryptography.hazmat.primitives.keywrap import aes_key_wrap, aes_key_unwrap",
    "llave_cajeros = os.urandom(16)",
    "partes = Shamir.split(3, 5, llave_cajeros)              # cinco custodios, umbral de tres",
    "assert Shamir.combine(partes[:3]) == llave_cajeros        # tres partes bastan",
    "kek_vieja, kek_nueva = os.urandom(32), os.urandom(32)",
    "dek_envuelta = aes_key_wrap(kek_vieja, os.urandom(32))",
    "dek_rotada = aes_key_wrap(kek_nueva, aes_key_unwrap(kek_vieja, dek_envuelta))",
    "token = secrets.token_hex(8)                             # sustituto sin relación con la cédula",
], titulo="LABORATORIO 6 · PYTHON 3 + CRYPTOGRAPHY + PYCRYPTODOME")
nota(s, y, "// LA PREGUNTA DEL EJERCICIO 2",
     "¿Qué cambió en la base al rotar la llave maestra? Solo las llaves envueltas, de 40 bytes cada una. <b>Esa es la "
     "respuesta a quien diga que rotar llaves es inviable.</b>", alto=0.72)

seccion(p, "04", "VEINTE AÑOS",
        "Cómo se conserva una prueba electrónica más tiempo del que dura su tecnología", sig())

s, y = base(p, "// 22  PROBLEMA", "LA FIRMA TAMBIÉN ENVEJECE", sig())
y = intro(s, y, "Una firma digital perfectamente válida hoy puede ser imposible de verificar en quince años, sin "
                "que nadie haya hecho nada malo. Esta es la parte del hallazgo H7 que no se resuelve firmando.")
y = tabla(s, y, ["QUÉ CADUCA", "POR QUÉ", "QUÉ PASA SI NO SE PREVÉ"], [
    [("El certificado del firmante", {"bold": True}), "Vence en pocos años, o se revoca antes", "No se puede comprobar que la llave era suya en el momento de firmar"],
    [("El algoritmo", {"bold": True, "color": NARANJA}), "SHA-1 era aceptable en 2005 y dejó de serlo. RSA 2048 tiene fecha", "La firma deja de constituir prueba, aunque el archivo esté intacto"],
    [("La información de verificación", {"bold": True}), "Las listas de revocación y las respuestas en línea no se guardan para siempre", "No hay forma de reconstruir el estado del certificado en aquella fecha"],
    [("El formato y el soporte", {"bold": True}), "Veinte años son varias generaciones de software y de medios", "El archivo existe y nadie puede abrirlo"],
], [3.0, 3.8, 3.2], alto_fila=0.56)

s, y = base(p, "// 23  SOLUCIÓN", "SELLO DE TIEMPO: QUÉ ES Y QUÉ PRUEBA", sig())
y = intro(s, y, "Es la pieza que quedó pendiente desde la sesión 4, y la que convierte una firma en una prueba "
                "fechada por alguien distinto de la parte interesada.")
y = bloque_codigo(s, y, [
    "  1. Se calcula el resumen del documento ya firmado.",
    "  2. Se envía ese resumen — no el documento — a una autoridad de sellado.",
    "  3. La autoridad le añade su fuente de tiempo y firma el conjunto.",
    "",
    "  Resultado: una afirmación firmada por un tercero que dice",
    "             \"este documento existía exactamente así, en este instante\".",
    "",
    "La autoridad nunca ve el contenido: solo el resumen. La confidencialidad",
    "del expediente se conserva intacta.",
], titulo="SELLADO CRONOLÓGICO")
nota(s, y, "// LO QUE ESTO RESUELVE EN EL CASO",
     "Sin sello, la fecha de la hipoteca la pone el reloj de un servidor de la cooperativa, que es parte "
     "interesada. <b>Con sello, la fecha la certifica un tercero</b>, y además queda probado que la firma se hizo "
     "cuando el certificado todavía estaba vigente.", alto=0.82)

s, y = base(p, "// 24  CONSERVACIÓN", "CÓMO SE CONSERVA UNA FIRMA VEINTE AÑOS", sig(), titulo_tam=24)
y = intro(s, y, "Existen formatos de firma diseñados exactamente para esto. La idea es sencilla y conviene "
                "explicarla así en el informe, sin nombres de norma.")
y = pasos(s, y + 0.05, [
    ("Se guarda todo lo necesario para verificar, junto con el documento",
     "La cadena de certificados completa y el estado de revocación de ese día. Así no hay que consultar nada en el futuro."),
    ("Se sella el conjunto con un sello de tiempo",
     "El sello cubre el documento, la firma y la evidencia de verificación. Congela el estado completo en una fecha."),
    ("Antes de que el sello envejezca, se vuelve a sellar por encima",
     "Con algoritmos vigentes en ese momento. Cada sello nuevo protege a todos los anteriores, como capas."),
    ("Se repite indefinidamente, cada pocos años",
     "Mientras se mantenga la cadena de sellos, la firma original sigue siendo verificable aunque su algoritmo ya no se use."),
], alto=0.78)
nota(s, y, "// POR QUÉ ES UN SERVICIO Y NO UNA COMPRA",
     "El resellado es una tarea periódica que alguien tiene que ejecutar durante dos décadas. <b>Si no hay un "
     "responsable y un presupuesto anual, el esquema se rompe solo en el tercer año</b>, y nadie se entera "
     "hasta el día del litigio.", alto=0.80)

s, y = base(p, "// 25  NORMA", "LOS NIVELES DE FIRMA PARA CONSERVAR: B, T, LT Y LTA", sig(), titulo_tam=22)
y = intro(s, y, "Los cuatro pasos de la diapositiva anterior tienen nombre en las normas europeas de firma avanzada, "
                "que son las que implementan los proveedores y las que hay que exigir en el contrato.")
y = tabla(s, y, ["NIVEL", "QUÉ AGREGA", "QUÉ RESUELVE"], [
    [("B · básico", {"bold": True}), "La firma con su certificado", "Integridad y autoría, mientras el certificado esté vigente"],
    [("T · con tiempo", {"bold": True}), "Un sello de tiempo de un tercero", "La prueba de cuándo se firmó"],
    [("LT · largo plazo", {"bold": True}), "La cadena y el estado de revocación, dentro del documento", "Verificar sin depender de servicios que ya no existan"],
    [("LTA · archivo", {"bold": True, "color": NARANJA}), "Sellos de archivo sucesivos sobre todo lo anterior", "Mantener la prueba cuando el algoritmo original envejezca"],
], [2.4, 3.9, 3.7], alto_fila=0.50)
nota(s, y, "// QUÉ PEDIR EN EL CONTRATO",
     "Para los pagarés de Coopaburrá: firma en PDF con nivel LTA, que en la norma se llama PAdES, <b>y el servicio de "
     "resellado periódico incluido</b>, con su costo anual. Pedir solo «firma digital» deja por fuera tres cuartas "
     "partes del problema.", alto=0.85)

s, y = base(p, "// 26  CASO", "EL HALLAZGO H7, CERRADO", sig())
y = intro(s, y, "Con esto ya está completa la respuesta que el comité pedía en febrero. Así se ve el esquema "
                "propuesto, de principio a fin.")
y = tabla(s, y, ["PIEZA", "QUÉ APORTA AL EXPEDIENTE"], [
    [("Firma digital con certificado de entidad acreditada", {"bold": True}), "Atribución al titular, con la presunción legal que la firma electrónica genérica no tiene"],
    [("Llave privada del asociado bajo su control exclusivo", {"bold": True}), "Es el requisito que convierte la firma en confiable. Sin él, lo demás no sostiene"],
    [("Sello de tiempo de un tercero", {"bold": True, "color": NARANJA}), "Fecha cierta, independiente del reloj de la cooperativa"],
    [("Evidencia de verificación guardada con el documento", {"bold": True}), "Permite verificar dentro de veinte años sin consultar servicios que ya no existirán"],
    [("Resellado periódico", {"bold": True}), "Mantiene la verificabilidad cuando el algoritmo original envejezca"],
    [("Custodia con integridad demostrable", {"bold": True}), "El registro encadenado de la sesión 3, para que la parte interesada no sea la única fuente"],
], [4.4, 5.6], alto_fila=0.44)

s, y = base(p, "// 27  DECISIÓN", "Y LO QUE YA SE FIRMÓ CON UNA IMAGEN", sig())
y = intro(s, y, "Lo anterior sirve de aquí en adelante. Para la cartera vigente no hay solución técnica completa, "
                "y por eso es una decisión del comité y no del área de tecnología.")
y = tabla(s, y, ["OPCIÓN", "QUÉ LOGRA", "QUÉ NO LOGRA"], [
    [("Sellar hoy los documentos existentes", {"bold": True}), "Prueba que el documento existía así desde hoy, y congela cualquier alteración futura", "No prueba nada sobre lo ocurrido antes de hoy, que es justo lo discutible"],
    [("Volver a firmar con el asociado", {"bold": True}), "Expediente completo y sólido", "Costo y fricción comercial enormes. Y muchos asociados no van a volver a firmar"],
    [("Documentar el riesgo y provisionarlo", {"bold": True, "color": NARANJA}), "Es honesto, es defendible ante la Superintendencia y tiene un número asociado", "No mejora la posición probatoria en un litigio concreto"],
], [3.2, 3.6, 3.2], alto_fila=0.66)
nota(s, y, "// LA RECOMENDACIÓN QUE SE ESPERA DE UN ESPECIALISTA",
     "Las tres a la vez, priorizadas: sellar ya lo existente porque es barato y detiene el deterioro, volver a "
     "firmar solo la cartera de mayor exposición, y provisionar el resto. <b>Elegir una sola es lo que delata "
     "un informe superficial.</b>", alto=0.80)

# ─────────────── SECCIÓN 04 ───────────────
seccion(p, "05", "LO QUE VIENE",
        "Bloque 12 · Transición post-cuántica y criptoagilidad", sig())

s, y = base(p, "// 28  PORQUÉ", "POR QUÉ ESTO NO ES UN TEMA DE CIENCIA FICCIÓN", sig(), titulo_tam=24)
y = intro(s, y, "La pregunta correcta no es cuándo habrá un computador cuántico. Es si el dato que estoy "
                "protegiendo hoy seguirá siendo sensible cuando lo haya.")
y = bloque_codigo(s, y, [
    "  vida útil del dato  +  tiempo que toma migrar   >   años hasta la amenaza",
    "                                                  ⇒   ya vamos tarde",
    "",
    "  Para una hipoteca de Coopaburrá:",
    "      vida útil del dato ................. 20 años",
    "      tiempo de migración en una entidad .. 3 a 5 años",
    "                                            ────────",
    "                                            23 a 25 años",
    "",
    "  No hay que decidir si la amenaza llega antes de 2050. Hay que decidir",
    "  qué se firma hoy sabiendo que debe resistir hasta 2046.",
], titulo="LA CUENTA QUE HAY QUE HACER")

s, y = base(p, "// 29  ALCANCE", "QUÉ SE ROMPE Y QUÉ NO", sig())
y = intro(s, y, "Es la tabla que más se malinterpreta del tema. No todo cae, y saber distinguir evita gastar "
                "donde no hace falta.")
y = tabla(s, y, ["MECANISMO", "EFECTO DE UN COMPUTADOR CUÁNTICO", "QUÉ HACER"], [
    [("RSA, curvas elípticas, acuerdo de llave", {"bold": True, "color": NARANJA}), "Se rompen por completo. Un algoritmo conocido desde 1994 los resuelve", "Migrar a los algoritmos nuevos. Es lo urgente"],
    [("Cifrado simétrico: AES", {"bold": True}), "Se debilita a la mitad, no se rompe", "Usar llaves de 256 bits. Con eso queda resuelto"],
    [("Funciones resumen", {"bold": True}), "Se debilitan, no se rompen", "Preferir salidas de 384 bits en adelante para datos de larga vida"],
    [("Firmas ya hechas", {"bold": True}), "No se alteran, pero se vuelven falsificables hacia adelante", "Resellar con algoritmos nuevos antes de que eso ocurra"],
], [3.3, 4.3, 2.4], alto_fila=0.54)

s, y = base(p, "// 30  ESTÁNDAR", "LOS ALGORITMOS YA ESTÁN PUBLICADOS", sig())
y = intro(s, y, "Esto dejó de ser investigación en agosto de 2024. Ya hay normas publicadas y productos que las "
                "implementan, así que la pregunta pasó de si migrar a cuándo y en qué orden.")
y = tabla(s, y, ["NORMA", "QUÉ ESTANDARIZA", "PARA QUÉ SE USA"], [
    [("FIPS 203", {"bold": True, "color": NARANJA}), "Encapsulamiento de llave, basado en retículos", "Reemplaza el acuerdo de llave: es lo primero que hay que migrar"],
    [("FIPS 204", {"bold": True}), "Firma digital basada en retículos", "La firma de propósito general, para la mayoría de los usos"],
    [("FIPS 205", {"bold": True}), "Firma digital basada en funciones resumen", "Más lenta y más grande, pero su seguridad descansa en supuestos muy conservadores"],
    [("Algoritmo de respaldo", {"bold": True}), "Un segundo mecanismo de encapsulamiento, de familia matemática distinta", "Para no depender de un único supuesto matemático"],
], [2.2, 4.2, 3.6], alto_fila=0.54)
nota(s, y, "// EL PLAZO QUE MANEJAN LOS GOBIERNOS",
     "Las guías de transición de los organismos de seguridad nacional apuntan a tener los sistemas críticos "
     "migrados hacia 2035, empezando <b>ahora</b> por lo que protege datos de larga vida. La cartera hipotecaria "
     "de Coopaburrá entra exactamente en esa categoría.", alto=0.82)

s, y = base(p, "// 31  CALENDARIO", "CNSA 2.0: EL CALENDARIO QUE SIGUEN LOS FABRICANTES", sig(), titulo_tam=22)
y = intro(s, y, "La suite de la agencia de seguridad nacional de Estados Unidos no obliga a una cooperativa "
                "colombiana, pero es el calendario que siguen los fabricantes, y por eso fija de hecho cuándo "
                "llegarán los productos.")
y = tabla(s, y, ["TIPO DE SISTEMA", "ADMITIR Y PREFERIR", "USAR EXCLUSIVAMENTE"], [
    [("Firma de software y de firmware", {"bold": True, "color": NARANJA}), "2025", "2030"],
    [("Equipos de red tradicionales", {"bold": True}), "2026", "2030"],
    [("Navegadores, servidores y servicios en la nube", {"bold": True}), "2025", "2033"],
    [("Sistemas operativos", {"bold": True}), "2027", "2033"],
    [("Aplicaciones a la medida y equipos heredados", {"bold": True}), "—", "Actualizar o reemplazar hacia 2033"],
], [5.0, 2.4, 2.6], alto_fila=0.40)
nota(s, y, "// LO QUE HAY QUE LEER EN ESTA TABLA",
     "Los cajeros y el hardware de red entran en la ola de 2030. <b>Un equipo que Coopaburrá compre hoy seguirá en "
     "servicio en 2030</b>: la pregunta de si admite ML-KEM-1024 y ML-DSA-87, los algoritmos de la suite, va en el "
     "pliego de esta compra, no de la próxima. La meta general es 2035.", alto=0.92)

s, y = base(p, "// 32  CALENDARIO", "NIST IR 8547: EL FIN ANUNCIADO DE RSA Y LAS CURVAS", sig(), titulo_tam=22)
y = intro(s, y, "El borrador del NIST de noviembre de 2024 pone fecha a lo que la sesión 4 dejó anunciado. Es la "
                "referencia que tendrá en la mano un supervisor cuando pregunte por el plan de transición.")
y = tabla(s, y, ["HITO", "QUÉ SIGNIFICA", "PARA COOPABURRÁ"], [
    [("Después de 2030", {"bold": True}), "Se desaprueban RSA y las curvas con seguridad de 112 bits, como RSA-2048", "No deben usarse en sistemas nuevos: el certificado RSA-2048 del portal entra aquí"],
    [("Después de 2035", {"bold": True, "color": NARANJA}), "Se prohíben RSA, Diffie-Hellman y las curvas elípticas, sin importar el tamaño", "Ninguna firma de los pagarés debería depender solo de ellos"],
    [("Mientras tanto", {"bold": True}), "Esquemas híbridos y migración por prioridad de exposición", "Primero lo que protege datos de vida larga: las hipotecas"],
], [2.2, 4.0, 3.8], alto_fila=0.58)
nota(s, y, "// LA DIFERENCIA ENTRE LAS DOS PALABRAS",
     "Desaprobado significa que se tolera con el riesgo aceptado y documentado; prohibido significa que deja de "
     "cumplir. <b>Entre 2030 y 2035 está la pista de aterrizaje</b>, y es más corta de lo que parece para una entidad "
     "que renueva sistemas cada diez años.", alto=0.85)

s, y = base(p, "// 33  CIFRAS", "EL TAMAÑO IMPORTA: LAS LLAVES POST-CUÁNTICAS EN CIFRAS", sig(), titulo_tam=22)
y = intro(s, y, "La consecuencia práctica más inmediata de la transición no es de seguridad sino de tamaño. Estos "
                "son los números de los estándares, frente a lo que se usa hoy.")
y = tabla(s, y, ["ESQUEMA", "LLAVE PÚBLICA", "CIFRADO O FIRMA", "FRENTE A HOY"], [
    [("X25519 · acuerdo clásico", {"bold": True}), "32 bytes", "32 bytes", "Referencia"],
    [("ML-KEM-768 · acuerdo post-cuántico", {"bold": True, "color": NARANJA}), "1.184 bytes", "1.088 bytes", "Unas 37 veces más"],
    [("Ed25519 · firma clásica", {"bold": True}), "32 bytes", "64 bytes", "Referencia"],
    [("ML-DSA-65 · firma post-cuántica", {"bold": True, "color": NARANJA}), "1.952 bytes", "3.309 bytes", "Unas 50 veces más en la firma"],
    [("SLH-DSA-128s · firma conservadora", {"bold": True}), "32 bytes", "7.856 bytes", "Llave mínima, firma enorme"],
], [3.8, 2.0, 2.0, 2.2], alto_fila=0.40)
nota(s, y, "// DÓNDE DUELE",
     "Un certificado con firma post-cuántica ocupa varias veces más, y una cadena completa puede no caber en los "
     "primeros paquetes del apretón de manos. <b>Los cajeros, los lectores de tarjetas y los enlaces lentos son los "
     "que más lo van a sentir</b>, y por eso el inventario tiene que incluir el hardware.", alto=0.88)

s, y = base(p, "// 34  MIGRACIÓN", "CÓMO SE MIGRA SIN APOSTARLO TODO", sig())
y = dos_columnas(s, y,
    ("// MODO HÍBRIDO", [
        "Se combinan el algoritmo clásico y el nuevo, de modo que <b>haya que romper los dos</b> para comprometer la comunicación.",
        "Protege contra dos riesgos opuestos: que el clásico caiga por un avance cuántico, y que el nuevo caiga por un fallo de diseño todavía no descubierto.",
        "Es la forma en que se está desplegando hoy en los canales seguros de internet."]),
    ("// LO QUE CAMBIA EN LA PRÁCTICA", [
        "Las llaves y las firmas nuevas son <b>mucho más grandes</b>: eso afecta al tamaño de los mensajes, a los certificados y a los dispositivos con memoria limitada.",
        "Los cajeros, los lectores de tarjetas y el hardware embebido son los que más van a sufrir, y son los que más tardan en renovarse.",
        "Por eso el inventario tiene que incluir el hardware, no solo el software."]),
    alto=2.15)

s, y = base(p, "// 35  DISEÑO", "CRIPTOAGILIDAD: DISEÑAR PARA PODER CAMBIAR", sig(), titulo_tam=24)
y = intro(s, y, "La lección de todo el módulo, convertida en requisito de arquitectura. Ningún algoritmo dura "
                "para siempre, así que el sistema tiene que poder cambiarlos sin rehacerse.")
y = tabla(s, y, ["PRÁCTICA", "QUÉ PERMITE"], [
    [("El algoritmo no está escrito dentro del código, sino en configuración", {"bold": True}), "Cambiarlo sin recompilar ni publicar una versión nueva en la tienda"],
    [("Cada dato cifrado o firmado lleva anotado con qué se produjo", {"bold": True, "color": NARANJA}), "Convivencia de dos algoritmos durante la transición, y migración gradual"],
    [("Existe un inventario que dice dónde se usa cada algoritmo", {"bold": True}), "Estimar el alcance de un cambio en horas, no en meses. Es el hallazgo H8 otra vez"],
    [("Las llaves tienen identificador y versión", {"bold": True}), "Rotar sin ambigüedad y saber qué llave descifra qué"],
    [("Hay pruebas automatizadas del cambio de algoritmo", {"bold": True}), "Que la migración sea un procedimiento ensayado y no un evento"],
], [5.0, 5.0], alto_fila=0.48)

s, y = base(p, "// 36  ACCIÓN", "QUÉ DEBERÍA HACER COOPABURRÁ ESTE AÑO", sig())
y = pasos(s, y + 0.05, [
    ("Incluir el algoritmo y el tamaño de llave en el inventario criptográfico",
     "No es trabajo nuevo: es una columna más en el inventario de la entrega 1. Sin ella no se puede estimar nada."),
    ("Marcar los datos de vida larga",
     "Hipotecas, historia de aportes, expedientes laborales. Son los que hay que migrar primero, no los más visibles."),
    ("Exigir criptoagilidad en las compras y en los contratos con proveedores",
     "La fábrica de software y el proveedor de cajeros deben comprometerse por escrito a soportar los algoritmos nuevos, con fecha."),
    ("Usar AES-256 y resúmenes de 384 bits en todo lo nuevo",
     "Es gratis, es hoy, y quita de la lista de preocupaciones todo el lado simétrico."),
], alto=0.84)

s, y = base(p, "// 37  INVENTARIO", "EL INVENTARIO CRIPTOGRÁFICO MADURO", sig())
y = intro(s, y, "Cerramos donde empezamos. Aquel de la entrega 1 era una lista; este es el instrumento de gestión "
                "que el módulo completo justifica. Estas son las columnas que debería tener al final.")
y = tabla(s, y, ["COLUMNA", "PARA QUÉ SIRVE", "QUÉ PREGUNTA RESPONDE"], [
    [("Identificador y propósito", {"bold": True}), "Distinguir llaves y evitar reutilización entre usos", "¿Cuántas llaves hay y para qué?"],
    [("Algoritmo y tamaño", {"bold": True, "color": NARANJA}), "Detectar lo que está fuera de política y estimar la migración", "¿Qué hay que cambiar antes de 2030?"],
    [("Dónde reside y bajo qué custodia", {"bold": True}), "Saber el nivel de protección real de cada una", "¿Qué pasa si se compromete ese equipo?"],
    [("Responsable, por rol", {"bold": True}), "Que la salida de una persona no deje llaves huérfanas", "¿Quién responde por esta llave hoy?"],
    [("Fecha de creación y de rotación", {"bold": True}), "Convertir la rotación en una tarea programada", "¿Cuáles están vencidas ahora mismo?"],
    [("Sistemas que dependen de ella", {"bold": True}), "Estimar el impacto de rotarla o retirarla", "¿Qué se cae si la cambio?"],
    [("Vida útil del dato que protege", {"bold": True}), "Priorizar la migración post-cuántica por exposición real", "¿Qué hay que migrar primero?"],
], [3.1, 3.9, 3.0], alto_fila=0.40)

s, y = base(p, "// 38  GOBIERNO", "QUÉ SE LE REPORTA AL COMITÉ CADA MES", sig())
y = intro(s, y, "Un comité no quiere ver hallazgos todos los meses: quiere ver si la situación mejora o empeora. "
                "Seis indicadores bastan, y todos salen del inventario.")
y = tabla(s, y, ["INDICADOR", "POR QUÉ ESE Y NO OTRO"], [
    [("Porcentaje de llaves con responsable nombrado", {"bold": True}), "Es el que más rápido revela el problema de fondo, y el más barato de corregir"],
    [("Certificados que vencen en los próximos 60 días", {"bold": True, "color": NARANJA}), "Convierte en rutina lo que hoy es una sorpresa cada tanto"],
    [("Llaves fuera de su periodo de rotación", {"bold": True}), "Si esta cifra no baja, la política existe solo en el papel"],
    [("Algoritmos en uso fuera de la política vigente", {"bold": True}), "Es el tablero de la migración, incluida la post-cuántica"],
    [("Llaves encontradas fuera del inventario en el último barrido", {"bold": True}), "Mide si el inventario refleja la realidad o solo la intención"],
    [("Hallazgos abiertos por antigüedad", {"bold": True}), "Distingue lo que se está resolviendo de lo que solo se está registrando"],
], [4.8, 5.2], alto_fila=0.44)

s, y = base(p, "// 39  NORMA", "LO QUE LE EXIGEN A COOPABURRÁ, Y DE DÓNDE SALE", sig(), titulo_tam=22)
y = intro(s, y, "Para la sustentación conviene poder decir de dónde sale cada obligación. Ustedes ya vieron el "
                "marco legal conmigo; esto es solo el recorte que aplica a este módulo.")
y = tabla(s, y, ["FUENTE", "QUÉ EXIGE EN MATERIA CRIPTOGRÁFICA"], [
    [("Ley 527 de 1999", {"bold": True}), "Condiciones para que un mensaje de datos y una firma tengan valor probatorio, y que la información se conserve accesible y consultable con su origen, destino y fecha"],
    [("Régimen de protección de datos personales", {"bold": True, "color": NARANJA}), "Medidas de seguridad sobre los datos de los 142.000 asociados, y deber de informar incidentes que los afecten"],
    [("Instrucciones de la Superintendencia Financiera", {"bold": True}), "Requisitos mínimos de seguridad de la información y ciberseguridad para sus vigilados. Citen la circular vigente al momento del informe, no una de memoria"],
    [("Normas de la industria de medios de pago", {"bold": True}), "Gestión de llaves de los cajeros y protección de datos de tarjeta, con exigencias explícitas de rotación y custodia"],
], [3.4, 6.6], alto_fila=0.60)

# ─────────────── SECCIÓN 05 ───────────────
seccion(p, "06", "EVALUACIÓN Y CIERRE",
        "Quiz 2, sustentación de la hoja de ruta y cierre del módulo", sig())

s, y = base(p, "// 40  QUIZ", "QUIZ 2 · QUINCE MINUTOS", sig())
y = intro(s, y, "Cubre las sesiones 4, 5 y 6. Mismo formato del primero: preguntas de criterio, no de memoria. "
                "Ninguna pregunta se responde recordando un nombre.")
y = tarjetas(s, y, [
    ("// LO QUE ENTRA", [
        "Llave pública y firma digital: qué prueba y qué no.",
        "Certificados: la cadena, las comprobaciones y el ciclo de vida.",
        "Canal seguro: versiones, confidencialidad persistente y límites.",
        "Gestión de llaves: ciclo, ceremonias, jerarquía y rotación.",
        "Conservación y transición post-cuántica."]),
    ("// CÓMO SE PREGUNTA", [
        "Un escenario corto y una decisión que justificar.",
        "Por ejemplo: un proveedor propone algo, ¿qué le preguntan antes de aceptarlo y por qué?",
        "<b>Se evalúa el criterio y la justificación.</b> Una respuesta correcta sin argumento vale la mitad."]),
], alto=2.10)

s, y = base(p, "// 41  SUSTENTACIÓN", "LA SUSTENTACIÓN ANTE EL COMITÉ", sig())
y = intro(s, y, "Setenta minutos. Cada equipo presenta durante diez y responde durante dos. No es una exposición "
                "académica: es una reunión de comité, y el auditorio actúa como tal.")
y = pasos(s, y + 0.05, [
    ("Se presenta la hoja de ruta, no el diagnóstico",
     "El comité ya conoce los hallazgos. Lo que no sabe es qué hacer primero, con $180 millones y cuatro horas de ventana semanal."),
    ("Cada acción va con costo, plazo, responsable y riesgo que mitiga",
     "Una acción sin esas cuatro columnas no se puede aprobar, y por lo tanto no cuenta."),
    ("El orden hay que defenderlo, no solo enunciarlo",
     "La pregunta que va a llegar siempre es por qué esto antes que aquello. Prepárenla."),
    ("Y hay que responder la pregunta del apoderado",
     "La misma de la sesión 1: cómo se demuestra que una operación la autorizó su titular. Si al final del módulo no se responde en un minuto, algo falló."),
], alto=0.84)

s, y = base(p, "// 42  RÚBRICA", "CÓMO SE CALIFICA LA SUSTENTACIÓN", sig())
y = tabla(s, y, ["CRITERIO", "QUÉ SE MIRA", "PESO"], [
    [("Corrección técnica", {"bold": True}), "Que lo afirmado sea cierto y que los mecanismos propuestos resuelvan lo que se dice que resuelven", "25%"],
    [("Priorización justificada", {"bold": True, "color": NARANJA}), "Que el orden responda a exposición y a plazo, no a facilidad. Y que se defienda", "25%"],
    [("Viabilidad", {"bold": True}), "Presupuesto, ventana de mantenimiento, dependencia de proveedores y capacidad del equipo", "20%"],
    [("Defensa ante preguntas", {"bold": True}), "Que se distinga lo que se sabe de lo que se supone, y que se acepte lo que no se sabe", "20%"],
    [("Comunicación al comité", {"bold": True}), "Sin jerga, con cifras y con una recomendación explícita. El comité decide, ustedes recomiendan", "10%"],
], [2.8, 5.8, 1.4], alto_fila=0.52)

s, y = base(p, "// 43  SÍNTESIS", "LAS SEIS IDEAS QUE DEBERÍAN QUEDAR", sig())
tabla(s, y, ["LA IDEA", "POR QUÉ"], [
    [("El algoritmo casi nunca es el problema", {"bold": True}), "En los ocho hallazgos del caso ninguno era un algoritmo roto: todos eran de uso, de custodia o de gestión"],
    [("Cada servicio exige un mecanismo distinto", {"bold": True}), "Confidencialidad, integridad, autenticación y no repudio no se resuelven con lo mismo"],
    [("El no repudio exige una llave privada por persona", {"bold": True, "color": NARANJA}), "Es una decisión de arquitectura, no de configuración, y por eso la toma el comité"],
    [("La confianza se desplaza, no desaparece", {"bold": True}), "Certificados, entidades acreditadas y sellos de tiempo son formas de repartirla, no de eliminarla"],
    [("Una llave sin dueño ni fecha es una deuda", {"bold": True}), "Y el inventario es la medida más barata y más rentable de todo el módulo"],
    [("Nada de esto dura para siempre", {"bold": True}), "Por eso se diseña para poder cambiar. La criptoagilidad es la conclusión, no un tema adicional"],
], [4.3, 5.7], alto_fila=0.50)

s, y = base(p, "// 44  CIERRE", "LO QUE SE LLEVAN", sig())
y = intro(s, y, "Este módulo no los convierte en criptógrafos, y ese nunca fue el objetivo. Los convierte en algo "
                "que las organizaciones necesitan más y encuentran menos.")
y = dos_columnas(s, y,
    ("// LO QUE NO SABEN HACER, Y ESTÁ BIEN", [
        "No saben diseñar un algoritmo, ni implementarlo, ni auditar una biblioteca criptográfica.",
        "Eso es un oficio distinto, con años de formación específica, y la regla profesional es no intentarlo."]),
    ("// LO QUE SÍ SABEN HACER", [
        "Leer una configuración y decir qué protege y qué no.",
        "Distinguir lo que un mecanismo prueba de lo que no prueba, y decirlo delante de un abogado.",
        "Preguntarle a un proveedor lo que hay que preguntarle antes de firmar.",
        "Y priorizar una inversión con criterio y defenderla ante un comité.",
        "<b>Eso es exactamente lo que le faltaba a Coopaburrá en febrero.</b>"]),
    alto=2.20)

trabajo_independiente(p, "// 45  CIERRE", ["TRABAJO INDEPENDIENTE", "DESPUÉS DE LA SESIÓN 6"], [
    ("12 h", "HASTA LA ENTREGA", "FINAL, A LOS 8 DÍAS", False),
    ("2 h", "LECTURA", "DE CIERRE", False),
    ("10 h", "VERSIÓN CONSOLIDADA", "DEL INFORME", True),
], [
    ("FIPS 203 y FIPS 204", "Secciones 1 y 2 de cada una: alcance, conjuntos de parámetros y nivel de seguridad de ML-KEM y ML-DSA. Una hora."),
    ("ETSI EN 319 142-1", "Firmas PAdES: introducción y niveles B, T, LT y LTA, para precisar la recomendación de H7. Una hora."),
    ("La realimentación recibida", "Las observaciones de las cinco entregas y de la sustentación: la versión final tiene que responderlas todas."),
], "// ENTREGA FINAL DEL MÓDULO",
   "La versión consolidada del informe se entrega a los ocho días de esta sesión: integra las cinco partes corregidas "
   "y la hoja de ruta sustentada. Con estas 12 horas se completan las 64 de trabajo independiente del módulo.",
   sig(), titulo_lecturas="Lectura de cierre · 2 horas")

glosario(p, "// 46  GLOSARIO", 1, 2, [
    ("ACM", "Association for Computing Machinery — Asociación profesional que publicó en 1979 el artículo de Shamir sobre el reparto de secretos."),
    ("AES / AES-256", "Advanced Encryption Standard — Con llaves de 256 bits resiste el cómputo cuántico conocido. Sesión 2."),
    ("CNSA 2.0", "Commercial National Security Algorithm Suite 2.0 — Suite y calendario post-cuántico de la NSA, publicado en 2022."),
    ("ETSI / PAdES", "European Telecommunications Standards Institute / PDF Advanced Electronic Signatures — La norma europea de firma avanzada en PDF."),
    ("B / T / LT / LTA", "Basic, Timestamp, Long-Term, Long-Term with Archive — Los niveles de firma para conservar a largo plazo."),
    ("FF1", "Modo de cifrado que conserva el formato del dato, de NIST SP 800-38G. Es la base de la tokenización sin bóveda."),
    ("FIPS", "Federal Information Processing Standards — Normas federales de Estados Unidos; FIPS 140-3 certifica los módulos de hardware."),
    ("IETF / RFC / TSP", "Internet Engineering Task Force / Request for Comments / Time-Stamp Protocol — El sello de tiempo es el RFC 3161."),
    ("ML-KEM / ML-DSA", "Module-Lattice-Based Key-Encapsulation Mechanism / Digital Signature Algorithm — Los estándares FIPS 203 y FIPS 204."),
    ("NIST / SP / IR", "National Institute of Standards and Technology / Special Publication / Interagency Report — El instituto y dos de sus series."),
], sig())

glosario(p, "// 47  GLOSARIO", 2, 2, [
    ("NSA", "National Security Agency — Agencia de Seguridad Nacional de Estados Unidos; publica la suite CNSA."),
    ("PCI DSS / SSC", "Payment Card Industry Data Security Standard / Security Standards Council — La norma de la industria de tarjetas y su consejo."),
    ("PDF", "Portable Document Format — El formato del contrato y del pagaré de las hipotecas de Coopaburrá."),
    ("PKI", "Public Key Infrastructure — Infraestructura de llave pública. Sesión 5."),
    ("RSA / RSA-2048", "Rivest, Shamir y Adleman — Llave pública de 1977. RSA-2048 queda desaprobado después de 2030 según NIST IR 8547."),
    ("SHA-1", "Secure Hash Algorithm 1 — Función resumen rota: el ejemplo de un algoritmo que envejeció con firmas todavía vigentes."),
    ("SLH-DSA", "Stateless Hash-Based Digital Signature Algorithm — La firma post-cuántica conservadora de FIPS 205."),
    ("X25519", "Acuerdo de llave sobre la curva 25519: la referencia clásica frente a ML-KEM."),
], sig())

fuentes(p, "// 48  FUENTES", "REFERENCIAS DE LA SESIÓN · 1 DE 2", [
    ("NIST. (2020).", "SP 800-57 Part 1 Rev. 5: Recommendation for key management — Part 1: General.", "Estados de la llave y periodos criptográficos"),
    ("NIST. (2019).", "FIPS 140-3: Security requirements for cryptographic modules.", "Niveles de los módulos de hardware"),
    ("NIST. (2024).", "FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) y FIPS 205 (SLH-DSA).", "Los estándares post-cuánticos"),
    ("NIST. (2024).", "IR 8547, borrador: Transition to post-quantum cryptography standards.", "Desaprobación en 2030 y prohibición en 2035"),
    ("National Security Agency. (2022).", "Commercial National Security Algorithm Suite 2.0 (CNSA 2.0).", "Algoritmos y calendario por tipo de sistema"),
], sig())

fuentes(p, "// 49  FUENTES", "REFERENCIAS DE LA SESIÓN · 2 DE 2", [
    ("NIST. (2016).", "SP 800-38G: Methods for format-preserving encryption.", "Tokenización sin bóveda: FF1"),
    ("PCI Security Standards Council. (2011).", "Information supplement: PCI DSS tokenization guidelines.", "Tokenización y reducción del alcance de auditoría"),
    ("Shamir, A. (1979).", "How to share a secret. Communications of the ACM, 22(11), 612–613.", "El reparto de un secreto con umbral"),
    ("Adams, C. et al. (2001).", "RFC 3161: Internet X.509 PKI Time-Stamp Protocol (TSP). IETF.", "El sello de tiempo"),
    ("ETSI. (versión vigente).", "EN 319 142-1: PAdES digital signatures — Building blocks and baseline levels.", "Niveles B, T, LT y LTA"),
], sig(), "// ACCESO A LAS FUENTES",
   "Las publicaciones del NIST, de la NSA, del PCI SSC, de la IETF y del ETSI son de acceso libre en sus páginas. El "
   "artículo de Shamir se consulta en las bases de datos de la Institución.")

p.save(os.path.join(AQUI, "..", "SIO0010-S6-Gestion-de-llaves-y-transicion.pptx"))
print(f"Diapositivas generadas: {n}")
