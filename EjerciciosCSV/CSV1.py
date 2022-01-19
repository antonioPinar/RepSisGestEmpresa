import csv

listaLiga = [["equipo local", "equipo visitante", "resultado", "tarjetas amarillas", "tarjetas rojas", "espectadores"],["Levante", "Mallorca", "2-0", "4", "1", "21000"],
    ["Real Sociedad", "Celta de Vigo", "1-0", "6", "0", "23000"],["Granada", "Barcelona", "1-1", "5", "1", "39000"],["Real Madrid", "Valencia", "4-1", "6", "0", "42510"],
    ["Rayo Vallecano", "Betis", "1-1", "4", "1", "28300"],["Sevilla", "Getafe", "1-0", "4", "0", "51000"],["Alaves", "Athletic", "0-0", "2", "0", "27012"],
    ["Osasuna", "Cadiz", "2-0", "4", "0", "31200"],["Villarreal", "Atletico de Madrid", "2-2", "0", "1", "44100"],["Espanyol", "Elche", "1-2", "10", "0", "18000"]]

#creamos el .csv y abrimos flujo de escritura 
with open("./EjerciciosCSV/LaLiga.csv", "w") as fichero:
    #creamos puntero para poder escribir en el CSV y despues escribimos en el
    writer = csv.writer(fichero, lineterminator = "\n")
    for elemento in listaLiga:
        writer.writerow(elemento)

#leemos el fichero .csv linea a linea
with open("./EjerciciosCSV/LaLiga.csv", "r") as f:
    resultados = csv.reader(f)
    for partido in resultados:
        print(partido)
