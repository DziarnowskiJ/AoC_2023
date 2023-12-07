import pandas as pd

with open('../inputs/real/input_day_7.txt', 'r') as file:
    lines = file.readlines()
    df = pd.DataFrame({'input': lines, 'hand': None, 'output': None})

with open('../inputs/sample/sample_input_day_7.txt', 'r') as file:
    sample_lines = file.readlines()
    sample_df = pd.DataFrame({'input': sample_lines, 'hand': None, 'output': None})

card_val = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


class Hand:
    def __init__(self, line):
        self.cards, self.bid = line.split(' ')
        self.bid = int(self.bid)
        self.c_dict = self.get_dict()
        self.type = self.get_type()

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        else:
            for i in range(len(self.cards)):
                if self.cards[i] != other.cards[i]:
                    return card_val[self.cards[i]] < card_val[other.cards[i]]
            return False

    def get_dict(self):
        c_dict = dict()
        for card in self.cards:
            if card in c_dict.keys():
                c_dict[card] += 1
            else:
                c_dict[card] = 1
        return c_dict

    def get_type(self):
        # Five of a kind
        if max(self.c_dict.values()) == 5:
            return 6
        # Four of a kind
        elif max(self.c_dict.values()) == 4:
            return 5
        # Full house
        elif 2 in self.c_dict.values() and 3 in self.c_dict.values():
            return 4
        # Three of a kind
        elif max(self.c_dict.values()) == 3:
            return 3
        # Two pair
        elif len([x for x in self.c_dict.values() if x == 2]) == 2:
            return 2
        # One pair
        elif max(self.c_dict.values()) == 2:
            return 1
        # High card
        else:
            return 0


def get_rank(row):
    return (row.name + 1) * row['hand'].bid


def process(dataframe):
    dataframe['hand'] = dataframe['input'].apply(Hand)
    dataframe.sort_values(by=['hand'], inplace=True)
    dataframe.reset_index(drop=True, inplace=True)
    dataframe['output'] = dataframe.apply(get_rank, axis=1)


process(sample_df)
process(df)
print("Sample output:", sample_df['output'].sum())
print("Answer", df['output'].sum())
