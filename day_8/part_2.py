import math
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

with open('../inputs/sample/sample_input_day_8_2.txt', 'r') as file:
    # DUE TO HOW THIS TOKENIZER WORKS, I MANUALLY REPLACED DIGITS WITH OTHER LETTERS
    # otherwise it would split 11A into two tokens (11, A) instead of 1 (11A) etc.
    sample_lines = file.readlines()
    encoded_sample_lines = [BytesIO(line.encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]


def tokens_to_dict(tok_lines):
    m_map = dict()
    for token_line in tok_lines[2:]:
        m_map[token_line[0][1]] = (token_line[3][1], token_line[5][1])
    return m_map


def find_path_AZ(m_map, lrs, s_pos):
    lrs = [*lrs[0][1]]
    orig_lrs = lrs.copy()

    position = s_pos
    counter = 0
    while not position.endswith('Z'):
        counter += 1
        if len(lrs) == 0:
            lrs = orig_lrs.copy()
        cur_lrs = lrs.pop(0)
        position = m_map[position][0 if cur_lrs == 'L' else 1]
    return counter
    

def lcm(a, b):
    return int(a * b / math.gcd(a, b))


def lcm_arr(arr):
    val = arr[0]
    for v in arr:
        val = lcm(val, v)
    return val


def process(tokens_line):
    map = tokens_to_dict(tokens_line)
    A_to_Z = []
    for start in [x for x in map if x.endswith('A')]:
         A_to_Z.append(find_path_AZ(map, tokens_line[0], start))

    return lcm_arr(A_to_Z)


print("Sample output:", process(token_sample_lines))
print("Answer", process(token_lines))

