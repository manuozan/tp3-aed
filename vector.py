import clase


def procesar_linea(linea):

    # Quitar los espacios
    cp = linea[:9].strip()
    dir = linea[9:29]
    tipo = int(linea[29])
    fp = int(linea[30])
    envio = clase.Envio(cp, dir, tipo, fp)

    return envio


def procesar_archivo():
    v = []
    archivo = open("envios-tp3.txt")
    control = archivo.readline()
    for linea in archivo:
        envio = procesar_linea(linea)
        v.append(envio)
    archivo.close()
    return v, control


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


def menu():
    print("Menú de opciones: ")
    print("1. Procesar archivo")
    print("2. Carga Manual")
    print("3. Mostrar registros")
    print("4. Buscar por dirección y tipo de envío ")
    print("5. Buscar por código postal")
    print("6. Contar envíos con dirección válida")
    print("7. Importe final acumulado por tipo de envío")
    print("8. Determinar envío con mayor recaudación")
    print("9. Calcular importe final promedio")
    print("0. Salir")
    return int(input("Ingrese opción: "))


def carga_manual(v):
    cp = input("Ingrese el código postal: ")
    dir = input("Ingrese la dirección de destino: ")
    fp = int(input("Ingrese el tipo de envío: "))
    tipo = int(input("Ingrese la forma de pado: "))
    envio = clase.Envio(cp, dir, tipo, fp)
    v.append(envio)
    # Validar el tipo y forma de pago


def principal():
    opcion = -1
    v = []
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            if len(v)> 0:
                print("ADVERTENCIA: El vector tiene datos!")
                borrar = int(input("Desea pisar el mismo? si:0 no:1"))
                if borrar == 1:
                    continue
            v, control = procesar_archivo()

        elif opcion == 2:
            carga_manual(v)

        elif opcion == 3:
            mostrar_vector(v)

        elif opcion == 4:
            pass

        elif opcion == 0:
            print("Adiós!")


if __name__ == "__main__":
    principal()
