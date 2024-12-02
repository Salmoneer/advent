sequences = [[int(x) for x in line.split(" ")] for line in open("data/9").read().splitlines()]

s = 0

for seq in sequences:
    diffs = [[b - a for a, b in zip(seq[:-1], seq[1:])]]

    while diffs == [] or set(diffs[-1]) != set([0]):
        diffs.append([b - a for a, b in zip(diffs[-1][:-1], diffs[-1][1:])])

    diffs[-1].append(0)

    for i in range(len(diffs) - 2, -1, -1):
        diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])

    s += seq[-1] + diffs[0][-1]

print(s)
