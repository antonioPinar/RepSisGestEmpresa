palabra = input("Introduce una palabra:")

#convertimos el String a lista
#recorremos la lista de manera inversa y guardamos en una variable
palindromo = ""
for i in reversed(range(len(list(palabra)))):
        palindromo += palabra[i]


#  si la palabra inversa y la de inicio son iguales
if palabra == palindromo:
    print("La palabra", palabra,"es un palindromo")
else:
    print("La palabra", palabra,"no es un palindromo")