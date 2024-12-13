from utils.geometry import *
from collections import deque

with open('../inputs/real/input_day_21.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    grid_size = len(lines)
    grid = grid_dict('\n'.join(lines))
    grid = {plot: grid[plot] for plot in grid.keys() if grid[plot] != '#'}

    visited = dict()
    queue = deque([(0, grid_position('S', grid)[0])])

    # BFS to get distances to all spots
    while queue:
        distance, point = queue.popleft()
        if point in visited:
            continue

        visited[point] = distance

        # Get possible steps
        for node in get_neighbours_dict(point, grid, False).keys():
            # If step was visited - skip it
            if node in visited:
                continue
            # Otherwise add it to the queue
            queue.append((distance + 1, node))

    distance_to_edge = grid_size // 2
    n = (26501365 - distance_to_edge) // grid_size
    num_odd_tiles = (n + 1) ** 2
    num_even_tiles = n ** 2

    odd_corners = len([spot for spot in visited.values() if spot > distance_to_edge and spot % 2 == 1])
    even_corners = len([spot for spot in visited.values() if spot > distance_to_edge and spot % 2 == 0])
    even_squares = len([spot for spot in visited.values() if spot % 2 == 0])
    odd_squares = len([spot for spot in visited.values() if spot % 2 == 1])

    answer = (num_odd_tiles * odd_squares
              + num_even_tiles * even_squares
              - ((n + 1) * odd_corners)
              + (n * even_corners))

    return answer


print("Answer:", process(input_lines))
