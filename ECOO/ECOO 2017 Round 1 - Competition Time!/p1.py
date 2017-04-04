with open(raw_input("file> ")) as file:
	for _ in range(10):
		# read money
		money = int(file.next())

		# read students
		students = map(float, file.next().split(" "))

		# read total students
		total = int(file.next())

		# make list of (% students, price, total students)
		students = zip([12, 10, 7, 5], students, [total for _ in range(4)])
		# print students

		# multiply each group
		students = map(lambda a: a[0]*a[1]*a[2], students)

		# Print answer
		print "NO" if sum(students)/2 >= money else "YES"

		