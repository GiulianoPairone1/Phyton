#Definir una función parecidas(lista1,lista2) que reciba 2 listas y que retorne un booleano verdadero si al menos 2 elementos coinciden, caso contrario devolver False. (2,5 puntos)


from pickle import TRUE
import re


def parecidad(lista1,lista2):
    #inicializo contador en 0
    elementos_conciden=0
    #recoprro ambas listas
    for x in lista1:
        for y in lista2:
            #compara si se repiten y sumo 1
            if (x==y):
                #si es igual sumo
                elementos_conciden+=1
    #si hay mas de 2 concidencias , retorno true
    if(elementos_conciden>=2):
        return TRUE
    return False