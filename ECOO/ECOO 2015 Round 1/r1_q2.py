#wordrap - question 2 from round 1 of ECOO 2015.
# I remember being at the competition, and being unable to solve this question. 
#I felt like I let down my team. This is take 2: A chance at redemption.
#sample input
# l1  = int("11")
# l2 = "Catches Theives just like flies".split(" ")
def dothething(l1, l2):
	# print l2
	c = ""
	for z in l2:
		# print z
		# print "starting"
		if len(z) >= l1:
			# print "tphis path"
			if c != "":
				# print "here"
				print c
				c = ""
			for x in z:
				# print x
				# print "?"
				if len(c) == l1:
					print c
					c = ""
				c += x
		else:

			if len(c) + len(z) + 1 > l1:

				print c
				c = ""
			# print "yes"
			# print c
			if c == "":
				c += z
			else:
				c += " " + z
			# print c
	print c
	print "====="
	c = ""
	return
fin = open("data/DATA21.txt", "r")
for i in range(10):
	l1 =  int(fin.readline().rstrip())
	l2 = fin.readline().rstrip().split(" ")
	# l1 = int(fin.readline())
	# l2 = fin.readline().split(" ")
	dothething(l1, l2)

fin.close()
