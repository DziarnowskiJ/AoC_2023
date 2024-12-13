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
    

with open('../inputs/real/input_day_19.txt', 'r') as file:
    lines = file.readlines()
    encoded_lines = [BytesIO(line.encode('utf-8')) for line in lines]
    token_lines = [tokens(encoded_line) for encoded_line in encoded_lines]

with open('../inputs/sample/sample_input_day_19.txt', 'r') as file:
    sample_lines = file.readlines()
    encoded_sample_lines = [BytesIO(line.encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]


def split_input(tokens: list):
    functions = dict()  # dict of functions
    parts = []          # list of dicts

    divider = tokens.index([])

    for token in tokens[:divider]:
        fnc_string = 'lambda dic: '
        fnc_string += f"'{token[6][1]}' if (dic['{token[2][1]}'] {token[3][1]} {token[4][1]})"
        for pt in range(8, len(token[8:-2]) + 6, 6):
            fnc_string += f" else '{token[pt+4][1]}' if (dic['{token[pt][1]}'] {token[pt+1][1]} {token[pt+2][1]})"
        fnc_string += f" else '{token[-2][1]}'"
        functions[token[0][1]] = eval(fnc_string)

    for token in tokens[divider + 1:]:
        part_dict = dict()
        for pt in range(1, len(token[1:-1]), 4):
            part_dict[token[pt][1]] = token[pt+2][1]
        parts.append(part_dict)

    return functions, parts


def get_rating(part):
    val = 0
    for value in part.values():
        val += value
    return val
    
    
def process(tokens_line):
    functions, parts = split_input(tokens_line)

    val = 0
    for part in parts:
        res = functions['in'](part)
        while res not in ['A', 'R']:
            res = functions[res](part)
        if res == 'A':
            val += get_rating(part)

    return val


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))
