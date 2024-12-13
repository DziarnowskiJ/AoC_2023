from utils.geometry import *

with open('../inputs/real/input_day_11.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_11.txt', 'r') as file:
    sample_lines = file.readlines()

FACTOR = 1_000_000 - 1


def min_dists(points, x_ranges, y_ranges):
    min_dists = []
    for index, point in enumerate(points):
        for i in range(index + 1, len(points), 1):
            inc = 0
            for xs in x_ranges:
                if (point.x > xs > points[i].x) or (point.x < xs < points[i].x):
                    inc += FACTOR
            for ys in y_ranges:
                if (point.y > -ys > points[i].y) or (point.y < -ys < points[i].y):
                    inc += FACTOR

            standard_dist = distance(point, points[i]) + inc
            min_dists.append(standard_dist)
    return min_dists


def expand(text_grid):
    empty_ranges_x = [index for index, row in enumerate(text_grid) if '#' not in row]
    empty_ranges_y = []
    for index in range(len(text_grid[0]) - 1):
        if '#' not in [row[index] for row in text_grid]:
            empty_ranges_y.append(index)
    return empty_ranges_x, empty_ranges_y


def process(text_lines):
    ranges_y, ranges_x = expand(text_lines)
    new_text = ''.join(text_lines)
    grid = grid_dict(new_text)
    dists = min_dists(grid_position('#', grid), ranges_x, ranges_y)
    return sum(dists)


print("Sample output:", process(sample_lines))
print("Answer", process(lines))