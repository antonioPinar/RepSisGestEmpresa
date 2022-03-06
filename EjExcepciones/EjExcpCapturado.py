import EjExcepciones as fichero

lista1 = [21, 12, 33, 14, 75, 61, 47, 28, 94]
lista2 = [11, 24, 0, 4, 15, 96, 7, 8, 2]
listaF = []

try:

    listaF = fichero.sumaListas(lista1, lista2)

except fichero.ListaMayorError as error:
    print(error)
except ZeroDivisionError as error:
    print("Error,", error)

finally:
    print(listaF)