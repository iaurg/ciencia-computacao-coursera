numero = int(input("Digite um número para fatorizar: "))
fat = 1
x = 1
while x <= numero:
    fat *= x
    x += 1
print(fat)