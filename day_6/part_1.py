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
    

with open('../inputs/real/input_day_6.txt', 'r') as file:
    lines = file.readlines()
    encoded_lines = [BytesIO(line.encode('utf-8')) for line in lines]
    token_lines = [tokens(encoded_line) for encoded_line in encoded_lines]

with open('../inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = file.readlines()
    encoded_sample_lines = [BytesIO(line.encode('utf-8')) for line in sample_lines]
    token_sample_lines = [tokens(encoded_line) for encoded_line in encoded_sample_lines]


def get_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time


def better_distances(race):
    distances = 0
    for i in range(0, race[0], 1):
        distances += 1 if (get_distance(i, race[0])) > race[1] else 0
    return distances


def get_races(tokens_line):
    return [(tokens_line[0][index + 2][1], tokens_line[1][index + 2][1]) for index in range(len(tokens_line[0][2:]))]


def mul_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def process(tokens_list):
    races = get_races(tokens_list)
    beaten = [better_distances(race) for race in races]
    result = mul_list(beaten)

    return result


print("Sample output:", process(token_sample_lines))
print("Answer", process(token_lines))
