
# Open the file
with open("DATA/DATA10.txt") as file:
	
	# Skip line one
	first = file.next()

	counter = 1
	in_line = 0
	served  = 0

	# For each command
	for word in file:
		# Strip line ending
		word = word.strip()
		
		if word == "TAKE":
			# Counter increase and rollover
			counter = 1 if counter == 999 else counter + 1
			in_line += 1

		if word == "SERVE":
			served += 1
			in_line -= 1

		if word == "CLOSE":
			print str(served) + " " + str(in_line) + " " + str(first)
			first = 0
			served  = 0
			in_line = 0
