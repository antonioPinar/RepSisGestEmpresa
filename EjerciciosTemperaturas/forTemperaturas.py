#libreria para tratar datos
import pandas as pd
#creamos un dataset que es una estructura de formato tabla
df=pd.read_csv("EjerciciosTemperaturas/temperaturas.csv", sep = ";")
print(df.head())

# convertimos el dataset lista de listas
lista=df.to_numpy().tolist()
#print(lista)

mediaMax = 0
mediaMin = 0

for i in range(len(lista)):
    print("fecha:", lista[i][0], "temperatura máxima:", lista[i][1], "temperatura mínima:",lista[i][2], 
    "temperatura media:", (lista[i][1] + lista[i][2] / 2))

    mediaMax += lista[i][1]
    mediaMin += lista[i][2]

print("\nMedia de las temperaturas máximas:", round(mediaMax / len(lista), 2))
print("Media de las temperaturas mínimas:", round(mediaMin / len(lista), 2))