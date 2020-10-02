"""
  problem: The Pythagorean Theorem
  https://www.urionlinejudge.com.br/judge/en/problems/view/1582
"""

def tripla_pitagorica(a, b, c):
    tripla = [a, b, c]
    tripla.sort()
    if (tripla[2]**2 == (tripla[1]**2 + tripla[0]**2)):
        return True
    return False


def gdc(a, b):
    if (b == 0):
        return a
    return gdc(b, a % b)


while True:
    try:
        a, b, c = map(int, input().split())
        resu_tripla = tripla_pitagorica(a, b, c)
        resu_gdc = gdc(a, gdc(b, c))
        if resu_tripla:
            if resu_gdc == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')
    except EOFError:
        break
