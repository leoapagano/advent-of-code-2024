from pathlib import Path


def check_table(table):
	# Checks a 2D table for how many times it contains two "SAM"s, crossing each other.
	h, w = len(table), len(table[0])
	total = 0
	for row in range(1, h-1):
		for col in range(1, w-1):
			if table[row][col] == "A":
				try:
					# Check first cross is either SAM or MAS
					cond1 = (table[row-1][col-1] + table[row][col] + table[row+1][col+1]) in ('SAM', 'MAS')
					# Check second cross is either SAM or MAS
					cond2 = (table[row-1][col+1] + table[row][col] + table[row+1][col-1]) in ('SAM', 'MAS')
					if (cond1 and cond2):
						total += 1
				except IndexError:
					pass
	
	return total


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
	

	# Calculate total number of X-SAMs
	print(f"TOTAL: {check_table(table)}")