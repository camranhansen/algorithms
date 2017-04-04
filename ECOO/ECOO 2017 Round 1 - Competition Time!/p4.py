def string2int(name):
	return map(lambda char: ord(char)-65, list(name))

def convert(max_len):
	weights = map(lambda x: 100**x, range(max_len-1, -1, -1))
	return lambda name: sum(map(lambda a: a[0]*a[1], zip(string2int(name), weights)))

def swap_distance(array):
	distances = [abs(kids.index(x) - skids.index(x)) for x in kids]
	return sum(map(lambda a: abs(a[0] - a[1]), zip(distances, range(len(array)-1)))) - len(array) + 2

				

with open(raw_input("file> ")) as file:
	for _ in range(10):
		# Read no kids
		kid_count = int(file.next().strip())

		# Read all kids
		kids = [file.next().strip() for _ in range(kid_count)]

		# longest name
		l_name = max(map(len, kids))

		# Convert to wieghts
		kids = map(convert(l_name), kids)

		# Sort them
		skids = sorted(kids)

		# Find distances between all names
		distances = [abs(kids.index(x) - skids.index(x)) for x in kids]
		kids.pop(distances.index(max(distances)))

		print swap_distance(kids)