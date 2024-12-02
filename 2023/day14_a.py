data = [list(x) for x in open("data/14").read().splitlines()]

out = [[] for _ in range(len(data))]

for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] == "O":
            out[y].append(".")
            for target_y in range(y, -2, -1):
                if target_y == -1 or out[target_y][x] != ".":
                    out[target_y + 1][x] = "O"
                    break
        else:
            out[y].append(data[y][x])


s = 0

for y in range(len(data)):
    s += out[y].count("O") * (len(data) - y)

print(s)
