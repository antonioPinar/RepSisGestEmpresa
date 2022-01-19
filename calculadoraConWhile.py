resp = "si"

while resp == "si":
    valor1 = int(input("Introduce primer entero: "))
    valor2 = int(input("Introduce segundo entero: "))

    respOpereacion = input("¿Que operacion quieres realizar? \n")
    print()

    if respOpereacion == "suma":
        print("Suma valores enteros ",valor1 ,"+",valor2,"=", valor1+valor2)
        print()
    elif respOpereacion == "multiplicacion":
        print("Multiplicacion valores enteros ",valor1 ,"x",valor2,"=", valor1*valor2)
        print()
    elif respOpereacion == "division":
        print("Division valores enteros ",valor1 ,"/",valor2,"=", valor1/valor2)
        print()
    elif respOpereacion == "resta":
        print("Resta valores enteros ",valor1 ,"-",valor2,"=", valor1-valor2)
        print()
    else:
        print("operacion introducida no valida")
        print()

    resp = input("¿Deseas realizar otra operacion? \n")

print("Calculadora cerrada")