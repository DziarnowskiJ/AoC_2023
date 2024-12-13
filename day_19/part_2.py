import re

with open('../inputs/real/input_day_19.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_19.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


class Part:
    minX = 0
    maxX = 4000
    minM = 0
    maxM = 4000
    minA = 0
    maxA = 4000
    minS = 0
    maxS = 4000

    nextRule = None

    @staticmethod
    def init_rule(nextRule):
        new_part = Part()
        new_part.nextRule = nextRule
        return new_part

    @staticmethod
    def init_part(part):
        new_part = Part()
        new_part.minX = part.minX
        new_part.maxX = part.maxX
        new_part.minM = part.minM
        new_part.maxM = part.maxM
        new_part.minA = part.minA
        new_part.maxA = part.maxA
        new_part.minS = part.minS
        new_part.maxS = part.maxS

        return new_part

    def addGreater(self, v, number):
        if v == "x":
            self.minX = max([self.minX, number])
        elif v == "m":
            self.minM = max([self.minM, number])
        elif v == "a":
            self.minA = max([self.minA, number])
        elif v == "s":
            self.minS = max([self.minS, number])

    def addSmaller(self, v, number):
        if v == "x":
            self.maxX = min([self.maxX, number])
        elif v == "m":
            self.maxM = min([self.maxM, number])
        elif v == "a":
            self.maxA = min([self.maxA, number])
        elif v == "s":
            self.maxS = min([self.maxS, number])

    def getCombinations(self):
        comb = self.maxX - self.minX
        comb = comb * (self.maxM - self.minM)
        comb = comb * (self.maxA - self.minA)
        comb = comb * (self.maxS - self.minS)
        return comb


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
        newList = list()

        if self.endArgument is None:
            if self.operation == self.GREATER:
                trueFP = Part.init_part(part)
                trueFP.addGreater(self.variable, self.number)

                falseFP = Part.init_part(part)
                falseFP.addSmaller(self.variable, self.number)

                newList += self.trueRule.evaluate(trueFP)
                newList += self.falseRule.evaluate(falseFP)
            else:
                trueFP = Part.init_part(part)
                trueFP.addSmaller(self.variable, self.number - 1)

                falseFP = Part.init_part(part)
                falseFP.addGreater(self.variable, self.number - 1)

                newList += self.trueRule.evaluate(trueFP)
                newList += self.falseRule.evaluate(falseFP)
        elif self.endArgument == "A":
            newList.append(part)
        elif self.endArgument == "R":
            pass
        else:
            part.nextRule = self.endArgument
            newList.append(part)

        return newList


def get_rules(lines):
    rules = dict()
    for line in lines:
        if len(line) == 0:
            break

        name, rest, *_ = line[:-1].split('{')
        rules[name] = Rule(rest)

    return rules


def process(lines):
    rules = get_rules(lines)

    part1 = Part.init_rule("in")
    partList = list()
    partList.append(part1)
    is_working = True
    while is_working:
        is_working = False
        newList = list()
        for part in partList:
            ruleName = part.nextRule
            if ruleName is not None:
                newList += rules[ruleName].evaluate(part)
                is_working = True
            else:
                newList.append(part)
        partList = newList

    return sum([part.getCombinations() for part in partList])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
