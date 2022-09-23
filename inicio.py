from persona import persona
misContactos = [persona(412,'Carlos', 'casa 1'), persona(542,'Sara', 'casa 2')]


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

def mostrarContactos():
    if len(misContactos) == 0:
        print("La lista esta vacia, no hay contactos que buscar...")
    else:
        for i in range(len(misContactos)):
            print('Nombre:', misContactos[i].verNombre(),'Direccion', misContactos[i].verDireccion(), 'Numero', misContactos[i].verNumero()) 

def modificarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar")
    else:
        encontrado = False
        posicion = None
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
               posicion = i
               encontrado = True
               break
            else:
                encontrado = False
        if encontrado == False:
            nuevoNumero = int(input("Ingrese el nuevo numero:"))
            nuevoNombre = int(input("Ingrese el nuevo nombre:"))
            nuevoDireccion = int(input("Ingrese la nueva direccion:"))
            misContactos[posicion]. modificarNumero(nuevoNumero)
            misContactos[posicion]. modificarNombre(nuevoNombre)
            misContactos[posicion]. modificarDireccion(nuevoDireccion)
            print("Datos actualizados con éxito...")
        else:
            print("Dato no encontrado...")

def  eliminarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar")
    else:
        encontrado = False
        posicion = None
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
               posicion = i
               encontrado = True
               break
            else:
                encontrado = False
        if encontrado == False:
           misContactos[posicion].pop(posicion)
           print("Datos eliminados con éxito...")
        else:
            print("Dato no encontrado...")

def crearReporte():
    print("Creando reporte HTML")





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
        elif op == 3:
            mostrarContactos()
        elif op == 4:
            nombre = input("Ingrese el nombre del contacto:")
            modificarContacto(nombre)
        elif op == 5: 
            nombre = input("Ingrese el nombre del contacto:")
            eliminarContacto(nombre)
        elif op == 6:
            crearReporte()
        elif op == 7:
            print("programa finalisado...")
        else:
            print("Opcion incorrecta...")
    

#Iniciar programa
main()
