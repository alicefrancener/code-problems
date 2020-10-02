"""
  problem: Pascal's Triangle
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/2232
"""

casos = int(input())

for i in range(casos):
    linhas = int(input())
    soma = 0
    for j in range(0, linhas):
        soma += 2**j
    print(soma)
