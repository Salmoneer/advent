import networkx

data: list[tuple[str, list[str]]] = [tuple([x if i == 0 else x.split(" ") for i, x in enumerate(line.split(": "))]) for line in open("data/25").read().splitlines()]

nodes: list[str] = []

for line in data:
    if line[0] not in nodes:
        nodes.append(line[0])
    for v in line[1]:
        if v not in nodes:
            nodes.append(v)

edges = []

for u, vs in data:
    for v in vs:
        edge = (u, v)
        if edge not in edges:
            edges.append(edge)

G = networkx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

sw = networkx.stoer_wagner(G)

print(len(sw[1][0]) * len(sw[1][1]))
