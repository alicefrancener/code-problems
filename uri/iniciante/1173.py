num = int(input())
if num > 50:
  exit()

vetor = []
vetor.append(num)
for i in range(0, 10):
  if i == 0:
    valor = vetor[i]
  else:
    valor = vetor[i-1] * 2
    vetor.append(valor)
  print('N[' + str(i) + '] = ' + str(valor))