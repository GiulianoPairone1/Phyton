#Se desea realizar un sistema para una jugueteria.  (5 puntos)
#Crear una clase llamada “juguete” con atributos : nombre, precio, color,porcentajeDescuento(opcional, por defecto 0 ),
#Un constructor
#Una property precioConDescuento calculada a partir del precio y porcentaje de descuento
#validarDescuento(): Validar que el porcentaje de descuento sea entre 0 y 100. En caso verdadero devolver un booleano verdadero, caso contrario un booleano falso


from dataclasses import dataclass
from operator import truediv
from pickle import TRUE

#contructor
@dataclass
class juguete:
    #define automaticamente serie de meotdos
    #Son metodos magicos
    nombre:str
    precio:float
    color:str
    porcentajeDescuento:int=0

    #property
    @property
    def preciocondescuento(self):
        return round(self.precio-(self.precio*self.porcentajeDescuento),2)

    def validarDescuento(self):
        if(0<=self.porcentajeDescuento<=100):
            return True
        return False