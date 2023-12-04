import pandas as pd
import tokenize
from io import BytesIO
from functools import reduce

with open('../inputs/real/input_day_4.txt', 'r') as file:
    lines = file.readlines()
    df = pd.DataFrame({'input': lines, 'encode': None, 'output': None})
    df['encode'] = df['input'].apply(lambda x: BytesIO(x.encode('utf-8')))

with open('../inputs/sample/sample_input_day_4.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_df = pd.DataFrame({'input': sample_lines, 'encode': None, 'output': None})
    sample_df['encode'] = sample_df['input'].apply(lambda x: BytesIO(x.encode('utf-8')))    


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [(tokenize.tok_name[token.type], token.string) for token in tok
                   if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER}]
    text.seek(0)
    return name_tuples
    
    
def pow_2(x):
    return 2 ** (x-1) if x > 0 else 0


def number_of_winnings(list):
    divider_pos = [index for index, val in enumerate(list) if val[1] == '|'][0]
    winning_numb = [number[1] for number in list[3:divider_pos]]
    my_numb = [number[1] for number in list[(divider_pos + 1):]]
    return sum([1 for numb in my_numb if numb in winning_numb])


def get_result(row):
    functions = [tokens, number_of_winnings, pow_2]
    result = reduce(lambda x, f: f(x), functions, row)
    return result


sample_df['output'] = sample_df['encode'].apply(get_result)
df['output'] = df['encode'].apply(get_result)
print("Sample output:", sample_df['output'].sum())
print("Answer", df['output'].sum())
