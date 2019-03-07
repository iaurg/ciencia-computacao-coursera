# Verificador de numero primo
i,cont = 1,0

n = int(input('Digite o numero: '))

while i <= n:
    if (n % i == 0):
        cont += 1
    i += 1

if cont == 2:
    print('primo')
else:
    print('não primo')