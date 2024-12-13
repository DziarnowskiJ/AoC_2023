def tokens(line):
    left, right_s = line.split(" ")
    right = [int(x) for x in right_s.split(",")]

    return left, right


with open('../inputs/real/input_day_12.txt', 'r') as file:
    lines = file.readlines()
    token_lines = [tokens(line) for line in lines]

with open('../inputs/sample/sample_input_day_12.txt', 'r') as file:
    sample_lines = file.readlines()
    token_sample_lines = [tokens(line) for line in sample_lines]

def search(spring: str, numbers: [int]):
    if len(spring) == 0:
        if len(numbers) == 0:
            return 1
        else:
            return 0
    if spring.startswith('.'):
        return search(spring.strip('.'), numbers)
    if spring.startswith('?'):
        return (search(spring.replace('?', '#', 1), numbers)
                + search(spring.replace('?', '.', 1), numbers))
    if spring.startswith('#'):
        if len(numbers) == 0:
            return 0
        if len(spring) < numbers[0]:
            return 0
        if any(c == "." for c in spring[0:numbers[0]]):
            return 0
        if len(numbers) > 1:
            if len(spring) < numbers[0] + 1 or spring[numbers[0]] == "#":
                return 0
            return search(spring[numbers[0] + 1:], numbers[1:])
        else:
            return search(spring[numbers[0]:], numbers[1:])

    raise Exception('Branch fail')


def process(tokens_line):
    res = []
    for line in tokens_line:
        res.append(search(line[0], line[1]))
    return sum(res)


print("Sample output:", process(token_sample_lines))
print("Answer", process(token_lines))
