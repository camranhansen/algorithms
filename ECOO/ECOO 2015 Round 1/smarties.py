#Over the course of me doing these problems, I have developed a distaste for ECOO problems. 
#hail c'thulu
#start time = 12:05 done = 00:39, perfect on test case 11
import math

f = open("data/DATA11.txt")
for i in range(10):
	t = 0
	cl = {"orange":0,"blue":0,"green":0,"yellow":0,"pink":0,"violet":0,"brown":0,"red":0}
	c = True
	while c == True:
		l = f.readline()
		l = l[0:len(l)-2]
		if l == "end of box":
			c = False
			break
		else:
			cl[l] += 1
	# print cl

	for i in range(8):
		if cl.keys()[i] == "red":
			# print t
			# print int(cl[cl.keys()[i]])
			t += int(cl[cl.keys()[i]])*16
			# print "doing it"
		else:
			# print math.ceil((cl[cl.keys()[i]])/7.0)
			t += (math.ceil((cl[cl.keys()[i]]/7.0)))*13
	print int(t)
f.close()

'''answers = 
716
246
300
377
834
297
814
528
322
834
'''
