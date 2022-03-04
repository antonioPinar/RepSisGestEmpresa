import csv

from sqlalchemy import false, true

def csvALista(fichero):
    calificaciones = []
    with open(fichero, "r") as f:
        #obtenemos todo el fichero
        datos = csv.reader(f, delimiter = ';')
        #lo pasamos a una lista
        registros = list(datos)
        cabecera = registros[0]
        #recorremos los datos de todas las personas
        for dato in registros[1:]:
            calificacion = {}
            for i in range(len(dato)):
                calificacion[cabecera[i]] = dato[i]
            
            #introduciomos la calificacion en la lista total   
            calificaciones.append(calificacion)

    return calificaciones


def notaFinal(lista):
    #recogemos cada uno de los dicc
    for dic in lista:
        sumCal = 0
        sumPrac = 0
        notaEx = 0
        notaPrac = 0
        notaF = 0
        for campo in dic.keys():
            if "examen" in campo:
                sumCal += float(dic[campo])
            if "practicas" in campo:
                sumPrac += float(dic[campo])
        notaEx = (sumCal/3 * 60) / 100
        notaPrac = (sumPrac/3 * 40) / 100
        notaF = notaEx + notaPrac
        #añadimos el nuevo campo notaF al dicc
        dic['nota final'] = notaF
    


def varemoAlumns(lista):
    listAprob = []
    listSusp = []
    for dic in lista:
        numPorcen = str(dic['Asistencia'])
        if int(numPorcen[0:2]) < 75:
            listSusp.append(dic)
        elif float(dic['nota final']) < 5:
            listSusp.append(dic)
        elif float(dic['1er trimestre examen']) < 5:
            listSusp.append(dic)
        elif float(dic['1er trimestre practicas']) < 5:
            listSusp.append(dic)
        elif float(dic['2do trimestre examen']) < 5:
            listSusp.append(dic)
        elif float(dic['2do trimestre practicas']) < 5:
            listSusp.append(dic)
        elif float(dic['3er trimestre examen']) < 5:
            listSusp.append(dic)
        elif float(dic['3er trimestre practicas']) < 5:
            listSusp.append(dic)
        else:
            listAprob.append(dic)

    return listAprob, listSusp


calificaciones = csvALista("calificaciones.csv")
notaFinal(calificaciones)
resultado = varemoAlumns(calificaciones)
print(f"lista de aprobados: {resultado[0]}\n")
print(f"lista de suspensos: {resultado[1]}")



