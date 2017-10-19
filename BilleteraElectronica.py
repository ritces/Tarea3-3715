'''
@author: Ritces Parra    carnet: 12-11088
@author: Carlos Perez    carnet: 13-11089
'''

import decimal

class BilleteraElectronica(object):
   
    '''
    Constructor de la clase
    
    atributos:
        id :: int  // numero que representa la identificacion de la billetera
        persona :: Persona // clase persona que contiene los datos del dueno de la billetera
        pin :: int // numero que representa la clave secreta para autorizar transacciones con la billetera
        
    '''
    def __init__(self, id, persona, pin):
        
        if type(pin) != int:

            raise TypeError("El PIN debe ser de tipo 'int'")

        self.id = id

        self.persona = persona
        
        self.pin = pin

        self.creditos = []

        self.debitos = []

        self.saldo_actual = decimal.Decimal(0)
        
        
    #Devuelve el saldo actual de la billetera    
    def devCreditos(self):
        
        return self.creditos
    
    
    #Devuelve la lista de debitos que se han realizado
    def devDebitos(self):
        
        return self.debitos
    
    
    #Devuelve la lista de creditos que se han realizado
    def saldo(self):

        return self.saldo_actual

    
    #Recibe un objeto Credito y recarga el saldo de la billetera
    def recargar(self, recarga):

        if (recarga.monto <= 0):

            return -1

        

        self.creditos.append(recarga)

        self.saldo_actual += recarga.monto

        
    #Recibe un objeto Debito y descuenta el monto de la transaccion
    def consumir(self, consumo):

        if (self.pin != consumo.pin_debito):

            return -1


        if (consumo.monto > self.saldo_actual):
            
            return -1
        
        self.debitos.append(consumo)
            
        self.saldo_actual -= consumo.monto