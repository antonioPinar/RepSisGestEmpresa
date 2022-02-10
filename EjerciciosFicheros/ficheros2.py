import math

def mostrarCabecera(numLineas):
    #abrimos flujo de lectura al fichero
    with open("listaOperaciones.txt", "r") as f:
        #recorremos las lineas de cabecera que queremos leer
        for _ in range(numLineas):
            print(f.readline())


def mostrarPie(numLineas):
    lineasAleer = 0
    #abrimos flujo de lectura al fichero
    with open("listaOperaciones.txt", "r") as f:
        #almacenamos desde que linea hasta el final tenemos que leer
        lineasTotal = len(f.readlines())
        lineasAleer = lineasTotal - numLineas
        
    #abrimos flujo de lectura otra vez porque el anterior flujo leyo todo el fichero 
    with open("listaOperaciones.txt", "r") as f:
        #guardamos el numero de la linea en la que estamos
        for i in range(lineasTotal):
            texto = f.readline()
            #visualizamos las lineas del fichero que sean igual o superiores a las que hemos introducido
            if i >= lineasAleer:
                print(texto)


def aniadirLineas():
    #abrimos flujo de escritura al final al fichero
    with open("listaOperaciones.txt", "a") as f:
        for i in range(10):
            numero = int(input("Introduce numero a calcular para la " + str(i+1) + " posicion:"))
            cuadrado = math.pow(numero, 2)
            raiz = math.sqrt(numero)
            cubo = math.pow(numero, 3)

            #por cada numero al azar de la lista la escribimos en el fichero
            f.write(f"numero={numero}#cuadrado={round(cuadrado, 2)}#raiz={round(raiz,2)}#cubo={cubo}\n")
    
    print("numeros añadidos con exito")


def borrarLineas(numLineas):
    #abrimos flujo de lectura al fichero
    with open("listaOperaciones.txt", "r") as f:
        lineasTotal = f.readlines()
        #recorremos el numero de elementos que queremos eliminar
        for _ in range(numLineas):
            #controlamos eliminar el numero de lineas indicadas, dejamos siempre la posicion a 0 porque la lista se redimensiona automatico
            lineasTotal.pop(0)
    with open("listaOperaciones.txt", "w") as f:
        for linea in lineasTotal:
            f.write(linea)
            
    print("Lineas eliminadas con exito")


opcion = 1

while opcion != 0:
    print("\n1.- Mostrar cabecera")
    print("2.- Mostrar pie")
    print("3.- Añadir")
    print("4.- Borrar")
    print("0.- Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        lineasV = int(input("Cuantas lineas de cabecera quieres leer: "))
        mostrarCabecera(lineasV)

    elif opcion == 2:
        lineasV = int(input("Cuantas lineas de pie quieres leer: "))
        mostrarPie(lineasV)

    elif opcion == 3:
        aniadirLineas()

    elif opcion == 4:
        lineasV = int(input("Cuantas lineas quieres borrar: "))
        borrarLineas(lineasV)

    elif opcion == 0:
        print("\nPrograma cerrado")