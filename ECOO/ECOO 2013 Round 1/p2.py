fi = open("DATA/DATA20.txt")
for i in range(1):
	z = fi.readline().strip().split(" ")
	# for a in z:
	s = 0
	a = ["42395"]
	for k in range(0,len(a),2):
		# s += int(str(int(a[k])*2)[0]) + int(str(int(a[k])*2)[1])
		# print k
		for q in str(int(a[k])*2):
			print q
			s += int(q)
			# print s
		# print "doing it again"	
		# print str(int(a[k])*2)[0] + str(int(a[k])*2)[1]
		# print s

	print "doing it again"



fi.close()