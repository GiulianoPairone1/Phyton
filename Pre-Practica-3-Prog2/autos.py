from dataclasses import dataclass
from typing import ClassVar

'''
Se desea crear un programa que simule el funcionamiento basico de un auto.

-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.
'''


#@dataclass
#class Vehiculo:
#    marca:str
#    ruedas:int
#    color:str
#    precio:str
#    enMarcha:bool=False




#De esta forma es la convencional

class Vehiculo:



    #Variable de clase. - Se colocan los 2 "__"
    __iva=0.21

    #Constructor
    def __init__(self,marca,ruedas,color,precio,enMarcha=False):
        #Desde aca
        self.marca=marca
        self.ruedas=ruedas
        self.color=color
        self.enMarcha=enMarcha
        self.precio=precio    
        #Hasta aca
        #Variables de instancia.
    
    #Una propery es una variable, como las que yo asigno en el constructor, pero calculada.
    @property
    def precioConEfectivo(self):
        return self.precio*0.9

    #Desde aca
    def arrancar(self):
        self.enMarcha=True
    
    def tipoVehiculo(self):
        if (self.ruedas==2):
            return "Motocicleta"
        else:
            return "Automovil"
    
    def mostrar(self):
        print(self.marca)
        print(self.ruedas)
        print(self.color)
        print(self.precio)
        print(self.enMarcha)
    #Hasta aca 
    #Metodos de instancia

    #Metodo de clase
    #Arroba y classmethod
    @classmethod
    def mostrarIva(cls):
        return cls.__iva

#Necesito instanciar para utilizar metodos de instancia
vehiculo=Vehiculo("Ford",2,"Gris",50,False)
vehiculo.mostrar()
print(vehiculo.precioConEfectivo)
#Aca no necesito instanciar.
Vehiculo.mostrarIva()


#Vehiculo.nuevoIva(0.50)
#vehiculo.mostrar()