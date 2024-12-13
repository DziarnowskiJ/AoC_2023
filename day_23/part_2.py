from utils.geometry import *
import sys
sys.setrecursionlimit(1000000)

with open('../inputs/real/input_day_23.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_23.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    grid = grid_dict('\n'.join(lines).replace('>', '.')
                     .replace('<', '.')
                     .replace('^', '.')
                     .replace('v', '.'))
    return grid


def get_optimised_grid(path_splits, grid):
    optimised_grid = dict()
    for split in path_splits:
        to_check = [split]
        seen = {split}
        dist = 0

        while to_check:
            queue = []
            dist += 1

            for point in to_check:
                for neighbour in get_neighbours_dict(point, grid, False).keys():
                    if neighbour not in seen:
                        if neighbour in path_splits:
                            if split in optimised_grid:
                                optimised_grid[split].append((dist, neighbour))
                            else:
                                optimised_grid[split] = [(dist, neighbour)]
                        else:
                            queue.append(neighbour)
                        seen.add(neighbour)
            to_check = queue
    return optimised_grid


def process(lines):
    grid = get_grid(lines)
    path_grid = {k: v for k, v in grid.items() if v == '.'}

    nw, se = grid_dimensions(grid)
    start = nw + one_step(Direction.E)
    end = se + one_step(Direction.W)

    path_splits = {start, end}
    for point in path_grid:
        if len(get_neighbours(point, path_grid, False)) > 2:
            path_splits.add(point)

    optimised_grid = get_optimised_grid(path_splits, path_grid)

    best = dfs(start, end, set(), 0, optimised_grid, 0)

    return best


def dfs(start, end, paths, total_dist, optimised_grid, best):
    if start == end:
        best = max(best, total_dist)
    for dist, point in optimised_grid[start]:
        if point not in paths:
            paths.add(point)
            best = dfs(point, end, paths, total_dist + dist, optimised_grid, best)
            paths.remove(point)
    return best


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
