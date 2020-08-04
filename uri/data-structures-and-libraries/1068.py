while True:
    correto = True
    try:
        expressao = input()
        parenteses_aberto = []
        for e in expressao:
          if e == '(':
            parenteses_aberto.append(e)
          if e == ')':
            if len(parenteses_aberto) > 0:
              parenteses_aberto.pop()
            else:
              correto = False
              break
        if correto and len(parenteses_aberto) == 0:
          print('correct')
        else:
          print('incorrect')
    except EOFError:
        break
