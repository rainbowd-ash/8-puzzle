import random as r

p_size = 9
p_side = int(p_size / 3)


def sliding_block_puzzle():
	goal_state = list(range(0, p_size))
	goal_state.append(goal_state.pop(0)) # move 0 to end of list
	
	initial_state = goal_state.copy()
	r.shuffle(initial_state)
	while (inversion_count(goal_state)-inversion_count(initial_state)%2!=0):
		r.shuffle(initial_state)

	print(str(goal_state))
	print(inversion_count(goal_state))
	print(str(initial_state))
	print(str(misplaced_tiles(initial_state, goal_state)))
	print(str(manhatten_distance(initial_state, goal_state)))
	print(str(linear_conflict(initial_state, goal_state)))


def inversion_count(state):
	i_count = 0
	
	i_state = state.copy()
	i_state.remove(0)
	
	for i in range(0, len(i_state)):
		for j in range(0, i):
			if i_state[j] > i_state[i]:
				i_count += 1
	return i_count


def misplaced_tiles(state, goal_state):
	tile_count = 0
	for i in range(0, len(state)):
		if state[i] != goal_state[i]:
			tile_count += 1
	return tile_count


def manhatten_distance(state, goal_state):
	total_distance = 0
	for i in range(0, p_size - 1):
		if state[i] == 0:
			continue
		
		goal_position = goal_state.index(state[i])
		curr_row, curr_col = i // p_side, i % p_side
		goal_row, goal_col = goal_position // p_side, goal_position % p_side
		distance = abs(goal_row - curr_row) + abs(goal_col - curr_col)
		total_distance += distance
	
	return total_distance


def linear_conflict(state, goal_state):
	total_distance = manhatten_distance(state, goal_state)
	
	for row in range(p_side):
		row_tiles = [state[row * p_side + col] for col in range(p_side)]
		goal_row_tiles = [goal_state[row * p_side + col] for col in range(p_side)]
		total_distance += count_conflicts(row_tiles, goal_row_tiles)
	
	for col in range(p_side):
		col_tiles = [state[row * p_side + col] for col in range(p_side)]
		goal_col_tiles = [goal_state[row * p_side + col] for row in range(p_side)]
		total_distance += count_conflicts(col_tiles, goal_row_tiles)
	
	return total_distance


def count_conflicts(line, goal_line):
	conflicts = 0
	for i in range(p_side):
		for j in range(i + 1, p_side):
			if line[i] in goal_line and line[j] in goal_line:
				if goal_line.index(line[i]) > goal_line.index(line[j]):
					conflicts += 2
	return conflicts


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
