from pathlib import Path


def check_table(table):
	# Checks a 2D table for how many times it contains "XMAS", going left-right. Returns the total as an integer.
	total = 0
	for row in table:
		for idx in range(len(row)):
			if row[idx] == "X":
				try:
					if (row[idx+1] == "M") and (row[idx+2] == "A") and (row[idx+3] == "S"):
						total += 1
				except IndexError:
					pass
	
	return total


def rotate_table_90deg(table, n):
	# Rotates a table n*90 degrees clockwise, shallow-copying it, and returns it.
	nt = table
	for i in range(n%4):
		nt = list(zip(*nt[::-1]))
	return nt


def stagger_table(table, mode):
	# Staggers a table left or right (select with mode parameter: 0 for left, 1 for right).
	# Create empty table to store staggered data in
	h, w = len(table), len(table[0])
	out = [[0 for x in range(w+h-1)] for y in range(h)]
	for row_idx in range(h):
		for item_idx in range(w):
			out[row_idx][(item_idx+h-row_idx-1) if mode else (item_idx+row_idx)] = table[row_idx][item_idx]
	return out


if __name__ == "__main__":
	# Input parser
	print("Copy and paste the contents of your input file here.")
	print("Alternatively, enter the name of a valid input file in your current working directory.")
	table = []
	while True:
		last_input = input()
		if not len(last_input):
			break
		path_attempt = Path.cwd() / last_input
		if path_attempt.is_file():
			with open(path_attempt, 'r') as f:
				lines = f.read().splitlines()
			for line in lines:
				table.append([char for char in line])
			break
		else:
			table.append([char for char in last_input])
	for row in table:
		if len(row) != len(table[0]):
			print("Table row lengths mismatched. Please double check your input and try again.")
	

	# Calculate total number of XMASes
	sum = 0

	# Look for horizontals and verticals
	sum += check_table(rotate_table_90deg(table, 0))
	sum += check_table(rotate_table_90deg(table, 1))
	sum += check_table(rotate_table_90deg(table, 2))
	sum += check_table(rotate_table_90deg(table, 3))

	# Look for diagonals
	sl = stagger_table(table, 0)
	sum += check_table(rotate_table_90deg(sl, 1))
	sum += check_table(rotate_table_90deg(sl, 3))
	sr = stagger_table(table, 1)
	sum += check_table(rotate_table_90deg(sr, 1))
	sum += check_table(rotate_table_90deg(sr, 3))

	# Close up shop
	print(f"TOTAL: {sum}")