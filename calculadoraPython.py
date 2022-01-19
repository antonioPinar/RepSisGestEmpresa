
valor1 = int(input("Introduce primer entero: "))
valor2 = int(input("Introduce segundo entero: "))

v1 = float(input("Introduce primer float: "))
v2 = float(input("Introduce segundo float: "))

cadena1 = str(valor1)
cadena2 = str(valor2)

resp = input("¿Que operacion quieres realizar? ")

if resp == "suma":
    print("Suma valores enteros ",valor1 ,"y",valor2,"=", valor1+valor2)
    print("Suma valores flotantes ",v1 ,"y",v2,"=", v1+v2)
elif resp == "multiplicacion":
    print("Multiplicacion valores enteros ",valor1 ,"y",valor2,"=", valor1*valor2)
    print("Multiplicacion valores flotantes ",v1 ,"y",v2,"=", v1*v2)
elif resp == "division":
    print("Division valores enteros ",valor1 ,"y",valor2,"=", valor1/valor2)
    print("Division valores flotantes ",v1 ,"y",v2,"=", v1/v2)
elif resp == "resta":
    print("Resta valores enteros ",valor1 ,"y",valor2,"=", valor1-valor2)
    print("Resta valores flotantes ",v1 ,"y",v2,"=", v1-v2)
else:
    print("operacion introducida no valida")

print("Concatenacion de los valores: ", cadena1+cadena2)

