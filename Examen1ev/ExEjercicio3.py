

ingVegetarianos = ["cebolla", "queso", "tomate", "pimiento", "aceitunas"]
ingNoVegetarianos = ["carne", "bacon", "pollo", "peperoni", "atun", "anchoas"]

pizzaVeg = []
pizzaNor = []
pizza = []

while True:
    print("\nMENU PIZZERIA")
    print("1. Realizar pedido de pizza")
    print("0. Salir")
    
    resp = int(input())

    if resp == 1:
        veg = input("¿Que tipo de pizza desea? [vegetariana/normal]")

        if veg == "vegetariana":
            tam = input("¿Que tamaño desea? [mediana/grande]")
            
            if tam == "mediana":
                print("ingredientes a elegir:", ingVegetarianos)
                ing = int(input("introduzca numero de ingredientes:"))

                for i in range(ing):
                    ingrediente = input("Introduce ingrediente :")

                    if ingrediente in ingVegetarianos:
                        pizzaVeg.append(ingrediente)
                    else:
                        print("Ingrediente no disponible")

                #calculamos el precio
                if len(pizzaVeg) <= 2:
                    precioMediana = int(10)

                else:
                    precioMediana = int(10)
                    for i in range(2, ing):
                       precioMediana += (precioMediana * 10) / 100 

                pizza.append(["pizza ",veg, tam, pizzaVeg, precioMediana])

                print("Datos de tu pedido:", pizza)

            elif tam == "grande":
                print("ingredientes a elegir:", ingVegetarianos)
                ing = int(input("introduzca numero de ingredientes:"))

                for i in range(ing):
                    ingrediente = input("Introduce ingrediente :")

                    if ingrediente in ingVegetarianos:
                        pizzaVeg.append(ingrediente)
                    else:
                        print("Ingrediente no disponible")

                 #calculamos el precio
                if len(pizzaVeg) <= 2:
                    precioGrande = int(16)

                else:
                    precioGrande = int(16)
                    for i in range(2, ing):
                       precioGrande += (precioGrande * 15) / 100

                pizza.append(["pizza ",veg, tam, pizzaVeg, precioGrande])

                print("Datos de tu pedido:", pizza)

            else:
                print("Tamaño introducido no disponible")

        elif veg == "normal":
            tam = input("¿Que tamaño desea? [mediana/grande]")

            if tam == "mediana":
                print("ingredientes a elegir:", ingNoVegetarianos, ingVegetarianos)
                ing = int(input("introduzca numero de ingredientes:"))

                for i in range(ing):
                    ingrediente = input("Introduce ingrediente :")

                    if ingrediente in ingNoVegetarianos or ingrediente in ingVegetarianos:
                        pizzaNor.append(ingrediente)
                    else:
                        print("Ingrediente no disponible")

                #calculamos el precio
                if len(pizzaNor) <= 2:
                    precioMediana = int(10)

                else:
                    precioMediana = int(10)
                    for i in range(2, ing):
                       precioMediana += (precioMediana * 10) / 100 

                pizza.append(["pizza ",veg, tam, pizzaNor, precioMediana])

                print("Datos de tu pedido:", pizza)

            elif tam == "grande":
                print("ingredientes a elegir:", ingNoVegetarianos, ingVegetarianos)
                ing = int(input("introduzca numero de ingredientes:"))

                for i in range(ing):
                    ingrediente = input("Introduce ingrediente :")

                    if ingrediente in ingNoVegetarianos or ingrediente in ingVegetarianos:
                        pizzaNor.append(ingrediente)
                    else:
                        print("Ingrediente no disponible")

                 #calculamos el precio
                if len(pizzaNor) <= 2:
                    precioGrande = int(16)

                else:
                    precioGrande = int(16)
                    for i in range(2, ing):
                       precioGrande += (precioGrande * 15) / 100

                pizza.append(["pizza ",veg, tam, pizzaNor, precioGrande])

                print("Datos de tu pedido:", pizza)

            else:
                print("Tamaño introducido no disponible")


    else:
        print("Pizzeria cerrada.")
        break