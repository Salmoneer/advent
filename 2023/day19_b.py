from functools import reduce
import re
import copy

raw_flows = open("data/19").read().split("\n\n")[0].strip().split("\n")

part_parts = ["x", "m", "a", "s"]

flows = {}

for flow in raw_flows:
    flow_regex = re.match(r"([a-z]+)\{(.*)\}", flow)

    if flow_regex is None:
        raise Exception("Regex is None")

    name = flow_regex.group(1)
    raw_rules = flow_regex.group(2)

    flows[name] = []
    
    for rule in raw_rules.split(","):
        rule_regex = re.match(r"([x|m|a|s])(\>|\<)(\d+):(.*)", rule)

        if rule_regex is None:
            flows[name].append(rule)
        else:
            flows[name].append([rule_regex.group(i) for i in range(1, 5)])

s = 0

def test(part):
    global s

    rule = part[4][part[5]]

    if type(rule) is str:
        letter_index = 0
        letter = part[letter_index]
        chunks = [[letter[0], letter[1], rule]]

    else:
        letter_index = "xmas".index(rule[0])
        letter = part[letter_index]

        if rule[1] == "<":
            if letter[0] + letter[1] - 1 < int(rule[2]):
                chunks = [[letter[0], letter[1], rule[3]]]
            elif letter[0] < int(rule[2]):
                chunks = [[letter[0], int(rule[2]) - letter[0], rule[3]],
                          [int(rule[2]), letter[0] + letter[1] - int(rule[2]), None]]
            else:
                chunks = [[letter[0], letter[1], None]]

        else:
            if letter[0] > int(rule[2]):
                chunks = [[letter[0], letter[1], rule[3]]]
            elif letter[0] + letter[1] > int(rule[2]):
                chunks = [[letter[0], int(rule[2]) - letter[0] + 1, None],
                          [int(rule[2]) + 1, letter[0] + letter[1] - int(rule[2]) - 1, rule[3]]]
            else:
                chunks = [[letter[0], letter[1], None]]

    return_parts = []

    for chunk in chunks:
        new_part = copy.deepcopy(part)

        new_letter = [chunk[0], chunk[1]]
        new_part[letter_index] = new_letter

        if chunk[2] == None:
            new_part[5] += 1
        elif chunk[2] == "A":
            s += reduce(lambda x, y: x * y, (letter[1] for letter in new_part[:4]))
            continue
        elif chunk[2] == "R":
            continue
        else:
            new_part[4] = flows[chunk[2]]
            new_part[5] = 0

        return_parts.append(new_part)

    return return_parts

current_parts = [[[1, 4000], [1, 4000], [1, 4000], [1, 4000], flows["in"], 0]]

while len(current_parts) > 0:
    next_parts = []

    for current_part in current_parts:
        next_parts += test(current_part)
    current_parts = next_parts

print(s)
