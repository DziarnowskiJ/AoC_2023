import tokenize
from io import BytesIO


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [(tokenize.tok_name[token.type], (int(token.string) if token.type == tokenize.NUMBER else token.string)) for token in tok
                   if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER, tokenize.NL}]
    text.seek(0)
    return name_tuples


with open('../inputs/real/input_day_5.txt', 'r') as file:
    lines = file.readlines()
    token_lines = [tokens(BytesIO(x.encode('utf-8'))) for x in lines]

with open('../inputs/sample/sample_input_day_5.txt', 'r') as file:
    sample_lines = file.readlines()
    token_sample_lines = [tokens(BytesIO(x.encode('utf-8'))) for x in sample_lines]


def get_seed_ranges(seed_line):
    seed_vals = seed_line[2:]
    seed_range = []
    for i in range(0, len(seed_vals), 2):
        seed_range.append((seed_vals[i][1], seed_vals[i][1] + seed_vals[i + 1][1] - 1))
    return seed_range


def get_locations(tokens_list, seeds):
    next_seeds = seeds
    seed_queue = []
    unmapped = []

    for line in [line for line in tokens_list if len(line) > 0]:
        if line[0][0] == 'NAME':
            # unnecessary to get name but was useful for testing
            name = line[0][1] + line[1][1] + line[2][1] + line[3][1] + line[4][1]
            seed_queue = next_seeds
            next_seeds = []
        else:
            seed_queue.extend(unmapped)
            unmapped = []

            # line parameters
            val = line[0][1]
            key_start = line[1][1]
            increment = line[2][1] - 1
            key_end = key_start + increment
            val_change = val - key_start

            while len(seed_queue) > 0:
                seed = seed_queue.pop(0)
                # seed_range completely in bounds
                if key_start <= seed[0] <= key_end and key_start <= seed[1] <= key_end:
                    next_seeds.append((seed[0] + val_change, seed[1] + val_change))
                # only first part of seed_range in bounds
                elif key_start <= seed[0] <= key_end < seed[1]:
                    next_seeds.append((seed[0] + val_change, key_end + val_change))
                    unmapped.append((key_end + 1, seed[1]))
                # only second part of seed_range in bounds
                elif key_end >= seed[1] >= key_start > seed[0]:
                    unmapped.append((seed[0], key_start - 1))
                    next_seeds.append((key_start + val_change, seed[1] + val_change))
                # bounds are included in seed_range
                elif key_start > seed[1] and key_end < seed[0]:
                    unmapped.append((seed[0], key_start - 1))
                    next_seeds.append((key_start + val_change, key_end + val_change))
                    unmapped.append((key_end + 1, seed[1]))
                # there is no overlap between bounds and seed_ranges
                elif key_start > seed[1] or key_end < seed[0]:
                    unmapped.append(seed)
    return next_seeds + unmapped


def smallest(ranges):
    return min([x[0] for x in ranges])


def process(tokens_list):
    seed_ranges = get_seed_ranges(tokens_list[0])
    new_ranges = get_locations(tokens_list[2:], seed_ranges)
    result = smallest(new_ranges)
    return result


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))
