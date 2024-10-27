import random as r
import argparse
from searches import *
from heuristics import *


def parse_args():
	parser = argparse.ArgumentParser(description="Welcome to the sliderrrrr")
	
	parser.add_argument(
		'--size',
		type = int,
		choices = [9, 16],
		default = 9,
		help = "Size of puzzle, either 9 (3x3) or 16 (4x4). Default is 9."
	)
	
	parser.add_argument(
		'--algo',
		type = str,
		choices=['a_star', 'best_first'],
		default = 'a_star',
		help="Search algorithm to use, 'a_star' or 'best_first'. Default is a_star."
    )
	
	parser.add_argument(
		'--heuristic',
		type=str,
		choices=['misplaced_tiles', 'manhatten_distance', 'linear_conflicts'],
		default='manhatten_distance',
		help="Heuristic to use for evaluation, 'misplaced_tiles', 'manhatten_distance', or 'linear_conflicts'. Default is 'manhatten_distance'."
	)
	
	return parser.parse_args()

def sliding_block_puzzle(size, algo_fn, heuristic_fn):
	side = int(math.sqrt(size))
	goal_state = list(range(1, size)) + [0]  # Goal state with 0 at the end

	# Generate a random initial state that is solvable
	initial_state = goal_state.copy()
	while True:
		r.shuffle(initial_state)
		if is_solvable(initial_state, side):
			break

	# Run the chosen algorithm and print results
	result = algo_fn(initial_state, goal_state, heuristic_fn)
	print("Solution Path:", result)
	print("Moves to Solve:", len(result))


def inversion_count(state):
	i_count = 0
	i_state = [tile for tile in state if tile != 0]

	for i in range(len(i_state)):
		for j in range(i):
			if i_state[j] > i_state[i]:
				i_count += 1
	return i_count


def is_solvable(state, side):
	inversions = inversion_count(state)
	blank_row = state.index(0) // side

	if side % 2 != 0:
		return inversions % 2 == 0

	return (inversions + blank_row) % 2 == 1


if __name__ == "__main__":
	args = parse_args()
	print("Running Solver:")
	print("Size:", args.size)
	print("Algorithm:", args.algo)
	print("Heuristic:", args.heuristic)
	print()

	algorithms = {
		'best_first': best_first,
		'a_star': a_star
	}

	heuristics = {
		'misplaced_tiles': misplaced_tiles,
		'manhatten_distance': manhatten_distance,
		'linear_conflicts': linear_conflicts
	}

	algo_fn = algorithms.get(args.algo)
	heuristic_fn = heuristics.get(args.heuristic)

	if not algo_fn or not heuristic_fn:
		print("Invalid algorithm or heuristic specified!")
	else:
		sliding_block_puzzle(args.size, algo_fn, heuristic_fn)
