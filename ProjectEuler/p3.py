'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

-------------------------------------------------------------
im not trying to code golf this stuff.
Also pro tip you can do memory overflow if your numbers get too big.
'''

n,p = 600851475143,[]
def isprime(x):
	for i in range(2,int(x**0.5)+1):
		if x%i==0:
			return False
	return True
for i in range(2,int((n**0.5))+1):
	if n%i==0:
		if isprime(i):
			p.append(i)
		if isprime(n/i):
			p.append(n/i)
print max(p)