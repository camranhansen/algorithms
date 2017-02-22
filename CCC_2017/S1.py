l1 = raw_input()
l2 = raw_input().split(" ")
l3 = raw_input().split(" ")
sf = 0
se = 0
last = 0
for i in range(int(l1)):
	sf += int(l2[i])
	se += int(l3[i])
	if se == sf:
		last = i+1
print str(last)

#memory leaks LUL