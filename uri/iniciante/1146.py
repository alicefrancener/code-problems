max = int(input())
string_valores = ''

while max != 0 and max > 0:
    for i in range(1, max):
        string_valores += str(i) + ' '
    string_valores += str(max)
    max = int(input())
    if max != 0:
      string_valores += '\n'

print(string_valores)
