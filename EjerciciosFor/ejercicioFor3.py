import random as rm

#creamos elemento para coger numeros aleatorios
rm.seed(2021)

lista = list(range(1000))

#De la lista creamos una lista mas pequeña de forma aleatoria
#Sample extrae un elemento al azar de objeto iterable,el segundo parametro es el numero de veces lo hacemos 
lista = rm.choices(lista, k = 100)
print(lista)


numMayor = lista[0]
numMenor = lista[0]
sumaNum = 0
numRepetidoMyr = 0
numRepetidoMnr = 0
for i in range(len(lista)):
    #buscamos el numero mayor de la lista
    if lista[i] > numMayor:
        numMayor = lista[i]
    
    #buscamos el numero menor en la lista
    if lista[i] < numMenor:
        numMenor = lista[i]
    
    #hacemos la media de la lista aleatoria
    sumaNum = sumaNum + lista[i]

    #buscamos numero mas repetido y menos repetido
    for j in range(len(lista)):
        if lista.count(lista[i]) > lista.count(lista[j]):
            numRepetidoMyr = lista[i]
        if lista.count(lista[i]) < lista.count(lista[j]):
            numRepetidoMnr = lista[i]
numMedia = sumaNum / len(lista)

#visualizar datos
print("Numero mayor de la lista: ", numMayor)
print("Numero menor de la lista: ", numMenor)
print("Media de la lista: ", numMedia)
print("El numero",numRepetidoMyr,"es el mas repetido")
print("El numero",numRepetidoMnr,"es el menos repetido")

