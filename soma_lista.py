lista = [1, 25, 4, 5, 5]


def soma_elementos(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma


print(soma_elementos(lista))
