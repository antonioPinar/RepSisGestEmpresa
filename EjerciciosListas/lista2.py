import random
def listaaleatoria(tamano):
	#el _ significa no uso el valor
	lista=[]
	for _ in range(tamano):
		lista.append(random.randint(0,1000))
	return lista

miLista = listaaleatoria(1000)
print(miLista)

print("10 primeros elementos:", miLista[:10],"\n")
print("10 últimos elementos:", miLista[990:],"\n")
print("Elementos del 56 al 86:",miLista[56:86],"\n")
print("100 primeros elementos por posicion par:",miLista[:100:2],"\n")
print("Elementos del 100 al 200 con saltos de 3:",miLista[100:200:3],"\n")
print("Muestra los elementos del 500 al 600 de forma inversa con saltos de 5:",miLista[600:500:-5])