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
        blocks[str(block_id)] = points

        block_id += 1

    return grid, blocks


def test_blocks(blocks_dict: dict[str, [Point]], grid: dict[Point, str]):
    support_info = dict()
    non_bearing = set()
    for id, blocks in blocks_dict.items():
        # check what blocks are supported but that one
        supports = set()
        for block in blocks:
            upper = block + one_step(Direction.U)
            if upper in grid.keys() and grid[upper] != id:
                supports.add(grid[upper])

        if id not in support_info.keys():
            support_info[id] = {'supports': set(), 'supported_by': set()}
        support_info[id]['supports'] = support_info[id]['supports'].union(supports)

        # check if block can be removed
        canBeRemoved = list()
        for supported in supports:
            rests_on = set()
            for supported_block in blocks_dict[supported]:
                lower = supported_block + one_step(Direction.D)
                if lower in grid.keys() and grid[lower] != supported:
                    rests_on.add(grid[lower])
            if len(rests_on) <= 1:
                canBeRemoved.append(False)
            else:
                canBeRemoved.append(True)
            if supported not in support_info.keys():
                support_info[supported] = {'supports': set(), 'supported_by': set()}
            support_info[supported]['supported_by'] = support_info[supported]['supported_by'].union(rests_on)
        if all(canBeRemoved):
            non_bearing.add(id)

    return non_bearing, support_info


def predict_fall(block_id, support_info: dict[str, dict[str, set[str]]]):
    would_fall = {block_id}
    blocks_to_test = [block_id]
    while len(blocks_to_test) > 0:
        test = blocks_to_test.pop(0)
        for will_fall in support_info[test]['supports']:
            if len(support_info[will_fall]['supported_by'].difference(would_fall)) == 0:
                would_fall.add(will_fall)
                blocks_to_test.append(will_fall)
    would_fall.remove(block_id)

    return would_fall

def process(tokens_line):
    grid, blocks = create_grid(tokens_line)
    non_bearing, support_info = test_blocks(blocks, grid)
    bearing = set(blocks.keys()).difference(non_bearing)

    fallen = 0
    for block in bearing:
        fallen += len(predict_fall(block, support_info))

    return fallen


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))
