'''
@author: Ritces Parra    carnet: 12-11088
@author: Carlos Perez    carnet: 13-11089
'''

class Persona(object):

    '''
    Constructor de la clase
    
    atributos:
        nombre :: str  // string que representa el(los) nombre(s) del dueno de la billetera
        apellido :: Persona // string que representa el(los) apellido(s) del dueno de la billetera
        ci :: int // numero que representa la cedula de identidad de la persona duena de la billetera
        
    '''

    def __init__(self, nombre, apellido, ci):

        self.nombre = nombre

        self.apellido = apellido

        self.ci = ci