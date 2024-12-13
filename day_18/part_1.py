from collections import deque

from utils.geometry import *


def tokens(text_lines):
    return [text_line.strip().split(' ') for text_line in text_lines]


with open('../inputs/real/input_day_18.txt', 'r') as file:
    lines = file.readlines()
    token_lines = tokens(lines)

with open('../inputs/sample/sample_input_day_18.txt', 'r') as file:
    sample_lines = file.readlines()
    token_sample_lines = tokens(sample_lines)
    

def flood_fill(grid: dict[Point, str], start_point: Point, fill_char: str) -> dict[Point, str]:
    """
    Perform flood fill on a grid starting from the given point.

    Parameters:
    - grid: A dictionary representing the grid.
    - start_point: The starting point for the flood fill.
    - fill_char: The character to fill the connected region with.

    Returns:
    A new grid with the flooded area filled with the specified character.
    """

    # Check if the starting point is in the grid
    if not is_in_grid(start_point, grid):
        raise ValueError("Starting point is outside the grid.")

    # Create a copy of the original grid to modify
    new_grid = grid.copy()

    # Initialize the queue for BFS
    queue = deque([start_point])

    # Keep track of visited points
    visited = set()

    # Fill only starting char
    old_char = grid[start_point]

    # Perform BFS until the queue is empty
    while queue:
        current_point = queue.popleft()

        # Check if the current point is within the grid and has not been visited
        if is_in_grid(current_point, new_grid) and current_point not in visited:
            # Fill the current point with the new character
            new_grid[current_point] = fill_char

            # Mark the current point as visited
            visited.add(current_point)

            # Add neighbors to the queue
            neighbors = get_neighbours_dict(current_point, new_grid, diagonal=False)
            for point, value in neighbors.items():
                if value == old_char:
                    queue.extend([point])

    return new_grid


def process(tokens_line):
    current = origin
    dig_path = [origin]

    for command in tokens_line:
        for i in range(int(command[1])):
            if command[0] == 'R':
                current += one_step(Direction.E)
            elif command[0] == 'L':
                current += one_step(Direction.W)
            elif command[0] == 'U':
                current += one_step(Direction.N)
            elif command[0] == 'D':
                current += one_step(Direction.S)

            dig_path.append(current)

    n = max([point.y for point in dig_path])
    s = min([point.y for point in dig_path])
    e = max([point.x for point in dig_path])
    w = min([point.x for point in dig_path])

    nw = Point(w-1, n+1)
    se = Point(e+1, s-1)

    full_grid = empty_grid(nw, se)
    for point in dig_path:
        full_grid[point] = '#'

    # print(points_to_text(full_grid))

    outside = flood_fill(full_grid, nw, ' ')
    # print(points_to_text(outside))

    counter = 0
    for value in outside.values():
        if value != ' ':
            counter += 1
    return counter


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))

