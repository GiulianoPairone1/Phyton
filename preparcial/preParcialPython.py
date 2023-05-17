
from ast import Try
from dataclasses import dataclass
from operator import truediv
from optparse import Option
from typing import List, Optional

def primeros_tres(lista) -> List:
    nueva=[]
    nueva=lista[:3]
    return nueva

lista = ["ho", 3.16, "la", 81, 6, 42]
listaNueva = primeros_tres(lista)
print(listaNueva)


# Definir una función concatena(string1, string2, nro) que reciba como 
# parámetro dos strings y un número y los devuelva concatenados. 

def concatena(string1, string2, nro) -> str:
    return string1 + " " + string2 + " " + str(nro)

stringConcatenado= concatena("Elias", "Gonzalez", 24)
print(stringConcatenado)

#Suponga que tiene que desarrollar un sistema para un estacionamiento.
# 1. Crear una clase llamada Vehiculo con atributos patente, y descripcion(opcional vacio por 
# defecto)
# Implementar los siguientes métodos:
# 1. Un constructor
# 2. mostrar(): muestra los datos del vehiculo
# 3. validarPatente(): Valida que la patente tenga 6 u 8 caracteres

class Vehiculo():
    def __init__(self, patente, descripcion: Optional[str]=None) -> None:
        self.patente=patente
        self.descripcion=descripcion

    def mostrar(self):
        return f'Vehiculo patente: {self.patente}, descripcion: {self.descripcion}'

    def validarPatente(self) -> bool:
        if len(self.patente) >= 6 and len(self.patente) <= 8:
            return True
        return False


objeto= Vehiculo("ASD123", "Auto")
print(objeto.mostrar())
print(objeto.validarPatente())


# 2. Crear una clase llamada Estadia con atributos Vehiculo, hora de entrada y salida.
# Implementar los siguientes métodos:
# 1. Un constructor
# 2. mostrar(): Debera mostrar TODOS los datos de la Estadia
# 3. calcularTarifaTotal(tarifaPorHora): Deberá retornar el valor de la tarifa total en pesos 
# teniendo encuenta la entrada y salida y la tarifa por hora. Si la patente es invalida o la entrada más
# reciente que la salida deberá informar un error.


class Estadia(Vehiculo):
    def __init__(self, patente, descripcion, hEntrada, hSalida) -> None:
        super().__init__(patente, descripcion)  
        self.hEntrada=hEntrada
        self.hSalida=hSalida   

    def mostrar(self):
        return f'El horario de entrada es {self.hEntrada} y el horario de salida es: {self.hSalida}'
    

    def calcularTarifaTotal(self, tarifaPorHora):
        self.tarifaPorHora=tarifaPorHora
        horarioTotal= (self.hSalida - self.hEntrada)
        tarifaTotal= (self.tarifaPorHora * horarioTotal)
        if super().validarPatente is False and self.hEntrada > self.hSalida:
            print("Error")       
        return tarifaTotal

objeto2= Estadia("ASD", "Auto", 2, 4)
print(objeto2.mostrar())
print(objeto2.calcularTarifaTotal(250))



        