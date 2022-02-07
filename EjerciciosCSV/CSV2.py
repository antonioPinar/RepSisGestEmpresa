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

#variables 
contL = 0
contV = 0
contE = 0
golesTotales = 0
tarjetasTotales = 0
numEspectadorT = 0
contT = 0
#si hay mas equipos locales o visitantes que hayan ganado y cuantos de cada uno
for resultado in resultados[1:]:
    #transformamos el resultado en una lista para poder operar
    operacion = resultado[2].split("-")

    #sumamos el numero total de goles de todos los partidos
    golesTotales += int(operacion[0]) + int(operacion[1])

    #convertimos el string en entero
    if int(operacion[0]) > int(operacion[1]):
        contL += 1
    elif int(operacion[0]) < int(operacion[1]):
        contV += 1
    else:
        contE += 1

    #contamos numero total de tarjetas en todos los partidos
    tarjetasTotales += int(resultado[3]) + int(resultado[4])

    #numero total de espectadores en todos los partidos y la media
    contT += 1
    numEspectadorT += int(resultado[5])

mediaEspectadores = numEspectadorT / contT
    

if contL > contV:
    print("Han ganado mas equipos locales esta jornada")
else:
    print("Han ganado mas equipos visitantes esta jornada")

print("Hay", contL, "equipo(s) locales que han ganado esta semana")
print("Hay", contV, "equipo(s) visitantes que han ganado esta semana")
print("Esta jornada, ha habido", golesTotales, "goles en total")
print("Esta jornada, ha habido", tarjetasTotales, "tarjetas en total")
print("El numero de espectadores totales esta jornada es de", numEspectadorT, "personas, con una media de", mediaEspectadores, "espectadores por partido")