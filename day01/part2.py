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
		
	# For each item to the left...
	# "How many times does it appear?"
	total = 0
	for item in A:
		total += item * B.count(item)

	print(f"RESULT: {total}")