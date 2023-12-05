import tokenize
from io import BytesIO


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [
        (tokenize.tok_name[token.type],
         (int(token.string) if token.type == tokenize.NUMBER else token.string))
        for token in tok
        if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER, tokenize.NL}]
    text.seek(0)
    return name_tuples


with open('../inputs/real/input_day_5.txt', 'r') as file:
    lines = file.readlines()
    token_lines = [tokens(BytesIO(x.encode('utf-8'))) for x in lines]

with open('../inputs/sample/sample_input_day_5.txt', 'r') as file:
    sample_lines = file.readlines()
    token_sample_lines = [tokens(BytesIO(x.encode('utf-8'))) for x in sample_lines]


def get_seeds(seed_line):
    seeds = [seed[1] for seed in seed_line[2:]]
    return seeds


def get_locations(tokens_list, seeds):
    next_seeds = seeds
    seed_queue = []
    unmapped = []

    for line in [line for line in tokens_list if len(line) > 0]:
        # get line that starts with text
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
                # seed is in bounds
                if key_start <= seed <= key_end:
                    next_seeds.append(seed + val_change)
                # seed is not in bounds
                else:
                    unmapped.append(seed)
    return next_seeds + unmapped


def process(tokens_list):
    seeds = get_seeds(tokens_list[0])
    locations = get_locations(tokens_list[2:], seeds)
    result = min(locations)
    return result


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))
