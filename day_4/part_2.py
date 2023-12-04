import pandas as pd
import tokenize
from io import BytesIO
from functools import reduce

with open('../inputs/real/input_day_4.txt', 'r') as file:
    lines = file.readlines()
    df = pd.DataFrame({'input': lines, 'encode': None, 'wins': None, 'output': 1})
    df['encode'] = df['input'].apply(lambda x: BytesIO(x.encode('utf-8')))

with open('../inputs/sample/sample_input_day_4.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_df = pd.DataFrame({'input': sample_lines, 'encode': None, 'wins': None, 'output': 1})
    sample_df['encode'] = sample_df['input'].apply(lambda x: BytesIO(x.encode('utf-8')))


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [(tokenize.tok_name[token.type], token.string) for token in tok
                   if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER}]
    text.seek(0)
    return name_tuples


def number_of_winnings(list):
    divider_pos = [index for index, val in enumerate(list) if val[1] == '|'][0]
    winning_numb = [number[1] for number in list[3:divider_pos]]
    my_numbers = [number[1] for number in list[(divider_pos + 1):]]
    return sum([1 for number in my_numbers if number in winning_numb])


def get_result(row):
    functions = [tokens, number_of_winnings]
    result = reduce(lambda x, f: f(x), functions, row)
    return result


def get_counts(df):
    for index, row in enumerate(df['wins'].values):
        for i in range(1, row + 1):
            df.at[index + i, 'output'] += df.at[index, 'output']


sample_df['wins'] = sample_df['encode'].apply(get_result)
df['wins'] = df['encode'].apply(get_result)

get_counts(df)
get_counts(sample_df)

print("Sample output:", sample_df['output'].sum())
print("Answer", df['output'].sum())
