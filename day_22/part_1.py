import tokenize
from io import BytesIO
from utils.geometry3D import *


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [
        (tokenize.tok_name[token.type],
         (int(token.string) if token.type == tokenize.NUMBER else token.string))
        for token in tok
        if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER, tokenize.NL}]
    text.seek(0)
    return name_tuples
    

with open('../inputs/real/input_day_22.txt', 'r') as file:
    lines = file.readlines()
    encoded_lines = [BytesIO(line.encode('utf-8')) for line in lines]
    token_lines = [tokens(encoded_line) for encoded_line in encoded_lines]

with open('../inputs/sample/sample_input_day_22.txt', 'r') as file:
    sample_lines = file.readlines()
    encoded_sample_lines = [BytesIO(line.encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]


def create_grid(tokens_line):
    grid = dict()
    blocks = dict()
    block_id = 0

    # Custom key function to extract the highest point of each set of blocks
    def last_digit_key(s):
        return s[-1]

    # Sort the list based on the highest point in set of blocks
    sorted_list = sorted(tokens_line, key=last_digit_key)

    for token in sorted_list:
        xs = [token[0][1], token[6][1]]
        ys = [token[2][1], token[8][1]]
        zs = [token[4][1], token[10][1]]

        points = []
        for x in range(min(xs), max(xs) + 1, 1):
            for y in range(min(ys), max(ys) + 1, 1):
                for z in range(min(zs), max(zs) + 1, 1):
                    points.append(Point(x, y, z))

        canFall = True
        while canFall:
            for point in points:
                if point + one_step(Direction.D) in grid.keys() or point.z <= 0:
                    canFall = False
            if canFall:
                for i in range(len(points)):
                    points[i] += one_step(Direction.D)

        for point in points:
            grid[point] = str(block_id)
        blocks[int(block_id)] = points

        block_id += 1

    return grid, blocks


def test_blocks(blocks_dict: dict[int, [Point]], grid: dict[Point, str]):
    counter = set()
    for id, blocks in blocks_dict.items():
        # check what blocks are supported but that one
        supports = set()
        for block in blocks:
            upper = block + one_step(Direction.U)
            if upper in grid.keys() and grid[upper] != str(id):
                supports.add(grid[upper])

        # check if block can be removed
        canBeRemoved = list()
        for supported in supports:
            rests_on = set()
            for supported_block in blocks_dict[int(supported)]:
                lower = supported_block + one_step(Direction.D)
                if lower in grid.keys() and grid[lower] != str(supported):
                    rests_on.add(grid[lower])
            if len(rests_on) <= 1:
                canBeRemoved.append(False)
            else:
                canBeRemoved.append(True)
        if all(canBeRemoved):
            counter.add(id)

    return counter


def process(tokens_line):
    grid, blocks = create_grid(tokens_line)
    counter = test_blocks(blocks, grid)

    return len(counter)


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))
