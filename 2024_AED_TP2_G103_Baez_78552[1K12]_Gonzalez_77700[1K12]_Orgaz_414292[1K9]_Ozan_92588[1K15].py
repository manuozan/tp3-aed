# FUNCIONES
###########################################################################################################
def procesar_timestamp(timestamp):
    if "SC" in timestamp:
        return "Soft Control"
    elif "HC" in timestamp:
        return "Hard Control"


def procesar_direccion(direc, control):
    if control != "Hard Control":
        return True  # Si no es "Hard Control", siempre es válido

    ant = ""
    cc = 0 #contador de caracteres
    cd = 0 #contador de dígitos
    pd = 0 #cont pal solo digitos


    for caracter in direc:
        
        # TERMINA LA PALABRA
        if caracter == ' ' or caracter == ".":
            if cc == cd and cd > 0:
                pd += 1 
            cc = cd = 0
        # RECORRE LA PALABRA    
        else:
            cc += 1
            if es_mayuscula(caracter) and es_mayuscula(ant):
                    return False  # Dos mayúsculas consecutivas

            if es_simbolo(caracter):
                return False  # No es alfanumérico ni un punto

            if es_numero(caracter):
                cd += 1
                
        ant = caracter
    if pd != 1:
        return False  # Al menos una palabra debe ser un número

    return True  # Si pasa todas las verificaciones


def contar_tipo_envio(tipo):
    ccs = ccc = cce = 0
    if tipo in (0,1,2):
        ccs = 1
    elif tipo in (3,4):
        ccc = 1
    elif tipo in (5,6):
        cce = 1
    return [ccs, ccc, cce]

def calcular_mayor (ccs,ccc,cce):
    mayor = ""

    if ccs >= ccc and ccs >= cce:
        mayor = "Carta Simple"

    elif ccc >= ccs and ccc >= cce:
        mayor = "Carta Certificada"

    else:
        mayor = "Carta Expresa"
    return mayor

def calcular_porcentaje(cont, ac):
    if ac != 0:
        porc = (cont *100) /ac
        porc = int(porc)
    else:
        porc = 0
    return porc

def calcular_promedio(cont, ac):
    if ac != 0:
        prom = ac / cont
        prom = int(prom)
    else:
        prom = 0
    return prom

def es_numero(caracter):
    numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    return caracter in numeros

def es_letra(caracter):
    return es_mayuscula(caracter.upper())


def es_mayuscula(caracter):
    mayusculas = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'Á', 'É', 'Í', 'Ó', 'Ú', 'Ñ', 'Ü', 'Â', 'Ê', 'Ô', 'Ã', 'Õ', 'Ç'
    )
    return caracter in mayusculas



def es_simbolo(caracter):
    if es_letra(caracter) or es_numero(caracter):
        return False
    else:
        return True


def eliminar_espacios(cadena):
    texto = ""
    for palabra in cadena:
        if palabra == " ":
            continue
        texto += palabra
    return texto

# Trabajo Práctico N°1 ---------------------------------------------------------------------------------
# PROCESAMIENTO
def procesar_envio(cp, direc, tipo, pago):
    # INICIALIZACIÓN DE VARIABLES
    destino = ""
    provincia = "No aplica"
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = '0123456789'
    inicial = 0
    final = int()
    precio = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    multiplicador = 1.5
    descuento = (1, 0.9, 1)

    # ENTRADA DE DATOS
    cp = cp
    direccion = direc
    tipo = tipo
    pago = pago
    cp = cp.upper()
    long = len(cp)

    if long == 8 and (cp[0] in letras and cp[0] not in "IO") and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in numeros and cp[5] in letras and cp[6] in letras and cp[7] in letras:
        destino = "Argentina"
        multiplicador = 1
        if cp[0] == "A":
            provincia = "Salta"
        elif cp[0] == "B":
            provincia = "Provincia de Buenos Aires"
        elif cp[0] == "C":
            provincia = "Ciudad Autónoma de Buenos Aires"
        elif cp[0] == "D":
            provincia = "San Luis"
        elif cp[0] == "E":
            provincia = "Entre Ríos"
        elif cp[0] == "F":
            provincia = "La Rioja"
        elif cp[0] == "G":
            provincia = "Santiago del Estero"
        elif cp[0] == "H":
            provincia = "Chaco"
        elif cp[0] == "J":
            provincia = "San Juan"
        elif cp[0] == "K":
            provincia = "Catamarca"
        elif cp[0] == "L":
            provincia = "La Pampa"
        elif cp[0] == "M":
            provincia = "Mendoza"
        elif cp[0] == "N":
            provincia = "Misiones"
        elif cp[0] == "P":
            provincia = "Formosa"
        elif cp[0] == "Q":
            provincia = "Neuquén"
        elif cp[0] == "R":
            provincia = "Río Negro"
        elif cp[0] == "S":
            provincia = "Santa Fe"
        elif cp[0] == "T":
            provincia = "Tucumán"
        elif cp[0] == "U":
            provincia = "Chubut"
        elif cp[0] == "V":
            provincia = "Tierra del Fuego"
        elif cp[0] == "W":
            provincia = "Corrientes"
        elif cp[0] == "X":
            provincia = "Córdoba"
        elif cp[0] == "Y":
            provincia = "Jujuy"
        elif cp[0] == "Z":
            provincia = "Santa Cruz"
    elif long == 4 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros:
        destino = "Bolivia"
        multiplicador = 1.20
    elif long == 9 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in numeros and cp[5] == "-" and cp[6] in numeros and cp[7] in numeros and cp[8] in numeros:
        destino = "Brasil"
        if cp[0] in "0123":
            multiplicador = 1.25
        elif cp[0] in "4567":
            multiplicador = 1.3
        else:
            multiplicador = 1.2
    elif long == 7 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in numeros and cp[5] in numeros and cp[6] in numeros:
        destino = "Chile"
        multiplicador = 1.25
    elif long == 6 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in numeros and cp[5] in numeros:
        destino = "Paraguay"
        multiplicador = 1.20
    elif long == 5 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in numeros:
        destino = "Uruguay"
        multiplicador = 1.25
        if cp[0] == "1":
            multiplicador = 1.20
    else:
        destino = "Otro"
        multiplicador = 1.5

    # PUNTO 2
    inicial = int(precio[tipo] * multiplicador)
    final = int(inicial * descuento[pago])

    # SALIDA
    return (destino,provincia,inicial,final)

###################################################################################################

def principal():
    # INICIALIZACIÓN DE VARIABLES
    control = ""
    cedvalid = cedinvalid = 0
    imp_acu_total = 0
    ccs = ccc = cce = 0
    tipo_mayor = 0
    primer_cp = ""
    cant_primer_cp = 0
    menimp = None
    mencp = ""
    c_r13 = ac_r13 = 0
    porc = prom = 0
    c_r14 = ac_r14 = 0

    # Abrimos el archivo en modo lectura
    m = open("envios.txt", "r")

    # Primera línea del archivo para el control
    control = procesar_timestamp(m.readline().strip())

    cp = direc = tipo_envio = forma_pago = ""

    n = 1
    while True:
        linea = m.readline()
        if linea == "": # Si no hay más líneas, salir del bucle
            break

        cp = eliminar_espacios(linea[:9])
        direc = linea[9:28]
        tipo_envio = int(linea[29])
        forma_pago = int(linea[30])

        importe = procesar_envio(cp, direc, tipo_envio, forma_pago)[3]

        if n == 1:
            primer_cp = cp

        #print(n, direc, procesar_direccion(direc, control))
        if procesar_direccion(direc, control):
            destino = procesar_envio(cp, direc, tipo_envio, forma_pago)[0]
            provincia = procesar_envio(cp, direc, tipo_envio, forma_pago)[1]
            cedvalid += 1
            imp_acu_total += procesar_envio(cp, direc, tipo_envio, forma_pago)[3]

            ccs += contar_tipo_envio(tipo_envio)[0]
            ccc += contar_tipo_envio(tipo_envio)[1]
            cce += contar_tipo_envio(tipo_envio)[2]
            tipo_mayor = calcular_mayor(ccs, ccc, cce)

            if destino != "Argentina":
                c_r13 += 1
                ac_r13 += 1
            else:
                ac_r13 += 1
                if provincia == "Provincia de Buenos Aires":
                    ac_r14 += importe
                    c_r14 += 1
        else:
            cedinvalid += 1
            destino = procesar_envio(cp, direc, tipo_envio, forma_pago)[0]

        if cp == primer_cp:
            cant_primer_cp += 1

        if destino == "Brasil":
            if menimp is None:
                menimp = importe
            if importe < menimp:
                menimp = importe
                mencp = cp

        n += 1

    m.close()

    porc = calcular_porcentaje(c_r13, n-1)
    prom = calcular_promedio(c_r14, ac_r14)

    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envíos con dirección válida:', cedvalid)
    print(' (r3) - Cantidad de envíos con dirección no válida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envíos:', tipo_mayor)
    print(' (r9) - Código postal del primer envío del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envíos a Brasil:', menimp)
    print('(r12) - Código postal del envío a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envíos al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envíos Buenos Aires:', prom)
principal()