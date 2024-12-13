with open('../inputs/real/input_day_15.txt', 'r') as file:
    lines = file.readlines()
    strings = lines[0].split(',')

with open('../inputs/sample/sample_input_day_15.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_strings = sample_lines[0].split(',')


def custom_hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val = val % 256

    return val

    
def process(string_list):
    resp = 0
    for string in string_list:
        resp += custom_hash(string)
    return resp


print("Sample output:", process(sample_strings))
print("Answer", process(strings))
