lista = [7, 3, 33, 12, 3, 3, 3, 7, 12, 100]


def remove_repetidos(lista):
    ordena = sorted(lista)
    novaLista = []
    for item in ordena:
        if item not in novaLista:
            novaLista.append(item)
    return novaLista


print(remove_repetidos(lista))