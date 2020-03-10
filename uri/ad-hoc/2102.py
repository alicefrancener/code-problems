n_casos = int(input())
matriz_final = []
for caso in range(n_casos):
  dados_matriz = input()
  dados_matriz = dados_matriz.split(' ')
  dim_matriz = int(dados_matriz[0])
  n_matriz = int(dados_matriz[1])
  matriz = []
  for linha in range(n_matriz):
    coordenadas = input() #pk, lk, ck e vk
    coordenadas = coordenadas.split(' ')
    if linha == 0:
      matriz.append([coordenadas[1] + ' ' + coordenadas[2], int(coordenadas[3])])
    else:
      appended = True
      for i in range(len(matriz)):
        if matriz[i][0] == coordenadas[1] + ' ' + coordenadas[2]:
          matriz[i][1] += int(coordenadas[3])
          appended = False
          break
      if appended:
        matriz.append([coordenadas[1] + ' ' + coordenadas[2], int(coordenadas[3])])
  matriz_final.append(matriz)

# formatar saida
n = 0
for matriz in matriz_final: 
  resu = []
  for vetor in matriz:
    resu.append(vetor[0] + ' ' + str(vetor[1]))
  resu.sort()
  for r in resu:
    print(r)
  n += 1
  if n < n_casos: print()
      
      
    