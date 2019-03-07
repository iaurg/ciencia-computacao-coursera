linha = int(input("Quantas linhas contém a bandeira?"))
coluna = int(input("Quantas colunas contém a bandeira?"))
posicaoEstrelaV = int(input("Qual linha deve estar a estrela?"))
posicaoEstrelaH = int(input("Qual coluna deve estar a estrela?"))
linhaLimite = 1
colunaLimite = 1
while linhaLimite <= linha:
    colunaLimite = 1
    while colunaLimite <= 5:
        if colunaLimite == posicaoEstrelaH and linhaLimite == posicaoEstrelaV:
            print("*", end="\t")
        else:
            print("-", end="\t")
        colunaLimite = colunaLimite + 1
    print()
    linhaLimite = linhaLimite + 1
