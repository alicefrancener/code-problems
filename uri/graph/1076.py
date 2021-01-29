"""
  author: Alice Francener
  problem: 1076 - Design Labirints
  description: https://www.urionlinejudge.com.br/judge/en/problems/view/1076
"""

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


n_casos = int(input())

for i in range(n_casos):
    vertice_entrada = int(input())
    entrada = input().split()
    n_vertices = int(entrada[0])
    n_arestas = int(entrada[1])

    graph = {}
    visited = set()

    for i in range(n_arestas):
        arestas = input().split()
        if int(arestas[0]) in graph:
            if int(arestas[1]) not in graph[int(arestas[0])]:
                graph[int(arestas[0])].append(int(arestas[1]))
        else:
            graph[int(arestas[0])] = [int(arestas[1])]
        if int(arestas[1]) in graph:
            if int(arestas[0]) not in graph[int(arestas[1])]:
                graph[int(arestas[1])].append(int(arestas[0]))
        else:
            graph[int(arestas[1])] = [int(arestas[0])]
    dfs(visited, graph, vertice_entrada)
    print((len(visited)-1)*2)
