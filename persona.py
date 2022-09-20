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