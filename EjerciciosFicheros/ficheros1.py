import random
import math

#creo una funcion para la lista y la lleno con numeros aleatorios del 0 al 1000
def listaaleatoria(tamano):
	#el _ significa no uso el valor
	lista=[]
	for _ in range(tamano):
		lista.append(random.randint(0,1000))
	return lista

def lineasMostrar():
    numLineas = int(input("Introduce numero de lineas a mostrar: "))
    with open("listaOperaciones.txt", "r") as f:
        for i in range(numLineas):
            print(f.readline())



listaNum = listaaleatoria(1000)

with open("listaOperaciones.txt", "w") as f:

	for i in listaNum:
		cuadrado = math.pow(i, 2)
		raiz = math.sqrt(i)
		cubo = math.pow(i, 3)

		#por cada numero al azar de la lista la escribimos en el fichero
		f.write(f"numero={i}#cuadrado={round(cuadrado, 2)}#raiz={round(raiz,2)}#cubo={cubo}\n")

lineasMostrar()