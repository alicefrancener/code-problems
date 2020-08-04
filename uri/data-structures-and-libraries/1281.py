for n in range(int(input())):
    produtos = []
    conta = 0
    for p in range(int(input())):
        produtos.append(input().split(' '))
    for i in range(int(input())):
        item = input().split(' ')
        conta += sum([(float(produ[1])*int(item[1]))
                      for produ in produtos if produ[0] == item[0]])
    print('R$ {:.2f}'.format(conta))
