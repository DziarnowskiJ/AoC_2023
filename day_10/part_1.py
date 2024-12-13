from utils.geometry import *
import utils.geometry as geo

with open('../inputs/real/input_day_10.txt', 'r') as file:
    lines = file.read()

with open('../inputs/sample/sample_input_day_10.txt', 'r') as file:
    sample_lines = file.read()

valid_moves = {
    'F': [(one_step(Direction.S)), (one_step(Direction.E))],
    'S': [(one_step(Direction.S)), (one_step(Direction.E))],  # According to input S works like F
    'J': [(one_step(Direction.N)), (one_step(Direction.W))],
    'L': [(one_step(Direction.N)), (one_step(Direction.E))],
    '7': [(one_step(Direction.S)), (one_step(Direction.W))],
    '|': [(one_step(Direction.N)), (one_step(Direction.S))],
    '-': [(one_step(Direction.W)), (one_step(Direction.E))]
}

def get_next_step(val, point, prev_point):
    possible_positions = [point + valid_moves[val][0], point + valid_moves[val][1]]
    prev_index = possible_positions.index(prev_point)
    return possible_positions[1] if prev_index == 0 else possible_positions[0]


def traverse_grid(grid):
    steps = 0
    curr_point = grid_position('S', grid)[0]
    prev_step = curr_point + one_step(Direction.E)
    next_step = get_next_step(grid[curr_point], curr_point, prev_step)
    next_val = grid[next_step]
    while next_val != 'S':
        prev_step = curr_point
        curr_point = next_step

        next_step = get_next_step(next_val, curr_point, prev_step)
        next_val = grid[next_step]
        steps += 1
    return steps


def process(input_text):
    grid_dict = geo.grid_dict(input_text, Direction.NE)
    step_count = traverse_grid(grid_dict)
    return int((step_count + 1) / 2)


print("Sample output:", process(sample_lines))
print("Answer", process(lines))
