# notused = raw_input()
# text_input = raw_input() 
text_input = "50 55 10440 5220 5220 3186 4375 3186 20880 52507 34095 7184 45323 45323 7184 1990 17896 995 293 409 293 4448 4448 7511 911 911 911 911 402 402 209 386 209 1822 911 911 53 53 5505 106 71893 1301 753 1609 753 1301 25303 5469 5469 10938 31"
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
	# print "d= " + str(d)
	# print "s= " + str(s)
	if d==[] and s==[]:
		# print "exiting hahAA"
		m.append(max(a))
		return
	else:
		for j in d:
			# print "going through: " + str(j)
			p = copy.deepcopy(a)
			# print "p= " + str(p)
			# print "a= " + str(p)
			# print "p(j) =" + str(p[j])
			# print "p(j+1) =" + str(p[j+1])
			# p.pop(j)
			d1 = p.pop(j)
			d2 = p.pop(j)
			p.insert(j, (d1+d2))
			# print "after, p= " + str(p)
			# print "after, a= " + str(a)
			stepstepstep(p)
		for z in s:
			p = copy.deepcopy(a)
			p1 = p.pop(z)
			p2 = p.pop(z)
			p3 = p.pop(z)
			p.insert(z, (p1+p2+p3))
			# print "after, p= " + str(p)
			stepstepstep(p)


stepstepstep(r)

# print "maximums: "
# print m
print max(m)