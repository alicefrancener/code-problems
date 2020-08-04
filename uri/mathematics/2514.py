def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return int(a * (b / gcd(a, b)))


while True:
    try:
        last_year = int(input())
        a, b, c = map(int, input().split())
        resu_lcm = lcm(a, lcm(b, c))
        print(resu_lcm - last_year)
    except EOFError:
        break
