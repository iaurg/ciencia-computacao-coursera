def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def test_maximo():
    assert maximo(1,2) == 2
    assert maximo(5,-3) == 5