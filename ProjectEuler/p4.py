'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
-------------------------------------------------------------------------
I know I will get some square overlap in my method of doing this, but whatever.
Im not trying to make the most effecient solutions - just trying to solve these relatively noncomplex problems so that I can get to the more interesting ones
'''
n = []
for x in range(999,0,-1):
	for y in range(999,0,-1):
		if str(x*y) == str(x*y)[::-1]:
			n.append(x*y)
print max(n)
