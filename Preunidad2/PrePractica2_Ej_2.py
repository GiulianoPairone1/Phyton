#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

lista=[]
listaImpar=[]
while True:
    print("Ingrese un numero distinto de 0")
    numero=int(input())
    if numero != 0:
        lista.append(numero)
        if numero%2 != 0:
            listaImpar.append(numero)
    else:
        break
print("Lista Original"+ str(lista))
print("Lista Impar"+ str(listaImpar))

#FIN