a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    area = a * b * c
    print("A area do triangulo é: ", area)
else:
    print("Esses valores não formam um triangulo: ", a,", ",b,", ", c)
