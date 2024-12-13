import re
import numpy as np
import mpmath

with open('../inputs/real/input_day_24.txt', 'r') as file:
    input_lines = file.readlines()

with open('../inputs/sample/sample_input_day_24.txt', 'r') as file:
    sample_lines = file.readlines()


def parse_line(line):
    vals = [int(v) for v in re.findall(r"-?\d+", line)]
    return {
        'x': vals[0],
        'y': vals[1],
        'z': vals[2],
        'dx': vals[3],
        'dy': vals[4],
        'dz': vals[5],
    }


def process(lines):
    hailstones = [parse_line(line) for line in lines]

    hail_0 = hailstones.pop(0)

    arr = []
    const = []
    for hail in hailstones[:3]:
        arr.append([hail['dy'] - hail_0['dy'], hail_0['dx'] - hail['dx'], 0, hail_0['y'] - hail['y'], hail['x'] - hail_0['x'], 0])
        arr.append([hail['dz'] - hail_0['dz'], 0, hail_0['dx'] - hail['dx'], hail_0['z'] - hail['z'], 0, hail['x'] - hail_0['x']])
        const.append(hail['x'] * hail['dy'] - hail['y'] * hail['dx'] + hail_0['y'] * hail_0['dx'] - hail_0['x'] * hail_0['dy'])
        const.append(hail['x'] * hail['dz'] - hail['z'] * hail['dx'] + hail_0['z'] * hail_0['dx'] - hail_0['x'] * hail_0['dz'])

    arr_np = np.array(arr)
    arr_np = [[mpmath.mpf(float(x)) for x in row] for row in arr_np]
    const_np = np.array(const)
    const_np = [mpmath.mpf(float(x)) for x in const_np]

    X, Y, Z, dx, dy, dz = mpmath.lu_solve(arr_np, const_np)
    return int(X + Y + Z)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
