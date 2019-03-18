
def fibo():
    a, b = 0, 1
    while True:
        a, b = b, a+b 
        yield b

