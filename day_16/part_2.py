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


def process_one(text, start, start_direction):
    grid = grid_dict(text)

    history = {start}

    traversed_grid = grid.copy()
    traversed_grid[start] = '#'

    paths = [(start, start_direction)]
    while len(paths) > 0:
        current = paths.pop(0)
        next = transition((current[0], grid[current[0]]), current[1])
        for nx in next:
            if is_in_grid(nx[0], grid) and nx not in history:
                history.add(nx)
                paths.append(nx)
                traversed_grid[nx[0]] = '#'

    return len(grid_position('#', traversed_grid))


def process(text_lines):
    vals = []
    text = ''.join(text_lines)
    grid = grid_dict(text)
    nw, se = grid_dimensions(grid)
    for i in range(nw.y, se.y, -1):
        lhs = nw.x
        rhs = se.x
        # print('lhs', Point(lhs, i), Direction.E)
        # print('rhs', Point(rhs, i), Direction.W)
        lhs_v = process_one(text, Point(lhs, i), Direction.E)
        rhs_v = process_one(text, Point(rhs, i), Direction.W)
        # print('lhs', lhs_v, 'rhs', rhs_v)
        vals.append(lhs_v)
        vals.append(rhs_v)
        # print(max(vals))
    for i in range(nw.x, se.x):
        t = nw.y
        b = se.y
        # print('top', Point(i, t), Direction.S)
        # print('btm', Point(i, b), Direction.N)
        vals.append(process_one(text, Point(i, t), Direction.S))
        vals.append(process_one(text, Point(i, b), Direction.N))
        # print(max(vals))
    return max(vals)


print("Sample output:", process(sample_lines))
print("Answer", process(lines))

# > 6855