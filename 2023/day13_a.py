data = [x.strip().split("\n") for x in open("data/13").read().split("\n\n")]

def test_horizontal(board, index):
    if not 0 < index < len(board):
        return False

    valid = True

    y1 = index - 1
    y2 = index

    for _ in range(min(y1 + 1, len(board) - y2)):
        if board[y1] != board[y2]:
            valid = False

        y1 -= 1
        y2 += 1

    return valid

def test_vertical(board, index):
    if not 0 < index < len(board[0]):
        return False

    valid = True

    x1 = index - 1
    x2 = index

    for _ in range(min(x1 + 1, len(board[0]) - x2)):
        for y in range(len(board)):
            if board[y][x1] != board[y][x2]:
                valid = False

        x1 -= 1
        x2 += 1

    return valid


s = 0

for board in data:
    for i in range(len(board)):
        if test_horizontal(board, i):
            s += 100 * i

    for i in range(len(board[0])):
        if test_vertical(board, i):
            s += i

print(s)
