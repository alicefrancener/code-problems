while True:
  try:
    n_phones = int(input())
  except EOFError:
    break
  economia = 0
  phones = []
  for i in range(n_phones):
    phones.append(input())
  phones.sort()
  for i in range(1, len(phones)):
    for j, k in zip(phones[i], phones[i - 1]):
      if j != k:
        break
      economia += 1
  print(economia)
