sequences = [[int(x) for x in line.split(" ")] for line in open("data/9").read().splitlines()]

s = 0

for seq in sequences:
    diffs = [[b - a for a, b in zip(seq[:-1], seq[1:])]]

    while set(diffs[-1]) != set([0]):
        diffs.append([b - a for a, b in zip(diffs[-1][:-1], diffs[-1][1:])])

    diffs[-1].insert(0, 0)

    for i in range(len(diffs) - 2, -1, -1):
        diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])

    s += seq[0] - diffs[0][0]

print(s)
