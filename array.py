numero = 1
lista = []
while numero != 0:
    numero = int(input("Digite um numero inteiro: "))
    lista.append(numero)

tam = len(lista) - 1
invert = []
while tam >= 0:
    invert.append(lista[tam])
    tam = tam - 1
print(invert)
