import psycopg2

conn = None

#creamos la tupla sql
sql =( """
    create table futbolistas(
        dni varchar(10) primary key,
        nombre varchar(30) not null,
        apellidos varchar(80) not null,
        posicion varchar(30) not null,
        equipo varchar(30) not null
    )
    """, 
    """
    INSERT INTO futbolistas VALUES('49211440G', 'Juan', 'Daniel Samba', 'delantero', 'deportivo loranca')
    """,
    """
    INSERT INTO futbolistas VALUES('49011840T', 'David', 'Salazar', 'portero', 'miraflor')
    """,
    """
    INSERT INTO futbolistas VALUES('49100180V', 'Miguel', 'Contreras', 'defensa', 'miraflor')
    """,
    """
    INSERT INTO futbolistas VALUES('49461000G', 'Samuel', 'Cavanilias', 'delantero', 'arroyo')
    """,
    """
    INSERT INTO futbolistas VALUES('49100440Y', 'Bryan', 'Sadowski', 'defensa', 'miraflor')
    """
)

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