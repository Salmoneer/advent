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

distance_map = {}

def follow_pipe(x, y, delta_to):
    dist = 1
    while data[y][x] != "S":
        x, y, delta_to, dist = next_pipe(x, y, delta_to, dist)

def next_pipe(x, y, delta_to, dist):
    if (x, y) in distance_map:
        distance_map[(x, y)] = min(dist, distance_map[(x, y)])
    else:
        distance_map[(x, y)] = dist

    dx, dy = list(filter(lambda x: x[0] != -delta_to[0] or x[1] != -delta_to[1], connections[data[y][x]]))[0]

    return x + dx, y + dy, (dx, dy), dist + 1

for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    test_char = data[start[1] + dy][start[0] + dx]
    if test_char in connections:
        if (-dx, -dy) in connections[test_char]:
            follow_pipe(start[0] + dx, start[1] + dy, (dx, dy))

print(distance_map[max(distance_map, key = lambda x: distance_map[x])])
