import math

Brick = list[list[int]]

bricks: list[Brick] = [[[int(y) for y in x.split(",")] for x in line.split("~")] for line in open("data/22").readlines()]

def brick_cells(brick: Brick):
    diff = [brick[1][i] - brick[0][i] for i in range(3)]
    diff_element = 0 if diff[0] != 0 else (1 if diff[1] != 0 else 2)

    delta = int(math.copysign(1, diff[diff_element]))

    cells = []

    for i in range(brick[0][diff_element], brick[1][diff_element] + delta, delta):
        out_cell = [x for x in brick[0]]
        out_cell[diff_element] = i

        cells.append(tuple(out_cell))

    return tuple(cells)

brick_cells_memo = [set(brick_cells(brick)) for brick in bricks]

while 1:
    moved_any = False
    for i, brick in enumerate(bricks):
        if brick[0][2] <= 1 or brick[1][2] <= 1:
            continue

        resting = False

        for cell in brick_cells(brick):
            cell_below = (cell[0], cell[1], cell[2] - 1)
            if any(cell_below in brick_cells_memo[j] for j in range(len(bricks)) if j != i):
                resting = True
                break

        if not resting:
            moved_any = True
            bricks[i][0][2] -= 1
            bricks[i][1][2] -= 1
            brick_cells_memo[i] = set(brick_cells(bricks[i]))

    if not moved_any:
        break

supported_by = [set() for _ in range(len(bricks))]

for i, brick in enumerate(bricks):
    if brick[0][2] <= 1 or brick[1][2] <= 1:
        continue

    for cell in brick_cells(brick):
        cell_below = (cell[0], cell[1], cell[2] - 1)
        for j, other_brick_cells in enumerate(brick_cells_memo):
            if i != j and cell_below in other_brick_cells:
                supported_by[i].add(j)

s = 0

print("Dropping all")

for k in range(len(bricks)):
    fallen = set()

    while 1:
        any_fell = False

        for i, brick in enumerate(bricks):
            if i not in fallen and brick[0][2] > 1 and brick[1][2] > 1  and supported_by[i] - fallen - set([k]) == set():
                fallen.add(i)
                any_fell = True

        if not any_fell:
            break

    s += len(fallen)

print(s)
