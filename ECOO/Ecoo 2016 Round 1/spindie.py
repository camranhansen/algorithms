'''
Spindie.py
Start time:
03:46 AM
End time:
04:16 PM
essentially I go through every possible die roll and try to see if it works.
I probably will use the eval function? maybe. il see what happens
I think I remember doing this from last year.
but man this solution takes way too long.
il try and optimize this solution tommorow morning.
'''
fi = open("DATA/DATA21.txt")
for i in range(10):
	a = int(fi.readline())
	b = fi.readline().split(" ")
	b = map(int, b)
	c = fi.readline().split(" ")
	c[-1] = c[-1][0:len(c)-2]
	c = map(int, c)
	r = [""]*len(c)
	for j in b:
		for k in b:
			for l in b:
				if ((j+k)+l) in c:
					r[c.index((j+k)+l)] = "T"
				if ((j*k)+l) in c:
					r[c.index((j*k)+l)] = "T"
				if ((j*k)*l) in c:
					r[c.index((j*k)*l)] = "T"
				if ((j+k)*l) in c:
					r[c.index((j+k)*l)] = "T"
	for z in r:
		if z != "T":
			print "F",
		else:
			print z,

	print "\n"
fi.close()



