# notused = raw_input()
# text_input = raw_input() 
text_input = "1 1 1 1 1 1 1 1 1 1 1 1"
r = map(int, text_input.split(' '))
# man map function is really useful didnt know
import copy 
#deep copying is neccesarry for this really terrible solution I have come up with. 
#It's a work-around around a work-around. Please don't do this in your actual code.
m = []
m.append(max(r))
def stepstepstep(a):
	# print "begining, one step in!"
	# print a
	d = []
	s = []

	#naive way of finding all possible matches. Finds indexes, appends them to arrays (d = double, s=sandwich)
	#This is naive because it could be done in one loop. 
	#However, i have chosen to do it this way because overall this code is severely unoptimised.
	for i in range(len(a)-1):
		if a[i]==a[i+1]:
			d.append(i)
	for i in range(len(a)-2):
		if a[i]==a[i+2]:
			s.append(i)
	if d==[] and s==[]:
		m.append(max(a))
		return
	else:
		for j in d:
			p = copy.deepcopy(a)
			d1 = p.pop(j)
			d2 = p.pop(j)
			p.insert(j, (d1+d2))
			stepstepstep(p)
		for z in s:
			p = copy.deepcopy(a)
			p1 = p.pop(z)
			p2 = p.pop(z)
			p3 = p.pop(z)
			p.insert(z, (p1+p2+p3))
			stepstepstep(p)


stepstepstep(r)

# print "maximums: "
# print m
print max(m)