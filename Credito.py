'''
@author: Ritces Parra    carnet: 12-11088
@author: Carlos Perez    carnet: 13-11089
'''

import decimal
import datetime

class Credito(object):

    '''
    Constructor de la clase
    
    atributos:
        monto :: number  // numero que representa el monto de la transaccion
        id_recarga :: int // numero que representa el id de la transaccion
        
    '''
    
    def __init__(self, monto, id_recarga):

        try:

            assert(type(monto) is int or type(monto) is float)

            self.monto = decimal.Decimal(monto)

            self.fecha_recarga = datetime.datetime.now()

            self.id_recarga = id_recarga

        except:

            self.fecha = None

            self.id_recarga = None

            self.monto = None