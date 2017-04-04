from math import floor

board = []
with open("DATA/DATA30.txt") as file:
	for line in file:
		board += map(lambda x: int(x, 16) if x != "-" else "-", line.strip())

print board

flr  = lambda x: int(floor(x))
row  = lambda x: board[flr(x/16):flr(x/16)+16]
col  = lambda x: board[x::16]
cell = lambda x: sum([board[flr(x/4)+(k*12):flr(x/4)+(k*12)+4] for k in range(4)], [])

solved = 1
for i in range(5):
	solve = 0
	for i in range(len(board)):
		if board[i] == "-":
			for c in range(17):
				if (c not in row(i)) and (c not in col(i)) and (c not in cell(i)):
					board[i] = c
					solve = 1

print board
