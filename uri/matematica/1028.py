n_casos = int(input())
mdc_result = []

for i in range(n_casos):
  pilhas_figuras = input()
  pilhas_figuras = pilhas_figuras.split(' ')
  pilhas_figuras[0] = int(pilhas_figuras[0])
  pilhas_figuras[1] = int(pilhas_figuras[1])

  # algoritmo de euclides para determinar mdc
  if pilhas_figuras[0] < pilhas_figuras[1]:
    divisor = pilhas_figuras[0]
    dividendo = pilhas_figuras[1]
  else:
    divisor = pilhas_figuras[1]
    dividendo = pilhas_figuras[0]

  quociente = dividendo//divisor
  resto = dividendo % divisor
  
  while resto != 0:
    dividendo = divisor
    divisor = resto
    resto = dividendo % divisor
  mdc_result.append(divisor)

for mdc in mdc_result:
  print(mdc)