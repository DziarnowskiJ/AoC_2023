import pandas as pd
import re
import tokenize
from io import BytesIO
from functools import reduce

with open('../inputs/real/input_day_2.txt', 'r') as file:
    lines = file.readlines()
    df = pd.DataFrame({'input': lines, 'encode': None, 'output': None})
    df['encode'] = df['input'].apply(lambda x: BytesIO(x.encode('utf-8')))

with open('../inputs/sample/sample_input_day_2.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_df = pd.DataFrame({'input': sample_lines, 'encode': None, 'output': None})
    sample_df['encode'] = sample_df['input'].apply(lambda x: BytesIO(x.encode('utf-8')))


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [(tokenize.tok_name[token.type], token.string) for token in tok
                   if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER}]
    text.seek(0)
    return name_tuples


possible = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def max_color(tokens):
    tokens = tokens[3:]
    color_dict = {}
    for index, token in enumerate(tokens):
        if token[0] != 'NUMBER':
            continue
        number = int(token[1])
        color = tokens[index + 1][1]
        if color not in color_dict or number > color_dict[color]:
            color_dict[color] = number
    return color_dict


def is_possible(dict):
    for color, val in dict.items():
        if possible[color] < val:
            return False
    return True


def get_result(row):
    functions = [tokens, max_color, is_possible]
    result = int(tokens(row)[1][1]) if reduce(lambda x, f: f(x), functions, row) else 0
    return result


sample_df['output'] = sample_df['encode'].apply(get_result)
df['output'] = df['encode'].apply(get_result)
print("Sample output:", sample_df['output'].sum())
print("Answer", df['output'].sum())