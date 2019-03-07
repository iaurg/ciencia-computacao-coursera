n = int(input("Digite um numero positivo inteiro e descubra se é primo:"))


def primo(numero):
    i, cont = 1, 0

    while i <= numero:
        if (numero % i == 0):
            cont += 1
        i += 1

    if cont == 2:
        print('primo')
    else:
        print('não primo')


while n >= 0:
    primo(n)
    n = int(input("Digite um numero positivo inteiro e descubra se é primo:"))
