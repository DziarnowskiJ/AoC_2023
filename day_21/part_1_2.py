from utils.geometry import *
from itertools import chain

with open('../inputs/real/input_day_21.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_21.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines, steps):
    grid = grid_dict('\n'.join(lines))
    grid = {plot: grid[plot] for plot in grid.keys() if grid[plot] != '#'}

    possible_locations = {grid_position('S', grid)[0]}
    for i in range(steps):
        possible_locations = set(
            chain.from_iterable(
                [get_neighbours_dict(loc, grid, False).keys() for loc in possible_locations]
            )
        )

    return len(possible_locations)


print("Sample output:", process(sample_lines, 6))
print("Answer:", process(input_lines, 64))
