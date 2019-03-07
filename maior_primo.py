def maior_primo(n):
    count = 1
    while count <= n:
        if éPrimo(count):
            maior_primo = count    
        count += 1
    return maior_primo

def éPrimo(k):
    i,cont = 1,0
    while i <= k:
        if (k % i == 0):
            cont += 1
        i += 1
    if cont == 2:
        return True
    else:
        return False
                
print(maior_primo(7))