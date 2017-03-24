'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
---------------------------------------------------------------------------
'''
def isprime(x):
	for i in range(2,int(x**0.5)+1):
		if x%i==0:
			return False
	return True
n = 20
r = 1
for i in range(2,n):
	for z in range(2,n):
		if isprime(i):
			t = z
			print "yes?"
			# print t
			if t%i == 0:
				while t%i == 0:
					print i
					print "doing it" + str(t)
					t = t/i
					# print t
					r *= i
			else:
				print "yes" + str(i)
				r *= i
print r