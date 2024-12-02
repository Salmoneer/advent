data = open("data/15").read().replace("\n", "").split(",")

hashmap = [{} for _ in range(256)]

def HASH(string):
    current = 0

    for c in string:
        current += ord(c)
        current *= 17
        current %= 256

    return current


def clear(key):
    for box in hashmap:
        if key in box:
            box.pop(key)

def assign(key, value):
    box = HASH(key)
    hashmap[box][key] = value


for operation in data:
    if operation.endswith("-"):
        clear(operation[:-1])
    else:
        assign(operation[:-2], int(operation[-1]))


s = 0

for i, box in enumerate(hashmap):
    for slot, key in enumerate(box):
        s += (i + 1) * (slot + 1) * box[key]

print(s)
