from utils.geometry import *

with open('../inputs/real/input_day_14.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_14.txt', 'r') as file:
    sample_lines = file.readlines()


def tilt(grid, grid_bounds, direction):
    nw, se = grid_bounds
    if direction == Direction.E or direction == Direction.S:
        points = reversed(grid_position('O', grid))
    else:
        points = grid_position('O', grid)
    for point in points:
        grid[point] = '.'
        new_point = point + one_step(direction)
        while nw.y >= new_point.y >= se.y and nw.x <= new_point.x <= se.x and grid[new_point] not in ['O', '#']:
            point = new_point
            new_point = point + one_step(direction)
        grid[point] = 'O'

    return grid


def process(input_lines):
    input_lines = ''.join(input_lines)
    grid = grid_dict(input_lines)
    nw, se = grid_dimensions(grid)
    directions = [Direction.N, Direction.W, Direction.S, Direction.E]

    steps = 0
    hist = dict()
    text_grid = points_to_text(grid)
    while text_grid not in hist.keys():
        hist[text_grid] = steps
        steps += 1
        for direction in directions:
            grid = tilt(grid, (nw, se), direction)
        text_grid = points_to_text(grid)

    index = hist[text_grid]
    show = (1_000_000_000 - index) % (steps - index) + index
    resp = 0
    shown_grid = [key for key, val in hist.items() if val == show][0]
    for point in grid_position('O', grid_dict(shown_grid)):
        resp += (se.y - 1) * -1 + point.y

    return resp


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
