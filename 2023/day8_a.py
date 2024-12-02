data = open("data/8").read().splitlines()

path = list(data[0])

nodes = {}

for line in data[2:]:
    nodes[line[:3]] = (line[7:10], line[12:15])


current_node = "AAA"

i = 0
while 1:
    side = 0 if path[i % len(path)] == "L" else 1
    current_node = nodes[current_node][side]

    i += 1

    if current_node == "ZZZ":
        break

print(i)
