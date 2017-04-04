with open("/Users/camran.hansen/Desktop/DATA21 2.txt") as file:

	for hellowrold in range(10):
		# carr = [["C1",[0,1,1],[0,1,1],[0,1,1]],["C2",[1,2,3]]]
		con = True
		indexthing = 0
		carr =[]
		while con == True:
			l = file.next().strip()
			
			# print l
			# print carr
			if l == "*":
				# print carr
				winners = []
				maxval = 0
				for i in range(len(carr)):
					s = 0
					b = carr[i][1:len(carr[i])]
					for z in b:
						for x in z:
							s += x
					# print carr[i]
					# print s
					if s== maxval:
						# print "yes"
						winners.append(carr[i])
						# print "fuck"
						# print carr[i]
					elif int(s) >= int(maxval):
						winners = [carr[i]]
						# print "no"
						# print carr[i]
						maxval = s
				# for asfd in winners:
					# print "FUCK"
					# print maxval
					# print asfd
				# print maxval
				# print "length"
				# print len(winners)
				gwinners = []
				gmax = 0
				fwinners = []
				fmax = 0
				pwinners = []
				pmax = 0
				# print len(winners)
				if len(winners) > 1:
					#initaite overdrive mde
					# print winners
					for thing_a in winners: #I really odn tcare that im really innefecient hHAHAHA 
						glocal = 0
						flocal = 0
						plocal = 0
						# print thing_a
						l = thing_a[1:len(thing_a)]
						for thing_b in l:
							# print thing_b
							glocal += thing_b[2]
							flocal += thing_b[1]
							plocal += thing_b[0]
						
						# if glocal >= gmax:
						# 	glocal = gmax
						if glocal == gmax:
							gwinners.append(thing_a)
						elif glocal >= gmax:
							gwinners = [thing_a]
							gmax = glocal
						if flocal == fmax:
							# print "FUCK asdf" + flocal
							fwinners.append(thing_a)
						elif flocal >= fmax:
							# print "Fuck asdf1234 " + str(flocal)
							fwinners = [thing_a]
							fmax = flocal
						if plocal == pmax:
							pwinners.append(thing_a)
						elif plocal >= pmax:
							pmax = plocal
							pwinners = [thing_a]
						# print thing_a
						# print "glocal = " + str(glocal)
						# print "flocal = " + str(flocal) 
						# print "plocal =" + str(plocal)
						# print "gmax = " + str(gmax)
						# print "fmax = " + str(fmax)
						# print "pmax = " + str(pmax)
					# Now for the last part of terrible logic
					# print len(gwinners)
					# print len(fwinners)
					# print len(pwinners)
					# print gwinners
					# print gmax
					# print "   JDFSFDSFLKDSK "
					# print fwinners
					# print fmax
					# print "   JDFSFDSFLKDSK "
					# print pwinners
					# print "   JDFSFDSFLKDSK "
					if len(gwinners[0]) == 1:
						print gwinners[0][0]
					elif len(fwinners[0]) == 1:
						print fwinners[0][0]
					elif len(pwinners[0]) == 1:
						print pwinners[0][0]
				else:
					for thing_z in winners:
						# print "DUCK"
						print thing_z[0]
				break
			elif l.split(" ")[0] == "J":
				l = l.split(" ")
				# print "fUCK"
				l = l[1:]
				l = map(int, l)
				carr[-1].append(l)
				# print l
				# print carr
				# carr[-1]
			else:
				carr.append([l])
			# elif len(l) == len(l.replace(" ","")):

			# 	carr.append([l])
			# 	indexthing += 1
			# # else:
			# 	carr[indexthing].append(map(int,l.split(" ")[1:]))
			# print carr

