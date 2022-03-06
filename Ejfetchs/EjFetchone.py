import psycopg2

conn = None 
sql = """
        select anno, (sum(colision_doble) + sum(colision_multiple) + sum(choque_con_objeto_fijo) + sum(caida_motocicleta) + sum(caida_ciclomotor) + sum(caida_bicicleta) + sum(caida_viajero_bus) + sum(otras_causas))
            from accidentes
            group by anno
            order by 1;

"""

try:
    #creamos conexión
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="pruebadb",
        user="prueba",
        password="prueba")
        
    #creamos un cursor
    cur = conn.cursor()
    
    #ejecutamos la query
    cur.execute(sql)
    
    #recuperamos la primera fila de la query que se encuentra en el cursor
    fila = cur.fetchone()
    #recorremos el cursor hasta que no haya mas datos devueltos
    while fila is not None:
        print(f"El total de accidentes en el año {fila[0]} es de {fila[1]}")
        input("Pulsa ENTER para continuar")
        fila = cur.fetchone()
        
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')
        