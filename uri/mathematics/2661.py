def primo_despojado(n):
    fatores = {}
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if fatores.get(i):
                fatores[i] += 1
            else:
                fatores[i] = 1
            n //= i
    if n > 1:
        if fatores.get(n):
            fatores[n] += 1
        else:
            fatores[n] = 1
    return fatores


n = int(input())
fatores = primo_despojado(n)
primos_distintos = len(fatores)
combinacoes = 2**primos_distintos - primos_distintos - 1
print(combinacoes)

# analise combinatoria resolvida com auxilio https://danielsaad.com/maratona/assets/22-maratona-de-programacao/editorial/despojados.pdf
