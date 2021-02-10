"""
  problem: 1018 - Banknotes
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1018
"""

valor = int(input())
notas = [100,50,20,10,5,2,1]
resto = valor

print(valor)
for n in notas:
    qtd = resto // n
    resto = resto % n
    print('{:d} nota(s) de R$ {:d},00'.format(qtd, n))
