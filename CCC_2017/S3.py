l1 = int("5")
l2 = "1 10 100 1000 2000"
# l1 = int(raw_input())
# l2 = raw_input()
#rainbow method
#like I know that you are supposed to do it using recursion i just dont know how.
# l1 = int(raw_input())
# l2 = raw_input()
l = l2.split(" ")
d = []
for item in l:
	d.append(int(item))
#this is REALLY BAD CODING PRACTICE
d.sort()
#step 1: find max length
fuck = [None]*max(d)*2 #memory intensive fuckfest
#i = 0
#n = last index of array we are looking at
#s = high end of new sum
#k = low end of new sum

def f(i):
	for x in range(l1):
		for z in range(x+1,5):
			asdf = d[x] + d[z]
			if fuck[asdf] == None:
				fuck[asdf] = 1
				# print "?!"
			else:
				fuck[asdf] += 1

	for n in range(l1-1, i+2,-1):
		# print "n = " + str(n)
		t = d[i] + d[n]
		
			# print "dsf"
		# # if  t > d[n-1] + d[n-2]:
		# # 	# print "fuck"
		# # 	# break
		# # 	pass
		# else:
		for s in range(n-1,i+1,-1):
			# print "s = " + str(s)
			# if t>d[s]+d[s-1]:
			# 	# print "fuck again"
			# 	# break
			# 	pass
			# else:
			for k in range(s-1, i,-1):
				# print "k = " + str(k)
				if t==d[s]+d[k]:
					fuck[t] += 1
					# print "works!"


for i in range(l1-3):
	f(i)
# print fuck.count(1)
m = 0
cd = 0
# for i in range(len(fuck)-1,0,-1):
# 	if fuck[i] != None:
# 		print fuck[i],
for i in range(len(fuck)-1,0,-1):
	if fuck[i]>m:
		m = fuck[i]
		cd = i
print fuck[cd]
print fuck.count(fuck[cd])


		# print i