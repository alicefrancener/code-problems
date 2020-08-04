while True:
    try:
        digitacao = input().split('[')
    except EOFError:
        break
    beiju = []
    for h in digitacao:
      h = h.split(']')
      beiju.insert(0, h[0])
      for e in h[1:]:
        beiju.append(e)
    print(''.join(beiju))

'''
  # time limit exceeded
  texto = []
  indice = 0
  append = True
  for d in digitacao:
    if d == '[':
      append = False
      indice = 0
    elif d == ']':
      append = True
    elif append:
      texto.append(d)
    else:
      texto.insert(indice, d)
      indice += 1
  print(''.join(texto))
'''
