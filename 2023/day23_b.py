data = [list("".join("." if c in "v^<>" else c for c in line)) for line in open("data/23").read().splitlines()]

width = len(data[0])
height = len(data)

start = (1, 0)
end = (width - 2, height - 1)

def get_neighbors(pos):
    out = []

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        x = pos[0] + dx
        y = pos[1] + dy

        if 0 <= x < width and 0 <= y < height and data[y][x] != "#":
            out.append((x, y))

    return out

junctions = [start, end]

stack = [start]
visited = set()

while stack:
    pos = stack.pop()

    neighbors = get_neighbors(pos)

    if len(neighbors) > 2:
        junctions.append(pos)

    for neighbor in neighbors:
        if neighbor in visited:
            continue

        stack.append(neighbor)
        visited.add(neighbor)

edges = {j: [] for j in junctions}

for j in junctions:
    stack = [(j, 0)]
    visited = set()

    while stack:
        pos, length = stack.pop()

        if pos in junctions and pos != j:
            edges[j].append((pos, length))
            continue

        for neighbor in get_neighbors(pos):
            if neighbor in visited:
                continue

            stack.append((neighbor, length + 1))
            visited.add(neighbor)

stack = [(start, [start], 0)]

longest_len = 0
longest_path = []

while stack:
    pos, path, current_len = stack.pop()

    if pos == end and current_len > longest_len:
        longest_len = current_len
        longest_path = path

    for neighbor, distance in edges[pos]:
        if neighbor in path:
            continue

        stack.append((neighbor, path + [neighbor], current_len + distance))

print(longest_len)
