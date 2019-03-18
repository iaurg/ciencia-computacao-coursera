import re


def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    return frase.split()


def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    sab = 0

    for i in range(0, 6):
        valor = as_a[i] - as_b[i]

        if (valor < 0):
            valor *= -1

        sab += valor

    return sab / 6
    pass


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentenca = separa_sentencas(texto)

    frases = []
    contaCaracterSentenca = []

    for item in sentenca:
        frases += separa_frases(item)
        contaCaracterSentenca.append(len(item))

    resultadoCaracterSentenca = sum(contaCaracterSentenca)

    palavras = []
    contaCaracterFrase = []
    for frase in frases:
        palavras += separa_palavras(frase)
        contaCaracterFrase.append(len(frase))
    resultadoCaracterFrases = sum(contaCaracterFrase)
    tamanhoMedioPalavra = soma_tamanho_palavras(palavras) / len(palavras)
    typeToken = n_palavras_diferentes(palavras) / len(palavras)
    razaoHapax = n_palavras_unicas(palavras) / len(palavras)
    tamanhoMedioSentenca = resultadoCaracterSentenca / len(sentenca)
    complexidadeSentenca = len(frases) / len(sentenca)
    tamanhoMedioFrase = resultadoCaracterFrases / len(frases)

    lista = [tamanhoMedioPalavra, typeToken, razaoHapax,
             tamanhoMedioSentenca, complexidadeSentenca, tamanhoMedioFrase]
    return lista
    pass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    grauSimilaridade = 1000.0
    numTexto = -1

    for i in range(0, len(assinaturas)):

        similaridade = compara_assinatura(ass_cp, assinaturas[i])

        if (similaridade < grauSimilaridade):
            grauSimilaridade = similaridade
            numTexto = i + 1

    return numTexto
    pass


def soma_tamanho_palavras(lista):
    soma = 0
    for item in lista:
        soma = soma + len(item)
    return soma


def main():

    ass = le_assinatura()

    textos = le_textos()

    numSimilar = avalia_textos(textos, ass)

    print("O autor do texto {} esta infectado com COH-PIAH".format(numSimilar))


main()
