numero = 1
lista = []
while numero > 0:
    numero = int(input("Digite um numero:"))
    if numero != 0:
        lista.append(numero)
lista.reverse()
for item in lista:
    print(item)
