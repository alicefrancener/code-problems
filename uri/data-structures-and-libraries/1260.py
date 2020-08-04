n = int(input())
input()
for i in range(n):
    tree_list = {}
    while True:
      try:
        tree = input()
        if tree == '':
            break
        if tree in tree_list.keys():
          tree_list[tree] += 1
        else:
          tree_list[tree] = 1
      except:
        break
    total = sum(tree_list.values())
    keys_sorted = sorted(tree_list.keys())
    if i > 0: print()
    for key in keys_sorted:
      print('{} {:.4f}'.format(key, tree_list[key]/total*100))