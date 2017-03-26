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
c = False
k = 1
import time
while c == False:
	c = True
	for i in range(n,0,-1):
		# print i
		if k%i != 0:
			# print "not divisible"
			c = False
			t = i
			while t>1:
					# print "did it once"
				# time.sleep(1)
				# print "starting loop, t = " + str(t)
				for j in range(t,0,-1):
					# time.sleep(0)
					# print "j = " + str(j)
						# print j
					if isprime(j) == True and t%j == 0:
						if j==2:
							pass
							# print "doing division, t = " + str(t) +  " J = " + str(j) + ". K = " + str(k)
							# print "multiplying by 2"
						t = t/j
						k *= j
						break
# c = False
# while c == False:
# 	c = True
# 	for x in range(20,1,-1):
# 		print x 
# 		print divmod(k, x)
# 		# time.sleep(0.1)
# 		# print "this is"

# 		print divmod(k, x)[0]%x
# 		if divmod(k, x)[0]%x == 0:
# 			# print k
# 			# print x

# 			# k = k/x
# 			# print k
# 			c = False
# 		if c == False:
# 			break
			

#yes I know that this is really bad coding practice but I know that I have to divide by 16 but am too lazy to rewrite my whole algorithm please forgive me
#it gets caught up when t = 16, and instead of simply just mulitplying once it does it
#I am going to recode this 
print k