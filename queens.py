#! python3

import sys

WIDTH, HEIGHT, N = 8, 8, 8

assert N <= min(WIDTH, HEIGHT)

def print_pos(pos):
	for i in range(HEIGHT):
		if i in pos:
			j = pos[i]
			print(". " * j + "#" + " ." * (WIDTH - 1 - j))
		else:
			print(". " * WIDTH)

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
			for i in range(max(pos) if pos else 0, HEIGHT):
				for j in range(WIDTH):
					if i not in pos:
						new_pos = pos | {i: j}
						if is_solution(new_pos):
							yield from impl(new_pos)

	yield from impl({})

if __name__ == "__main__":

	def usage():
		print(f"usage: {sys.argv[0]} <method> [--width=<width>] [-W=<width>] [--height=<height>] [-H=<height>] [-N=<N>] [--silent] [-S]")
		print("\nThe available methods are:\n\toct - for using base 8\n\trec - for using recursion")

	silent = False

	for i in sys.argv[1:]:
		if i.startswith('-'):
			match i[1:].split('='):
				case ['-silent' | 'S']:
					silent = True
				case ['-width' | 'W', w]:
					WIDTH = int(w)
				case ['-height' | 'H', h]:
					HEIGHT = int(h)
				case ['N', n]:
					N = int(n)
				case _:
					usage()
					print(f"Unknown flag: '{i}'")
					exit(1)

	if min(WIDTH, HEIGHT) <= 0:
		print("The board cannot have non-positive dimentions.")
		exit(1)

	if N < 0:
		print("There cannot be a number of negative queens.")
		exit(1)

	if N > min(WIDTH, HEIGHT):
		print(f"Cannot place {N} queens on an {WIDTH} x {HEIGHT} board.")
		if N > WIDTH:
			print("There are not enough columns.")
		if N > HEIGHT:
			print("There are not enough rows.")
		exit(1)

	num = 0
	if silent:
		for _ in get_solutions(): num += 1
		match num:
			case 0:
				print("No solutions")
			case 1:
				print("1 solution")
			case _:
				print(num, "solutions")
	else:
		for pos in get_solutions():
			num += 1
			print("-" * (WIDTH * 2 - 1), num)
			print_pos(pos)
		if not num:
			print("No solutions")
