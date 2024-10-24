import random as r

puzzle_size = 9


def sliding_block_puzzle():
	goal_state = list(range(0, puzzle_size))
	goal_state.append(goal_state.pop(0)) # move 0 to end of list
	
	initial_state = goal_state.copy()
	r.shuffle(initial_state)

	print(str(goal_state))
	print(str(initial_state))
	print(str(manhatten_distance(initial_state, goal_state)))


def manhatten_distance(current_state, goal_state):
	total_distance = 0
	for i in range(puzzle_size):
		if current_state[i] == 0:
			continue
		
		goal_position = goal_state.index(current_state[i])
		curr_row, curr_col = i // 3, i % 3
		goal_row, goal_col = goal_position // 3, goal_position % 3
		distance = abs(goal_row - curr_row) + abs(goal_col - curr_col)
		total_distance += distance
	
	return total_distance


def get_possible_states(state):
	possiblities = []
	blank        = state.index(0)
	row, col     = blank // 3, blank % 3
	directions   = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	
	for drow, dcol in directions:
		new_row, new_col = row + drow, col + dcol
		
		if 0 <= new_row < 3 and 0 <= new_col < 3:
			new_state = state.copy()
			swap_index = new_row * 3 + new_col
			new_state[blank], new_state[swap_index] = \
			new_state[swap_index], new_state[blank]
		possiblities.append(new_state)
	return possiblities

sliding_block_puzzle()
