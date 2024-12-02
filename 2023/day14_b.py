data = [list(x) for x in open("data/14").read().splitlines()]

def tilt_platform_y(board, delta_y):
    out = [["" for _ in range(len(data[i]))] for i in range(len(data))]

    for x in range(len(board[0])):
        for y in range(0 if delta_y == -1 else len(board) - 1, len(board) if delta_y == -1 else -1, -delta_y):
            if board[y][x] == "O":
                out[y][x] = "."

                for target_y in range(y, -2 if delta_y == -1 else len(board) + 1, delta_y):
                    if target_y in [-1, len(board)] or out[target_y][x] != ".":
                        out[target_y - delta_y][x] = "O"
                        break
            else:
                out[y][x] = board[y][x]

    return out

def tilt_platform_x(board, delta_x):
    out = [["" for _ in range(len(data[i]))] for i in range(len(data))]

    for y in range(len(board)):
        for x in range(0 if delta_x == -1 else len(board[0]) - 1, len(board) if delta_x == -1 else -1, -delta_x):
            if board[y][x] == "O":
                out[y][x] = "."

                for target_x in range(x, -2 if delta_x == -1 else len(board[0]) + 1, delta_x):
                    if target_x in [-1, len(board[0])] or out[y][target_x] != ".":
                        out[y][target_x - delta_x] = "O"
                        break
            else:
                out[y][x] = board[y][x]

    return out

history = []

for i in range(1_000_000_000):
    history.append([[x for x in y] for y in data])

    if data in history[:-1]:
        index = history.index(data)
        data = history[index + (1_000_000_000 - i) % (i - index)]
        break
    else:
        data = tilt_platform_y(data, -1)
        data = tilt_platform_x(data, -1)
        data = tilt_platform_y(data, 1)
        data = tilt_platform_x(data, 1)

for line in data:
    print("".join(line))

s = 0

for y in range(len(data)):
    s += data[y].count("O") * (len(data) - y)

print(s)
