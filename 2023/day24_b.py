# https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kxqjg33/

data = [[[int(z) for z in y.split(", ")] for y in x.split(" @ ")] for x in open("data/24").read().splitlines()]

def cross_product(v0, v1):
    return [
        v0[1] * v1[2] - v0[2] * v1[1],
        v0[2] * v1[0] - v0[0] * v1[2],
        v0[0] * v1[1] - v0[1] * v1[0],
    ]

def dot_product(v0, v1):
    return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]

def prepare_paths(path0, path1):
    return (path0[0], path1[0], path0[1], path1[1])

def vec_add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def vec_sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def scalar_mul(a, b):
    return [a * b[0], a * b[1], a * b[2]]

def scalar_div(a, b):
    return [a[0] / b, a[1] / b, a[2] / b]

p1 = vec_sub(data[1][0], data[0][0])
v1 = vec_sub(data[1][1], data[0][1])
p2 = vec_sub(data[2][0], data[0][0])
v2 = vec_sub(data[2][1], data[0][1])

t1 = -(dot_product(cross_product(p1, p2), v2) / dot_product(cross_product(v1, p2), v2))
t2 = -(dot_product(cross_product(p1, p2), v1) / dot_product(cross_product(p1, v2), v1))

c1 = vec_add(data[1][0], scalar_mul(t1, data[1][1]))
c2 = vec_add(data[2][0], scalar_mul(t2, data[2][1]))

v = scalar_div(vec_sub(c2, c1), (t2 - t1))
p = vec_sub(c1, scalar_mul(t1, v))

print(p)
print(int(sum(p)))
