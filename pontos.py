import math

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))
numero4 = int(input("Informe o quarto número: "))

distAB = math.sqrt((numero1-numero2)**2 + ((numero3-numero4)**2))

if distAB >= 10:
    print("longe")
else:
    print("perto")