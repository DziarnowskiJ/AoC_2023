import tokenize
from io import BytesIO
import math


def tokens(text):
    tok = tokenize.tokenize(text.readline)
    name_tuples = [
        (tokenize.tok_name[token.type],
         (int(token.string) if token.type == tokenize.NUMBER else token.string))
        for token in tok
        if token.type not in {tokenize.ENCODING, tokenize.NEWLINE, tokenize.ENDMARKER, tokenize.NL}]
    text.seek(0)
    return name_tuples


with open('../inputs/real/input_day_6.txt', 'r') as file:
    lines = file.readlines()
    encoded_lines = [BytesIO(line.replace(' ', '').encode('utf-8')) for line in lines]
    token_lines = [tokens(encoded_line) for encoded_line in encoded_lines]

with open('../inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = file.readlines()
    encoded_sample_lines = [BytesIO(line.replace(' ', '').encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]


def get_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time


def max_lost_time(race):
    full_time = race[0]
    max_time = full_time
    min_time = 0
    time_to_check = math.floor(max_time / 2)

    while max_time - min_time > 1:
        if race[1] >= get_distance(time_to_check, full_time):
            min_time = time_to_check
            time_to_check = math.floor((max_time + min_time) / 2)
        else:
            max_time = time_to_check
            time_to_check = math.floor((max_time + min_time) / 2)

    return time_to_check


def get_races(tokens_line):
    # whitespaces are removed when reading the file
    # so the input contains only one race
    return tokens_line[0][2][1], tokens_line[1][2][1]


def process(tokens_list):
    race = get_races(tokens_list)
    print(race)
    max_lost = max_lost_time(race)
    wins = race[0] - 2 * max_lost - 1
    return wins


print("Sample output:", process(token_sample_lines))
print("Answer", process(token_lines))
