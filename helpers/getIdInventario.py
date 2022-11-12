import psycopg2
from config import config


def getIdInventario(userId,prodId):

    """ Obtiene todos los estados """

    sql = f"select  * from inventario i where id_cliente = '{userId}' and id_producto = '{prodId}';"

    conn = None

    resultado= None

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

    return resultado