def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        pecas = n % (m+1)
        if pecas > 0:
            return pecas
        return m


def usuario_escolhe_jogada(n, m):
    pecas_remove = int(input("Quantas peças você vai tirar?"))
    if pecas_remove <= m:
        return pecas_remove
    while pecas_remove > m:
        print("Oops! Jogada inválida! Tente de novo.")
        pecas_remove = int(input("Quantas peças você vai tirar?"))
    return pecas_remove


def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    vezDoComputador = False
    if n % (m + 1) == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
        vezDoComputador = True

    while n > 0:
        if vezDoComputador:
            pecaRemovida = computador_escolhe_jogada(n, m)
            vezDoComputador = False
            print("Computador tirou", pecaRemovida, "peças.")
        else:
            pecaRemovida = usuario_escolhe_jogada(n, m)
            vezDoComputador = True
            print("Voce tirou", pecaRemovida, "peças.")

        n = n - pecaRemovida
        print("Agora restam", n, "peças no tabuleiro.")

        if n == 0:
            if vezDoComputador:
                print("Você ganhou!")
                return 1
            else:
                print("Fim do jogo! O computador ganhou!")
                return 0


def campeonato():
    jogador = 0
    computador = 0
    rodada = 1
    while rodada <= 3:
        print()
        print('**** Rodada', rodada, '****')
        print()
        vencedor = partida()
        if vencedor == 1:
            jogador = jogador + 1
        else:
            computador = computador + 1
        rodada += 1

    print("Você", jogador, "X", "Computador", computador)


def bemVindo():
    print("")
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada \n2 - para jogar um campeonato")
    escolha = int(input("Qual você vai escolher?"))
    if escolha == 1:
        partida()
    else:
        print("Você escolheu Campeonato")
        campeonato()


bemVindo()
