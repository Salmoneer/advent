import math

data = open("data/8").read().splitlines()

path = list(data[0])

nodes = {}

for line in data[2:]:
    nodes[line[:3]] = (line[7:10], line[12:15])


current_nodes = [n for n in nodes if n.endswith("A")]
cycle_lengths = []

i = 0
while 1:
    side = 0 if path[i % len(path)] == "L" else 1
    for j, node_name in enumerate(current_nodes):
        current_nodes[j] = nodes[node_name][side]

    i += 1

    for node in current_nodes:
        if node.endswith("Z"):
            current_nodes.remove(node)
            cycle_lengths.append(i)
    
    if len(current_nodes) == 0:
        break

print(math.lcm(*cycle_lengths))
