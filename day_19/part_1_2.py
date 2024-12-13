import re

with open('../inputs/real/input_day_19.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_19.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


class Part:
    def __init__(self, line):
        pattern = r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}"
        match = re.search(pattern, line)
        if match:
            self.x = int(match.group(1))
            self.m = int(match.group(2))
            self.a = int(match.group(3))
            self.s = int(match.group(4))

    def getVar(self, var):
        if var == 'x':
            return self.x
        elif var == 'm':
            return self.m
        elif var == 'a':
            return self.a
        elif var == 's':
            return self.s
        else:
            raise ValueError(f'invalid variable name {var}')

    def getValue(self):
        return self.x + self.m + self.a + self.s

    def __str__(self):
        return f"{{x={self.x},m={self.m},a={self.a},s={self.a}}}"

class Rule:
    GREATER = '>'
    SMALLER = '<'
    operation = -1

    variable = None
    number = None
    trueRule = None
    falseRule = None
    endArgument = None

    def __init__(self, line):
        argumentSplit = line.find(':')
        if argumentSplit == -1:
            self.endArgument = line
            return

        self.variable = line[0]
        if line[1] == ">":
            self.operation = self.GREATER
        else:
            self.operation = self.SMALLER

        self.number = int(line[2:argumentSplit])

        ruleSplit = line.find(",")

        self.trueRule = Rule(line[argumentSplit + 1:ruleSplit])
        self.falseRule = Rule(line[ruleSplit + 1:])

    def __str__(self):
        return 'Rule ' + self.variable + ' ' + str(self.operation) + ' ' + str(self.number)

    def evaluate(self, part):
        if self.endArgument is not None:
            return self.endArgument

        if self.operation == self.GREATER:
            if part.getVar(self.variable) > self.number:
                return self.trueRule.evaluate(part)
            else:
                return self.falseRule.evaluate(part)
        else:
            if part.getVar(self.variable) < self.number:
                return self.trueRule.evaluate(part)
            else:
                return self.falseRule.evaluate(part)


def get_rules_parts(lines):
    is_rules = True
    rules = dict()
    parts = list()
    for line in lines:
        if len(line) == 0:
            is_rules = False
            continue

        if is_rules:
            name, rest, *_ = line[:-1].split('{')
            rules[name] = Rule(rest)
        else:
            parts.append(Part(line))
    return rules, parts

def process(lines):
    rules, parts = get_rules_parts(lines)
    counter = 0
    for part in parts:
        ruleName = 'in'
        while True:
            ruleName = rules[ruleName].evaluate(part)
            if ruleName == 'R':
                break
            elif ruleName == 'A':
                counter += part.getValue()
                break

    return counter


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
