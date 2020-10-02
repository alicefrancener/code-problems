"""
  problem: Travel to Mars in Primo Speed
  https://www.urionlinejudge.com.br/judge/en/problems/view/2180
"""

def isPrime(n):
    if ((n < 2) or ((n > 2) and (n % 2 == 0))):
        return False
    i = 3
    while i * i <= n:
        if isPrime(i):
            if(n % i == 0):
                return False
        i = i + 2
    return True

peso = int(input())

primos = []
n_teste = peso
while len(primos) < 10:
    if isPrime(n_teste):
        primos.append(n_teste)
    n_teste = n_teste + 1

velocidade = sum(primos)
horas = int(60000000/velocidade)
dias = int(horas/24)

print('{:d} km/h'.format(velocidade))
print('{:d} h / {:d} d'.format(horas, dias))
