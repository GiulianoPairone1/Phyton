#Definir una función vocales(letra) que reciba una letra y devuelva un booleano verdadero si la misma es una vocal, caso contrario devolver un booleano falso. (2,5 puntos)

def vocales(letra):
    letra=letra.lower()
    vocales='aeiou'
    if(letra in vocales):
        return True
    return False



    