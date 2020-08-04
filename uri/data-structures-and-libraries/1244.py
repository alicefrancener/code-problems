for i in range(int(input())):
    conjunto_strings = input().split()
    conjunto_strings.sort(reverse=True, key=len)
    print(*conjunto_strings)