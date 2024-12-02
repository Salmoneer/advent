data = [list(line) for line in open("data/11").read().splitlines()]

EXPANSION = 1000000

def expand(data):
    out = []

    columns = []
    rows = []

    for y in range(len(data)):
        if "#" not in data[y]:
            rows.append(y)

    for x in range(len(data[0])):
        galaxy = False

        for y in range(len(data)):
            if data[y][x] == "#":
                galaxy = True

        if not galaxy:
            columns.append(x)

    for y in range(len(data)):
        temp = []

        for x in range(len(data[y])):
            if x in columns:
                for _ in range(EXPANSION - 1):
                    temp.append(".")
            temp += data[y][x]

        if y in rows:
            for _ in range(EXPANSION - 1):
                out.append(["."] * (len(data[y]) + len(columns)))

        out.append(temp)

    return out

data = expand(data)

galaxies = []

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == "#":
            galaxies.append((x, y))

s = 0

for start in range(len(galaxies) - 1):
    for stop in range(start, len(galaxies)):
        s += abs(galaxies[start][0] - galaxies[stop][0]) + abs(galaxies[start][1] - galaxies[stop][1])

print(s)
