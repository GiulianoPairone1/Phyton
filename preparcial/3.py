#Se desea realizar un sistema para la NASA.  (5 puntos)
#Crear una clase llamada “piloto” con atributos : nombre, apellido, edad (int), estudiosUniversitarios ( Booleano ) , pais ( opcional, en caso de que no se posea pais el valor por defecto es “NA” ).
#Un constructor
#mostrar() : Mostrar los datos del piloto
#esMayor(): Valida que el piloto sea mayor de edad, devolviendo un booleano con valor verdadero en caso de que sea afirmativo y falso en caso contrario.
#Crear una clase llamada “cohete”  con atributos : modelo,piloto,combustibleTotal,consumoPorKilometro
#Un constructor
#mostrar () : Mostrar los datos de la nave
#calcularFactibilidad ( distancia ) : Determinar si es factible o no el viaje de la nave espacial teniendo en cuenta el consumo del combustible.  La función debe de devolver un  booleano verdadero si el viaje es factible y falso si no lo es.

from statistics import mode


class Piloto:
    def __init__(self,nombre,apellido,edad,estudiosUniversitarios,pais='NA'):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.estudiosUniversitarios=estudiosUniversitarios
        self.pais=pais
    def mostrar(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)
        print(self.estudiosUniversitarios)
        print(self.pais)
    
    def esMayor(self):
        if(self.edad > 17):
            return True
        return False

ejemplo_Piloto=Piloto("JUan","Perez",75,False)
print(ejemplo_Piloto.mostrar())
print(ejemplo_Piloto.esMayor())


class Cohete:
    def __init__(self,modelo,piloto,combustibleTotal,consumoxKilomentro):
        self.modelo=modelo
        self.piloto=piloto
        self.combustibleTotal=combustibleTotal
        self.consumoxKilomentro=consumoxKilomentro
    
    def mostrar(self):
        print(self.modelo)
        #print(self.piloto)#Mal
        self.piloto.mostrar()
        print(self.combustibleTotal)
        print(self.consumoxKilomentro)

    def calcularfactibilidad(self,distancia):
        if(self.consumoxKilomentro*distancia<self.combustibleTotal):
            return True
        return False

ejemplo_cohete=Cohete("Apolo",ejemplo_Piloto,16,1)
ejemplo_cohete.mostrar()
print(ejemplo_cohete.calcularfactibilidad(50))
        