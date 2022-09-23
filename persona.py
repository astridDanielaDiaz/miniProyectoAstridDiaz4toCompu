class persona():
    def __init__(self, numero, nombre, direccion):
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion
        
    #creaccion de GETTERS
    def verNumero(self):
        return self.numero
    
    #creaccion de GETTERS
    def verNombre(self):
        return self.nombre

    #creaccion de GETTERS
    def verDireccion(self):
        return self.direccion
    
    #Creacion de SETTERS
    def modificarNumero(self, nuevoNumero):
        self.numero = nuevoNumero

    #Creacion de SETTERS
    def modificarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    #Creacion de SETTERS
    def modificarDireccion(self, nuevoDireccion):
        self.direccion = nuevoDireccion