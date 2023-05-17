class Banda:
    def __init__(self,nombre,cantidadIntegrantes,estiloMusical,popularidad):
        self.nombre=nombre
        self.integrantes=cantidadIntegrantes
        self.estilo=estiloMusical
        self.popularidad=popularidad
    
    def mostrar(self):
        print(self.nombre)
        print(self.integrantes)
        print(self.estilo)
        print(self.popularidad)
        

    def validarPopularidad(self):
        if(self.popularidad>0 & self.popularidad<11):
            return True
        return False

ejemplo_banda=Banda("Marron5",5,"sin estilo",5)
print(ejemplo_banda.mostrar())
print(ejemplo_banda.validarPopularidad())