data = [x.strip().split("\n") for x in open("data/13").read().split("\n\n")]

def test_horizontal(board, index):
    if not 0 < index < len(board):
        return False

    smudges = 0

    y1 = index - 1
    y2 = index

    for _ in range(min(y1 + 1, len(board) - y2)):
        for x in range(len(board[0])):
            if board[y1][x] != board[y2][x]:
                smudges += 1

        y1 -= 1
        y2 += 1

    return smudges == 1

def test_vertical(board, index):
    if not 0 < index < len(board[0]):
        return False

    smudges = 0

    x1 = index - 1
    x2 = index

    for _ in range(min(x1 + 1, len(board[0]) - x2)):
        for y in range(len(board)):
            if board[y][x1] != board[y][x2]:
                smudges += 1

        x1 -= 1
        x2 += 1

    return smudges == 1


s = 0

for board in data:
    for i in range(len(board)):
        if test_horizontal(board, i):
            s += 100 * i

    for i in range(len(board[0])):
        if test_vertical(board, i):
            s += i

print(s)
