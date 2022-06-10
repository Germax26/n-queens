import sys

def print_pos(pos):
	for i in pos:
		print(". " * i + "#" + " ." * (7 - i))

def is_unique(pos):
	"""
	The way this works is by checking that there aren't
	any duplication digits (by checkin that the set of
	all the digits in poses doesn't fall below 8), if so,
	it means that there are no queens on the same row.
	"""

	return len(set(pos)) == len(pos)

def is_nondiagonal(pos):
	"""
	The way this works is by going through each digit pair 
	and checking if the difference in position is equal to 
	the difference in the value of the digits. If so, it
	means that the queens are on a diagonal
	"""
	for i in range(len(pos)):
		for j in range(i + 1, len(pos)):
			if abs(pos[i] - pos[j]) == abs(i - j):
				return False
	return True

def is_solution(pos):
	return is_unique(pos) and is_nondiagonal(pos)
			
def get_solutions():
	def impl(pos):
		if len(pos) == 8:
			yield pos
		else:
			for i in range(8):
				new_pos = pos + [i]
				if is_solution(new_pos):
					yield from impl(new_pos)

	yield from impl([])

if __name__ == "__main__":

	def usage():
		print(f"usage: {sys.argv[0]} <method> [--silent] [-s]")
		print("\nThe available methods are:\n\toct - for using base 8\n\trec - for using recursion")

	silent = False

	for i in sys.argv[1:]:
		if i.startswith('-'):
			match i[1:]:
				case '-silent' | 'S':
					silent = True
				case _:
					usage()
					print(f"Unknown flag: '{i}'")
					exit(1)

	num = 0
	if silent:
		for _ in get_solutions(): num += 1
		print("Total solutions:", num)
	else:
		for pos in get_solutions():
			num += 1
			print("-" * 15, num)
			print_pos(pos)
