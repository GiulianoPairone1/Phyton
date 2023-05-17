#Se desea crear un programa que simule el funcionamiento basico de un vehiculo.
#-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
#-Crear su constructor
#-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
#-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
#-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.

class Vehiculo():

    def __init__(self , marca ,ruedas , color , enMarcha=False):
        self.marca =  marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha
    def arrancar(self):
        self.enMarcha = True
        print("Vehiculo en marcha")
    def tipoVehiculo(self):
        if self.ruedas==4:
            print("Es un automovil")
        else:
            print("Es un amotocicleta")
    def mostrar(self):
        print(self.marca)
        print(self.ruedas)
        print(self.color)
        print(self.enMarcha)



r12 = Vehiculo("Renault" , 4 , "Rojo")
r12.arrancar()
r12.tipoVehiculo()
r12.mostrar()