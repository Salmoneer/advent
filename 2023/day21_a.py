data = [list(x) for x in open("data/21").read().splitlines()]

MAX_STEPS = 64

start_pos = None

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start_pos = (x, y)

if start_pos == None:
    raise Exception("Couldn'd find start_pos!")

queue: list[tuple[int, tuple[int, int]]] = [(0, start_pos)]

destinations = set()

closed = set()

while queue:
    item = queue.pop(0)

    current_distance = item[0]
    current_pos = item[1]

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_x = current_pos[0] + dx
        new_y = current_pos[1] + dy

        if 0 <= new_x < len(data[0]) and 0 <= new_y < len(data) and data[new_y][new_x] != "#":
            new_distance = current_distance + 1
            new_pos = (new_x, new_y)

            if (new_distance, new_pos) in closed:
                continue
            else:
                closed.add((new_distance, new_pos))

            if new_distance < MAX_STEPS:
                queue.append((new_distance, new_pos))
            elif new_distance == MAX_STEPS:
                destinations.add(new_pos)
            else:
                raise Exception("Distance exceeded max steps!")

print(len(destinations))
