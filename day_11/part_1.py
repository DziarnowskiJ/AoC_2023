from utils.geometry import *

with open('../inputs/real/input_day_11.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_11.txt', 'r') as file:
    sample_lines = file.readlines()


def min_dists(points):
    min_dists = []
    for index, point in enumerate(points):
        for i in range(index + 1, len(points), 1):
            min_dists.append(distance(point, points[i]))
    return min_dists


def expand(text_grid):
    # expand vertically (add rows)
    skip = False
    for index, line in enumerate(text_grid):
        if skip:
            skip = False
            continue
        if '#' not in line:
            text_grid.insert(index, ('.' * (len(line) - 1)) + '\n')
            skip = True

    # expand horizontally (add cols)
    skip = False
    for row_index in range(len(text_grid[0])):
        if skip:
            skip = False
            continue
        if '#' not in [row[row_index] for row in text_grid]:
            for line_ind, line in enumerate(text_grid):
                text_grid[line_ind] = line[:row_index] + '.' + line[row_index:]
            skip = True
    return text_grid

    
def process(text_lines):
    text_grid_exp = expand(text_lines)
    new_text = ''.join(text_grid_exp)
    grid = grid_dict(new_text)
    dists = min_dists(grid_position('#', grid))
    return sum(dists)


print("Sample output:", process(sample_lines))
print("Answer", process(lines))

