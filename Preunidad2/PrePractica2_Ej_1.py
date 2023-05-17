#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
print("Ingrese 2 numero")
a=int(input())
b=int(input())
if a < b:
    resultado=b
else:
    resultado=a
# resultado=max(a,b)
print(resultado)

#FIN