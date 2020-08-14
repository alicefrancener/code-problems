"""
  author: Alice Francener
  problem: The Dark Elf
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1766
"""


class Rena:
    def __init__(self, nome, peso, idade, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura


casos_teste = int(input())

for i in range(casos_teste):
    n_total, n_treno = map(int, input().split())
    renas = []

    for j in range(n_total):
        nome, peso, idade, altura = input().split()
        renas.append(Rena(nome, int(peso), int(idade), float(altura)))

    renas = sorted(renas, key=lambda rena: rena.nome)
    renas = sorted(renas, key=lambda rena: rena.altura)
    renas = sorted(renas, key=lambda rena: rena.idade)
    renas = sorted(renas, key=lambda rena: rena.peso, reverse=True)

    print('CENARIO {', i+1, '}', sep='')
    for j in range(n_treno):
        print('{} - {}'.format(j+1, renas[j].nome))
