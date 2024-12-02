import re

data = open("data/2").read()

s = 0

colors = {
    "green": 0,
    "red": 1,
    "blue": 2
}

for i, line in enumerate(data.splitlines()):
    hands = [x.split("; ") for x in re.findall(r"Game \d+: (.*)", line)][0]

    maxes = [0, 0, 0]

    for hand in hands:
        for pair in [x.split(" ") for x in hand.split(", ")]:
            maxes[colors[pair[1]]] = max(maxes[colors[pair[1]]], int(pair[0]))

    s += maxes[0] * maxes[1] * maxes[2]

print(s)
