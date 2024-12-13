def tokens(text):
    text = text.strip()
    text = text.replace(',', '')
    return text.split()


with open('../inputs/real/input_day_24.txt', 'r') as file:
    lines = file.readlines()
    token_dict = [{'token_line': tokens(encoded_line), 'x': None, 'y': None, 'm': None, 'b': None}
                  for encoded_line in lines]

with open('../inputs/sample/sample_input_day_24.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_token_dict = [{'token_line': tokens(encoded_line), 'x': None, 'y': None, 'm': None, 'b': None}
                         for encoded_line in sample_lines]


def calc(token):
    token['x'] = int(token['token_line'][0])
    token['y'] = int(token['token_line'][1])
    token['dx'] = int(token['token_line'][4])
    token['dy'] = int(token['token_line'][5])
    token['m'] = token['dy'] / token['dx']
    token['b'] = token['y'] - (token['m'] * token['x'])


def process(tokens_line, v_min, v_max):
    x_min = v_min
    x_max = v_max
    y_min = v_min
    y_max = v_max

    for token in tokens_line:
        calc(token)

    counter = 0
    for index, token in enumerate(tokens_line):
        for index_2, check_tok in enumerate(tokens_line[index:]):
            if check_tok['m'] == token['m']:
                continue
            x = (token['b'] - check_tok['b']) / (check_tok['m'] - token['m'])
            y = token['m'] * x + token['b']

            if (x_min <= x <= x_max and y_min <= y <= y_max and       # check for bounds
                    ((x <= token['x'] and token['dx'] < 0) or (x >= token['x'] and token['dx'] > 0)) and
                    ((y <= token['y'] and token['dy'] < 0) or (y >= token['y'] and token['dy'] > 0)) and
                    ((x <= check_tok['x'] and check_tok['dx'] < 0) or (x >= check_tok['x'] and check_tok['dx'] > 0)) and
                    ((y <= check_tok['y'] and check_tok['dy'] < 0) or (y >= check_tok['y'] and check_tok['dy'] > 0))):
                counter += 1

    return counter


print("Sample output:", process(sample_token_dict, 7, 27))
print("Answer:", process(token_dict, 200000000000000, 400000000000000))
