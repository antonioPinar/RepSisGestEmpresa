import csv
import json

def leerCSV():
    pizzas = []
    totalP = 0
    pizzasG = 0
    pizzasM = 0
    #abrimos fichero csv
    with open("pizzas.csv", "r") as f:
        pizzas = csv.DictReader(f)
        for pizza in pizzas:
            totalP += 1
            if pizza['Tamano'] == "Grande":
                pizzasG += 1
            elif pizza['Tamano'] == "Mediana":
                pizzasM += 1
        
    print(f"Total de pizzas: {totalP}")
    print(f"Pizzas grandes: {pizzasG}")
    print(f"Pizzas medianas: {pizzasM}")


def leerJSON():
    totalP = 0
    pizzasG = 0
    pizzasM = 0
    mediaIng = 0
    #abrimos fichero json
    with open("pizzas.json", "r") as f:
        pizzas = json.load(f)
        for pizza in pizzas:
            totalP += 1
            if pizza['Tamano'] == "Grande":
                pizzasG += 1
            elif pizza['Tamano'] == "Mediana":
                pizzasM += 1

            for _ in pizza['ingredientes']:
                mediaIng += 1

        mediaIng = mediaIng / totalP

    print(f"Total de pizzas: {totalP}")
    print(f"Pizzas grandes: {pizzasG}")
    print(f"Pizzas medianas: {pizzasM}")
    print(f"Media de ingredientes por pizza: {mediaIng}")


opcion = 0
while opcion != 3:

    print("1.- Leer fichero .csv")
    print("2.- Leer fichero .json")
    print("3.- Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print()
        leerCSV()
    elif opcion == 2:
        print()
        leerJSON()
    elif opcion == 3:
        print("Programa cerrado")
    print()