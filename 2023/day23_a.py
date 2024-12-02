data = [list(line) for line in open("data/23").read().splitlines()]
width = len(data[0])
height = len(data)

start = (1, 0)
target = (width - 2, height - 1)

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pointing_to = {
    "<": (-1,  0),
    ">": ( 1,  0),
    "^": ( 0, -1),
    "v": ( 0,  1),
}

def neighbors(pos):
    out = []

    c = data[pos[1]][pos[0]]

    for dx, dy in deltas:
        if c in pointing_to.keys() and (dx, dy) != pointing_to[c]: continue

        x = pos[0] + dx
        y = pos[1] + dy

        if not (0 <= x < width and 0 <= y < height): continue
        if data[y][x] == "#": continue

        out.append((x, y))

    return out

longest_len = 0
longest_path = []

stack = [(start, [start], 0)]
visited = {}

while stack:
    current, path, current_len = stack.pop()

    if current == target:
        if current_len > longest_len:
            longest_len = current_len
            longest_path = path
        continue

    for neighbor in neighbors(current):
        next_len = current_len + 1
        if neighbor in path: continue
        if neighbor not in visited or next_len > visited[neighbor]:
            visited[neighbor] = next_len
            stack.append((neighbor, path + [neighbor], next_len))

print(longest_len)
