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


while True:
    try:
        primo = int(input())
        if isPrime(primo):
            primo = str(primo)
            flag_primo = True
            for dig in primo:
                if not isPrime(int(dig)):
                    flag_primo = False
                    break
            print('Super') if flag_primo else print('Primo')
        else:
            print('Nada')
    except EOFError:
        break
