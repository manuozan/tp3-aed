import os
from clase import *


def principal():
    opcion = -1
    v = []
    acu = []
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            if len(v) > 0:
                print("\nADVERTENCIA: Existen registros cargados anteriormente.\n")
                borrar = int(input("¿Desea sobreescribir los envíos?\n0: Sobreescribir \n1: Cancelar\nIngrese opción...  "))
                if borrar == 1:
                    continue
            v, control = procesar_archivo()

        elif opcion == 2:
            carga_manual(v)
        elif opcion in [3, 4, 5, 6, 7, 8, 9]:
            if not validar_vector(v):
                print("\nError: No hay registros cargados. Por favor, cargue datos primero.\n")
                continue

            elif opcion == 3:
                validar_vector(v)
                ordenar_por_cp(v)
                mostrar_vector(v)

            elif opcion == 4 and validar_vector(v):
                d = str(input("Ingrese la dirección de envío a buscar: "))
                e = int(input("Ingrese el tipo de envío a buscar: "))
                envio = buscar_por_dir_y_tipo(v, d, e)
                print(envio)

            elif opcion == 5:
                cp = input('Ingrese el CP a buscar: ')
                pos = buscar_por_cp(v, cp)
                if pos == -1:
                    print('\nNo se encontraron resultados...')
                else:
                    if v[pos].forma_pago == 1:
                        v[pos].forma_pago = 2
                    else:
                        v[pos].forma_pago = 1
                    print(v[pos])

            elif opcion == 6:
                c_dir_val = 0
                control = procesar_archivo()[1]
                print(control)
                cont = contar_por_tipo(v, control)

                print('Cantidad de envios validos por tipo:')
                mostrar_conteo(cont)

            elif opcion == 7:
                acu = acumular_por_tipo(v, control)
                mostrar_acumulador(acu)

            elif opcion == 8:
                
                if acu != []:
                    mayor = indice_del_mayor(acu)
                    porc = round(max(acu) / sum(acu) * 100, 2)
                    print(f"Tipo de envío con mayor recaudación: Tipo {mayor}, representando un {porc}% del total\n")
                else:
                    print("\nError. Por favor, ingrese a la opción 7 primero. \n")

            elif opcion == 9:
                prom = round(calcular_promedio(v), 2)
                print(f"El importe final promedio de todos los envíos fue de ${prom}")

                c9 = 0
                for envio in v:
                    monto_final = procesar_envio(envio.codigo_postal.strip(),
                                                envio.direccion, envio.tipo, envio.forma_pago)[-1]
                    if monto_final < prom:
                        c9 += 1
                print(f"Envios con importe final menor al promedio: {c9}\n")

        elif opcion == 0:
            print("Adiós!")
            
def procesar_linea(linea):

    # Quitar los espacios con el método strip() 
    cp = linea[:9].strip()
    dire = linea[9:29].strip()
    tipo = int(linea[29])
    fp = int(linea[30])
    envio = Envio(cp, dire, tipo, fp)

    return envio


def procesar_archivo():
    v = []
    archivo = open("envios-tp3.txt")
    timestamp = archivo.readline()
    control = procesar_timestamp(timestamp)
    for linea in archivo:
        envio = procesar_linea(linea)
        v.append(envio)
    archivo.close()
    return v, control


def procesar_timestamp(timestamp):
    if "SC" in timestamp:
        return "Soft Control"
    elif "HC" in timestamp:
        return "Hard Control"


def mostrar_vector(v):
    opcion = 0
    while opcion not in [1, 2]:
        opcion = int(input("\n[1] Mostrar todos los registros \n[2] Elegir cantidad de registros:"
                           " \nIngrese una opción: "))
        if opcion == 1:
            m = len(v)
        elif opcion == 2:
            m = int(input("Ingrese la cantidad de registros a mostrar: "))
        else:
            print("\nError, ingrese una opción válida...")
    for i in range(m):
        print(v[i])
    print()


def menu():
    print()
    print("Menú de opciones: ")
    print("1. Procesar archivo")
    print("2. Carga Manual")
    print("3. Mostrar registros")
    print("4. Buscar por dirección y tipo de envío ")
    print("5. Buscar por código postal")
    print("6. Contar envíos con dirección válida")
    print("7. Importe final acumulado por tipo de envío")
    print("8. Determinar tipo de envío con mayor recaudación")
    print("9. Calcular importe final promedio")
    print("0. Salir\n")
    return int(input("Ingrese opción: "))


def carga_manual(v):
    cp = input("Ingrese el código postal: ")
    dire = input("Ingrese la dirección de destino: ")
    fp = int(input("Ingrese el tipo de envío: "))
    tipo = int(input("Ingrese la forma de pago: "))
    envio = Envio(cp, dire, tipo, fp)
    v.append(envio)
    # Validar el tipo y forma de pago


def procesar_direccion(direc, control):
    if control != "Hard Control":
        return True  # Si no es "Hard Control", siempre es válido

    ant = ""
    # contador de caracteres
    cc = 0
    # contador de dígitos
    cd = 0
    # cont pal solo digitos
    pd = 0

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


def es_numero(caracter):
    numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    return caracter in numeros


def es_letra(caracter):
    return es_mayuscula(caracter.upper())


def es_mayuscula(caracter):
    mayusculas = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'Á', 'É', 'Í', 'Ó', 'Ú', 'Ñ', 'Ü', 'Â', 'Ê', 'Ô', 'Ã', 'Õ', 'Ç')
    return caracter in mayusculas


def es_simbolo(caracter):
    if es_letra(caracter) or es_numero(caracter):
        return False
    else:
        return True
    


def ordenar_por_cp(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo_postal.strip() > v[j].codigo_postal.strip():
                v[i], v[j] = v[j], v[i]


def buscar_por_cp(v, cp):
    for i in range(len(v)):
        if v[i].codigo_postal.strip() == cp:
            return i
    return -1


def buscar_por_dir_y_tipo(v, dire, tipo):
    for envio in v:
        if dire.lower() in envio.direccion.lower() and envio.tipo == tipo:
            return envio
    return "\nNo se encontraron resultados... \n"


def limpiar_consola():
    # Verifica el sistema operativo y ejecuta el comando adecuado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/macOS
        os.system('clear')


def contar_por_tipo(v, control):
    cont = [0] * 7
    for i in range(len(v)):
        pos = v[i].tipo
        if control == "Hard Control":
            if procesar_direccion(v[i].direccion, control):
                cont[pos] += 1
        else:
            cont[pos] += 1
    return cont


def acumular_por_tipo(v, control):
    total = [0] * 7
    for envio in v:
        monto_final = procesar_envio(envio.codigo_postal.strip(), envio.direccion, envio.tipo, envio.forma_pago)[-1]
        pos = envio.tipo
        if control == "Hard Control":
            if procesar_direccion(envio.direccion, control):
                total[pos] += monto_final
        else:
            total[pos] += monto_final

    return total


def mostrar_conteo(cont):
    for i in range(len(cont)):
        if cont[i] > 0:
            print('Tipo', i, ': ', cont[i], 'envíos válidos')


def mostrar_acumulador(cont):
    for i in range(len(cont)):
        if cont[i] > 0:
            print('Tipo', i, ': ', 'Total $ ', cont[i])


def indice_del_mayor(arreglo):
    if not arreglo:  
        return None

    indice_mayor = 0
    valor_mayor = arreglo[0]

    for i in range(len(arreglo)):
        if arreglo[i] > valor_mayor:
            valor_mayor = arreglo[i]
            indice_mayor = i

    return indice_mayor


def calcular_promedio(v):
    total = 0
    cant = 0
    for envio in v:
        monto_final = procesar_envio(envio.codigo_postal.strip(), envio.direccion, envio.tipo, envio.forma_pago)[-1]
        total += monto_final
        cant += 1
    if cant == 0:
        return 0
    else:
        return total / cant

def validar_vector(v):
    return v > []
        
    
    
    
if __name__ == "__main__":
    limpiar_consola()
    principal()
