lista=["ESte","es","un","codigo","muy","bueno"]

def listaNueva(lista):
    nuevaLista=[]
    nuevaLista.append(lista[-1])
    nuevaLista.append(lista[5])
    nuevaLista.append(lista[1])
    return nuevaLista

print(listaNueva(lista))