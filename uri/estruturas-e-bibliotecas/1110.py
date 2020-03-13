while True:
    cartas_descartadas = []
    n = int(input())
    if n == 0:
        break
    cartas = list(range(n, 0, -1))
    while len(cartas) > 1:
        cartas_descartadas.append(cartas.pop())
        cartas.insert(0, cartas.pop())
    print('Discarded cards:', str(cartas_descartadas)[1:-1])
    print('Remaining card:', cartas[0])
