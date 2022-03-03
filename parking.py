from datetime import datetime
from sqlalchemy import false, true

hoy = datetime.now()

def ticketEntrada(parking):
    coche = {}
    matricula = input("Introduce matricula: ")
    hora = int(input("Hora de entrada: "))
    min = int(input("Minuto de entrada: "))
    horaEntrada = datetime(hoy.year, hoy.month, hoy.day, hora, min, 00, 0000)
    estado = true

    #añadimos los campos del vehiculo
    coche['matricula'] = matricula
    coche['hora_entrada'] = horaEntrada
    coche['estado'] = estado

    parking.append(coche)
    print("Ticket abierto adecuadamente.")

def ticketSalida(parking):
    ticket = {}
    matricula = input("Introduce matricula: ")

    #recorremos la lista donde estan los coches
    for coche in parking:
        #recorremos el dicc
        for clave, valor in coche.items():
            if matricula == valor:
                ticket = coche
    
    if ticket:
        hora = int(input("Hora de salida: "))
        min = int(input("Minuto de salida: "))
        horaSalida = datetime(hoy.year, hoy.month, hoy.day, hora, min, 00, 0000)
        ticket['estado'] = false

        #calculamos el precio del parking por horas
        tiempoE = int(horaSalida.hour) - int(ticket['hora_entrada'].hour)
        if horaSalida.min < ticket['hora_entrada'].min:
            tiempoE -= 1

        tarifa = tiempoE * 3.5

        ticket['tarifa'] = tarifa
        print("Ticket cerrado adecuadamente.")

    else:
        print("El coche a buscar no se encuentra en el parking")


def cochesEnParking(parking):
    contCochesParking = 0
    #recorremos la lista donde estan los coches
    for coche in parking:
        #recorremos el dicc
        for clave, valor in coche.items():
            if coche[clave] == true:
                contCochesParking += 1
    
    print(f"Dentro del parking se encuentran {contCochesParking} coches en este momento.")


def cochesFueraParking(parking):
    contCochesF = 0
    contDinero = 0
    #recorremos la lista donde estan los coches
    for coche in parking:
        #recorremos el dicc
        for clave, valor in coche.items():
            if valor == false:
                contCochesF += 1
            if clave == "tarifa" and coche['estado'] == false:
                contDinero += coche[clave]
    
    print(f"Han salido del parking {contCochesF} coches registrados.")
    print(f"Se ha recaudado {contDinero} dinero.")

parking = []
opcion = 0
while opcion != 5:

    print("1.- Crear ticket")
    print("2.- Cerrar ticket")
    print("3.- Coches en parking")
    print("4.- Coches fuera del parking")
    print("5.- Salir")
    
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        print()
        ticketEntrada(parking)
    elif opcion == 2:
        print()
        ticketSalida(parking)
    elif opcion == 3:
        print()
        cochesEnParking(parking)
    elif opcion == 4:
        print()
        cochesFueraParking(parking)
    elif opcion == 5:
        print("Programa cerrado")
    
    print()