from utils.geometry import *
import heapq
from typing import Callable

with open('../inputs/real/input_day_23.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_23.txt', 'r') as file:
    sample_lines = file.readlines()


# def dijkstra(start: Point, goal: Point, grid: dict[Point, str],
#              is_valid_move: Callable[[Point, str, Point, str], bool], diagonal: bool = False) -> (list[Point], set[Point]):
#     priority_queue = [(0, start, [start])]
#     visited = set()
#
#     while priority_queue:
#         current_distance, current, path = heapq.heappop(priority_queue)
#
#         if current == goal:
#             return path, visited
#
#         if current in visited:
#             continue
#
#         visited.add(current)
#
#         neighbors = get_neighbours_dict(current, grid, diagonal=diagonal)
#         for neighbor, value in neighbors.items():
#             if neighbor not in visited and is_valid_move(current, grid[current], neighbor, value):
#                 new_distance = current_distance - 1
#                 heapq.heappush(priority_queue, (new_distance, neighbor, path + [neighbor]))
#
#     # If no path is found
#     return [], visited

def find_paths(start: Point, goal: Point, grid: dict[Point, str]):
    queue = [(start, [start], set())]

    all_paths = list()
    while len(queue) > 0:
        current, path, visited = queue.pop(0)
        visited = visited.union({current})

        if current == goal:
            all_paths.append(path)
            continue

        neighbors = get_neighbours_dict(current, grid, diagonal=False)
        for neighbor, value in neighbors.items():
            if neighbor not in visited and is_valid(current, grid[current], neighbor, value):
                queue.append((neighbor, path + [neighbor], visited))

    return all_paths


def is_valid(curr: Point, curr_val: str, next: Point, next_val: str):

    if next_val == '#':
        return False

    if curr_val == '>' and curr + one_step(Direction.E) == next:
        return True
    elif curr_val == '<' and curr + one_step(Direction.W) == next:
        return True
    elif curr_val == 'v' and curr + one_step(Direction.S) == next:
        return True
    elif curr_val == '^' and curr + one_step(Direction.N) == next:
        return True

    if next_val == '>' and curr + one_step(Direction.E) == next:
        return True
    elif next_val == '<' and curr + one_step(Direction.W) == next:
        return True
    elif next_val == 'v' and curr + one_step(Direction.S) == next:
        return True
    elif next_val == '^' and curr + one_step(Direction.N) == next:
        return True

    if curr_val == '.' and next_val == '.':
        return True

    return False


def process(tokens_line):
    grid = grid_dict(''.join(tokens_line))
    nw, se = grid_dimensions(grid)
    paths = find_paths(nw + one_step(Direction.E), se + one_step(Direction.W), grid)

    # print('Found', len(paths), 'paths')
    # for path in paths:
    #     print(path)

    length = max([len(path) for path in paths])
    return length - 1


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
