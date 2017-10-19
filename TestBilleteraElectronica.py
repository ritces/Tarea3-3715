'''
@author: Ritces Parra    carnet: 12-11088
@author: Carlos Perez    carnet: 13-11089
'''

import unittest

from BilleteraElectronica import BilleteraElectronica
from Persona import Persona
from Credito import Credito
from Debito import Debito


# La clase servicios test es utilizada para los casos de prueba unitarios, usando el plugin PyUnit

class ServiciosTest(unittest.TestCase):

    def setUp(self):
        
        carlos = Persona("Alvin", "Yakitori", 1)
        
        self.billetera = BilleteraElectronica(13, carlos, 1234)
        
    '''
    Funcionalidades
    '''  
        
    #Verifica que la recarga se ejecute de manera exitosa
    def testRecargaExitosamente(self):
        
        credito = Credito(1000, 1)
        self.billetera.recargar(credito)
        
        self.assertEquals(1000, self.billetera.saldo())
        
        
    #Verifica que una transaccion se realice de manera correcta 
    def testConsumoPinCorrectoMontoSuficiente(self):
        
        credito = Credito(1000, 1)
        self.billetera.recargar(credito)

        debito = Debito(800, 1, 1234)
        
        self.assertNotEquals(-1, self.billetera.consumir(debito))
        self.assertEquals(200, self.billetera.saldo())
        
        
    #Verifica que las transacciones estan siendo almacenadas debidamente
    def testAlmacenTransacciones(self):
        
        credito = Credito(1000, 1)
        self.billetera.recargar(credito)
        
        credito1 = Credito(100, 10)
        self.billetera.recargar(credito1)
        
        debito = Debito(100, 1, 1234)
        self.billetera.consumir(debito)
        
        self.assertEquals(2, len(self.billetera.devCreditos()))
        self.assertEquals(1, len(self.billetera.devDebitos()))
        self.assertEquals(1000, self.billetera.saldo())
        
        
    '''
    Fronteras
    '''
        
    #Verifica que el estado inicial del saldo de una billetera electronica es 0
    def testSaldoNulo(self):
        
        self.assertEquals(0, self.billetera.saldo())
        


    #Verifica que si el pin introducido en la transaccion no es correcto, la transaccion no se ejecute
    def testConsumoPinIncorrectoSaldoCorrecto(self):
        
        credito = Credito(2000, 1)
        self.billetera.recargar(credito)
        
        debito = Debito(1200, 1, 1254)
        
        self.assertEquals(-1, self.billetera.consumir(debito))
        self.assertEquals(2000, self.billetera.saldo())
        
        
    #Verifica que si el saldo de la billetera electronica no es suficiente, la transaccion no se ejecute
    def testConsumoPinCorrectoSaldoInsuficiente(self):
        
        credito = Credito(1000, 1)
        self.billetera.recargar(credito)
        
        debito = Debito(1200, 1, 1234)
        
        self.assertEquals(-1, self.billetera.consumir(debito))
        self.assertEquals(1000, self.billetera.saldo())
        
        
    '''
    Esquinas
    '''
        
    #Verifica que una transaccion con Pin incorrecto no pase a pesar de que tampoco tiene saldo suficiente
    def testConsumoPinIncorrectoSaldoInsuficiente(self):
        
        credito = Credito(1199, 1)
        self.billetera.recargar(credito)
        
        debito = Debito(1200, 1, 1234)
        
        self.assertEquals(-1, self.billetera.consumir(debito))
        self.assertEquals(1199, self.billetera.saldo())
        
        
    '''
    Malicia
    '''
        
    #Verifica que no se puedan recargar saldos negativos
    def testRecargaSaldoIncorrecto(self):
        
        credito = Credito(-1000, 1)
        
        self.assertEquals(-1, self.billetera.recargar(credito))
        self.assertEquals(0, self.billetera.saldo())
        
        
    
        
        
    
    