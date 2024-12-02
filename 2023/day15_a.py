data = open("data/15").read().replace("\n", "").split(",")

s = 0

for string in data:
    current = 0

    for c in string:
        current += ord(c)
        current *= 17
        current %= 256

    s += current

print(s)
