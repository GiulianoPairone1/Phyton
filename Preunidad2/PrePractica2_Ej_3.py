#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
try:
    print("Ingrese dos numeros")
    a=int(input())    
    b=int(input())
    resultado=a/b
    print(resultado)
except ZeroDivisionError as exception:    
    print(f"Ha ocurrido un error | {exception}") 

#FIN