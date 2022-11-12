from Controllers import Setters,getters
from helpers import getIdInventario
from config import config

var = config()
userObj = {'USERNAME': 'LUIS', 
           'ENTRADAS': [['a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',1],
                        ['b0eebc99-7c0b-4ef8-bb6d-6bb9bd380a11',1],['b0eebc99-7c0b-5ef8-bb6d-6aa2ad380a11',0],['c0cccc29-1a0a-5ef8-bb6d-6aa2ad380a11',0]]
          }
#userName = 'CESAR RODRIGO'
#cantidadActualUser = getters.getInventarioByUser(username)
# userID = getters.getUserId(userName)
#idInv = getIdInventario.getIdInventario('a1eacc19-5a1a-5ae8-ba5c-9bc9ba430a29','a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11')
# result = getters.getAllBOxesUser(userID)
    
# for i in result:
#          print(i[1])

Setters.SetNewEntrada(userObj['USERNAME'],userObj['ENTRADAS'])
#Setters.SetNewSalida(userObj['USERNAME'],userObj['ENTRADAS'])

#print(idInv[0])
