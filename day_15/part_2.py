with open('../inputs/real/input_day_15.txt', 'r') as file:
    lines = file.readlines()
    strings = lines[0].split(',')

with open('../inputs/sample/sample_input_day_15.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_strings = sample_lines[0].split(',')


def spl(text):
    l, *r = text.split('=')
    if len(r) == 0:
        l, r = text.split('-')
        r = None
    else:
        r = r[-1]

    return l, r


def custom_hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val = val % 256

    return val


def get_value(box):
    resp = 0

    counter = 1
    for key in box.keys():
        location = 1
        for focal in box[key].values():
            resp += counter * location * int(focal)
            location += 1
        counter += 1

    return resp


def process(string_list):
    box = dict()
    for i in range(256):
        box[i] = dict()

    for string in string_list:
        label, focal = spl(string)
        hash_val = custom_hash(label)
        if focal is None:
            if label in box[hash_val].keys():
                box[hash_val].pop(label)
        else:
            box[hash_val][label] = focal

    resp = get_value(box)

    return resp


print("Sample output:", process(sample_strings))
print("Answer", process(strings))
