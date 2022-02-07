import os
import shutil

#creamos funcion para introducir en diccionario datos que recuperamos de una estructura de ficheros/directorios
def crearDicDeFichero():
    diccNum = {}
    #abrimos el directorio principal
    listarDirec = os.listdir("numeros")

    #dentro del directorio principal, descomponemos la estructura hasta llegar al archivo
    for dir in listarDirec:
        with open(os.path.join("numeros", dir, dir+".txt")) as f:
            #leemos los datos que hay en cada fichero
            lineaDatos = f.readline()
            listaDatos = lineaDatos.split(",")
            listaDatos.pop(0)

            #creamos diccionario para limpiar datos de cada fichero, y luego lo añadimos al dicc final
            dicDatos = {}
            for dato in listaDatos:
                datoSeparado = dato.split("=")
                dicDatos[datoSeparado[0]] = datoSeparado[1]

                #agregamos los datos al diccionario final
                diccNum[dir] = dicDatos
    
    return diccNum

#creamos funcion para borrar toda la estructura del directorio creado
def borrarDirectorio():
    shutil.rmtree("numeros")
    print("Estructura de directorios borrada con exito")

#ejecutamos 
print(crearDicDeFichero())

borrarDirectorio()
