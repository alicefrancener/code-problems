n_casos = int(input())

'''
# recursão
def fibonacci(number):
    if number == 1:
        return 1
    if number == 0:
        return 0
    return fibonacci(number - 1) + fibonacci(number - 2)
'''
# sem recursão
def fibonacci(n):
    if n == 0:
        return 0
    resultado, n_1, n_2 = 1, 1, 1
    for i in range(2, n):
        resultado = n_1 + n_2
        n_1 = n_2
        n_2 = resultado
    return resultado

for caso in range(n_casos):
    number = int(input())
    resultado = fibonacci(number)
    print('Fib({}) = {}'.format(number, resultado))
