for i in range(int(input())):
  diamantes = input()
  diamantes_menor = []
  extraidos = 0
  for d in diamantes:
    if d == '<': diamantes_menor.append(d)
    if d == '>' and len(diamantes_menor) > 0: 
      diamantes_menor.pop()
      extraidos += 1
  print(extraidos)
