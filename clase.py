class Envio:
    def __init__(self, cp, dire, tipo, fp):
        self.codigo_postal = cp
        self.direccion = dire
        self.tipo = tipo
        self.forma_pago = fp

    def __str__(self):
        pais = procesar_envio(self.codigo_postal.strip(), self.direccion, self.tipo, self.forma_pago)[0]
        
        return (
            f"Código Postal: {self.codigo_postal:<10} "
            f"Dirección de destino: {self.direccion:<20} "
            f"Tipo de envío: {self.tipo:<2} "
            f"Forma de pago: {self.forma_pago:<2} "
            f"País: {pais:<10}"
        )

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

    if (long == 8 and (cp[0] in letras and cp[0] not in "IO") and cp[1] in numeros and cp[2] in numeros and cp[3] in
            numeros and cp[4] in numeros and cp[5] in letras and cp[6] in letras and cp[7] in letras):
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
    elif (long == 9 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in
          numeros and cp[5] == "-" and cp[6] in numeros and cp[7] in numeros and cp[8] in numeros):
        destino = "Brasil"
        if cp[0] in "0123":
            multiplicador = 1.25
        elif cp[0] in "4567":
            multiplicador = 1.3
        else:
            multiplicador = 1.2
    elif (long == 7 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in
          numeros and cp[5] in numeros and cp[6] in numeros):
        destino = "Chile"
        multiplicador = 1.25
    elif (long == 6 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in numeros and cp[4] in
          numeros and cp[5] in numeros):
        destino = "Paraguay"
        multiplicador = 1.20
    elif (long == 5 and cp[0] in numeros and cp[1] in numeros and cp[2] in numeros and cp[3] in
          numeros and cp[4] in numeros):
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
    return destino, provincia, inicial, final
