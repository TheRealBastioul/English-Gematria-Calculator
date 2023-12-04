import json
import re
# english gematria key dictionary
apple = {
    6: ('a'),
    12: ('b'),
    18: ('c'),
    24: ('d'),
    30: ('e'),
    36: ('f'),
    42: ('g'),
    48: ('h'),
    54: ('i'),
    60: ('j'),
    66: ('k'),
    72: ('l'),
    78: ('m'),
    84: ('n'),
    90: ('o'),
    96: ('p'),
    102: ('q'),
    108: ('r'),
    114: ('s'),
    120: ('t'),
    126: ('u'),
    132: ('v'),
    138: ('w'),
    144: ('x'),
    150: ('y'),
    156: ('z'),
    0: ('!','@', '$', '%', '^', '&', '*', '(', ')', '_', '+', '"', ':', '<', '>', '?', '|', '}', '~', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'")
}
# format dictionary into text string in input file
with open('original.txt', 'w') as gematriatext:
    json.dump(apple, gematriatext)
# convert input string into dictionary item
with open('original.txt', 'r') as gematriatext:
    string_input_to_dict = json.load(gematriatext)

#Gematria Calculator function
def gematriakey(name):
    # This inverses the original.txt dictionary
    def invert_dict(d):
        inverse = dict()
        for key in d:
            val = d[key]
            for i in val:
                if i not in inverse:
                    inverse[i] = [key]
                else:
                    inverse[i].append(key)
        return inverse

    invertlist = invert_dict(string_input_to_dict)
    # Format each item in inverted dictionary as text string
    with open('inverted.txt', 'w') as gematriainverted:
        json.dump(invertlist, gematriainverted)
    # this adds the gematric value of each letter to 'mynumber'
    mynumber = 0
    for i in name:
        addit = invertlist[i][0]
        mynumber += int(addit)
    return mynumber
#This function is to let you test the calculator multiple times in the console.
def calculateGematriac():
    name = str(input('Type in a name to calculate its gematriac value: '))
    print(f'The gematriac value of {name} is {gematriakey(name.lower())}')
    calculateGematriac()
#Initiate function call...
calculateGematriac()
