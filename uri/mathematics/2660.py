def lcm(a, b):
    return (a/gcd(a, b))*b


def gcd(a, b):
    if b == 0:
        return a
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b


n, limite = map(int, input().split())
ciclos_vida = list(map(int, input().split()))

# encontrar o maximo multiplo comum (mmc) entre populacoes existentes
lcm_resu = 1
for c in ciclos_vida:
    lcm_resu = lcm(lcm_resu, c)

# encontrar o maior mmc da nova populacao que seja menor que o limite
gcd_max = 1
ciclo_max = 1
for i in range(0, limite + 1):
    gcd_tmp = lcm(lcm_resu, i)
    if gcd_tmp > gcd_max and gcd_tmp <= limite:
        gcd_max = gcd_tmp
        ciclo_max = i

print(ciclo_max)
