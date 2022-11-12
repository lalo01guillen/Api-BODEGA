import psycopg2
from config import config

def getIdCat_prods():

    """ Obtiene todos los estados """

    sql = f"select  * from cat_productos;"

    conn = None

    resultado= None
    resultArr = []
    try:

        # read database configuration

        params = config()

        # connect to the PostgreSQL database

        conn = psycopg2.connect(**params)

        # create a new cursor

        cur = conn.cursor()

        # execute the INSERT statement

        cur.execute(sql)

        # get the generated id back

        resultado = cur.fetchall()

        # commit the changes to the database

        conn.commit()

        # close communication with the database

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:
            conn.close()
            for i in resultado:
                resultArr.append([i[0],i[1]]) 
    return resultArr