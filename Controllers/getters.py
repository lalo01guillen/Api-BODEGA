import psycopg2
from config import config
from datetime import datetime
from helpers import getIdProds
from helpers import superquery
def getAllEdos():
    """ Obtiene todos los estados """ 
    sql = """select * from cat_estado;"""
    conn = None
    resultado= None
    respuesta = []
    now = datetime.now()
    print(now)
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
                respuesta.append({ 
                    'Id': i[0],
                    'Estado': i[1]
                }) 
           
    return respuesta


def getInventarioByUser(userName):
    """ Obtiene todos los estados """ 
    sql = """
select
clientes.nombre,
clientes.apellido,
cat_productos.descripcion,
clientes.id_cliente,
cat_productos.id_producto,
sum(I.cantidad)
FROM inventario I
    inner join entrada
    on entrada.id_inventario=I.id_inventario
    inner join clientes
    on clientes.id_cliente= I.id_cliente
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by clientes.apellido,cat_productos.id_producto,clientes.nombre,cat_productos.descripcion,I.id_inventario,clientes.id_cliente
    order by clientes.apellido,clientes.nombre;
    """
    conn = None
    resultado= None
    filtrada = []
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
            print(type(resultado))  
            for elemento in resultado:
                if userName == elemento[0]:
                    filtrada.append(elemento)            
    return filtrada

def getAllInventario():
    """ Obtiene todos los estados """ 
    sql = "select * from inventario"
    conn = None
    resultado= None
    cat_Prods_Id = getIdProds.getIdCat_prods()
    print(cat_Prods_Id)
    filteredArr = []
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
        for i in cat_Prods_Id:
            sumValue = 0
            for j in resultado:
                if i[0] == j[1]:
                    sumValue += j[3] 
            filteredArr.append([i[1],sumValue])

    return filteredArr


def getUserId(userName):
    """ Obtiene todos los estados """ 
    sql = f"select * from  clientes c  where nombre = '{userName}'"
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
        
    return resultado[0][0]




def getAllBOxesUser(userId):
    """ Obtiene todos los estados """ 
    sql = f"select * from inventario where id_cliente = '{userId}'; "
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


def getAllUser():

    """ Obtiene todos los estados """

    sql = """select * from clientes ;"""

    conn = None

    resultado= None

    respuesta= []

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

            print("ERROR EN CONEXION")  

            conn.close()

            #codear resultado

            for arr in resultado:

                respuesta.append({"NOMBRE": arr[1],"apellido": arr[2]})



    return respuesta


def getUserByName(name):

    """ Obtiene todos los estados """

    sql = f"""select * from clientes where nombre = '{name}';"""

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

            #codear resultado

            print(name)



    return {"NOMBRE": resultado[0][1],"APELLIDO": resultado[0][2], "DIRECCION": resultado[0][3], "TELEFONO": resultado[0][4]}



def getHistoryProducts():

    """ Obtiene todos los estados """

    sql = superquery.superQry()

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

def getHistoryProductsByUser(userName):

    """ Obtiene todos los estados """

    sql = f"""
select
DATE_TRUNC('day',entrada.fecha_de_registro),
clientes.nombre,
clientes.apellido,
cat_productos.descripcion,
--clientes.id_cliente,
--cat_productos.id_producto,
sum(I.cantidad)
FROM inventario I 
	inner join entrada
	on entrada.id_inventario=I.id_inventario
	inner join clientes
	on clientes.id_cliente= I.id_cliente
	inner join cat_productos
	ON cat_productos.id_producto = I.id_producto
	where I.id_inventario in( select id_inventario from entrada 
							 where clientes.nombre='{userName}')
	group by DATE_TRUNC('day',entrada.fecha_de_registro),clientes.nombre,clientes.apellido,cat_productos.descripcion
	order by clientes.nombre
    """

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


    
def getHistoryProductsByUserSALIDAS(userName):

    """ Obtiene todos los estados """

    sql = f"""
select
DATE_TRUNC('day',salida.fecha_de_registro),
clientes.nombre,
clientes.apellido,
cat_productos.descripcion,
--clientes.id_cliente,
--cat_productos.id_producto,
sum(I.cantidad)
FROM inventario I 
	inner join salida
	on salida.id_inventario=I.id_inventario
	inner join clientes
	on clientes.id_cliente= I.id_cliente
	inner join cat_productos
	ON cat_productos.id_producto = I.id_producto
	where I.id_inventario in( select id_inventario from salida 
							 where clientes.nombre='{userName}')
	group by DATE_TRUNC('day',salida.fecha_de_registro),clientes.nombre,clientes.apellido,cat_productos.descripcion
	order by clientes.nombre
    """

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


    
