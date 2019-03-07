largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
guardaLargura = largura
guardaAltura = altura
while altura > 0:
    larguraLimite = largura
    while larguraLimite > 0:
        if larguraLimite == 1 or larguraLimite == guardaLargura:
            print("#", end="")
        elif altura == 1 or altura == guardaAltura:
            print("#", end="")
        else:
            print(" ", end="")
        larguraLimite = larguraLimite - 1
    print()
    altura = altura - 1
