a = float(input("Introduce primer cateto: "))
b = float(input("Introduce segundo cateto: "))
c = float(input("Introduce la hipotenusa: "))
print()

if c**2 == (a**2 + b**2):
    print("Es un triangulo rectangulo")
elif c == a or c == b or b == a:
    print("Es un triangulo isosceles")
elif c == a and c == b and b == a:
    print("Es un triangulo equilatero")
else:
    print("Es un triangulo escaleno")
