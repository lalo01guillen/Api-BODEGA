from urllib import response
from flask import Flask, request, Response
from flask import jsonify
from Controllers import getters,Setters
def create_app():
    app = Flask(__name__)
    return app

app = create_app()



@app.route('/', methods=['GET'])
def wellcome():
    response= """----Bienvenido a la API de la bodega----
    *Obtener todos los estados   /estados
    *Obtener todo el inventario /inventario
    *Obtener inventario por cliente /inventario/CLIENTE NAME
    *Obtener todos los ususarios /clientes
    *Obtener cliente por nombre /clientes/CLIENTE NAME
    *Obtener un historial de productos por dia /historialProductos
    *Obtener un historial de productos por dias por clientes ENTRADAS  /historialProductosENTRADAS/NOMBRE CLIENTE
    *Obtener un historial de productos por dias por clientes SALIDAS  /historialProductosSALIDAS/NOMBRE CLIENTE
    *Agregar nueva entrada /newEntrada   DATA EN JSON
    *Agregar nueva salida /newSalida     DATA EN JSON
    """
    return response

@app.route('/estados', methods =['GET'])
def RouteGetAllEdos():
    response = getters.getAllEdos()
    return jsonify(response)

@app.route('/clientes', methods =['GET'])
def RouteGetAllUsers():
    response = getters.getAllUser()
    return jsonify(response)

@app.route('/clientes/<string:name>', methods=['GET'])
def getUserById(name):

                    response = getters.getUserByName(name.upper())
                    return jsonify(response)


@app.route('/inventario', methods=['GET'])
def getAllInventario():

        response = getters.getAllInventario()

    
        return jsonify(response)


@app.route('/inventario/<string:name>', methods=['GET'])
def getInventarioByUser(name):
    
                    response = getters.getInventarioByUser(name.upper())
    
                    return jsonify(response)

@app.route('/historialProductosENTRADAS/<string:name>', methods=['GET'])
def getHistoryProdByUser(name):

                    response = getters.getHistoryProductsByUser(name.upper())
                    return jsonify(response)

@app.route('/historialProductosSALIDAS/<string:name>', methods=['GET'])
def getHistoryProdByUserSALIDAS(name):

                    response = getters.getHistoryProductsByUserSALIDAS(name.upper())
                    return jsonify(response)

@app.route('/historialProductos', methods=['GET'])
def getHistoryProds():
    response = getters.getHistoryProducts()
    return jsonify(response)

@app.route('/newEntrada', methods=['POST'])
def setNewEntrada():
     request_data = request.get_json()
     userName = request_data['USERNAME']
     arrBox = request_data['ENTRADAS']
     Setters.SetNewEntrada(userName.upper(),arrBox)
     return "insertado correctamente"

@app.route('/newSalida', methods=['POST'])
def setNewSalida():
     request_data = request.get_json()
     userName = request_data['USERNAME']
     arrBox = request_data['ENTRADAS']
     Setters.SetNewSalida(userName.upper(),arrBox)
     return "Se retiraron cajas correctamente"

if __name__ == '__app__':
    app.run(debug=True)  