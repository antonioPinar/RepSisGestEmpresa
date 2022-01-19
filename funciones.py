#Funciones
def sumar(num, val):
    return num + val

def restar(num, val):
    return num - val

def multiplicar(num, val):
    return num * val

def dividir(num, val):
    return num / val

resp = "si"

while resp == "si":
    respOp = input("¿Que operacion quieres realizar? \n")
    print()

    valor1 = int(input("Introduce primer entero: "))
    valor2 = int(input("Introduce segundo entero: "))

    if respOp == "suma":
        print("Suma valores enteros ",valor1 ,"+",valor2,"=", sumar(valor1,valor2))
        print()
    elif respOp == "multiplicacion":
        print("Multiplicacion valores enteros ",valor1 ,"x",valor2,"=", multiplicar(valor1,valor2))
        print()
    elif respOp == "division":
        print("Division valores enteros ",valor1 ,"/",valor2,"=", dividir(valor1,valor2))
        print()
    elif respOp == "resta":
        print("Resta valores enteros ",valor1 ,"-",valor2,"=", restar(valor1,valor2))
        print()
    else:
        print("operacion introducida no valida")
        print()

    resp = input("¿Deseas realizar otra operacion? \n")

print("Calculadora cerrada")