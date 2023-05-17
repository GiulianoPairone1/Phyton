from dataclasses import dataclass
import string


lista = ["ho", 3.16, "la", 81, 6, 42]

#Tenemos varias opciones
# 1 : append basico, ir haciendo un append por cada posición de la lista
# 2 : append dentro de un bucle for, rango 3
# 3 : utilizando indexado.

def primeros_tres(lista):
    nueva_lista=[]
    #nueva_lista=lista[:3] Opción 2 

    for i in range(3):
       nueva_lista.append(lista[i])
    return nueva_lista

print(primeros_tres(lista))


#Definir una función que reciba una lista y devuelva el primer y ultimo elemento de la lista
#Ejemplo : 
lista = ["ho", 3.16, "la", 81, 6, 42]

def primero_ultimo(lista):
    nueva_lista=[]
    nueva_lista.append(lista[0])
    nueva_lista.append(lista[-1])
    return nueva_lista

#PRIMER EJERCICIO REALIZADO.

#SEGUNDO EJERCICIO : 

def concatena(string1,string2,nro):
    #numero_casteado=str(nro)
    concatenacion=string1+string2+str(nro)
    #return concatenacion

print(concatena("hola","como",1))

#TERCER EJERCICIO
#VEHICULO : patente, descripción ( por defecto no tiene)
#Parte 1

class Vehiculo:
    def __init__(self,patente,descripcion=''):
        self.patente=patente
        self.descripcion=descripcion

    def mostrar(self):
        print(self.patente)
        print(self.descripcion)

    def validarPatente(self):
        if(len(self.patente)==6 or len(self.patente)==8):
            return True
        return False

vehiculo_nuevo=Vehiculo("ABC12345","auto rojo")
print(vehiculo_nuevo.validarPatente())

#Parte 2
#Estadia : Vehiculo,hsEntrada,hsSalida

class Estadia:
    #Constructor de Entrada
    def __init__(self,vehiculo,hsEntrada,hsSalida):
        self.vehiculo=vehiculo
        self.hsEntrada=hsEntrada
        self.hsSalida=hsSalida
    
    def mostrar(self):
        print(self.hsEntrada)
        print(self.hsSalida)
        self.vehiculo.mostrar()

    def calcularTarifaTotal(self,tarifaPorHora):
        #Valido la patente con el metodo creado para el autito
        if(self.vehiculo.validarPatente()==False):
            return "Patente invalida"
        #Verifico no este presente ningun error de tiempos.
        elif(self.hsSalida-self.hsEntrada<=0):
            return "Error de tiempos"
        #Por ultimo, si todo esta ok, me devuelva el calculo
        else:
            return (tarifaPorHora*(self.hsSalida-self.hsEntrada))
            
    
nueva_estadia=Estadia(vehiculo_nuevo,6,8)
print('Estadia datos: ')
nueva_estadia.mostrar()
print(nueva_estadia.calcularTarifaTotal(5))




