#Definir una función listaPares  que reciba una lista con numeros y devuelva  una lista con los números pares. (2,5 puntos)
def listapares(listnumeros):
    listapares=[]
    for i in listnumeros:
        if(i %2  == 0):
            listapares.append(i)
    return listapares

lista=[1,2,3,4,5,6,7,8,9,]
print(listapares(lista))