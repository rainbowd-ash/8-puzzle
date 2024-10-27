import math

def misplaced_tiles(state, goal_state):
	tile_count = 0
	for i in range(0, len(state)):
		if state[i] != goal_state[i]:
			tile_count += 1
	return tile_count


def manhatten_distance(state, goal_state):
	size = len(state)
	side = int(math.sqrt(size))
	total_distance = 0
	for i in range(size):
		if state[i] == 0:  # Skip the blank space
			continue
		
		goal_position = goal_state.index(state[i])
		curr_row, curr_col = i // side, i % side
		goal_row, goal_col = goal_position // side, goal_position % side
		distance = abs(goal_row - curr_row) + abs(goal_col - curr_col)
		total_distance += distance

	return total_distance


def linear_conflicts(state, goal_state):
	side = int(math.sqrt(len(state)))
	total_distance = manhatten_distance(state, goal_state)

	# Check for conflicts in each row
	for row in range(side):
		row_tiles = [state[row * side + col] for col in range(side)]
		goal_row_tiles = [goal_state[row * side + col] for col in range(side)]
		total_distance += count_conflicts(side, row_tiles, goal_row_tiles)

	# Check for conflicts in each column
	for col in range(side):
		col_tiles = [state[row * side + col] for row in range(side)]
		goal_col_tiles = [goal_state[row * side + col] for row in range(side)]
		total_distance += count_conflicts(side, col_tiles, goal_col_tiles)

	return total_distance


def count_conflicts(side, line, goal_line):
	conflicts = 0
	for i in range(side):
		for j in range(i + 1, side):
			if line[i] in goal_line and line[j] in goal_line:
				# If two tiles are in goal row or column but out of order
				if goal_line.index(line[i]) > goal_line.index(line[j]):
					conflicts += 2  # Add 2 for each pair conflict
	return conflicts
