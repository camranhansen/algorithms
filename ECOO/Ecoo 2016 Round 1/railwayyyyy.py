'''
[railw] ayy lmao
just to make sure I understand why it takes 12 moves:
3 5 1 4 2
5 3 1 4 2 [1]
4 5 3 1 2 [3]
3 4 5 1 2 [2]
2 3 4 5 1 [4]
1 2 3 4 5 [4]
1 +3 +2 +4 +4 = 14.
hmmmm: where am I wrong.
What if I just ignore the 5:
3 5 1 4 2
4 3 5 1 2 [3]
3 4 5 1 2 [1]
2 3 4 5 1 [4]
1 2 3 4 5 [4]
= 12
Ok, so that works. I guess what I do is ignore the back-end max values
assuming that they are sorted.
So like if it was 3 2 4 5 1 I would not worry about moving 4 5, as well as 3.
------------
another learning point: check to make sure that all of the functions work before you do a test, test them with other data just incase.
------------
Post-problem breakdown:
I initially thought that the big numbers had to be consecutively sorted
(for example 4,5,1,2,3)
but in fact
they just need to be sorted without regard to other numbers
from smallest left to largest right
so 
4,2,5,1,3
also requires no moving of either 4 or 5
So the takeway from this is that
I should test other cases than the test case.
Especially strange cases (already sorted for example)
Before zealously testing. Since during the competition that will lose us marks.
'''
fi = open("DATA/DATA31.txt")
for i in range(10):
	a,b = int(fi.readline()), fi.readline().split(" ")
	del b[-1]
	b = map(int, b)
	if sorted(b) == b:
		print 0
		continue
	z,c,t,k = 0,1,0,True
	# c is the number of indices we should skip. start out at 1 because we do not move the last number.
	while k:
		q = c
		c = c + 1 if b.index(a-z) > b.index(a-z-1) else c
		z += 1
		k = False if q == c else True
	for i in range(a-c,0,-1):
		x = list()
		t += b.index(i)
		x.append(b[b.index(i)])
		b.pop(b.index(i))
		b = x + b
	print t
fi.close()