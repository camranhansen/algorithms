with open("DATA/DATA10.txt") as file:

	first = file.next()

	TAKEN = 0
	SERVED = 0

	for word in file:
		word = word.strip()

		if word == "TAKE":
			TAKEN += 1 if TAKEN == 999 else TAKEN + 1
		if word == "SERVE":
			SERVED += 1
		if word == "CLOSE":
			print str(TAKEN + (TAKEN-SERVED) + first)
