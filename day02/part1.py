from pathlib import Path


def check_seq(sequence):
	# Returns 1 if a sequence is "safe" and 0 if a sequence is "unsafe"
	# For "mode": 0 is "undetermined", 1 is increasing, -1 is decreasing
	mode = 0
	# Check if safe
	for i in range(len(sequence)-1):
		# Compare items at index i and index i+1
		delta = sequence[i+1] - sequence[i]
		
		# Ensure delta has acceptable value
		if (abs(delta) not in (1, 2, 3)):
			return 0

		# Ensure delta has acceptable sign
		match mode:
			case 0: # Set mode and proceed
				if delta > 0:
					mode = 1
				elif delta < 0:
					mode = -1
				else:
					return 0
			case 1: # Fail if not increasing
				if delta <= 0:
					return 0
			case -1: # Fail if not decreasing
				if delta >= 0:
					return 0
	
	return 1


if __name__ == "__main__":
	# Input parser
	print("Copy and paste the contents of your input file here.")
	print("Alternatively, enter the name of a valid input file in your current working directory.")
	sequences = []
	while True:
		try:
			last_input = input()
			a = last_input.split()
			if not len(a):
				break
			sequences.append([int(i) for i in a])
		except ValueError:
			path_attempt = Path.cwd() / last_input
			if path_attempt.is_file():
				with open(path_attempt, 'r') as f:
					lines = f.read().strip().splitlines()
				for line in lines:
					a = line.split()
					sequences.append([int(i) for i in a])
			break
		
	# Check all sequences
	total = 0
	for sequence in sequences:
		total += check_seq(sequence)

	print(f"TOTAL SAFE SEQUENCES: {total}")