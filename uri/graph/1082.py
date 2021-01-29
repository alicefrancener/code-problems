"""
  author: Alice Francener
  problem: 1082 - Connected Components
  description: https://www.urionlinejudge.com.br/judge/en/problems/view/1082
"""

'''Problema: quantos grafos conexos existem'''

class DisjointSets:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = []
        for i in range(0, n):
            self.parent.append(i)

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
        if self.rank[x] == self.rank[y]:
            self.rank[y] = self.rank[y] + 1

'''input: 1. numero de casos, 2. numero de nos & numero de arestas, 3. arestas'''
n_casos = int(input())
for caso in range(n_casos):
    entrada = input().split()
    n_nodes = int(entrada[0])
    n_edges = int(entrada[1])
    alfabeto = DisjointSets(n_nodes)

    for e in range(n_edges):
        edge = input().split()
        alfabeto.union(ord(edge[0])-97, ord(edge[1])-97)
    
    for i in range(0, n_nodes):
        alfabeto.find(i)
    
    print("Case #{}:".format(caso+1))
    connected = 0
    for i in range(0, len(alfabeto.parent)):
        graph = ''
        if alfabeto.parent[i] != -1:
            graph = graph + chr(i+97) + ','
            for j in range(i+1, len(alfabeto.parent)):
                if alfabeto.parent[i] == alfabeto.parent[j]:
                    graph = graph + chr(j+97) + ','
                    alfabeto.parent[j] = -1
        if len(graph):
            print(graph)
            connected = connected + 1
    print('{} connected components\n'.format(connected))