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
I mean it works
but like 
it's not effecient whatsoever.
wait, I just checked the input file. there are 5000 numbers on the spinner. LMAo
hmm I guess one solution
is to remove duplicates from b
i'l try that I guess.
Ther leaning point from this is to READ the input specifications.
But in hindsight this is an abomination of a code.
version 2 lets go
Hmm not much of an improvement.
OH wow. I realize I was not effectively using the set() method. 
TIL that set(b) does not actually change b
but now I have another problem - the last index is always "T". Why is this so?
Im going to try and solve it in the morning.
'''
fi = open("DATA/DATA21.txt")
for i in range(10):
	a = int(fi.readline())
	b = fi.readline().split(" ")
	b = map(int, b)
	b = list(set(b))
	# print b
	c = fi.readline().split(" ")
	c[-1] = c[-1][0:len(c)-2]
	c = map(int, c)
	r = [""]*len(c)
	for j in b:
		# print r
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
	# for z in r:
	# 	if z != "T":
	# 		print "F",
	# 	else:
	# 		print z,
	# print "\n"
	print r
fi.close()

'''
solutions:
TTTTF
FFTTT
TFTTF
FTFFF
TTTTT
FFFFT
TTFFF
FFFTT
FTFTT
TFTFF
'''
