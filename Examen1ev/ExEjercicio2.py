import sys

if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    aniosVisiestos = []

    if sys.argv[1] > sys.argv[2]:
        anios = list(range(num1, num2 + 1, -1))

        for i in range(len(anios)):
            if anios[i] % 4 == 0 and anios[i] % 100 != 0:
                aniosVisiestos.append(anios[i])

            elif anios[i] % 400 == 0:
                aniosVisiestos.append(anios[i])
        print(aniosVisiestos)

    else:
        anios = list(range(num1, num2 + 1))
        
        for anio in anios:
            if anio % 4 == 0 and anio % 100 != 0:
                aniosVisiestos.append(anio)

            elif anio % 400 == 0:
                aniosVisiestos.append(anio)
        print(aniosVisiestos)
else:
    print("Numero de parametros no válido, sigue el elemplo :\n", sys.argv[0], "<parametro 1> <parametro 2>")