import sys

WIDTH, HEIGHT, N = 8, 8, 8

assert N <= min(WIDTH, HEIGHT)

def print_pos(pos):
	for i in range(HEIGHT):
		if i in pos:
			j = pos[i]
			print(". " * j + "#" + " ." * (HEIGHT - 1 - j))

def is_solution(pos):
	"""
	The way this works is by going through each digit pair 
	and checking if either the rows are equal, or the 
	difference in the value of the digits is equal to the
	difference in the indexes. If so, then that means that
	the queens can attack each other.
	"""
	for i, k in enumerate(pos):
		for j, l in enumerate(pos):
			if i < j and (pos[k] == pos[l] or abs(pos[k] - pos[l]) == abs(k - l)):
				return False
	return True

def get_solutions():
	def impl(pos):
		if len(pos) == N:
			yield pos
		else:
			for i in range(max(pos) if pos else 0, WIDTH):
				for j in range(HEIGHT):
					if i not in pos:
						new_pos = pos | {i: j}
						if is_solution(new_pos):
							yield from impl(new_pos)

	yield from impl({})

if __name__ == "__main__":

	def usage():
		print(f"usage: {sys.argv[0]} <method> [--silent] [-S]")
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
			print("-" * (HEIGHT * 2 - 1), num)
			print_pos(pos)
