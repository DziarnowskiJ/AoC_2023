import pandas as pd
import re

with open('../inputs/real/input_day_1.txt', 'r') as file:
    lines = file.readlines()
    df = pd.DataFrame({'input': lines, 'output': None})

with open('../inputs/sample/sample_input_day_1.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_df = pd.DataFrame({'input': sample_lines, 'output': None})

def to_digit(text):
    text = text.replace('zero', 'z0o')
    text = text.replace('one', 'o1e')
    text = text.replace('two', 't2o')
    text = text.replace('three', 't3e')
    text = text.replace('four', 'f4r')
    text = text.replace('five', 'f5e')
    text = text.replace('six', 's6x')
    text = text.replace('seven', 's7n')
    text = text.replace('eight', 'e8t')
    text = text.replace('nine', 'n9e')
    return text


def get_digits(text):
    pattern = re.compile(r'\d')
    digits = pattern.findall(text)

    if len(digits) > 0:
        return int(digits[0] + '' + digits[-1])
    else:
        return 0


def answer(text):
    return get_digits(to_digit(text))


df['output'] = df['input'].apply(answer)
sample_df['output'] = sample_df['input'].apply(answer)

print(f"Sample answer: {sample_df['output'].sum()}")
print(f"Answer: {df['output'].sum()}")
