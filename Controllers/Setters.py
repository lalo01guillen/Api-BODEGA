import psycopg2
from config import config
from datetime import datetime
from helpers import getIdInventario
from helpers import folioGenerator
import uuid
from Controllers import getters
#hola
def SetNewEntrada(username,arrboxes):    #{USERNAME: 'CESAR RODRIGO' ENTRADAS: [['a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',10],['b0eebc99-7c0b-4ef8-bb6d-6bb9bd380a11',5],['b0eebc99-7c0b-5ef8-bb6d-6aa2ad380a11',2]]}
    """ Obtiene todos los estados """ 
    #RECORTAR EL ID GENERADO PARA EL FOLIO
    now = datetime.now()
    folio = folioGenerator.folioG()
    userId = getters.getUserId(username)
    userBoxes = getters.getAllBOxesUser(userId)
    arrRes = []
    for i in arrboxes:
        idInvent = getIdInventario.getIdInventario(userId,i[0])
        idEntrada = uuid.uuid4()
       # idInvNewCreate = uuid.uuid4()   para ingrear nuevo cliente 
        operacionNuevoValue = None
        for j in userBoxes: 
            if j[1] == i[0]:
                operacionNuevoValue = j[3] + i[1]  #el id inventario despues del insert es idInvent[0][0]
        sql = f"""INSERT INTO entrada (id_entrada, folio, id_inventario,fecha_de_registro,fecha_ultima_modificacion) 
        VALUES ('{idEntrada}', '{folio}', '{idInvent[0][0]}','{now}','{now}');"""
       # sql3 = f"""INSERT INTO inventario (id_inventario,id_producto,id_cliente, cantidad, fecha_de_registro, fecha_ultima_modificacion)
       # VALUES ('{idInvNewCreate}','{i[0]}', '{userId}','{i[1]}','{now}','{now}') """
        sql2 = f"UPDATE inventario SET cantidad = {operacionNuevoValue} , fecha_ultima_modificacion = '{now}' WHERE id_inventario = '{idInvent[0][0]}';"
        arrRes.append(sql2)
       # arrRes.append(sql3)
        arrRes.append(sql)
    conn = None    
   
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        for i in arrRes:
           
            cur.execute(i)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()  
            
                        
    print('se insertó correctamente') 

def SetNewSalida(username,arrboxes):    #{USERNAME: 'CESAR RODRIGO' ENTRADAS: [['a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',10],['b0eebc99-7c0b-4ef8-bb6d-6bb9bd380a11',5],['b0eebc99-7c0b-5ef8-bb6d-6aa2ad380a11',2]]}
    """ Obtiene todos los estados """ 
    #RECORTAR EL ID GENERADO PARA EL FOLIO
    now = datetime.now()
    folio = folioGenerator.folioG()
    userId = getters.getUserId(username)
    userBoxes = getters.getAllBOxesUser(userId)
    arrRes = []
    for i in arrboxes:
        idInvent = getIdInventario.getIdInventario(userId,i[0])
        idSalida = uuid.uuid4()
        operacionNuevoValue = None
        for j in userBoxes: 
            if j[1] == i[0] and j[3]>= i[1]:
                operacionNuevoValue = j[3] - i[1]
        sql = f"""INSERT INTO salida (id_salida, folio, id_inventario,fecha_de_registro,fecha_ultima_modificacion) 
        VALUES ('{idSalida}', '{folio}', '{idInvent[0][0]}','{now}','{now}');"""
        sql2 = f"UPDATE inventario SET cantidad = {operacionNuevoValue} , fecha_ultima_modificacion = '{now}' WHERE id_inventario = '{idInvent[0][0]}';"
        arrRes.append(sql)
        arrRes.append(sql2)
    conn = None    
   
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        for i in arrRes:
           
            cur.execute(i)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()  
            
                        
    print('se insertó') 