'''
#this is what I tried first. Works, but only if there are no repeated zeroes. 
t = int(raw_input())
z = []
s = 0
for i in range(t):
	z.append(int(raw_input()))
# z = [4,0,3,0]
#[4,0,3,0]
z.reverse()
#[0,3,0,4]
for i in range(len(z)):
	if z[i] == 0:
		s -= z[i+1]
	else:
		s += z[i]

print s
'''

#This solution actually works.
t = int(raw_input())
z = []
for i in range(t):
	f = int(raw_input())
	if f==0:
		del z[-1] #delete the last element of list
	else:
		z.append(f)
print sum(z)