n = float(input())

if (n < 0 or n > 100):
    print('Fora de intervalo')
else:
    for i in range(25,101,25):
        if n <= i:
            if (i == 25):
                print('Intervalo [{},{}]'.format(i-25, i))
            else:
                print('Intervalo ({},{}]'.format(i-25, i))
            break
