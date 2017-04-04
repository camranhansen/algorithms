import math
'''
Making your code look good, or even readable? In 2017? what a foreign concept. Sorry about the unreadability of the code, in advance.
Also, interesting story: I was wondering why my code was not working, (it was returning a value ~2% from test case), and I was starting to get worried. But then I realized that in fact.
My circle generation function was generating a square. So, takeway: make sure that your functions actually work.
'''
def pythag(x1,y1,x2,y2):
	return math.sqrt(((abs(x1-x2))**2)+((abs(y1-y2))**2))

def fa(x,y,r):
	lns = [100000]*3
	for pexhs in r:
		if pythag(x,y,pexhs[0],pexhs[1]) == 0:
			return [0,0]
		elif pythag(x,y,pexhs[0],pexhs[1])<max(lns):
			lns[lns.index(max(lns))] = pythag(x,y,pexhs[0],pexhs[1])
	#yes, I know that I do not have to go through this so many times. However, I do not really care much for the effeciency of my solution.. hopefuly?
	#im going to code a better solution tommorow morning. but right now (3-4AM), not really.
	lns.sort()
	af = [] #the ARRAY of affiliations
	for b in r:
		if pythag(x,y,b[0],b[1]) == lns[0] or pythag(x,y,b[0],b[1]) == lns[1] or pythag(x,y,b[0],b[1]) == lns[2]:
			af.append(b[2])
	if af.count('D')>=af.count('R'):
		return [1.0,1.0]
	else:
		return [0.0,1.0]
def dothething(z,r):
	for g in r:
		h = r.index(g)
		r[h] = g.split(" ") 
		#yes I know that list comrephension is a thing as well as the map function
		#I will probably make this a map function later
		#but whatever
		r[h][-1] = r[h][-1][0:1]
		r[h][0],r[h][1] = int(r[h][0]),int(r[h][1])
	#strip newlines
	z[1] = z[1][0:len(z[1])-2]
	z = map(int,z)
	democrats = 0.0
	total = 0.0
	# print z
	# print r
	for xc in range(-50,51,1):
		for yc in range(-50,51,1):
			if pythag(xc,yc,0,0) <=50.0:
				ar = fa((xc+z[0]),(yc+z[1]),r)
				democrats += ar[0]
				total += ar[1]
					# print "didnt do it"
					# todo actually learn the any() function https://docs.python.org/3/library/functions.html#any

	print round((democrats/total), 3)*100 #not excactly sure why my numbers dont match the answers.. Strange..... I wonder why I am 0.1 percent off.
fi = open("DATA/DATA41.txt")
for i in range(10):
	iz = fi.readline().split(" ")
	ir = []
	for i in range(100):
		ir.append(fi.readline())
	dothething(iz,ir)
fi.close()