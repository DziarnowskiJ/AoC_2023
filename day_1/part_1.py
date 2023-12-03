import pandas as pd
import re

with open('../inputs/real/input_day_1.txt', 'r') as file:
    lines = file.readlines()
    df = pd.DataFrame({'input': lines, 'output': None})

with open('../inputs/sample/sample_input_day_1.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_df = pd.DataFrame({'input': sample_lines, 'output': None})


def get_digits(text):
    pattern = re.compile(r'\d')
    digits = pattern.findall(text)

    if len(digits) > 0:
        return int(digits[0] + '' + digits[-1])
    else:
        return 0


def answer(text):
    return get_digits(text)


df['output'] = df['input'].apply(answer)
sample_df['output'] = sample_df['input'].apply(answer)

print(f"Sample answer: {sample_df['output'].sum()}")
print(f"Answer: {df['output'].sum()}")
