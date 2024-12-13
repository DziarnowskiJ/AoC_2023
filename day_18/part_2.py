from utils.geometry import *


def tokens(text_lines):
    return [text_line.strip().split(' ') for text_line in text_lines]


with open('../inputs/real/input_day_18.txt', 'r') as file:
    lines = file.readlines()
    token_lines = tokens(lines)

with open('../inputs/sample/sample_input_day_18.txt', 'r') as file:
    sample_lines = file.readlines()
    token_sample_lines = tokens(sample_lines)


def decrypt_command(tokens_lien):
    commands = []
    for command in tokens_lien:
        direc = command[2][-2]
        val = int(command[2][2:-2], 16)

        if direc == '0':
            commands.append(('R', val))
        elif direc == '1':
            commands.append(('D', val))
        elif direc == '2':
            commands.append(('L', val))
        elif direc == '3':
            commands.append(('U', val))

    return commands


def calc_area(verts):
    # shoelace algorithm
    vert_count = len(verts)
    temp = 0
    for i in range(vert_count - 1):
        temp += verts[i].x * verts[i + 1].y
        temp -= verts[i].y * verts[i + 1].x

    # Add xn.y1
    temp += verts[vert_count - 1].x * verts[0].y
    # Add x1.yn
    temp -= verts[0].x * verts[vert_count - 1].y

    area = abs(temp) / 2

    return area


def inside_area(perimeter, area):
    # pick's formula
    # A = I + B/2 – 1
    # --> I = A + 1 - B/2
    return area + 1 - perimeter / 2
    # return area - perimeter // 2 + 1


def process(tokens_line):
    current = origin
    dig_vert = [origin]

    commands = decrypt_command(tokens_line)

    perimeter = 0
    for command in commands:
        if command[0] == 'R':
            current += one_step(Direction.E).mul(command[1])
        elif command[0] == 'L':
            current += one_step(Direction.W).mul(command[1])
        elif command[0] == 'U':
            current += one_step(Direction.N).mul(command[1])
        elif command[0] == 'D':
            current += one_step(Direction.S).mul(command[1])

        perimeter += command[1]
        dig_vert.append(current)

    area = calc_area(dig_vert)
    inside = inside_area(perimeter, area)

    return inside + perimeter


print("Sample output:", process(token_sample_lines))
print("Answer:", process(token_lines))
