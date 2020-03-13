duracao_notas = {'W': 1, 'H': 1/2, 'Q': 1/4,
                 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}

while True:
    notas = input()
    if notas == '*':
        break
    compassos_corretos, compasso = 0, 0
    for nota in notas:
        if nota == '/':
            if compasso == 1:
                compassos_corretos += 1
            compasso = 0
        else:
            compasso += duracao_notas[nota]
    print(compassos_corretos)
