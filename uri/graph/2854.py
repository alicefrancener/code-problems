"""
  author: Alice Francener
  problem: 2854 - Family Tree
  description: https://www.urionlinejudge.com.br/judge/en/problems/view/2854
"""

# -*- coding: utf-8 -*-

'''Problema: quantas familias diferentes existem'''

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


entrada = input().split()
n_pessoas = int(entrada[0])
n_conecoes = int(entrada[1])

familias = DisjointSets(n_pessoas)
pessoas = []
for i in range(n_conecoes):
    conexao = input().split()
    if conexao[0] not in pessoas:
        pessoas.append(conexao[0])
    if conexao[2] not in pessoas:
        pessoas.append(conexao[2])
    ia = pessoas.index(conexao[0])
    ib = pessoas.index(conexao[2])
    familias.union(ia, ib)

for i in range(0, n_pessoas):
    familias.find(i)

print(len(set(familias.parent)))