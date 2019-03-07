largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))

while altura > 0:
    larguraLimite = largura
    while larguraLimite > 0:
        print("#", end="")
        larguraLimite = larguraLimite - 1
    print()
    altura = altura - 1
