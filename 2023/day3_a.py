import re

data = open("data/3").read()

data_map = [[x for x in y] for y in data.splitlines()]

s = 0

for i, line in enumerate(data.splitlines()):
    numbers = re.finditer(r"\d+", line)

    for number in numbers:
        valid_number = False

        for x in range(number.span()[0] - 1, number.span()[1] + 1):
            for y in range(i - 1, i + 2):
                if 0 <= y < len(data_map) and 0 <= x < len(data_map[y]) and data_map[y][x] not in ".0123456789":
                    valid_number = True

        if valid_number:
            s += int(number.group())

print(s)
