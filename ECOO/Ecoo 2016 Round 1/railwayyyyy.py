'''
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
'''
# a = 5
# b = [3,5,1,4,2]
# z = b.index(max(b))
 
#to be continued...