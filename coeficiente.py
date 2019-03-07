def fatorial(num):
    fat = 1
    while num > 1:
        fat *= num
        num -= 1
    return fat

def numBionominal(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

def testaBinomial():
    if numBionominal(5,2) == 10:
        print("Ta funcionando para 5,2")
    else: 
        print("Não funciona em 5,2")
    if numBionominal(7,4) == 35:
        print("Ta funcionando em 7,4")
    else:
        print("Não funciona em 7,4")
    if numBionominal(6,1) == 6:
        print("Funciona em 6,1")
    else:
        print("Não funciona 6,1")

testaBinomial()