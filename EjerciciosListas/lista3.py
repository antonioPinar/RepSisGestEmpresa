
usuarios = []

def menu():
    print("1. Añadir usuario")
    print("2. Mostrar usuarios")
    print("3. Modificar usuario")
    print("4. Borrar usuario")
    print("5. Mostrar fecha")
    print("0. Salir")

def aniadirU():
    encontrado = False
    id = input("introduce id:")

    for i in range(len(usuarios)):
        if usuarios[i][0] == id:
            print("id ya usado")
            encontrado = True
    
    if encontrado == False:
        dia = int(input("Introduce dia:"))
        mes = int(input("Introduce mes:"))
        anio = int(input("Introduce año:"))
        rol = input("Elige rol de usuario [usuario, usuario avanzado, admin]:")

        usuarios.append([id, [dia, mes, anio], rol])

    input("Pulsa cualquier tecla para continuar\n")

def mostrarU():
    for usuario in usuarios:
        print(usuario)

    input("Pulsa cualquier tecla para continuar\n")

def modifU():
    id = input("Introduce el id que deseas modificar:")

    for usuario in usuarios:
        if usuario[0] == id:
            print("Ha elegido modificar el usuario :",id)
            print("1. Modificar fecha")
            print("2. Modificar rol")

            resp = int(input("¿Que campo desea modificar? [1/2]:"))

            if resp == 1:
                dia = int(input("Introduce dia:"))
                mes = int(input("Introduce mes:"))
                anio = int(input("Introduce año:"))

                usuario[1][0] = dia
                usuario[1][1] = mes
                usuario[1][2] = anio

                print("Fecha nueva:",usuario[1])

            elif resp == 2:
                rol = input("Introduce el rol: ")
                usuario[2] = rol
                print("Rol nuevo:",usuario[2])

            print("USUARIO MODIFICADO CON EXITO")

        else:
            print("Usuario introducido no encontrado")

    input("Pulsa cualquier tecla para continuar\n")

def borrarU():
    id = input("Introduce el id del usuario que deseas borrar:")

    for usuario in usuarios:
        if usuario[0] == id:

            usuarios.remove(usuario)
        
            print("USUARIO BORRADO CON EXITO")

        else:
            print("Usuario no encontrado en la lista")

    input("Pulsa cualquier tecla para continuar\n")

def mostrarFechas():
    for usuario in usuarios:
        print(usuario[1])

    input("Pulsa cualquier tecla para continuar\n")

while True:
    menu()

    resp = int(input())

    if resp == 1:
        aniadirU()
    elif resp == 2:
        mostrarU()
    elif resp == 3:
        modifU()
    elif resp == 4:
        borrarU()
    elif resp == 5:
        mostrarFechas()
    elif resp == 0:
        print("Proceso cerrado")
        break