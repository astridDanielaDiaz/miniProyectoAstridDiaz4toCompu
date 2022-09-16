def crearContacto():
    print("creando contacto")

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
            crearContacto()
    

#Iniciar programa
main()
