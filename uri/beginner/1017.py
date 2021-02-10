"""
  problem: 1017 - Fuel Spent
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1017
"""

tempo = int(input())
velocidade = int(input())
distancia = tempo*velocidade
litros = distancia/12

print('{:.3f}'.format(litros))
