import itertools

data = [[x, [int(z) for z in y.split(",")]] for x, y in [h.split(" ") for h in open("data/12").read().splitlines()]]

def join_replacements(string, replacements):
    out = ""

    r = iter(replacements)
    
    for c in string:
        if c == "?":
            out += next(r)
        else:
            out += c

    return out

def test_replacements(string, replacements, expected):
    new = join_replacements(string, replacements)

    blocks = list(filter(None, new.split(".")))

    actual = [len(x) for x in blocks]

    if actual == expected:
        return True

    return False

s = 0

for line in data:
    for replacement in list(itertools.product([".", "#"], repeat=line[0].count("?"))):
        if test_replacements(line[0], replacement, line[1]):
            s += 1

print(s)
