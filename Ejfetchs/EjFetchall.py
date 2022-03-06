import psycopg2
conn=None

sql = """
    select *
        from pisos
        where direccion like ('%M_stoles%');
"""

totalP = 0
totalC = 0
precioP = 0
precioC = 0

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
    
    consultas = cur.fetchall()
    
    for row in consultas:
        if row[2].startswith("Piso"):
            totalP = totalP + 1
            precioP = precioP + row[3]
        elif row[2].find("chalet") != -1 or row[2].startswith("Chalet"):
            totalC = totalC + 1     
            precioC = precioC + row[3]    
        
    cur.close()

    print(f"Hay un total de {totalP} pisos en Mostoles")
    print(f"Hay un total de {totalC} chalets en Mostoles")
    print("Media de precio de los pisos en Mostoles: {:,.2f}€".format(precioP / totalP))
    print("Media de precio de los chalets en Mostoles: {:,.2f}€".format(precioC / totalC))
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')
    
