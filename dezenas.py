entrada = input("Digite um número inteiro: ")

numero = int(entrada)

parteInteira = numero // 10
ultimoNumero = parteInteira % 10

print("O dígito das dezenas é", ultimoNumero)