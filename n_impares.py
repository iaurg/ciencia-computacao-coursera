numero = int(input("Digite um valor: "))

naturais = 1

while naturais < numero * 2:
    if naturais % 2 != 0:
        print(naturais)
    naturais += 1