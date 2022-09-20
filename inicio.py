from persona import persona
misContactos = []


def crearContacto(numero, nombre, direccion):
   misContactos.append(persona(numero, nombre, direccion))
   print("Contacto almacenado...")


def buscarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar")
    else:
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                print("El telefono es", misContactos[i].verNumero())
                print("La dirección es", misContactos[i].verDireccion())
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == False:
            print("Dato no existente...")

def main():
    op = 0
    while op != 7:
        print("-------Agenda Telefonica---------")
        print("1. Crear contacto")
        print("2. Buscar contacto")
        print("3. Ver contacto")
        print("4. Modificar contacto")
        print("5. Eliminar contacto")
        print("6. Crear reporte en HTML")
        print("7. Salir del programa\n")
        op = int(input("Ingrese el numero de opción"))
        if op== 1:
            numero = int(input("Ingrese el numero de telefonos"))
            nombre = int(input("Ingrese el nombre"))
            direccion = int(input("Ingrese la direccion"))
            crearContacto(numero,nombre, direccion )
        elif op == 2:
            nombre = input("Ingrese el nombre del contacto a buscar")
            buscarContacto(nombre)
        
    

#Iniciar programa
main()
