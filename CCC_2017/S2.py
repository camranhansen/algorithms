l1 = int(raw_input())
l2 = raw_input()
l = l2.split(" ")
d = []
for item in l:
	d.append(int(item))
#terrible coding practice I know, but hwatever
if l1%2==0:
# print d
	d.sort()
	lo = d[0:(l1/2)]
	lo.reverse()
	# print lo
	high = d[(l1/2):l1]
	# print high

	for i in range(l1/2):
		print lo[i],
		print high[i],
else:
	d.sort()
	lo = d[0:((l1/2)+1)]
	lo.reverse()
	# print lo
	high = d[((l1/2)+1):l1]
	# print high
	for i in range(l1/2):
		print lo[i],
		print high[i],
	print lo[(l1/2)],