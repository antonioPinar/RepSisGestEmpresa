caracter = input("Introduce un caracter: ")
lineas = int(input("Introduce un numero de lineas "))


#for i in range(lineas):
#    for j in range(i):
#        print(caracter, end=" ")
#        if range(i) != range(lineas):
#            if j == 1:
#                print(end=" ")
#    print()

cadena = ""

for i in range(lineas):
    for j in range(lineas * 2):
        if j >= lineas - i and j <= lineas + i:
            cadena += caracter
        else:
            cadena += " "
    print(cadena)
    cadena = ""

print()
frase = input("Introduce una frase: ")
num = int(input("Introduce un número para el cifrado: "))
aux = ""

for i in range(len(frase)):
    if (ord(frase[i]) + num) > 122:
        aux = aux + chr(ord(frase[i]) + num - 26)
    else:
        aux = aux + chr(ord(frase[i]) + num)

print("El texto cifrado es:", aux)