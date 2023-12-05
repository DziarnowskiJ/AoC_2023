with open('../inputs/real/input_day_3.txt', 'r') as file:
    real_lines = file.readlines()

with open('../inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = file.readlines()


def get_digit_forward(start_index, end_index, line):
    curr_number = ''
    temp_index = start_index
    while temp_index < end_index and line[temp_index].isdigit():
        curr_number += line[temp_index]
        temp_index += 1
    return curr_number


def get_digit_backward(start_index, end_index, line):
    curr_number = ''
    temp_index = start_index
    while temp_index >= end_index and line[temp_index].isdigit():
        curr_number = line[temp_index] + curr_number
        temp_index -= 1
    return curr_number


def is_valid(row_no, index, lines):
    lines_len = len(lines)
    line_len = len(lines[row_no])

    n = '.' if not (row_no > 0) else lines[row_no - 1][index]
    ne = '.' if not (row_no > 0 and index + 1 < line_len) else lines[row_no - 1][index + 1]
    e = '.' if not (index + 1 < line_len) else  lines[row_no][index + 1]
    se = '.' if not (row_no + 1 < lines_len and index + 1 < line_len) else lines[row_no + 1][index + 1]
    s = '.' if not (row_no + 1 < lines_len) else  lines[row_no + 1][index]
    sw = '.' if not (row_no + 1 < lines_len and index - 1 >= 0) else lines[row_no + 1][index - 1]
    w = '.' if not (index - 1 >= 0) else lines[row_no][index - 1]
    nw = '.' if not (row_no - 1 >= 0 and index - 1 >= 0) else lines[row_no - 1][index - 1]

    numbers = []

    if n.isdigit():
        if row_no - 1 >= 0:
            # get digits to the right of n
            digit_right = get_digit_forward(index + 1, line_len, lines[row_no - 1])
            # get digits to the left of n
            digit_left = get_digit_backward(index - 1, 0, lines[row_no - 1])
            # get whole number
            full_digit = ((str(digit_left) if digit_left is not None else '') +
                          str(n) +
                          (str(digit_right) if digit_right is not None else ''))
            numbers.append(int(full_digit))
    else:
        if ne.isdigit():
            digit = get_digit_forward(index + 1, line_len, lines[row_no - 1])
            numbers.append(digit)
        if nw.isdigit():
            digit = get_digit_backward(index - 1, 0, lines[row_no - 1])
            numbers.append(digit)
    if s.isdigit():
        if row_no + 1 < lines_len:
            # get digits to the right of s
            digit_right = get_digit_forward(index + 1, line_len, lines[row_no + 1])
            # get digits to the left of s
            digit_left = get_digit_backward(index - 1, 0, lines[row_no + 1])
            # get whole number
            full_digit = ((str(digit_left) if digit_left is not None else '') +
                          str(s) +
                          (str(digit_right) if digit_right is not None else ''))
            numbers.append(int(full_digit))
    else:
        if se.isdigit():
            digit = get_digit_forward(index + 1, line_len, lines[row_no + 1])
            numbers.append(digit)
        if sw.isdigit():
            digit = get_digit_backward(index - 1, 0, lines[row_no + 1])
            numbers.append(digit)
    if e.isdigit():
        digit = get_digit_forward(index + 1, line_len, lines[row_no])
        numbers.append(digit)
    if w.isdigit():
        digit = get_digit_backward(index - 1, 0, lines[row_no])
        numbers.append(digit)

    ret = 0
    if len(numbers) == 2:
        ret = int(numbers[0]) * int(numbers[1])
    return ret


def get_valids(lines):
    valids = []
    for row_no, line in enumerate(lines):
        for index, char in enumerate(line):
            if char == '*':
                valids.append(is_valid(row_no, index, lines))
    return valids


sample_answer = sum(get_valids(sample_lines))
real_answer = sum(get_valids(real_lines))

print(f"Sample answer: {sample_answer}")
print(f"Answer: {real_answer}")

