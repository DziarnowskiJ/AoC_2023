with open('../inputs/real/input_day_3.txt', 'r') as file:
    real_lines = file.readlines()

with open('../inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = file.readlines()


def is_sign(c):
    return c not in [1,2,3,4,5,6,7,8,9,0,'.']


def is_valid(row_no, index, lines):
    lines_len = len(lines)
    line_len = len(lines[row_no])
    n = '.' if not (row_no > 0) else lines[row_no - 1][index]
    ne = '.' if not (row_no > 0 and index + 1 < line_len) else lines[row_no - 1][index + 1]
    e = '.' if not (index + 1 < line_len) else lines[row_no][index + 1]
    se = '.' if not (row_no + 1 < lines_len and index + 1 < line_len) else lines[row_no + 1][index + 1]
    s = '.' if not (row_no + 1 < lines_len) else lines[row_no + 1][index]
    sw = '.' if not (row_no + 1 < lines_len and index - 1 >= 0) else lines[row_no + 1][index - 1]
    w = '.' if not (index - 1 >= 0) else lines[row_no][index - 1]
    nw = '.' if not (row_no - 1 >= 0 and index - 1 >= 0) else lines[row_no - 1][index - 1]

    has_sign = not all([
        (n  == '\n' or n.isdigit()  or n == '.'),
        (ne == '\n' or ne.isdigit() or ne == '.'),
        (e  == '\n' or e.isdigit()  or e == '.'),
        (se == '\n' or se.isdigit() or se == '.'),
        (s  == '\n' or s.isdigit()  or s == '.'),
        (sw == '\n' or sw.isdigit() or sw == '.'),
        (w  == '\n' or w.isdigit()  or w == '.'),
        (nw == '\n' or nw.isdigit() or nw == '.'),
    ])

    return has_sign


def get_valids(lines):
    valids = []
    for row_no, line in enumerate(lines):
        last_number = ''
        is_last_valid = False
        for index, char in enumerate(line):
            if char.isdigit():
                last_number += char
                is_last_valid = True if is_valid(row_no, index, lines) else is_last_valid
            else:
                if is_last_valid:
                    valids.append(int(last_number))
                    last_number = ''
                    is_last_valid = False
                else:
                    last_number = ''
    return valids

sample_answer = sum(get_valids(sample_lines))
real_answer = sum(get_valids(real_lines))

print(f"Sample answer: {sample_answer}")
print(f"Answer: {real_answer}")