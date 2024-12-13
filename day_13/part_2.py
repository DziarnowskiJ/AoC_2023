import numpy as np

def tokens(text):
    resp = []
    pattern = []
    for line in text:
        line = line.strip()
        if len(line) != 0:
            pattern.append(line)
        else:
            resp.append(pattern)
            pattern = []
    resp.append(pattern)
    return resp


with open('../inputs/real/input_day_13.txt', 'r') as file:
    lines = file.readlines()
    token_lines = tokens(lines)

with open('../inputs/sample/sample_input_day_13.txt', 'r') as file:
    sample_lines = file.readlines()
    token_sample_lines = tokens(sample_lines)


def find_horiz_match(lines):
    h = 0
    for index in range(len(lines)):
        min_index = min(index, len(lines) - index)
        orig = lines[index:index + min_index]
        rev = list(reversed((lines[index - min_index:index])))
        # print(orig)
        # print(rev)

        matching = 0
        for i in range(len(orig)):
            for j in range(len(orig[i])):
                if orig[i][j] == rev[i][j]:
                    matching += 1
        # matching =  np.count_nonzero(orig == ref)
        # print(matching)
        if matching == min_index * len(lines[0]) - 1:
            h += index
    return h


def find_vert_match(lines):
    lines = list(map(list, zip(*lines)))
    resp = find_horiz_match(lines)
    return resp


def process(tokens_line):
    horiz = [find_horiz_match(patt) for patt in tokens_line]
    vert = [find_vert_match(patt) for patt in tokens_line]
    h_count = sum(horiz)
    v_count = sum(vert)
    return 100 * h_count + v_count


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))
