while True:
    try:
        pilha, fila, fila_p, contagem = [], [], [], [0, 0, 0]
        desconhecido = False
        for n in range(int(input())):
            comando = list(map(int, input().split()))
            if comando[0] == 1:  # inserir elemento
                pilha.append(comando[1])
                fila.append(comando[1])
                fila_p.append(comando[1])
            else:  # tirar elemento
              try:
                if comando[1] not in pilha and comando[1] not in fila and comando[1] not in fila_p:
                  desconhecido = True
                else:
                  if comando[1] == pilha.pop():
                      contagem[0] += 1  # stack
                  if comando[1] == fila.pop(0):
                      contagem[1] += 1  # queue
                  if comando[1] == fila_p.pop(fila_p.index(max(fila_p))):
                      contagem[2] += 1  # priority queue
              except: 
                desconhecido = True
        if sum([1 for elem in contagem if elem == 0]) == 3 or desconhecido:
            print('impossible')
        elif contagem[0] > contagem[1] and contagem[0] > contagem[2]:
            print('stack')
        elif contagem[1] > contagem[0] and contagem[1] > contagem[2]:
            print('queue')
        elif contagem[2] > contagem[0] and contagem[2] > contagem[1]:
            print('priority queue')
        else:
            print('not sure')
    except EOFError:
        break
