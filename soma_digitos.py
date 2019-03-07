numero = int(input("Digite um numero: "))

multi = 0

while numero and numero > 0:
    mat = numero % 10
    numero = numero // 10
    multi = multi + mat
print(multi)