import csv
import json

from nbformat import write

def crearPizza(listaPizzas):
    tamanio = 1
    ingredientes = ["Ternera", "Pollo", "Bacon", "Queso", "Peperoni", "Cebolla"]

    while tamanio == 1 or tamanio == 2:
        pizza = {}
        tamanio = int(input("¿Que tamaño deseas?[Grande/Mediana] -> [1/2]: "))
        if tamanio == 1:
            tamanio = "Grande"
        elif tamanio == 2:
            tamanio = "Mediana"
        else:
            print("Error al elegir tamaño.")

        pizza['Tamano'] = tamanio

        print("Lista de ingredientes:", ingredientes)
        ing = ingredientes[int(input("Selecciona el primer ingrediente por posicion: ")) - 1]
        pizza['Ingrediente1'] = ing
        ing = ingredientes[int(input("Selecciona el segundo ingrediente por posicion: ")) - 1]
        pizza['Ingrediente2'] = ing
        ing = ingredientes[int(input("Selecciona el tercer ingrediente por posicion: ")) - 1]
        pizza['Ingrediente3'] = ing
        ing = ingredientes[int(input("Selecciona el cuarto ingrediente por posicion: ")) - 1]
        pizza['Ingrediente4'] = ing

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
            writer = csv.DictWriter(f, fieldnames = cabecera, extrasaction = 'ignore', lineterminator = "\n")
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