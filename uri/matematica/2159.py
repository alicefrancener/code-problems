import math

n = int(input())

minPrimos = n / math.log(n)
maxPrimos = 1.25506 * minPrimos
print('{:.1f} {:.1f}'.format(minPrimos, maxPrimos))
