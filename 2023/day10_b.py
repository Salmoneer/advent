data = [list(x) for x in open("data/10").read().splitlines()]

connections = {
    "|": (( 0, -1), ( 0,  1)),
    "-": ((-1,  0), ( 1,  0)),
    "L": (( 0, -1), ( 1,  0)),
    "J": (( 0, -1), (-1,  0)),
    "7": (( 0,  1), (-1,  0)),
    "F": (( 0,  1), ( 1,  0))
}

start = None

for i, line in enumerate(data):
    if "S" in line:
        start = (line.index("S"), i)

if start == None:
    quit()

points = {}

def follow_pipe(x, y, delta_to):
    while data[y][x] != "S":
        x, y, delta_to = next_pipe(x, y, delta_to)

def next_pipe(x, y, delta_to):
    dx, dy = list(filter(lambda x: x[0] != -delta_to[0] or x[1] != -delta_to[1], connections[data[y][x]]))[0]

    points[(x, y)] = dy if dy else delta_to[1]

    return x + dx, y + dy, (dx, dy)

for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    test_char = data[start[1] + dy][start[0] + dx]
    if test_char in connections:
        if (-dx, -dy) in connections[test_char]:
            points[start] = dy
            follow_pipe(start[0] + dx, start[1] + dy, (dx, dy))
            break


for y in range(len(data)):
    for x in range(len(data[y])):
        if (x, y) in points:
            print(data[y][x], end = "")
        else:
            print(" ", end = "")
    print()

s = 0

for y, line in enumerate(data):
    counting = False
    print("Line", y)
    for x, c in enumerate(line):
        if (x, y) in points:
            if points[(x, y)] == -1:
                counting = True
                print("Set counting at", x)
            elif points[(x, y)] == 1:
                counting = False
                print("Unset counting at", x)

        elif counting:
            s += 1
            print("Added at", x)

print(s)
