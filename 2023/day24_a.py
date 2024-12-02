data = [[[int(z) for z in y.split(", ")[:2]] for y in x.split(" @ ")] for x in open("data/24").read().splitlines()]

minxy = 200000000000000
maxxy = 400000000000000

epsilon = 0.001

def intersect_in_box(p0, p1, v0, v1) -> bool:
    m0 = v0[1] / v0[0]
    m1 = v1[1] / v1[0]

    if abs(m0 - m1) < epsilon: return False

    b0 = p0[1] - m0 * p0[0]
    b1 = p1[1] - m1 * p1[0]

    x = (b1 - b0) / (m0 - m1)
    y = m0 * x + b0

    if not (minxy <= x <= maxxy and minxy <= y <= maxxy): return False

    if v0[0] > 0:
        if x < p0[0]: return False
    else:
        if x > p0[0]: return False

    if v0[1] > 0:
        if y < p0[1]: return False
    else:
        if y > p0[1]: return False

    if v1[0] > 0:
        if x < p1[0]: return False
    else:
        if x > p1[0]: return False

    if v1[1] > 0:
        if y < p1[1]: return False
    else:
        if y > p1[1]: return False

    return True

def prepare_paths(path0, path1):
    return (path0[0], path1[0], path0[1], path1[1])

s = 0

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if j == i: continue

        if intersect_in_box(*prepare_paths(data[i], data[j])):
            s += 1

print(s)
