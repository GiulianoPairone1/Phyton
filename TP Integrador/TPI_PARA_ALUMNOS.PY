import sqlite3

class ProgramaPrincipal:            

    def menu(self): # se crea un menu, primero llama a programaprincipal
        while True:
            print("0- Salir") # se repite hasta que el usuario ponga 0
            print("1- Autos")
            print("2- Motocicletas") 
            nro= int(input("Por favor ingrese un número: "))
            if nro == 1: # si es 1, entra aca " auto "
                while True:
                    print("Menu de opciones Concesionaria")
                    print("5- Mostrar automoviles")
                    print("4- Cargar disponibilidad")
                    print("3- Borrar Automovil")
                    print("2- Modificar Automovil")
                    print("1- Cargar Automovil") 
                    print("0- Salir de menu")
                    nro = int(input("Por favor ingrese un número: "))
                    if nro == 1:
                        marca = input("Por favor ingrese la marca del automovil: ")
                        modelo = input("Por favor ingrese el modelo del automovil: ")
                        precio = input("Por favor ingrese el precio del automovil: ")
                        cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                        nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles) # se carga marca, modelo,precio,cantidaddispo
                        nuevo_automovil.cargar_automovil() # accedo a la clase carga automovil
                    if nro ==2:
                        marca = input("Por favor ingrese el nombre de la marca: ")
                        modelo = input("Por favor ingrese el nombre del modelo: ")
                        precio = input("Por favor ingrese el nuevo precio: ")
                        automovil_a_modificar=Automovil(marca,modelo,precio)
                        automovil_a_modificar.modificar_automovil()
                    if nro == 3:
                        marca = input("Por favor ingrese el nombre de la marca: ")
                        modelo = input("Por favor ingrese el nombre del modelo: ")
                        automovil_a_eliminar=Automovil(marca,modelo)
                        automovil_a_eliminar.eliminar_automovil()
                    if nro == 4:
                        marca = input("Por favor ingrese el nombre de la marca: ")
                        modelo = input("Por favor ingrese el nombre del modelo: ")
                        automovil_a_incrementar=Automovil(marca,modelo,cantidadDisponibles)
                        automovil_a_incrementar.incrementar_disponibilidad()
                    if nro == 5:
                        Automovil(marca, modelo).listar_automoviles()  
                    if nro==0:
                        break
            elif nro == 2: # si es 2 entra aca " moto "
                while True:
                    print("Menu de opciones Concesionaria")
                    print("7- Mostrar Motocicletas por fecha")
                    print("6- Aumentar 10% los precios")
                    print("5- Mostrar Motocicletas")
                    print("4- Cargar disponibilidad")
                    print("3- Borrar Motocicleta")
                    print("2- Modificar Motocicleta")
                    print("1- Cargar Motocicleta")
                    print("0- Salir de menu")
                    nro = int(input("Por favor ingrese un número: "))
                    if nro == 1:
                        modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                        marca = input("Por favor ingrese la marca de la motocicleta: ")
                        cilindrada = input("Por favor ingrese la cilindrada de la motocicleta: ")
                        precio = input("Por favor ingrese el precio de la motocicleta: ")
                        color = input("Por favor ingrese el color de la motocicleta: ")
                        cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                        # fechaUltimoPrecio = input("Por favor ingrese la fecha del ultimo precio: ")
                        nueva_motocicleta = Motocicleta(modelo,marca,cilindrada,precio,color,cantidadDisponibles)#,fechaUltimoPrecio)
                        nueva_motocicleta.cargar_motocicleta()
                    if nro ==2:
                        marca = input("Por favor ingrese el nombre de la marca: ")
                        modelo = input("Por favor ingrese el nombre del modelo: ")
                        precio = input("Por favor ingrese el nuevo precio: ")
                        motocicleta_a_modificar=Motocicleta(marca,modelo,precio)
                        motocicleta_a_modificar.modificar_motocicleta()
                    if nro == 3:
                        marca = input("Por favor ingrese el nombre de la marca: ")
                        modelo = input("Por favor ingrese el nombre del modelo: ")
                        motocicleta_a_eliminar=Motocicleta(marca,modelo)
                        motocicleta_a_eliminar.eliminar_motocicleta()
                    if nro == 4:
                        marca = input("Por favor ingrese el nombre de la marca: ")
                        modelo = input("Por favor ingrese el nombre del modelo: ")
                        motocicleta_a_incrementar=Motocicleta(marca,modelo,cantidadDisponibles)
                        motocicleta_a_incrementar.incrementar_disponibilidad()
                    if nro == 5:
                        Motocicleta(marca, modelo, cilindrada).listar_motocicletas()
                    if nro == 6:
                        Motocicleta(precio, marca, cilindrada).actualizar10_motocicleta()
                    if nro == 7:
                        Motocicleta(marca, modelo, cilindrada).listar_motocicletas_fecha()
                    if nro==0:
                        break  
            elif nro == 0:
                break    
            else:
                print("")

    
    def crearTablas(self): # crea la tabla
        conexion = Conexiones() # llama a conexiones
        conexion.abrirConexion() # Me crea el cursor y abrir conexion
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES") # Con el cursor voy a ejecutar el comando sql. Elimina la tabla si existe
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))") # Aca creo la tabla automoviles. El id automoviles va ser la llave primaria. un numero entero y se va ir incrementando cada vez que le sume datos. La marca va ser un string de 30/ variable char 30. Modelo lo mismo y el precio no puede estar vacio y es flotante y la cantidad disponible va ser entera no nulla. Marca/modelo unicos
        conexion.miConexion.commit() #hace un commit como el de git
        conexion.cerrarConexion() # Cerrar conexion

        conexion = Conexiones() # Lo mismo pero para motocicletas
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , modelo  VARCHAR(30), marca  VARCHAR(30), cilindrada  VARCHAR(30), precio INTEGER NOT NULL, color  VARCHAR(30), cantidadDisponibles INTEGER NOT NULL, fechaUltimoPrecio DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)")   
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def motocicletas_historico(self):
        conexion = Conexiones() 
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS_HISTORICO")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS_HISTORICO (id_moto INTEGER , modelo  VARCHAR(30), marca  VARCHAR(30), cilindrada  VARCHAR(30), precio INTEGER, color  VARCHAR(30), cantidadDisponibles INTEGER, fechaUltimoPrecio DATETIME)")
        conexion.miConexion.commit()     
        conexion.cerrarConexion()

class Automovil: # recibe los parametros que le pasamos (en automovil )
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self): # llamamos a la funcion
        conexion = Conexiones() # creo conexion " tabla base de dato "
        conexion.abrirConexion()
        print(self.cantidadDisponibles)
        try: #execute te permite escribir codigos sql (dentro de esa funcion) 
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles)) # Insertar en automoviles (es la tabla). Formateas y le pasas lo que declaraste en la clase marca,modelo 
            conexion.miConexion.commit()  #haces un commit como el de github
            print("Automovil cargado exitosamente")
        except: #Muestra los errores
            print("Error al agregar un automovil")
        finally: # Se cierra la conexion, lo hace siempre
            conexion.cerrarConexion()    
    
    
    def modificar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  

            
    def eliminar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}'".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil eliminado exitosamente")
        except:
            print("Error al eliminar un automovil")
        finally:
            conexion.cerrarConexion()


    def incrementar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        print(self.cantidadDisponibles)
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles+1 where marca= '{}' and modelo= '{}' ".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Automovil incrementado exitosamente")
        except:
            print("Error al incrementar un automovil")
        finally:
            conexion.cerrarConexion()    

    def listar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()
            # print(autos)
            print("----------------------------------")
            for auto in autos:
                print(f'ID: {auto[0]}\nMarca: {auto[1]}\nModelo: {auto[2]}\nPrecio: {auto[3]}\nCantidad Disponible: {auto[4]}')
                print("----------------------------------")
        except:
            print("Error al mostrar automoviles")
        finally:
            conexion.cerrarConexion()

class Motocicleta:
    def __init__(self,modelo,marca,cilindrada,precio=None,color=None,cantidadDisponibles=None):
        self.modelo = modelo
        self.marca = marca
        self.cilindrada = cilindrada
        self.precio=precio
        self.color = color
        self.cantidadDisponibles=cantidadDisponibles


        
    def cargar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(modelo,marca,cilindrada,precio,color,cantidadDisponibles) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(self.modelo,self.marca,self.cilindrada,self.precio,self.color,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
        except: #Muestra los errores
            print("Error al agregar una motocicleta") 
        finally: # Se cierra la conexion 
            conexion.cerrarConexion()    
    
    
    def modificar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Motocicleta modificado correctamente")
        except:
            print('Error al actualizar una motocicleta')
        finally:
            conexion.cerrarConexion()

    def actualizar10_motocicleta(self):
        try:
            programa.motocicletas_historico() # creo la tabla
            conexion = Conexiones()
            conexion.abrirConexion()
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS") # selecciono todo desde BD
            motocicletas = conexion.miCursor.fetchall() # lo extraido lo guardo en una variable
            for moto in motocicletas:   # recorro esa variable
                id, modelo, marca, cilindrada, precio, color, cantidadDisponibles, fecha = moto # destructuring de cada moto           
                conexion.miCursor.execute("INSERT INTO MOTOCICLETAS_HISTORICO(id_moto,modelo,marca,cilindrada,precio,color,cantidadDisponibles,fechaUltimoPrecio) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(id,modelo,marca,cilindrada,precio,color,cantidadDisponibles,fecha))
            conexion.miConexion.commit()
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio= precio*1.1, fechaUltimoPrecio=CURRENT_TIMESTAMP")
            conexion.miConexion.commit()
            print("Motocicletas actualizadas correctamente")
        except:
            print("Error al actualizar precios")
        finally:
            self.listar_motocicletas() # listar motos
            conexion.cerrarConexion()
            
            

            
    def eliminar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM MOTOCICLETAS where marca='{}' and modelo='{}'".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Motocicleta eliminado exitosamente")
        except:
            print("Error al eliminar una motocicleta")
        finally:
            conexion.cerrarConexion()


    def incrementar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET cantidadDisponibles= cantidadDisponibles+1 where marca= '{}' and modelo= '{}' ".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Motocicleta incrementada exitosamente")
        except:
            print("Error al incrementar una Motocicleta")
        finally:
            conexion.cerrarConexion()    

    def listar_motocicletas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motocicletas = conexion.miCursor.fetchall()
            print("----------------------------------")
            for moto in motocicletas:
                print(f'ID: {moto[0]}\nModelo: {moto[1]}\nMarca: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')
                print("----------------------------------")
        except:
            print("Error al mostrar motocicletas")
        finally:
            conexion.cerrarConexion()

    def listar_motocicletas_historico(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS_HISTORICO")
            motocicletas_historico = conexion.miCursor.fetchall()
            print("----------------------------------")
            for moto in motocicletas_historico:
                print(f'ID: {moto[0]}\nModelo: {moto[1]}\nMarca: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')
                print("----------------------------------")
        except:
            print("Error al mostrar motocicletas")
        finally:
            conexion.cerrarConexion()        

    def listar_motocicletas_fecha(self):
        conexion = Conexiones() # crea un objecto con la clase conexion
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS") # selecciono todo de motocicleta
            motocicletas = conexion.miCursor.fetchall() # creo una lista de motocicleta
            fecha = input("ingrese una fecha: ") # le pido al usuario una fecha
            print("----------------------------------")     
            for moto in motocicletas: # cada elemento va ser moto. recorro con un for. motocicleta seria la extraccion en forma de lista 
                print(f'ID: {moto[0]}\nModelo: {moto[1]}\nMarca: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')
                print("----------------------------------") # lo recorro para mostrar en una linea
                if moto[7] == fecha: # cuando la moto en posicion 7 sea la que yo llame se corta
                    break # se modifico y el for va arriba para que no te tire el elemento 7
                    
        except:
            print("Error al mostrar motocicletas")
        finally:
            conexion.cerrarConexion()        
        
    
class Conexiones: # crea conexiones
    
    def abrirConexion(self): # abre conexion
        self.miConexion = sqlite3.connect("Concesionaria") # sqlite3 se conecta a la base de datos concesionaria
        self.miCursor = self.miConexion.cursor() # se crea cursor. Acceso a datos que se que se puede utilizar para recorrer el conjunto de filas de una tabla o insertar nuevas filas en una tabla.
        
    def cerrarConexion(self): # Se cierra la conexion
        self.miConexion.close()


            
programa = ProgramaPrincipal() #1
programa.crearTablas() #2
programa.menu() #3