import re

data = open("data/2").read()

s = 0

maximums = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for i, line in enumerate(data.splitlines()):
    hands = [x.split("; ") for x in re.findall(r"Game \d+: (.*)", line)][0]

    possible = True

    for hand in hands:
        for pair in [x.split(" ") for x in hand.split(", ")]:
            if int(pair[0]) > maximums[pair[1]]:
                possible = False

    if possible:
        s += i + 1

print(s)
