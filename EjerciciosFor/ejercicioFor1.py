import math

cadena = str("maquinaria")
lista = [2, 4.5, "hola", 65, 9.7, "adios"]
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript']}

for i in cadena:
    print(i)

print()
for i in lista:
    print(i)

print()
for v, i in diccionario.items():
    print(v, "=", i)


print()
aux = ""
cad = input("Introduce una cadena: ")
for i in range(len(cad)):
    if cad[i].lower():
        aux += cad[i].upper()
print("    ",aux)


print()
list = [2, 3, 5, 67, 66, 22, 48, 123, 2022, 11, 3456]
for num in list:
    if num % 2 == 0:
        print(math.pow(num, 2))
    else:
        print(math.sqrt(num))

