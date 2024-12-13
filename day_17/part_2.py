from utils.geometry import *
from queue import PriorityQueue

with open('../inputs/real/input_day_17.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_17.txt', 'r') as file:
    sample_lines = file.readlines()


def offset(direction):
    if direction == 'V':
        return [one_step(Direction.E), one_step(Direction.W)]
    elif direction == 'H':
        return [one_step(Direction.N), one_step(Direction.S)]


def min_heat_loss(grid):
    visited = set()
    queue = PriorityQueue()

    def add_moves(heat_loss, current, direction):
        for offset_node in offset(direction):
            heat_loss2 = heat_loss
            for i in range(1, 11):  # max steps
                point = current + offset_node.mul(i)
                if is_in_grid(point, grid):
                    heat_loss2 += int(grid[point])
                    if i >= 4:  # min steps
                        queue.put((heat_loss2, point, "V" if direction == "H" else "H"))

    queue.put((0, origin, "H"))
    queue.put((0, origin, "V"))

    end = grid_dimensions(grid)[1]
    while not queue.empty():
        heat_loss, point, direction = queue.get()
        if point == end:
            return heat_loss

        combination = (point, direction)
        if combination not in visited:
            visited.add(combination)
            add_moves(heat_loss, point, direction)


def process(text_lines):
    text = ''.join(text_lines)
    grid = grid_dict(text)
    resp = min_heat_loss(grid)
    return resp


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
