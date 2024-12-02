data = [["?".join([x] * 5), [int(z) for z in y.split(",")] * 5] for x, y in [h.split(" ") for h in open("data/12").read().splitlines()]]

def print_table(dp, line, lengths):
    print("\\ - " + " ".join(line))
    for j, c in enumerate(["-"] + [str(x) for x in lengths]):
        print(c, " ".join(str(dp[i][j]) for i in range(len(line) + 1)))

s = 0

for line, lengths in data:
    n = len(line)
    m = len(lengths)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for j in range(m + 1):
        for i in range(n + 1):
            if dp[i][j] == 0:
                continue

            if i < n and line[i] != "#":
                dp[i + 1][j] += dp[i][j]

            if j < m and i + lengths[j] <= n and all(line[k] != "." for k in range(i, i + lengths[j])):
                if i + lengths[j] == n:
                    dp[i + lengths[j]][j + 1] += dp[i][j]
                elif line[i + lengths[j]] != "#":
                    dp[i + lengths[j] + 1][j + 1] += dp[i][j]

    s += dp[n][m]

print(s)
