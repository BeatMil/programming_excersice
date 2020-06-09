box1 = [1,2,3]
box2 = ['a','b','c']
box3 = []
for i in range(len(box1)):
	box3.append(box1[i])
	for j in range(len(box2)):
		if i == j:
			box3.append(box2[j])

print(box3)


