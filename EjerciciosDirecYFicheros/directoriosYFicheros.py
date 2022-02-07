import random
import math
import os

#creo una funcion para la lista y la lleno con numeros aleatorios del 0 al 100000
def listaaleatoria(tamano):
	#el _ significa no uso el valor
	lista=[]
	for _ in range(tamano):
		lista.append(random.randint(0,100000))
	return lista


def crearCarpeta():
    nombre = input("Introduce nombre de la carpeta inicial: ")
    os.mkdir(nombre)

    for i in listaaleatoria(100):
        #creamos el directorio de cada fichero de texto dentro de la carpeta 
        rutaFichero = f"{nombre}/{i}"
        os.mkdir(rutaFichero)

        #creamos cada fichero de texto dentro de cada directorio, e introducimos los datos del fichero
        with open(f"{rutaFichero}/{i}.txt", "w") as f:
            cuadrado = math.pow(i, 2)
            raiz = math.sqrt(i)
            cubo = math.pow(i, 3)

            f.write(f"numero={i},cuadrado={round(cuadrado, 2)},raiz={round(raiz,2)},cubo={cubo}")

    print("Carpeta creada con exito")


#ejecucion del programa
crearCarpeta()