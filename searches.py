import heapq
import math

def get_possible_states(state):
	side = int(math.sqrt(len(state)))
	possiblities = []
	blank        = state.index(0)
	row, col     = blank // side, blank % side
	directions   = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	
	for drow, dcol in directions:
		new_row, new_col = row + drow, col + dcol
		
		if 0 <= new_row < side and 0 <= new_col < side:
			new_state = state.copy()
			swap_index = new_row * side + new_col
			new_state[blank], new_state[swap_index] = new_state[swap_index], new_state[blank]
			possiblities.append(new_state)
	return possiblities


def best_first(start_state, goal_state, heuristic_fn):
	open_list = []
	heapq.heappush(open_list, (heuristic_fn(start_state, goal_state), start_state, []))

	visited = set()

	while open_list:
		_, current_state, path = heapq.heappop(open_list)
		if current_state == goal_state:
			return path + [current_state]
		
		visited.add(tuple(current_state))
		
		for future in get_possible_states(current_state):
			if tuple(future) not in visited:
				new_path = path + [current_state]
				heuristic = heuristic_fn(future, goal_state)
				heapq.heappush(open_list, (heuristic, future, new_path))
	return None


def a_star(start_state, goal_state, heuristic_fn):
	frontier = []
	heapq.heappush(frontier, (0, start_state))
	came_from = {}
	g_score = {tuple(start_state): 0}
	came_from[tuple(start_state)] = None

	while frontier:
		current_f, current_state = heapq.heappop(frontier)
		
		# Goal check
		if current_state == goal_state:
			return reconstruct_path(came_from, current_state)

		# Expand neighbors
		for neighbor in get_possible_states(current_state):
			tentative_g = g_score[tuple(current_state)] + 1
			neighbor_tuple = tuple(neighbor)
			
			if neighbor_tuple not in g_score or tentative_g < g_score[neighbor_tuple]:
				g_score[neighbor_tuple] = tentative_g
				f_score = tentative_g + heuristic_fn(neighbor, goal_state)
				heapq.heappush(frontier, (f_score, neighbor))
				came_from[neighbor_tuple] = current_state

	return None  # Return None if no solution is found


def reconstruct_path(came_from, current_state):
	path = [current_state]
	while came_from[tuple(current_state)]:
		current_state = came_from[tuple(current_state)]
		path.append(current_state)
	path.reverse()
	return path

