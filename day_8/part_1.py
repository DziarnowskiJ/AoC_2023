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
    

with open('../inputs/real/input_day_8.txt', 'r') as file:
    lines = file.readlines()
    encoded_lines = [BytesIO(line.encode('utf-8')) for line in lines]
    token_lines = [tokens(encoded_line) for encoded_line in encoded_lines]

with open('../inputs/sample/sample_input_day_8_1.txt', 'r') as file:
    sample_lines = file.readlines()
    encoded_sample_lines = [BytesIO(line.encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]


def tokens_to_dict(toks):
    m_map = dict()
    for token_line in toks[2:]:
        m_map[token_line[0][1]] = (token_line[3][1], token_line[5][1])
    return m_map


def find_path(movement_map, lrs):
    lrs = [*lrs[0][1]]
    orig_lrs = lrs.copy()

    position = 'AAA'
    counter = 0
    while position != 'ZZZ':
        counter += 1
        if len(lrs) == 0:
            lrs = orig_lrs.copy()
        cur_lrs = lrs.pop(0)
        position = movement_map[position][0 if cur_lrs == 'L' else 1]
    return counter
    

def process(tokens_line):
    movement_map = tokens_to_dict(tokens_line)
    result = find_path(movement_map, tokens_line[0])
    return result


print("Sample output:", process(token_sample_lines))
print("Answer", process(token_lines))

