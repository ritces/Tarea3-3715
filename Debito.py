'''
@author: Ritces Parra    carnet: 12-11088
@author: Carlos Perez    carnet: 13-11089
'''

import decimal
import datetime

class Debito(object):   
    
    '''
    Constructor de la clase
    
    atributos:
        monto :: number  // numero que representa el monto de la transaccion
        id_consumo :: int // numero que representa el id de la transaccion
        pin_debito :: int // numero que representa el pin introducido para autorizar la transaccion
        
    ''' 

    def __init__(self, monto, id_consumo, pin_debito):

        try:

            assert(type(monto) is int or type(monto) is float)

            self.monto = decimal.Decimal(monto)

            self.fecha_consumo = datetime.datetime.now()

            self.id_consumo = id_consumo
            
            self.pin_debito = pin_debito

        except:

            self.fecha = None

            self.id_consumo = None

            self.monto = None
