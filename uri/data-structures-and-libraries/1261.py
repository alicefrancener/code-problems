n = list(map(int, input().split()))
dicio = {}

for i in range(n[0]):
    item = input().split()
    dicio[item[0]] = int(item[1])

salario = 0
while n[1] > 0:
  descricao = input().split()
  if descricao[0] == '.':
    print(salario)
    salario = 0
    n[1] -= 1
  for d in descricao: 
    salario += dicio.get(d, 0)