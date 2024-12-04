from pathlib import Path

if __name__ == "__main__":
	# Input parser
	print("Copy and paste the contents of your input file here.")
	print("Alternatively, enter the name of a valid input file in your current working directory.")
	A = []
	B = []
	while True:
		try:
			last_input = input()
			a, b = last_input.split()
			A.append(int(a))
			B.append(int(b))
		except ValueError:
			path_attempt = Path.cwd() / last_input
			if path_attempt.is_file():
				with open(path_attempt, 'r') as f:
					lines = f.read().strip().splitlines()
				for line in lines:
					a, b = line.split()
					A.append(int(a))
					B.append(int(b))
			break
		
	# Sort and reverse lists
	A.sort()
	A.reverse()
	B.sort()
	B.reverse()

	# Compute total
	total = 0
	for _ in range(len(A)):
		total += abs(A.pop() - B.pop())
	
	print(f"RESULT: {total}")