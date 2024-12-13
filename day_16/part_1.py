from utils.geometry import *

with open('../inputs/real/input_day_16.txt', 'r') as file:
    lines = file.readlines()

with open('../inputs/sample/sample_input_day_16.txt', 'r') as file:
    sample_lines = file.readlines()


def transition(check: (Point, str), dir: Direction) -> [(Point, Direction)]:
    node = check[0]
    char = check[1]
    if char == '.':
        return [(node + one_step(dir), dir)]
    elif char == '/':
        if dir == Direction.N:
            return [(node + one_step(Direction.E), Direction.E)]
        elif dir == Direction.E:
            return [(node + one_step(Direction.N), Direction.N)]
        elif dir == Direction.S:
            return [(node + one_step(Direction.W), Direction.W)]
        elif dir == Direction.W:
            return [(node + one_step(Direction.S), Direction.S)]
    elif char == '\\':
        if dir == Direction.N:
            return [(node + one_step(Direction.W), Direction.W)]
        elif dir == Direction.E:
            return [(node + one_step(Direction.S), Direction.S)]
        elif dir == Direction.S:
            return [(node + one_step(Direction.E), Direction.E)]
        elif dir == Direction.W:
            return [(node + one_step(Direction.N), Direction.N)]
    elif char == '|':
        if dir in [Direction.N, Direction.S]:
            return [(node + one_step(dir), dir)]
        elif dir in [Direction.E, Direction.W]:
            return [(node + one_step(Direction.N), Direction.N),
                    (node + one_step(Direction.S), Direction.S)]
    elif char == '-':
        if dir in [Direction.E, Direction.W]:
            return [(node + one_step(dir), dir)]
        elif dir in [Direction.N, Direction.S]:
            return [(node + one_step(Direction.E), Direction.E),
                    (node + one_step(Direction.W), Direction.W)]

    
def process(text_lines):
    text = ''.join(text_lines)
    grid = grid_dict(text)

    start = (Point(0, -4), Direction.E)
    history = {start}

    traversed_grid = grid.copy()
    traversed_grid[start[0]] = '#'

    paths = [start]
    while len(paths) > 0:
        current = paths.pop(0)
        next = transition((current[0], grid[current[0]]), current[1])
        for nx in next:
            if is_in_grid(nx[0], grid) and nx not in history:
                history.add(nx)
                paths.append(nx)
                traversed_grid[nx[0]] = '#'

    print(points_to_text(traversed_grid))
    return len(grid_position('#', traversed_grid))


print("Sample output:", process(sample_lines))
# print("Answer", process(lines))

