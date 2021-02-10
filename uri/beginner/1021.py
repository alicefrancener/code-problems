"""
  problem: 1021 - Banknotes and Coins
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1021
"""

# -*- coding: utf-8 -*-

cent, dec = map(int, input().split('.'))
inteiros = [100, 50, 20, 10, 5, 2, 1]
fracoes = [50, 25, 10, 5, 1]

print('NOTAS:')
for i in inteiros:
    qtd = cent // i
    cent = cent % i
    if (i > 1):
        print('{} nota(s) de R$ {}.00'.format(qtd, i))

print('MOEDAS:')
print('{} moeda(s) de R$ {}.00'.format(qtd, i))

for i in fracoes:
    qtd = dec // i
    dec = dec % i
    print('{} moeda(s) de R$ {:.2f}'.format(qtd, float(i / 100)))
