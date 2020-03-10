n_suspeitos = int(input())
indice_suspeito = []
while n_suspeitos != 0:
    # ler suspeitos
    suspeitos = input()
    suspeitos = suspeitos.split(' ')
    suspeitos = [int(i) for i in suspeitos]
    suspeitos_ordem = suspeitos.copy()
    suspeitos_ordem.sort(reverse=True)
    indice_suspeito.append(suspeitos.index(suspeitos_ordem[1]))
    n_suspeitos = int(input())

for i in indice_suspeito:
    print(i + 1)
