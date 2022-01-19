import csv

#volcamos el contenido del .csv a una lista
with open("./EjerciciosCSV/LaLiga.csv") as f:
    datos = csv.reader(f)
    resultados = list(datos)

#visualizamos los resultados de todos los partidos
for resultado in resultados:
    if resultado == resultados[0]:
        print(resultado[2],":")
    else:
        print(resultado[2])

print()
contL = 0
contV = 0
contE = 0
#si hay mas equipos locales o visitantes que hayan ganado y cuantos de cada uno
for resultado in resultados[1:]:
    #transformamos el resultado en una lista para poder operar
    operacion = resultado[2].split("-")
    #convertimos el string en entero
    if int(operacion[0]) > int(operacion[1]):
        contL += 1
    elif int(operacion[0]) < int(operacion[1]):
        contV += 1
    else:
        contE += 1
    

if contL > contV:
    print("Han ganado mas equipos locales esta jornada")
else:
    print("Han ganado mas equipos visitantes esta jornada")

print("Hay", contL, "equipos locales que han ganado esta semana")
print("Hay", contV, "equipos visitantes que han ganado esta semana")

