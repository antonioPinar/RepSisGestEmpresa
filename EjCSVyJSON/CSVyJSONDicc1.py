import csv
import json

from nbformat import write

def crearPizza(listaPizzas):
    tamanio = 1

    while tamanio == 1 or tamanio == 2:
        pizza = {}
        ingredientes = []
        tamanio = int(input("¿Que tamaño deseas?[Grande/Mediana] -> [1/2]: "))
        if tamanio == 1:
            tamanio = "Grande"
        elif tamanio == 2:
            tamanio = "Mediana"
        else:
            print("Error al elegir tamaño.")

        pizza['Tamano'] = tamanio

        #hemos decidido insertar 4 ingredientes por pedido
        for i in range(4):
            ing = input(f"Selecciona el ingrediente {i}: ")
            ingredientes.append(ing)

        pizza['ingredientes'] = ingredientes
        listaPizzas.append(pizza)
        tamanio = int(input("¿Quieres hacer otro pedido?[1-SI/3-NO]: "))

pizzas = []
opcion = 0
while opcion != 4:

    print("1.- Pedir pizza")
    print("2.- Introducir pedidos en CSV")
    print("3.- Introducir pedidos en JSON")
    print("4.- Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print()
        crearPizza(pizzas)
    elif opcion == 2:
        print()
        cabecera = []
        with open("pizzas.csv", "w") as f:
            for clave, valor in pizzas[0].items():
                cabecera.append(clave)
            writer = csv.DictWriter(f, fieldnames = cabecera, lineterminator = "\n")
            writer.writeheader()
            for pizza in pizzas:
                writer.writerow(pizza)
        print("Listado pasado a CSV con exito")
        
    elif opcion == 3:
        print()
        with open("pizzas.json", "w") as f:
            json.dump(pizzas, f, indent = 5)
        print("Listado pasado a JSON con exito")

    elif opcion == 4:
        print("Programa cerrado")
    
    print()