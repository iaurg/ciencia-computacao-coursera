n = int(input("Digite um numero positivo inteiro:"))


def fatorial(numero):
    fat = 1
    while numero > 1:
        fat = fat * numero
        numero = numero - 1
    return fat


while n >= 0:
    print(fatorial(n))
    n = int(input("Digite um numero positivo inteiro:"))
