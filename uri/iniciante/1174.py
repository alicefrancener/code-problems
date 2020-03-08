vetor = []
lista_menores = ''

for i in range(0, 100):
  num = float(input())
  vetor.append(num)
  if vetor[i] <= 10.0:
    lista_menores += 'A[{}] = {:.1f}'.format(i, vetor[i])
    if i < 99:
      lista_menores += '\n'

print(lista_menores)