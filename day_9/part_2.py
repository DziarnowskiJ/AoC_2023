def tokens(text):
    return [int(x) for x in text.split(' ') if x != '']


with open('../inputs/real/input_day_9.txt', 'r') as file:
    lines = file.readlines()
    token_lines = [tokens(encoded_line) for encoded_line in lines]

with open('../inputs/sample/sample_input_day_9.txt', 'r') as file:
    sample_lines = file.readlines()
    token_sample_lines = [tokens(encoded_line) for encoded_line in sample_lines]


def get_differences(nums):
    return [nums[i+1] - nums[i] for i in range(len(nums) - 1)]


def predict_prev(data):
    line_prev = data[-1]
    line_prev.append(0)
    for line in reversed(data[:-1]):
        line.insert(0, line[0] - line_prev[0])
        line_prev = line
    return data


def build_hist(tokens_line):
    line = [x for x in tokens_line]
    hist = [line]
    while not all([x == 0 for x in line]):
        line = get_differences(line)
        hist.append(line)
    return hist


def get_firsts_sum(data):
    return sum([datum[0] for datum in data])


def process(tokens_line):
    final_pred = []
    for tok_line in tokens_line:
        hist = build_hist(tok_line)
        hist_pred = predict_prev(hist)
        final_pred.append(hist_pred[0])
    sum_firsts = get_firsts_sum(final_pred)
    return sum_firsts


print("Sample output:", process(token_sample_lines))
print("Answer", process(token_lines))