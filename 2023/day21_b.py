from collections import deque

data = [list(x) for x in open("data/21").read().splitlines()]

start_pos = None

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start_pos = (x, y)

if start_pos == None:
    raise Exception("Couldn'd find start_pos!")

queue: deque[tuple[int, tuple[int, int]]] = deque([(0, start_pos)])

visited: dict[tuple[int, int], int] = {}

while queue:
    item = queue.popleft()

    current_distance = item[0]
    current_pos = item[1]

    if current_pos in visited:
        continue

    visited[current_pos] = current_distance

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_x = current_pos[0] + dx
        new_y = current_pos[1] + dy

        if 0 <= new_x < len(data[0]) and 0 <= new_y < len(data) and data[new_y][new_x] != "#" and (new_x, new_y) not in visited:
            queue.append((current_distance + 1, (new_x, new_y)))

even_inside = odd_inside = even_outside = odd_outside = 0

grid = [[x for x in y] for y in data]

for x, y in visited:
    if visited[(x, y)] % 2 == 0:
        if visited[(x, y)] <= 65:
            even_inside += 1
        else:
            even_outside += 1
        grid[y][x] = "E"
    else:
        if visited[(x, y)] <= 65:
            odd_inside += 1
        else:
            odd_outside += 1
        grid[y][x] = "O"

for line in grid:print("".join(line))

print(f"insde: odd: {odd_inside} even: {even_inside}")
print(f"outside: odd: {odd_outside} even: {even_outside}")

n = 202300

odd_square_count = (n + 1) ** 2
even_square_count = n ** 2

s = (odd_inside + odd_outside) * odd_square_count + (even_inside + even_outside) * even_square_count \
  - (n + 1) * odd_outside                         + n * even_outside

print(s)
