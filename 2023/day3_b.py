import re

data = open("data/3").read()
data_map = [[x for x in y] for y in data.splitlines()]

s = 0

for i, line in enumerate(data.splitlines()):
    stars = re.finditer(r"\*", line)

    for star in stars:
        indices = []
        for x in range(star.span()[0] - 1, star.span()[1] + 1):
            for y in range(i - 1, i + 2):
                if 0 <= y < len(data_map) and 0 <= x < len(data_map[y]) and data_map[y][x] in "0123456789":
                    indices.append((x, y))

        starts = set()
        for index in indices:
            start = None
            for x in range(index[0], -1, -1):
                if data_map[index[1]][x] not in "0123456789":
                    start = (x + 1, index[1])
                    break

            if not start:
                start = (0, index[1])

            starts.add(start)

        numbers = []
        for start in starts:
            x = start[0]
            y = start[1]

            line_from_start = ''.join(data_map[y][x:])

            numbers.append(int(re.search(r"\d+", line_from_start).group()))

        if len(numbers) == 2:
            s += numbers[0] * numbers[1]

print(s)
