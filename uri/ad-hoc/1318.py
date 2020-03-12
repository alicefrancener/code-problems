convidados = input()
convidados = convidados.split(' ')
repetidos = []

while int(convidados[0]) != 0 and int(convidados[1]) != 0:
    bilhetes = input()
    bilhetes = bilhetes.split(' ')
    bilhetes.sort()
    repetidos.append(0)
    for i in range(len(bilhetes) - 1):
        if bilhetes[i] == bilhetes[i+1]:
            if i == 0:
                repetidos[len(repetidos) - 1] += 1
            elif  bilhetes[i -1] != bilhetes[i]:
                repetidos[len(repetidos) - 1] += 1
    convidados = input()
    convidados = convidados.split(' ')

for repetido in repetidos:
    print(repetido)
