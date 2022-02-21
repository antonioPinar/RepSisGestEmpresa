# -*- coding: utf-8 -*-
import psycopg2

conn = None

def creartuplaSQL():
    scriptCrearTabla = ""
    listScript = []
    #abrimos el fichero donde esta el script de la cracion de la tabla
    with open("tabla-pisos.sql", "r") as f:
        scriptCrearTabla = f.read()
        #buscamos el nombre de la tabla y lo reemplazamos
        scriptCrearTabla = scriptCrearTabla.replace("pisos", "pisosNuevos")

    #abrimos el fichero donde estan los datos a insertar
    with open("pisos (1).sql", "r", encoding = "utf-8") as f:
        #añadimos el script de creacion de tabla
        listScript.append(scriptCrearTabla)
        #añadimos cada insert del fichero a la lista
        for linea in f:
            linea = linea.replace("pisos", "pisosNuevos")
            listScript.append(linea)
        
    return listScript

try:
    #creamos conexión
    conn = psycopg2.connect(
        host="localhost",
        database="pruebadb",
        user="prueba",
        password="prueba")
    #creamos un cursor
    cur = conn.cursor()
    #ejecutamos la query
    sql = creartuplaSQL()
    for query in sql:
        cur.execute(query)

    conn.commit()
    #cerramos el cursor
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')