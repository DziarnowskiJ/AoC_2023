from utils.geometry import *
from queue import Queue

with open('../inputs/real/input_day_21.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_21.txt', 'r') as file:
    sample_lines = file.readlines()


def steps_to_reach(grid: dict[Point, str], start: Point) -> dict[Point, int]:
    visited = {start: 0}
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        current_point = queue.get()
        current_distance = visited[current_point]

        neighbors = get_neighbours_dict(current_point, grid, diagonal=False)

        for neighbor_point, neighbor_char in neighbors.items():
            if neighbor_char == '.' and neighbor_point not in visited:
                visited[neighbor_point] = current_distance + 1
                queue.put(neighbor_point)

    return visited


def process(input_lines, steps):
    grid = grid_dict(''.join(input_lines))
    step_dict = steps_to_reach(grid, grid_position('S', grid)[0])

    possible_grid = grid
    for key, val in step_dict.items():
        if val % 2 == 0 and val <= steps:
            possible_grid[key] = 'O'

    return len(grid_position('O', possible_grid))


print("Sample output:", process(sample_lines, 6))
print("Answer:", process(lines, 64))
