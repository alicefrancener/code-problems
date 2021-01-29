"""
  author: Alice Francener
  problem: 2959 - StopAll
  description: https://www.urionlinejudge.com.br/judge/en/problems/view/2959
  obs: Union find (baseado em https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d)
"""

""" Problema: A partir de um bairro eh possivel chegar a outro? """

# Union find
def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]
def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj

'''
input:
  1. numero de bairros (nodes)
  2. numero de conexoes (edges)
  3. numero de perguntas (conectado ou nao?)
'''

entrada = input().split()
n_nodes = int(entrada[0])
n_edges = int(entrada[1])
n_perguntas = int (entrada[2]) 
data = list( range(0,n_nodes+1))

# union
for edge in range(n_edges):
  edges = input().split()
  union(data, int(edges[0]), int(edges[1]))
  
# find
for pergunta in range(n_perguntas):
  bairro = input().split()
  set1 = find(data, int(bairro[0]))
  set2 = find(data, int(bairro[1]))
  if set1 == set2:
    print("Lets que lets")
  else:
    print("Deu ruim")