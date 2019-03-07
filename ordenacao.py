numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

if numero1 < numero2 and numero2 < numero3:
    print("crescente")
else:
    print("não está em ordem crescente")