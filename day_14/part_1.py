from utils.geometry import *

with open('../inputs/real/input_day_14.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_14.txt', 'r') as file:
    sample_lines = file.readlines()


def process(input_lines):
    input_lines = ''.join(input_lines)
    grid = grid_dict(input_lines)
    nw, se = grid_dimensions(grid)
    direction = Direction.N
    for point in grid_position('O', grid):
        grid[point] = '.'
        new_point = point + one_step(direction)
        while nw.y >= new_point.y and grid[new_point] not in ['O', '#']:
            point = new_point
            new_point = point + one_step(direction)
        grid[point] = 'O'

    resp = 0
    for point in grid_position('O', grid):
        resp += (se.y - 1) * -1 + point.y

    print(points_to_text(grid))
    return resp


print("Sample output:", process(sample_lines))
print("Answer", process(lines))
