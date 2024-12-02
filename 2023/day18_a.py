data = [(line.split(" ")[0], int(line.split(" ")[1])) for line in open("data/18").read().splitlines()]

directions = {
    "L": (-1,  0),
    "R": ( 1,  0),
    "U": ( 0, -1),
    "D": ( 0,  1)
}

points = []

b = 0

current_pos = [0, 0]

for letter, distance in data:
    direction = directions[letter]

    b += distance

    current_pos[0] += direction[0] * distance
    current_pos[1] += direction[1] * distance

    points.append(tuple(current_pos))

s = points[-1][0] * points[0][1] - points[0][0] * points[-1][1]

for i in range(len(points) - 1):
    s += points[i][0] * points[i+1][1]
    s -= points[i+1][0] * points[i][1]

s = abs(s) // 2

print(s + b // 2 + 1)
