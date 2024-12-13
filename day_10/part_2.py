from utils.geometry import *
from utils.flood import flood_fill

with open('../inputs/real/input_day_10.txt', 'r') as file:
    lines = file.read()

with open('../inputs/sample/sample_input_day_10_5.txt', 'r') as file:
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
    curr_point = grid_position('S', grid)[0]
    prev_step = curr_point + one_step(Direction.E)
    next_step = get_next_step(grid[curr_point], curr_point, prev_step)
    next_val = grid[next_step]
    path = [curr_point]
    while next_val != 'S':
        prev_step = curr_point
        curr_point = next_step

        next_step = get_next_step(next_val, curr_point, prev_step)
        next_val = grid[next_step]

        path.append(curr_point)
    return path


def expand_point(p, char=None):
    big_point = dict()
    if char == '.':
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '.', Point(p.x * 3 + 1, p.y * 3 - 0): '.', Point(p.x * 3 + 2, p.y * 3 - 0): '.',
            Point(p.x * 3, p.y * 3 - 1): '.', Point(p.x * 3 + 1, p.y * 3 - 1): '.', Point(p.x * 3 + 2, p.y * 3 - 1): '.',
            Point(p.x * 3, p.y * 3 - 2): '.', Point(p.x * 3 + 1, p.y * 3 - 2): '.', Point(p.x * 3 + 2, p.y * 3 - 2): '.',
        }
    elif char == 'F':
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '#', Point(p.x * 3 + 1, p.y * 3 - 0): '#', Point(p.x * 3 + 2, p.y * 3 - 0): '#',
            Point(p.x * 3, p.y * 3 - 1): '#', Point(p.x * 3 + 1, p.y * 3 - 1): 'F', Point(p.x * 3 + 2, p.y * 3 - 1): '-',
            Point(p.x * 3, p.y * 3 - 2): '#', Point(p.x * 3 + 1, p.y * 3 - 2): '|', Point(p.x * 3 + 2, p.y * 3 - 2): '#',
        }
    elif char == 'S':  # According to input S works like F
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '#', Point(p.x * 3 + 1, p.y * 3 - 0): '#', Point(p.x * 3 + 2, p.y * 3 - 0): '#',
            Point(p.x * 3, p.y * 3 - 1): '#', Point(p.x * 3 + 1, p.y * 3 - 1): 'S', Point(p.x * 3 + 2, p.y * 3 - 1): '-',
            Point(p.x * 3, p.y * 3 - 2): '#', Point(p.x * 3 + 1, p.y * 3 - 2): '|', Point(p.x * 3 + 2, p.y * 3 - 2): '#',
        }
    elif char == 'J':
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '#', Point(p.x * 3 + 1, p.y * 3 - 0): '|', Point(p.x * 3 + 2, p.y * 3 - 0): '#',
            Point(p.x * 3, p.y * 3 - 1): '-', Point(p.x * 3 + 1, p.y * 3 - 1): 'J', Point(p.x * 3 + 2, p.y * 3 - 1): '#',
            Point(p.x * 3, p.y * 3 - 2): '#', Point(p.x * 3 + 1, p.y * 3 - 2): '#', Point(p.x * 3 + 2, p.y * 3 - 2): '#',
        }
    elif char == 'L':
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '#', Point(p.x * 3 + 1, p.y * 3 - 0): '|', Point(p.x * 3 + 2, p.y * 3 - 0): '#',
            Point(p.x * 3, p.y * 3 - 1): '#', Point(p.x * 3 + 1, p.y * 3 - 1): 'L', Point(p.x * 3 + 2, p.y * 3 - 1): '-',
            Point(p.x * 3, p.y * 3 - 2): '#', Point(p.x * 3 + 1, p.y * 3 - 2): '#', Point(p.x * 3 + 2, p.y * 3 - 2): '#',
        }
    elif char == '7':
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '#', Point(p.x * 3 + 1, p.y * 3 - 0): '#', Point(p.x * 3 + 2, p.y * 3 - 0): '#',
            Point(p.x * 3, p.y * 3 - 1): '-', Point(p.x * 3 + 1, p.y * 3 - 1): '7', Point(p.x * 3 + 2, p.y * 3 - 1): '#',
            Point(p.x * 3, p.y * 3 - 2): '#', Point(p.x * 3 + 1, p.y * 3 - 2): '|', Point(p.x * 3 + 2, p.y * 3 - 2): '#',
        }
    elif char == '|':
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '#', Point(p.x * 3 + 1, p.y * 3 - 0): '|', Point(p.x * 3 + 2, p.y * 3 - 0): '#',
            Point(p.x * 3, p.y * 3 - 1): '#', Point(p.x * 3 + 1, p.y * 3 - 1): '|', Point(p.x * 3 + 2, p.y * 3 - 1): '#',
            Point(p.x * 3, p.y * 3 - 2): '#', Point(p.x * 3 + 1, p.y * 3 - 2): '|', Point(p.x * 3 + 2, p.y * 3 - 2): '#',
        }
    elif char == '-':
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '#', Point(p.x * 3 + 1, p.y * 3 - 0): '#', Point(p.x * 3 + 2, p.y * 3 - 0): '#',
            Point(p.x * 3, p.y * 3 - 1): '-', Point(p.x * 3 + 1, p.y * 3 - 1): '-', Point(p.x * 3 + 2, p.y * 3 - 1): '-',
            Point(p.x * 3, p.y * 3 - 2): '#', Point(p.x * 3 + 1, p.y * 3 - 2): '#', Point(p.x * 3 + 2, p.y * 3 - 2): '#',
        }
    elif char is None:
        big_point = {
            Point(p.x * 3, p.y * 3 - 0): '', Point(p.x * 3 + 1, p.y * 3 - 0): '', Point(p.x * 3 + 2, p.y * 3 - 0): '',
            Point(p.x * 3, p.y * 3 - 1): '', Point(p.x * 3 + 1, p.y * 3 - 1): '', Point(p.x * 3 + 2, p.y * 3 - 1): '',
            Point(p.x * 3, p.y * 3 - 2): '', Point(p.x * 3 + 1, p.y * 3 - 2): '', Point(p.x * 3 + 2, p.y * 3 - 2): '',
        }
    return big_point

def stretch_grid(grid):

    new_grid = dict()
    for k, v in grid.items():
        new_grid.update(expand_point(k, v))

    return new_grid


def process(input_text):
    grid = grid_dict(input_text, Direction.NE)

    # Get original loop path
    small_path = traverse_grid(grid)

    # Expand the grid such that each point becomes 9 points
    big_grid = stretch_grid(grid)

    # Get loop on expanded grid
    big_path = traverse_grid(big_grid)

    # Get expanded grid without path
    grid_no_path = big_grid.copy()
    for key in big_path:
        grid_no_path.pop(key, None)

    # Flood the expanded grid from Point(0 0), to check which elements are outside the loop
    grid_flooded = flood_fill(grid_no_path, Point(0, 0), 'x')

    # Remove elements that are outside the loop
    grid_no_outside = {k: v for k, v in grid_flooded.items() if v != 'x'}

    # Since each point of the path was also expanded but only actual path was removed,
    # surroundings of the path also need to be removed
    grid_no_path_remains = grid_no_outside.copy()
    for p in small_path:
        for bp in expand_point(p).keys():
            grid_no_path_remains.pop(bp, None)

    # Divide remaining points by 9 to get number of original points
    return len(grid_no_path_remains) // 9


print("Sample output:", process(sample_lines))
print("Answer", process(lines))
