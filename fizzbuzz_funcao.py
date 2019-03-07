def fizzbuzz(numero):
    resposta = "x"
    if numero % 3 == 0 and numero % 5 != 0:
        resposta = "Fizz"
    if numero % 5 == 0 and numero % 3 != 0:    
        resposta = "Buzz"
    if numero % 5 == 0 and numero % 3 == 0:
        resposta = "FizzBuzz"
    if numero % 5 != 0 and numero % 3 != 0:
        resposta = numero
    return resposta

def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(4) == 4
