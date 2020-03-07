swingArray = []
for i in range(20):
  num = int(input())
  swingArray.append(num)

for i in range(10):
	tmp = swingArray[i]
	swingArray[i] = swingArray[19-i]
	swingArray[19-i] = tmp

for i in range(20):
	print('N[' + str(i) + '] = ' + str(swingArray[i]))