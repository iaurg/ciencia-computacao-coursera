numero = int(input("Digite um numero: "))
adjacente = False
while numero:
    ultimoNumero = numero % 10
    numeroCortado = (numero // 10)
    if ultimoNumero == numeroCortado % 10:
        adjacente = True
    numero = numeroCortado
if adjacente == True:
    print("sim")
else:
    print("não")